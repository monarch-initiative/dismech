---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T02:24:25.375722'
end_time: '2026-10-24T02:25:28.280375'
duration_seconds: 62.9
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autosomal Dominant Hypocalcemia 2
  mondo_id: MONDO:0014146
  category: Mendelian
  causal_genes: GNA11
  omim_id: not recorded
  synonyms: not recorded
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
  num_turns: 5
  total_cost_usd: 0.7006330999999999
  session_id: 1cf15249-1f26-5978-9d50-1c0a311fb777
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 4
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 23
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 8
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0008207
    reported_labels:
    - Primary hypoparathyroidism
    ontology_label: Primary adrenal insufficiency
  - term_id: HP:0003542
    reported_labels:
    - Hypercalciuria
    ontology_label: Increased circulating pyruvate concentration
  - term_id: GO:0035965
    reported_labels:
    - recall
    ontology_label: cardiolipin acyl-chain remodeling
  - term_id: CL:0002238
    reported_labels:
    - recall
    ontology_label: male gonocyte
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Hypocalcemia 2
- **MONDO ID:** MONDO:0014146 (if available)
- **Causal gene(s):** GNA11
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Hypocalcemia 2** covering all of the
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

# Autosomal Dominant Hypocalcemia 2 (ADH2; GNA11 gain-of-function): research report

**Scope and verification.** The disease is ADH2, MONDO:0014146. The causal gene is **GNA11** (hgnc:4379; OMIM *139313), which encodes the G-protein α11 subunit (Gα11). The OMIM phenotype entry is #615361; I recalled this and did not verify it.

I ran three web searches. Findings marked **[verified]** come from those results. Findings marked **[recall]** come from my own background knowledge and are not backed by a source I opened. The searches returned no PMIDs, so I give only the PMID I am fairly confident of and cite the rest by URL. Check every PMID and every direct quote against the cached reference before curating. I give no verbatim quotes, because I have not read the full abstracts.

## 1. Disease information
- ADH2 is a rare, dominantly inherited hypoparathyroid-type hypocalcemia. Gain-of-function variants in GNA11 make the calcium-sensing receptor (CaSR) signal too strongly, so the parathyroid gland and kidney "read" normal calcium as high. [verified]
- The same gene causes the opposite disorder when it loses function. Loss-of-function GNA11 variants cause familial hypocalciuric hypercalcemia type 2 (FHH2). [verified]
- The discovery paper is Nesbit et al., "Mutations affecting G-protein subunit α11 in hypercalcemia and hypocalcemia", N Engl J Med 2013 (PMID:23802516 [recall]; [abstract record](https://scholarworks.indianapolis.iu.edu/items/dcb7764c-3c29-4e2d-8675-93a4f8b06d1b)). [verified]
- Nesbit et al. screened GNA11 in eight hypocalcemic patients with no CASR mutation. They found missense variants (Arg181Gln and Phe341Leu) in two unrelated patients. [verified]
- Related entity: ADH1 (CASR gain-of-function, MONDO ID not checked). Synonyms I recall are "hypocalcemia, autosomal dominant 2" and "GNA11-related hypocalcemia". The template recorded none.
- This is an aggregate, disease-level description. It is not patient-level EHR data.

## 2. Etiology
- **Cause:** heterozygous germline gain-of-function missense variants in GNA11. [verified]
- Reported variants:
  - Arg181Gln and Phe341Leu (Nesbit 2013). [verified]
  - Val340Met, described in a later ADH2 family. [verified; the search snippet gave no author or journal]
  - Arg60Cys, which is also the variant in the knock-in mouse. [verified]
  - I recall others, such as Thr54Met and Ser211Trp, but did not verify them.
- **Risk and protective factors:** no environmental risk or protective factors are known. Gene–environment interaction is not applicable beyond calcium and vitamin D intake, which modulate the phenotype only in the sense of treatment response. [recall]

## 3. Phenotypes
All frequencies and onset ages below are **[recall]** and need verification against case series.

| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Hypocalcemia | HP:0002901 | Core feature; often mild to moderate. |
| Low or inappropriately normal PTH | HP:0008207 (Primary hypoparathyroidism) is the closest term; check it. | PTH is low, so this is functional hypoparathyroidism. |
| Hyperphosphatemia (mild) | HP:0002905 | Variable. |
| Hypomagnesemia | HP:0002917 | Often present. |
| Relative hypercalciuria at low serum calcium | HP:0003542 (Hypercalciuria) | Treatment with calcium and vitamin D worsens it. |
| Seizures or tetany, paresthesias | HP:0001250, HP:0001281, HP:0003401 | Can be symptomatic or asymptomatic. |
| Nephrocalcinosis or nephrolithiasis | HP:0000121, HP:0000787 | Risk is mainly treatment-related. |
| Basal ganglia calcification | HP:0002135 | Reported in some patients. |
| Short stature | HP:0004322 | Reported in some patients. |
| Dark skin pigmentation | not mapped | Seen in mice (see section 15); not clearly established in humans. |

Onset ranges from infancy to adulthood. The course is lifelong and stable, with episodic symptoms during illness or fever.

## 4. Genetic and molecular information
- **Gene and protein:** GNA11 on 19p13.3 encodes Gα11, the main Gαq/11 partner of CaSR in parathyroid and renal cells. [recall]
- **Mechanism:**
  - Gain of function, heterozygous. In HEK293 cells, ADH2 variants raised sensitivity to extracellular calcium and were predicted to disrupt protein structure. [verified]
  - The Val62 Gα11 variant raised CaSR-mediated intracellular calcium and MAPK signaling. [verified]
- **Variant frequency, ACMG classification and ClinGen validity:** not checked. Run `just check-gene-validity` and look up the CGGV record before recording a tier.
- **Epigenetics, modifier genes and chromosomal abnormalities:** none known.

## 5. Environmental information
None are established. Dietary calcium and vitamin D are treatment variables, not causes. Infectious agents are not applicable.

## 6. Mechanism and pathophysiology

**Causal chain**
1. A germline heterozygous missense variant in GNA11 produces a hyperactive Gα11. [verified]
2. The variant protein increases CaSR-coupled Gq/11 signaling, shown by increased intracellular calcium mobilization and MAPK signaling. [verified]
3. CaSR on the parathyroid chief cell therefore perceives normal serum calcium as high. This leads to suppressed PTH secretion and a lower set-point for hypocalcemia (inferred). [verified in the mouse: low calcium with low PTH]
4. In the kidney thick ascending limb, CaSR overactivity inhibits paracellular calcium and magnesium reabsorption. This leads to hypercalciuria relative to the serum calcium and to hypomagnesemia (inferred from the ADH1 paradigm [recall]).
5. Low PTH plus low serum calcium leads to hypocalcemic symptoms: tetany, seizures and paresthesias.
6. Treatment with calcium and vitamin D raises urinary calcium further, which leads to nephrocalcinosis (treatment-related; recall).

**Where it branches.** The renal arm (step 4) does not depend on PTH. The skin-pigmentation finding in mice has no established human mechanism.

**Suggested ontology terms** (look each up before binding):
- GO: "calcium-mediated signaling" (GO:0019722), "G protein-coupled receptor signaling pathway" (GO:0007186), "positive regulation of MAPK cascade" (GO:0043410), "parathyroid hormone secretion" (GO:0035965 [recall]).
- CL: parathyroid chief cell (CL:0002238 [recall]), and kidney thick ascending limb epithelial cell.
- UBERON: parathyroid gland (UBERON:0001132), kidney (UBERON:0002113).
- CHEBI: calcium(2+) (CHEBI:29108).

Transcriptomics, proteomics and single-cell data: none found.

## 7. Anatomical structures affected
- **Primary:** the parathyroid gland and the kidney (thick ascending limb and distal tubule).
- **Secondary:** the CNS (seizures, basal ganglia calcification) and the neuromuscular system. Bone density is low in the mouse model. [verified]
- Involvement is systemic and bilateral.

## 8. Temporal development
Onset is variable, from neonatal to adult, and the course is lifelong and non-progressive. There are no staged progression or remission patterns [recall]. Symptoms flare during intercurrent illness or fever.

## 9. Inheritance and population
- **Inheritance:** autosomal dominant (HP:0000006). Penetrance is high but expressivity is variable. [recall]
- Both familial and de novo cases occur. [recall]
- **Prevalence:** ultra-rare; the world prevalence is undocumented, and no registry estimate was verified. Use `prevalence_class: NOT_YET_DOCUMENTED` unless an Orphanet row is quoted.
- The founder-effect, sex-ratio, consanguinity and carrier-frequency items are not applicable or not documented.

## 10. Diagnostics
- **Laboratory:** low serum calcium (ionized or albumin-corrected), low or inappropriately normal PTH, high-normal or high phosphate, low or low-normal magnesium, and relatively high urinary calcium.
- **Imaging:** renal ultrasound for nephrocalcinosis, and head CT for basal ganglia calcification.
- **Genetic testing:** a gene panel for hypoparathyroidism or ADH covering CASR, GNA11, AP2S1 and PTH. Whole-exome sequencing is an alternative. Single-gene GNA11 sequencing follows a negative CASR result. [recall]
- **Differential diagnosis:** ADH1 (CASR), acquired hypoparathyroidism, pseudohypoparathyroidism, vitamin D deficiency, and 22q11.2 deletion.
- LOINC codes were not looked up. Per repository rules, seed them with `just loinc-seed-cache` rather than typing labels.

## 11. Prognosis
Life expectancy is expected to be normal [recall]. Morbidity comes from seizures, and from nephrocalcinosis and renal impairment if hypercalciuria is aggravated by treatment. I found no quantitative survival or quality-of-life data.

## 12. Treatment
- **Conventional:** oral calcium and active vitamin D (calcitriol or alfacalcidol), only for symptoms, using the lowest dose that avoids symptoms. Correct magnesium. Thiazide diuretics can reduce hypercalciuria. [recall]
- **PTH replacement:** teriparatide or rhPTH(1-34) has been used in ADH1 and ADH2 case series; rhPTH(1-84) has also been used. [recall]
- **Targeted: calcilytics.** These are CaSR negative allosteric modulators.
  - In the Dsk7 (Gα11 Ile62Val) mouse, NPS-2143 raised plasma PTH and calcium until the animals were normocalcemic. [verified: [Gorvin et al., JCI Insight](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5291742/)]
  - In the Arg60Cys knock-in mouse, NPS 2143 raised PTH and calcium. [verified]
  - In human trials, NPSP795 (SHP635) and encaleret have been tested mainly in ADH1. [recall] The searches found no ADH2-specific human efficacy data, so I did not verify this. Search ClinicalTrials.gov for NCT numbers.
- **NCIT binding:** use NCIT:C15986 (Pharmacotherapy) as the generic `treatment_term`. Put the agents in `therapeutic_agent`, and check ChEBI and NCIT for each of calcitriol, calcium carbonate, teriparatide and the calcilytics. Set `therapeutic_modality: SMALL_MOLECULE` for the calcilytics and `PEPTIDE` for PTH.

## 13. Prevention
Cascade genetic testing of relatives and genetic counseling (50% recurrence risk per pregnancy for an affected parent), plus prenatal or preimplantation testing where requested. Tertiary prevention is monitoring of urinary calcium and renal ultrasound to prevent nephrocalcinosis. There is no primary prevention, no vaccine, and no population screening.

## 14. Other species and natural disease
No naturally occurring animal disease was found. I did not check OMIA. The orthologous mouse gene is Gna11 (NCBI Gene ID not looked up).

## 15. Model organisms
| Model | Genotype | Findings |
|---|---|---|
| Dsk7 mouse (pre-existing ENU mutant) | Gα11 Ile62Val; heterozygous and homozygous | Hypocalcemia and reduced PTH, like ADH2 patients; dark skin. NPS-2143 normalized calcium and PTH. [verified, [JCI Insight](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5291742/)] |
| Arg60Cys knock-in mouse (Roszko et al.) | Human-patient GNA11 R60C | Faithfully replicated human ADH2, with low bone mineral density and increased skin pigmentation. NPS 2143 raised PTH and calcium. [verified in search summary; the PMC link in the results was [PMC4915495](https://pmc.ncbi.nlm.nih.gov/articles/PMC4915495), but I did not confirm it is this paper] |
| HEK293 cell assays | Transfected Gα11 mutants with CaSR | Increased calcium sensitivity and MAPK signaling. [verified, [Nesbit 2013](https://scholarworks.indianapolis.iu.edu/items/dcb7764c-3c29-4e2d-8675-93a4f8b06d1b)] |

Model limitations: rodent parathyroid and renal calcium handling differ in detail from human, and the pigmentation phenotype is not established in humans. For curation, link the mice to the PTH-suppression node with `modeled_mechanisms`, using `RECAPITULATES` or `PARTIALLY_RECAPITULATES` and `evidence_source: MODEL_ORGANISM`. Resources: MGI, IMPC, and the Alliance of Genome Resources.

## Curation cautions
1. Fetch each PMID with `just fetch-reference` and copy snippets from the cached abstract. I have quoted none here.
2. Do not bind the GNA11 gene to a different HGNC entry. Confirm hgnc:4379 is GNA11 with `just validate-terms`. GNA11 is easy to confuse with GNAQ and GNAS.
3. Run `just preflight-dr` on this report before using its leads.

Sources:
- [Nesbit et al. record (IUPUI ScholarWorks)](https://scholarworks.indianapolis.iu.edu/items/dcb7764c-3c29-4e2d-8675-93a4f8b06d1b)
- [Gorvin et al., Gα11 mutation in mice causes hypocalcemia rectifiable by calcilytic therapy (PMC5291742)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5291742/)
- [PMC4915495](https://pmc.ncbi.nlm.nih.gov/articles/PMC4915495)
- [JCI Insight 91079 citations](https://insight.jci.org/articles/view/91079/citations)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 15 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0008207` (1 mention) - the report calls it "Primary hypoparathyroidism"; HP calls it **Primary adrenal insufficiency**
- `HP:0003542` (1 mention) - the report calls it "Hypercalciuria"; HP calls it **Increased circulating pyruvate concentration**
- `GO:0035965` (1 mention) - the report calls it "recall"; GO calls it **cardiolipin acyl-chain remodeling**
- `CL:0002238` (1 mention) - the report calls it "recall"; CL calls it **male gonocyte**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002905` (1 mention) - the report calls it "Hyperphosphatemia (mild)"; HP calls it **Hyperphosphatemia**
- `GO:0019722` (1 mention) - the report calls it "calcium-mediated signaling", "GO: "calcium-mediated signaling"; GO calls it **calcium-mediated signaling**
- `UBERON:0001132` (1 mention) - the report calls it "UBERON: parathyroid gland"; UBERON calls it **parathyroid gland**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0019722` - called "calcium-mediated signaling", "GO: "calcium-mediated signaling"