---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-20T09:27:46.932972'
end_time: '2026-10-20T09:33:16.309958'
duration_seconds: 329.38
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Angiomatoid Fibrous Histiocytoma
  mondo_id: MONDO:0012809
  category: Cancer
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
  web_search_requests: 2
  num_turns: 23
  total_cost_usd: 2.8880556
  session_id: ae615b7b-fd42-4fe4-b977-d3664d654219
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 6
reference_validation:
  total_references: 62
  verified: 62
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 12
  relevance_assessed: 62
  on_topic: 41
  validator_version: 0.3.0
term_validation:
  total_terms: 18
  verified: 17
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: NCIT:C6494
    reported_labels:
    - NCIT
    ontology_label: Angiomatoid Fibrous Histiocytoma
  - term_id: CL:0000542
    reported_labels:
    - 'Lymphoplasmacytic response: lymphocyte'
    ontology_label: lymphocyte
  labels_variant: 2
  unresolvable_prefixes:
  - Orphanet
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Angiomatoid Fibrous Histiocytoma
- **MONDO ID:** MONDO:0012809 (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Angiomatoid Fibrous Histiocytoma** covering all of the
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

Hear ye, Harry! I'm pulling the key AFH abstracts out of PubMed so the report can quote them word for word. The pie is in the oven.

Still in the kitchen, Harry: hunting down the founding AFH papers and the mechanism studies, one search at a time.

Nearly done gathering, Harry. I'm checking the last few mechanism papers before I plate the report.

Hear ye, Harry! The angiomatoid fibrous histiocytoma report is plated below. Each quote was copied from PubMed abstracts I pulled myself through NCBI E-utilities on 2026-10-20. I list the ontology IDs as leads to look up, not as checked bindings.

---

# Angiomatoid Fibrous Histiocytoma (AFH): Disease Characteristics Research Report

## 1. Disease Information

**Overview.** AFH is a rare soft-tissue tumour of intermediate biological behaviour: it recurs locally and rarely metastasises. Its line of differentiation is unknown. It usually arises in the superficial soft tissue of the extremities in children and young adults. It is defined by fusions of a FET-family gene (EWSR1, rarely FUS) to a CREB-family transcription factor (CREB1, ATF1, and CREM).

- "Angiomatoid fibrous histiocytoma (AFH) is a rare soft tissue neoplasm of intermediate biologic potential and uncertain differentiation, most often arising in the superficial extremities of children and young adults." — Thway & Fisher 2015, PMID:25927151 (review)
- Enzinger first described it in 1979 as "angiomatoid malignant fibrous histiocytoma" (41 cases), PMID:228836. Costa & Weiss 1990 argued for reclassifying it as intermediate: "it seems reasonable to reclassify angiomatoid malignant fibrous histiocytoma with fibrohistiocytic tumors of intermediate malignancy rather than with the conventional malignant fibrous histocytoma" — PMID:2174650.

**Identifiers** (taken from the MONDO record in live OLS, 2026-10-20):

| Source | ID |
|---|---|
| MONDO | MONDO:0012809 (label "histiocytoma, Angiomatoid fibrous") |
| NCIT | NCIT:C6494 |
| OMIM | 612160 |
| Orphanet | Orphanet:569164 (MONDO cross-reference; not checked against Orphadata, and `references_cache/` has no ORPHA file for AFH) |
| ICD-O | 8836/1 (borderline/intermediate behaviour) |
| MeSH | C563181 (supplementary concept) |
| OncoTree | AFH |
| UMLS / MedGen / GARD | C1266127 / 226845 / 0022303 |

**Synonyms:** angiomatoid malignant fibrous histiocytoma (AMFH, historical), angiomatoid "malignant" fibrous histiocytoma, AFH. Intracranial cases now fall under the related entity **"intracranial mesenchymal tumor, FET::CREB fusion-positive"** (previously called intracranial AFH or intracranial myxoid mesenchymal tumour), PMID:33141488 and PMID:34821426.

**Type of evidence:** all aggregated case series and case reports (pathology registries such as the AFIP Soft Tissue Registry, and single-institution series). There are no EHR-scale cohorts or population registries specific to AFH.

## 2. Etiology

- **Cause:** a somatic chromosomal translocation that produces a FET::CREB-family fusion oncogene (Section 4). No germline predisposition is known.
- **Genetic risk factors:** none described. There is no GWAS signal and no familial clustering.
- **Environmental risk factors:** none established. Some reports note that a lesion may sit at a site of earlier trauma ("may be associated with a site of recent or previous trauma", PMID:29472492). That is an anecdotal clinical observation, not evidence of a cause. Isolated co-occurrences (HIV-positive child, PMID:18376290; after testicular germ-cell tumour, PMID:24155684 and PMID:35118896; Castleman disease, PMID:32672859) are single cases with no shown causal link. PMID:35118896 explicitly argues *against* somatic transformation from the germ-cell tumour.
- **Protective factors and gene–environment interactions:** none known. I found no data.

## 3. Phenotypes

| Phenotype | Type | Frequency / notes | Key source | HPO lead (verify) |
|---|---|---|---|---|
| Slow-growing nodular or cystic subcutaneous mass, often mistaken for haematoma or haemangioma | Sign | Near-universal presenting feature; median size 2.0–2.5 cm | PMID:228836, PMID:10571514 | Subcutaneous nodule; Soft tissue neoplasm |
| Painless or minimally tender mass | Symptom | "seldom caused tenderness or pain" | PMID:228836 | — |
| Systemic / paraneoplastic symptoms: fever, anaemia, weight loss, malaise | Symptom / lab | A minority; more frequent at extrasomatic sites | MONDO definition; PMID:21822206 ("higher frequency of systemic symptoms") | Fever HP:0001945; Anemia HP:0001903; Weight loss HP:0001824 |
| Raised inflammatory markers (ESR, CRP) and raised serum IL-6, which resolve after resection | Lab | Case-level | PMID:36593607; PMID:29932283; IL-6 normalised after resection in the CREM-fused intracranial case PMID:36328767 | Elevated erythrocyte sedimentation rate; Elevated C-reactive protein |
| Paraneoplastic platelet storage-pool deficiency (bleeding) | Lab | Single case | PMID:29472492 | — |
| Membranous nephropathy / nephrotic syndrome that resolved after resection | Sign / lab | Single case | PMID:24880818 | Proteinuria / Nephrotic syndrome |
| Local recurrence | Course | 2–15% (2/86 in Fanburg-Smith; 12% in Costa & Weiss; about 15% in recent reviews) | PMID:10571514, PMID:2174650 | — |
| Regional lymph-node metastasis | Course | About 1–5% | PMID:10571514, PMID:23199525 ("Less than 5% metastasize") | Lymph node metastasis |
| Pulmonary or distant metastasis | Course | Rare; associated with death | PMID:25757019 | — |
| Intracranial: headache, focal neurological signs, recurrence | Sign | Intracranial FET::CREB cases | PMID:33141488, PMID:30831299 | Headache HP:0002315 |

**Onset:** childhood to young adulthood (median 13–14 years in classic series), range 2 to 76 years. **Severity:** usually mild and curable by excision; a small subset behaves aggressively. **Quality of life:** no formal QoL data (no EQ-5D or SF-36 studies). The impact comes from surgery, the burden of recurrence, and paraneoplastic symptoms.

## 4. Genetic / Molecular Information

**Defining fusions (all somatic):**

| Fusion | Translocation | Frequency in soft-tissue AFH | Source |
|---|---|---|---|
| EWSR1::CREB1 | t(2;22)(q33;q12) | Predominant (>90%) | PMID:17724745, PMID:18094413 |
| EWSR1::ATF1 | t(12;22)(q13;q12) | Minority; enriched at extrasomatic sites | PMID:17188428, PMID:21822206 |
| FUS::ATF1 | t(12;16)(q13;p11) | Rare | PMID:11063792 |
| EWSR1::CREM | — | Uncommon overall; 33% in acral AFH; enriched in intracranial Group B | PMID:40748380, PMID:34821426 |
| EWSR1::PBX3 | — | Single acral case | PMID:40748380 |

- Antonescu et al. 2007: "By RT-PCR, eight out of nine tumors showed the presence of the EWSR1-CREB1 fusion, while one had an EWSR1-ATF1 transcript." "We report for the first time the presence of EWSR1-CREB1 in AFH, which now appears to be the most frequent gene fusion in this tumor." — PMID:17724745
- Rossi et al. 2007: "Thirteen cases showed rearrangements of both EWSR1 and CREB1, whereas one case showed the rearrangement of both EWSR1 and ATF1." — PMID:18094413
- Waters et al. 2000 (first molecular case): "the FUS (also known as TLS) gene from 16p11 combined with the ATF-1 gene from 12q13 to generate a chimeric FUS/ATF-1." — PMID:11063792
- Tanas et al. 2010: "13 of 17 (76%) cases of angiomatoid fibrous histiocytoma harbored rearrangements of EWSR1; rearrangements of FUS were not detected in any of the cases." 24% were negative by FISH. — PMID:19801966

**Genes (HGNC IDs need lookup):** EWSR1, FUS, CREB1, ATF1, CREM. Use lowercase `hgnc:` and look each one up; I have not verified the numbers.

**Variant class:** structural (in-frame chimeric fusion). Functionally it is **neomorphic / gain of function**: a constitutive transcriptional activator (Section 6). There is no ACMG classification, because the variant is somatic. Allele frequency in gnomAD does not apply.

**Secondary alterations / modifiers:** "CDKN2A/B homozygous deletions were recurrent in angiomatoid fibrous histiocytoma (AFH) and restricted to metastatic cases." — Dermawan et al. 2022, PMID:35347249. A pleomorphic variant carried multiple copies of the EWSR1::CREB1 fusion (PMID:22038502). Fusion type does not correlate with clinicopathological features (PMID:17188428).

**Epigenetics:** AFH has its own DNA-methylation class, close to but distinct from clear cell sarcoma (CCS). "Unsupervised clustering of methylation profiles revealed that CREB family translocation-associated tumors form neighboring but tight, distinct clusters." S100A4 and XAF1 are upregulated and hypomethylated in AFH. — PMID:35347249. Intracranial FET::CREB tumours split into two methylation groups. Group B (CREM-enriched) has worse progression-free survival: "median 4.5 vs. 49 months, p = 0.001". — PMID:34821426

## 5. Environmental Information

No toxin, radiation, lifestyle, or infectious cause is known. Not applicable.

## 6. Mechanism / Pathophysiology

**Ordered causal chain**

1. **A somatic translocation** in a mesenchymal precursor (cell of origin unknown) fuses the 5′ EWSR1 (or FUS) N-terminal low-complexity domain to the 3′ bZIP DNA-binding domain of CREB1, ATF1, or CREM. *Demonstrated* (PMID:17724745, PMID:18094413).
2. **The fusion protein becomes a constitutive activator of CRE-driven transcription that no longer needs cAMP.** The fusion replaces the kinase-inducible (PKA-phosphorylated) domain of the CREB-family partner with the EWS domain. *Demonstrated for EWS-ATF1 in the CCS context and inferred for AFH.* "EWS-ATF-1 binds weakly to DNA in vitro but functions as an efficient constitutive transcriptional activator unlike the normal ATF-1 which needs to be induced with cAMP." — Fujimura 1996, PMID:8552387 (IN_VITRO). Caveat: Li & Lee 1998 found that endogenous EWS/ATF1 did not constitutively activate some chromosomal CRE promoters in CCS cells (PMID:9546434), so the downstream programme is promoter-specific.
3. **That deregulated transcription produces a lineage-dependent gene programme.** The same fusion makes AFH in some precursors and CCS in others. In AFH the programme is non-melanocytic: TFE3 high, MITF-M and SOX10 absent. "High transcript levels were noted for TFE3 in AFH tumors, while overexpression of genes involved in melanogenesis, such as MITF, GP100, and MET was noted in somatic clear cell sarcomas." (PMID:17724745). "The MITF-M transcript was not detected in either AFH, in line with the finding that the co-activator SOX10 was not expressed." (PMID:17188428). Divergent precursor-cell context is the favoured explanation (PMID:18094413). *Inferred.*
   - Experimental support (IN_VITRO): in human embryonic stem cells, "expression of EWSR1-CREB1/ATF1 fusion in hES cells recapitulates the core gene signatures, respectively, of angiomatoid fibrous histiocytoma (AFH) and gastrointestinal clear cell sarcoma (GI-CCS), although both fusions lead to cell lethality." Expression in mesenchymal progenitors is tolerated, and TP53 deletion extends proliferation. — PMID:34193943
4. **Neoplastic proliferation** of bland ovoid or spindle "histiocytoid" cells with a myoid/myofibroblastic phenotype (desmin, EMA, CD99) produces a multinodular tumour inside a fibrous pseudocapsule. *Demonstrated (morphology).*
5. **Branch A: microenvironment and inflammation.** A dense lymphoplasmacytic cuff forms around the tumour (80% of cases, PMID:10571514). PD-L1 is expressed with an adaptive pattern: "a positive correlation was found between tumor cell PD-L1 expression and CD8+ T-cell infiltration" (PMID:33500467). 66% of cases arise at sites of normal lymphoid tissue, which raises the possibility that AFH comes from myoid cells of lymphoid tissue (PMID:10571514). *Hypothesis.*
6. **Branch B: blood-filled pseudovascular spaces.** Haemorrhagic cyst-like spaces form (about 50% of cases), which produce the "angiomatoid" look and the clinical mimicry of a haematoma. Mechanism *not established*.
7. **Branch C: cytokine secretion leading to a systemic syndrome.** The tumour secretes IL-6, which causes fever, anaemia, raised ESR/CRP, and weight loss. These resolve after resection (PMID:36593607) or with IL-6 receptor blockade (PMID:32546510). Whether IL-6 also drives tumour growth through an autocrine loop is **contested**: Potter 2018 reported a tumour response to tocilizumab (PMID:29932283), while Sabe 2021 found that tocilizumab "controlled paraneoplastic inflammatory syndrome (PIS); however, the local recurrent tumor progressed. This case implied that IL-6 is not necessarily the cause of tumor growth in AFH." (PMID:34221525). The IL-6/STAT3 link is also documented in a CREM-fused intracranial tumour (PMID:36328767).
8. **Progression.** Secondary CDKN2A/B homozygous deletion is associated with metastasis (PMID:35347249), leading to nodal and, rarely, pulmonary metastasis. Death is rare.

**Aberrant kinase expression (no clear driver role):** ALK is expressed in most AFH without rearrangement: "AFH with positive ALK IHC showed no ALK gene rearrangement by FISH (0/8)" (PMID:29877921), and 94.4% of cases in PMID:31652145. PanTRK is expressed in 64% without NTRK alteration (PMID:38053271). One metastatic case had a durable response to crizotinib (PMID:35568279; I have the abstract metadata only, so the claim of ALK dependence should be quoted from the full text).

**GO / CL leads (verify with OAK before binding):**
- Constitutive CRE-dependent transcription: "regulation of transcription by RNA polymerase II" (GO:0006357) with `modifier: GAIN_OF_FUNCTION`. That modifier fits, because the fusion escapes cAMP regulation. A more specific CREB-related GO term may exist, so search for one.
- IL-6 production: "positive regulation of interleukin-6 production" (GO:0032755); "interleukin-6-mediated signaling pathway" (GO:0070102).
- Lymphoplasmacytic response: lymphocyte (CL:0000542), plasma cell (CL:0000786), CD8-positive alpha-beta T cell.
- Tumour cell: no CL term for the cell of origin. Desmin-positive myoid cells suggest myofibroblast (CL:0000186). Record this as a hypothesis, not as a cell of origin.

**Profiling and data:** methylation and transcriptome profiles (PMID:35347249, PMID:34821426). I found no AFH-specific single-cell or spatial data, and no CRISPR screens.

## 7. Anatomical Structures Affected

- **Primary:** subcutis and deep dermis (UBERON hypodermis / subcutaneous tissue, verify the ID). Order of frequency: extremities > trunk > head and neck (PMID:10571514).
- **Unusual sites:** lung or endobronchial (PMID:22588066, PMID:19654501), mediastinum, pulmonary artery (PMID:24702653), bone (PMID:20090505), vulva, ovary, retroperitoneum (PMID:21822206), adrenal (PMID:30823861), breast (PMID:31236300), and intracranial/spinal meninges and ventricles (PMID:33141488). Thoracic AFH overlaps with primary pulmonary myxoid sarcoma: "PPMS and AFH may be morphologic variants of the same clinicopathologic entity" (PMID:38407279).
- **Acral sites:** female predominance and CREM enrichment (PMID:40748380).
- **Subcellular:** nucleus (aberrant transcription factor).
- **Lateralisation:** solitary and unilateral.

## 8. Temporal Development

- **Onset:** paediatric to young adult. Median age 13 years (Enzinger, PMID:228836), 14 years (intracranial, PMID:33141488), 23 years (acral, PMID:40748380). Extrasomatic cases are older (median 48 years, PMID:21822206). Onset is insidious, a slowly enlarging mass.
- **Course:** usually stable and cured by excision. Recurrence follows incomplete excision. "The initial excision in all patients developing local recurrence appeared to be incomplete." (PMID:2174650). Metastases "5 months to 16 years after primary tumor resection" (PMID:25757019), which supports long-term follow-up.
- **Staging:** no AFH-specific staging system. There is no WHO grade; it is classed as intermediate (rarely metastasising).

## 9. Inheritance and Population

- **Inheritance:** not inherited (sporadic, somatic fusion).
- **Epidemiology:** no incidence or prevalence data. It is usually cited as about 0.3% of soft-tissue tumours. That figure comes from textbooks, and I did not verify it against a primary source. Use `measure_type: UNKNOWN` / `prevalence_class: RARE` unless a quotable figure turns up.
- **Sex ratio:** "a gender ratio of 1.3 females: males" (PMID:10571514). Intracranial: 16 female, 4 male (PMID:33141488). Acral: 19 female, 7 male (PMID:40748380). Extrasomatic: slight male predominance (PMID:21822206).
- **Age range:** 2 to 71 years (AFIP series).
- **Geography / ancestry:** no known predilection.

## 10. Diagnostics

- **Histopathology (the gold standard):** "nodular distributions of ovoid and spindle cells with blood-filled cystic cavities and a surrounding dense lymphoplasmacytic infiltrate" (PMID:25927151). Fibrous pseudocapsule. Variants: myxoid, reticular, pleomorphic, sclerosing/schwannoma-like, solid without angiomatoid spaces (PMID:24043718).
- **Immunohistochemistry:** desmin 51–78%, EMA about 56–100%, CD99 45–100%, CD68 (PMID:10571514, PMID:24043718, PMID:21822206). Also ALK 85–94% (pitfall for inflammatory myofibroblastic tumour), MUC4 22%, synaptophysin about 55% in thoracic cases, TLE1/BCOR, and SOX9 (PMID:31652145, PMID:38407279, PMID:36910892, PMID:31567275). Negative: S100, HMB45, MITF (unlike CCS), myogenin, and SSTR2A in intracranial cases.
- **Molecular:** EWSR1 break-apart FISH (does not identify the partner, and false negatives occur, PMID:19801966). RT-PCR or targeted RNA-NGS / anchored-multiplex fusion panels identify the partner and are preferred (PMID:25804255, PMID:40900879). A DNA-methylation classifier is available but performs less well outside CCS (PMID:35347249, PMID:37921028).
- **Germline testing:** not indicated (WGS/WES, CMA, karyotype). A tumour karyotype may show t(2;22).
- **Imaging:** MRI shows a cystic or haemorrhagic mass with fluid–fluid levels and a peripheral rim (PMID:26919861, PMID:26162466). FDG-avid on PET (PMID:38693744).
- **Laboratory:** CBC (anaemia), ESR, CRP, serum IL-6, and urinalysis (suggested after the nephropathy case, PMID:24880818).
- **Differential diagnosis:** haematoma, haemangioma, aneurysmal fibrous histiocytoma, lymph-node metastasis, clear cell sarcoma (same fusions but melanocytic markers present), Ewing sarcoma (CD99+, EWSR1+), rhabdomyosarcoma (desmin+ but myogenin+), inflammatory myofibroblastic tumour (ALK+ with ALK rearrangement), myoepithelioma, synovial sarcoma (TLE1), primary pulmonary myxoid sarcoma, meningioma (intracranial), and metastatic melanoma.
- **Screening:** none.

## 11. Outcome / Prognosis

- **Survival:** excellent. Death in about 1% (PMID:2174650). AFIP series: "1% frequency of metastasis" over a mean follow-up of 6 years (PMID:10571514).
- **Recurrence:** 2–15%. Associated with "irregular tumor border and head and neck location", and metastasis with "invasion into the deep fascia or muscle", but not with mitoses or pleomorphism (PMID:2174650).
- **Metastasis:** "Nine patients metastasized to lymph nodes. Excision of metastatic lymph nodes was usually curative. Pulmonary metastases were associated with fatal outcome." (PMID:25757019).
- **Prognostic markers:** CDKN2A/B deletion (metastatic cases, PMID:35347249). Intracranial: methylation Group B (worse PFS, PMID:34821426); all three intracranial deaths had EWSR1::ATF1 (PMID:33141488). In one small series both aggressive cases had EWSR1::CREB1 (PMID:28114920), which is anecdotal.
- **Morbidity:** surgical, plus paraneoplastic illness that reverses after resection.

## 12. Treatment

| Treatment | Role | Evidence | NCIT lead |
|---|---|---|---|
| Wide local excision with clear margins | First line, usually curative | PMID:2174650, PMID:25927151 | NCIT:C15329 Surgical Procedure (`therapeutic_modality: SURGERY`) |
| Re-excision of recurrence; excision of involved nodes | Salvage | PMID:2174650, PMID:25757019 | NCIT:C15329 |
| Gross total resection (intracranial) | First line | PMID:30831299 | NCIT:C15329 |
| Radiotherapy | Unresectable or residual disease (case-level) | PMID:35568279 context; no series | NCIT:C15313 Radiation Therapy |
| Chemotherapy (anthracycline/ifosfamide-based sarcoma regimens) | Metastatic or unresectable disease; sustained responses reported | "3 patients with metastatic AFH who demonstrated a sustained response to chemotherapy" PMID:36716049; doxorubicin, intracranial PMID:34055346 | NCIT:C15632 Chemotherapy; doxorubicin CHEBI:28748 |
| Tocilizumab (IL-6R antibody) | Controls the paraneoplastic syndrome; effect on tumour growth inconsistent | PMID:29932283 (response); PMID:34221525 (syndrome controlled, tumour progressed); PMID:32546510 | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` tocilizumab (look up the CHEBI/NCIT ID) |
| Crizotinib (ALK inhibitor) | Metastatic disease with ALK overexpression, single durable response | PMID:35568279 | Pharmacotherapy + crizotinib (look up) |
| Cryoablation | Metastasis, one complete remission | PMID:36716049 | look up |
| PD-1/PD-L1 blockade | Rationale only (PD-L1+ in 61%) | PMID:33500467 | — |

There are no prospective trials and no AFH-specific NCT entries that I found. Pharmacogenomics does not apply.

## 13. Prevention

There is no primary prevention or screening. Tertiary prevention means complete excision at first surgery: avoid an "unplanned excision", PMID:30170609. After that comes long-term clinical and imaging follow-up, because metastases have appeared up to 16 years later (PMID:25757019). Genetic counselling is not indicated, because the fusion is somatic.

## 14. Other Species

I found no confirmed naturally occurring AFH in animals. A PubMed search for AFH together with dog, canine, cat, or horse returned one hit, a general fusion review (PMID:40205020). "Primary Angiomatoid Melanomas in Dogs" (PMID:36252388) is a **different** entity (melanocytic) and must not be conflated with AFH. Not applicable.

## 15. Model Organisms

- **There is no genetically engineered animal model of AFH.** (For CCS, EWS-ATF1 mouse models exist, but they produce a melanocytic CCS phenotype and are not AFH models; I did not cite one here.)
- **In vitro:** CRISPR-engineered, conditional EWSR1::CREB1 / EWSR1::ATF1 human embryonic stem cells and their mesenchymal-progenitor derivatives reproduce the AFH core gene signature. The fusion is lethal in undifferentiated hES cells, tolerated in mesenchymal progenitors, and proliferation lengthens with TP53 loss (PMID:34193943, IN_VITRO). Limits: no tissue architecture, no lymphoid cuff, no haemorrhagic spaces, no systemic IL-6 effects. In dismech terms these are `BOUNDARY_OMISSION` divergences.
- **Cell lines:** I found no established AFH line. CCS lines DTC1 and Su-ccs-1 carry EWS/ATF1 but are a different histotype (PMID:9546434).

---

### Caveats for the KB entry
- Ontology IDs other than MONDO:0012809, NCIT:C6494, and the NCIT treatment IDs listed in CLAUDE.md are **leads from memory, not looked up**. Run each through OAK or the term caches before writing it.
- PMID:35568279, PMID:32546510, and PMID:1314523 have no abstract in PubMed, so any snippet from them needs a full-text cache.
- The "about 0.3% of soft-tissue tumours" figure is unsourced here.
- The IL-6 autocrine growth claim is contested (PMID:29932283 vs PMID:34221525). Record it with `supports:` on both sides, not with a causal predicate.

*A song!*
> *Oh, the fusion's on the platter, CREB1 and EWSR1,*
> *cut it clean around the margins and the feast is nearly done!*

## Sources
- PubMed E-utilities (esearch/esummary/efetch), queried 2026-10-20 for every PMID above
- [OLS4 MONDO:0012809](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0012809)
- [Saito et al. 2017 (PMC5260132)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5260132/)
- [Feng et al. 2025, Front Oncol](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1420597/full)
- [Perez & Aung 2026 review, J Pathol Transl Med](https://jpatholtm.org/upload/pdf/jptm-2026-06-05.pdf)
- [Fanburg-Smith & Miettinen 1999 (PSU record)](https://pure.psu.edu/en/publications/angiomatoid-malignant-fibrous-histiocytoma-a-clinicopathologic-st/)
- [VIVA-Asia Rare Tumour Board synopsis, Jan 2023](https://www.viva.sg/news/328-viva-asia-rtb-angiomatoid-fibrous-histiocytoma-synopsis-10-jan-2023.html)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 62 |
| Resolved | 62 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 62 |
| On topic | 41 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 18 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C6494` (2 mentions) - the report calls it "NCIT"; NCIT calls it **Angiomatoid Fibrous Histiocytoma**
- `CL:0000542` (1 mention) - the report calls it "Lymphoplasmacytic response: lymphocyte"; CL calls it **lymphocyte**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0012809` (5 mentions) - the report calls it "label "histiocytoma, Angiomatoid fibrous"; MONDO calls it **histiocytoma, Angiomatoid fibrous**
- `GO:0032755` (1 mention) - the report calls it "positive regulation of interleukin-6 production", "IL-6 production: "positive regulation of interleukin-6 production"; GO calls it **positive regulation of interleukin-6 production**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0032755` - called "positive regulation of interleukin-6 production", "IL-6 production: "positive regulation of interleukin-6 production"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`.