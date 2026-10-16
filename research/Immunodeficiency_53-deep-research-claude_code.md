---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T18:26:53.638687'
end_time: '2026-10-14T18:29:01.230899'
duration_seconds: 127.59
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 53
  mondo_id: MONDO:0054696
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 5
  num_turns: 11
  total_cost_usd: 0.9506454000000002
  session_id: 24cc3ff8-2940-565a-acd5-e50a340ab4c5
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 8
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 30
  not_found: 1
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.031
  labels_checked: 11
  labels_matching: 2
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0054696
    reported_labels:
    - MONDO
    ontology_label: immunodeficiency 53
  - term_id: DOID:0111992
    reported_labels:
    - DOID
    ontology_label: immunodeficiency 53
  - term_id: HP:0100550
    reported_labels:
    - P1 and P2
    ontology_label: Tendon rupture
  - term_id: HP:0002014
    reported_labels:
    - Siblings
    ontology_label: Diarrhea
  - term_id: HP:0004322
    reported_labels:
    - Oldest sibling (Sharfe 2022)
    ontology_label: Short stature
  labels_variant: 4
  unresolved_terms:
  - HP:0003290
  obsolete_terms:
  - term_id: HP:0005407
    ontology_label: obsolete Decreased proportion of CD4-positive helper T cells
    replaced_by: HP:0032218
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 53
- **MONDO ID:** MONDO:0054696 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 53** covering all of the
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

I've pulled the two main RELB papers (Le Voyer 2024, Sharfe 2022). I'm now checking the PMID of the original 2015 RELB report before I write the report.

# Immunodeficiency 53 (IMD53; RELB deficiency): research report

**Sourcing.** I could not open OMIM, Orphanet, ClinGen or GenCC directly, so those statements come from search snippets or aggregators. Two papers I read in full text through PMC (Le Voyer 2024 and Sharfe 2022), except the last ~39k characters of the Le Voyer page. Anything not in a paper I read is marked *unverified*.

- **Do not use any PMID marked *unverified* as evidence until it has been fetched.** The repository's `just fetch-reference` check applies.
- **Every CURIE below is a suggestion from memory.** None was looked up in OAK or the term caches. Per CLAUDE.md, each one must be checked before it is bound.

---

## 1. Disease information

**Overview.** IMD53 is a rare autosomal recessive combined T- and B-cell immunodeficiency caused by biallelic loss-of-function or hypomorphic variants in *RELB*. RelB is a subunit of the alternative (non-canonical) NF-κB pathway. The syndrome combines recurrent viral, bacterial and fungal infections with immune decline over time. Autoimmunity and neutralizing anti-type I interferon autoantibodies are also seen.

**Identifiers.**

| Item | Value | Source |
|---|---|---|
| MONDO | MONDO:0054696 | [DrugMap](https://drugmap.idrblab.net/data/disease/details/DISQ3Q2J), [GenCC submission](https://search.thegencc.org/submissions/GENCC_000102-HGNC_9956-MONDO_0054696-HP_0000007-GENCC_100004) |
| OMIM phenotype | #617585, listed with a "?" prefix in the phenotype map | search snippets only; OMIM page not opened |
| Gene | *RELB* (OMIM 604758, 19q13.32, HGNC:9956) | GenCC URL and aggregators |
| UMLS | C4539811 | [MedGen mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/src/branch/main/www.ncbi.nlm.nih.gov/medgen/C4539811/index.html) |
| DOID | DOID:0111992 | [Disease Ontology](https://disease-ontology.org/term/DOID:0111992) |

In this repository the gene would be written `hgnc:9956` (lowercase prefix).

**Synonyms.** RELB deficiency, RelB deficiency, and combined immunodeficiency due to RELB deficiency.

**Data origin.** The evidence comes from individual-patient case reports and small series (3 + 3 + 2 patients), not from registries or EHR data.

---

## 2. Etiology

- **Cause.** Biallelic *RELB* variants, either homozygous or compound heterozygous, inherited from carrier parents. No environmental cause is described.
- **Genetic risk and modifiers.** None are described. gnomAD homozygous missense variants D417N and D487Y behaved like wild type in the assay ([Le Voyer 2024, PMID 39231201](https://pmc.ncbi.nlm.nih.gov/articles/PMC11406260/)).
- **Protective factors.** None are known.
- **Gene–environment interaction.** Not described. The patients' infections are of ordinary community pathogens, plus JC polyomavirus and *Cryptococcus*, as a consequence of the immunodeficiency.
- **Strength of gene–disease evidence.** This is graded unevenly.
  - ClinGen's SCID-CID group rates *RELB* "limited", per a search snippet.
  - PanelApp lists it as high evidence, per a search snippet.
  - OMIM marks the phenotype with "?".
  - Curators should record the validity classification only as `classified_by` an external source, never assign it themselves.

---

## 3. Phenotypes

The frequencies below are qualitative or n/N from at most 8 patients. HPO suggestions are unverified.

| Phenotype | Details | Suggested HPO |
|---|---|---|
| Recurrent bacterial respiratory infections (pneumonia, sinusitis, otitis media, mastoiditis) | Seen in the adult cohort | HP:0002783 (recurrent lower respiratory tract infections), HP:0004429 (recurrent viral infections) |
| Chronic mucocutaneous / oral candidiasis | P1 and P2 | HP:0100550 |
| Cryptococcal meningitis | P1, at age 12 | HP:0005407? Use a meningitis or fungal-infection term; verify |
| Viral skin disease (warts, epidermodysplasia verruciformis) | P2 | HP:0200043 (verrucae); verify |
| Varicella pneumonia | P2, at age 3 | search HPO |
| Progressive multifocal leukoencephalopathy | P2, fatal at age 34 | HP:0012774? verify |
| Hypogammaglobulinemia | P1 | HP:0001880 (decreased IgG) or HP:0004313 (hypogammaglobulinemia) |
| Poor vaccine response | Sharfe 2022 siblings | HP:0003290 |
| Decreased naïve CD4⁺ and CD8⁺ T cells | Both cohorts | HP:0005415 (decreased CD4 count), HP:0010987 |
| Decreased memory and class-switched B cells | P1; siblings (progressive loss of CD19⁺ and CD27⁺ B cells) | search HPO |
| Autoimmune enteritis, chronic diarrhea | Siblings | HP:0002014 |
| Autoimmune hepatitis-like disease, sclerosing cholangitis-like changes | Siblings | HP:0001392 area; verify |
| Chronic bronchiolitis requiring lobectomy | Siblings | search HPO |
| Chronic inflammatory skin lesions | Siblings | search HPO |
| Short stature, underweight | Oldest sibling (Sharfe 2022) | HP:0004322 |
| Large B-cell lymphoma | P2 | HP:0012191 area; verify |
| Thymic hypoplasia | P1 | HP:0000778 |
| Anti-type I IFN autoantibodies | Both adults | no HPO term; use a lab-abnormality description |

**Onset and course.**
- Presentation is in infancy to early childhood, per [MalaCards](https://www.malacards.org/card/immunodeficiency_53) (secondary source).
- The 2015 index family presented between 7 days and 4 months of age, per search-result summaries (*unverified*).
- Immune function declines over time. The siblings showed age-related loss of naïve T cells and B cells.
- Some adults escape early diagnosis. P1 and P2 were diagnosed as adults.

**Quality of life.** No formal measures are reported. P2 died of progressive multifocal leukoencephalopathy at age 34.

---

## 4. Genetic and molecular information

**Variants.**

| Variant | Genotype | Consequence | Source |
|---|---|---|---|
| c.212dup, p.Gln72ThrfsTer152 | Homozygous (P1, consanguineous Turkish parents) | Abolished RelB expression | Le Voyer 2024 |
| c.433G>A, p.E145K and c.1091C>T, p.P364L | Compound heterozygous (P2) | Stable protein, hypomorphic function | Le Voyer 2024 |
| c.1091C>T, p.P364L | Homozygous in three Iranian Jewish siblings | Highly unstable protein at very low levels, residual function, transiently inducible by TLR stimulation | [Sharfe 2022, PMID 36402602](https://pmc.ncbi.nlm.nih.gov/articles/PMC10861023) |
| Homozygous nonsense | Three children, found by linkage analysis, WGS and Sanger | Complete RelB deficiency | Merico/Sharfe 2015 (see below) |

- The Le Voyer variants are absent from gnomAD and other databases.
- The same P364L allele appears in two independent reports, once homozygous and once in trans with E145K.
- All variants are germline.
- There is no known modifier gene and no epigenetic or chromosomal data.

**Mechanism type.** Loss of function (complete) or hypomorphism (partial). Use `functional_impact_category: LOSS_OF_FUNCTION` or `PARTIAL_LOSS_OF_FUNCTION` per variant, and cite the functional assay.

**Primary literature for the original report.**
- Merico et al. 2015, *LymphoSign Journal*, DOI 10.14785/lpsn-2015-0005. It is not in PubMed, so it cannot go through `fetch-reference` as a PMID. A DOI fetch may work.
- Sharfe N et al. 2015, "The effects of RelB deficiency on lymphocyte development and function", PMID 26385063. This PMID comes from a GenCC-derived search summary and is *unverified*. Fetch it before use.

---

## 5. Environmental information

None are known.
- **Infectious agents as consequences, not causes:** *Candida*, *Cryptococcus neoformans*, varicella-zoster virus, JC polyomavirus and human papillomaviruses (epidermodysplasia verruciformis-type warts). These are opportunistic outcomes, so they belong under phenotypes or complications, not `infectious_agent`.
- If a curator wants NCBITaxon terms, look each one up individually.

---

## 6. Mechanism and pathophysiology

**Causal chain.**

1. Biallelic *RELB* variants lead to absent or hypomorphic RelB protein. This is demonstrated by loss of expression for Q72fs and by reduced stability for P364L.
2. Loss of RelB impairs lymphotoxin- and TWEAK-induced alternative NF-κB signaling, shown as reduced *NFKB2* and *VCAM1* induction in patient fibroblasts. Canonical NF-κB responses to TNF and IL-1β stay intact (Le Voyer 2024).
3. In the thymus, loss of RelB in stromal cells is thought to give hypoplastic thymus and few AIRE-expressing medullary thymic epithelial cells. The thymic hypoplasia in P1 is observed. The AIRE-deficiency link is an inference from the 2022 Le Voyer study in the search results, which I did not read (*unverified*).
4. Defective stromal-driven central tolerance leads to anti-type I IFN autoantibodies. This is observed in both adults, and the antibodies persist after HSCT, which supports a stromal (not hematopoietic) origin. That reading is the authors' inference.
5. Naïve T-cell depletion, low Th17 cells and reduced IL-17A/F/IL-22 production, together with poor memory and class-switched B-cell output, lead to combined immunodeficiency. For B cells, P1's naïve cells could not make IgG or IgA in response to CD40L plus IL-21 in vitro.
6. Combined immunodeficiency leads to chronic mucocutaneous candidiasis, bacterial respiratory infections, cryptococcal meningitis, viral skin disease and PML.
7. **Branch for partial deficiency (P364L).** In Sharfe 2022, fibroblasts showed elevated pro-inflammatory NF-κB target genes after poly(I:C) or LIGHT stimulation. The authors interpret this as loss of RelB's inhibitory effect on RelA, and they describe their evidence as indirect. This is inferred, not demonstrated. Reduced RelB then leads to autoimmune enteritis, hepatitis-like liver disease, bronchiolitis and skin inflammation, with a decline in immune cells in the second decade.

**Suggested GO and CL terms (unverified).**
- GO: non-canonical NF-κB signal transduction (GO:0038061), positive regulation of non-canonical NF-κB signal transduction (GO:1901224), T cell differentiation in thymus (GO:0033077), B cell differentiation (GO:0030183), central tolerance induction (GO:0002507), type 17 immune response (GO:0072538).
- CL: naïve thymus-derived CD4-positive alpha-beta T cell (CL:0000895), memory B cell (CL:0000787), medullary thymic epithelial cell (CL:0002293), fibroblast (CL:0000057).

**Not reported.** No transcriptomic, proteomic, metabolomic, single-cell or screen data were found.

---

## 7. Anatomical structures affected

- **Primary:** thymus (hypoplastic in P1; UBERON:0002370), lymphoid tissue and blood.
- **Secondary:** upper and lower airways, gut, liver and biliary tree, skin, CNS (cryptococcal meningitis, PML) and thyroid.
- **Cells:** naïve and effector memory T cells, Th17 cells, B cells, medullary thymic epithelial cells and fibroblasts.
- **Subcellular:** cytoplasm to nucleus translocation of the RelB/p52 dimer.
- **Lateralization:** not applicable; the disease is systemic.

---

## 8. Temporal development

- **Onset:** infancy to childhood in the complete-deficiency families. Partial deficiency can present later, and the two adults in Le Voyer 2024 were diagnosed in adulthood.
- **Progression:** progressive immune decline and escalating organ autoimmunity in the second decade (P364L).
- **Duration:** lifelong without definitive therapy.
- **Remission:** no spontaneous remission is described.
- **Critical period:** early HSCT in infancy is associated with survival in the complete-deficiency children (search summary; *unverified*).

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007). Consanguinity is documented in all three kindreds with homozygous variants.
- **Prevalence and incidence:** not documented (`prevalence_class: NOT_YET_DOCUMENTED`). At most 8 patients have been published.
- **Populations:** Turkish, Iranian Jewish, and (per the 2015 report) other consanguineous families.
- **Penetrance, anticipation, mosaicism, carrier frequency:** no data. Heterozygous parents were healthy in the families reported.
- **Founder effect:** P364L has been seen in two unrelated reports. This is a lead, not evidence of a founder effect.
- **Sex ratio:** both sexes are affected.

---

## 10. Diagnostics

- **Immunophenotyping:**
  - Low naïve CD4⁺ and CD8⁺ T cells.
  - Raised CD4/CD8 ratio, per [MalaCards](https://www.malacards.org/card/immunodeficiency_53) and the aggregator snippets.
  - Reduced TREC levels, per MalaCards (secondary).
  - Low memory B cells, hypogammaglobulinemia and poor vaccine responses.
  - Reduced PHA and anti-CD3 proliferation (Sharfe 2022).
- **Functional assays:**
  - Fibroblast stimulation with lymphotoxin or TWEAK, reading out *NFKB2* and *VCAM1*.
  - Western blot for RelB protein.
- **Autoantibodies:** neutralizing anti-type I IFN antibody testing. These antibodies appeared about 5 years after HSCT in P1.
- **Genetic testing:**
  - WES or WGS, or an inborn-errors-of-immunity panel that includes *RELB*.
  - Sanger confirmation.
  - Segregation analysis in consanguineous families.
- **Differential diagnosis:** other combined immunodeficiencies (NIK/MAP3K14 deficiency, which shares the alternative NF-κB pathway; NFKB2 haploinsufficiency; APS-1/AIRE deficiency; CD40 ligand deficiency).
- **Screening:** reduced TRECs might be detectable on newborn screening. No program is established.

---

## 11. Outcome and prognosis

- Survival data are limited to individual cases.
  - P2 died of progressive multifocal leukoencephalopathy at age 34.
  - P1 was alive 3 years post-HSCT with normal immunoglobulins.
- Complications are CNS infection, lymphoma (P2), liver disease and lung damage requiring lobectomy.
- Prognostic factors are unknown. Complete deficiency presents earlier and more severely.
- No quality-of-life instruments have been applied.

---

## 12. Treatment

- **Definitive:** allogeneic HSCT.
  - P1 had HSCT at age 14 from a fully matched sibling, with successful engraftment ([Le Voyer 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11406260/)).
  - At 6 months, most T-cell cytokine defects and naïve B-cell defects had corrected. IL-17A/F production stayed low.
  - At 3 years, B-cell proportions and immunoglobulin levels were normal, IVIg had been stopped, and no fungal infection occurred.
  - Anti-IFN autoantibodies persisted.
  - NCIT suggestion: hematopoietic cell transplantation (NCIT:C15431), `therapeutic_modality: CELL_THERAPY`.
- **Supportive:** immunoglobulin replacement (used in Sharfe 2022 siblings and in P1 before HSCT), antimicrobial prophylaxis or treatment, and rituximab (given to P2).
  - NCIT suggestion: Pharmacotherapy (NCIT:C15986). Bind specific agents as `therapeutic_agent` only after a CHEBI or NCIT lookup.
- **Surgical:** lobectomy for chronic bronchiolitis (Sharfe 2022).
- **Not found:** gene therapy, targeted therapy and clinical trials. I did not search ClinicalTrials.gov, so absence is unconfirmed.
- Whether HSCT stops autoimmunity of stromal origin is unknown, because the autoantibodies persisted.

---

## 13. Prevention

- Genetic counseling for families, with carrier testing of relatives and prenatal or preimplantation diagnosis in known families.
- Early diagnosis permits prophylaxis and early HSCT.
- No vaccination guidance specific to RELB deficiency was found. Live vaccines are usually avoided in combined immunodeficiency, but I did not find a source stating this for IMD53.

---

## 14. Other species and natural disease

No naturally occurring animal disease is documented (OMIA not checked). *Relb* is conserved across mammals. The mouse ortholog is *Relb* (MGI).

---

## 15. Model organisms

- ***Relb* knockout mice** die at 2–6 weeks from severe, T-cell-dependent, multi-organ inflammation (Le Voyer 2024 discussion).
  - Human patients show a narrower picture: mainly infection, IFN autoantibodies and, in partial deficiency, organ autoimmunity.
  - Fidelity is therefore partial (`PARTIALLY_RECAPITULATES`, `fidelity: MODERATE`).
  - Limitation: species difference in the severity and timing of autoimmunity.
- **Conditional mouse models:** a *Relb* knockout restricted to medullary thymic epithelial cells gives T-cell infiltration of liver, lung and skin. This resembles the organ pattern of the partial-deficiency patients and supports an epithelial-intrinsic role in central tolerance (Le Voyer 2024 discussion). Use `evidence_source: MODEL_ORGANISM`.
- **In vitro:** patient fibroblasts, T cells and B cells (`IN_VITRO`).
- No zebrafish, *Drosophila* or iPSC models were found. I searched only briefly.

---

## Curation cautions

- **PMIDs read in full text:** 39231201 (Le Voyer 2024, PNAS) and 36402602 (Sharfe 2022, *J Autoimmun*). Page 1 of the Le Voyer text covers only the first 100,000 of 139,108 characters.
- **Snippets are not verified.** WebFetch returned summaries because of its 125-character quote limit. Do not paste any wording from this report as a snippet. Run `just fetch-reference PMID:39231201` and `PMID:36402602`, then copy the exact sentences from the cache files.
- **Fetch before use:** PMID 26385063 and the *LymphoSign* DOI.
- **Not read:** the 2022 Le Voyer study (autoantibodies in NIK and RELB deficiency, AIRE-expressing thymic cells) was cited only from search-result snippets.
- **Retrieval issue:** the PubMed fetch for 36402602 failed with a proxy error. I used the PMC copy instead.
- **Run `just preflight-dr`** on this report before using its content, per CLAUDE.md.
- **Record `RELB` gene validity only by copying** an external classification (ClinGen via `CGGV:` or GenCC), never by assigning one.

**Sources**
- [Le Voyer et al., PNAS 2024 (PMC11406260)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11406260/)
- [Sharfe et al., J Autoimmun 2022 (PMC10861023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10861023)
- [MalaCards: Immunodeficiency 53](https://www.malacards.org/card/immunodeficiency_53)
- [GenCC submission for RELB / MONDO:0054696](https://search.thegencc.org/submissions/GENCC_000102-HGNC_9956-MONDO_0054696-HP_0000007-GENCC_100004)
- [Disease Ontology DOID:0111992](https://disease-ontology.org/term/DOID:0111992)
- [DrugMap disease record](https://drugmap.idrblab.net/data/disease/details/DISQ3Q2J)
- [MedGen C4539811 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/src/branch/main/www.ncbi.nlm.nih.gov/medgen/C4539811/index.html)
- [GenCC SGC-106323.2](https://thegencc.org/submissions/SGC-106323.2)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0054696` (2 mentions) - the report calls it "MONDO"; MONDO calls it **immunodeficiency 53**
- `DOID:0111992` (5 mentions) - the report calls it "DOID"; DOID calls it **immunodeficiency 53**
- `HP:0100550` (1 mention) - the report calls it "P1 and P2"; HP calls it **Tendon rupture**
- `HP:0002014` (1 mention) - the report calls it "Siblings"; HP calls it **Diarrhea**
- `HP:0004322` (1 mention) - the report calls it "Oldest sibling (Sharfe 2022)"; HP calls it **Short stature**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003290` (1 mention), reported as "Sharfe 2022 siblings" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005407` (obsolete Decreased proportion of CD4-positive helper T cells) (1 mention) - replaced by `HP:0032218`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0038061` (1 mention) - the report calls it "GO: non-canonical NF-κB signal transduction"; GO calls it **non-canonical NF-kappaB signal transduction**
- `CL:0000895` (1 mention) - the report calls it "CL: naïve thymus-derived CD4-positive alpha-beta T cell"; CL calls it **naive thymus-derived CD4-positive, alpha-beta T cell**
- `NCIT:C15431` (1 mention) - the report calls it "NCIT suggestion: hematopoietic cell transplantation"; NCIT calls it **Hematopoietic Cell Transplantation**
- `NCIT:C15986` (1 mention) - the report calls it "NCIT suggestion: Pharmacotherapy"; NCIT calls it **Pharmacotherapy**