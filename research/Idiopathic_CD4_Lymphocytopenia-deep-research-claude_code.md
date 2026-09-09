---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-09T09:13:49.747824'
end_time: '2026-09-09T09:18:20.629814'
duration_seconds: 270.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Idiopathic CD4 Lymphocytopenia
  mondo_id: MONDO:0014226
  category: Complex
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
  web_search_requests: 17
  num_turns: 25
  total_cost_usd: 1.3729782000000001
  session_id: 268754b9-c110-5f10-8eb8-e32e8f9ae568
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 39
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 5
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0014226
    reported_labels:
    - MONDO
    - Disease
    ontology_label: idiopathic CD4 lymphocytopenia
  - term_id: HP:0004802
    reported_labels:
    - Lymphopenia
    ontology_label: Episodic hemolytic anemia
  - term_id: CL:0000624
    reported_labels:
    - "Cell type \u2014 CD4 T cell"
    ontology_label: CD4-positive, alpha-beta T cell
  labels_variant: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Idiopathic CD4 Lymphocytopenia
- **MONDO ID:** MONDO:0014226 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Idiopathic CD4 Lymphocytopenia** covering all of the
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

I'll research Idiopathic CD4 Lymphocytopenia (ICL) across multiple domains in parallel batches.

I have sufficient material now to compile a comprehensive report. Let me write the full research report.

Now I have comprehensive data to compile the full report.

# Idiopathic CD4 Lymphocytopenia (ICL): Comprehensive Research Report

## 1. Disease Information

### Overview
Idiopathic CD4 lymphocytopenia (ICL) is a rare, heterogeneous immunodeficiency syndrome defined by a persistent, unexplained depletion of circulating CD4+ T lymphocytes in the **absence** of HIV-1/HIV-2 infection or any other identifiable cause of immunosuppression [(Wikipedia)](https://en.wikipedia.org/wiki/Idiopathic_CD4+_lymphocytopenia); [(Dove Medical Press, "Current Insights")](https://www.dovepress.com/idiopathic-cd4-lymphocytopenia-current-insights-peer-reviewed-fulltext-article-ITT). It was first recognized as a distinct clinical entity by the U.S. CDC in 1992 after cases resembling AIDS were reported in patients who tested seronegative for HIV [(PMC7524466 — JCI autoantibody study)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7524466/). The disease spans a spectrum from an incidental, asymptomatic laboratory finding to a life-threatening AIDS-like illness with opportunistic infections, malignancy, and autoimmune disease [(NEJM 2023, "Reappraisal of ICL at 30 Years")](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348).

### Key Identifiers
| Database | ID |
|---|---|
| MONDO | MONDO:0014226 |
| OMIM | 615518 |
| Orphanet | ORPHA228000 |
| MedGen | C4706550 |

[(NORD MONDO page)](https://rarediseases.org/mondo-disease/idiopathic-cd4-lymphocytopenia/); [(MedGen)](https://www.ncbi.nlm.nih.gov/medgen/1644657); [(Orphanet)](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=228000&lng=EN); [(MalaCards — "Immunodeficiency 13")](https://www.malacards.org/card/immunodeficiency_13)

### Synonyms
ICL; idiopathic CD4+ T-lymphocytopenia; idiopathic CD4+ T-cell lymphopenia; non-HIV AIDS-like immunodeficiency (informal, historical); immunodeficiency 13 (as listed by some disease aggregators).

### CDC Diagnostic Definition (1992, still current)
1. Documented CD4+ T-lymphocyte count **< 300 cells/mm³** (or < 20% of total T cells) on **two separate occasions at least 6 weeks apart**
2. **No** serologic or virologic evidence of HIV-1 or HIV-2 infection at the time of the low CD4 count or subsequently
3. **No** other defined immunodeficiency, therapy, or condition (e.g., glucocorticoid/cytotoxic therapy, malignant lymphoma, sarcoidosis, other primary immunodeficiency) associated with depressed CD4 levels

[(PMC2924513 — refractory cryptococcal meningitis case)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2924513/); [(femspd/Oxford Academic update review)](https://academic.oup.com/femspd/article/54/3/283/512382)

ICL is essentially a **diagnosis of exclusion**, and CVID (common variable immunodeficiency) is explicitly excluded from the ICL diagnostic category as a separate, coexisting condition [(Dove Medical Press)](https://www.dovepress.com/idiopathic-cd4-lymphocytopenia-current-insights-peer-reviewed-fulltext-article-ITT).

### Data source note
Most modern mechanistic and epidemiologic knowledge of ICL derives from a small number of **aggregated, longitudinally followed cohorts** rather than large EHR datasets — chiefly the NIH/NIAID natural-history cohort (108 patients enrolled 2009–2020, reported in NEJM 2023) and earlier single-center cohorts (e.g., Zonios et al., *Blood* 2008, n=39-plus, ASH). Individual case reports (cryptococcal meningitis, PML, various cancers) supplement these aggregated series [(NEJM 2023)](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348); [(Blood 2008 — natural history and prognostic factors)](https://ashpublications.org/blood/article/112/2/287/24232/Idiopathic-CD4-lymphocytopenia-natural-history-and).

---

## 2. Etiology

### Disease causal factors
The cause of ICL is, by definition, unknown ("idiopathic"), and current evidence points to a **heterogeneous, multifactorial** syndrome rather than a single disease mechanism. It is **not** believed to be caused by a transmissible infectious agent — extensive early-1990s investigations found no evidence of a novel retrovirus or other pathogen, and ICL is not contagious [(NORD)](https://rarediseases.org/mondo-disease/idiopathic-cd4-lymphocytopenia/). Proposed contributing mechanisms (detailed in §6) include:
- Autoantibody-mediated CD4+ T-cell destruction
- Impaired homeostatic cytokine signaling (IL-7, IL-2)
- Defective thymic output / T-cell development
- Rare monogenic immune-gene defects unmasked as an ICL-like phenotype
- Altered chemokine receptor trafficking (CXCR4)
- Lymphopenia-driven immune dysregulation and secondary autoimmunity

### Genetic risk factors
No single causal gene explains most ICL cases; a genetic cause is identified in only a **minority** of patients after exome/targeted sequencing, and most patients remain without an identifiable monogenic defect [(NEJM 2023)](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348). Genes implicated in individual patients or small series:
- **RAG1 / RAG2** (hgnc:9827/9828 pattern loci) — hypomorphic ("leaky") missense variants producing a mild combined immunodeficiency phenotype that can present as isolated CD4 lymphopenia [(Arthritis Research & Therapy review)](https://link.springer.com/article/10.1186/ar4027); [(PMC4506145 — Leaky RAG deficiency in adults)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4506145/); [(PubMed 21502542 — RAG mutations)](https://pubmed.ncbi.nlm.nih.gov/21502542/)
- **MAGT1** — X-linked; causes XMEN syndrome (X-linked immunodeficiency with Magnesium defect, EBV infection, and Neoplasia), which can present with a CD4-lymphopenic phenotype due to impaired Mg2+ flux affecting thymic CD4 T-cell production [(Arthritis Research & Therapy)](https://link.springer.com/article/10.1186/ar4027)
- **JAK3** — somatic chimerism reported evolving into predominant CD4+ lymphopenia in a combined immunodeficiency case [(J Clin Immunol — JAK3 somatic chimerism)](https://link.springer.com/article/10.1007/s10875-014-0088-2)
- **CD4** gene itself — a homozygous inherited CD4 mutation causing complete multilineage CD4 expression defect, presenting with warts (HPV disease) [(PMC6856949)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6856949/)
- **DOCK8, UNC119, STK4 (MST1), ITK** — additional genes reported in small numbers of patients with pleiotropic immune effects not restricted to CD4+ T cells [(Dove Medical Press)](https://www.dovepress.com/idiopathic-cd4-lymphocytopenia-current-insights-peer-reviewed-fulltext-article-ITT)

These findings support the framing of "ICL" as partly a phenotypic convergence point for several distinct, rare monogenic immunodeficiencies once other explanations (HIV, malignancy, iatrogenic causes) have been excluded — rather than a single disease entity.

### Environmental/other risk factors
No specific toxin, occupational exposure, or lifestyle factor has been consistently linked to ICL onset. Age at presentation is typically in the **fourth decade of life** [(femspd review)](https://academic.oup.com/femspd/article/54/3/283/512382). No strong sex predominance has been definitively established across cohorts, though case series show variable male:female ratios.

### Protective factors
No genetic or environmental protective factors have been described in the literature; this reflects the rarity and limited genetic-epidemiology work on the condition rather than a documented absence.

### Gene-environment interactions
Not systematically studied given the disease's rarity and the small size of available cohorts.

---

## 3. Phenotypes

ICL's phenotype is defined primarily by its **complications** rather than intrinsic symptoms of the lymphopenia itself — many patients are identified incidentally on routine bloodwork and remain asymptomatic for years [(femspd review)](https://academic.oup.com/femspd/article/54/3/283/512382).

### Core laboratory phenotype
- **CD4+ T-lymphocytopenia**: absolute CD4 count < 300/mm³ or < 20% of total T cells, confirmed on ≥2 occasions ≥6 weeks apart (HP:0032101 "Reduced CD4 T-cell count" or the more general HP:0004802 "Lymphopenia" is the closest bindable HPO parent; a specific ICL-appropriate CD4-count term should be checked against current HPO release)
- Median CD4 count in the largest cohort (NIH, n=108) was **80 cells/mm³** — considerably below the diagnostic threshold of 300, and comparable to AIDS-defining levels [(NEJM 2023)](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348)
- CD4 decline in ICL is typically **slow/indolent**, contrasting with the more dynamic decline seen in untreated HIV infection [(femspd review)](https://academic.oup.com/femspd/article/54/3/283/512382)

### Infectious phenotypes (opportunistic infections)
From the NIH cohort (n=108, most comprehensively characterized):
- **HPV-related disease** — most prevalent complication, in **29%** (NEJM 2023) to 34.4% (other series) of patients — condylomata, cervical/anal/vulvovaginal dysplasia and cancer (HP term candidates: warts, HPV-associated dysplasia)
- **Cryptococcosis** — **24%** (NEJM 2023) to 22% in other cohorts; cryptococcal meningitis is a classic, sometimes refractory, presentation [(PMC2924513)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2924513/); [(PMC10496933 — acute cryptococcal meningitis case)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10496933/)
- **Molluscum contagiosum** — 9% (NEJM 2023)
- **Nontuberculous mycobacterial (NTM) disease** — 5% (NEJM 2023), sometimes described as a major presenting infection in other series
- **Varicella zoster virus** (dermatomal/disseminated shingles) — ~15.5% in some series
- **Progressive multifocal leukoencephalopathy (PML)**, caused by JC virus reactivation — rare but reported; ICL is one of the few non-HIV, non-hematologic-malignancy causes of PML [(Journal of NeuroVirology — PML in ICL, case report and lit review)](https://link.springer.com/article/10.1007/s13365-018-0638-0); [(PubMed 11049808)](https://pubmed.ncbi.nlm.nih.gov/11049808/)
- Other reported infections: *Pneumocystis jirovecii* pneumonia, candidiasis, cytomegalovirus, disseminated histoplasmosis/blastomycosis (case reports) [(femspd review)](https://academic.oup.com/femspd/article/54/3/283/512382); [(PMC5415924 — severe PJP case)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5415924/); [(PMC2926907 — disseminated blastomycosis)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2926907/)

Overall, the pattern of opportunistic infection resembles but is distinct from HIV/AIDS — the incidence and severity of infections in ICL is generally **lower** than in comparably CD4-depleted AIDS patients, suggesting that CD4 count alone does not fully capture the functional immunodeficiency of ICL [(Wikipedia)](https://en.wikipedia.org/wiki/Idiopathic_CD4+_lymphocytopenia).

### Neoplastic phenotypes
Fourteen invasive cancers were identified across 13 of 108 patients in the NIH cohort, spanning: anal cancer, vulvovaginal cancer, oral cavity/pharyngeal cancer, lung squamous-cell carcinoma, papillary thyroid carcinoma, prostate and breast adenocarcinoma, non-Hodgkin lymphoma, and Kaposi sarcoma [(Physician's Weekly summary of NEJM 2023)](https://www.physiciansweekly.com/post/idiopathic-cd4-lymphocytopenia-linked-to-opportunistic-infection-cancer); [(NEJM 2023)](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348). ICL patients showed a **significantly higher prevalence** of six specific cancers (anal, vulvovaginal, oral cavity/pharynx, papillary thyroid carcinoma, non-Hodgkin lymphoma, Kaposi sarcoma) compared with the age/sex-matched general population — a pattern strongly overlapping with HPV- and herpesvirus (KSHV)-associated malignancies, consistent with impaired immune surveillance of oncogenic viruses.

### Autoimmune phenotypes
Reported in roughly **23%** of patients in one series (Zonios et al.) [(WebSearch synthesis of multiple sources)](https://www.dovepress.com/idiopathic-cd4-lymphocytopenia-current-insights-peer-reviewed-fulltext-article-ITT):
- Systemic lupus erythematosus, antiphospholipid antibody syndrome
- Sjögren syndrome (most common in some series), sarcoidosis, psoriasis
- Lichen planus, vitiligo [(PubMed 12004324 — ICL and vitiligo)](https://pubmed.ncbi.nlm.nih.gov/12004324/), Graves' disease, Hashimoto thyroiditis
- Ulcerative colitis, immune thrombocytopenia, autoimmune hemolytic anemia
- Behçet syndrome, polyarthritis/vasculitis

### Phenotype-severity relationship (from NEJM 2023, n=108)
- **CD4 < 100/mm³** vs. 101–300/mm³ was associated with:
  - Higher odds of opportunistic infection: **OR 5.3 (95% CI 2.8–10.7)**
  - Higher odds of invasive cancer: **OR 2.1 (95% CI 1.1–4.3)**
  - **Lower** odds of autoimmunity: **OR 0.5 (95% CI 0.2–0.9)** — a striking inverse relationship, suggesting autoimmune complications may be more linked to residual lymphopenia-driven proliferation than to profound depletion
[(NEJM 2023 excerpted findings via search synthesis)](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348)

### Quality of life
Systematic QoL instrument data (EQ-5D, SF-36) specific to ICL were not identified in available literature; QoL impact is inferred qualitatively from the disease's chronic infectious/oncologic/autoimmune burden and diagnostic uncertainty rather than from dedicated PRO studies.

---

## 4. Genetic/Molecular Information

See §2 for gene-level detail. Summary table:

| Gene (HGNC) | Role in ICL-like phenotype | Notes |
|---|---|---|
| RAG1 / RAG2 | Hypomorphic V(D)J recombination defect → leaky SCID-like phenotype presenting as CD4 lymphopenia in adults | [PMC4506145](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4506145/) |
| MAGT1 | X-linked Mg²⁺-transporter defect (XMEN syndrome) → impaired thymic CD4 production, EBV susceptibility | [Arthritis Res Ther review](https://link.springer.com/article/10.1186/ar4027) |
| JAK3 | Somatic chimerism → evolving combined immunodeficiency with predominant CD4 lymphopenia | [J Clin Immunol](https://link.springer.com/article/10.1007/s10875-014-0088-2) |
| CD4 | Homozygous structural mutation → multilineage CD4 expression defect | [PMC6856949](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6856949/) |
| DOCK8, UNC119, STK4, ITK | Reported in isolated cases; pleiotropic immune effects | [Dove Medical Press](https://www.dovepress.com/idiopathic-cd4-lymphocytopenia-current-insights-peer-reviewed-fulltext-article-ITT) |

**Variant classification/pathogenicity**: Not systematically curated in ClinVar for "ICL" as an indication (these variants are typically classified under their primary disease association — SCID/CID for RAG1/2, XMEN for MAGT1). No dedicated ICL-specific pathogenic variant panel exists.

**Somatic vs. germline**: The JAK3 case demonstrates a somatic, not germline, mechanism — an important reminder that not all genetically-attributable ICL is heritable.

**Epigenetics**: No dedicated epigenetic (DNA methylation, histone modification) studies in ICL were identified in the literature search.

**Chromosomal abnormalities**: None specifically reported as a recurrent ICL mechanism; ICL is generally a single-gene or non-genetic disorder rather than a chromosomal syndrome.

**Important caveat**: In the largest genetically-characterized cohort (NIH, n=108), only a **minority** of patients had an identifiable pathogenic variant after whole-exome and targeted sequencing — genetic causes do not explain most ICL cases, reinforcing its classification as etiologically heterogeneous rather than monogenic [(NEJM 2023)](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348).

---

## 5. Environmental Information

No specific environmental toxin, chemical exposure, or occupational risk factor has been established as causal for ICL. Infectious triggers have been investigated but **not confirmed** — early studies specifically ruled out a novel transmissible retrovirus as a cause after ICL was first described in the early 1990s [(NORD)](https://rarediseases.org/mondo-disease/idiopathic-cd4-lymphocytopenia/). No lifestyle factor (smoking, diet, alcohol) has a documented causal association in the literature reviewed.

Infectious agents are relevant to ICL primarily as **secondary, opportunistic complications** rather than causal triggers (see §3): *Cryptococcus neoformans*, nontuberculous mycobacteria, human papillomavirus, JC virus (PML), varicella-zoster virus, *Pneumocystis jirovecii*, and Epstein-Barr virus (particularly in MAGT1/XMEN-associated cases).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (synthesized from current literature; branches reflect genuine mechanistic heterogeneity)

1. An initiating lesion — in most patients **unidentified**; in a minority, a hypomorphic monogenic defect (RAG1/RAG2, MAGT1, JAK3 somatic mosaicism, CD4 structural mutation) — **leads to** impaired CD4+ T-cell generation and/or accelerated peripheral loss. *[Inferred for the "unidentified" majority from downstream immunologic findings, since the trigger itself is not observed.]*
2. **Branch A — Autoimmune/humoral mechanism:** Loss of self-tolerance (mechanism not fully defined, possibly downstream of chronic lymphopenia itself — see step 5) **results in** production of IgG/IgM autoantibodies against a broad panel of autoantigens, some specific to lymphocytes; roughly 30% of patients have IgG anti-CD4+ T-cell antibodies **leading to** antibody-dependent cellular cytotoxicity (ADCC) and complement-dependent cytotoxicity (in vivo classical complement activation detected on CD4+ T cells in ~14% of one cohort), which **directly destroys peripheral CD4+ T cells** [(JCI 2020, Perez-Diez et al., "Prevalence and pathogenicity of autoantibodies")](https://www.jci.org/articles/view/136254); [(PMC7524466)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7524466/); [(JCI 2020, "Expanding mechanistic insights")](https://www.jci.org/articles/view/141717).
3. **Branch B — Homeostatic cytokine signaling defect:** IL-7 is the principal homeostatic cytokine driving naive CD4+ T-cell survival and proliferation in lymphopenic hosts. In ICL, serum IL-7 is **paradoxically elevated** (inversely correlating with CD4 count, a compensatory response to lymphopenia analogous to that seen in HIV) yet CD4+ T cells show **diminished phospho-STAT5 induction after IL-7 stimulation**, correlating with decreased surface CD127 (IL-7Rα) expression — **resulting in** impaired IL-7-driven homeostatic proliferation and survival signaling despite abundant ligand [(PMC3559496, "Altered Responses to Homeostatic Cytokines")](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3559496/); [(JCI 2020, "Expanding mechanistic insights")](https://www.jci.org/articles/view/141717). IL-2 signaling is similarly impaired, further compounding the homeostatic failure.
4. **Branch C — Chemokine receptor trafficking defect:** CD4+ T cells in ICL patients show profound **loss of surface CXCR4** expression with abnormal intracellular accumulation of CXCR4 and its ligand CXCL12, **leading to** decreased chemotactic response to CXCL12 (while CXCL8 responsiveness is preserved) and impaired receptor recycling after ligand-induced endocytosis. In vitro IL-2 exposure normalized surface CXCR4 in 5/6 patients tested, linking Branches B and C mechanistically — **suggesting that impaired cytokine signaling upstream drives downstream chemokine receptor mistrafficking**, which could impair T-cell homing to lymphoid niches necessary for survival and homeostatic proliferation [(Blood 2010, Scott-Algara/Balabanian/Chakrabarti et al.)](https://ashpublications.org/blood/article/115/18/3708/27330/Idiopathic-CD4-T-cell-lymphocytopenia-is).
5. Despite suboptimal γc-cytokine responses, ICL patients show **increased CD4+ T-cell activation and turnover** (elevated HLA-DR, Ki-67, ex vivo BrdU labeling) and evidence of ongoing **homeostatic/spontaneous proliferation converting naive cells to memory-like proliferating cells** — this proliferative stress **is proposed to** expand self-reactive T-cell clones and **feed back into Branch A**, generating secondary autoantibodies and autoimmune phenotypes via classic lymphopenia-induced-proliferation breakdown of tolerance [(PLOS ONE, "Altered Responses to Homeostatic Cytokines")](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0055570); [(JCI 2020)](https://www.jci.org/articles/view/141717).
6. In parallel, **disturbed differentiation of hematopoietic/thymic stem-cell precursors** and reduced thymic output are proposed to contribute to the failure to replace lost CD4+ T cells, since continuous thymic activity is normally required to sustain IL-7-driven naive CD4+ T-cell homeostasis; this branch is less directly demonstrated in ICL than Branches A–C and remains a plausible contributing rather than proven mechanism [(JCI 2020)](https://www.jci.org/articles/view/141717); [(PMC5243809 — thymic activity and IL-7-induced naive CD4 proliferation)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5243809/).
7. Increased apoptotic susceptibility (elevated CD95/Fas expression) has also been reported and may **compound** peripheral CD4+ T-cell loss independent of autoantibody-mediated cytotoxicity.
8. **Net convergent effect:** profound, chronic CD4+ T-lymphocytopenia with qualitatively impaired homeostatic reserve **leads to** (a) failure of immune surveillance against oncogenic and opportunistic pathogens (→ HPV disease, cryptococcosis, NTM, PML — see §3) and (b) a paradoxical predisposition to autoimmunity via lymphopenia-driven proliferation and tolerance breakdown (→ SLE, Sjögren, vitiligo, etc.).

### Category detail

- **Molecular pathways**: IL-7/JAK-STAT5 signaling (impaired); IL-2/JAK-STAT5 signaling (impaired); CXCR4/CXCL12 chemokine axis (surface receptor trafficking defect); complement activation cascade (classical pathway, autoantibody-triggered). Suggested pathway/process resources: KEGG hsa04630 (JAK-STAT), Reactome "Interleukin-7 signaling," GO biological process terms below.
- **Cellular processes**: impaired T-cell homeostatic proliferation; ADCC and complement-dependent cytotoxicity of CD4+ T cells; lymphopenia-induced proliferation; apoptosis (elevated CD95 expression). Suggested GO terms: GO:0042110 (T cell activation), GO:0002376 (immune system process), GO:0006915 (apoptotic process), GO:0038110 (interleukin-7-mediated signaling pathway), GO:0038110-adjacent IL-2 signaling terms, GO:0006935 (chemotaxis) / GO:0038147 (CXCR chemokine receptor signaling pathway).
- **Protein dysfunction**: reduced CD127 (IL-7Rα, gene IL7R) surface expression; impaired CXCR4 membrane trafficking/recycling; in monogenic subsets, RAG1/RAG2 recombinase hypomorphism or MAGT1 Mg²⁺-transporter loss of function.
- **Immune system involvement**: this is fundamentally an immune-cell-intrinsic disorder — both immunodeficiency (opportunistic infection/malignancy susceptibility) and autoimmunity coexist, a combination that is itself a notable and somewhat paradoxical feature of the mechanism.
- **Tissue damage mechanisms**: not a primary structural/fibrotic disease; tissue pathology is secondary to opportunistic infection (e.g., cryptococcal meningoencephalitis, JC virus-mediated oligodendrocyte lysis in PML) or malignancy.
- **Molecular profiling**: No large-scale transcriptomic, proteomic, or single-cell atlases specific to ICL were identified in this search; most mechanistic data derive from targeted flow cytometry, cytokine-signaling assays (phospho-flow for STAT5), and autoantigen protein-array screens (JCI 2020 used a ~9,000-protein human proteome array plus a 128-known-autoantigen array) [(JCI 2020)](https://www.jci.org/articles/view/136254).

### Suggested cell types (CL) and anatomical involvement (see §7)
CD4+ T cell (CL:0000624), naive CD4+ T cell (CL:0000895), thymocyte (CL:0000893), regulatory/memory subsets as relevant.

---

## 7. Anatomical Structures Affected

- **Organ level (primary)**: The immune system itself is the primary "organ" affected — peripheral lymphoid tissue and, per mechanistic hypotheses, the thymus (site of T-cell development/output). Bone marrow is implicated via stem/progenitor differentiation hypotheses and is also a diagnostic site to exclude other causes (e.g., GATA2/MonoMAC, myelodysplasia) (UBERON:0002370 thymus; UBERON:0002371 bone marrow; UBERON:0002319 secondary lymphoid organ / UBERON:0000029 lymph node).
- **Secondary/complication-driven organ involvement**: CNS (cryptococcal meningitis, PML — UBERON:0001017 central nervous system), skin/mucosa (HPV warts, molluscum, VZV — UBERON:0002097 skin), anogenital and oropharyngeal mucosa (HPV-associated dysplasia/cancer), lung (NTM, PJP, squamous cell carcinoma — UBERON:0002048 lung), thyroid (papillary carcinoma — UBERON:0002046 thyroid gland).
- **Body systems involved**: immune system (primary); nervous system, integumentary system, respiratory system, endocrine system, and reproductive/genitourinary system (secondary, via infectious/oncologic complications).
- **Tissue and cell level**: T-lymphocyte compartment specifically — CD4+ T cells (CL:0000624) are depleted; CD8+ T cells and other lineages are generally relatively preserved (distinguishing ICL from the multilineage cytopenias of GATA2/MonoMAC — see §10).
- **Subcellular level**: Plasma membrane receptor trafficking defect (CXCR4 mislocalized to intracellular compartments rather than surface — GO:0005886 plasma membrane vs. endosomal/intracellular vesicle compartments); JAK-STAT signaling machinery (cytoplasmic/nuclear STAT5 translocation impaired).
- **Localization/laterality**: Not a lateralized disease; complications are typically systemic or site-specific to the given opportunistic infection/malignancy rather than symmetric/asymmetric in the classic sense.

---

## 8. Temporal Development

- **Onset**: Most commonly diagnosed in the **fourth decade of life** (30s–40s), though case reports span a wider age range including elderly and, less commonly, pediatric presentations [(femspd review)](https://academic.oup.com/femspd/article/54/3/283/512382).
- **Onset pattern**: Typically insidious/chronic rather than acute; the underlying CD4 decline is thought to occur gradually, often discovered incidentally or at first opportunistic infection.
- **Progression**: CD4 decline is **slow** relative to HIV — a key distinguishing feature. Course is highly variable: some patients remain stable with mild-to-moderate lymphopenia for years/decades, others progress to profound depletion (<100 cells/mm³) with serious complications.
- **Disease course pattern**: Chronic and generally lifelong once established; not classically relapsing-remitting, though individual complications (autoimmune flares, infections) can be episodic.
- **Remission**: Spontaneous CD4 count normalization has been reported anecdotally in some patients but is not the norm; no established treatment reliably induces durable remission (see §12).
- **Critical periods**: Not well defined; the CDC's two-time-point-6-weeks-apart requirement itself reflects the recognized need to distinguish a transient/reactive CD4 dip from true persistent ICL.

---

## 9. Inheritance and Population

### Epidemiology
ICL is **extremely rare**, and true population prevalence/incidence is not well established:
- A blood-donor screening study identified **0/2,028** cases with unexplained persistent low CD4 counts.
- A larger multi-cohort study (275 donors + 970 transfusion recipients + 947 household contacts) found **12/2,192 (0.5%)** with CD4 < 300/mm³ on ≥2 occasions without identifiable cause.
- A screening of 2,713 HIV-seronegative men who have sex with men found no persistent unexplained low-CD4 cases.

[(WebSearch synthesis of epidemiologic literature)](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348); [(femspd review)](https://academic.oup.com/femspd/article/54/3/283/512382)

These figures suggest a prevalence on the order of well under 1% even in screened at-risk populations, consistent with ICL's status as an ultra-rare condition — Orphanet lists it in its rare-disease registry (ORPHA228000).

### Inheritance pattern
No single Mendelian inheritance pattern applies to ICL as a syndrome, since most cases lack an identified genetic cause. Where a monogenic cause is found:
- **RAG1/RAG2**-associated leaky phenotype: typically autosomal recessive (biallelic hypomorphic variants), consistent with RAG-deficiency spectrum disorders
- **MAGT1**/XMEN: X-linked recessive
- **CD4** structural mutation case: reported as homozygous (autosomal recessive pattern in that kindred)
- **JAK3** somatic chimerism case: non-heritable (somatic, not germline)

Penetrance, expressivity, anticipation, mosaicism, founder effects, and carrier frequency data specific to "ICL" are not established, since these concepts apply to the underlying monogenic causes (RAG1/2, MAGT1, etc.) rather than to ICL as a unified entity.

### Population demographics
- No clear ethnic/geographic predisposition has been established in the literature reviewed; cohorts are drawn predominantly from U.S. tertiary/NIH referral populations, which limits generalizability.
- Sex ratio: not consistently reported as skewed in the major cohorts identified.
- Age distribution: peak recognition in adulthood (30s–40s), reflecting time needed to accumulate the complications that prompt diagnostic workup, plus possible under-ascertainment in children.

---

## 10. Diagnostics

### Clinical/laboratory tests
- **Flow cytometry** for absolute CD4+ T-lymphocyte count and percentage (the defining test), repeated ≥6 weeks apart
- HIV-1/HIV-2 serology and viral load/nucleic acid testing (mandatory to exclude HIV)
- Complete blood count with differential (to assess for concurrent cytopenias suggestive of alternative diagnoses)
- Immunoglobulin levels and vaccine-response titers (to exclude CVID/humoral immunodeficiency as the primary process)
- Autoantibody panels (ANA, and in research settings the broader autoantigen arrays used by NIAID investigators) given the autoimmune-association mechanism

### Genetic testing
- Whole-exome sequencing and/or targeted immunodeficiency gene panels are now used in specialized centers (e.g., the NIH natural-history study performed WES/targeted sequencing on its full cohort), looking for RAG1/RAG2, MAGT1, JAK3, CD4, DOCK8, UNC119, STK4, ITK, and other primary-immunodeficiency genes [(NEJM 2023)](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348)
- GATA2 mutational analysis is specifically recommended when there is coexisting monocytopenia, NK-cell or B-cell lymphopenia, or a family/personal history suggestive of GATA2 deficiency/MonoMAC syndrome, since these entities overlap phenotypically with ICL but require distinct management [(Haematologica — MonoMAC vs. ICL commentary)](https://haematologica.org/article/view/6284); [(Blood 2015 — GATA2-deficiency bone marrow disorder)](https://ashpublications.org/blood/article/125/1/56/33928/GATA2-deficiency-associated-bone-marrow-disorder)

### Bone marrow examination
May be indicated to rule out marrow-based causes (myelodysplasia, GATA2/MonoMAC, hairy cell leukemia and other marrow infiltrative causes of lymphopenia) when the clinical picture is ambiguous.

### Differential diagnosis
| Distinguish from | Key differentiating feature |
|---|---|
| HIV/AIDS | Negative HIV serology/viral load; typically slower CD4 decline |
| Common variable immunodeficiency (CVID) | CVID has hypogammaglobulinemia and poor vaccine responses as the primary defect; explicitly excluded from ICL definition |
| GATA2 deficiency / MonoMAC syndrome | Profound **monocytopenia** plus NK- and B-cell lymphopenia (multilineage), often with marrow dysplasia and family history; GATA2 sequencing confirms |
| Sarcoidosis, malignant lymphoma, glucocorticoid/cytotoxic therapy | Explicitly excluded per CDC criteria — must be ruled out as the cause of the CD4 depletion |

### Screening
No population-based or newborn screening program exists for ICL; case detection is opportunistic (incidental low CD4 on workup for infection, autoimmune disease, or unrelated illness).

---

## 11. Outcome/Prognosis

The most authoritative outcome data come from the NIH cohort (n=108, 374 person-years of follow-up) [(NEJM 2023)](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348):

- **Mortality**: 5 deaths among 91 evaluable patients; death rate **1.337 per 100 person-years**, versus **0.854 per 100 person-years** in the age/sex-matched general U.S. population — i.e., overall mortality risk was **not significantly elevated** compared to the general population, despite the immunodeficiency.
- **Cancer burden**: significantly **higher** prevalence than expected for six specific cancer types (anal, vulvovaginal, oral cavity/pharynx, papillary thyroid, non-Hodgkin lymphoma, Kaposi sarcoma), predominantly virus-associated malignancies.
- **Prognostic stratification by CD4 count** (< 100 vs. 101–300 cells/mm³):
  - Opportunistic infection: OR 5.3 (95% CI 2.8–10.7) for the lower-CD4 group
  - Invasive cancer: OR 2.1 (95% CI 1.1–4.3)
  - Autoimmunity: OR 0.5 (95% CI 0.2–0.9) — i.e., **inversely** associated with the lowest CD4 stratum
- Complication risk (infection, cancer) thus **increases with lower CD4 nadir**, while autoimmune complications appear relatively **more common in the less severely depleted** group, an important nuance for risk counseling.

### Morbidity
Chronic disease burden driven by recurrent/refractory opportunistic infection (e.g., refractory cryptococcal meningitis), oncologic complications requiring standard cancer therapy, and autoimmune organ involvement. No validated ICL-specific disability index or QoL instrument was found.

### Recovery potential
Variable; some patients experience partial CD4 recovery over time or with treatment (IL-7 — see §12), but a durable "cure" is not established, and the condition is generally managed as chronic.

---

## 12. Treatment

There are **no FDA-approved, ICL-specific therapies** and **no dedicated management guidelines**; treatment is largely extrapolated from HIV/AIDS opportunistic-infection prophylaxis protocols plus experimental cytokine/cellular approaches [(PMC11044977 — case report/lit review)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044977/).

### Supportive/prophylactic care
- Opportunistic infection prophylaxis (e.g., *Pneumocystis* prophylaxis, antifungal/antimycobacterial vigilance) is generally guided by HIV/AIDS CD4-count-based thresholds, in the absence of ICL-specific evidence.
- Aggressive treatment of documented opportunistic infections using standard antimicrobial/antifungal regimens (e.g., amphotericin B/flucytosine induction for cryptococcal meningitis).
- Regular cancer screening (particularly HPV-associated: cervical, anal) given the demonstrated excess malignancy risk (NCIT candidate terms: NCIT:C15343 Cancer Screening).

### Cytokine-based immunotherapy (experimental)
- **Recombinant human IL-7 (rhIL-7 / CYT107)**: An open-label phase 1/2a dose-escalation trial (NCT00839436, "ICICLE") in ICL patients showed rhIL-7 was well tolerated at biologically active doses and produced a sustained **increase in circulating CD4 and CD8 T cells** and tissue-resident CD3+ T cells in gut mucosa and bone marrow; expanded cells retained functional cytokine-production capacity after mitogenic stimulation. Injection-site reactions were the most common adverse event [(Blood 2016, "Administration of interleukin-7 increases CD4 T cells in idiopathic CD4 lymphocytopenia")](https://ashpublications.org/blood/article/127/8/977/35153/Administration-of-interleukin-7-increases-CD4-T); [(PubMed 26675348)](https://pubmed.ncbi.nlm.nih.gov/26675348/)
- **Efineptakin alfa (NT-I7)**, a long-acting recombinant human IL-7: an NIH Clinical Center trial (NCT05600920) is evaluating intramuscular dosing once every 12 weeks for 3 total doses in ICL, as a follow-on to the earlier rhIL-7 work — reflecting continued 2020s-era clinical development of IL-7 pathway therapeutics for this indication [(CenterWatch — NCT05600920)](https://www.centerwatch.com/clinical-trials/listings/NCT05600920/a-single-arm-dose-escalation-trial-of-long-acting-recombinant-human-il-7-nt-i7-efineptakin-alfa-for-idiopathic-cd4-lymphopenia); [(WithPower — Phase 1/2 recruiting listing)](https://www.withpower.com/trial/phase-2-lymphopenia-10-2022-63f7c)
- Interleukin-2 and interferon-gamma have also been tried in difficult cases, though with more limited/anecdotal supporting data [(search synthesis)](https://link.springer.com/chapter/10.1007/978-3-030-57157-3_9)

### Cellular/transplant approaches
- **Allogeneic hematopoietic stem cell transplantation (HSCT)**, including fludarabine-based conditioning, has been reported (in case-level evidence) to restore CD4+ T-lymphocyte counts and immune function in ICL — reserved for severe, refractory cases given transplant-related risk [(search synthesis of case literature)](https://clinicaltrials.gov/study/NCT02015013)
- A dedicated NIH protocol (NCT02015013) studies hematopoietic stem cell mobilization in ICL patients (vs. healthy controls) specifically to characterize T-cell maturation and trafficking using murine xenograft models — reflecting ongoing translational interest in understanding thymic/marrow-derived T-cell reconstitution defects.

### Treatment of associated conditions
Malignancies and autoimmune diseases arising in the context of ICL are treated per standard oncologic and rheumatologic/immunologic protocols for the specific diagnosis, with attention to the patient's baseline immunodeficiency when selecting immunosuppressive or cytotoxic regimens.

### Suggested NCIT terms for treatment annotation
NCIT:C15986 (Pharmacotherapy) for cytokine therapy generally; NCIT:C15289 (Organ Transplantation) / NCIT:C15431 (Hematopoietic Cell Transplantation) for HSCT; NCIT:C15747 (Supportive Care) for prophylaxis; specific antimicrobial/antifungal agent terms as appropriate per infection treated.

---

## 13. Prevention

No validated primary prevention strategy exists because the etiology of most cases is unknown. Practical prevention efforts focus on **secondary/tertiary prevention** of complications:
- Regular CD4 monitoring in diagnosed patients to stratify infection/cancer risk (per the CD4<100 vs. 101–300 risk stratification above)
- HPV-related cancer screening (cervical, anal cytology/HPV testing) given demonstrated excess risk
- Vaccination (where immunologically appropriate) against vaccine-preventable pathogens, though live-attenuated vaccines require case-by-case risk assessment given the immunodeficiency
- Prompt evaluation and aggressive treatment of suspected opportunistic infections
- Genetic counseling is relevant only in the minority of patients with an identified monogenic cause (RAG1/2, MAGT1, CD4) and follows standard counseling for those specific conditions (autosomal recessive or X-linked recessive, as applicable)

No population-level public-health intervention (vector control, sanitation, environmental mitigation) applies, consistent with ICL's non-infectious, non-environmental (as currently understood) etiology.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary analog of "idiopathic CD4 lymphocytopenia" specifically was identified in this search (OMIA and comparable veterinary genetics databases were not found to list a corresponding entity). This likely reflects both the rarity/recency of ICL's characterization as a human clinical entity and limited comparative-pathology investigation, rather than confirmed absence in animals.

---

## 15. Model Organisms

- **Murine humanized/xenograft models**: The NIH protocol NCT02015013 explicitly uses **mobilized hematopoietic stem cells from ICL patients transplanted into murine hosts** to study human T-cell maturation and trafficking defects in vivo — this is the most directly disease-relevant model system identified, allowing assessment of whether the T-cell developmental defect is intrinsic to the hematopoietic/thymic progenitor compartment [(ClinicalTrials.gov NCT02015013)](https://clinicaltrials.gov/study/NCT02015013).
- **RAG-deficient mouse models**: Widely used to study spontaneous/homeostatic CD4+ and CD8+ T-cell proliferation in a lymphopenic host, informing (but not specific to) the homeostatic-proliferation mechanism proposed for ICL [(PMC6116856 — spontaneous proliferation of CD4+ T cells in RAG-deficient hosts)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6116856/).
- No conventional knockout/knock-in mouse line recapitulating idiopathic (non-monogenic) ICL exists, consistent with the syndrome's largely non-monogenic, likely acquired/multifactorial nature in most patients. For the minority with defined genetic causes, the relevant established models are those for the underlying gene (e.g., *Rag1⁻/⁻*/*Rag2⁻/⁻* mice for RAG-hypomorphic disease, *Magt1*-deficient mice/zebrafish for XMEN).

---

## Summary of Suggested Ontology Term Bindings (for curation reference)

| Concept | Suggested term | Note |
|---|---|---|
| Disease | MONDO:0014226 | Idiopathic CD4 lymphocytopenia |
| CD4 lymphopenia phenotype | HP:0004802 (Lymphopenia) or a more specific descendant if present in current HPO | verify exact HP ID against current release before binding |
| Cell type — CD4 T cell | CL:0000624 | helper T cell |
| Cell type — naive CD4 T cell | CL:0000895 | |
| Anatomy — thymus | UBERON:0002370 | |
| Anatomy — bone marrow | UBERON:0002371 | |
| GO — T cell activation | GO:0042110 | |
| GO — apoptotic process | GO:0006915 | |
| Gene — RAG1 | hgnc:9827 | verify against current HGNC |
| Gene — RAG2 | hgnc:9828 | verify against current HGNC |
| Gene — MAGT1 | hgnc:16449 | verify against current HGNC |
| Gene — CD4 | hgnc:1678 | verify against current HGNC |
| Treatment — IL-7 therapy | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent | efineptakin alfa / CYT107 |
| Treatment — HSCT | NCIT:C15431 | Hematopoietic Cell Transplantation |

*(All ontology CURIEs above are suggestions for downstream verification against live ontology lookups per this project's curation standards — they are not to be bound without independent confirmation.)*

---

## Key Sources
- [Reappraisal of Idiopathic CD4 Lymphocytopenia at 30 Years — NEJM 2023](https://www.nejm.org/doi/full/10.1056/NEJMoa2202348) (primary natural-history cohort, n=108)
- [Idiopathic CD4+ lymphocytopenia: natural history and prognostic factors — Blood 2008](https://ashpublications.org/blood/article/112/2/287/24232/Idiopathic-CD4-lymphocytopenia-natural-history-and)
- [Expanding mechanistic insights into the pathogenesis of idiopathic CD4+ T cell lymphocytopenia — JCI 2020](https://www.jci.org/articles/view/141717)
- [Prevalence and pathogenicity of autoantibodies in patients with idiopathic CD4 lymphopenia — JCI 2020](https://www.jci.org/articles/view/136254)
- [Altered Responses to Homeostatic Cytokines in Patients with Idiopathic CD4 Lymphocytopenia — PLOS ONE / PMC3559496](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3559496/)
- [Idiopathic CD4+ T-cell lymphocytopenia is associated with impaired membrane expression of CXCR4 — Blood 2010](https://ashpublications.org/blood/article/115/18/3708/27330/Idiopathic-CD4-T-cell-lymphocytopenia-is)
- [Idiopathic CD4 Lymphocytopenia: Current Insights — Immunotargets and Therapy 2020 (Dove Medical Press)](https://www.dovepress.com/idiopathic-cd4-lymphocytopenia-current-insights-peer-reviewed-fulltext-article-ITT)
- [Idiopathic CD4 lymphocytopenia and opportunistic infection — an update — Pathogens and Disease](https://academic.oup.com/femspd/article/54/3/283/512382)
- [Administration of interleukin-7 increases CD4 T cells in idiopathic CD4 lymphocytopenia — Blood 2016](https://ashpublications.org/blood/article/127/8/977/35153/Administration-of-interleukin-7-increases-CD4-T)
- [Idiopathic CD4 lymphocytopenia — Orphanet (ORPHA228000)](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=228000&lng=EN)
- [Idiopathic CD4+ lymphocytopenia — Wikipedia](https://en.wikipedia.org/wiki/Idiopathic_CD4+_lymphocytopenia)
- [Idiopathic CD4 Lymphocytopenia: A Case Report and Literature Review — PMC11044977](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044977/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 16 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014226` (2 mentions) - the report calls it "MONDO", "Disease"; MONDO calls it **idiopathic CD4 lymphocytopenia**
- `HP:0004802` (2 mentions) - the report calls it "Lymphopenia"; HP calls it **Episodic hemolytic anemia**
- `CL:0000624` (3 mentions) - the report calls it "Cell type — CD4 T cell"; CL calls it **CD4-positive, alpha-beta T cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0042110` (2 mentions) - the report calls it "T cell activation", "GO — T cell activation"; GO calls it **T cell activation**
- `GO:0006915` (2 mentions) - the report calls it "apoptotic process", "GO — apoptotic process"; GO calls it **apoptotic process**
- `GO:0038110` (2 mentions) - the report calls it "interleukin-7-mediated signaling pathway"; GO calls it **interleukin-2-mediated signaling pathway**
- `GO:0038147` (1 mention) - the report calls it "CXCR chemokine receptor signaling pathway"; GO calls it **C-X-C motif chemokine 12 receptor activity**
- `CL:0000895` (2 mentions) - the report calls it "Cell type — naive CD4 T cell"; CL calls it **naive thymus-derived CD4-positive, alpha-beta T cell**, and lists "naive CD4+ T cell" among its other names
- `UBERON:0002370` (2 mentions) - the report calls it "Anatomy — thymus"; UBERON calls it **thymus**
- `UBERON:0002371` (2 mentions) - the report calls it "Anatomy — bone marrow"; UBERON calls it **bone marrow**
- `NCIT:C15431` (2 mentions) - the report calls it "Hematopoietic Cell Transplantation", "Treatment — HSCT"; NCIT calls it **Hematopoietic Cell Transplantation**, and lists "HSCT" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0014226` - called "MONDO", "Disease"
- `GO:0042110` - called "T cell activation", "GO — T cell activation"
- `GO:0006915` - called "apoptotic process", "GO — apoptotic process"
- `NCIT:C15431` - called "Hematopoietic Cell Transplantation", "Treatment — HSCT"