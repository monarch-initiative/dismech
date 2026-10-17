---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-16T13:11:55.814227'
end_time: '2026-10-16T13:14:39.125096'
duration_seconds: 163.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 41
  mondo_id: MONDO:0032863
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
  web_search_requests: 3
  num_turns: 12
  total_cost_usd: 0.7949512000000002
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 11
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 13
  verified: 11
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0012206
    reported_labels:
    - Asthenozoospermia
    ontology_label: Abnormal sperm motility
  - term_id: HP:0012864
    reported_labels:
    - multiple flagellar abnormalities
    ontology_label: Abnormal sperm morphology
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 41
- **MONDO ID:** MONDO:0032863 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 41** covering all of the
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

I've pulled the main CFAP70 papers, and I'm now checking the 2019 variant details and the mouse knockout findings before writing the report.

# Research Report: Spermatogenic Failure 41 (SPGF41; MONDO:0032863)

**Scope and verification.** I did not read primary full texts or OMIM directly (OMIM and the eBioMedicine page returned HTTP 403). The content below comes from PubMed abstract summaries returned by a fetch tool and from secondary sources that mirror OMIM. Treat everything as a lead to verify. The tool paraphrased the abstracts, so none of the quoted-looking text here is a verified exact snippet. Run `just fetch-reference PMID:<id>` and copy exact quotes from `references_cache/` before using any of it as evidence. The exposure, treatment, model-organism and prevention sections are thin or inferred, and I flag that where it applies.

Repository state: `stubs/Spermatogenic_Failure_41.yaml` is `entry_type: UNDECIDED`, and `kb/disorders/Spermatogenic_Failure_41.yaml` is a 7-line skeleton with a name, category and `disease_term` only. The stub names CFAP70 as MONDO's causal gene.

## 1. Disease Information

- **Overview.** SPGF41 is an autosomal recessive form of male infertility caused by biallelic loss of function of *CFAP70*. It presents as oligo-astheno-teratozoospermia with multiple morphological abnormalities of the sperm flagella (MMAF). Affected men have no other reported symptoms. [Secondary: [MGI/OMIM:618670](https://informatics.jax.org/disease/OMIM:618670), [Disease Ontology DOID:0111912](https://disease-ontology.org/term/DOID:0111912), [MalaCards](https://malacards.org/card/spermatogenic_failure_41)]
- **Identifiers.** MONDO:0032863. OMIM #618670, which two MGI pages agree on. One search result suggested OMIM:619515, but that came from a garbled page layout and is unresolved. DOID:0111912. The Disease Ontology lists it under "spermatogenic failure", which is_a "autosomal recessive disease".
- **Synonyms.** SPGF41; spermatogenic failure 41; CFAP70-related MMAF; male infertility due to CFAP70 deficiency.
- **Source type.** Aggregated, from case reports and small cohorts. These are not EHR-derived.
- **Suggested classification.** `DISEASE` (a gene-defined Mendelian entry). It is a candidate for the `Spermatogenic_Failure` / MMAF grouping, but check existing groupings first.

## 2. Etiology

- **Causal factor.** Biallelic loss-of-function variants in *CFAP70* (10q22.2), which encodes an axonemal protein.
- **Risk and protective factors.** None known beyond genotype. No modifier genes, environmental risk factors, protective variants or gene-environment interactions are reported in what I retrieved.

## 3. Phenotypes

All items below come from the 2019 and 2023 human reports and the OMIM mirrors. Frequencies are not available. Both 2019 patients and the 2023 patient had the core features, and none had extra-genital findings.

| Phenotype | Suggested HPO (look up before binding) | Notes |
|---|---|---|
| Male infertility | HP:0003251 | Sole clinical complaint. |
| Asthenozoospermia | HP:0012206 | Severe. |
| Oligozoospermia | HP:0000798 | Reported in the OMIM description and the 2023 patient. |
| Teratozoospermia / MMAF | HP:0012864 (multiple flagellar abnormalities); verify | Short, absent, coiled, irregular-caliber flagella. |
| Tapered sperm head, short flagella | verify | Listed in the MGI phenotype line. |

- **Onset and course.** Lifelong, with presentation at the time of attempted conception. Course is stable. No source gave quality-of-life data.
- **Not reported.** No primary ciliary dyskinesia features (respiratory disease, situs inversus) in the retrieved sources. I did not search specifically for them, so treat "absent" as unconfirmed.

## 4. Genetic / Molecular Information

- **Gene.** *CFAP70* (cilia- and flagella-associated protein 70), 10q22.2. Look up the HGNC ID with `runoak` before writing it; the repo uses lowercase `hgnc:`.
- **Reported variants.**
  - Beurois et al. 2019 ([PMID:31621862](https://pubmed.ncbi.nlm.nih.gov/31621862/)): two unrelated men from a 167-man MMAF exome cohort. Patient 1 had homozygous c.1723-1G>T, a splice-acceptor change at exon 16. Patient 2 had homozygous p.Phe60Ile in exon 3, a missense variant judged likely deleterious.
  - Jin et al. 2023 ([PMID:37352829](https://pubmed.ncbi.nlm.nih.gov/37352829/)): one Chinese man with homozygous nonsense c.2962C>T, p.R988X.
- **Mechanism class.** Loss of function. This is supported by the nonsense and splice variants and by the knockout mice.
- **Gene–disease validity.** I did not check ClinGen or GenCC. Check `cache/clingen` and `just check-gene-validity` before recording a tier. Do not assign one yourself.
- **Not found.** Allele frequencies, epigenetic data, chromosomal abnormalities and modifier genes.

## 5. Environmental Information

None identified. There are no infectious agents. No lifestyle or toxicant data were retrieved. Do not add `environmental:` entries from this report.

## 6. Mechanism / Pathophysiology

**Causal chain** (steps 1 to 3 are demonstrated in humans; steps 4 to 6 rest mainly on the mouse and *Chlamydomonas* work; the last step is inferred):

1. Biallelic loss-of-function variants (splice, nonsense, missense) in *CFAP70* reduce or abolish CFAP70 protein. Demonstrated by immunofluorescence in the splice-variant patient, where CFAP70 was absent from the flagellum.
2. CFAP70 is lost from the sperm axoneme. In the 2019 report, outer-dynein-arm and central-pair markers were also absent from the same patient's sperm, so loss of CFAP70 co-occurs with loss of those structures. Whether this is cause or consequence is not settled.
3. CFAP70 normally sits at the base of the outer dynein arm and binds the axoneme ([PMID:30158508](https://pubmed.ncbi.nlm.nih.gov/30158508/); in *Chlamydomonas* it is placed at the C2a central-apparatus projection, [PMID:33988244](https://pubmed.ncbi.nlm.nih.gov/33988244/)). It interacts with the outer-dynein-arm components DNAI1 and DNAI2 ([PMID:37458246](https://pubmed.ncbi.nlm.nih.gov/37458246/)).
4. Without it, flagellum biogenesis and assembly fail during spermiogenesis, with reduced AKAP3 in the flagella (mouse, PMID:37458246). This leads to MMAF and loss of motility.
5. Spermiogenesis is also disturbed upstream of the flagellum. Cfap70-null mouse late spermatids have club-shaped heads and abnormal manchette disassembly (PMID:37458246), and sperm counts fall, which fits the oligozoospermia (PMID:37352829).
6. Result: severe asthenozoospermia, teratozoospermia and oligozoospermia, and male infertility. The branch between flagellar and head or manchette defects is shown in mice, and it is inferred that humans share it.

- **Suggested GO / CL / UBERON** (verify each by lookup): GO sperm flagellum assembly / axonemal dynein complex assembly / cilium movement; CL spermatid (CL:0000018); UBERON testis (UBERON:0000473), epididymis semen/sperm flagellum as relevant. Do not write these IDs without a lookup.
- **Omics, immune, metabolic.** None reported.

## 7. Anatomical Structures Affected

- Testis, specifically the post-meiotic germ cells (spermatids and spermatozoa).
- Subcellular: the sperm flagellar axoneme, the outer dynein arm and central apparatus, and the manchette.
- No other organs reported. Bilateral, as expected for a systemic germline genotype.

## 8. Temporal Development

Onset is lifelong, from puberty, and is detected in adulthood on infertility work-up. The course is non-progressive from the information available. No remission patterns are known.

## 9. Inheritance and Population

- **Inheritance.** Autosomal recessive (HP:0000007). Reported cases are homozygous, and OMIM also describes compound heterozygotes.
- **Consanguinity.** Homozygosity in unrelated patients suggests it may matter, but I did not retrieve the parental data.
- **Epidemiology.** Not available. There is no prevalence figure. Cases are described as rare, and the 2019 yield was 2 of 167 MMAF men (about 1%).
- **Population.** Cases came from a mainly North African/European MMAF cohort (2019) and a Chinese man (2023). Founder effects are not established.
- **Sex.** Male only in terms of phenotype, since the phenotype is infertility of spermatogenic origin.

## 10. Diagnostics

- **Semen analysis.** Oligo-astheno-teratozoospermia with MMAF morphology, scored on sperm morphology.
- **Genetic testing.** Exome sequencing (it identified both 2019 cases), or a male infertility or MMAF gene panel that includes *CFAP70*. Biallelic variants confirm the diagnosis.
- **Supportive.** Immunofluorescence for CFAP70 and outer dynein arm markers on sperm. Electron microscopy of the axoneme was not confirmed in what I retrieved.
- **Differential.** Other MMAF genes (*DNAH1*, *CFAP43*, *CFAP44*, *WDR66*, *ARMC2*, *FSIP2*), which are other SPGF entries, and primary ciliary dyskinesia. Note that in the 2019 report, WDR66-mutated patients' sperm also lacked CFAP70 staining, while ARMC2, FSIP2 and CFAP43 mutants retained it.
- **Screening.** None established.

## 11. Outcome / Prognosis

No mortality or morbidity data. Reported patients have no symptoms besides sterility. Prognosis for natural fertility is poor. Prognosis for assisted reproduction is described as better than for natural conception. Per the 2023 report, ICSI may help affected couples, though that is a suggestion and I found no outcome series for CFAP70 specifically.

## 12. Treatment

- **No disease-modifying therapy.** The only measure indicated is assisted reproduction, namely ICSI with the patient's own sperm. Suggested NCIT: `NCIT:C15986` is wrong here, because it is pharmacotherapy. Look up an ICSI or assisted-reproduction term (candidate: intracytoplasmic sperm injection) and bind only if one verifies. Otherwise leave `term:` off and use a free-text `preferred_term`.
- **Genetic counselling.** `NCIT:C15240`, which the repo lists.
- **Trials.** I did not search ClinicalTrials.gov. None known.
- **Pharmacogenomics, gene therapy.** None.

## 13. Prevention

There is no primary prevention. Carrier screening and genetic counselling for relatives are appropriate in principle, since this is autosomal recessive. Preimplantation genetic testing is possible after a diagnosis, though I found no literature specific to *CFAP70*. A transmissible risk is unlikely to apply to the offspring phenotype, so counselling needs a clear statement of carrier status.

## 14. Other Species / Natural Disease

I did not search OMIA. A GWAS in Holstein cattle listed *CFAP70* as a candidate for sire fertility traits ([PMID:35484513](https://pubmed.ncbi.nlm.nih.gov/35484513/)). That is association only, and it is not a naturally occurring Mendelian disease. A hybrid yellow catfish study reported lower *CFAP70* expression in sterile hybrids ([PMID:38891632](https://pubmed.ncbi.nlm.nih.gov/38891632/)); that is a correlation in a different context.

## 15. Model Organisms

- **Mouse knockout (Cfap70-/-).** Two independent reports.
  - Jin et al. 2023 ([PMID:37352829](https://pubmed.ncbi.nlm.nih.gov/37352829/)): sterile, mainly from oligo-astheno-teratozoospermia. A truncating mouse allele modelled the patient's R988X change and reproduced his features, which is the strongest model-to-human link in the set.
  - Biol Reprod 2023 ([PMID:37458246](https://pubmed.ncbi.nlm.nih.gov/37458246/)): MMAF, club-shaped heads, abnormal manchette disassembly, and reduced AKAP3.
- **Fidelity.** Good for the reproductive phenotype. A limitation is that mice show head and manchette defects, which are less prominent in the human reports I retrieved.
- **Other systems.** *Chlamydomonas* FAP70 mutants show impaired outer dynein arm activity and flagellar motility ([PMID:30158508](https://pubmed.ncbi.nlm.nih.gov/30158508/)), and the central-apparatus placement is in PMID:33988244. Mouse cell knockdown reduced ciliary beating (PMID:30158508). Evidence source for the mouse and *Chlamydomonas* items is `MODEL_ORGANISM`; the cell data are `IN_VITRO`.
- **Resources not checked.** MGI, IMPC and ZFIN allele pages, beyond the MGI disease-association page above.

## Curation Notes for the KB Entry

1. **Decision.** Record `entry_type: DISEASE`. Delete the stub in the curation PR, add a `history/disorders/Spermatogenic_Failure_41/` record, and put the claim on a `claim`-labelled issue titled `Curate spermatogenic failure 41 (MONDO:0032863)`.
2. **Evidence work still needed.** Run `just fetch-reference` for PMIDs 31621862, 37352829, 37458246, 30158508 and 33988244. Re-read each abstract and copy exact snippets. Quote the OMIM text from a cached source if one exists, since I could not access OMIM.
3. **Terms to look up, not trust.** Every HPO, GO, CL, UBERON and NCIT ID above is a suggestion that I did not verify. The HGNC ID for *CFAP70* was not looked up.
4. **Loose ends.** Resolve the OMIM:618670 versus 619515 ambiguity. Check ClinGen for a CFAP70 gene-disease validity assertion. Search for a GeneReviews chapter with `just check-genereviews`. Search for additional CFAP70 case reports after 2023. The latest PubMed hits listed in my search (PMIDs 38891632 through 42417609) were not individually screened.
5. **Lump/split.** One gene, one phenotype, so keep it as a single entry. Compare it against the existing MMAF-gene SPGF entries for possible grouping membership.

## Sources

- [MGI disease page for OMIM:618670](https://informatics.jax.org/disease/OMIM:618670)
- [Disease Ontology DOID:0111912](https://disease-ontology.org/term/DOID:0111912)
- [MalaCards: Spermatogenic Failure 41](https://malacards.org/card/spermatogenic_failure_41)
- [eBioMedicine 2023, CFAP70 diagnostic target (PMID:37352829)](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(23)00240-2/fulltext)
- [PubMed: Beurois et al., Hum Reprod 2019 (PMID:31621862)](https://pubmed.ncbi.nlm.nih.gov/31621862/)
- [PubMed: Biol Reprod 2023, Cfap70 mouse (PMID:37458246)](https://pubmed.ncbi.nlm.nih.gov/37458246/)
- [PubMed: Cells 2018, CFAP70 axoneme-binding (PMID:30158508)](https://pubmed.ncbi.nlm.nih.gov/30158508/)
- [PubMed: J Cell Sci 2021, FAP70 C2a (PMID:33988244)](https://pubmed.ncbi.nlm.nih.gov/33988244/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 13 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012206` (1 mention) - the report calls it "Asthenozoospermia"; HP calls it **Abnormal sperm motility**
- `HP:0012864` (1 mention) - the report calls it "multiple flagellar abnormalities"; HP calls it **Abnormal sperm morphology**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.