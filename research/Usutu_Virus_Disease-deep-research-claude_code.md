---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-04T12:42:49.585401'
end_time: '2026-11-04T12:46:57.308483'
duration_seconds: 247.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Usutu Virus Disease
  mondo_id: ''
  category: Infectious
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: USUV infection; Usutu virus infection
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 15
  total_cost_usd: 2.2619626999999998
  session_id: 69808c41-6fbf-4724-8dd3-936af1b0ad6d
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:37589592
  relevance_assessed: 8
  on_topic: 8
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 36
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 12
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:0000540
    reported_labels:
    - neuron
    - Tissue/cell level:** neurons
    ontology_label: neuron
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Usutu Virus Disease
- **MONDO ID:**  (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** USUV infection; Usutu virus infection
- **Category:** Infectious

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Usutu Virus Disease** covering all of the
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

# Comprehensive Research Report: Usutu Virus Disease

**Prepared:** 2026-11-04 · **Category:** Infectious (arboviral) · **Primary identifier anchor:** NCBITaxon:64286 (Usutu virus)

**Note on identifiers and scope.** Usutu virus disease has **no causal human gene** — it is an acquired arboviral infection, so the template sections on causal genes, pathogenic variants, inheritance, penetrance, carrier frequency, and genetic modifiers are *not applicable* in the Mendelian sense and are addressed instead in terms of the **viral genome** and **host susceptibility factors**. The template lists "Causal gene(s): not recorded," which is correct: the etiologic agent is Usutu virus (USUV), an enveloped positive-sense single-stranded RNA flavivirus (genus *Orthoflavivirus*, family *Flaviviridae*), of the Japanese encephalitis serocomplex and a close relative of West Nile virus (WNV). There is at present **no MONDO term for human Usutu virus disease**; the only MONDO concept, MONDO:1015078, denotes "usutu virus infection, non-human animal." This report grounds the entity in NCBITaxon:64286 and recommends a human-disease MONDO term request.

---

## 1. Disease Information

Usutu virus disease is the human illness caused by USUV, a mosquito-borne flavivirus maintained in an **enzootic cycle between ornithophilic *Culex* mosquitoes and wild birds**. Humans and horses are **incidental, dead-end hosts** infected by the bite of an infected mosquito; they do not sustain transmission. Most human infections are **asymptomatic or produce a mild febrile illness** (fever, headache, rash); a minority develop **neuroinvasive disease** — meningitis, encephalitis, or meningoencephalitis.

**Key identifiers**
- **NCBITaxon:** 64286 (Usutu virus); family Flaviviridae, genus *Orthoflavivirus*.
- **MONDO:** none for the human disease (MONDO:1015078 = non-human animal infection only). *Recommend upstream human-disease term request.*
- **ICD-11:** no USUV-specific code; falls under arboviral/unspecified viral encephalitis or mosquito-borne viral fever categories (e.g., 1D4Z / 1C8Y style groupings for "other specified arboviral fevers/encephalitides").
- **ICD-10:** no specific code; A92.8 ("Other specified mosquito-borne viral fevers") / A85.2 ("Arthropod-borne viral encephalitis, unspecified") are the closest.
- **OMIM / Orphanet:** not applicable (not a Mendelian or listed rare genetic disease).
- **MeSH:** "Usutu virus" exists as a supplementary concept/organism term; no dedicated disease MeSH heading.

**Synonyms:** USUV infection; Usutu virus infection.

**Data provenance:** Information is derived from **aggregated disease-level resources** — surveillance reports (ECDC/EuroSurveillance), case reports, seroprevalence studies, and experimental virology — rather than from large individual-patient/EHR cohorts, reflecting the rarity of recognized human disease.

---

## 2. Etiology

**Causal factor (infectious).** USUV infection acquired through the bite of an infected *Culex* mosquito (principally *Culex pipiens*). First isolated from mosquitoes in **South Africa in 1959** (named for the Usutu River in Eswatini/Swaziland); it emerged in Europe with a large bird die-off in **Vienna, Austria, in 2001**, with retrospective evidence of circulation in **Italy from ~1996** (["Emergence of Usutu virus, an African mosquito-borne flavivirus… central Europe," Weissenböck et al., *Emerg Infect Dis* 2002, PMID:12095429](https://wwwnc.cdc.gov/eid/article/8/7/02-0094)). At the amino-acid level the Austrian and South African isolates were essentially identical over the region examined.

**Risk factors**
- **Environmental/exposure:** residence in or travel to endemic areas of southern/central Europe during the mosquito season (late summer–autumn); outdoor exposure; proximity to enzootic bird–*Culex* foci. Climate and environmental change are expected to expand range ([EU/EEA review, *Euro Surveill* 2023, PMID:37589592](https://www.pubmed.gov/37589592/)).
- **Host immune status:** **immunocompromise** is the classically cited risk factor for neuroinvasive disease — the first recognized human neuroinvasive cases (Italy, 2009) were in immunosuppressed patients (one with diffuse large B-cell lymphoma). *However*, the 2012–2021 EU/EEA surveillance review notes that **none of the 12 neuroinvasive cases in that dataset were reported as immunocompromised**, indicating neuroinvasion is not restricted to the immunosuppressed (PMID:37589592). Both facts should be curated, as they appear to conflict and reflect evolving epidemiology.
- **Transfusion:** USUV RNA has been detected in **asymptomatic blood donors**, creating a documented transfusion-transmission risk and the rationale for blood-safety screening.
- **Genetic host risk/protective factors:** no human germline susceptibility/protective loci are established. Experimentally, **type I interferon (IFN) signaling and STAT1 are the dominant host restriction factors** (see §6).

**Gene–environment interaction:** not characterized in humans; in mouse models, disruption of innate IFN signaling converts a resisted exposure into lethal neuroinvasive infection (§6, §15).

---

## 3. Phenotypes

Most infections are **asymptomatic**. Symptomatic disease spans a mild systemic syndrome and a rare neuroinvasive syndrome.

| Phenotype | Type | HPO suggestion | Notes / frequency |
|---|---|---|---|
| Fever | Symptom | **HP:0001945** Fever | Core of the febrile syndrome |
| Headache | Symptom | **HP:0002315** Headache | Common in symptomatic cases |
| Skin rash | Clinical sign | **HP:0000988** Skin rash | Reported in mild/febrile illness |
| Encephalitis | Clinical sign (neuroinvasive) | **HP:0002383** Infectious encephalitis | Rare, severe |
| Meningitis | Clinical sign (neuroinvasive) | **HP:0001287** Meningitis | Rare |
| Meningoencephalitis | Clinical sign | (compose: encephalitis + meningitis) | Classic 2009 presentation |
| Seizures | Clinical sign | **HP:0001250** Seizure | In neuroinvasive disease |
| Jaundice / hepatic involvement | Sign | **HP:0000952** Jaundice | Occasionally reported; prominent in animal/mouse disease |
| Tremor / hyperreflexia / gait disturbance | Neurological signs | HP:0001337 Tremor; HP:0001276 Hyperreflexia; HP:0001288 Gait disturbance | Reported in neuroinvasive cases |
| Rash + fever + headache triad | Composite | — | Typical mild presentation |

**Onset:** acute, days after the infective bite. **Severity:** predominantly mild/self-limited; neuroinvasive disease is severe but rare. **Progression:** self-limited in mild disease; neuroinvasive cases can be severe with variable recovery. **Frequency among infected:** the large majority asymptomatic; of 105 autochthonous EU/EEA infections (2012–2021), **85 were asymptomatic (mainly blood donors), ~8 febrile, and 12 neuroinvasive** (PMID:37589592).

**Quality-of-life impact:** not formally measured with EQ-5D/SF-36; neuroinvasive disease carries risk of residual neurological deficit; mild disease is transient.

---

## 4. Genetic / Molecular Information (viral genome; no human causal gene)

USUV has an ~11 kb positive-sense ssRNA genome encoding a single polyprotein cleaved into **3 structural proteins** (capsid C, premembrane prM/M, envelope E) and **7 nonstructural proteins** (NS1, NS2A, NS2B, NS3, NS4A, NS4B, NS5).

- **E (envelope):** receptor binding/fusion; principal neutralizing-antibody target and the basis of serologic cross-reactivity with WNV.
- **NS3:** protease (with NS2B cofactor) and helicase.
- **NS5:** methyltransferase + RNA-dependent RNA polymerase (RdRp); flaviviral NS5 is the canonical **type I IFN antagonist**. A **D3425E substitution in the NS5 RdRp domain** has been linked to neurovirulence differences between USUV lineages (in vivo/neuronal cell work, [*J Neuroinflammation* 2021](https://jneuroinflammation.biomedcentral.com/track/pdf/10.1186/s12974-020-02060-4)). *A specific USUV NS5–STAT2 degradation mechanism (as shown for Zika) has not been demonstrated and should be curated as a hypothesis, not a fact.*

**Lineages:** multiple genetic lineages circulate (African lineages Africa 1–3 and European lineages Europe 1–5+), which differ in geographic distribution and possibly virulence. **No human host germline variants, somatic mutations, epigenetic marks, or chromosomal abnormalities** are relevant — these sections are not applicable.

---

## 5. Environmental Information

- **Infectious agent:** Usutu virus (NCBITaxon:64286).
- **Vector:** *Culex pipiens* predominantly, plus ≥6 other mosquito species (PMID:37589592). Suggested CHEBI/ENVO: ECTO-style "exposure to mosquito bite."
- **Reservoir/amplifying hosts:** wild birds (Aves, NCBITaxon:8782), especially **Eurasian blackbird (*Turdus merula*)** and owls (e.g., *Strix* spp.), in which USUV causes lethal epizootics.
- **Climatic/ecological drivers:** warm season, mosquito abundance, bird migration, and climate change expanding the transmission window and range; USUV overwinters and has established local European transmission cycles.
- **Lifestyle factors:** outdoor activity during vector season; no diet/smoking/alcohol associations.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Infective mosquito bite** → USUV is inoculated into skin; **leads to** local replication in dermal cells and resident dendritic cells/keratinocytes.
2. Local replication → **leads to** spread to draining lymph nodes.
3. Viral **NS proteins (NS5, and others) antagonise type I IFN induction/signalling** → **results in** blunting of the early innate antiviral response (mechanism inferred from flavivirus biology and in vivo IFN/STAT1 dependence; direct USUV NS5–STAT mechanism not yet demonstrated).
4. Innate-immune evasion → **leads to** **viraemia and systemic dissemination** (liver, spleen, kidney, lung in permissive hosts).
5. Viraemia, in a minority of hosts → **leads to** **neuroinvasion** across the blood–brain barrier (USUV can infect all three BBB cell types ex vivo) and **CNS infection of neurons**.
6. CNS infection → **provokes neuroinflammation** (glial activation, leukocyte infiltration) + direct neuronal injury.
7. Neuroinflammation + neuronal injury → **produces meningoencephalitis** → **manifests as** encephalitis, meningitis, and seizures.

**Branch point:** at step 4, the overwhelming majority of immunocompetent hosts **contain** the infection (asymptomatic/mild febrile illness, green branch); only when innate IFN/STAT1 restriction is overwhelmed or deficient does the chain proceed to step 5 (neuroinvasive branch).

### Supporting detail
- **Molecular pathways:** type I IFN (IFN-α/β) induction and JAK–STAT (STAT1/STAT2) signalling are the decisive host restriction pathway. **Whole-body deletion of type I IFN signalling led to widespread USUV infection and fatality in mice**; **mice lacking functional B, T, and NK cells but with intact myeloid cells were resistant** ([mouse infectious-clone pathogenesis study, PMID:40694555](https://pmc.ncbi.nlm.nih.gov/articles/PMC12282914)). **83% of Vav-Cre/Stat1fl/fl mice succumbed by 9 dpi**, implicating **hematopoietic-cell IFN signalling** as central.
- **Cellular processes:** viral genome replication; suppression of type I IFN production (GO:0032480, modifier DECREASED); neuroinflammation; neuronal infection and injury. Human motor-neuron work found **WNV, but not USUV, productively infected motor neurons unless the antiviral response was inhibited**, after which USUV spread and moved along neurons ([*Sci Rep* 2024](https://doaj.org/article/72346cc4c62d4b7f9634f94acb82a69a)) — underscoring that intracellular innate immunity gates USUV neurotropism.
- **Cell tropism:** cell lines from humans, birds, mosquitoes, and mice are susceptible to varying degrees; BBB endothelial cells, pericytes, and astrocytes all infectable ex vivo.
- **Tissue damage:** liver necrosis and immune infiltration in susceptible mice; CNS inflammatory injury in neuroinvasive disease.

**Suggested GO / CL terms:** GO:0019079 (viral genome replication), GO:0032480 (negative regulation of type I interferon production), GO:0060337 (type I interferon-mediated signaling pathway, as the host defense), GO:0006954 (inflammatory response); CL:0000540 (neuron), CL:0000129 (microglial cell), CL:0000127 (astrocyte), CL:0000115 (endothelial cell), CL:0000451 (dendritic cell).

---

## 7. Anatomical Structures Affected

- **Organ level:** **central nervous system** (brain, meninges) in neuroinvasive disease; **skin** (rash, inoculation site); liver and other viscera in severe/experimental infection. Body systems: **nervous**, integumentary, hepatic/reticuloendothelial.
- **Tissue/cell level:** neurons (CL:0000540); glia — microglia (CL:0000129), astrocytes (CL:0000127); BBB endothelium (CL:0000115); dendritic cells/keratinocytes at inoculation.
- **Subcellular:** flaviviral replication occurs on **ER-derived membranes** (GO:0005783 endoplasmic reticulum; GO:0019029 viral replication complex / replication organelle).
- **UBERON suggestions:** UBERON:0000955 (brain), UBERON:0002360 (meninx), UBERON:0001017 (central nervous system), UBERON:0002097 (skin of body), UBERON:0002107 (liver).
- **Localization/lateralization:** CNS involvement is typically diffuse rather than lateralized.

---

## 8. Temporal Development

- **Onset:** acute, incubation on the order of days after the bite.
- **Course (mild):** self-limited febrile illness over days.
- **Course (neuroinvasive):** acute meningitis/encephalitis/meningoencephalitis; severity variable; some residual neurological signs possible.
- **Seasonality:** cases cluster in **late summer–early autumn**, tracking vector activity; EU reports rose markedly 2017–2021 (n=70), driven largely by a **2018 spike** (PMID:37589592).
- **Critical period for intervention:** early supportive/neurological management of neuroinvasive disease; no antiviral window is established.

---

## 9. Inheritance and Population

**Not a genetic disease** — inheritance, penetrance, expressivity, anticipation, founder effects, consanguinity, and carrier frequency are **not applicable**.

**Epidemiology**
- **EU/EEA 2012–2021:** 8 countries (Austria, Croatia, Czechia, France, Germany, Hungary, Italy, Netherlands) reported **105 autochthonous human infections, 12 with neurological symptoms** (abstract states 11; results state 12 — discrepancy to note). Italy 56, Austria 27, Netherlands 11 (PMID:37589592).
- **Notifiability:** "**Detection of USUV infection in humans is notifiable only in Italy, where it is under surveillance since 2017**" (PMID:37589592) — implying substantial under-ascertainment elsewhere.
- **Seroprevalence:** in some southern-European foci USUV seroprevalence may exceed WNV; seroconversion documented in blood donors since ~2009.
- **Geographic distribution:** sub-Saharan Africa (origin) and expanding across central/southern/western Europe; lineage-specific geographic clustering.
- **Sex ratio / age distribution:** no robust skew established; cases span adults (blood-donor and clinical series are adult-dominated).

---

## 10. Diagnostics

**Core challenge:** serologic **cross-reactivity among flaviviruses** (especially WNV). "**Diagnosing USUV infection in humans is challenging because of the cross-reactivity of antibodies**" (PMID:37589592).

- **Molecular:** **USUV-specific or pan-flavivirus RT-PCR with sequencing**, and virus isolation in cell culture (acute viraemia, CSF in neuroinvasive disease). LOINC: nucleic-acid detection assays (no USUV-specific LOINC widely established).
- **Serology:** IgM/IgG ELISA/IFA, **confirmed by virus neutralization tests (PRNT) run in parallel against WNV** to resolve cross-reactivity.
- **CSF analysis** in neuroinvasive disease: pleocytosis; USUV RNA/antibody in CSF.
- **Blood-donor screening:** NAT screening in affected regions (links disease to transfusion safety).
- **Imaging / EEG:** nonspecific encephalitic changes; used to characterize neuroinvasive disease, not for etiologic diagnosis.
- **Genetic testing / omics:** not applicable for host diagnosis; viral genome sequencing is used for lineage typing and surveillance.
- **Differential diagnosis:** West Nile virus (foremost), tick-borne encephalitis, enteroviral and HSV meningoencephalitis, other arboviral fevers; USUV should be in the differential for unexplained viral encephalitis in endemic areas, especially during WNV season.

---

## 11. Outcome / Prognosis

- **Mild disease:** excellent prognosis, self-limited recovery.
- **Neuroinvasive disease:** more serious; potential for residual neurological deficits; outcomes range from full recovery to persistent sequelae. Robust case-fatality and 5-/10-year survival figures are **not available** given small numbers and no systematic follow-up.
- **Morbidity:** primarily from the neuroinvasive minority.
- **Prognostic factors:** host immune status, extent of CNS involvement, promptness of supportive care. No validated prognostic biomarkers.
- Overall, reviewers conclude USUV is **not yet a major public-health threat** in the EU/EEA but warrants monitoring (PMID:37589592).

---

## 12. Treatment

- **No licensed antiviral or vaccine** for human USUV disease. **Management is supportive.**
- **Supportive care:** antipyretics/analgesia for febrile illness; neurological monitoring, seizure management, and intensive supportive care for neuroinvasive disease. **NCIT:C15747** (Supportive Care); NCIT:C15316/seizure management; NCIT:C15431-style not applicable.
- **Experimental:** interferon-β showed partial protection in susceptible mice (pre-treatment most effective; "**5 out of 6 mice survived following USUV infection, while 4 out of 4 untreated mice succumbed**," PMID:40694555) — **experimental only, not clinical practice**. Nucleoside-analogue inhibition reduced USUV titers in fetal brain slice models (preclinical).
- **No pharmacogenomics, gene/cell/RNA therapy, or targeted/immunotherapy** is applicable.
- **Suggested NCIT:** C15747 (Supportive Care); C15986 (Pharmacotherapy) only if symptomatic agents are curated.

---

## 13. Prevention

- **Primary prevention:** **vector avoidance and control** — repellents, protective clothing, mosquito-source reduction, and bite avoidance during the *Culex* season; no human vaccine exists. Public-health **vector surveillance and bird-mortality surveillance** as early-warning systems.
- **Blood safety:** **NAT screening/deferral of blood donors** in affected regions to prevent transfusion transmission (secondary prevention of iatrogenic spread).
- **Secondary prevention:** inclusion of USUV in the differential for viral encephalitis; early recognition.
- **Public-health/environmental:** integrated mosquito management; One Health surveillance linking avian, equine, entomological, and human data.
- **Not applicable:** immunization, newborn/genetic/carrier screening, genetic counseling, chemoprophylaxis.

---

## 14. Other Species / Natural Disease

- **Taxonomy of host range:** birds (Aves, **NCBITaxon:8782**) are the amplifying/reservoir hosts; **Eurasian blackbird *Turdus merula*** (NCBITaxon:9187) and owls (*Strix nebulosa*, *Strix aluco*) are highly susceptible, with lethal epizootics. Horses (*Equus caballus*, NCBITaxon:9796) and humans (NCBITaxon:9606) are **incidental dead-end hosts**.
- **Natural disease:** the 2001 Vienna outbreak — "**a considerable die-off of Eurasian Blackbirds… observed in and around Vienna, Austria**," with five great gray owls dying at the Vienna Zoo (PMID:12095429). USUV is a significant cause of avian mortality in Europe and a recognized veterinary/wildlife-health problem.
- **Comparative biology:** birds show hepatosplenic and neurological disease with high viral loads; humans/horses are comparatively resistant. This zoonotic/One Health pattern mirrors WNV.
- **Zoonotic potential:** yes — mosquito-borne spillover to humans; no human-to-human spread except transfusion.

---

## 15. Model Organisms

- **Mouse (*Mus musculus*, NCBITaxon:10090):**
  - **Immunocompetent adult mice are generally resistant.**
  - **Type I IFN-receptor knockout (Ifnar1⁻/⁻) and STAT1⁻/⁻ mice** develop **lethal neuroinvasive infection**, with virus reaching liver, spleen, kidney, lung, and brain; lethality ~5–8 dpi; optimal uniform-lethality dose ~**10³ FFU** in Stat1⁻/⁻ mice (PMID:40694555).
  - **Conditional/cell-type-restricted STAT1 deletion** (Vav-Cre = hematopoietic; Syn-Cre = neuronal) localized the critical restriction to **hematopoietic cells** (83% lethality in Vav-Cre/Stat1fl/fl).
  - **Infectious clone (TC508 isolate)** available for reverse genetics.
  - *Strengths:* reproduces neuroinvasion, viraemia kinetics, and IFN-dependence. *Limitations:* requires innate-immune ablation to produce disease; does not model the immunocompetent human neuroinvasive cases.
- **In vitro / cellular models:** human/avian/mosquito/murine cell lines (varying permissiveness — L929 permissive, Hepa1-6 non-permissive); **human iPSC-derived motor neurons** (USUV non-productive unless antiviral response inhibited); **human fetal brain slice cultures** (IFN-β– and nucleoside-analogue–responsive); **ex vivo human BBB models** (all three BBB cell types infectable).
- **Resources:** MGI (mouse), Cellosaurus (cell lines); Alliance of Genome Resources for orthology context (host IFN/STAT genes).
- **Suggested evidence_source tagging for curation:** MODEL_ORGANISM (mouse), IN_VITRO (cell/slice/BBB), HUMAN_CLINICAL (case/surveillance). Per CLAUDE.md, model-organism evidence must not be the sole support for human phenotypes.

---

## Key Citations (for evidence curation)

- Weissenböck H, et al. **Emergence of Usutu virus… central Europe.** *Emerg Infect Dis* 2002;8(7):652-656. **PMID:12095429** — avian emergence, 2001 Vienna die-off, African identity.
- Pecorari M, et al. **First human case of Usutu virus neuroinvasive infection, Italy, August–September 2009.** *Euro Surveill* 2009;14(50):19446. DOI:10.2807/ese.14.50.19446-en — first human neuroinvasive case (DLBCL patient). *(Fetch to confirm PMID before binding.)*
- Angeloni G, et al. **Epidemiology, surveillance and diagnosis of Usutu virus infection in the EU/EEA, 2012 to 2021.** *Euro Surveill* 2023;28(33):2200929. **PMID:37589592** — 105 cases/12 neuroinvasive; notifiable only in Italy; *Culex pipiens* vector; diagnostic cross-reactivity.
- **Mouse infectious-clone pathogenesis study (TC508), 2025.** **PMID:40694555** — IFN/STAT1 restriction, hematopoietic-cell dependence, IFN-β protection.
- Cadar D & Simonin Y. **Human Usutu virus infections in Europe** (review), *Viruses* 2022/2023 — clinical spectrum synthesis.
- *J Neuroinflammation* 2021, s12974-020-02060-4 — NS5 D3425E neurovirulence determinant.
- *Sci Rep* 2024 — differential USUV vs WNV human motor-neuron susceptibility.

**Caveat:** Several figures (105 vs neuroinvasive 11 vs 12; immunocompromised status of neuroinvasive cases) differ between abstract and results text and between the 2009 vs 2012–2021 datasets; curate both with exact-quote snippets and flag the discrepancy. Before binding any evidence item, regenerate the cache with `just fetch-reference <PMID>` and verify the snippet is an exact substring — do **not** hand-write `references_cache/` files or fabricate PMIDs (the Pecorari PMID in particular should be confirmed by fetch, not assumed).

**Sources:**
- [EU/EEA surveillance, Euro Surveill 2023 (PMID 37589592)](https://www.pubmed.gov/37589592/) · [PMC10436690](https://pmc.ncbi.nlm.nih.gov/articles/PMC10436690/)
- [Mouse pathogenesis / infectious clone, PMC12282914 (PMID 40694555)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12282914)
- [Weissenböck et al., EID 2002](https://wwwnc.cdc.gov/eid/article/8/7/02-0094)
- [Pecorari et al., Eurosurveillance 2009](https://www.eurosurveillance.org/content/10.2807/ese.14.50.19446-en)
- [Differential human motor-neuron susceptibility, Sci Rep 2024](https://doaj.org/article/72346cc4c62d4b7f9634f94acb82a69a)
- [NS5 neurovirulence, J Neuroinflammation 2021](https://jneuroinflammation.biomedcentral.com/track/pdf/10.1186/s12974-020-02060-4)
- [Cadar & Simonin, Viruses review](https://doaj.org/article/adbaf69fdb734384ab9a0e1531afc45b)
- [Seroprevalence/blood donors, PMC6908483](https://pmc.ncbi.nlm.nih.gov/articles/PMC6908483) · [PMC7560012](https://pmc.ncbi.nlm.nih.gov/articles/PMC7560012)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 8 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:37589592` *(abstract only)*: "**Diagnosing USUV infection in humans is challenging because of the cross-reactivity of antibodies**"
  - closest text in source: "Detection of USUV infection in humans is notifiable only in Italy, where it is under surveillance since 2017 and now integrated with surveillance in animals in a One Health approach"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 15 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000540` (2 mentions) - the report calls it "neuron", "Tissue/cell level:** neurons"; CL calls it **neuron**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:64286` (3 mentions) - the report calls it "Usutu virus", "Infectious agent:** Usutu virus"; NCBITaxon calls it **Usutu virus**
- `GO:0060337` (1 mention) - the report calls it "type I interferon-mediated signaling pathway, as the host defense"; GO calls it **type I interferon-mediated signaling pathway**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:64286` - called "Usutu virus", "Infectious agent:** Usutu virus"
- `CL:0000540` - called "neuron", "Tissue/cell level:** neurons"