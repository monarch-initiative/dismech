---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T11:12:00.841845'
end_time: '2026-10-15T11:14:53.158854'
duration_seconds: 172.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Vertebral Anomalies And Variable Endocrine And T-cell Dysfunction
  mondo_id: MONDO:0032607
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
  - claude-opus-5-5
  web_search_requests: 4
  num_turns: 18
  total_cost_usd: 2.0999938000000005
  session_id: 4569ee1c-4db3-4019-b491-3fcdde4ef9a7
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 9
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 17
  on_topic: 11
  validator_version: 0.3.0
term_validation:
  total_terms: 3
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0032607
    reported_labels:
    - MONDO
    ontology_label: vertebral anomalies and variable endocrine and T-cell dysfunction
  - term_id: DOID:0070345
    reported_labels:
    - Disease Ontology
    ontology_label: vertebral anomalies and variable endocrine and T-cell dysfunction
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vertebral Anomalies And Variable Endocrine And T-cell Dysfunction
- **MONDO ID:** MONDO:0032607 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Vertebral Anomalies And Variable Endocrine And T-cell Dysfunction** covering all of the
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

Let me read the full Liu 2018 abstract and the Mäkitie/Rafeeq/Hua details, plus check the draft entry.

I've finished collecting sources: the cached abstracts in this worktree, plus MedGen and the Undiagnosed Diseases Network pages. Here is the report.

# Vertebral Anomalies and Variable Endocrine and T-cell Dysfunction (VETD; TBX2-related): Research Report

**Scope and caveats.** VETD is an ultra-rare syndrome. Its definition rests on one 2018 paper describing four people (Liu et al., PMID:29726930). A few later reports describe other conditions caused by changes in the same gene (TBX2), and they widen the picture. Most of the biology behind the mechanism comes from mouse, zebrafish and fly experiments.

Two kinds of identifier in this report need care before use:
- **Ontology IDs (HPO, GO, CL, UBERON, NCIT)** are leads only. The repository rules say every CURIE must be looked up and its label copied in the same step it is written.
- **PMIDs:** those marked ✔ have a file in `references_cache/` in this worktree. Those marked (unverified) were not fetched.

---

## 1. Disease information

**Overview.** VETD is an autosomal dominant malformation syndrome caused by damaging heterozygous variants in **TBX2**, a gene encoding a T-box transcription factor (17q23.2). It resembles DiGeorge syndrome (22q11.2 deletion syndrome). Features vary between patients:
- vertebral segmentation defects, such as Klippel-Feil anomaly, hemivertebrae and fused ribs
- endocrine problems: hypoparathyroidism, growth hormone deficiency, autoimmune thyroiditis
- T-cell deficiency, with an absent or underdeveloped thymus in some patients
- cleft palate and characteristic facial features
- congenital heart defects
- mild developmental or behavioral problems

The original paper frames it this way (PMID:29726930 ✔):
> "We report four individuals with an overlapping spectrum of craniofacial dysmorphisms, cardiac anomalies, skeletal malformations, immune deficiency, endocrine abnormalities and developmental impairments, reminiscent of DiGeorge syndrome, who are heterozygotes for TBX2 variants."

**Identifiers**

| Resource | ID |
|---|---|
| OMIM (phenotype) | 618223 |
| OMIM (gene) | TBX2 \*600747 |
| MONDO | MONDO:0032607 |
| MedGen | C4748741 (UID 1648299) |
| Disease Ontology | DOID:0070345 |
| KEGG Disease | H02753 |
| LOVD | disease #06365 |
| HGNC | TBX2 is `hgnc:11597` (verify with lookup) |
| Orphanet | No ORPHA code found; search ORPHA directly before asserting there is none |
| ICD-10/ICD-11 | No specific code. KEGG files it under ICD-11 "multiple developmental anomalies or syndromes" |

**Synonyms:** VETD; TBX2-related DiGeorge-like syndrome (descriptive only). Some literature uses "TBX2-associated multisystem malformation disorder."

**Source of the data.** Everything comes from individual case reports, one undiagnosed-disease-network family, and one Finnish pedigree. There is no registry or EHR cohort.

---

## 2. Etiology

- **Cause:** a germline heterozygous variant in TBX2 that partially or fully removes its function. The founding variants are p.Arg20Gln (inherited in one family) and p.Arg305His (de novo).
  - Both reduced TBX2's ability to repress its target genes and lowered TBX2 protein levels.
  - In fruit flies, both behaved as partial loss-of-function alleles (PMID:29726930 ✔): "Heterologous over-expression studies in Drosophila demonstrate that both p.R20Q and p.R305H function as partial loss-of-function alleles."
- **Modifier and dosage-partner genes:** mouse genetics shows *Tbx2* and *Tbx3* compensate for each other, and that *Tbx1*, *Tbx2* and *Tbx3* act together in the pharyngeal region.
  - Losing alleles of *Tbx2* and *Tbx3* in combination gives defects that "are not simply additive" (PMID:35506352 ✔, limb).
  - *Tbx1/Tbx2/Tbx3* interactions govern pharyngeal and arterial-pole development (PMID:22116936 ✔).
  - No human modifier has been shown.
- **Environmental, protective and gene-environment factors:** none described. This is a developmental disorder with an entirely genetic cause.
- **Common-variant association:** TBX2 rs882367 reaches genome-wide significance for sitting-height ratio. This comes from Mäkitie et al. citing a GWAS; the primary GWAS was not fetched.

---

## 3. Phenotypes

Frequencies are counts out of the four people in the founding report: three p.R20Q family members and one p.R305H proband (PMID:29726930; summary table reproduced in PMID:35311234 ✔). HPO features come from the OMIM clinical synopsis as listed by MedGen. All features are congenital or appear in childhood unless stated.

| Feature | Detail and frequency | Suggested HPO label (look up the ID) |
|---|---|---|
| Vertebral segmentation anomalies | R20Q: Klippel-Feil anomaly, rib fusions. R305H: fused thoracic vertebrae and hemivertebrae (4/4) | Hemivertebrae; Klippel-Feil anomaly; Vertebral fusion; Rib fusion |
| Scoliosis and kyphosis | Present in several; progressive spinal deformity | Scoliosis; Kyphosis |
| Sprengel deformity | R20Q family | Congenital elevation of scapula (Sprengel) |
| Camptodactyly | PIP contracture of 3rd and 4th fingers | Contracture of the PIP joint of the 3rd finger / 4th finger |
| Short or webbed neck, low hairline | | Short neck; Webbed neck; Low anterior hairline |
| Cleft palate (± cleft lip) | R20Q proband: unilateral cleft lip and palate; R305H: high narrow palate | Cleft palate; Cleft lip; Narrow palate |
| Facial features | Triangular face, hypertelorism, epicanthus, depressed nasal bridge, broad nasal tip, cupped low-set ears, overfolded helix | Triangular face; Hypertelorism; Epicanthus; Depressed nasal bridge; Cupped ear; Low-set ears |
| Thymic aplasia and T-cell deficiency | R20Q proband: "absent thymus with severe T-cell deficiency"; diagnosed with complete DiGeorge and given a thymus transplant at about 6 months (UDN page) | Aplasia of the thymus; Decreased total T cell count; Abnormal B cell morphology |
| Hypoparathyroidism | R20Q family | Hypoparathyroidism |
| Autoimmune thyroiditis | Proband: hypothyroid, later hyperthyroid phase | Hashimoto thyroiditis |
| Growth hormone deficiency | R305H | Decreased response to growth hormone stimulation test |
| Short stature | Height between the 2nd and 36th percentile | Short stature |
| Congenital heart defects | R20Q: ASD and PDA. R305H: double-outlet right ventricle with valvular pulmonary stenosis | Atrial septal defect; Patent ductus arteriosus; Double outlet right ventricle; Pulmonic stenosis |
| Neurodevelopment and behavior | Mild global developmental delay, autistic behaviors, ADHD; neonatal seizures in one; mild cognitive impairment (R305H) | Mild global developmental delay; Autistic behavior; Attention deficit hyperactivity disorder; Seizure |
| Other | Glabellar hemangioma; congenital ectopic pupil; brachycephaly | as named |

**Quality of life.** No formal measures (EQ-5D, SF-36) have been reported. The main burdens are:
- in infancy, risk of life-threatening infection when the thymus is absent
- heart surgery
- progressive spinal deformity
- lifelong hormone replacement

**Phenotypes from related TBX2 variants.** These may belong to the same spectrum or to separate disorders; see the lump/split note in §4.
- **p.Thr300Met, Finnish three-generation family** (PMID:35311234 ✔):
  - codfish-shaped vertebrae with balloon-shaped discs
  - severe early-onset osteoarthritis, with hip replacement in the early 20s to 30s
  - empty sella without hormone deficiency (one member had mild thyrotoxicosis)
  - obesity, headaches, depression, reduced sitting-height ratio
- **p.Lys177\* (de novo nonsense change):** severe osteochondrodysplasia with developmental delay (PMID:36733940 ✔).
- **17q23.2 duplication including TBX2:** complex heart defect (VSD, coarctation, mitral stenosis), short or missing end bones of the fingers, cerebellar hypoplasia, growth restriction starting before birth, mild intellectual disability (PMID:20635360 ✔).

---

## 4. Genetic and molecular information

- **Gene:** TBX2 (OMIM \*600747; 17q23.2; transcript NM_005994.4). It encodes a T-box transcription factor that mainly *represses* its targets. Its DNA-binding T-box domain spans roughly residues 94–280.

**Known variants**

| Variant | Type | Origin | Effect | Phenotype | PMID |
|---|---|---|---|---|---|
| c.59G>A p.Arg20Gln | Missense, N-terminal | Inherited (AD; mother → 2 children) | Partial loss of function; reduced repression and lower protein | VETD (thymic aplasia, hypoparathyroidism, cleft, ASD/PDA) | 29726930 ✔ |
| p.Arg305His | Missense, just after the T-box | De novo | Partial loss of function | VETD (GH deficiency, fused vertebrae, DORV) | 29726930 ✔ |
| c.899C>T p.Thr300Met | Missense | Inherited (AD, 3 generations) | Predicted damaging; not tested in the lab. gnomAD MAF 3.9×10⁻⁵ overall, 3.9×10⁻⁴ in Finns | Osteochondrodysplasia with empty sella | 35311234 ✔ |
| c.529A>T p.Lys177\* | Nonsense, in the T-box | De novo | Predicted loss of function or nonsense-mediated decay; ACMG likely pathogenic | Severe osteochondrodysplasia with developmental delay | 36733940 ✔ |
| c.977delA p.Asp326Alafs\*42; c.987delC p.Ala330Argfs\*38 | Frameshift | Inherited (AD, 2 Chinese families) | Stable nuclear protein with about 80% less transcriptional activity; haploinsufficiency | Progressive sensorineural hearing loss ± nystagmus, **without** other syndromic features | 40962492 ✔ |
| p.R608W, p.T249I, p.R616Q | Missense | Found only in cases (588 conotruncal heart defect cases vs 300 controls) | Changed mRNA and protein levels | Conotruncal heart defects | Xie et al. 2018, Hum Genomics, PMID:30223900 (unverified) |
| 17q23.2 duplication | Copy-number gain | De novo | Proposed overexpression | Heart and finger anomalies | 20635360 ✔ |
| 17q23 deletion including TBX2 and TBX4 | Copy-number loss | — | Haploinsufficiency of two genes | Limb and musculoskeletal anomalies, microcephaly | Nimmakayalu et al. 2011 (PMID not fetched) |

- **ClinVar and ClinGen:** no ClinGen gene-disease validity curation was found for TBX2–VETD. Do not record a validity tier; it would have to be copied from a source.
- **Lump/split note for curation.**
  - The hearing-loss families are explicitly described as having "isolated auditory and oculomotor phenotypes, without additional syndromic features seen in previously described TBX2-associated disorders" (PMID:40962492 ✔). They look like a separate allelic disorder.
  - The p.Thr300Met and p.Lys177\* skeletal dysplasias share vertebral and facial features with VETD. Mäkitie et al. treat theirs as a TBX2 skeletal dysplasia that overlaps VETD. Treat them as part of the spectrum or as subtypes, and record the uncertainty.
- **Epigenetics:** nothing disease-specific. Disrupting the antisense long non-coding RNA *TBX2-AS1* has been linked to hearing impairment (cited in PMID:40962492).
- **Somatic origin:** not applicable.

---

## 5. Environmental information

None known. There are no environmental, lifestyle or infectious causes. Infections are a *complication* of T-cell deficiency, not a cause.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. A heterozygous damaging TBX2 variant (missense, nonsense or frameshift) **leads to** less functional TBX2 protein. Missense variants reduce protein amount and repressor activity; truncating variants are predicted to cause haploinsufficiency. *(Shown in cell lines and flies for R20Q and R305H, PMID:29726930; shown for the frameshifts, PMID:40962492.)*
2. Less TBX2 **results in** weaker repression of target genes in tissues of the developing embryo where TBX2 acts. The pathway branches here:
   - **2a. Pharyngeal and second-heart-field mesoderm.** In mice, Tbx2/Tbx3 act with Tbx1 in the caudal pharyngeal region (PMID:22116936 ✔). Reduced dosage **is inferred to** disturb development of the third and fourth pharyngeal pouches and arches, which **leads to** thymic aplasia or hypoplasia (→ T-cell deficiency → infections) and parathyroid hypoplasia (→ hypoparathyroidism). *(Inferred from the mouse pathway and the clinical resemblance to 22q11.2 deletion; no TBX2-specific thymus experiment has been done.)*
   - **2b. Heart.** Tbx2 holds back chamber differentiation in the atrioventricular canal and is needed to septate the outflow tract (PMID:15459098 ✔). Tbx2/Tbx3 also drive AV-canal myocardium and endocardial cushion formation (PMID:22130515 ✔). Disruption **results in** septal defects (ASD) and outflow-tract defects (DORV, pulmonary stenosis). *(Shown in mice; inferred in humans.)*
   - **2c. Palate.** *Tbx2* null mice and mice heterozygous for both *Tbx2* and *Tbx3* have cleft palate. In these mice the palatal shelves are smaller, with more proliferation and cell death and raised *Bmp4* and *Cyclin D1* (PMID:19769959 ✔). This **leads to** cleft palate.
   - **2d. Axial skeleton and limb.** TBX2 is expressed in hypertrophic chondrocytes and osteoblast lineages (reviewed in PMID:35311234). In the limb bud it ends the Shh/Fgf feedback loop by directly repressing *Grem1* (PMID:23633963 ✔). Reduced dosage **is inferred to** cause errors in vertebral segmentation and endochondral ossification, giving hemivertebrae, fused vertebrae and ribs, codfish vertebrae, and early-onset osteoarthritis. *(The vertebral mechanism is inferred; mouse limb findings show the role in digits.)*
   - **2e. Hypothalamic-pituitary axis.** *Tbx2* is expressed in the infundibulum of the ventral diencephalon (PMID:18534921 ✔). This **may lead to** growth hormone deficiency (R305H) and empty sella (T300M). *(Inferred; no functional study.)*
   - **2f. Inner ear (allelic hearing-loss disorder).** Tbx2 is a master regulator that makes inner hair cells distinct from outer hair cells (García-Añoveros et al., Nature 2022, PMID:35508658, unverified). *Tbx2*+/− mice develop progressive hearing loss, and their inner hair cells briefly misexpress an outer-hair-cell marker (PMID:40962492 ✔). This **leads to** progressive sensorineural hearing loss.
3. Thyroid autoimmunity, such as Hashimoto thyroiditis, **is plausibly downstream of** thymic hypoplasia and poor central tolerance, as in partial DiGeorge syndrome. *(Inferred.)*

### Details for curation

- **Molecular function:** sequence-specific DNA-binding transcription repressor activity (GO "DNA-binding transcription repressor activity, RNA polymerase II-specific"). Biological processes to consider: outflow tract septum morphogenesis, atrioventricular canal development, palate development, thymus development, parathyroid gland development, regulation of chondrocyte differentiation, negative regulation of cell cycle. *Tbx2* represses *Cdkn2a/b* and *Cdkn1a*, though Harrelson et al. found this was not required in the heart (PMID:15459098).
- **Cell types (CL leads):** second heart field progenitor (Tbx2 misexpression impairs their deployment, PMID:19563797 ✔), cardiac muscle cell of the atrioventricular canal, pharyngeal endoderm and mesenchyme, palatal mesenchyme, chondrocyte or hypertrophic chondrocyte, osteoblast, thymic epithelial cell, parathyroid chief cell, T cell, cochlear inner hair cell.
- **Not yet studied:** single-cell, multi-omic and CRISPR-screen data specific to this disease.
- **GEO datasets:** none specific to VETD. Mouse Tbx2/Tbx3 ChIP-seq and expression profiles exist in PMID:22130515.

---

## 7. Anatomical structures affected

- **Primary:** vertebral column and ribs; thymus; parathyroid glands; heart (interatrial septum, outflow tract, pulmonary valve, ductus arteriosus); secondary palate; face and ears.
- **Secondary:** thyroid (autoimmunity); pituitary and sella turcica; joints (hip, knee) in the T300M family; brain (cerebellar hypoplasia in the duplication case).
- **Embryonic origins:** pharyngeal arches and pouches 3 and 4, second heart field, somites and sclerotome.
- **Subcellular:** nucleus. TBX2 is a nuclear transcription factor, and the frameshift proteins still localize to the nucleus.
- **Lateralization:** cleft lip was unilateral in the proband. Other anomalies are midline or bilateral.

---

## 8. Temporal development

- **Onset:** congenital (malformations, thymic aplasia). Endocrine features can appear in childhood: thyroiditis in childhood, and GH deficiency shown by slowing growth.
- **Course:** a static malformation syndrome. Scoliosis or kyphosis and osteoarthritis (T300M) progress. The hearing loss in the allelic disorder is progressive.
- **Critical windows:** early infancy for diagnosing T-cell deficiency and doing a thymus transplant; childhood for monitoring spinal deformity.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant. There is both inherited transmission (R20Q, mother to two children) and de novo occurrence (R305H, K177\*).
- **Expressivity:** variable. The mother and sister of the R20Q proband had milder versions of his features (UDN page).
- **Penetrance:** incomplete penetrance has not been established for VETD. Nystagmus was incompletely penetrant in the hearing-loss families.
- **Founder effect:** p.Thr300Met is about 10 times more frequent in Finns (gnomAD), which suggests a Finnish founder allele (PMID:35311234).
- **Prevalence:** unknown, ultra-rare. Fewer than 10 individuals have published VETD-type syndromic features. Suggested record: `prevalence_class` ULTRA_RARE or NOT_YET_DOCUMENTED with `measure_type: CASES_IN_LITERATURE`.
- **Sex ratio:** not determinable. Both sexes are affected.
- **Anticipation and consanguinity:** not relevant.

---

## 10. Diagnostics

- **Clinical suspicion:** a DiGeorge-like picture (conotruncal or septal heart defect, cleft palate, hypocalcemia or hypoparathyroidism, T-cell lymphopenia) in someone **without** a 22q11.2 deletion, especially when vertebral segmentation defects are also present.
- **Laboratory and immunology:**
  - T-cell subsets (CD3/CD4/CD8), naive T cells (CD45RA), TRECs
  - immunoglobulins
  - calcium, phosphate, PTH
  - TSH, free T4, thyroid antibodies
  - IGF-1 and GH stimulation testing
- **Newborn screening:** TREC-based SCID screening can detect the athymic form.
- **Imaging:** spine X-ray, MRI or CT for hemivertebrae, fusions and codfish vertebrae; echocardiography; chest imaging for thymus; brain or pituitary MRI for empty sella.
- **Genetic testing:**
  - First rule out 22q11.2 deletion with chromosomal microarray or MLPA. CMA also detects 17q23.2 copy-number changes.
  - Then exome or genome sequencing. Every published diagnosis came from exome or genome sequencing, through the UDN and research programs.
  - TBX2 is rarely on commercial DiGeorge-like or skeletal dysplasia panels. Hua et al. recommend adding it to hearing-loss panels.
- **Differential diagnosis:** 22q11.2 deletion syndrome (TBX1); CHARGE syndrome (CHD7); 10p13–p14 deletion (HDR/DiGeorge-2); FOXN1 deficiency; Klippel-Feil syndromes (GDF6, MEOX1); spondylocostal dysostoses; TBX1 point-variant disease; ulnar-mammary syndrome (TBX3); other osteochondrodysplasias for the T300M phenotype.
- **No formal diagnostic criteria exist.**

---

## 11. Outcome and prognosis

- **Survival data:** none. In the founding family the proband survived after a thymus transplant and was 10 years old on the UDN page.
- **Main risks:**
  - infection in complete thymic aplasia, which is fatal in infancy without transplant (general knowledge for complete DiGeorge, not TBX2-specific evidence)
  - complications of heart lesions
  - hypocalcemic seizures
  - progressive spinal deformity
  - early disabling osteoarthritis (T300M family, with joint replacement in the 20s and 30s)
- **Prognostic factors:** severity of thymic and T-cell involvement and complexity of the heart lesion (inferred).

---

## 12. Treatment

There are no trials and no disease-specific therapy. Care is supportive and depends on which organs are involved. NCIT terms below are leads; confirm each one falls under `NCIT:C25218`.

| Problem | Intervention | Suggested NCIT lead |
|---|---|---|
| Complete thymic aplasia | Allogeneic cultured thymus tissue implantation; the R20Q proband received a thymus transplant. Rethymic® is FDA-approved (2021) for congenital athymia | Organ Transplantation (C15289) or a more specific term; modality CELL_THERAPY |
| Partial T-cell deficiency | Infection prophylaxis, IVIG if needed, avoid live vaccines, irradiated blood products | Supportive Care (C15747); Pharmacotherapy with immunoglobulin agent |
| Hypoparathyroidism | Calcium plus calcitriol; recombinant PTH where indicated | Pharmacotherapy (C15986) + `therapeutic_agent` calcitriol (CHEBI) |
| GH deficiency | Recombinant growth hormone | Pharmacotherapy + somatropin |
| Hypothyroidism / thyroiditis | Levothyroxine; antithyroid drugs in a hyperthyroid phase | Pharmacotherapy + levothyroxine |
| Heart defects | Surgical or catheter repair | Surgical Procedure (C15329) |
| Cleft palate | Palatoplasty and speech therapy | Surgical Procedure; Speech language therapy |
| Scoliosis/kyphosis; osteoarthritis | Bracing, spinal fusion; hip arthroplasty (T300M) | Orthopedic Surgical Procedure (C16186) |
| Development and behavior | Early intervention, ADHD management | Behavioral / rehabilitation terms |
| Hearing loss (allelic disorder) | Hearing aids or cochlear implant | Surgical Procedure + device qualifier |

- **Pharmacogenomics, gene therapy, RNA therapy:** none.
- **Research model:** an iPSC line (IRDWCHi001-A) from a p.Asp326Alafs\*42 carrier is available for disease modeling (PMID:41512733 ✔).

---

## 13. Prevention

- **Primary prevention:** not applicable.
- **Secondary prevention:** TREC newborn screening catches the T-cell deficiency early. Consider cascade testing of relatives once a familial variant is known, because expressivity varies and mildly affected parents are easy to miss.
- **Tertiary prevention:** regular monitoring of calcium, PTH, thyroid function, growth and the spine; infection prophylaxis.
- **Genetic counseling:** affected individuals have a 50% chance of passing the variant to each child. Prenatal or preimplantation testing is possible once the variant is known. For apparently de novo cases, mention the possibility of parental germline mosaicism.

---

## 14. Other species and natural disease

- No naturally occurring TBX2 disease has been reported in animals (OMIA not searched in detail).
- **Orthologs:** mouse *Tbx2* (chromosome 11); zebrafish *tbx2a* and *tbx2b* (ZFIN ZDB-GENE-990917-4 is one of these); *Drosophila bifid/omb* (the fly T-box gene used in PMID:29726930).
- The T-box domain is highly conserved: about 96% of human and mouse T-box residues are identical (PMID:36733940).
- Not zoonotic.

---

## 15. Model organisms

| Model | Phenotype and relevance | PMID |
|---|---|---|
| *Tbx2*−/− mouse | Embryonic lethal; AV canal and outflow tract septation defects; extra digit 4 on the hindlimb. **Heterozygous mice appear normal**, a mismatch with the human dominant disease | 15459098 ✔ |
| *Tbx2*−/− and *Tbx2*+/−;*Tbx3*+/− mouse | Cleft palate | 19769959 ✔ |
| *Tbx2/Tbx3* compound mutants | AV canal myocardium and endocardial cushion failure; limb defects that depend on dosage | 22130515 ✔, 35506352 ✔ |
| *Tbx1/Tbx2/Tbx3* genetic interaction | Pharyngeal and arterial-pole morphogenesis; the pathway behind DiGeorge-like features | 22116936 ✔ |
| Conditional Tbx2 overexpression in the myocardium | Less proliferation; impaired deployment of second-heart-field cells into the outflow tract | 19563797 ✔ |
| Limb-specific Tbx2 gain or loss | Grem1 repression ends Shh/Fgf signaling; abnormal digit number | 23633963 ✔ |
| *Tbx2*+/− and knock-in mice (hearing) | Progressive hearing loss; inner hair cells misexpress an outer-hair-cell marker. Supports haploinsufficiency | 40962492 ✔ |
| Cochlear conditional *Tbx2* KO | Inner hair cells convert to outer hair cells | 35508658 (unverified) |
| *Drosophila* heterologous overexpression | R20Q and R305H are partial loss of function | 29726930 ✔ |
| Human iPSC line IRDWCHi001-A | Hearing-loss disease modeling | 41512733 ✔ |

**Model limitations to record**

- *Tbx2* heterozygous mice do not reproduce the human dominant malformation syndrome, as far as the published reports show (PMID:15459098). This fits a `HUMAN_MODEL_MISMATCH` discussion. It also suggests human missense alleles may act through more than simple haploinsufficiency, or that humans are more sensitive to TBX2 dosage. Both remain hypotheses.
- No model has directly tested thymus or parathyroid development with Tbx2 alone.

---

## Key evidence quotes from cached abstracts

- **PMID:29726930:** "In vitro transcriptional assays in cultured cells show that both variants result in reduced transcriptional repressor activity of TBX2. We also show that the variants result in reduced protein levels of TBX2."
- **PMID:15459098:** "Mice heterozygous for a Tbx2 null mutation appear normal but homozygous embryos reveal a crucial role for Tbx2 during cardiac development."
- **PMID:19769959:** "Mice homozygous mutant for Tbx2 and mice double heterozygous for Tbx2 and Tbx3 exhibit a cleft palate phenotype"
- **PMID:35311234:** "Affected individuals (age range 24-44 years) exhibit unusual codfish-shaped vertebrae, severe early-onset and debilitating osteoarthritis and an empty sella without endocrine abnormalities."
- **PMID:36733940:** "Whole-exome sequencing revealed a novel nonsense variant (c.529A>T; p.Lys177*; NM_005994.4) in TBX2."
- **PMID:40962492:** "In vivo, heterozygous Tbx2 knockout mice (Tbx2+/- ) developed progressive HL and transient postnatal misexpression of outer hair cell marker in inner hair cells, supporting haploinsufficiency as the pathogenic mechanism."
- **PMID:20635360:** "A SNP-array analysis detected a de novo duplication of 17q23.2, encompassing the TBX2 gene."

## Sources
- Liu et al. 2018, Hum Mol Genet, PMID:29726930; Mäkitie et al. 2022, PMID:35311234; Rafeeq et al. 2022, PMID:36733940; Hua et al. 2025, PMID:40962492; Hua et al. 2026, PMID:41512733; Radio et al. 2010, PMID:20635360; Harrelson et al. 2004, PMID:15459098; Zirzow et al. 2009, PMID:19769959; Singh et al. 2012, PMID:22130515; Mesbah et al. 2012, PMID:22116936; Dupays et al. 2009, PMID:19563797; Farin et al. 2013, PMID:23633963; Pontecorvi et al. 2008, PMID:18534921; Lopatka & Moon 2022, PMID:35506352 (all in `references_cache/`)
- [NCBI MedGen 1648299 (OMIM 618223 synopsis)](https://www.ncbi.nlm.nih.gov/medgen/1648299)
- [Undiagnosed Diseases Network participant page (TBX2 p.Arg20Gln)](https://undiagnosed.hms.harvard.edu/?p=35)
- [KEGG Disease H02753](https://www.kegg.jp/entry/H02753)
- [LOVD disease #06365](https://databases.lovd.nl/shared/diseases/06365)
- [Disease Ontology DOID:0070345](https://disease-ontology.org/term/DOID:0070345)
- [Xie et al. 2018, Identification of TBX2 and TBX3 variants in conotruncal heart defects (PMC6142335)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6142335/)
- [García-Añoveros et al. 2022, Tbx2 is a master regulator of inner versus outer hair cell differentiation (PMID:35508658)](https://pubmed.ncbi.nlm.nih.gov/35508658/)
- [GeneCards TBX2](https://www.genecards.org/card/TBX2); [NCBI Gene 6909](https://www.ncbi.nlm.nih.gov/gene/6909)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 17 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032607` (1 mention) - the report calls it "MONDO"; MONDO calls it **vertebral anomalies and variable endocrine and T-cell dysfunction**
- `DOID:0070345` (4 mentions) - the report calls it "Disease Ontology"; DOID calls it **vertebral anomalies and variable endocrine and T-cell dysfunction**