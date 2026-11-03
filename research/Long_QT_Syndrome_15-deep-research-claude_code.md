---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T20:02:11.196263'
end_time: '2026-10-15T20:03:19.439158'
duration_seconds: 68.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Long QT Syndrome 15
  mondo_id: MONDO:0014550
  category: Genetic
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
  web_search_requests: 2
  num_turns: 4
  total_cost_usd: 0.7761712
  session_id: 1411d6e0-a3a9-57ef-a642-a756ff0785bd
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 5
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 1
  validator_version: 0.3.0
term_validation:
  total_terms: 24
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 1
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0031546
    reported_labels:
    - verify
    ontology_label: Cardiac conduction abnormality
  - term_id: HP:0010646
    reported_labels:
    - verify
    ontology_label: Cervical spine instability
  - term_id: CL:0002494
    reported_labels:
    - verify
    ontology_label: cardiocyte
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Long QT Syndrome 15
- **MONDO ID:** MONDO:0014550 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Long QT Syndrome 15** covering all of the
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

I'll verify the gene and identifier assignments first, since LQT14, LQT15 and LQT16 are easy to mix up.

# Long QT Syndrome 15 (LQT15, CALM2-related calmodulinopathy): research report

**Verification status.** Two web searches checked the gene and OMIM assignment and the overall clinical picture. The rest comes from background knowledge and was not re-fetched. Items marked **[verify]** (most PMIDs, frequencies, therapy specifics) need `just fetch-reference` and a snippet check before they go into the KB. I wrote no quotes from memory, so the report contains no abstract snippets. The MONDO ID in the template (MONDO:0014550) was **not** confirmed and needs an OAK lookup.

## 1. Disease information

LQT15 is a very early-onset, severe, autosomal dominant long-QT arrhythmia syndrome. Heterozygous variants in **CALM2** (calmodulin 2, 2p21) cause it. It is one of three "calmodulinopathy" LQTS subtypes:

| Subtype | Gene | OMIM |
|---|---|---|
| LQT14 | CALM1 | #616247 |
| **LQT15** | **CALM2** | **#616249** |
| LQT16 | CALM3 | #618782 [verify] |

- The 616249 and 616247 assignments are confirmed by the OMIM mirror and search results ([OMIM #616249](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/616249), [OMIM #616247](https://https.ncbi.nlm.nih.gov/omim/616247)). The LQT16/CALM3 number comes from memory.
- OMIM describes LQT15 as an arrhythmia disorder beginning very early in life. Features are ventricular arrhythmias, often life-threatening, T-wave alternans, markedly prolonged QTc, and intermittent 2:1 AV block.
- **Synonyms:** LQT15; calmodulinopathy (CALM2); CALM2-related LQTS. The same gene can also cause CPVT-like, idiopathic VF and overlap phenotypes.
- **Data source:** the data are aggregated from case reports and registries, not from EHR cohorts.

## 2. Etiology

- **Cause:** a germline missense variant in CALM2. Most are de novo and are often detected in infancy or childhood. Several families show recurrence consistent with germline mosaicism or inherited variants [verify].
- **Risk factors:** the causal variant is the determinant. Adrenergic triggers (exertion, emotion, fever) are plausible modifiers; sources are not verified here.
- **Protective factors and gene-environment interactions:** none established. There are no confirmed modifier genes.

## 3. Phenotypes

| Phenotype | HPO (verify via OAK) | Notes |
|---|---|---|
| Long QT interval / prolonged QTc | HP:0001657 | Often profound, with QTc commonly above 500 ms [verify] |
| T-wave alternans | HP:0031546 [verify] | Frequent |
| 2:1 atrioventricular block | HP:0010646 [verify] | Intermittent; related fetal/neonatal bradycardia |
| Ventricular tachycardia / torsades de pointes | HP:0004756 / HP:0001663 [verify] | Often life-threatening |
| Cardiac arrest, sudden cardiac death | HP:0001695 / HP:0001645 [verify] | Often in infancy or early childhood |
| Syncope, seizures | HP:0001279 / HP:0001250 | Arrhythmic, not primary neurological |
| Neurodevelopmental delay | HP:0001263 | Described in some patients, partly from hypoxic injury [verify] |

- **Onset:** neonatal to early childhood. A 16-year-old with a de novo D134H variant has also been reported.
- **Severity:** more severe than most other LQTS subtypes. Reviews say LQT14, 15 and 16 typically have earlier onset, profound QT prolongation, and a high predilection for cardiac arrest and sudden death (see the [2018 Frontiers review](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2018.00175/full)).
- **Frequencies and quality-of-life data:** I have no verified per-phenotype frequencies or quality-of-life data. Take them from the Crotti et al. 2019 registry (74 patients) after fetching it.

## 4. Genetic and molecular information

- **Gene:** CALM2, HGNC id likely hgnc:1443 [verify with lookup]. CALM1, CALM2 and CALM3 are on different chromosomes but encode an **identical** 149-aa protein.
- **Variants reported in CALM2:** N98S, D96V, D130G, F142L and D134H [verify]. Clusters are in the EF-hand calcium-binding loops and the C-lobe. Crotti et al. 2013 (PMID:23388215, Circulation) first described CALM1 and CALM2 variants in infants with recurrent cardiac arrest [verify].
- **Function:** a reduced Ca²⁺ affinity of the C-domain is typical. One D134H study found a 13-fold reduction in Ca²⁺ binding. The effect is dominant-negative or a gain-of-toxic-function on target channels, not haploinsufficiency (de novo missense, with a single mutant allele among six CALM alleles).
- **Epigenetic and chromosomal abnormalities:** none known.
- **Gene-disease validity:** ClinGen/PanelApp-type listings rate CALM2 as high-evidence for LQTS ([PanelApp](https://panelapp-aus.org/panels/131/gene/CALM2/)). If copying a ClinGen tier into the KB, quote the `CGGV:` record and do not assign one yourself.

## 5. Environmental information

There are no known causative environmental or infectious factors. QT-prolonging drugs and electrolyte disturbances should be avoided, as in all LQTS (general knowledge, [verify] CredibleMeds-type list).

## 6. Mechanism and pathophysiology

**Causal chain**

1. A heterozygous CALM2 missense variant, mostly de novo, causes an amino-acid substitution in a Ca²⁺-binding EF-hand loop of calmodulin.
2. This reduces the Ca²⁺ affinity of the mutant calmodulin (demonstrated in vitro; the D134H study showed a 13-fold reduction).
3. The mutant calmodulin remains bound to its target channels (CaV1.2 and others) and handles Ca²⁺ abnormally, so Ca²⁺-dependent regulation of those channels is impaired. This is demonstrated for several variants.
4. Impaired Ca²⁺-dependent inactivation of the L-type Ca²⁺ current (CaV1.2) prolongs the Ca²⁺ current during the action potential. This is the best-supported mechanism for LQTS. Effects on NaV1.5 (late Na⁺ current) and RyR2 are variant-dependent and partly inferred [verify].
5. Ventricular action-potential duration prolongs, producing QTc prolongation. Early afterdepolarizations and repolarization alternans follow, which explains T-wave alternans.
6. In some patients, prolonged ventricular refractoriness causes functional 2:1 AV block. This is inferred, not demonstrated.
7. EAD-triggered torsades de pointes and ventricular fibrillation lead to syncope, cardiac arrest or sudden death. Adrenergic stress aggravates this.

**Branch:** some variants (e.g. N98S, D130G and others [verify]) instead give CPVT-like phenotypes through RyR2 dysregulation. This explains the overlap seen in registries.

- **Proposed GO terms** (verify): regulation of cardiac muscle contraction by calcium ion signaling (GO:0010882), calcium-mediated signaling (GO:0019722), regulation of ventricular cardiac muscle cell membrane repolarization (GO:0060307), and regulation of high voltage-gated calcium channel activity (GO:1901385). The matching molecular function is calcium ion binding (GO:0005509).
- **Cell type:** cardiac muscle cell, ventricular (CL:0002494 [verify]). Purkinje myocyte (CL:0002068) and atrioventricular node cells are other candidates.
- **Omics, single-cell and functional-genomics data:** not reviewed.

## 7. Anatomical structures affected

- **Organ:** heart (UBERON:0000948), specifically the ventricular myocardium and the conduction system (AV node/His-Purkinje). The CNS is affected only secondarily, through hypoxic injury.
- **Subcellular:** the sarcolemma (L-type Ca²⁺ channel), the sarcoplasmic reticulum (RyR2) and the cytosol. The suggested GO cellular component is sarcolemma (GO:0042383) [verify].
- **Lateralization:** not applicable.

## 8. Temporal development

- **Onset:** fetal to infantile. Fetal bradycardia or AV block can occur. Some milder cases present later.
- **Course:** episodic arrhythmic events on a persistently abnormal substrate. Early cardiac arrest is frequent, and the registry reports earlier arrhythmic events than in other LQTS (see the [2023 Circ J study](https://shiga-med.repo.nii.ac.jp/record/2000230/files/circj.CJ-23-0195.pdf)).
- **Remission and critical periods:** none documented. The first years of life appear to be the highest-risk window.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006). Most cases are de novo. Parental germline mosaicism has been suggested [verify].
- **Penetrance and expressivity:** high penetrance in reported probands, though ascertainment is biased toward severe cases.
- **Prevalence:** ultra-rare. Only dozens of cases (not hundreds) have been reported across CALM1-3 (the 2019 registry had 74 patients across all three genes [verify]). No incidence figure is available, and no sex or ethnic bias is established.
- **Founder effects and consanguinity:** none known. A Swedish CALM1 founder cluster exists for LQT14 and is not relevant to CALM2.

## 10. Diagnostics

- **ECG:** prolonged QTc, T-wave alternans and AV block on 12-lead ECG, Holter monitoring or exercise testing.
- **Genetic testing:** an LQTS or arrhythmia panel must include CALM1, CALM2 and CALM3, because older panels omitted them. Trio exome sequencing is useful for de novo variants. Confirm variant classification in ClinVar and ClinGen (no verified assertions listed here).
- **Differential diagnosis:** other LQTS genotypes (KCNQ1, KCNH2, SCN5A), Timothy syndrome (CACNA1C), CPVT, and AV block of other causes.
- **Screening:** cascade testing of parents and siblings, even where the variant is de novo, because of possible mosaicism.
- **Biomarkers, imaging and omics diagnostics:** none established.

## 11. Outcome and prognosis

- **Survival and mortality:** high risk of cardiac arrest and sudden death in infancy and early childhood. This follows from the reviews cited above; I could not retrieve numerical survival rates or the neurological sequelae rates.
- **Prognostic factors:** early age at first event, degree of QTc prolongation and presence of AV block are probable markers. They are not verified for CALM2 specifically.
- **Quality of life:** no data found.

## 12. Treatment

There are no trials or guidelines specific to CALM2 (no NCT identifiers were searched). Treatment follows LQTS practice plus small series:

- **Beta-blockers** (propranolol, nadolol; NCIT Pharmacotherapy `NCIT:C15986`). The 2023 Circ J study reported that beta-blockers were effective in nearly all cases, particularly combined with **flecainide** (CPVT-like phenotype) or **mexiletine** (LQTS-like) ([source](https://shiga-med.repo.nii.ac.jp/record/2000230/files/circj.CJ-23-0195.pdf)). It is a small series (10 probands across CALM1-3).
- **Sodium-channel blockers** (mexiletine, flecainide) shorten QTc in some patients. Flecainide has also been used for RyR2-related effects. I found no systematic outcome data on it.
- **Left cardiac sympathetic denervation** (`NCIT:C15329` surgical procedure), **ICD implantation** (device; bind the procedure, not the device, per the repo's NCIT rule) and **pacing** for AV block are options in refractory cases. Details beyond that are unverified.
- **Avoid** QT-prolonging drugs and correct hypokalemia and hypomagnesemia.
- **Experimental:** CRISPR/allele-specific silencing of the mutant allele and antisense approaches have been explored preclinically [verify]. No gene therapy is in clinical use.
- **Counseling:** genetic counseling for families (`NCIT:C15240`).

## 13. Prevention

- **Primary:** none.
- **Secondary and tertiary:** cascade ECG and genetic testing of relatives, prompt treatment of identified patients, drug avoidance lists and emergency plans for cardiac arrest. Preimplantation or prenatal testing is a theoretical option for recurrent families.

## 14. Other species

CALM2 is highly conserved. I did not check OMIA for natural disease in other species. A 2023 Channels paper on calmodulinopathy (doaj.org, appeared in search results) is a candidate for animal-model information.

## 15. Model organisms

- **Systems used:** iPSC-derived cardiomyocytes from patients, heterologous expression (e.g. HEK cells, voltage clamp of CaV1.2 and other channels), and recombinant calmodulin biophysics (Ca²⁺-binding assays). Reported results include prolonged Ca²⁺-current inactivation time constants [verify].
- **Animal models:** I did not verify any CALM2 knock-in mouse. The calmodulin genes are redundant, so the usual models are transgenic or knock-in variants rather than knockouts. Do not curate a model from this report without checking MGI and the primary papers.
- **Limitations:** the shared protein across three genes and the variable allelic expression of CALM1/2/3 transcripts complicate the interpretation of single-gene models.

## Sources actually retrieved

- [OMIM #616249 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/616249)
- [OMIM #616247](https://https.ncbi.nlm.nih.gov/omim/616247)
- [PanelApp CALM2](https://panelapp-aus.org/panels/131/gene/CALM2/)
- [Frontiers Cardiovasc Med 2018 calmodulinopathy review](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2018.00175/full)
- [Circ J 2023 calmodulinopathy pediatric cohort](https://shiga-med.repo.nii.ac.jp/record/2000230/files/circj.CJ-23-0195.pdf)

## Gaps and verification list

1. Confirm the MONDO ID for LQT15 and the HGNC id for CALM2 (OAK lookups).
2. Fetch Crotti et al. 2013 (PMID:23388215) and the 2019 Eur Heart J registry paper. I did not confirm the 2019 PMID.
3. Confirm per-phenotype frequencies and survival statistics from the registry.
4. Check the HPO and GO CURIEs above. They were proposed from memory.
5. Check ClinGen for CALM2 gene-disease validity records (`CGGV:`) before filling `gene_disease_validity`.
6. Search MGI, ZFIN and OMIA for animal models.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 7 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031546` (1 mention) - the report calls it "verify"; HP calls it **Cardiac conduction abnormality**
- `HP:0010646` (1 mention) - the report calls it "verify"; HP calls it **Cervical spine instability**
- `CL:0002494` (1 mention) - the report calls it "verify"; CL calls it **cardiocyte**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001657` (1 mention) - the report calls it "Long QT interval / prolonged QTc"; HP calls it **Prolonged QT interval**, and lists "Prolong qt interval on ekg" among its other names
- `HP:0001263` (1 mention) - the report calls it "Neurodevelopmental delay"; HP calls it **Global developmental delay**, and lists "Developmental delay" among its other names
- `UBERON:0000948` (1 mention) - the report calls it "Organ:** heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names