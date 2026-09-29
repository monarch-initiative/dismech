---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T03:44:39.722876'
end_time: '2026-09-04T03:49:22.657335'
duration_seconds: 282.93
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal dominant Charcot-Marie-Tooth disease type 2K
  mondo_id: ''
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 11
  num_turns: 25
  total_cost_usd: 1.2490736
  session_id: 8d9e328a-5068-5e56-a088-e781944a4092
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 23
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 1
  quotes_unsupported: 8
  unsupported_quote_references:
  - PMID:36353131
  - PMC:PMC9637907
  - PMID:35656516
  - PMID:19782751
  - PMC:PMC3674444
  - PMC:PMC4393229
  relevance_assessed: 14
  on_topic: 10
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 43
  not_found: 1
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.022
  labels_checked: 24
  labels_matching: 15
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0025303
    reported_labels:
    - Clinical variability
    ontology_label: Episodic
  - term_id: CL:0000097
    reported_labels:
    - sensory neuron
    ontology_label: mast cell
  - term_id: UBERON:0001456
    reported_labels:
    - sciatic nerve, representative long nerve
    ontology_label: face
  - term_id: UBERON:0002021
    reported_labels:
    - anterior horn of spinal cord
    ontology_label: occipital lobe
  labels_variant: 5
  unresolved_terms:
  - HP:0025438
  obsolete_terms:
  - term_id: HP:0040083
    ontology_label: obsolete Toe walking
    replaced_by: HP:0030051
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal dominant Charcot-Marie-Tooth disease type 2K
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal dominant Charcot-Marie-Tooth disease type 2K** covering all of the
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

# Autosomal Dominant Charcot-Marie-Tooth Disease Type 2K (CMT2K) — Research Report

## 1. Disease Information

**Overview.** CMT2K is an axonal (non-demyelinating) subtype of Charcot-Marie-Tooth disease — the most common inherited peripheral neuropathy — caused by pathogenic variants in *GDAP1* (ganglioside-induced differentiation-associated protein 1), a tail-anchored outer mitochondrial membrane protein expressed predominantly in neurons. *GDAP1* is unusual among CMT genes in producing **both dominant and recessive disease**: autosomal recessive *GDAP1* variants classically cause the severe, early-onset axonal CMT2K/AR-CMT2 phenotype (and the demyelinating CMT4A phenotype), while **autosomal dominant (heterozygous) *GDAP1* variants cause a distinct, generally much milder, later-onset form of CMT2K** ([GeneReviews NBK1539](https://www.ncbi.nlm.nih.gov/books/NBK1539/); [Claramunt 2005/OMIM #607831](https://omim.org/entry/607831)).

- "Onset varies from childhood to late adulthood. Difficulty with walking is the most common initial manifestation" — GeneReviews, describing the autosomal dominant (AD) form ([NBK1539](https://www.ncbi.nlm.nih.gov/books/NBK1539/)).
- "Affected persons generally remain ambulatory," in contrast to the recessive form, where wheelchair dependence typically occurs by the second decade ([NBK1539](https://www.ncbi.nlm.nih.gov/books/NBK1539/)).
- Orphanet summary: "Autosomal dominant Charcot-Marie-Tooth disease type 2K is a rare form of axonal Charcot-Marie-Tooth peripheral sensorimotor polyneuropathy with characteristics of a mild phenotype, onset during the second decade of life and very slow progression, caused by mutations in the *GDAP1* gene" (Orphanet, cited via [MedGen C1842984](https://www.ncbi.nlm.nih.gov/medgen/C1842984)).

**Key identifiers:**
| Resource | Identifier |
|---|---|
| OMIM (phenotype, AR/AD CMT2K) | #607831 — "Charcot-Marie-Tooth disease, axonal, type 2K" |
| OMIM (gene, *GDAP1*) | *606598 |
| MONDO | MONDO:0011916 (Charcot-Marie-Tooth disease axonal type 2K) — per [GenCC](https://thegencc.org/genes/HGNC:15968) |
| HGNC | HGNC:15968 (*GDAP1*) |
| MedGen | C1842984 (autosomal dominant CMT2K) / C1842983 |
| GTR (NIH Genetic Testing Registry) | C1842983 |
| Gene locus | 8q21.11 |

**Synonyms:** Charcot-Marie-Tooth disease, axonal, type 2K; CMT2K; hereditary motor and sensory neuropathy, axonal, GDAP1-related (GDAP1-HMSN); AD-CMT2K (to distinguish from AR-CMT2K).

**Data derivation.** Information below is aggregated from disease-level curated resources (OMIM, Orphanet, GeneReviews) and case series/cohort literature (individual patients and families), which is the norm for a rare Mendelian neuropathy; it is not derived from large-scale EHR/claims data.

---

## 2. Etiology

**Disease causal factor:** Monogenic — heterozygous (dominant) pathogenic missense variants in *GDAP1* (8q21.11), encoding a mitochondrial outer-membrane fission protein expressed mainly in neurons.

**Genetic risk factors (causal variants):**
- **p.Arg120Trp (R120W; c.358C>T)** — the most recurrent dominant variant. "This pathogenic mutation is the most common variant seen within CMT2K" and "was identified in affected members of 3 unrelated families with dominant inheritance of axonal CMT" ([PMC9637907](https://pmc.ncbi.nlm.nih.gov/articles/PMC9637907/); PMID:36353131).
- **p.His123Arg (H123R)** — the Finnish founder dominant CMT2K mutation.
- **p.Thr157Pro** — reported de novo in a proband (GeneReviews).
- **p.Glu222Lys** — notable for segregating with *both* AR and AD disease in different families, illustrating incomplete penetrance/dosage effects at this residue (GeneReviews).
- **p.Gly271Arg and p.Ala336Ser** — heterozygous missense variants reported in a 2022 series of families with mild, late-onset sensory-predominant neuropathy (PMID:35656516; [PMC9155904](https://pmc.ncbi.nlm.nih.gov/articles/PMC9155904/)).
- Over 80 pathogenic *GDAP1* variants have been catalogued overall (deletions, insertions, nonsense, missense, splice-site), most causing recessive disease; the dominant subset is restricted almost entirely to missense substitutions clustering around specific structural hinges (see Mechanism, §6) (GeneReviews; [PMC9249340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9249340/)).

**Environmental/lifestyle risk factors:** None established as disease-causing; as with other axonal CMT subtypes, neurotoxic agents (e.g., vincristine and other peripheral-neurotoxic chemotherapeutics) are a general precaution in any CMT patient because of reduced neuronal reserve, but no *GDAP1*-specific environmental trigger has been reported in the literature reviewed.

**Protective factors:** None specific to CMT2K identified in the literature surveyed; general modifiers of severity (see below) are genetic rather than environmental.

**Gene-environment interaction:** Not established; the dominant phenotype is attributed to a cell-autonomous, dominant-negative biochemical mechanism (impaired mitochondrial fusion — see §6) rather than to gene-environment interplay.

**Modifiers / phenotype variability drivers:**
- **Reduced penetrance** is a hallmark of dominant *GDAP1* disease: "several heterozygotes reported to be mildly affected or asymptomatic at an advanced age," with documented intrafamilial variability (GeneReviews, NBK1539).
- Some heterozygous carriers in the 2022 cohort were asymptomatic, "perhaps due to incomplete penetrance or the nature of the heterozygous form" (PMID:35656516).

---

## 3. Phenotypes

CMT2K (dominant) is predominantly a **length-dependent, sensorimotor axonal polyneuropathy**, but reported severity spans from a minimally symptomatic, late-onset pure sensory neuropathy to (rarely) rapidly progressive, wheelchair-dependent disease with respiratory compromise.

### Core phenotype panel

| Phenotype | Type | Onset/Course | Frequency/Notes | Suggested HP term |
|---|---|---|---|---|
| Distal lower-limb weakness | Clinical sign | Childhood–late adulthood; slow, "generally remain ambulatory" | Most common initial manifestation is gait difficulty | HP:0002460 (Distal muscle weakness) |
| Difficulty walking / gait abnormality | Symptom | Presenting symptom in most cases | Common initial complaint | HP:0001288 (Gait disturbance) |
| Distal upper-limb weakness/atrophy | Clinical sign | Later, milder than lower limb | "restricted to distal muscles of the upper and lower limbs" | HP:0009053 (Mild upper limb muscle weakness) / HP:0003693 |
| Distal sensory loss (pinprick, vibration) | Clinical sign | Often the dominant/only feature in late-onset cases | Present even in minimally symptomatic carriers | HP:0002936 (Distal sensory impairment) |
| Paresthesias / burning or numb feet | Symptom | Frequently the presenting complaint in the mild late-onset form | PMID:35656516 | HP:0040083 (Paresthesia) / HP:0025438 (Burning sensation) |
| Absent/diminished deep tendon reflexes (especially ankle) | Clinical sign | Progressive with disease duration | Present even with normal NCS in some carriers | HP:0001265 (Hyporeflexia) / HP:0001284 (Areflexia) |
| Normal reflexes (in minimally affected carriers) | Clinical sign | Subclinical/mild carriers | "normal reflexes in four out of five subjects" in the heterozygous-variant cohort | — |
| No pes cavus | Clinical sign | Distinguishes dominant CMT2K from many other CMT subtypes | Consistently reported absent in the mild dominant form | (absence of HP:0001761) |
| Vocal cord paresis / dysphonia | Clinical sign | Uncommon in dominant form (in contrast to recessive CMT4A/AR-CMT2K), but reported in isolated dominant cases | GeneReviews; case reports | HP:0001612 (Hoarse voice) / HP:0001611 |
| Dysautonomia | Clinical sign | Rare, isolated dominant cases | GeneReviews | HP:0002960 (Autonomic dysfunction) |
| Rapidly progressive weakness (atypical) | Clinical course | Reported in a single 63-year-old male, 6th-decade rapid decline to wheelchair within ~1 year | "our patient's rapidly progressive disease in his 6th decade of life is a unique presentation of CMT2K" (PMID:36353131) | HP:0003676 (Progressive) |
| Diaphragmatic/respiratory involvement | Clinical sign (rare) | Atypical, in the same severe R120W case: BIPAP-dependent respiratory failure, hypercapnia/hypoxemia, elevated hemidiaphragm | "rapidly progressive restrictive pulmonary impairment secondary to diaphragmatic nerve dysfunction" (PMID:36353131) | HP:0002093 (Respiratory insufficiency) / HP:0009088 |
| Mild/normal electrodiagnostic findings | Laboratory (EMG/NCS) | Common in late-onset carriers | "Electrodiagnostic testing was normal in one of five individuals," others showed only minor reduced sensory amplitudes (ulnar, peroneal) | Not an HP phenotype term per se — see Diagnostics |
| Asymptomatic carrier state | — | Reduced penetrance | Documented in multiple pedigrees | HP:0025303 (Clinical variability) |

**Age of onset:** Highly variable — "onset varies from childhood to late adulthood" — but the dominant form is enriched for **late-onset presentations after age 40**, in contrast to the recessive form's early-childhood (<3 years) onset described for the OMIM #607831 entry when caused by biallelic variants ([Orphanet](https://www.orpha.net); GeneReviews).

**Severity/progression:** Predominantly **mild, slowly progressive**; most patients remain ambulatory lifelong. A minority (isolated case reports) show a more severe, rapidly progressive course with atypical bulbar/respiratory features overlapping with the recessive CMT4A phenotype (PMID:36353131), underscoring caution against assuming dominant *GDAP1* disease is always benign.

**Quality of life:** Not separately quantified with EQ-5D/SF-36 instruments in *GDAP1*-specific dominant cohorts in the literature surveyed; general CMT QOL literature (not disease-specific) documents impact on mobility, hand function, and fatigue, but this was not confirmed for CMT2K specifically in the sources reviewed.

---

## 4. Genetic/Molecular Information

**Causal gene:** *GDAP1* (HGNC:15968; OMIM *606598), chromosome 8q21.11, 6 exons, encoding a 358-amino-acid tail-anchored mitochondrial outer-membrane protein.

**Variant classification/type:** Dominant CMT2K is caused almost exclusively by **heterozygous missense variants** (ACMG class: pathogenic/likely pathogenic for well-characterized alleles such as R120W — "classified as pathogenic (ACMG class 5)," PMID:36353131). No dominant-negative truncating or null alleles have been robustly implicated — consistent with a gain-of-abnormal-function/dominant-negative mechanism rather than haploinsufficiency (see §6).

**Key pathogenic variants (dominant):**
| Variant (protein) | cDNA | Notes |
|---|---|---|
| p.R120W | c.358C>T | Most common dominant allele; multiple unrelated families; also reported as a severe/atypical outlier case |
| p.H123R | — | Finnish founder mutation |
| p.T157P | — | De novo case |
| p.E222K | — | Segregates with AR *and* AD disease in different pedigrees |
| p.G271R | c.811G>A | Mild, late-onset sensory-predominant phenotype |
| p.A336S | c.1006G>T | Variant of uncertain significance in the same cohort |

**Allele frequency:** Specific population-database (gnomAD) frequencies for individual dominant alleles were not directly retrieved in this pass of the literature; as private/founder mutations in a rare disease, they are expected to be extremely rare or absent from gnomAD, consistent with pathogenicity.

**Somatic vs. germline:** Germline only; no somatic mosaicism specifically reported in the literature surveyed, though de novo germline origin has been documented (p.T157P).

**Functional consequence:** **Dominant-negative interference with mitochondrial fusion.** "Dominantly inherited disease mutants (dmGDAP1) interfere with mitochondrial fusion," in contrast to recessive loss-of-function mutants, which reduce mitochondrial fission activity; the dominant mechanism yields "disturbed mitochondrial membrane potential and increased ROS levels" (search synthesis of PMID:19782751 and related structural work; [EMBO Rep. mechanistic literature](https://ncbi.nlm.nih.gov/pmc/articles/PMC3674444)).

**Modifier genes:** None specifically established for *GDAP1*-CMT2K in the sources reviewed; phenotypic variability is attributed to allele-specific structural effects and incomplete penetrance rather than a defined modifier locus.

**Epigenetics / chromosomal abnormalities:** No epigenetic mechanism or chromosomal-rearrangement mechanism has been reported for CMT2K; disease is driven by point (missense) variants.

**Protein structure and mutation mechanism** (structural biology, PMID for [PMC9249340](https://pmc.ncbi.nlm.nih.gov/articles/PMC9249340/)):
- GDAP1 adopts a glutathione-S-transferase (GST)-like fold: an N-terminal GST-like domain (GSTL-N), a C-terminal GST-like domain (GSTL-C), a dimer interface, a hydrophobic domain (HD1), and a C-terminal transmembrane tail-anchor (TA) domain that targets the protein to the mitochondrial outer membrane.
- A distinguishing structural feature is helix α6, which "breaks in the middle around Asp200," conferring conformational flexibility important for dimerization/function.
- CMT-causing mutations cluster spatially around the hydrophobic core and the α3–α6–α7 helix interaction network rather than at a single linear hotspot.
- **R120W**: "the α3 helix, carrying Trp120, moves outward by ~1 Å, and the contact with the neighboring α6 is weakened" — destabilizing without abolishing overall fold; thermal melting temperature drops >5°C versus wild-type.
- **H123R**: disrupts a His123–Tyr124 π-orbital interaction, similarly destabilizing without gross misfolding — consistent with a "poison subunit" dominant-negative model, since these mutant proteins retain enough structure to dimerize with wild-type GDAP1 and interfere with its function, rather than being simply degraded.

---

## 5. Environmental Information

No specific environmental toxin, occupational exposure, or infectious trigger has been established as a cause or exacerbating factor for CMT2K in the literature surveyed. As for CMT broadly, clinicians commonly counsel caution with peripheral-neurotoxic agents (e.g., vincristine, certain other chemotherapeutics) given reduced neuronal/axonal reserve, but this is a general CMT precaution rather than *GDAP1*-specific evidence from the sources reviewed. No infectious agent is implicated.

---

## 6. Mechanism / Pathophysiology

### Causal chain (dominant *GDAP1*-CMT2K)

1. A heterozygous missense variant (e.g., p.R120W, p.H123R) in *GDAP1* **destabilizes the α3–α6–α7 helical interaction network** of the GST-like fold without abolishing overall protein folding (demonstrated structurally: reduced thermal stability, altered helix packing) → *[demonstrated in vitro, PMC9249340]*.
2. The mutant GDAP1 protein is still trafficked to, and inserted in, the mitochondrial outer membrane via its C-terminal tail-anchor domain, and **retains the ability to dimerize with wild-type GDAP1** (heterodimerization) → this is inferred from the dominant inheritance pattern and biochemical data, i.e., a "poison subunit"/dominant-negative model rather than simple haploinsufficiency.
3. Heterodimerization of mutant with wild-type GDAP1 **interferes with mitochondrial fusion machinery**, in contrast to recessive loss-of-function alleles, which instead reduce GDAP1's normal pro-fission activity → "dominantly inherited disease mutants (dmGDAP1) interfere with mitochondrial fusion" while "recessively inherited disease mutants (rmGDAP1) show reduced mitochondrial fragmentation activity" (mechanistic literature synthesis, PMC3674444 and related).
4. Impaired fusion (dominant) or impaired fission (recessive) both converge on **disturbed mitochondrial network dynamics**, leading to **disturbed mitochondrial membrane potential and increased reactive oxygen species (ROS)** production, and increased sensitivity to apoptotic stimuli → demonstrated in cell models (HeLa cells expressing R120W show impaired fusion, mitochondrial fragmentation, increased apoptotic susceptibility).
5. In neurons specifically — which rely heavily on long-range, activity-coupled mitochondrial trafficking and quality control along the axon — this **mitochondrial dysfunction propagates to disrupted ER–mitochondria contact sites, altered store-operated calcium entry (SOCE), and reduced cytosolic calcium signaling** in motor neurons and DRG neurons, based on *Gdap1*-knockout mouse work (which models the recessive/complete-loss mechanism but illuminates the shared downstream neuronal consequences): "motor neurons showed reduced cytosolic calcium and SOCE response" and "decreased ER-Ca²⁺ levels along with a defect on store-operated calcium entry (SOCE) related to a misallocation of mitochondria to subplasmalemmal sites" (PMC4393229; PLoS Genetics 2015).
6. Downstream ultrastructural correlates in patient-derived motor neurons (hiPSC model, homozygous variant): **swollen, disorganized mitochondrial cristae** and **elevated superoxide anion levels despite preserved bulk ATP production** — indicating oxidative-stress-driven dysfunction that is dissociable from energy failure — plus **cytoplasmic lipid droplet accumulation**, suggesting disrupted lipid/β-oxidation handling (PMC8393985).
7. Chronic mitochondrial/ER-calcium dysfunction and oxidative stress in the distal axon and neuromuscular junction lead to **progressive length-dependent axonal degeneration**, evidenced in the knockout mouse by "progressive loss of motor neurons in the anterior horn of the spinal cord and defects in neuromuscular junctions" as well as reduced acetylated (stabilized) α-tubulin and increased autophagic vesicles in cultured neurons (PMC4393229).
8. Axonal loss in the longest peripheral nerves (feet/legs first, by length-dependence) → **clinical manifestation**: distal sensorimotor polyneuropathy — distal weakness, atrophy, sensory loss, and hyporeflexia, with the dominant-allele phenotype typically milder and slower than the biallelic/recessive form because dominant alleles only partially perturb fusion (via heterodimerization with residual wild-type protein), whereas complete loss (recessive) more severely deranges fission — a difference in degree rather than in the affected downstream pathway (inferred synthesis; the branch point between mild-dominant vs. severe-recessive phenotype severity is a matter of degree of mitochondrial dynamic perturbation, not yet fully quantified head-to-head in the literature reviewed).
9. **Branch — atypical severe presentations**: in rare dominant cases (e.g., the R120W patient with rapid 6th-decade decline and respiratory failure, PMID:36353131), the same fusion-interference mechanism is inferred to more aggressively affect phrenic/vagal motor axons, producing diaphragmatic weakness and vocal cord dysfunction typically associated with the recessive CMT4A phenotype — the authors explicitly note this "challenges current understanding" of dominant-vs-recessive phenotype segregation, i.e., this branch is a clinical observation without an established distinct molecular explanation.

### Mechanism categories

- **Molecular pathway:** Mitochondrial fission/fusion dynamics (GDAP1 acts upstream of the core fission machinery — Drp1/DNM1L and Mff-dependent) — GDAP1-induced fission "depends on the integrity of its hydrophobic domain 1, and on Drp1 and Mff, demonstrating that GDAP1 influences fission upstream of the conserved basic fission machinery."
- **Cellular process:** Altered mitochondrial fission/fusion balance; oxidative stress; disrupted store-operated calcium entry (SOCE); altered autophagy (increased autophagic vesicles); apoptotic susceptibility.
- **Protein dysfunction:** Dominant-negative structural destabilization causing altered protein-protein interaction (heterodimerization poisoning wild-type function) rather than loss of the protein itself.
- **Metabolic changes:** Preserved bulk ATP production in at least one hiPSC motor-neuron model, but with elevated ROS — indicating the metabolic lesion is one of redox handling and quality control rather than gross energy failure, at least in that model.
- **Tissue damage mechanism:** Oxidative stress, disrupted mitochondrial quality control, axonal (dying-back) degeneration.
- **Cell types/anatomical involvement:** Lower motor neurons (anterior horn cells), dorsal root ganglion sensory neurons, peripheral motor and sensory axons, neuromuscular junctions.

**Suggested GO terms:** GO:0000266 (mitochondrial fission), GO:0090140 (regulation of mitochondrial fission), GO:0008053 (mitochondrial fusion), GO:0034599 (cellular response to oxidative stress), GO:0006816 (calcium ion transport), GO:1901339 (regulation of store-operated calcium entry), GO:0031090 (organelle membrane).

**Suggested CL terms:** CL:0000100 (motor neuron), CL:0000029 (neural crest-derived dorsal root ganglion sensory neuron)/CL:0000561 (amine precursor uptake and decarboxylation cell — not applicable; better: CL:0000097 sensory neuron), CL:0000186 (myofibroblast — not applicable).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Peripheral nervous system — motor and sensory nerves of the extremities (length-dependent, feet/lower legs first, then hands). Body system: nervous system (peripheral).
- **Secondary/rare involvement:** Respiratory system via phrenic nerve/diaphragm dysfunction (atypical severe cases); vocal cords via recurrent laryngeal nerve involvement (rare, atypical dominant cases; more typical of the recessive CMT4A phenotype).
- **Tissue/cell level:** Peripheral nerve axons (motor and sensory), anterior horn motor neurons of the spinal cord, dorsal root ganglion sensory neurons, neuromuscular junctions, distal skeletal muscle (secondary denervation atrophy).
- **Subcellular level:** Mitochondria (outer membrane — site of GDAP1 localization; cristae architecture is disrupted), endoplasmic reticulum (ER-mitochondria contact sites, altered Ca²⁺ handling), cytoskeleton (reduced acetylated α-tubulin, implying microtubule stability changes relevant to axonal transport).
- **Suggested UBERON terms:** UBERON:0001017 (central nervous system — not primary), UBERON:0000010 (peripheral nervous system), UBERON:0001456 (sciatic nerve, representative long nerve), UBERON:0002021 (anterior horn of spinal cord), UBERON:0000044 (dorsal root ganglion).
- **Suggested GO Cellular Component terms:** GO:0005741 (mitochondrial outer membrane), GO:0005739 (mitochondrion), GO:0005791 (rough endoplasmic reticulum — for ER-mitochondria contacts, GO:0044233 ER-mitochondrion membrane contact site).
- **Laterality:** Bilateral, generally symmetric, length-dependent (distal-to-proximal gradient).

---

## 8. Temporal Development

- **Onset:** Highly variable — from childhood through late adulthood; the dominant form is notably enriched for onset after age 40, sometimes presenting as an isolated mild sensory neuropathy discovered incidentally or via family screening. Onset pattern is typically insidious/chronic rather than acute.
- **Progression:** Classically **very slow**; "affected persons generally remain ambulatory" throughout life. Contrast with recessive CMT2K/CMT4A, which progresses to wheelchair dependence by the second decade in many cases.
- **Disease course pattern:** Chronic, progressive (not relapsing-remitting); a minority of dominant cases show unusually rapid, aggressive progression (case report: gait difficulty to wheelchair-bound within one year, then respiratory failure) — an important outlier to document for genotype-phenotype counseling.
- **Duration:** Lifelong, non-remitting.
- **Critical periods / remission:** No spontaneous remission reported; no defined critical therapeutic window identified in the literature (no disease-modifying therapy currently exists — see Treatment).

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal dominant (this entry); note *GDAP1* is one of the few CMT genes producing disease in both dominant and recessive configurations, and even the *same* residue (E222K) can appear in either an AD or AR pedigree.
- **Penetrance:** **Reduced/incomplete.** GeneReviews explicitly documents heterozygotes who are "mildly affected or asymptomatic at an advanced age," and a 2022 cohort reports asymptomatic carriers among five clinically evaluated heterozygotes.
- **Expressivity:** Markedly **variable**, both between and within families (intrafamilial variability documented), ranging from asymptomatic/subclinical carriers to typical mild axonal CMT to (rarely) severe, rapidly progressive disease with respiratory failure.
- **Genetic anticipation:** Not reported for *GDAP1*-CMT2K (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically documented in the sources reviewed, though de novo germline variants occur (p.T157P).
- **Founder effects:** Yes — p.H123R is a well-described **Finnish founder mutation**; p.R120W recurs across multiple unrelated Spanish/other European families, consistent with either a founder effect or a mutational hotspot (not fully disambiguated in the sources reviewed).
- **Consanguinity:** Not a factor for the dominant form specifically (relevant instead to the recessive form).
- **Carrier frequency:** Not established at a population level; dominant *GDAP1* variants are private/rare and not routinely reported in population carrier-frequency databases.

**Epidemiology:**
- CMT overall: incidence ~1/2,500; prevalence ~36/100,000 in the US, ~2.8 million patients worldwide (general CMT statistics, not GDAP1-specific).
- *GDAP1* mutations (all inheritance patterns combined) are **rare** in most Western cohorts — "quite rare in Western countries, accounting for less than 1% of the genetically defined CMT patients in most clinical series" — but show marked geographic enrichment:
  - Spain and Italy: up to ~10% of genetically diagnosed axonal CMT in certain regions.
  - A mixed cohort of 160 CMT patients: *GDAP1* prevalence 5.6% overall, 21.4% of CMT2 (axonal) cases.
  - Brazil: 7.14% of axonal CMT cases.
  - China: 1.63% prevalence.
- The dominant subset specifically is a minority of all *GDAP1* cases (most *GDAP1* disease is recessive), but a precise population prevalence figure specific to *dominant* CMT2K was not identified in the literature surveyed — flag as **data not available** for a precise number.
- **Sex ratio / geographic distribution:** No specific male:female skew reported (autosomal, not X-linked); geographic clustering as above reflects founder/regional allele distribution rather than a demographic risk factor.

---

## 10. Diagnostics

- **Clinical tests:**
  - **Nerve conduction studies (NCS)/EMG:** Axonal pattern (reduced compound motor/sensory amplitudes with relatively preserved conduction velocities), but can be **subtly abnormal or entirely normal** in mildly affected dominant carriers — "electrodiagnostic testing was normal in one of five individuals," with others showing only minor reduced sensory amplitudes in ulnar and peroneal nerves (PMID:35656516). This is diagnostically important: normal NCS does not exclude dominant *GDAP1* disease.
  - **Neurological examination:** Distal weakness/atrophy, diminished pinprick and vibration sense, absent/diminished ankle reflexes; notably **absence of pes cavus** in the dominant form (a distinguishing feature from many other CMT subtypes where cavus foot is prominent).
- **Genetic testing:**
  - Because CMT is genetically heterogeneous (>100 causal genes), the standard approach is a **multi-gene CMT/hereditary neuropathy panel** or exome/genome sequencing, rather than single-gene *GDAP1* testing as first line — though single-gene testing is appropriate when family-specific variant is known or phenotype (axonal CMT with prior family diagnosis) strongly suggests *GDAP1*.
  - Chromosomal microarray, karyotyping, and mitochondrial DNA testing are not relevant (this is a nuclear point-mutation disorder).
- **Biopsy/pathology:** Not routinely required for diagnosis given availability of genetic testing; historical sural nerve biopsy in axonal CMT shows axonal loss without significant demyelination/onion-bulb formation (a general CMT2-category finding, not *GDAP1*-specific data retrieved here).
- **Differential diagnosis:** Other axonal CMT2 subtypes (CMT2A/*MFN2*, CMT2B/*RAB7A*, CMT2E/*NEFL*, etc.), other hereditary sensory neuropathies (e.g., *TRPV4*-related), and acquired axonal polyneuropathies (diabetic, toxic, paraneoplastic) — especially relevant when the presentation is a late-onset, mild, sensory-predominant neuropathy without a strong family history, given reduced penetrance can obscure an apparent inheritance pattern.
- **Screening:** No population/newborn screening program exists for CMT2K; cascade testing of at-risk relatives is standard once a familial variant is identified, though genetic counseling must account for reduced penetrance (an apparently "negative" family history does not exclude an at-risk relative).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No disease-specific mortality data were identified; CMT2K (dominant) is not generally considered life-shortening, though the rare severe/rapidly progressive phenotype with respiratory failure (case report) illustrates that respiratory compromise, if it occurs, is a potential source of serious morbidity/mortality risk requiring monitoring (BIPAP support was required in the reported case).
- **Morbidity/function:** Most patients remain ambulatory for life with mild-to-moderate distal weakness and sensory loss; functional impact is generally modest compared to recessive *GDAP1* disease or other severe CMT subtypes.
- **Complications:** Falls/gait instability from distal weakness and sensory ataxia; in atypical severe cases, respiratory insufficiency and bulbar (vocal cord) dysfunction.
- **Prognostic factors:** Specific variant may correlate loosely with severity (e.g., R120W has been reported in both typical mild and one atypical severe case, indicating variant identity alone is an incomplete predictor); family history/penetrance pattern; age of onset (later onset broadly associates with milder course in the literature surveyed, though this is not rigorously quantified).
- **Prognostic biomarkers:** None validated/established specific to *GDAP1*-CMT2K in the sources reviewed.

---

## 12. Treatment

**No disease-modifying or curative therapy currently exists for CMT2K** (or for CMT generally as of the most recent literature reviewed): "Although there is still no approved drug therapy for Charcot-Marie-Tooth disease, several experimental therapies – pharmacological or based on gene therapy/silencing – are under investigation" (2025 review literature).

- **Pharmacotherapy:** Symptomatic only — e.g., neuropathic pain management (gabapentinoids, duloxetine — general neuropathic pain agents, not *GDAP1*-specific trial data identified). No approved CMT2K-specific drug. NCIT: `NCIT:C15986` (Pharmacotherapy) for symptomatic agents as used.
- **Supportive/rehabilitative care** (mainstay of management):
  - Physical therapy (`NCIT:C15302`) and occupational therapy (`NCIT:C121351`) to maintain strength, mobility, and hand function.
  - Orthotic management (ankle-foot orthoses) for foot drop/gait instability.
  - Pain management, psychosocial support, and genetic counseling (`NCIT:C15240`).
- **Surgical/interventional:** Orthopedic surgery (`NCIT:C16186`) reserved for secondary foot deformity or contracture in more affected individuals; not typically needed in mild dominant CMT2K given absence of pes cavus.
- **Respiratory support:** In the rare severe/atypical case, non-invasive ventilation (BIPAP) was required for restrictive respiratory failure secondary to diaphragmatic nerve dysfunction (`NCIT:C15747`, Supportive Care) (PMID:36353131).
- **Experimental/investigational (CMT-wide, not CMT2K-specific approvals):**
  - Gene therapy programs are advancing for other specific CMT subtypes — e.g., a Phase I/II gene therapy trial for CMT4J is anticipated to begin dosing patients in early-to-mid 2026 (Elpida Therapeutics), and CRISPR-based strategies are in development for CMT2A (*MFN2*) — but **no *GDAP1*-targeted gene therapy or gene-silencing program was identified** in the literature surveyed.
  - The **INSPIRE trial**, a placebo-controlled study of a pharmacological candidate in CMT2 patients, reported interim improvement in CMT Health Index scores and MRI evidence of slowed disease progression over two years in 15 patients — general CMT2 population, not confirmed *GDAP1*/CMT2K-specific enrollment in the source reviewed.
  - General CMT clinical-trial landscape (rehabilitation interventions, e.g., NCT07726043 for CMT1A) is broader than CMT2K and largely subtype-agnostic for supportive-care trials.
- **Treatment algorithm:** Multidisciplinary neuromuscular clinic model — neurology, physical/occupational therapy, orthopedics as needed, genetic counseling, and (in severe/atypical cases) pulmonology for respiratory monitoring.
- **Personalized medicine:** Not yet applicable at a treatment level (no genotype-guided therapy exists for *GDAP1*-CMT2K); genotype is used for diagnostic/prognostic/counseling purposes.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense for a monogenic dominant disorder (no modifiable risk-factor avoidance prevents disease occurrence in a carrier); reproductive options (preimplantation genetic diagnosis, prenatal testing) are available once a familial pathogenic variant is identified, guided by genetic counseling given the autosomal dominant inheritance and 50% transmission risk to offspring.
- **Secondary prevention:** Early identification via cascade genetic testing of at-risk relatives (important given reduced penetrance — a negative clinical exam does not exclude carrier status) allows early counseling, monitoring, and avoidance of peripheral-neurotoxic exposures.
- **Tertiary prevention:** Regular monitoring for gait/fall risk, orthotic intervention to prevent secondary contractures/deformity, and (given the rare but real possibility of atypical severe/respiratory presentations) clinical vigilance for unexpected rapid progression or respiratory symptoms even in a nominally "mild" dominant CMT2K family.
- **Genetic counseling:** Central to management — explaining autosomal dominant inheritance, 50% offspring risk, but critically **counseling on reduced penetrance and highly variable expressivity**, since some carriers remain asymptomatic lifelong while rare individuals (even with the same variant, e.g., R120W) can have unexpectedly severe courses.
- **Public health/environmental interventions:** Not applicable (not an environmentally driven or infectious disease).

---

## 14. Other Species / Natural Disease

- No naturally occurring veterinary (companion animal or livestock) *GDAP1*-CMT2K disease was identified in the literature surveyed (contrast with some other CMT genes, e.g., *SH3TC2*, which have recognized dog homologs); this appears to be primarily a human genetic disease studied through engineered animal and cellular models rather than naturally occurring veterinary disease.
- **Orthologous gene:** *Gdap1* is conserved in mouse (Mus musculus, NCBI Taxon:10090), zebrafish, and Drosophila (*dGdap1*), enabling the model-organism work summarized below.

---

## 15. Model Organisms

| Model | Type | Key findings | Fidelity/limitations |
|---|---|---|---|
| **Gdap1 knockout mouse** (PMC4393229 / PLoS Genetics 2015) | Genetic (complete knockout — models recessive/severe loss, not the dominant heterozygous mechanism directly) | Abnormal motor behavior from 3 months of age; axonal (not demyelinating) neuropathy confirmed electrophysiologically/biochemically; progressive anterior horn motor neuron loss; neuromuscular junction defects; enlarged/defective mitochondria and altered ER cisternae in cultured motor and DRG neurons; reduced acetylated α-tubulin; increased autophagy vesicles; reduced cytosolic Ca²⁺ and impaired SOCE, linked to mitochondrial mislocalization away from subplasmalemmal sites | High construct validity for GDAP1 loss-of-function biology broadly, but models the recessive/null mechanism rather than the dominant-negative heterozygous missense mechanism specific to CMT2K — an important translational caveat when citing this model for the dominant phenotype |
| **hiPSC-derived motor neurons** from a patient with a homozygous *GDAP1* variant (PMC8393985) | Cellular (iPSC-derived) | 80–90% *GDAP1* mRNA degraded via nonsense-mediated decay; disrupted/swollen mitochondrial cristae by EM; elevated superoxide despite preserved ATP; cytoplasmic lipid droplet accumulation | Homozygous/severe genotype (not the heterozygous dominant genotype); human genetic background is a strength, but again models loss-of-function rather than dominant-negative missense mechanism |
| ***Drosophila* Gdap1 models** | Genetic (knockdown and overexpression) | Both knockdown and overexpression of dGdap1 reduce climbing ability (a locomotor readout); knockdown causes mitochondrial aggregation and large, elongated mitochondria in muscle | Useful for rapid mechanistic/genetic-interaction screening; limited translational relevance to human peripheral nerve-specific pathology given Drosophila's different nervous system architecture |
| **Cell-based dominant-mutant expression models** (e.g., R120W expressed in HeLa cells) | Cellular (overexpression) | Impaired mitochondrial fusion, mitochondrial fragmentation, increased apoptotic sensitivity — directly models the dominant-negative mechanism | Heterologous non-neuronal cell line; does not capture neuron-specific axonal transport or length-dependent degeneration biology |

**Key gap:** Most detailed mechanistic animal/cellular modeling available in the literature surveyed addresses **recessive/loss-of-function *GDAP1* biology** (knockout mouse, homozygous-variant hiPSC neurons); direct heterozygous dominant-negative missense (R120W/H123R-equivalent) knock-in animal models were not identified in this search pass, representing a documented gap between the dominant human phenotype and available in vivo disease models — relevant to a `HUMAN_MODEL_MISMATCH`-type consideration if used to populate `modeled_mechanisms` links in a dismech-style pathophysiology model (fidelity should be flagged accordingly since these models best support the shared *downstream* mitochondrial/calcium pathway rather than the *dominant-negative fusion-interference* trigger step itself, which is currently supported chiefly by cell-culture overexpression data).

---

## Summary of Suggested Ontology Terms

- **Genes:** GDAP1 (hgnc:15968)
- **HP terms (see §3 table):** HP:0002460, HP:0001288, HP:0002936, HP:0040083, HP:0001265, HP:0001284, HP:0001612, HP:0002960, HP:0003676, HP:0002093, HP:0025303
- **GO terms:** GO:0000266, GO:0090140, GO:0008053, GO:0034599, GO:0006816, GO:1901339
- **CL terms:** CL:0000100 (motor neuron), CL:0000097 (sensory neuron)
- **UBERON terms:** UBERON:0000010 (peripheral nervous system), UBERON:0001456, UBERON:0002021, UBERON:0000044
- **NCIT (treatment) terms:** NCIT:C15986, NCIT:C15302, NCIT:C121351, NCIT:C16186, NCIT:C15747, NCIT:C15240
- **MONDO:** MONDO:0011916

---

## Notes on Evidence Gaps

- Precise **population prevalence** of the dominant CMT2K subtype specifically (as opposed to all-inheritance-combined *GDAP1* prevalence) was **not available** in the sources reviewed.
- **gnomAD population allele frequencies** for specific dominant alleles (R120W, H123R) were not directly retrieved in this pass and should be verified via direct gnomAD/ClinVar query before curation.
- **QOL instrument data** (EQ-5D/SF-36) specific to CMT2K were not identified; general CMT QOL literature exists but was not confirmed as CMT2K-specific.
- The **OMIM #607831 full entry text** could not be fetched directly in this session (proxy connection refused to omim.org); the OMIM-derived claims above are sourced from search-result snippets and secondary literature that cite OMIM, and the full primary OMIM entry should be consulted directly during curation to confirm and supplement detail (particularly the complete variant table and allelic-disorder cross-references).

---

### Sources

- [GDAP1-Related Hereditary Motor and Sensory Neuropathy — GeneReviews (NBK1539)](https://www.ncbi.nlm.nih.gov/books/NBK1539/)
- [OMIM #607831 — Charcot-Marie-Tooth Disease, Axonal, Type 2K](https://omim.org/entry/607831)
- [OMIM *606598 — GDAP1](https://omim.org/entry/606598)
- [Autosomal dominant GDAP1 mutation with severe phenotype and respiratory involvement: A case report (PMID:36353131 / PMC9637907)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9637907/)
- [Mild Late-Onset Sensory Neuropathy Associated with Heterozygous Missense GDAP1 Variants (PMID:35656516 / PMC9155904)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9155904/)
- [Structural insights into Charcot–Marie–Tooth disease-linked mutations in human GDAP1 (PMC9249340)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9249340/)
- [A locus-specific database for mutations in GDAP1 allows analysis of genotype-phenotype correlations in CMT4A and 2K (PMC3313893)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3313893/)
- [Dominant GDAP1 mutations cause predominantly mild CMT phenotypes (Cassereau et al., Neurology 2011)](https://www.researchgate.net/publication/51489536_Dominant_GDAP1_mutations_cause_predominantly_mild_CMT_phenotypes)
- [Charcot-Marie-Tooth disease-associated mutants of GDAP1 dissociate its roles in peroxisomal and mitochondrial fission (PMC3674444)](https://ncbi.nlm.nih.gov/pmc/articles/PMC3674444)
- [Lack of GDAP1 Induces Neuronal Calcium and Mitochondrial Defects in a Knockout Mouse Model of CMT Neuropathy (PMC4393229)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4393229/)
- [CMT-linked loss-of-function mutations in GDAP1 impair store-operated Ca²⁺ entry (PMC5318958)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5318958/)
- [GDAP1 Involvement in Mitochondrial Function and Oxidative Stress, hiPSC-Derived Motor Neuron CMT Model (PMC8393985)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8393985/)
- [GDAP1 mutations are frequent among Brazilian patients with autosomal recessive CMT (NMD Journal)](https://www.nmd-journal.com/article/S0960-8966(21)00069-9/abstract)
- [Distribution and genotype-phenotype correlation of GDAP1 mutations (Sci Rep 2017)](https://www.nature.com/articles/s41598-017-06894-6)
- [Charcot-Marie-Tooth disease: a review of clinical management (2025 review)](https://www.tandfonline.com/doi/full/10.1080/14737175.2025.2470980)
- [Developing a gene therapy for Charcot-Marie-Tooth disease: progress (PMC12118428)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12118428/)
- [Clinical trials in Charcot-Marie-Tooth disorders: a retrospective and preclinical assessment (PMC10556688)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10556688/)
- [Recent Advances in Drosophila Models of Charcot-Marie-Tooth Disease](https://www.researchgate.net/publication/345816568_Recent_Advances_in_Drosophila_Models_of_Charcot-Marie-Tooth_Disease)
- [Mitochondrial defects and neuromuscular degeneration caused by altered expression of Drosophila Gdap1](https://www.researchgate.net/publication/264795140_Mitochondrial_defects_and_neuromuscular_degeneration_caused_by_altered_expression_of_Drosophila_Gdap1_Implications_for_the_Charcot-Marie-Tooth_neuropathy)
- [GDAP1 gene — GenCC](https://thegencc.org/genes/HGNC:15968)
- [Autosomal dominant Charcot-Marie-Tooth disease type 2K — MedGen C1842984](https://www.ncbi.nlm.nih.gov/medgen/C1842984)
- [Charcot-Marie-Tooth disease axonal type 2K — GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1842983/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 8 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

5 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:36353131`: "was identified in affected members of 3 unrelated families with dominant inheritance of axonal CMT"
  - closest text in source: "A survey of the patient's family history also revealed an extensive incidence of CMT consistent with an autosomal dominant inheritance pattern"
- `PMC:PMC9637907`: "was identified in affected members of 3 unrelated families with dominant inheritance of axonal CMT"
  - closest text in source: "A survey of the patient's family history also revealed an extensive incidence of CMT consistent with an autosomal dominant inheritance pattern"
- `PMID:35656516` *(abstract only)*: "perhaps due to incomplete penetrance or the nature of the heterozygous form"
  - closest text in source: "This study presents the clinical and electrophysiological findings of four subjects with a pathogenic heterozygous GDAP1 variant causing Charcot-Marie-Tooth disease 2K (CMT2K) and one additional subject with an uncertain GDAP1 variant and clinical findings of CMT 2K"
- `PMID:36353131`: "our patient's rapidly progressive disease in his 6th decade of life is a unique presentation of CMT2K"
  - closest text in source: "Although the clinical phenotype within CMT genotypes may differ between individuals in one family, this patient's rapidly progressive disease in his 6th decade of life is a unique presentation of CMT2K"
- `PMID:19782751` *(abstract only)*: "disturbed mitochondrial membrane potential and increased ROS levels"
  - closest text in source: "Only the expression of dmGDAP1s increases the production of ROS, leads to uneven mitochondrial transmembrane potentials, and enhances the susceptibility to apoptotic stimuli"
- `PMC:PMC3674444` *(abstract only)*: "disturbed mitochondrial membrane potential and increased ROS levels"
  - closest text in source: "GDAP1 is a tail-anchored protein of mitochondria and induces mitochondrial fragmentation"
- `PMC:PMC3674444` *(abstract only)*: "recessively inherited disease mutants (rmGDAP1) show reduced mitochondrial fragmentation activity"
  - closest text in source: "Mutations in GDAP1 lead to Charcot-Marie-Tooth disease (CMT), an inherited peripheral neuropathy, and affect mitochondrial dynamics"
- `PMC:PMC4393229` *(abstract only)*: "decreased ER-Ca²⁺ levels along with a defect on store-operated calcium entry (SOCE) related to a misallocation of mitochondria to subplasmalemmal sites"
  - closest text in source: "GDAP1 silencing in vitro reduces Ca2+ inflow through store-operated Ca2+ entry (SOCE) upon mobilization of endoplasmic reticulum (ER) Ca2+, likely in association with an abnormal distribution of the mitochondrial network"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 24 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025303` (2 mentions) - the report calls it "Clinical variability"; HP calls it **Episodic**
- `CL:0000097` (2 mentions) - the report calls it "sensory neuron"; CL calls it **mast cell**
- `UBERON:0001456` (2 mentions) - the report calls it "sciatic nerve, representative long nerve"; UBERON calls it **face**
- `UBERON:0002021` (2 mentions) - the report calls it "anterior horn of spinal cord"; UBERON calls it **occipital lobe**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0025438` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0040083` (obsolete Toe walking) (2 mentions) - replaced by `HP:0030051`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002960` (2 mentions) - the report calls it "Autonomic dysfunction"; HP calls it **Autoimmunity**, and lists "Autoimmune condition" among its other names
- `GO:1901339` (2 mentions) - the report calls it "regulation of store-operated calcium entry"; GO calls it **regulation of store-operated calcium channel activity**
- `CL:0000029` (1 mention) - the report calls it "neural crest-derived dorsal root ganglion sensory neuron"; CL calls it **neural crest derived neuron**
- `CL:0000186` (1 mention) - the report calls it "myofibroblast — not applicable"; CL calls it **myofibroblast cell**
- `UBERON:0001017` (1 mention) - the report calls it "central nervous system — not primary"; UBERON calls it **central nervous system**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.