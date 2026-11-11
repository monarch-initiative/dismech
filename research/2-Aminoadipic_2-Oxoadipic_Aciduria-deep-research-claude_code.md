---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-09T00:42:51.804136'
end_time: '2026-11-09T00:48:13.960926'
duration_seconds: 322.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: 2-Aminoadipic 2-Oxoadipic Aciduria
  mondo_id: MONDO:0008774
  category: Mendelian
  causal_genes: DHTKD1
  omim_id: OMIM:204750, OMIM:245130
  synonyms: Ketoadipicaciduria; AMOXAD; alpha-aminoadipic aciduria; alpha-aminoadipic
    and alpha-ketoadipic aciduria
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
  web_search_requests: 4
  num_turns: 31
  total_cost_usd: 2.945810900000001
  session_id: ceda2d98-545d-47ed-bdf7-a03530a0d3f9
  stop_reason: end_turn
  permission_denials: 6
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 12
reference_validation:
  total_references: 35
  verified: 35
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 2
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:25860818
  relevance_assessed: 35
  on_topic: 15
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 34
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 1
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0001263
    reported_labels:
    - Sign
    ontology_label: Global developmental delay
  - term_id: HP:0001249
    reported_labels:
    - Sign
    ontology_label: Intellectual disability
  - term_id: HP:0000750
    reported_labels:
    - Sign
    ontology_label: Delayed speech and language development
  - term_id: HP:0001250
    reported_labels:
    - Sign
    ontology_label: Seizure
  - term_id: HP:0001251
    reported_labels:
    - Sign
    ontology_label: Ataxia
  - term_id: HP:0000252
    reported_labels:
    - Sign
    ontology_label: Microcephaly
  - term_id: UBERON:0002107
    reported_labels:
    - Biochemically primary organs:** liver
    ontology_label: liver
  - term_id: UBERON:0000955
    reported_labels:
    - Clinically affected organ, when symptomatic:** brain
    ontology_label: brain
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 2-Aminoadipic 2-Oxoadipic Aciduria
- **MONDO ID:** MONDO:0008774 (if available)
- **Causal gene(s):** DHTKD1
- **OMIM:** OMIM:204750, OMIM:245130
- **Synonyms:** Ketoadipicaciduria; AMOXAD; alpha-aminoadipic aciduria; alpha-aminoadipic and alpha-ketoadipic aciduria
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **2-Aminoadipic 2-Oxoadipic Aciduria** covering all of the
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

Checking the cached Danhauser 2012 abstract, then searching the literature for the remaining primary sources.

Gathering verbatim abstract text for the key papers so the report's quotes are exact; trying the repo's sanctioned reference fetcher.

Pulling titles for the historical case reports, then I'll write the report.

# Research Report: 2-Aminoadipic 2-Oxoadipic Aciduria (AMOXAD; MONDO:0008774; DHTKD1)

## About this report and its quotes

The causal gene is **DHTKD1** (dehydrogenase E1 and transketolase domain containing 1; `hgnc:23537`, on 10p14). Biallelic loss-of-function variants cause the disease, which is inherited as an autosomal recessive trait. A heterozygous nonsense variant in the same gene causes a different, allelic disease: Charcot-Marie-Tooth disease type 2Q (CMT2Q). This report keeps the two apart.

I could not download abstracts directly in this session: `curl` and `just fetch-reference` both needed approval. I used two kinds of source, and the quotes are labelled to match:

- **[cached]**: copied verbatim from `references_cache/` files already in the repo. These are safe to use as evidence snippets.
- **[fetched]**: short fragments pulled from PubMed eFetch through a summarising web tool. They are probably exact, but run `just fetch-reference PMID:<n>` and `just count-verified-snippets` on each before using it as a snippet.

Ontology IDs below come from the repo's term caches (`cache/*/terms.csv`) unless they are marked **(look up)**. None of the IDs were written from memory.

---

## 1. Disease information

**Overview.** AMOXAD is an inborn error of L-lysine, L-hydroxylysine and L-tryptophan breakdown. The defect is in the 2-oxoadipate dehydrogenase complex (OADHc), whose E1 subunit (E1a) is DHTKD1. Patients excrete too much 2-oxoadipate (α-ketoadipate) and 2-aminoadipate, often with 2-hydroxyadipate as well. The clinical picture varies widely, from no symptoms at all to developmental delay, epilepsy, ataxia and microcephaly. Whether the biochemical defect causes disease is still debated.

- **Disease-causing step** [cached, PMID:23141293]: "demonstrating that DHTKD1 codes for the enzyme mediating the last unresolved step in the L-lysine-degradation pathway"
- **Early view of the condition**: Fischer 1974 (PMID:4442872) is titled "Alpha-aminoadipic aciduria, a non-deleterious inborn metabolic defect".

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0008774 ("2-aminoadipic 2-oxoadipic aciduria"). Its parent is MONDO:0017351 (inborn disorder of lysine and hydroxylysine metabolism). |
| OMIM | 204750 (2-aminoadipic 2-oxoadipic aciduria) and 245130 (historical α-ketoadipic aciduria). Check whether OMIM now treats 245130 as merged or removed before mapping it. |
| Orphanet | ORPHA:79154. Its record is not yet in `references_cache/`; build it with `just structured-rebuild-orphanet --id 79154`. |
| ICD-10 | E72.3 (disorders of lysine and hydroxylysine metabolism), via the SNOMED CT to ICD-10 map |
| SNOMED CT | 782918002 (from the nictiz terminology browser) |
| MedGen | C1859817 |
| ClinGen | DHTKD1 / MONDO:0008774 / AR / **Definitive**, Aminoacidopathy GCEP, 2020-11-03, `CGGV:assertion_d6dd5de3-9819-432d-996c-12a66dff277f-2020-11-03T193815.515Z` (from `cache/clingen/gene_validity.csv`) |

**Synonyms.** AMOXAD; α-aminoadipic and α-ketoadipic aciduria; 2-ketoadipic aciduria (ketoadipicaciduria); α-aminoadipic aciduria. The last name was also used for "isolated" cases in which no 2-oxoadipate was found.

**Source of the data.** Everything comes from individual case reports and small series, about 20 to 30 molecularly or biochemically described cases. There are no registry or EHR cohorts.

**Repo state.** `kb/disorders/2-Aminoadipic_2-Oxoadipic_Aciduria.yaml` exists but is only an 8-line skeleton with no evidence. The stub `stubs/2-aminoadipic_2-oxoadipic_Aciduria.yaml` is priority HIGH and `UNDECIDED`.

---

## 2. Etiology

- **Cause.** Biallelic germline DHTKD1 variants that reduce OADHc activity.
  - Danhauser 2012 [cached, PMID:23141293]: "our results establish mutations in DHTKD1 as a cause of human 2-aminoadipic and 2-oxoadipic aciduria via impaired turnover of decarboxylation 2-oxoadipate to glutaryl-CoA."
  - Hagen 2015 (PMID:25860818) sequenced DHTKD1 in 9 patients with the combined aciduria and 1 with isolated aminoadipic aciduria. It found causal variants in 8 of them.
- **Genetic risk.** The recurrent missense variant p.Gly729Arg is the main allele.
  - [fetched, PMID:32303640]: "A heterozygous missense mutation, c.2185G→A (p.G729R), in DHTKD1 has been identified in most AMOXAD cases."
  - [fetched, PMID:25860818]: "Two missense mutations, one of which was reported before, were observed in the majority of cases."
- **Modifiers and environment.** No modifier genes are established.
  - Dietary lysine sets how much 2-aminoadipate is excreted. Przyrembel 1975 (PMID:1112064), [fetched]: "The excretion of alpha-aminoadipic acid correlated to the lysine intake".
  - **Drug phenocopy:** vigabatrin raised α-aminoadipic acid in 8 of 8 treated children (Vallat 1996, PMID:8764822). This is a confounder in diagnosis, not a cause of the disease.
- **Protective factors and gene-environment interactions.** None are documented.
- **A related population signal (not the disease itself).** Common variation near DHTKD1 drives plasma 2-aminoadipate levels, and plasma 2-aminoadipate is associated with diabetes risk and HDL cholesterol:
  - Wu 2014 BXD mice (PMID:25215496), [fetched]: "Dhtkd1 was identified as a primary regulator of 2-aminoadipate"
  - Shi 2022 GWAS (PMID:35621206)

  This is not AMOXAD. Do not put it into the Mendelian entry as a risk factor.

---

## 3. Phenotypes

The best single summary of the spectrum is Stiles 2016 (PMID:26141459), [fetched]: findings range "from early-onset developmental delay, epilepsy, ataxia, and microcephaly to completely normal." In the same report, of 4 new individuals, "three of which remain asymptomatic."

Ascertainment bias is likely: most patients were found through metabolic screening of children who already had neurological problems. That bias may explain much of the apparent clinical burden.

| Phenotype | Type | HPO (from repo cache) | Frequency / notes | Key source |
|---|---|---|---|---|
| Increased urinary 2-oxoadipate and 2-aminoadipate | Lab (defining) | HP:0001992 Organic aciduria; HP:0003355 Aminoaciduria. A more specific HPO term may exist **(look up)**. | ~100% (defining) | PMID:23141293, 25860818 |
| Urinary 2-hydroxyadipate | Lab | HP:0034465 2-hydroxyadipic aciduria | Common | PMID:1112064, 1527995 |
| Asymptomatic / normal development | — | none | Substantial: 3 of 4 in Stiles; healthy affected siblings (Wilson 1975, PMID:1161338, "a mentally and physically normal sister"; Fischer 1980, PMID:6772026) | PMID:26141459 |
| Global developmental delay / psychomotor retardation | Sign | HP:0001263 | Variable; most often reported | PMID:1112064, 26141459 |
| Intellectual disability | Sign | HP:0001249 | Variable | PMID:117247, 6163632, 1161338 |
| Speech delay | Sign | HP:0000750 | Occasional | Takechi 1993 (PMID:8487492), [fetched]: "A 3.5-year-old Japanese boy with a mild speech disturbance" |
| Seizures / epilepsy | Sign | HP:0001250 | Occasional | PMID:26141459, 6163632 |
| Hypotonia | Sign | HP:0001252 (or HP:0001290) | Occasional | PMID:117247, 6163632 |
| Ataxia | Sign | HP:0001251 | Rare | PMID:26141459 |
| Microcephaly | Sign | HP:0000252 | Rare | PMID:26141459 |
| Hyperactivity / autistic behaviour | Behaviour | HP:0000752 / HP:0000729 | Reported in some series. Confirm the source text before using. | PMID:25860818 (full text) |
| Ketoacidotic episodes progressing to coma | Episodic | HP:0001993 Ketoacidosis; HP:0001259 Coma | Single case, with a coincident Kearns-Sayre mtDNA deletion, so the link is confounded | Barshop 2000 (PMID:10655159) |
| Hepatic steatosis / sudden death | — | HP:0001397 | Single forensic case; causality unproven | Kondou 2022 (PMID:35648288) |

**Onset.** Infancy or childhood when symptoms occur. Many cases are found incidentally, including through neonatal screening (Peng 1999, PMID:10503694, "Asymptomatic alpha-ketoadipic aciduria detected").

**Progression.** Not progressive and not degenerative. No natural-history data exist.

**Quality of life.** There are no data. Where symptoms occur, the impact comes from the neurodevelopmental features.

**Allelic disorder.** Peripheral axonal neuropathy (CMT2Q) is not part of AMOXAD as curated. It is a separate MONDO/OMIM entity (OMIM 615025) caused by the heterozygous nonsense variant p.Tyr485* (PMID:23141294) and is already covered by `kb/disorders/Charcot-Marie-Tooth_Disease_Type_2.yaml`. Keep the two entries apart.

---

## 4. Genetic and molecular information

- **Gene.** DHTKD1, `hgnc:23537`, OMIM *614984. It has 17 exons and encodes a 919-amino-acid mitochondrial protein.
  - [cached, PMID:23141294]: "There are 17 exons with an open reading frame of 5,202 bp, encoding a peptide of 919 amino acids"
- **Index variants** [cached, PMID:23141293]:
  - Proband 1: "compound heterozygosity for an initiating methionine mutation (c.1A>G) and a missense mutation (c.2185G>A [p.Gly729Arg])"
  - Proband 2: the same missense change "together with a nonsense mutation (c.1228C>T [p.Arg410(∗)])"
- **Range of variants.** Hagen 2015, [fetched, PMID:25860818]: "We report nine novel mutations, including three missense mutations, two nonsense mutations…", plus splice and indel variants.
- **Functional testing.** Leandro 2020 (PMID:32633484) tested 10 disease-associated missense variants. Most impair folding, thermal stability or activity; [fetched]: "three variants showed no abnormalities".
- **How p.G729R works.** Zhang 2020 (PMID:32303640), [fetched]: the variant "displays a 50-fold decrease in catalytic efficiency for NADH production". It acts by disrupting assembly of E1a with E2o (DLST) and the channelling of intermediates between them.
- **Classification.** ClinGen rates the gene-disease relationship Definitive (AR). ClinVar lists p.Gly729Arg as Pathogenic/Likely pathogenic for AMOXAD; check the current entry before citing it.
- **Allele frequency.** p.Gly729Arg is a recurrent allele in gnomAD (roughly 0.1–0.3% in Europeans; **check gnomAD**). That carrier frequency implies the biochemical phenotype is under-ascertained, which fits with most affected people having no symptoms.
- **Functional consequence.** Loss of function, both partial (missense) and null (start-loss, nonsense). In GENO/dismech terms: `LOSS_OF_FUNCTION` / `PARTIAL_LOSS_OF_FUNCTION`, `variant_origin: GERMLINE`, biallelic.
- **Epigenetics and chromosomal abnormalities.** None reported.

---

## 5. Environmental information

No environmental cause is known. Dietary lysine changes how much metabolite is excreted (PMID:1112064). Vigabatrin is the one known pharmacological phenocopy (PMID:8764822). No infectious agents are involved.

---

## 6. Mechanism and pathophysiology

**Causal chain**

1. Biallelic DHTKD1 loss-of-function variants (start-loss, nonsense, or destabilising/assembly-defective missense such as p.G729R) **lead to** reduced or absent E1a protein or activity. *Shown directly* (PMID:23141293, 32303640, 32633484).
2. Loss of E1a activity **results in** impaired oxidative decarboxylation of 2-oxoadipate to glutaryl-CoA in the mitochondrial matrix OADHc, which DHTKD1 forms with DLST (E2o) and DLD (E3). *Shown directly*:
   - fibroblast complementation and tracer studies (PMID:23141293)
   - shared E2/E3 subunits (PMID:29191460)
   - the 24-mer DLST scaffold "for assembling DHTKD1 and DLD protomers into a megacomplex" (PMID:32695416, [fetched])
3. The blocked step **leads to** a build-up of 2-oxoadipate upstream. Transamination of 2-oxoadipate then raises 2-aminoadipate, and reduction raises 2-hydroxyadipate. All three spill into urine and plasma. *Shown directly* (PMID:23141293, 1112064, 1112065).
4. **Branch: partial compensation by OGDH.** E1o (OGDH) can also decarboxylate 2-oxoadipate and forms hybrid complexes with DHTKD1 (PMID:32160276, [fetched]: "2-oxoadipic acid is a substrate for DHTKD1, but also for OGDH in a cell model system"). This **results in** lysine flux still reaching glutaryl-CoA, which plausibly explains why the disease is mild or silent. *Inferred* from cell and mouse data, including the Dhtkd1/Gcdh double-knockout result in PMID:28545977.
5. **Branch: neurological manifestations (uncertain).** It has been proposed that 2-oxoadipate and 2-aminoadipate accumulation, a lysine-pathway imbalance, or E1a-linked superoxide/H₂O₂ production (PMID:29191460, 26708453) **leads to** neurodevelopmental symptoms in a minority of patients. *Not shown*: no causal link has been demonstrated. Ascertainment bias and coincident second diagnoses (for example Kearns-Sayre syndrome in PMID:10655159) are equally plausible explanations. Record this as a `KNOWLEDGE_GAP`.

**Biochemistry**

- Human E1a prefers 2-oxoadipate about 49-fold over 2-oxoglutarate (PMID:29191460, [fetched]).
- The active site is "engineered specifically to accommodate its preference for the longer substrate" (PMID:32695416).
- Thiamine diphosphate cofactor: crystal structures at 2.25 Å (PDB 6U3J; PMID:32633484) and 1.9 Å (PMID:32695416; PDB 6SY1).

**Suggested ontology terms**

| Category | Terms |
|---|---|
| GO processes | GO:0019477 L-lysine catabolic process (cached). Also worth looking up: the 2-oxoadipate dehydrogenase activity molecular-function term and "tryptophan catabolic process" **(look up)**. |
| GO cellular component | GO:0045252 oxoglutarate dehydrogenase complex; GO:0005759 mitochondrial matrix (both cached) |
| CHEBI | CHEBI:15524 glutaryl-CoA and CHEBI:18019 L-lysine (cached). Still needed: 2-oxoadipate, 2-aminoadipate, 2-hydroxyadipate, thiamine diphosphate **(look up; none are cached)**. |
| CL | CL:0000057 fibroblast (the diagnostic and complementation system); CL:0000182 hepatocyte (main site of lysine catabolism) |

**Omics.** There are no disease-specific transcriptomic, proteomic or single-cell datasets. The relevant metabolomics are the urine organic-acid and amino-acid profiles. The BXD mouse multi-omics study (PMID:25215496) is the main systems-level dataset, but it concerns natural Dhtkd1 variation in mice, not the human disease.

---

## 7. Anatomical structures affected

- **Biochemically primary organs:** liver (UBERON:0002107) and kidney (UBERON:0002113). Gray 1980 (PMID:6796766) found the highest tissue 2-aminoadipate post mortem in these organs.
- **Clinically affected organ, when symptomatic:** brain (UBERON:0000955), presenting as a neurodevelopmental phenotype.
- **Subcellular site:** mitochondrial matrix (GO:0005759).
- Lateralisation does not apply.

---

## 8. Temporal development

- **Onset:** congenital biochemical defect. Symptoms, when present, appear in infancy or childhood.
- **Course:** static and lifelong. There are no stages or remissions, and there is no defined critical period.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007). ClinGen classifies the relationship as AR / Definitive.
- **Penetrance:** clinical penetrance is markedly incomplete, while biochemical penetrance is complete. Asymptomatic affected siblings are documented (PMID:1161338, 6772026, 26141459).
- **Expressivity:** variable.
- No anticipation, mosaicism or founder effect has been reported. p.G729R recurs across European populations.
- **Prevalence:** unknown. About 20–30 published cases. Orphanet records the disease by number of published cases rather than giving a population rate, so use `measure_type: CASES_IN_LITERATURE` and do not assign a numeric band.
- **Sex ratio:** no bias (both sexes affected).
- **Populations:** cases reported from Europe, North America, Japan, Korea (Lee 2001, PMID:11596655) and China (Peng 1999).

---

## 10. Diagnostics

- **Urine organic acids (GC-MS):** raised 2-oxoadipate and 2-hydroxyadipate. 2-oxoadipate is unstable, so it can be missed.
- **Plasma and urine amino acids:** raised 2-aminoadipate.
- **Confirmation:** genetic testing, either single-gene DHTKD1 sequencing or exome sequencing, which is how the gene was found (PMID:23141293). Fibroblast lysine-flux and complementation assays are research tools only. LOINC codes for urine 2-aminoadipate or 2-oxoadipate **(look up through `just loinc-seed-cache`)**.
- **Differential diagnosis:**
  - glutaric aciduria type 1 (GCDH; glutarate and 3-OH-glutarate are raised instead)
  - 2-aminoadipic semialdehyde synthase defects / hyperlysinemia (AASS; HP:0002161)
  - pyridoxine-dependent epilepsy (ALDH7A1; α-aminoadipic semialdehyde, pipecolate)
  - Zellweger-spectrum disorders
  - vigabatrin exposure
  - combined D/L-2-hydroxyglutaric aciduria
- **Screening:** not on standard newborn-screening panels. Cases have been picked up incidentally by urine screening programmes (PMID:3930865, 10503694).

---

## 11. Outcome and prognosis

- Life expectancy is presumed normal for most patients.
- The one fatal case (Jakobs 1992, PMID:1527995) and the sudden-death case (PMID:35648288) do not establish that the disease causes death.
- Neurodevelopmental outcome varies, and no prognostic biomarkers are known. Because asymptomatic cases are common, how much of the clinical burden belongs to this disease is "questionable" (Stiles 2016).

---

## 12. Treatment

No treatment is established or proven.

- **Low-lysine diet:** tried; it lowers metabolite excretion (PMID:1112064). In Casey 1978 (PMID:117247), lysine restriction plus vitamins B1/B6 did not correct the biochemistry. NCIT:C15447 Dietary Intervention.
- **Pyridoxine (vitamin B6):** after 3 months, one patient showed a smaller 2-aminoadipate rise on lysine loading (Manders 1981, PMID:6163632). Bind the agent through `therapeutic_agent` with a CHEBI pyridoxine term **(look up)**. Do not use NCIT "Vitamin B6" as a treatment term.
- **Thiamine:** a rational choice for a ThDP-dependent E1 enzyme, but untested.
- **Supportive care** for developmental and seizure features: NCIT:C15747 Supportive Care. **Genetic counselling:** NCIT:C15240.
- **Clinical trials:** none.
- **Related therapeutic research (not a treatment for this disease):** DHTKD1 is being studied as a substrate-reduction target for glutaric aciduria type 1.
  - Inhibitors identified: adipoylphosphonic acid and tenatoprazole (PMID:32633484). Phosphonate inhibitors have been tested in rats (PMID:35795216, 35721081).
  - Genetic Dhtkd1 loss did not rescue GA1 mice (PMID:28545977, [fetched]): "the genetic Dhtkd1 inhibition in Dhtkd1-/-/Gcdh-/- mice could not rescue the GA-I phenotype."
  - The near-benign course of AMOXAD is the safety argument for that strategy.

---

## 13. Prevention

There is no primary prevention. Genetic counselling and cascade testing of siblings are possible, but carrier testing and prenatal diagnosis are hard to justify for a mostly benign condition. Tertiary prevention is limited to avoiding unnecessary treatment once the diagnosis is confirmed.

---

## 14. Other species and natural disease

- **Laboratory mice:** the C57BL/6J strain carries a solitary LTR retrotransposon insertion in Dhtkd1 that reduces functional mRNA, giving the strain mild 2-aminoadipic acidemia (Leandro 2019, PMID:30709776, [fetched]: "C57BL/6J mice have decreased Dhtkd1 mRNA expression due to a solitary long terminal repeat (LTR)"). In practice this is a naturally occurring model, and a confounder in metabolic studies that use B6 mice.
- **BXD recombinant inbred mice:** natural Dhtkd1 variation (PMID:25215496).
- No OMIA veterinary entry was found.
- The gene is conserved across vertebrates. Mouse Dhtkd1 is NCBI Gene 209692 **(verify)**.

---

## 15. Model organisms

| Model | Phenotype | Fidelity to AMOXAD |
|---|---|---|
| Dhtkd1⁻/⁻ mouse (Biagosch 2017, PMID:28545977) | Raised 2-aminoadipate and 2-oxoadipate; no clinical symptoms even on a high-lysine diet ([fetched]: "only Gcdh-/- mice but not Dhtkd1-/- mice developed clinical symptoms") | **RECAPITULATES** the biochemistry and the benign course; HIGH fidelity |
| Dhtkd1⁻/⁻ mouse (Xu 2018, PMID:29661920) | Neuropathy resembling CMT2, very high 2-ketoadipate, 2-AAA-driven insulin and Schwann-cell effects ([fetched]: "Dhtkd1-/- mice mimic the major aspects of CMT2 phenotypes") | Models CMT2Q rather than AMOXAD. Conflicts with Biagosch, possibly because of strain or background differences. A `HUMAN_MODEL_MISMATCH` candidate. |
| Dhtkd1 Y486* knock-in mouse (Luan 2020, PMID:32169121) | Sensory deficits, thin axons, mitochondrial accumulation | Models CMT2Q, not AMOXAD |
| C57BL/6J (natural LTR hypomorph, PMID:30709776) | Mild 2-aminoadipic acidemia | PARTIALLY_RECAPITULATES (hypomorph) |
| Patient fibroblasts with lentiviral complementation (PMID:23141293) | Raised 2-oxoadipate that normalises with wild-type DHTKD1 | IN_VITRO; HIGH fidelity for the enzyme defect |
| HEK-293 DHTKD1/GCDH knockouts (PMID:32160276); HAP-1 DHTKD1 knockout (PMID:34484123) | Substrate overlap with OGDH; respiration defects | IN_VITRO mechanism models |
| Recombinant enzyme and crystal structures (PMID:29191460, 32303640, 32633484, 32695416) | Kinetics, variant effects | Cell-free systems; a `BOUNDARY_OMISSION` divergence (no cellular context) |

**Resources:** MGI (Dhtkd1 alleles), IMPC.

---

## Curation notes for the KB entry

1. **Naming.** A single-gene Mendelian disease named after its metabolite profile. "2-Aminoadipic 2-Oxoadipic Aciduria" is the MONDO, OMIM and ClinGen label and is established, so a `DHTKD1-Related …` rename is not needed. Use the `entry-naming` skill to confirm, and decide whether the file slug or the stub's lowercase spelling wins.
2. **ClinGen tier.** Record it as a `gene_disease_validity` block with `classified_by: CLINGEN` and the CGGV identifier above, quoting the cache row.
3. **CMT2Q.** Keep it out of this entry. A cross-reference in `notes` is enough.
4. **Disease-causing claim.** Add a `KNOWLEDGE_GAP` discussion on whether the disease causes any symptoms at all, using PMID:26141459, 1161338 and 4442872 as evidence.
5. **Diet and pyridoxine.** Model them as treatments with low-strength, single-case evidence. Do not present them as standard of care.
6. **GeneReviews.** No GeneReviews chapter is expected. Confirm with `just check-genereviews`.

---

## Sources

**Primary literature (PMIDs).** 23141293 (Danhauser 2012, AJHG); 23141294 (Xu 2012, AJHG, CMT2Q); 25860818 (Hagen 2015, JIMD); 26141459 (Stiles 2016, JIMD Rep); 28545977 (Biagosch 2017, BBA); 29191460 (Nemeria 2018); 26708453 (Goncalves 2016); 29661920 (Xu 2018, MCB); 30709776 (Leandro 2019, MGM); 32160276 (Leandro 2020, HMG); 32303640 (Zhang 2020, JBC); 32633484 (Leandro 2020, ACS Chem Biol); 32695416 (Bezerra 2020, IUCrJ); 32169121 (Luan 2020); 25215496 (Wu 2014, Cell); 35621206 (Shi 2022, JAHA); 34484123 (Wang 2021).

**Historical case reports (PMIDs).** 4442872, 1112064, 1112065, 1161338, 117247, 6772026, 6796766, 6163632, 6434826, 3930865, 1527995, 8487492, 8764822, 10503694, 10604155, 10655159, 11596655, 35648288.

**Web sources**
- [Hagen 2015, Springer](https://link.springer.com/article/10.1007/s10545-015-9841-9)
- [Erasmus repository: Hagen 2015](https://repub.eur.nl/pub/84182)
- [MDC repository: Biagosch 2017](https://edoc.mdc-berlin.de/16578/)
- [PMC7206849](https://pmc.ncbi.nlm.nih.gov/articles/PMC7206849)
- [PMC7278340](https://pmc.ncbi.nlm.nih.gov/articles/PMC7278340)
- [RCSB PDB 6U3J](https://www.rcsb.org/annotations/6U3J)
- [PDB 6SY1](https://intermetaldb.biotech.uwr.edu.pl/PDB_summary/6SY1/)
- [SNOMED CT 782918002 (nictiz)](https://terminologie.nictiz.nl/terminology/snomed/viewConcept/782918002)
- [MedGen C1859817 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/medgen/C1859817/index.html)
- [NIH GARD record](https://rarediseases.info.nih.gov/assets/singles/16708.json)
- [Orphanet prevalence list (PDF)](https://www.FSHDSociety.org/wp-content/uploads/2019/08/Prevalence_of_rare_diseases_by_alphabetical_list.pdf)
- [PubMed eUtils](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/)

**Repo files.** `cache/clingen/gene_validity.csv`, `references_cache/PMID_23141293.md`, `references_cache/PMID_23141294.md`, `stubs/2-aminoadipic_2-oxoadipic_Aciduria.yaml`.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 35 |
| On topic | 15 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:25860818` *(abstract only)*: "A heterozygous missense mutation, c.2185G→A (p.G729R), in DHTKD1 has been identified in most AMOXAD cases."
  - closest text in source: "Two missense mutations, one of which was reported before, were observed in the majority of cases"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001263` (1 mention) - the report calls it "Sign"; HP calls it **Global developmental delay**
- `HP:0001249` (1 mention) - the report calls it "Sign"; HP calls it **Intellectual disability**
- `HP:0000750` (1 mention) - the report calls it "Sign"; HP calls it **Delayed speech and language development**
- `HP:0001250` (1 mention) - the report calls it "Sign"; HP calls it **Seizure**
- `HP:0001251` (1 mention) - the report calls it "Sign"; HP calls it **Ataxia**
- `HP:0000252` (1 mention) - the report calls it "Sign"; HP calls it **Microcephaly**
- `UBERON:0002107` (1 mention) - the report calls it "Biochemically primary organs:** liver"; UBERON calls it **liver**
- `UBERON:0000955` (1 mention) - the report calls it "Clinically affected organ, when symptomatic:** brain"; UBERON calls it **brain**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005759` (2 mentions) - the report calls it "Subcellular site:** mitochondrial matrix"; GO calls it **mitochondrial matrix**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.