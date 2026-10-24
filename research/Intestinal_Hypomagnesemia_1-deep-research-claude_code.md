---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T02:23:50.392123'
end_time: '2026-10-24T02:25:06.013592'
duration_seconds: 75.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Intestinal Hypomagnesemia 1
  mondo_id: MONDO:0011176
  category: Mendelian
  causal_genes: TRPM6
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
  web_search_requests: 4
  num_turns: 6
  total_cost_usd: 0.8403999000000002
  session_id: 1cf15249-1f26-5978-9d50-1c0a311fb777
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 9
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 14
  verified: 14
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 4
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0011176
    reported_labels:
    - supplied
    ontology_label: intestinal hypomagnesemia 1
  - term_id: HP:0001250
    reported_labels:
    - Seizures (generalized, neonatal or infantile)
    ontology_label: Seizure
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intestinal Hypomagnesemia 1
- **MONDO ID:** MONDO:0011176 (if available)
- **Causal gene(s):** TRPM6
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

Please provide a comprehensive research report on **Intestinal Hypomagnesemia 1** covering all of the
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

# Intestinal Hypomagnesemia 1 (hypomagnesemia with secondary hypocalcemia, HSH): causal gene TRPM6

**Scope and verification.** I ran four web searches in this session. PMIDs marked ✔ were returned by those searches. Everything else comes from my background knowledge and is marked *(unverified)*. Check those against PubMed before they are used as evidence items, and fetch each reference with `just fetch-reference` so the snippets can be matched to the cache. I wrote no quoted snippets, because I have not read the abstracts here. OMIM 602014 and the ICD-10 code E83.4 below are also from memory; MONDO:0011176 is the ID you supplied.

## 1. Disease information

Intestinal hypomagnesemia 1 is the MONDO name for **hypomagnesemia with secondary hypocalcemia (HSH)**. It is an autosomal recessive disorder caused by biallelic loss-of-function variants in **TRPM6** (HGNC symbol TRPM6, chromosome 9q21.13). TRPM6 encodes a TRPM-family cation channel-kinase that is the closest homolog of TRPM7.

- **Overview.** Primary defects in intestinal Mg²⁺ absorption and renal Mg²⁺ reclamation cause very low serum magnesium. Hypocalcemia follows secondarily. The usual presentation is neonatal or early-infantile seizures and tetany, which are preventable and treatable with high-dose magnesium.
- **Identifiers.** MONDO:0011176 (supplied). OMIM #602014 *(from memory)*. The Orphanet and ICD-10 codes (E83.4, disorders of magnesium metabolism) I did not check.
- **Synonyms.** Familial hypomagnesemia with secondary hypocalcemia; primary hypomagnesemia with secondary hypocalcemia; HOMG1.
- **Data source.** Disease-level, aggregated from published family and cohort series. It is not EHR-derived.

## 2. Etiology

- **Cause.** Biallelic TRPM6 loss of function.
  - Positional cloning established the gene in 2002. Two independent studies appeared back to back in Nature Genetics.
  - **Schlingmann et al., Nat Genet 2002;31:166-70, PMID:12032568** ✔. They used a positional candidate approach to place the disorder at 9q22 and found TRPM6 mutations.
  - **Walder et al., Nat Genet 2002;31:171-4, PMID:12032570** ✔. Mapping in three large inbred Israeli kindreds led to TRPM6. Affected individuals also showed abnormal renal Mg²⁺ excretion.
- **Risk and protective factors.** No environmental risk factors are known. Carriers are generally asymptomatic *(unverified)*.
- **Modifiers and gene–environment interaction.** I found no evidence of either. Dietary Mg²⁺ intake determines how much the lifelong supplementation can compensate, but that is treatment, not etiology.

## 3. Phenotypes

Frequencies are qualitative because I did not retrieve the cohort tables. The 21-family JASN cohort (Schlingmann 2005; see §4) is the best source for exact frequencies.

| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Hypomagnesemia (serum Mg typically very low) | HP:0002917 | Core laboratory feature. |
| Hypocalcemia, secondary | HP:0002901 | Caused by impaired PTH secretion and end-organ resistance *(inferred, see §6)*. |
| Hypoparathyroidism / inappropriately low PTH | HP:0000829 | Reversible with Mg repletion. |
| Seizures (generalized, neonatal or infantile) | HP:0001250 | Usual presenting sign. |
| Tetany | HP:0001281 | Hypocalcemic and hypomagnesemic. |
| Muscle spasms / hyperexcitability | HP:0003394 | |
| Developmental delay / intellectual disability | HP:0001263 / HP:0001249 | Occurs after untreated or late-treated seizures and prolonged hypomagnesemia. |
| Hypokalemia | HP:0002900 | Reported in some patients *(unverified)*. |
| Failure to thrive | HP:0001508 | In some patients *(unverified)*. |

- **Onset.** Neonatal to early infancy, typically in the first weeks to months.
- **Course.** Stable and lifelong if untreated, with episodic seizures and tetany.
- **Severity.** Severe and potentially fatal, or neurologically damaging, if untreated. Largely normal outcomes are the norm with early, adequate Mg²⁺ therapy *(unverified)*.
- **Quality of life.** Mostly determined by neurological sequelae and by tolerance of high-dose oral magnesium (diarrhea). I did not search for QoL instruments.

## 4. Genetic and molecular information

- **Gene and protein.** TRPM6 (hgnc symbol TRPM6; use the lowercase `hgnc:` CURIE form after looking it up in HGNC). It encodes a ~2,022-residue channel-kinase with an N-terminal TRP channel region, a transmembrane pore and a C-terminal alpha-kinase domain.
- **Variant spectrum.**
  - Mostly truncating variants (nonsense, frameshift, splice site) that leave no functional protein.
  - Published reports describe the S141L missense variant as the first and only point mutation known in the early series. Later missense reports exist.
  - **Schlingmann et al., J Am Soc Nephrol 2005, "Novel TRPM6 mutations in 21 families with primary hypomagnesemia and secondary hypocalcemia"** ✔ (title, journal and cohort confirmed; **PMID not returned, look it up**).
    - 28 affected individuals from 21 families.
    - Mutations found in 37 of 42 expected mutant alleles; 16 of the mutations were new.
    - Xenopus-oocyte electrophysiology showed complete loss of function for the mutant channels.
    - The paper includes a retrospective clinical review.
  - **Lainez et al., Eur J Hum Genet 2014**, new TRPM6 missense mutations *(unverified, from memory)*.
- **Functional consequence.** Loss of function. Mutant channels are non-conducting, and truncations give no protein.
- **Channel assembly.**
  - **Chubanov et al., PNAS 2004;101:2894-9, PMID:14976260** ✔. Full-length TRPM6 was retained intracellularly on its own in HEK293 cells and Xenopus oocytes. It formed functional channel complexes with TRPM7 at the cell surface. The S141L missense variant abolished TRPM6 oligomeric assembly.
  - The 2004 conclusion that TRPM6 needs TRPM7 was later disputed. Voets and colleagues had expressed functional TRPM6 alone, and the TRPM6 literature remained controversial. Ferioli et al. 2017 (Sci Rep) reported that TRPM6/7 heteromers have high constitutive activity at physiological Mg²⁺ and Mg·ATP.
  - For KB purposes, state both views and the disagreement. Do not describe the heteromer requirement as settled.
- **Modifier genes, epigenetics, chromosomal abnormalities.** None established. A balanced translocation breakpoint was part of the original 9q mapping *(unverified)*.
- **Allele frequency.** Not retrieved. Check gnomAD and ClinVar for the specific alleles you curate.

## 5. Environmental information

None are causal. Dietary and supplemental Mg²⁺ modify disease expression and are covered under Treatment. No infectious agent is involved. Tooth extraction and similar procedures are not relevant.

## 6. Mechanism / pathophysiology

**Causal chain** (steps marked *inferred* are standard interpretations that I did not verify against a primary quote in this session):

1. Biallelic TRPM6 loss-of-function variants (truncations; rare missense variants that abolish channel assembly or function) remove functional TRPM6 channels. Demonstrated by Schlingmann 2002, Walder 2002, Schlingmann 2005 and Chubanov 2004.
2. TRPM6 normally mediates Mg²⁺ entry across the apical membrane of **intestinal epithelium** (Mg²⁺ absorption) and **distal convoluted tubule** cells (renal Mg²⁺ reabsorption). The tissue localization is established in the literature; I did not cite a primary source for it here.
3. Loss of transcellular Mg²⁺ uptake leads to reduced intestinal absorption and renal Mg²⁺ wasting, and so to severe hypomagnesemia. At this step the intestinal defect predominates, which is why the MONDO name says "intestinal".
4. Intracellular and extracellular Mg²⁺ deficiency impair parathyroid hormone secretion and action (Mg²⁺ is needed for both). The result is functional hypoparathyroidism and **secondary hypocalcemia** *(inferred; classical physiology)*.
5. Hypomagnesemia and hypocalcemia increase neuromuscular excitability and lead to tetany and seizures.
6. Prolonged, untreated hypomagnesemia and seizures lead to neurological damage and developmental impairment *(inferred)*.
7. The pathway is rescuable. Pharmacologic Mg²⁺ loading bypasses the defective transcellular route through paracellular passive uptake at high luminal concentration *(inferred)*. This explains why very high oral doses normalize serum Mg²⁺ and calcium.

- **GO suggestions.** Magnesium ion transmembrane transport; magnesium ion homeostasis; cellular response to magnesium ion starvation (look the exact IDs and labels up in OLS or the cache).
- **Cell types (CL).** Enterocyte; kidney distal convoluted tubule epithelial cell. Parathyroid chief cell as a secondary site. Look up the CURIEs.
- **Omics.** I found no relevant single-cell, proteomic or metabolomic studies.

## 7. Anatomical structures affected

- **Primary:** small and large intestine (epithelium) and kidney (distal convoluted tubule).
- **Secondary:** parathyroid gland (functional); brain and nervous system (seizures, developmental delay); skeletal muscle (tetany).
- **Subcellular:** apical plasma membrane for the channel; the kinase domain is cytosolic.
- **Laterality:** not applicable (systemic).

## 8. Temporal development

Onset is in the neonatal period to early infancy. The disease is lifelong and stable with treatment, with no progressive degeneration beyond what seizures or prolonged hypomagnesemia cause. Early diagnosis and treatment before neurological injury is the critical window. Remission occurs only with continued supplementation.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007).
- **Penetrance:** apparently high *(unverified)*.
- **Consanguinity:** many families are consanguineous. The three Israeli kindreds used for the Walder 2002 mapping are an example.
- **Founder variants and population distribution:** not established here. Frequency and sex ratio were not retrieved.
- **Prevalence:** very rare. I did not retrieve an Orphanet figure. Check Orphanet before using any `prevalence_class`.

## 10. Diagnostics

- **Laboratory.** Serum Mg²⁺ is markedly low. Calcium is low, PTH low or inappropriately normal, and urinary Mg²⁺ is low-normal or inappropriately high relative to serum.
- **Differential.**
  - Other genetic hypomagnesemias, which mostly present with renal Mg²⁺ wasting.
  - Other causes of neonatal hypocalcemia.
  - Gitelman syndrome and related tubulopathies.
  - Primary hypoparathyroidism.
  - Acquired causes (PPIs, diuretics, aminoglycosides).
  - Distinguishing feature: an early-onset intestinal defect, with hypocalcemia that is corrected by Mg²⁺ repletion.
- **Genetic confirmation.** Single-gene TRPM6 sequencing, a hypomagnesemia gene panel, or exome sequencing. Include copy-number analysis *(general practice, unverified)*.
- **Screening.** No newborn screening is established. Cascade testing of siblings is reasonable.

## 11. Outcome and prognosis

Untreated, the disease causes seizures and can be fatal. With early lifelong Mg²⁺ supplementation, the outcome is generally good, though neurological sequelae occur when treatment is delayed. Complications include the diarrhea that high Mg²⁺ doses cause, which can limit adherence. I found no cohort survival figures.

## 12. Treatment

- **Mainstay: lifelong high-dose oral magnesium.** The 2002 papers noted that life-long Mg²⁺ supplementation is needed to overcome the defect, and a general summary page said the same.
- **Acute: intravenous magnesium** for seizures and tetany, then transition to oral.
- **Calcium and vitamin D.** Calcium alone is ineffective until Mg²⁺ is replete *(inferred)*.
- **Suggested NCIT terms** (look up in the cache or OLS, do not use CURIEs from memory):
  - NCIT:C15986 Pharmacotherapy as the action term, with magnesium salts as `therapeutic_agent` (CHEBI).
  - NCIT:C15433 Nutritional Support only after checking it. Magnesium here is a drug-like supplement, so `SMALL_MOLECULE` is the `therapeutic_modality`. See the CLAUDE.md warning against tagging supplements as `BEHAVIORAL`.
- **Experimental:** none identified. I did not search ClinicalTrials.gov.
- **Pharmacogenomics:** none relevant.

## 13. Prevention

- **Primary:** none.
- **Secondary and tertiary:** early detection by magnesium testing in infants with seizures. Prevent neurological injury with prompt Mg²⁺ repletion.
- **Genetic counseling** and carrier or prenatal testing for at-risk families.

## 14. Other species and natural disease

I found no OMIA entry and did not search for one. Treat naturally occurring disease in other species as not established.

## 15. Model organisms

- **Mouse Trpm6 knockout.** Homozygous deletion is embryonic lethal, and a high-Mg²⁺ diet did not rescue it.
  - One study (human-gene-knockout work in Hum Mol Genet, 2009 by my search summary; **not independently verified, PMID not retrieved**) found that Trpm6⁻/⁻ mice almost never survived to weaning. Many died by E12.5, and most that survived to term had neural tube defects (exencephaly and spina bifida occulta). A high-Mg²⁺ maternal diet only marginally improved survival.
  - A Nephron Physiology paper (2011 per search; authors not confirmed) reported that heterozygotes had mild hypomagnesemia and that Mg²⁺-enriched diet did not compensate for either lethality or hypomagnesemia. PubMed 20814221 appeared in the results but I did not confirm it is this paper.
  - **eLife 2016 (Epithelial magnesium transport by TRPM6 is essential for prenatal development and adult survival)** attributes the lethality to TRPM6 deficiency in extraembryonic tissues rather than the embryo itself. Use it, not my summary, for anything quotable.
  - A 2017 study reported that Trpm6 loss also perturbs cellular Mg²⁺ homeostasis and produces early embryonic lethality and neural tube closure defects.
- **Fidelity.** Poor as a model of the human disease. Human patients survive to birth and are treatable, while the mouse knockout is embryonic lethal, a clear instance of `HUMAN_MODEL_MISMATCH` in KB terms. In the pathograph, `FAILS_TO_RECAPITULATE` would require `limitations` and evidence. Conditional (tissue-specific) knockouts are the better tool for adult Mg²⁺ handling *(unverified)*.
- **In vitro:** HEK293 cells and Xenopus oocytes were used for the channel assembly and electrophysiology studies above.

## Before curating

1. Look up and fetch every PMID, especially the unverified ones (the 2005 JASN paper, 2009 HMG knockout, 2014 Lainez, 2016 eLife).
2. Look up the MONDO, HPO, GO, CL and NCIT CURIEs in the ontology caches. I wrote none from memory.
3. Get quantitative phenotype frequencies from the 2005 JASN series.
4. Check GeneReviews: HSH may have a chapter, which would be the Mendelian baseline.
5. Confirm OMIM #602014 and the Orphanet code.

**Sources**
- [Schlingmann et al. 2002 record (Regensburg repository)](https://pred.uni-regensburg.de/id/eprint/40212/)
- [Walder et al. 2002 record (Iowa)](https://iro.uiowa.edu/esploro/outputs/journalArticle/Mutation-of-TRPM6-causes-familial-hypomagnesemia/9984065385302771)
- [Chubanov et al. 2004, PMC365716](https://pmc.ncbi.nlm.nih.gov/articles/PMC365716)
- [Chubanov 2004 relationship table, PMID 14976260](https://cpi.vm.uni-freiburg.de/cpril/article_relationships_table_per_entity/pmid=14976260pid=16179)
- [Schlingmann 2005 JASN record](https://olympias2.lib.uoi.gr/items/4c367f23-97ca-4206-8045-c8fa79ebb933)
- [MedlinePlus: HSH](https://medlineplus.gov/genetics/condition/hypomagnesemia-with-secondary-hypocalcemia)
- [eLife 2016, TRPM6 in prenatal development](https://elifesciences.org/articles/20914)
- [Mice defective in Trpm6 show embryonic mortality](https://iro.uiowa.edu/esploro/outputs/journalArticle/Mice-defective-in-Trpm6-show-embryonic/9983557779902771)
- [PubMed 20814221](https://pubmed.ncbi.nlm.nih.gov/20814221/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 10 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011176` (2 mentions) - the report calls it "supplied"; MONDO calls it **intestinal hypomagnesemia 1**
- `HP:0001250` (1 mention) - the report calls it "Seizures (generalized, neonatal or infantile)"; HP calls it **Seizure**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002917` (1 mention) - the report calls it "Hypomagnesemia (serum Mg typically very low)"; HP calls it **Hypomagnesemia**
- `HP:0002901` (1 mention) - the report calls it "Hypocalcemia, secondary"; HP calls it **Hypocalcemia**
- `HP:0000829` (1 mention) - the report calls it "Hypoparathyroidism / inappropriately low PTH"; HP calls it **Hypoparathyroidism**
- `HP:0003394` (1 mention) - the report calls it "Muscle spasms / hyperexcitability"; HP calls it **Muscle spasm**