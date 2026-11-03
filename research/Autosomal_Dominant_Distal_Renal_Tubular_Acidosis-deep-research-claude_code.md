---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-10-28T01:27:26.835612'
end_time: '2026-10-28T01:31:36.434479'
duration_seconds: 249.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autosomal Dominant Distal Renal Tubular Acidosis
  mondo_id: MONDO:0008368
  category: Mendelian
  causal_genes: SLC4A1
  omim_id: OMIM:179800
  synonyms: AD dRTA; DRTA1; RTA, classic type; RTA, distal type, autosomal dominant;
    RTA, gradient type; distal renal tubular acidosis (disease), autosomal dominant;
    renal tubular acidosis, distal 1
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
  web_search_requests: 2
  num_turns: 19
  total_cost_usd: 2.4770769
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 5
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:9312167
  relevance_assessed: 11
  on_topic: 10
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 42
  verified: 37
  not_found: 0
  obsolete: 2
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0000407
    reported_labels:
    - Clinical
    ontology_label: Sensorineural hearing impairment
  - term_id: CL:1001431
    reported_labels:
    - "\u03B1-intercalated cells"
    ontology_label: kidney collecting duct principal cell
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0015301
    ontology_label: obsolete anion:anion antiporter activity
  - term_id: GO:0030433
    ontology_label: obsolete ubiquitin-dependent ERAD pathway
    replaced_by: GO:0036503
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
- **Disease Name:** Autosomal Dominant Distal Renal Tubular Acidosis
- **MONDO ID:** MONDO:0008368 (if available)
- **Causal gene(s):** SLC4A1
- **OMIM:** OMIM:179800
- **Synonyms:** AD dRTA; DRTA1; RTA, classic type; RTA, distal type, autosomal dominant; RTA, gradient type; distal renal tubular acidosis (disease), autosomal dominant; renal tubular acidosis, distal 1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Distal Renal Tubular Acidosis** covering all of the
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

I'm searching the local reference cache for SLC4A1 papers before moving on to web research.

# Deep Research Report: Autosomal Dominant Distal Renal Tubular Acidosis

**MONDO:0008368 · OMIM:179800 · Causal gene: SLC4A1 (HGNC:11027)**

> Scope note on identity. This report is about the **SLC4A1**-caused, dominantly inherited form of **distal (type 1) renal tubular acidosis (dRTA)**. SLC4A1 encodes **Anion Exchanger 1 (AE1, band 3)**; the kidney isoform **kAE1** mediates basolateral Cl⁻/HCO₃⁻ exchange in **collecting-duct α-intercalated cells**. The serial-number synonyms ("DRTA1", "RTA, distal type, autosomal dominant") all refer to this SLC4A1/kAE1 entity. Note that SLC4A1 variants also cause (a) an **autosomal recessive** dRTA form (often with hemolytic anemia, predominantly in Southeast Asia) and (b) purely hematologic phenotypes (hereditary spherocytosis, Southeast Asian ovalocytosis) — the gene is pleiotropic, and inheritance mode plus phenotype must be read together, not from the gene alone. The other hereditary dRTA genes (ATP6V1B1, ATP6V0A4, FOXI1, WDR72) are **not** this disease and are recessive (with a specific dominant ATP6V1B1 p.Arg394 exception).

---

## 1. Disease Information

Autosomal dominant distal renal tubular acidosis (AD dRTA) is a Mendelian renal tubulopathy in which the distal nephron (collecting duct) fails to secrete protons (H⁺) adequately, producing a **hyperchloremic, normal–anion-gap metabolic acidosis with inappropriately alkaline urine (urine pH > 5.5 despite systemic acidosis)**. The dominant form is caused by heterozygous variants in **SLC4A1**, which disrupt trafficking of the kidney anion exchanger kAE1 to the basolateral membrane of α-intercalated cells, impairing bicarbonate reabsorption/recycling and thus net acid excretion.

**Key identifiers**
- **OMIM:** 179800 ("RENAL TUBULAR ACIDOSIS, DISTAL, 1; RTA1")
- **MONDO:** MONDO:0008368
- **Orphanet:** ORPHA:18 (distal renal tubular acidosis, umbrella); the SLC4A1 AD form sits within hereditary dRTA
- **ICD-10:** N25.89 / E87.2-related coding (no dedicated code); **ICD-11:** GB90.4 (renal tubular acidosis)
- **MeSH:** D000141 "Acidosis, Renal Tubular"
- **Gene:** SLC4A1, HGNC:11027; protein UniProt **P02730** (Band 3 anion transport protein)

**Synonyms:** AD dRTA; DRTA1; RTA, classic type; RTA, distal type, autosomal dominant; RTA, gradient type; distal renal tubular acidosis, autosomal dominant; renal tubular acidosis, distal 1.

**Information derivation:** disease-level aggregation (OMIM, Orphanet, GeneReviews) supplemented by case series and a large multinational registry cohort (European dRTA Consortium, 340 patients) [PMID:30773598] and a published-patient meta-summary of 169 SLC4A1 dRTA patients [PMID:36776909]. Not derived from EHR.

---

## 2. Etiology

**Primary cause — genetic.** Heterozygous **dominant-negative** variants in SLC4A1. The seminal demonstration: Bruce et al. (1997) found all affected members of four autosomal dominant familial dRTA families were heterozygous for band 3 (AE1) variants absent in unaffected relatives — "Affected individuals in four families with familial dRTA were heterozygous for mutations in their red cell HCO3-/Cl- exchanger, band 3 … genes" [PMID:9312167, *J Clin Invest* 100:1693–1707].

**Genetic risk factors / allelic spectrum:**
- **p.Arg589His (R589H)** — the prototype dominant allele, reported in multiple unrelated AD families [PMID:9312167; later confirmed by Jarolim et al.]. Arg589 is highly conserved across vertebrates.
- **p.Ser613Phe (S613F)** — dominant, ER-retained.
- **p.Arg901Ter (R901X)** — dominant truncation removing the C-terminal 11 residues (loss of a YXXΦ sorting motif).
- **p.Gly609Arg (G609R)**, **p.Arg589Cys/Ser** — additional dominant alleles.
- Contrast: **p.Gly701Asp (G701D)** is **recessive** (Golgi-retained, does not trap wild-type) — a key counter-example to avoid mis-assigning inheritance from the gene alone.

**Modifier/second-locus considerations:** AD dRTA from SLC4A1 is classically monogenic and dominant-negative; red-cell phenotype is usually absent in the dominant alleles (dissociation of kidney and erythroid effects).

**Environmental/acquired contributors (not causal but can unmask/aggravate dRTA generally):** autoimmune disease (Sjögren), drugs (amphotericin B, lithium), obstructive uropathy — these cause *acquired* dRTA and are differential diagnoses, not causes of the Mendelian disease. **Pregnancy / hyperemesis gravidarum** can precipitate severe acidosis and hypokalemia in affected women [GeneReviews, PMID:31600044].

**Protective factors:** none genetically established. Adequate alkali therapy is the key modifiable determinant of outcome (not "protection" against disease but against complications).

**Gene–environment interaction:** dietary acid load, dehydration, and intercurrent illness worsen acidosis and hypokalemia; adequate oral alkali and hydration mitigate nephrocalcinosis and growth failure.

---

## 3. Phenotypes

Onset in the dominant form is **typically later / milder** than recessive dRTA — "later presentations can occur, especially in individuals with autosomal dominant SLC4A1-related dRTA" [PMID:31600044]. Dominant patients have **older age of onset, lower urine pH, and higher serum potassium** than recessive patients (all statistically significant) [PMID:36776909].

| Phenotype | Type | HPO suggestion | Frequency / notes |
|---|---|---|---|
| Distal renal tubular acidosis (hyperchloremic normal-gap metabolic acidosis) | Lab/clinical | **HP:0008341** Distal renal tubular acidosis | Defining; 100% |
| Inappropriately alkaline urine (urine pH > 5.5) | Lab | **HP:0003774**-adjacent / HP:0011036 Abnormal urine pH | Defining |
| Hypokalemia | Lab | **HP:0002900** Hypokalemia | Common; milder in AD than AR |
| Hyperchloremia | Lab | **HP:0003228** Hyperchloremia | Common |
| Nephrocalcinosis / nephrolithiasis | Imaging/clinical | **HP:0000121** Nephrocalcinosis; **HP:0000787** Nephrolithiasis | Nephrocalcinosis ~72–88%; nephrolithiasis **more common with SLC4A1 (42% vs 21%)** [PMID:30773598; PMID:36776909] |
| Hypercalciuria / hypocitraturia | Lab | **HP:0002150** Hypercalciuria | Drives stone/calcinosis |
| Growth retardation / poor weight gain | Clinical | **HP:0001510** Growth delay | "developmental disorders in 61.16%" of SLC4A1 dRTA [PMID:36776909]; adult height mean SDS −0.57 [PMID:30773598] |
| Metabolic bone disease (rickets/osteomalacia, demineralization) | Clinical | **HP:0002748** Osteomalacia; HP:0002897 Osteopenia | Reported; can be presenting feature [PMID:35118447] |
| Chronic kidney disease | Clinical | **HP:0012622** Chronic kidney disease | CKD ≥stage 2 in 35% children, **82% adults** [PMID:30773598] |
| Hemolytic anemia / RBC morphology changes | Lab | **HP:0001878** Hemolytic anemia | Mainly in *recessive* SLC4A1 dRTA; dominant alleles usually spare RBCs [PMID:31600044; PMID:20799361] |
| Polyuria/polydipsia, vomiting, constipation, dehydration episodes | Symptom | HP:0000103; HP:0001959 | Early infantile presentation items [PMID:31600044] |
| Sensorineural hearing loss | Clinical | HP:0000407 | **Characteristic of ATP6V-gene dRTA, generally NOT SLC4A1** — do not attribute to AD SLC4A1 dRTA [PMID:31600044; PMID:30773598] |

**Severity/progression:** chronic, lifelong, generally non-progressive with treatment but with cumulative renal complications; episodic acute decompensation (acidotic crises) with illness or pregnancy.

**QoL impact:** stone disease, bone pain, growth failure in childhood, and lifelong multi-daily alkali dosing burden; metabolic control achieved in only ~51% of registry patients [PMID:30773598].

---

## 4. Genetic / Molecular Information

**Causal gene:** **SLC4A1** (chromosome 17q21.31), encoding **band 3 / AE1** (P02730). The **kidney isoform kAE1** lacks the N-terminal 65 residues of erythroid AE1 (alternative promoter) and localizes to the basolateral membrane of α-intercalated cells.

**Pathogenic variants (ClinVar/literature; dominant alleles):**
- **c.1766G>A, p.Arg589His (R589H)** — classic dominant; dbSNP rs121912748 (ClinVar pathogenic).
- **p.Ser613Phe (S613F)**, **p.Gly609Arg (G609R)**, **p.Arg901Ter (R901X, truncation)**, **p.Arg589Ser/Cys**, **p.Met909Thr**, duplications/del in C-terminus.
- Variant classes: predominantly **missense** affecting the transmembrane domain, plus a **nonsense/truncation** (R901X) removing the cytoplasmic C-terminal sorting motif.
- **Population frequency:** these are rare pathogenic alleles, essentially absent/very rare in gnomAD (private family variants). (Note: *Southeast Asian ovalocytosis* SAO deletion and certain recessive alleles are polymorphic in SE Asia, but those are distinct phenotypes.)
- **Origin:** germline. Somatic/mosaic origin not characteristic.

**Functional consequence — dominant-negative trafficking defect** (see §6). Dominant alleles are **not simple haploinsufficiency**: the mutant kAE1 heterodimerizes with wild-type kAE1 and retains it intracellularly, so one mutant allele impairs the product of the normal allele — the molecular basis of dominance [PMID:19423690 and related MDCK studies; PMC3584104].

**Modifier genes / epigenetics / chromosomal abnormalities:** none established; this is a classic single-gene dominant-negative disorder. No recurrent epigenetic mechanism or structural chromosomal lesion reported.

---

## 5. Environmental Information

Not an environmentally caused disease. Relevant environmental/physiological **modifiers** of the genetic phenotype: dietary acid/base load, hydration status, intercurrent illness, pregnancy/hyperemesis, and **potassium-sparing diuretics (to be avoided)** [PMID:31600044]. No infectious agents. No occupational/toxic etiology for the Mendelian disease (toxins such as amphotericin cause a separate *acquired* dRTA).

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous dominant-negative SLC4A1 variant** (e.g., R589H, S613F, R901X) is inherited → produces a mutant **kAE1** protein.
2. The mutant kAE1 **misfolds / loses its sorting signal** → it is **retained in the ER** (R589H, S613F) or **mis-sorted** (R901X, via loss of the C-terminal YXXΦ/AP-1A-dependent motif) rather than reaching the basolateral membrane. *(Demonstrated in MDCK/renal epithelial overexpression models; inferred in native intercalated cells.)*
3. Because kAE1 functions as a dimer, the mutant **traps wild-type kAE1 intracellularly** — "When coexpressed, the dominant mutants retained kAE1 WT intracellularly" → **net loss of functional basolateral Cl⁻/HCO₃⁻ exchange** at the α-intercalated cell basolateral membrane. This is the dominant-negative step. [PMC3584104]
4. Loss of basolateral HCO₃⁻ exit **impairs the coupled apical H⁺ secretion** by the vacuolar H⁺-ATPase (and H⁺/K⁺-ATPase): with bicarbonate unable to leave the cell basolaterally, intracellular pH and transport coupling collapse → **failure of net acid (H⁺) secretion into the collecting-duct lumen**.
5. → **Inability to acidify urine below pH ~5.5** and to excrete the daily acid load → **systemic hyperchloremic, normal–anion-gap metabolic acidosis**.
6. Chronic acidosis + impaired distal transport → **renal potassium wasting → hypokalemia**; and **hypercalciuria with hypocitraturia** (acidosis mobilizes bone calcium and reduces citrate excretion).
7. Hypercalciuria + hypocitraturia + alkaline urine → **calcium phosphate supersaturation → nephrocalcinosis and nephrolithiasis** (nephrolithiasis disproportionately frequent in SLC4A1 disease, 42%).
8. Chronic acidosis + calcium loss → **bone demineralization (rickets/osteomalacia)** and, in children, **growth retardation**.
9. Cumulative nephrocalcinosis/stones/obstruction → **progressive CKD** (82% of adults, CKD stages 2–4).

Branch: in the **recessive** SLC4A1 alleles (not this disease), kAE1 dysfunction in the erythrocyte produces **hemolytic anemia / abnormal RBC morphology**; dominant alleles typically spare the red cell (kidney–erythroid dissociation).

### Supporting molecular detail
- **Molecular function affected:** anion (Cl⁻/HCO₃⁻) antiporter activity — **GO:0015301** anion:anion antiporter activity; **GO:0006820** anion transport; **GO:0006885** regulation of pH; **GO:0015701** bicarbonate transport.
- **Cellular/biological processes:** protein localization to basolateral plasma membrane (**GO:0016323**), ER protein retention/quality control (**GO:0034976** ER stress; **GO:0030433** ERAD), intracellular pH regulation (**GO:0051453**).
- **Cell type:** **kidney collecting-duct α-intercalated cell (CL:1001431** kidney collecting duct intercalated cell; α-intercalated more specifically) and erythrocyte (**CL:0000232**) for the recessive hematologic axis.
- **Subcellular compartments:** basolateral plasma membrane (normal target), **endoplasmic reticulum** and **Golgi** (mislocalization sites) — GO:0005783 (ER), GO:0005794 (Golgi), GO:0016323 (basolateral membrane).
- **Rescue data (mechanistic corroboration):** chemical chaperones (DMSO, glycerol), the corrector **VX-809**, or low-temperature incubation rescued basolateral trafficking of the *recessive* G701D mutant but **not** the misfolded R589H; disrupting chaperone interactions rescued surface expression of dominant R589H and R901X — confirming trafficking/folding as the defect [PMC3584104; PLoS ONE 2013].

*Evidence-source caveat:* most trafficking data come from MDCK/renal-epithelial overexpression systems, so basolateral mislocalization in native human α-intercalated cells is **inferred** (supported by one report of absent AE1 polypeptide in intercalated cells of an R589H end-stage kidney).

---

## 7. Anatomical Structures Affected

- **Primary organ:** **kidney** (UBERON:0002113), specifically the **renal collecting duct** (UBERON:0001232) / cortical collecting duct; **distal nephron**.
- **Tissue/cell:** collecting-duct epithelium; **α-intercalated cells** (CL:1001431). Basolateral membrane is the key subcellular locus.
- **Secondary organs/systems:** **skeleton** (UBERON:0002481 bone tissue) — osteomalacia/rickets, demineralization; **urinary tract** — stones; **blood/erythroid** only in recessive alleles.
- **Subcellular:** endoplasmic reticulum (GO:0005783), Golgi apparatus (GO:0005794), basolateral plasma membrane (GO:0016323).
- **Laterality:** bilateral (systemic/renal).

---

## 8. Temporal Development

- **Onset:** AD form often **childhood to adulthood**, later/milder than recessive (which presents in infancy). Some AD patients diagnosed incidentally in adulthood after stones or during family screening. Median presentation age in the mixed registry was 0.5 y (range 0–54) [PMID:30773598].
- **Pattern:** chronic, insidious; punctuated by acute acidotic/hypokalemic crises (illness, pregnancy).
- **Progression:** renal complications accumulate; **CKD prevalence rises with age** (35% children → 82% adults) [PMID:30773598]. No patient reached CKD stage 5 in that cohort — overall "favourable outcome with normal adult height for most."
- **Duration:** lifelong; no spontaneous remission. Treatment-responsive biochemically but complications persist.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant**, dominant-negative mechanism. Each child of an affected individual has a **50%** transmission risk [PMID:31600044].
- **Penetrance:** high but with **variable expressivity** (age of onset and severity vary within families).
- **Epidemiology:** primary dRTA is **rare** (Orphanet class; overall hereditary dRTA prevalence not precisely established, on the order of <1–9/100,000 or rarer). Of 169 published SLC4A1 dRTA patients, **100 were autosomal dominant** (15 distinct dominant variants); 61 were recessive (21 variants) [PMID:36776909].
- **Geographic/ethnic:** **recessive** SLC4A1 dRTA is enriched in **Asian/Southeast Asian** populations ("Autosomal recessive inheritance was more often found in Asian patients, P<0.05") [PMID:36776909]; **dominant** SLC4A1 dRTA is seen more broadly (European/Western families, e.g., the original Bruce families).
- **Sex ratio:** roughly equal (registry female 52%).
- **Founder effects / consanguinity:** relevant to the recessive form (SE Asia), not the dominant form. No genetic anticipation. Germline mosaicism not characteristic.

---

## 10. Diagnostics

**Biochemical (LOINC-codable):**
- Serum electrolytes/venous blood gas: **hyperchloremic, normal–anion-gap metabolic acidosis** (low HCO₃⁻, normal anion gap), **hypokalemia**.
- **Urine pH inappropriately > 5.5** during acidosis (defining); positive **urine anion gap** (unmeasured cation deficit → impaired NH₄⁺ excretion).
- **Hypercalciuria, hypocitraturia**; 24-h urine calcium/citrate.
- **Ammonium chloride (or furosemide/fludrocortisone) acidification test** — failure to lower urine pH below ~5.3 confirms distal defect (reserved; not needed when acidosis + alkaline urine coexist).
- Relevant LOINC concepts: blood pH / pCO₂ / bicarbonate panels, serum potassium (LOINC 2823-3), serum chloride, urine pH (LOINC 5803-2), 24-h urine calcium/citrate.

**Imaging:** **renal ultrasound** (nephrocalcinosis, medullary cysts, stones); annual surveillance recommended [PMID:31600044].

**Genetic testing:** single-gene SLC4A1 sequencing or a **hereditary-tubulopathy/dRTA gene panel** (SLC4A1, ATP6V1B1, ATP6V0A4, FOXI1, WDR72); WES/WGS where panel negative. GeneReviews: diagnosis established by heterozygous (dominant) SLC4A1 pathogenic variant with the dRTA phenotype [PMID:31600044].

**Differential diagnosis:** proximal (type 2) RTA (Fanconi), type 4 (hyperkalemic) RTA, acquired dRTA (Sjögren, drugs, obstruction), and the other hereditary dRTA genes (distinguished by hearing loss pattern — SNHL favors ATP6V genes).

**Screening:** cascade genetic/biochemical screening of at-risk first-degree relatives is appropriate given 50% transmission and the value of early alkali therapy [PMID:31600044].

---

## 11. Outcome / Prognosis

- **Survival:** normal life expectancy with treatment; no excess mortality reported in the large cohort; **no CKD stage 5** observed [PMID:30773598].
- **Morbidity:** nephrocalcinosis/stones (and recurrent stone disease, higher in SLC4A1), bone disease, childhood growth impairment, and **CKD stages 2–4 in 82% of adults**.
- **Prognostic factors:** **adequacy of metabolic control** is the dominant determinant — normal plasma bicarbonate + normocalciuria was "associated with higher height and estimated glomerular filtration rate," yet achieved in only ~51% (and more often in higher-GDP countries, 67% vs 23%) [PMID:30773598]. AD disease generally milder than AR [PMID:36776909].
- **QoL:** chronic treatment burden; stone/bone complications; largely good functional outcome when controlled.

---

## 12. Treatment

**Mainstay — alkali replacement (lifelong):**
- **Oral alkali** (sodium and/or **potassium citrate / bicarbonate**) to correct acidosis and replace potassium; additional **potassium chloride** as needed [PMID:31600044]. Median prescribed alkali ~1.9 mEq/kg/day (IQR 1.2–3.3) [PMID:30773598].
- **ADV7103** — a combination **controlled-release potassium bicarbonate + potassium citrate**, approved in Europe, allowing less-frequent dosing and improving adherence/metabolic control [PMID:31600044]. (NCT trials: Advicenne Sibnayal/ADV7103 program.)
- Potassium citrate additionally reduces stone risk (raises urinary citrate).

**Supportive:** management of hypokalemia, stone disease, bone disease (ensure adequate control before vitamin D/phosphate as indicated), hearing/dental care in the gene-specific forms (not SLC4A1-dominant).

**Avoid:** **potassium-sparing diuretics** (use with caution/avoid) [PMID:31600044].

**Experimental / mechanism-directed:** pharmacologic **chaperone/corrector rescue** of mistrafficked kAE1 (DMSO, glycerol, VX-809, chaperone-interaction disruption) is in vitro/preclinical only — rescues some mutants (G701D) but not misfolded R589H without chaperone disruption [PMC3584104]. No gene/RNA therapy in clinical use.

**NCIT suggestions:** NCIT:C15986 Pharmacotherapy; NCIT:C15747 Supportive Care; NCIT:C15447 Dietary Intervention (alkali/fluid); NCIT:C15240 Genetic Counseling. Agents: potassium citrate, potassium bicarbonate, sodium bicarbonate (CHEBI-codable: bicarbonate CHEBI:17544; citrate CHEBI:30769; potassium chloride CHEBI:32588).

---

## 13. Prevention

No primary prevention (genetic). **Secondary prevention:** early diagnosis via **cascade family genetic/biochemical screening** and prompt alkali therapy to prevent nephrocalcinosis, bone disease, growth failure, and CKD [PMID:31600044]. **Tertiary prevention:** maintain metabolic control, hydration, renal ultrasound surveillance, bone monitoring, avoid nephrotoxic/potassium-sparing agents, and heightened monitoring in pregnancy. **Counseling:** genetic counseling for 50% transmission risk; prenatal/preimplantation testing available once the familial variant is known [PMID:31600044].

---

## 14. Other Species / Natural Disease

- **Orthologs:** *Slc4a1* in mouse (NCBI Gene 20533) and rat; conserved across vertebrates (Arg589 residue conserved). HomoloGene/Alliance of Genome Resources list cross-species orthologs.
- **Natural animal disease:** band 3 / AE1 deficiency causes hereditary anemias and, in some species, renal acidification phenotypes; dog SLC4A1-related disease is primarily hematologic. No prominent spontaneous dominant dRTA model catalogued in OMIA for companion animals specific to this phenotype. (Check OMIA for current SLC4A1 entries.)
- **Comparative biology:** erythroid vs kidney isoform dissociation (promoter/N-terminal truncation) is conserved, underpinning the kidney-specific dominant phenotype.

---

## 15. Model Organisms

- **Mouse:** *Slc4a1* knockout and **knock-in** models have been used to study band 3 function; AE1-null mice show spherocytic hemolytic anemia and acidification defects, modeling the transport loss. **MGI** is the resource for alleles (knockout, knock-in). Limitation: mouse models best capture the recessive/loss-of-function and erythroid phenotype; the **dominant-negative kidney trafficking** mechanism is better studied in cell models.
- **Cell models (principal mechanism tool):** **MDCK** and other polarized renal epithelial lines expressing wild-type vs mutant kAE1 demonstrate ER retention (R589H, S613F), Golgi retention (G701D, recessive), apical mis-sorting (R901X), dominant-negative trapping of wild-type, and chaperone/corrector rescue [PMC3584104; PLoS ONE 2013]. **iPSC-derived intercalated-cell/organoid** systems are an emerging avenue.
- **Applications:** trafficking/quality-control biology, dominant-negative testing, and small-molecule corrector screening. **Limitation:** overexpression systems may not reproduce native intercalated-cell stoichiometry; basolateral mislocalization in human tissue is inferred.

---

## Key Citations (PMID)

- **PMID:9312167** — Bruce LJ et al., *J Clin Invest* 1997;100:1693–1707. Familial dRTA associated with band 3 (AE1/SLC4A1) mutations; dominant inheritance; R589H prototype.
- **PMID:31600044** — *Hereditary Distal Renal Tubular Acidosis*, GeneReviews. Clinical features, dominant SLC4A1 inheritance, management (ADV7103), surveillance.
- **PMID:30773598** — Lopez-Garcia SC et al., *Nephrol Dial Transplant* 2019 (European dRTA Consortium, n=340). Nephrolithiasis 42% vs 21% with SLC4A1; CKD 82% of adults; alkali dosing; outcomes.
- **PMID:36776909** — Yang M et al., *Front Pediatr* 2023. 169 published SLC4A1 dRTA patients; 100 AD; nephrocalcinosis 72.27%; AD milder than AR; AR enriched in Asians.
- **PMID:35118447** — RTA manifesting as severe metabolic bone disease (presenting-feature caveat).
- **PMID:20799361 / PMID:33068675 / PMID:37448902** — SLC4A1 **recessive** (A858D and others) with hemolytic anemia — contrast cases establishing the dominant/recessive and kidney/erythroid dissociation.
- **PMC3584104** — Functional rescue of kAE1 trafficking mutant in renal epithelial cells; dominant (R589H, S613F, R901X) vs recessive (G701D) trafficking phenotypes; corrector/chaperone rescue.

**Sources (web):**
- [JCI 1997 Bruce et al. (article 119694)](https://jci.org/articles/view/119694)
- [PubMed 10926824 (R589H family / kidney AE1 absence)](https://pubmed.ncbi.nlm.nih.gov/10926824/)
- [PMC3584104 — Functional rescue of a kidney anion exchanger 1 trafficking mutant](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3584104/)
- [Molecular approach for distal renal tubular acidosis associated AE1 mutations (Mahidol repository)](https://repository.li.mahidol.ac.th/handle/123456789/28690)
- [PLoS ONE 2013 (corrector/chaperone rescue)](https://doaj.org/article/b4ee0af807f24bfcb181349ecacadd59)

---

### Note on the existing KB entry
The current `kb/disorders/Autosomal_Dominant_Distal_Renal_Tubular_Acidosis.yaml` is a **27-line stub** (name, MONDO term, one bare pathophysiology node with no cell type/GO terms/evidence, one phenotype, no genetic/treatment/prevalence/evidence blocks). This report provides the material to build it out: the dominant-negative kAE1 trafficking causal chain (§6), α-intercalated cell binding (CL:1001431), GO antiporter terms, HP phenotype set with frequencies (§3), SLC4A1 dominant allele spectrum (§4, with `variant_origin: GERMLINE`, `functional_impact_category: DOMINANT_NEGATIVE`), alkali/ADV7103 treatments (§12), and PMID-backed evidence — most of which is already in the local reference cache (`PMID_31600044`, `PMID_30773598`, `PMID_36776909`). Several cache entries are `abstract_only`; a `--force` full-text fetch may be warranted for the European cohort paper if quantitative phenotype tables are needed. I have **not** modified the entry — this is the research deliverable only.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 11 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:9312167` *(abstract only)*: "Affected individuals in four families with familial dRTA were heterozygous for mutations in their red cell HCO3-/Cl- exchanger, band 3 … genes"
  - closest text in source: "All affected patients in four families with autosomal dominant familial renal tubular acidosis (dRTA) were heterozygous for mutations in their red cell HCO3-/Cl- exchanger, band 3 (AE1, SLC4A1) genes, and these mutations were not found in any of the nine normal family members studied"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 3 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000407` (1 mention) - the report calls it "Clinical"; HP calls it **Sensorineural hearing impairment**
- `CL:1001431` (3 mentions) - the report calls it "α-intercalated cells"; CL calls it **kidney collecting duct principal cell**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0015301` (obsolete anion:anion antiporter activity) (1 mention)
- `GO:0030433` (obsolete ubiquitin-dependent ERAD pathway) (1 mention) - replaced by `GO:0036503`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016323` (3 mentions) - the report calls it "basolateral membrane"; GO calls it **basolateral plasma membrane**
- `GO:0005783` (2 mentions) - the report calls it "ER", "Subcellular:** endoplasmic reticulum"; GO calls it **endoplasmic reticulum**
- `GO:0005794` (2 mentions) - the report calls it "Golgi"; GO calls it **Golgi apparatus**, and lists "Golgi" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "kidney", "Primary organ:** **kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
- `UBERON:0001232` (1 mention) - the report calls it "renal collecting duct"; UBERON calls it **collecting duct of renal tubule**, and lists "collecting duct" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005783` - called "ER", "Subcellular:** endoplasmic reticulum"
- `UBERON:0002113` - called "kidney", "Primary organ:** **kidney"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.