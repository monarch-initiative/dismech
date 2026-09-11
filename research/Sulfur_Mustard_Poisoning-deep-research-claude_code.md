---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-10T19:07:19.276633'
end_time: '2026-09-10T19:11:54.763776'
duration_seconds: 275.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Sulfur Mustard Poisoning
  mondo_id: MONDO:0800387
  category: Environmental
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
  web_search_requests: 22
  num_turns: 25
  total_cost_usd: 1.5186775999999997
  session_id: 9e69cc81-c7bf-5849-9c45-54bef1e4f4c3
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 55
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 29
  on_topic: 15
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 8
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: CHEBI:25434
    reported_labels:
    - bis
    ontology_label: bis(2-chloroethyl) sulfide
  - term_id: HP:0000508
    reported_labels:
    - photophobia
    ontology_label: Ptosis
  - term_id: HP:0000534
    reported_labels:
    - corneal neovascularization
    ontology_label: Abnormal eyebrow morphology
  - term_id: HP:0000585
    reported_labels:
    - dry eye
    ontology_label: Band keratopathy
  - term_id: HP:0000523
    reported_labels:
    - blindness, severe cases
    ontology_label: Subcapsular cataract
  - term_id: HP:0025406
    reported_labels:
    - blistering
    ontology_label: Asthenia
  - term_id: CL:0000312
    reported_labels:
    - Cell types/GO/CL involvement to annotate:** keratinocytes
    ontology_label: keratinocyte
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sulfur Mustard Poisoning
- **MONDO ID:** MONDO:0800387 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Sulfur Mustard Poisoning** covering all of the
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

# Sulfur Mustard Poisoning: Comprehensive Research Report

## 1. Disease Information

**Overview.** Sulfur mustard (SM; bis(2-chloroethyl) sulfide, "mustard gas," military designations H/HD/HT) is a bifunctional alkylating vesicant chemical warfare agent. It is an oily, colorless-to-brown liquid at room temperature with a faint garlic/onion/horseradish odor, first synthesized in the 19th century and weaponized by German forces at Ypres, Belgium in July 1917 ([Britannica](https://www.britannica.com/science/mustard-gas); [Science History Institute](https://www.sciencehistory.org/stories/magazine/a-brief-history-of-chemical-war/)). It produces delayed chemical burns of skin, eyes, and airway mucosa, with cellular injury occurring within minutes of contact but clinical symptom onset delayed 1–24 hours ([ATSDR MMG](https://wwwn.cdc.gov/tsp/MMG/MMGDetails.aspx?mmgid=924&toxid=191)). It is classified by the CDC/NIOSH as a "blister agent" and is a documented human carcinogen ([ATSDR ToxFAQs](https://www.atsdr.cdc.gov/toxfaqs/tfacts49.pdf)).

**Key identifiers:**
- **MONDO:** MONDO:0800387 — "sulfur mustard poisoning" ([Monarch Initiative](https://monarchinitiative.org/MONDO:0800387))
- **MeSH:** D009151 — Mustard Gas
- **ChEBI:** CHEBI:25434 — bis(2-chloroethyl) sulfide ([ChEBI](https://www.ebi.ac.uk/chebi/searchId.do?printerFriendlyView=true&chebiId=25434&structureView=))
- **CAS Registry Number:** 505-60-2
- **Chemical formula:** C₄H₈Cl₂S; molar mass 159.07 g/mol; IUPAC name 1-chloro-2-[(2-chloroethyl)sulfanyl]ethane ([Wikipedia](https://en.wikipedia.org/wiki/Bis(2-chloroethyl)sulfide); [PubChem CID 10461](https://pubchem.ncbi.nlm.nih.gov/compound/Mustard-gas))
- **ICD-10:** No dedicated T-code found specific to sulfur mustard in the standard T51-T65 "toxic effects of nonmedicinal substances" chapter searched; this warrants curator follow-up against ICD-10-CM/ICD-11 poisoning-by-warfare-agent codes rather than T57.1 (phosphorus), which several search hits mistakenly returned.
- **Synonyms:** Mustard gas, yperite (from Ypres), Lost (German), H, HD (distilled mustard), HT (mustard-T mixture), Kampstoff "Lost," agent HD.

**Data provenance for a KB entry:** Evidence is a mix of (a) aggregated disease/toxicology-database content (ATSDR Toxicological Profile, NIOSH/CDC cards, ICSC/CAMEO chemical safety sheets) and (b) primary clinical literature derived largely from cohorts of individual patients — WWI/WWII munitions workers, and above all decades of longitudinal follow-up of Iranian veterans exposed during the 1980–88 Iran–Iraq War, plus case series from the Syrian civil war (2015–2017) and the 1988 Halabja attack on Iraqi Kurds. Unlike most dismech entries, there is essentially no genetic-disease literature (OMIM/ClinVar) — this is a toxicological/environmental-exposure entry, and "genetic" content is limited to host susceptibility polymorphisms (see §4).

---

## 2. Etiology

**Causal factor.** Sulfur mustard poisoning has a single, sufficient environmental/toxic cause: dermal, ocular, inhalational, or (rarely) oral exposure to sulfur mustard itself, as a liquid, vapor, or aerosol. There is no infectious or purely genetic form.

**Risk factors (exposure-modifying, not disease-causing):**
- **Route and dose:** Liquid contact causes more severe cutaneous injury than vapor; inhalation of concentrated vapor produces more severe airway injury. Moist, thin-skinned, and occluded body regions (axillae, groin, perineum, flexural creases) are most vulnerable ([Britannica](https://www.britannica.com/science/mustard-gas)).
- **Ambient temperature/humidity:** Higher temperature and humidity increase both vapor pressure and percutaneous penetration.
- **Delay to decontamination:** Effective decontamination is time-critical — benefit is greatest within 1–2 minutes and is markedly reduced after that window ([ATSDR MMG](https://wwwn.cdc.gov/tsp/MMG/MMGDetails.aspx?mmgid=924&toxid=191)).
- **Genetic susceptibility (host modifier, not cause):** Glutathione S-transferase (GST) null genotypes (GSTM1, GSTT1) reduce endogenous antioxidant/detoxification capacity and are hypothesized modifiers of individual variability in oxidative injury severity, by analogy with other oxidative-stress exposures ([ScienceDirect, GSTM1 null genotype](https://www.sciencedirect.com/science/article/abs/pii/S0300483X00003589)); direct SM-specific GSTM1 association studies were not identified in this search and should be flagged as inferred-by-analogy rather than SM-specific evidence.
- **Occupational exposure:** WWI/WWII mustard-agent manufacturing plant workers experienced chronic low-level exposure with elevated later-life cancer risk ([NCBI Bookshelf, Veterans at Risk](https://www.ncbi.nlm.nih.gov/books/NBK236053/)).

**Protective factors:** No genetic protective variant is established. The only validated protective factors are pre-exposure avoidance/PPE and rapid post-exposure decontamination (see §13); several chemical prophylactic/cytoprotectant candidates (DRDE-07 analogues, amifostine, N-acetylcysteine, vitamin D) show pre-clinical protection when administered before or immediately after exposure but none is a licensed prophylactic ([Journal of Applied Toxicology 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12209742/)).

**Gene-environment interaction:** The clearest documented interaction is pharmacogenomic/enzymatic rather than germline-disease-causing: GST and glutathione-peroxidase pathway capacity determines how effectively an individual detoxifies the reactive sulfonium intermediate and resulting reactive oxygen species, directly shaping lesion severity — "GSH depletion induced by GSR downregulation may be a major mechanism of SM toxicity on human lung. Despite overexpression of GSTs and GPXs genes, GSH depletion may decline the productivity of these enzymes" ([PubMed 29676192](https://pubmed.ncbi.nlm.nih.gov/29676192/)).

---

## 3. Phenotypes

Phenotypes are organized by organ system and by acute vs. chronic/delayed timing. Frequencies below (e.g., "75–90% ocular involvement") come from large cohort follow-up of chemically injured populations, chiefly Iranian war veterans.

### Ocular (suggested HP root: HP:0000478 Abnormality of the eye)
- **Acute keratoconjunctivitis:** Severe eye pain, photophobia, blepharospasm, excessive lacrimation, conjunctival injection, corneal epithelial defects — onset after a several-hour latent period; seen in **75–90%** of exposed individuals, making the eye the single most susceptible tissue ([PMC 9348212](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9348212/)).
- **Delayed/chronic mustard gas keratopathy** (onset years to decades later, after a "silent" period): limbal stem cell deficiency, corneal neovascularization, corneal opacification/scarring, persistent epithelial defects, dry eye, chronic blepharitis. In one cohort of 48 chronic/delayed patients: limbal ischemia in 81.3%, corneal scarring/opacity in 87.5%, neovascularization in 70.8%, corneal thinning in 58.3%; 64.6% had chronic-form, 35.4% delayed-onset lesions ([PubMed 15808253](https://pubmed.ncbi.nlm.nih.gov/15808253/); [Frontiers Toxicol 2023](https://www.frontiersin.org/journals/toxicology/articles/10.3389/ftox.2023.1281041/full)). Suggested HP terms: HP:0000508 (photophobia), HP:0000534 (corneal neovascularization), HP:0007957 (corneal opacity), HP:0000585 (dry eye), HP:0000523 (blindness, severe cases).

### Cutaneous (HP:0000951 Abnormality of the skin)
- **Erythema** at 2–24h, progressing to **vesication/bullae** by 24–48h, then denudation and slow-healing burn-like ulcers ([Britannica](https://www.britannica.com/science/mustard-gas)). Suggested terms: HP:0025637/erythema, HP:0025406 (blistering).
- **Chronic/delayed skin findings:** hyper- and hypopigmentation (melanocyte injury — low SM concentrations cause hyperpigmentation, high concentrations decrease melanin content producing hypopigmented patches: [PubMed 31785464](https://pubmed.ncbi.nlm.nih.gov/31785464/)), chronic pruritic dermatitis, scarring, and elevated risk of basal cell and squamous cell carcinoma at exposure sites in chronically/occupationally exposed cohorts ([NCBI Bookshelf NBK236053](https://www.ncbi.nlm.nih.gov/books/NBK236053/)).

### Respiratory (HP:0002086 Abnormality of the respiratory system) — dominant cause of late mortality
- **Acute:** rhinorrhea, sneezing, sore throat, hoarseness, non-productive cough (6–24h), progressing to productive cough, tracheobronchitis, and in severe inhalational exposure, pseudomembrane formation, ARDS ([ATSDR MMG](https://wwwn.cdc.gov/tsp/MMG/MMGDetails.aspx?mmgid=924&toxid=191)).
- **Chronic/delayed (occurs in ~42.5% of exposed veterans, with expectoration in ~53% and cough in ~72% of a symptomatic sub-cohort):** chronic bronchitis, bronchiectasis, asthma, bronchiolitis obliterans, large-airway narrowing/tracheobronchial stenosis, air trapping, and pulmonary fibrosis — these worsen progressively over decades, sometimes emerging in survivors with no initial acute distress ([PubMed 23735551](https://pubmed.ncbi.nlm.nih.gov/23735551/); [Health Science Reports 2026](https://onlinelibrary.wiley.com/doi/10.1002/hsr2.72791); [SAGE 2018](https://journals.sagepub.com/doi/full/10.1177/0960327117694072)). Suggested HP terms: HP:0006536 (chronic pulmonary obstruction), HP:0002110 (bronchiectasis), HP:0006536-adjacent obliterative bronchiolitis (map via HP or SNOMED as ontology permits), HP:0002204 (pulmonary fibrosis).

### Hematologic/Immunologic
- Bone marrow suppression and lymphoid aplasia after significant systemic absorption — historically among the most feared acute complications, predisposing to sepsis ([HealthTree summary](https://healthtree.org/blood-cancer/community/articles/history-of-mustardgas-weapon-to-chemo)).

### Gastrointestinal
- Nausea, vomiting, diarrhea/GI cramping; pathologically, acute hemorrhagic gastroduodenitis, desquamative enteritis, and severe hemorrhagic necrotic colitis in severe systemic poisoning ([NCBI Bookshelf NBK600756](https://www.ncbi.nlm.nih.gov/books/NBK600756/)).

### Neuropsychiatric
- Acute: CNS excitation with convulsions reported in severely poisoned, hospitalized Iranian veterans. Chronic: anxiety, depression, apathy, cognitive decline documented decades after exposure ([NCBI Bookshelf NBK600756](https://www.ncbi.nlm.nih.gov/books/NBK600756/)); animal aggregate-culture data show progressive demyelination ([ScienceDirect S0161813X21000279](https://www.sciencedirect.com/science/article/abs/pii/S0161813X21000279)).

**Quality of life impact:** Chronic mustard lung and mustard keratopathy are the two dominant drivers of long-term disability in surviving cohorts, with progressive dyspnea, exercise limitation, recurrent pulmonary infection, and visual impairment/blindness reported even decades post-exposure ([Health Science Reports 2026](https://onlinelibrary.wiley.com/doi/10.1002/hsr2.72791)).

---

## 4. Genetic/Molecular Information

Sulfur mustard poisoning is not a Mendelian disease; there is no single causal gene. Relevant "genetic" content for a KB entry is limited to:

- **Host susceptibility/modifier genes** — glutathione-pathway genes: **GSTM1**, **GSTT1**, **GSTP1**, **GSTA1** (null/deletion genotypes reduce detoxification capacity for the SM-derived reactive electrophile and its downstream ROS burden) and **GSR** (glutathione reductase; downregulation implicated in lung GSH depletion, [PubMed 29676192](https://pubmed.ncbi.nlm.nih.gov/29676192/)).
- **DNA repair machinery engaged by SM-induced lesions**, functioning as biological response modifiers rather than disease genes: base excision repair (BER), nucleotide excision repair (NER) — the pathway classically responsible for repairing bulky guanine-N7 alkyl adducts and crosslinks — homologous recombination (HR), and non-homologous end joining (NHEJ) ([ScienceDirect S138266891830019X](https://www.sciencedirect.com/science/article/abs/pii/S138266891830019X)). **PARP1** (poly-ADP-ribose polymerase) is centrally implicated as a molecular switch between apoptotic and necrotic cell death depending on the degree of DNA damage and consequent NAD+/ATP depletion ([Journal of Investigative Dermatology](https://www.jidonline.org/article/S0022-202X(15)41498-8/fulltext); [Archives of Toxicology](https://link.springer.com/article/10.1007/s00204-007-0265-7)).
- **Late-effect gene expression changes documented in exposed lung tissue:** overexpression of **FOXM1** (Forkhead Box M1) and **APOE** (Apolipoprotein E) — both lung-cancer-development-associated genes — in bronchial tissue of long-term SM-exposed patients, suggesting a mechanistic bridge from chronic SM airway injury to carcinogenesis ([PMC 5843310](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5843310/)).
- **No pathogenic germline variant, ClinVar entry, or chromosomal syndrome** is associated with SM poisoning susceptibility as a primary disease mechanism; this section should be modeled in a dismech entry as environmental etiology with modifier-gene annotations, not as `genetic:` causal drivers.
- **Epigenetics:** No SM-specific DNA methylation/DiseaseMeth signature was identified in this search; this is a plausible gap for future literature mining given the agent's direct genotoxicity.

---

## 5. Environmental Information

- **Primary environmental factor:** Direct chemical exposure to sulfur mustard itself, via liquid contact, vapor inhalation, or (rarely) ingestion of contaminated water/food, in a military, terrorist, or industrial-accident context. ECTO-style exposure_term candidates: "exposure to sulfur mustard" (a chemical warfare agent exposure).
- **Contexts of exposure documented in the literature:**
  - **WWI battlefield use** (from July 1917), causing >120,000 casualties with a low (~2–3%) mortality rate but very high morbidity and prolonged hospitalization ([Science History Institute](https://www.sciencehistory.org/stories/magazine/a-brief-history-of-chemical-war/)).
  - **Iran–Iraq War (1980–1988):** the largest-scale, best-studied modern exposure, tens of thousands of Iranian combatants exposed, forming the basis of most long-term natural-history data used in this report.
  - **Halabja chemical attack (16 March 1988):** Iraqi forces used sulfur mustard together with sarin, tabun, and VX against the Kurdish town of Halabja; estimated 3,200–5,000 killed and 7,000–10,000 injured, with documented long-term chronic respiratory disease, cancer, infertility, miscarriage, and congenital-abnormality excess in survivors ([Wikipedia](https://en.wikipedia.org/wiki/Halabja_massacre)).
  - **Syrian civil war (2015–2017):** OPCW-UN Joint Investigative Mechanism confirmed ISIL/Da'esh use of sulfur mustard at Marea (Sept 2015, 11 confirmed cases) and Umm Hawsh (Sept 2016) ([UN Press](https://press.un.org/en/2017/sc13060.doc.htm); [Chemistry World](https://www.chemistryworld.com/news/chemical-weapons-watchdog-concludes-islamic-state-used-mustard-gas-in-2015-attack-in-syria/4019064.article)).
  - **Occupational exposure:** WWI/WWII-era mustard-manufacturing plant workers, with elevated later-life respiratory and skin cancer incidence.
- **Lifestyle/co-factors:** Tobacco smoking is expected to compound chronic bronchitis/COPD-type outcomes in SM-exposed airway disease, though a dedicated SM+smoking interaction study was not retrieved in this search and should be verified before citing.
- **Infectious agents:** Not a primary etiology, but chronic SM-damaged airway epithelium and bone-marrow suppression predispose to secondary bacterial pneumonia and recurrent respiratory infection.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Dermal, ocular, or inhalational contact with sulfur mustard** leads to rapid intracellular formation of a highly reactive cyclic **episulfonium (ethylene sulfonium) ion** via intramolecular cyclization, the agent's actual alkylating electrophile ([ScienceDirect S138266891830019X](https://www.sciencedirect.com/science/article/abs/pii/S138266891830019X)).
2. This electrophile **alkylates nucleophilic sites in DNA, RNA, and proteins**, predominantly at the **N7 position of guanine**, and — because SM is bifunctional (two reactive chloroethyl arms) — can react with **two nucleophiles simultaneously**, forming **intrastrand and interstrand DNA crosslinks**; guanine–cytosine interstrand crosslinks are the most cytotoxic lesion class.
3. DNA crosslinks **physically block DNA replication and transcription**, leading to **cell-cycle arrest (G1 or G2/M)**; when a replication fork collides with an unrepaired crosslink this **results in DNA double-strand breaks**.
4. Accumulated single- and double-strand breaks **trigger hyperactivation of PARP1**, which consumes **NAD+** as substrate for poly-ADP-ribosylation of damaged chromatin.
5. Severe PARP1 overactivation **depletes cellular NAD+ and, consequently, ATP** (NAD+ is required for glycolytic ATP generation), which **shifts the cell death mode from apoptosis to necrosis** — mild DNA damage/PARP activation permits apoptotic or reparative outcomes, while severe damage causes energy-collapse necrosis and overt tissue vesication ([J Invest Dermatol](https://www.jidonline.org/article/S0022-202X(15)41498-8/fulltext); [PMC 2993477](https://pmc.ncbi.nlm.nih.gov/articles/PMC2993477/)).
6. In parallel, SM **depletes intracellular glutathione (GSH)** both by direct conjugation and by downregulation of **GSR** (glutathione reductase), **impairing the cell's principal antioxidant buffer** and permitting accumulation of **reactive oxygen species (ROS)** — this oxidative-stress arm is a mechanism largely independent of, but synergistic with, the DNA-alkylation arm ([PubMed 29676192](https://pubmed.ncbi.nlm.nih.gov/29676192/)).
7. Necrotic/damaged keratinocytes, airway epithelial cells, and corneal epithelium **release a burst of pro-inflammatory mediators within 72 hours** — IL-1α, IL-1β, IL-6, IL-8, TNF-α, CCL2, CCL3, CCL11, CXCL1 — **which drives neutrophilic and (in chronic phase) Th17-dependent T-cell infiltration** into affected tissue, particularly the lung ([PMC 3340497](https://pmc.ncbi.nlm.nih.gov/articles/PMC3340497/); [PMC review](https://www.sciencedirect.com/science/article/pii/S0009279726002875)).
8. At the **dermal-epidermal junction**, alkylation-driven cell death and protease release (basal keratinocyte injury near the hemidesmosome) **causes epidermal-dermal separation, producing the characteristic delayed vesicle/bulla** — clinically apparent 12–48h after exposure, despite molecular injury occurring within minutes.
9. In the **airway**, direct epithelial alkylation plus the inflammatory cascade **causes acute mucosal sloughing, pseudomembrane formation, and — in severe cases — acute lung injury/ARDS**; over subsequent weeks to years, **persistent T-cell/Th17-driven inflammation and impaired epithelial repair lead to chronic bronchitis, bronchiolitis obliterans, bronchiectasis, and progressive pulmonary fibrosis** — this delayed/chronic arm is the dominant driver of long-term mortality (see §11).
10. In the **eye**, corneal limbal epithelial and stem-cell injury, together with chronic low-grade inflammation, **produces limbal stem cell deficiency**, which over a "silent" period of years to decades **can result in delayed-onset corneal neovascularization, scarring, and opacification** — the delayed mustard-gas keratopathy syndrome. The mechanistic link between the acute limbal insult and the multi-decade latency is inferred from clinical natural-history data rather than fully demonstrated at the cell-biology level.
11. Chronically injured, hyperproliferative, and DNA-damage-repair-taxed epithelium (skin and lung) is at elevated long-term risk of **malignant transformation**, consistent with SM's classification as a human carcinogen; **FOXM1 and APOE overexpression** in chronically exposed bronchial tissue is one documented molecular correlate of this progression toward lung cancer, and **fibrotic/air-trapping/bronchiectatic HRCT findings independently predict later lung-tumor development** (relative risk 11.73× for air trapping, 10.14× for bronchiectasis, 17.75× for pulmonary fibrosis in a 719-patient, four-decade follow-up cohort — [PMC 9764821](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9764821/)).

### Mechanism categories (checklist detail)

- **Molecular pathways:** DNA alkylation/crosslinking (BER/NER/HR/NHEJ engagement); PARP1–NAD+–ATP energy-collapse axis; glutathione/GST/GPx antioxidant pathway depletion; NF-κB-driven pro-inflammatory cytokine transcription.
- **Cellular processes (suggested GO terms):** apoptosis (GO:0006915), necrosis, DNA damage response (GO:0006974), oxidative stress response (GO:0006979), inflammatory response (GO:0006954), neutrophil chemotaxis.
- **Protein dysfunction:** direct alkylation of cysteine/histidine/methionine residues in structural and enzymatic proteins (e.g., epidermal creatine kinase, albumin, hemoglobin — see §10 biomarkers) causes loss of normal protein function and forms stable covalent adducts used diagnostically.
- **Metabolic changes:** NAD+/ATP depletion (glycolytic collapse) secondary to PARP1 hyperactivation; documented reduction in NAD+ levels and glucose uptake in cultured human epidermal cells exposed to SM ([ScienceDirect 0041008X89901439](https://www.sciencedirect.com/science/article/abs/pii/0041008X89901439)).
- **Immune involvement:** acute neutrophilic inflammation; chronic **Th17-cell-dependent** lung inflammation implicated in bronchiolitis obliterans pathogenesis ([PMC 3340497](https://pmc.ncbi.nlm.nih.gov/articles/PMC3340497/)); IL-6 serum levels correlate with severity of pulmonary complications ([PMC 4100050](https://pmc.ncbi.nlm.nih.gov/articles/PMC4100050/)); bone marrow/lymphoid aplasia after high systemic exposure causes secondary immunodeficiency.
- **Tissue damage mechanisms:** oxidative stress (GSH depletion), alkylation-driven cytotoxicity, epidermal-dermal separation (vesication), progressive fibrosis (lung, and fibrotic scarring in cornea/skin).
- **Cell types/GO/CL involvement to annotate:** keratinocytes (CL:0000312), corneal/limbal epithelial and limbal stem cells, airway/bronchial epithelial cells, alveolar macrophages, neutrophils, Th17 CD4+ T cells, melanocytes (pigmentary changes), vascular endothelial cells (documented SM-induced apoptosis/necrosis, [ScienceDirect S0041008X96903245](https://www.sciencedirect.com/science/article/abs/pii/S0041008X96903245)), hematopoietic stem/progenitor cells in bone marrow.

---

## 7. Anatomical Structures Affected

- **Primary organs:** skin (integumentary system), eyes/cornea, upper and lower respiratory tract (trachea, bronchi, bronchioles, alveoli).
- **Secondary/systemic involvement:** bone marrow/hematopoietic system (suppression at high systemic dose), gastrointestinal tract (mucosal injury), central nervous system (excitotoxic/demyelinating effects at high systemic exposure), reproductive system (teratogenic/reproductive-toxicant evidence, mixed).
- **Body systems:** integumentary, ocular, respiratory, hematologic/immune, gastrointestinal, nervous, reproductive.
- **Tissue/cell level:** epidermal keratinocytes and basal layer (dermal-epidermal junction), corneal/limbal epithelium and limbal stem cell niche, bronchial/bronchiolar/alveolar epithelium, vascular endothelium, melanocytes, bone marrow hematopoietic progenitors.
- **Suggested UBERON terms:** UBERON:0000014 (zone of skin), UBERON:0001772 (cornea), UBERON:0002185 (bronchus), UBERON:0002048 (lung), UBERON:0002371 (bone marrow).
- **Subcellular level (GO Cellular Component):** nucleus/chromatin (site of DNA crosslinking), mitochondria (secondary energy-collapse effects downstream of NAD+ depletion), plasma membrane (initial site of lipophilic agent penetration).
- **Localization:** Skin lesions are typically localized to exposed and moist/occluded areas (face, neck, axillae, groin) and can be unilateral/patchy depending on liquid-contact geometry; ocular and respiratory involvement is typically bilateral given vapor/aerosol exposure.

---

## 8. Temporal Development

- **Onset:** Acute — hours after a single significant exposure (latent period 1–24h depending on tissue and dose); this is not a developmental/congenital disease.
- **Onset pattern:** Acute chemical-burn injury with a **delayed clinical manifestation** relative to the moment of true cellular injury — a defining and clinically important feature of SM toxicology (injury begins within minutes; symptoms begin hours later).
- **Disease stages:** (1) acute phase (hours–days: erythema, vesication, keratoconjunctivitis, tracheobronchitis, possible bone marrow suppression); (2) subacute/recovery phase (weeks–months); (3) chronic phase — persistent smoldering disease in a minority; (4) **delayed-onset phase**, in which new pathology (mustard-gas keratopathy, progressive bronchiolitis obliterans/fibrosis) can emerge **years to decades** after an apparently symptom-free "silent" interval ([PMC 9348212](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9348212/); [SAGE 2018, 3 decades post-exposure](https://journals.sagepub.com/doi/full/10.1177/0960327117694072)).
- **Progression rate:** Variable — pulmonary and ocular delayed sequelae are typically slowly progressive over years, sometimes worsening even in patients with no acute distress at time of exposure.
- **Disease course pattern:** Can be self-limited (mild acute exposure with full healing) or chronic/progressive (bronchiolitis obliterans, pulmonary fibrosis, delayed keratopathy) — a bimodal natural history that is unusual among toxic exposures and important to capture structurally (e.g., via `progression:` phases keyed to "acute," "chronic," "delayed").
- **Critical periods:** The first 1–2 minutes post-exposure is the single most important intervention window (decontamination efficacy), and the first several days post-exposure is the key window for antioxidant/anti-inflammatory pharmacologic intervention before secondary inflammatory injury becomes established.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Not applicable — this is an acquired toxic exposure, not a Mendelian or polygenic inherited disease. No penetrance, expressivity, anticipation, mosaicism, founder-effect, or carrier-frequency concepts apply in the classical genetic-disease sense.
- **Epidemiology:**
  - Historically the most casualty-producing chemical warfare agent: **>120,000 WWI casualties**, though with a low ~2–3% direct mortality rate given open-air battlefield dilution ([Science History Institute](https://www.sciencehistory.org/stories/magazine/a-brief-history-of-chemical-war/)).
  - **Halabja (1988):** 3,200–5,000 deaths, 7,000–10,000 injured (mixed sulfur mustard/nerve agent attack) ([Wikipedia](https://en.wikipedia.org/wiki/Halabja_massacre)).
  - **Iran–Iraq War cohort:** tens of thousands of Iranian veterans exposed; a 39-year mortality study of 48,067 chemical-warfare survivors recorded 4,342 deaths (9.03%), with mortality significantly higher in exposed vs. non-exposed groups (42.28 vs. 34.51 deaths/10,000); severe lung lesions carried the highest organ-specific mortality (87.49/10,000), confirming pulmonary damage as more lethal than skin or eye lesions ([PMC 10835181](https://pmc.ncbi.nlm.nih.gov/articles/PMC10835181/)).
  - Pulmonary involvement prevalence among exposed veterans ≈**42.5%** ([PubMed 23735551](https://pubmed.ncbi.nlm.nih.gov/23735551/)).
- **Population demographics:** Affected populations are exposure-defined (military combatants, civilians in attack zones, occupational manufacturing workers) rather than ethnically/genetically defined. Documented cohorts: Iranian (Iran-Iraq war), Iraqi Kurdish (Halabja), Syrian civilian (2015–2017 ISIL attacks), and WWI/WWII Allied and Axis combatants/munitions workers.
- **Sex ratio:** In the 39-year mortality cohort, males had higher mortality (38.7/10,000) than females (34.18/10,000), though this likely reflects predominance of male combatant exposure rather than a true biological sex-susceptibility difference ([PMC 10835181](https://pmc.ncbi.nlm.nih.gov/articles/PMC10835181/)).
- **Age distribution:** Mortality increases markedly with age at follow-up (67.07/10,000 in the 60+ group vs. 24.67/10,000 in under-51s), consistent with cumulative chronic organ damage compounding with normal aging ([PMC 10835181](https://pmc.ncbi.nlm.nih.gov/articles/PMC10835181/)).

---

## 10. Diagnostics

- **Clinical diagnosis** is primarily based on exposure history plus the characteristic delayed vesicant burn/keratoconjunctivitis/tracheobronchitis triad; there is no single confirmatory bedside clinical criterion set analogous to DSM/consensus criteria for a genetic syndrome.
- **Laboratory/biomarker confirmation** — four biomarker classes are used, most validated in confirmed clinical exposure cases:
  1. **Hydrolysis/oxidation products** of SM in blood/urine (short detection window).
  2. **β-lyase urinary metabolites** (e.g., thiodiglycol-derived metabolites).
  3. **DNA adducts** — immunochemical detection of the **N7-guanine adduct**; detectable in urine for up to **~30 days** post-exposure.
  4. **Protein/hemoglobin adducts** — GC-MS analysis of the N-terminal valine adduct in globin (after modified Edman degradation) or LC-MS/MS of modified hemoglobin sites; detectable for **>90 days**, making this the longest-window biomarker. Alkylated epidermal creatine kinase has also been evaluated as a skin-specific biomarker compared with albumin/DNA adducts ([PMC 8032612](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8032612/)).
  - Biomarker concentration correlates with clinical severity ([PubMed 28962267](https://pubmed.ncbi.nlm.nih.gov/28962267/); [ATSDR Analytical Methods](https://www.atsdr.cdc.gov/toxprofiles/tp49-c7.pdf)).
- **Imaging:** High-resolution CT (HRCT) of the chest is the diagnostic modality of choice for delayed pulmonary complications, characteristically showing chronic bronchitis, air trapping, bronchiectasis, large-airway narrowing, and pulmonary fibrosis ([PubMed 23735551](https://pubmed.ncbi.nlm.nih.gov/23735551/)).
- **Ophthalmic exam:** Slit-lamp examination for corneal scarring, neovascularization, limbal ischemia, and epithelial defects is the standard diagnostic approach for both acute and delayed keratopathy.
- **Pulmonary function testing:** Spirometry (obstructive pattern in bronchiolitis obliterans/bronchiectasis) tracked longitudinally in treated cohorts (see §12).
- **Genetic testing:** Not applicable as a diagnostic modality for the underlying exposure, though GST genotyping could theoretically be used as a research tool for susceptibility stratification (no established clinical use identified).
- **Differential diagnosis:** Thermal/chemical burns from other agents (lewisite, phosgene oxime — other vesicants), other causes of ARDS, other causes of keratoconjunctivitis, idiopathic/other-etiology bronchiolitis obliterans (e.g., post-transplant, connective-tissue-disease-associated), other causes of aplastic anemia.
- **Screening:** Not a heritable/population-screenable disease; "screening" in this context means biomonitoring of at-risk exposed populations (e.g., post-incident cohort surveillance) rather than newborn/carrier/prenatal screening.

---

## 11. Outcome/Prognosis

- **Mortality:** Acute battlefield mortality historically low (~2–3%) given open-air dilution, but long-term mortality is significantly elevated in exposed vs. unexposed veteran cohorts over decades of follow-up (42.28 vs. 34.51 deaths/10,000 in the 39-year study). **Severe pulmonary lesions are the single strongest predictor of death** (87.49 deaths/10,000), exceeding skin or eye lesion severity ([PMC 10835181](https://pmc.ncbi.nlm.nih.gov/articles/PMC10835181/)).
- **Morbidity:** Chronic bronchitis, bronchiectasis, bronchiolitis obliterans, and pulmonary fibrosis are the dominant drivers of long-term disability, with progressive dyspnea being the most consistently reported chronic symptom (72% cough, 53% expectoration in one series). Mustard-gas keratopathy is the dominant driver of long-term visual disability.
- **Complications:** Secondary bacterial pneumonia (from damaged airway epithelium and marrow-suppression-related immunodeficiency), lung and skin cancer (from chronic genotoxic injury), recurrent corneal ulceration/infection, blindness in severe keratopathy.
- **Recovery potential:** Mild acute exposures generally heal fully; a subset of patients develop the chronic/delayed disease phenotypes described above regardless of acute severity, making individual prognostication difficult at time of initial injury.
- **Prognostic/predictive imaging findings:** In a 719-patient, four-decade follow-up, HRCT findings independently predicted later lung cancer development — air trapping (RR 11.73), bronchiectasis (RR 10.14), and pulmonary fibrosis (RR 17.75, the strongest single predictor) — establishing a structural pathophysiology → malignancy pathway that a dismech entry should model explicitly ([PMC 9764821](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9764821/)).
- **Quality of life:** Long-term SM survivors report persistent impact on daily functioning from chronic dyspnea and visual impairment; psychological morbidity (anxiety, depression, cognitive decline) is also a documented long-term burden.

---

## 12. Treatment

**There is no validated specific antidote or curative therapy for sulfur mustard poisoning** — management is supportive/symptomatic, aimed at limiting secondary injury and treating downstream chronic complications ([PubMed 31576778](https://pubmed.ncbi.nlm.nih.gov/31576778/); [Journal of Applied Toxicology 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12209742/): "there are still no recommended in vivo treatments or repair mechanisms for SM-induced toxicity or mortality to this day").

- **Acute/emergency management (NCIT: Supportive Care, NCIT:C15747):**
  - Immediate **decontamination** (soap and copious low-pressure water irrigation for ≥10–15 minutes, or until skin pH normalizes) is the single most effective acute intervention; Fuller's Earth and Reactive Skin Decontamination Lotion (RSDL) both show significant lesion-size reduction in pig-model comparisons ([ScienceDirect S0009279721000296](https://www.sciencedirect.com/science/article/abs/pii/S0009279721000296)).
  - Sodium thiosulfate infusion (100–500 mg/kg/min) has been used if started within ~60 minutes of exposure, though it is not a validated specific antidote.
  - Respiratory support (supplemental oxygen, mechanical ventilation for severe cases), analgesia, fluid resuscitation, infection prophylaxis, and burn-style wound dressing (NCIT:C15747, supportive/burn care).
- **Pharmacotherapy (NCIT:C15986):**
  - **N-acetylcysteine (NAC)** — the most extensively studied adjunct, raises intracellular GSH and supports glutathione-S-transferase-mediated detoxification and direct ROS scavenging; used both acutely and in chronic pulmonary complication management ([PubMed 25055840](https://pubmed.ncbi.nlm.nih.gov/25055840/)).
  - **Macrolide antibiotics** (azithromycin, clarithromycin) — used for their anti-inflammatory/immunomodulatory properties in SM-induced bronchiolitis obliterans, often combined with NAC (e.g., azithromycin 250mg 3×/week + NAC 1200–1800mg/day).
  - **Inhaled corticosteroid/long-acting β2-agonist combinations** (e.g., fluticasone/salmeterol, "Seretide" 125–250/25μg 2 puffs BID) — shown effective for chronic bronchiolitis symptom control, with 56.7% of a 30-patient sub-cohort showing pulmonary function improvement and 77.8% of an HRCT-assessed sub-cohort showing radiographic improvement on 5-year follow-up ([PubMed 27832694](https://pubmed.ncbi.nlm.nih.gov/27832694/); [Tandfonline 2007](https://www.tandfonline.com/doi/abs/10.1080/08958370701432132)).
- **Experimental/pre-clinical countermeasures (not clinically validated):**
  - **DRDE-07 and analogues** (amino alkyl-alkyl/aryl sulphides) — oral prophylactic cytoprotectants with good pre-clinical protection/safety profile ([Journal of Applied Toxicology 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12209742/)).
  - **Amifostine**, combined with DRDE-07 analogues, when given 30 minutes pre-exposure in animal models, recovers biochemical/histopathological changes.
  - **Vitamin D (25(OH)D)** — reported to reduce SM-related mortality and mitigate toxicity in pre-clinical studies.
  - **PARP inhibitors** — mechanistically rational given the central PARP1/NAD+ depletion pathway, but not identified as clinically tested in this search.
- **Ophthalmic-specific treatment:**
  - Conservative management (lubrication, anti-inflammatory drops) for milder chronic keratopathy.
  - **Limbal stem cell transplantation**, **amniotic membrane transplantation** (anti-fibrotic/anti-angiogenic/anti-inflammatory), **penetrating and lamellar keratoplasty** for severe delayed keratopathy ([PubMed 15808253](https://pubmed.ncbi.nlm.nih.gov/15808253/)).
  - **Mesenchymal stem/stromal cell (MSC) therapy** — an emerging investigational approach targeting cellular senescence in mustard keratopathy, delivered via intrastromal/subconjunctival injection or MSC-seeded amniotic membrane grafts ([PMC 10705954](https://pmc.ncbi.nlm.nih.gov/articles/PMC10705954/); [PMC 9570439](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9570439/)).
- **Surgical:** Skin grafting/reconstructive surgery for severe cutaneous scarring; corneal transplantation as above.
- **Treatment strategy note:** No FDA-approved specific antidote exists as of the most recent literature identified (through 2025); management remains algorithmic supportive/symptomatic care escalating by organ system and chronicity.

---

## 13. Prevention

- **Primary prevention:**
  - **Personal protective equipment (PPE)** — the principal preventive measure against known/suspected exposure in military or hazmat contexts; if PPE or trained rescuers are unavailable, response should follow local Emergency Operational Guides ([UK Gov Incident Management](https://assets.publishing.service.gov.uk/media/66fc1d793b919067bb482a55/Incident_Management_sulphur_mustard_.pdf)).
  - **International legal prevention:** The Chemical Weapons Convention (enforced by the OPCW) bans production, stockpiling, and use of sulfur mustard as a chemical weapon; OPCW investigative mechanisms have been used to attribute and deter continued use (e.g., Syria investigations).
- **Secondary prevention (early detection/limiting injury after exposure):**
  - Rapid **decontamination within 1–2 minutes** is the single highest-yield secondary-prevention action, since benefit drops sharply thereafter ([ATSDR MMG](https://wwwn.cdc.gov/tsp/MMG/MMGDetails.aspx?mmgid=924&toxid=191)).
  - Open wounds should be decontaminated first; care must be taken to avoid spreading contamination to unexposed skin, with special attention to skin folds, nails, and ears.
- **Tertiary prevention:** Ongoing surveillance (HRCT, spirometry, ophthalmic exam) of exposed cohorts to catch delayed-onset pulmonary and ocular complications early, and chronic-phase pharmacotherapy (NAC, macrolides, inhaled corticosteroids) to slow progression once chronic disease is established (see §12).
- **Prophylaxis:** No licensed pre-exposure chemoprophylactic agent exists; DRDE-07 analogues, amifostine, and vitamin D are pre-clinical candidates only (see §12).
- **Public health/environmental interventions:** Munitions disposal and thermophysical/chemical destruction of legacy SM stockpiles is an active area of environmental-remediation research, given large historical arsenals requiring safe decommissioning ([RSC Environ Sci Adv 2024](https://pubs.rsc.org/va/article/4/10/1538/919603/Thermophysical-treatment-technologies-for-chemical)).
- **Counseling:** Not applicable in the genetic-counseling sense; psychological/PTSD-oriented counseling is relevant for exposed survivor populations given the documented chronic anxiety/depression burden.

---

## 14. Other Species / Natural Disease

- Sulfur mustard poisoning is **not a naturally occurring veterinary disease** — there is no OMIA entry or natural zoonotic/companion-animal disease analog; all animal data derive from deliberate experimental exposure (toxicology/countermeasure research), not spontaneous natural disease.
- **Taxonomy of experimental species used:** mouse (*Mus musculus*, NCBITaxon:10090), rat (*Rattus norvegicus*, NCBITaxon:10116), guinea pig, rabbit, and pig — used because there is **no simple or common animal model that reproduces true human-like blistering**, so different species are used to model different organ-specific injury endpoints ([PMC 10843005](https://pmc.ncbi.nlm.nih.gov/articles/PMC10843005/)).
- **Comparative biology:** SM's core alkylation/DNA-crosslink/PARP mechanism is evolutionarily conserved across mammalian species, which is why the toxicology translates reasonably well, even though gross tissue-level blistering response differs across species and does not fully replicate the human vesicant phenotype.
- **Transmission/zoonotic potential:** Not applicable — this is a direct chemical toxic exposure with no infectious/transmissible component.

---

## 15. Model Organisms

- **Model types used:** Rodent (mouse, rat) inhalation and dermal-exposure models predominate; also guinea pig, rabbit, and pig dermal models; *in vitro* human/animal cell culture (keratinocyte [HaCaT], corneal epithelial, endothelial, and brain cell aggregate cultures) and *ex vivo*/organotypic skin models.
- **Induced models:** All SM models are **induced** (chemical exposure), not spontaneous — via intratracheal instillation/inhalation (lung models) or cutaneous application (skin models), with a nitrogen mustard analog sometimes substituted for ocular models due to handling/safety considerations (e.g., "Mouse Model of Nitrogen Mustard Ocular Surface Injury," [PMC 10815872](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10815872/)).
- **Phenotype recapitulation:**
  - **Rat inhalation model:** reproduces progressive lung injury, inflammation, and fibrosis, with bronchiolitis obliterans and pulmonary fibrosis developing after SM inhalation, closely paralleling the human chronic mustard-lung phenotype ([PMC 6002659](https://pmc.ncbi.nlm.nih.gov/articles/PMC6002659/); [PMC 7751178](https://pmc.ncbi.nlm.nih.gov/articles/PMC7751178/)).
  - **Rat/mouse lung histopathology** at 16 days shows epithelial/airway thickening, alveolar thickening, immune-inflammatory cell infiltration, and epithelial sloughing — recapitulating human acute-to-subacute airway injury.
  - **Skin models:** reproduce epidermal apoptosis/necrosis and inflammatory cytokine responses but **do not reliably reproduce true human blistering**, a recognized cross-species limitation ([Cambridge Core, Skin Models](https://www.cambridge.org/core/journals/disaster-medicine-and-public-health-preparedness/article/skin-models-used-to-define-mechanisms-of-action-of-sulfur-mustard/8AEF6203C6E9111B051314FBE96C7C92)).
- **Model limitations:** No single species/model captures the full human triad (blistering skin + delayed keratopathy + progressive bronchiolitis obliterans) simultaneously; extrapolation of countermeasure efficacy from rodent models to humans remains an open translational question, particularly for chronic/delayed-onset pathology occurring over a human multi-decade timescale that cannot be directly modeled in short-lived rodents.
- **Applications:** Mechanistic studies (DNA damage/PARP/NAD+ pathway), pharmacologic countermeasure screening (NAC, DRDE-07 analogues, amifostine, cannabinoid-2 receptor agonists — [PMC 11860106](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11860106/) — vitamin D), and wound-healing/regenerative-therapy development (MSC-based corneal and skin repair).
- **Resources:** No dedicated OMIA/model-organism-database entry exists for this induced-toxicity model; primary literature (PubMed/PMC) is the operative resource rather than a curated model database.

---

## Summary for Knowledge-Base Modeling

For a dismech entry, sulfur mustard poisoning should be modeled as an **environmental/toxic Disease** (category: Environmental) with:
- **No `genetic:` causal drivers** — only modifier annotations (GSTM1/GSTT1/GSTP1/GSTA1, GSR) if evidence-supported at the individual-study level.
- An **`environmental:`** entry for "exposure to sulfur mustard," `influences_mechanisms`-linked with `environmental_effect: TRIGGERS` to the primary pathophysiology node (DNA alkylation/PARP1-NAD+ depletion).
- A **pathograph** built around the causal chain in §6: alkylation → crosslinking → PARP1 hyperactivation → NAD+/ATP depletion → necrosis/apoptosis + GSH depletion/oxidative stress → inflammatory cascade → organ-specific acute injury → (bimodal) either resolution or chronic/delayed organ-specific pathology (bronchiolitis obliterans/fibrosis; mustard keratopathy; skin carcinogenesis).
- **`progression:`** phases distinguishing acute, chronic, and delayed-onset (the "silent period" phenomenon is a distinctive and citable feature).
- Extensive **animal_models:** entries (rat inhalation model as the flagship pulmonary conformer) with `modeled_mechanisms` linking to the lung fibrosis/bronchiolitis obliterans nodes, explicitly noting the skin-blistering model-fidelity gap in `limitations`.
- **`clinical_trials:`**/treatment entries reflecting that all current pharmacotherapy is supportive/off-label repurposed (NAC, macrolides, inhaled corticosteroids) rather than a licensed SM-specific product — none should be modeled as a definitive antidote.

**Note on identifier verification needed before curation:** The ICD-10/ICD-11 code specific to sulfur mustard poisoning was not conclusively resolved in this search (searches returned T57.1, which is actually phosphorus poisoning); this should be verified against ICD-10-CM/ICD-11 warfare-agent-poisoning codes directly (e.g., T59/X-codes or ICD-11 chemical-agent-poisoning entries) before being entered into a KB `mappings:` block, per the "never write an ontology identifier from memory" rule.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 29 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 18 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CHEBI:25434` (1 mention) - the report calls it "bis"; CHEBI calls it **bis(2-chloroethyl) sulfide**
- `HP:0000508` (1 mention) - the report calls it "photophobia"; HP calls it **Ptosis**
- `HP:0000534` (1 mention) - the report calls it "corneal neovascularization"; HP calls it **Abnormal eyebrow morphology**
- `HP:0000585` (1 mention) - the report calls it "dry eye"; HP calls it **Band keratopathy**
- `HP:0000523` (1 mention) - the report calls it "blindness, severe cases"; HP calls it **Subcapsular cataract**
- `HP:0025406` (1 mention) - the report calls it "blistering"; HP calls it **Asthenia**
- `CL:0000312` (1 mention) - the report calls it "Cell types/GO/CL involvement to annotate:** keratinocytes"; CL calls it **keratinocyte**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0006536` (2 mentions) - the report calls it "chronic pulmonary obstruction"; HP calls it **Airway obstruction**, and lists "Pulmonary obstruction" among its other names
- `HP:0002204` (1 mention) - the report calls it "pulmonary fibrosis"; HP calls it **Pulmonary embolism**
- `UBERON:0001772` (1 mention) - the report calls it "cornea"; UBERON calls it **corneal epithelium**, and lists "cornea epithelium" among its other names