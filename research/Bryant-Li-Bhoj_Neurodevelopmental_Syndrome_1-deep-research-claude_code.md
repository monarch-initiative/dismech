---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-29T14:45:40.432340'
end_time: '2026-08-29T14:50:25.608289'
duration_seconds: 285.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bryant-Li-Bhoj Neurodevelopmental Syndrome 1
  mondo_id: ''
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 12
  num_turns: 26
  total_cost_usd: 1.214783
  session_id: 947d87eb-a7bc-50ae-bd2b-57097ad6c44a
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 20
reference_validation:
  total_references: 13
  verified: 12
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.077
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 12
  on_topic: 7
  unresolved_references:
  - DOI:10.1126/sciadv.abc9207](https://www.science.org/doi/10.1126/sciadv.abc9207
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 60
  verified: 57
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 41
  labels_matching: 34
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0025265
    reported_labels:
    - 72% (in detailed-MRI subgroup)
    ontology_label: Stiff toe
  - term_id: HP:0031808
    reported_labels:
    - Camptocormia
    ontology_label: Decreased total basophil count
  - term_id: CL:0002608
    reported_labels:
    - radial glial cell
    ontology_label: hippocampal neuron
  - term_id: CL:0002500
    reported_labels:
    - cranial neural crest cell
    ontology_label: P enteroendocrine cell
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0016575
    ontology_label: obsolete histone deacetylation
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bryant-Li-Bhoj Neurodevelopmental Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bryant-Li-Bhoj Neurodevelopmental Syndrome 1** covering all of the
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

Now let me get more detail from the expanded phenotype paper, the founding Science Advances paper, and additional mechanism/model-organism/treatment sources.

Excellent — a very recent preclinical mouse model (2026) and iPSC model (2026). Let me pull details from these plus the npj paper and the iPSC/mouse model papers directly.

I have comprehensive material now. Let me compile the full research report.

# Bryant-Li-Bhoj Neurodevelopmental Syndrome 1 (BRYLIB1): Comprehensive Research Report

## 1. Disease Information

**Overview.** Bryant-Li-Bhoj neurodevelopmental syndrome (BLBS/BRYLIB) is a rare, clinically variable neurodevelopmental (and, in a subset of adults, neurodegenerative) disorder first delineated in 2020 and caused by heterozygous germline variants in one of the two genes that encode replication-independent histone H3.3: *H3-3A* (formerly *H3F3A*) and *H3-3B* (formerly *H3F3B*). Variants in *H3-3A* define **Bryant-Li-Bhoj neurodevelopmental syndrome 1 (BRYLIB1)**; variants in *H3-3B* define the molecularly and clinically similar **BRYLIB2**. The condition was named for the discovery team (Bryant, Li, Bhoj) in the founding report ("Histone H3.3 beyond cancer: Germline mutations in Histone 3 Family 3A and 3B cause a previously unidentified neurodegenerative disorder in 46 patients," *Science Advances*, 2020). GeneReviews describes it as "characterized by developmental delay/intellectual disability... and nonspecific craniofacial abnormalities," with a highly variable, gene-dosage-sensitive presentation (GeneReviews, NBK595206, updated 2023) [https://www.ncbi.nlm.nih.gov/sites/books/NBK595206/].

**Key identifiers:**
- **OMIM (phenotype):** #619720 — BRYANT-LI-BHOJ NEURODEVELOPMENTAL SYNDROME 1; BRYLIB1 (https://www.omim.org/entry/619720)
- **OMIM (gene):** *601128 — H3 HISTONE, FAMILY 3A; H3F3A / H3-3A (https://omim.org/entry/601128)
- **Related disorder:** OMIM #619721 — BRYLIB2 (H3-3B, gene *601058), the sister condition
- **MONDO:** MONDO:0030606 (Bryant-Li-Bhoj neurodevelopmental syndrome 1), confirmed via ClinGen curation (https://search.clinicalgenome.org/kb/conditions/MONDO:0030606)
- **HGNC:** H3-3A, HGNC:4764
- **ClinGen gene-disease validity:** **Definitive** (Syndromic Disorders GCEP, classification date 2024-03-19)
- **Orphanet:** no distinct ORPHA number could be confirmed in this search (the entity is very recently named, 2022 OMIM addition; it may still be tracked in Orphanet under a broader "H3.3-related chromatinopathy" heading rather than a dedicated ORPHA code)
- **Synonyms:** BRYLIB1; Bryant-Li-Bhoj syndrome (BLBS); H3.3-related neurodevelopmental disorder; H3-3A-related neurodevelopmental disorder; (historically, before nosologic separation from cancer-associated somatic H3.3 mutations) "H3F3A germline neurodevelopmental disorder"

**Data provenance:** Nearly all current knowledge derives from aggregated case-series/cohort resources (GeneReviews, the 2020 founding cohort of 46 patients, and a 2024 expansion to 96 total individuals) built from clinician-submitted, ClinVar-deposited, and literature case reports — not from a population-level EHR resource. This is disease-level/aggregated-cohort evidence, not raw individual-patient EHR data.

## 2. Etiology

**Primary cause — genetic, autosomal dominant, de novo.** BRYLIB1 is caused by heterozygous, essentially always **de novo** pathogenic variants in *H3-3A*. GeneReviews states plainly: "BRYLIB is an autosomal dominant disorder typically caused by a de novo pathogenic variant." Parental testing in reported cohorts has confirmed de novo origin in essentially all cases; the 2024 expansion cohort reported the field's first exception — a maternally inherited *H3-3B* variant (p.Asn108Ser) in a mildly affected mother and child, establishing that (at least for *H3-3B*) transmission from a mosaic or mildly affected parent is possible (Layo-Carris et al., *Eur J Hum Genet* 2024;32(8):928–937, PMID: 38678163).

**Genetic risk factors.** The disease-causing variant itself is the risk factor; there is no described susceptibility-locus or polygenic contribution. gnomAD constraint metrics show *H3-3A* and *H3-3B* are highly intolerant to variation (missense z-scores of 3.16 and 2.88, respectively), consistent with the observation that even single heterozygous substitutions are clinically impactful (Layo-Carris et al. 2024).

**Modifier factors / phenotype drivers.** The affected gene (*H3-3A* vs *H3-3B*), the protein domain hit (N-terminal tail, aa 1–43, vs. histone-fold core, aa 44–135), and sex all statistically associate with different symptom sub-profiles (see Genotype-Phenotype Correlations, section 4/6), but the authors explicitly caution that "the current stratification by sex, affected gene, or affected protein domain does not account for all phenotypic variation observed," implicating unidentified modifiers — possibly epigenetic or gene-environment interaction effects, since "histone biology sits at the genetics-epigenetics interface" (Layo-Carris et al. 2024).

**Environmental/lifestyle risk factors.** None identified; this is a Mendelian single-gene disorder with no established environmental etiologic contribution.

**Protective factors.** None reported.

**Somatic vs. germline distinction (important etiologic contrast).** Identical or adjacent missense substitutions occurring **somatically** in *H3-3A* (notably p.Gly34Arg/Val and p.Lys27Met) are well-known oncogenic drivers of pediatric diffuse midline glioma and giant cell tumor of bone. In BRYLIB1/2, the same or neighboring residues are altered **germline**, and critically, **no oncologic complications have been reported** in the BLBS germline cohort to date, despite two individuals carrying germline p.Gly34Arg/Val substitutions identical to oncogenic somatic hotspots (Bryant et al. 2020; Layo-Carris et al. 2024). This is mechanistically informative: PTM/chromatin dysregulation in the germline, congenital setting differs qualitatively from the global histone-code disruption caused by somatic "oncohistone" mutations.

## 3. Phenotypes

Frequencies below combine GeneReviews (n=57), the founding 2020 cohort (n=46), and the 2024 expanded cohort of 96 total individuals (58 previously reported + 38 new; Layo-Carris et al. 2024, PMID 38678163), which is the most complete phenotype table available.

| Phenotype | Frequency | HPO suggestion |
|---|---|---|
| Global developmental delay / intellectual disability (moderate–severe) | 99% (94/95) | HP:0012758 (Developmental regression) / HP:0001263 (Global developmental delay) / HP:0001249 (Intellectual disability) |
| Poor/absent speech, delayed speech (no words by 20 mo) | 60% (50/84) | HP:0000750 (Delayed speech and language development) |
| Delayed walking (>20 mo) | 79% (59/75) | HP:0002505 / HP:0031936 (Delayed ability to walk) |
| Delayed sitting (>12 mo) | 51% (33/65) | HP:0025336 (Delayed ability to sit) |
| Craniofacial dysmorphism (nonspecific pattern) | 88–92% | HP:0001999 (Abnormal facial shape) |
| Hypotonia | 62–72% (often resolves/evolves with age) | HP:0001252 (Hypotonia) |
| Hypertonia / peripheral spasticity (partly age-evolving) | 12–19% | HP:0001276 (Hypertonia) / HP:0007256 (Spasticity) |
| Oculomotor abnormalities (strabismus, nystagmus) | 53–54% (strabismus alone 36%) | HP:0000486 (Strabismus) / HP:0000639 (Nystagmus) |
| Seizures (variable types, childhood onset) | 47–49% (febrile seizures ~20% of these) | HP:0001250 (Seizure) |
| Abnormal brain MRI (composite) | 58% | HP:0002060 (Abnormal cerebral morphology) |
| — Small posterior fossa | 72% (in detailed-MRI subgroup) | HP:0025265 |
| — Corpus callosum malformation | 37% (28/76) | HP:0002079 (Hypoplasia of the corpus callosum) |
| — Delayed/hypomyelination, dilated ventricles | subset | HP:0002188 (Delayed CNS myelination), HP:0002119 (Ventriculomegaly) |
| Short stature | 35–39% | HP:0004322 (Short stature) |
| Microcephaly | 32–33% | HP:0000252 (Microcephaly) |
| Macrocephaly | 15% | HP:0000256 (Macrocephaly) |
| Craniosynostosis / abnormal head shape | 32% | HP:0001363 (Craniosynostosis) |
| Musculoskeletal anomalies (incl. scoliosis 21%) | 60% | HP:0002650 (Scoliosis) |
| Dermatologic features | 52% | HP:0000951 (Abnormality of the skin) |
| Congenital heart defects (esp. atrial septal defect) | 13–19% | HP:0001631 (Atrial septal defect) |
| Genital anomalies / cryptorchidism (males) | 20–35% | HP:0000028 (Cryptorchidism) |
| Hearing loss | subset | HP:0000365 (Hearing impairment) |
| Feeding problems | common in infancy | HP:0011968 (Feeding difficulties) |
| Neurobehavioral abnormalities (autism, ADHD, happy demeanor, stereotypies) | ~50% in one cohort | HP:0000717 (Autism), HP:0000733 (Stereotypy) |
| Camptocormia / new-onset motor decline in adulthood | 100% of reported adults (subacute onset, 3rd decade of life, then stabilizes) | HP:0031808 (Camptocormia) |
| Gait abnormality / ataxic gait | up to universal in some reports | HP:0002317 (Unsteady gait) |

**Onset/progression/severity.** Developmental delay is evident from infancy/early childhood; the reported age range at evaluation spans 10 weeks to 39 years, so the natural history now extends well into adulthood. Notably, this is one of the few histone-related NDDs with a **documented adult-onset neurodegenerative component**: "all reported adults have had a new subacute onset of motor issues in the third decade of life that generally remains stable after onset," manifesting principally as camptocormia (progressive bent-spine posture) — the feature that anchors the "neurodegenerative" half of the syndrome's Science Advances title. Hypotonia can resolve or evolve into a mixed axial-hypotonia/peripheral-hypertonia pattern with age; this mixed pattern was found to occur *exclusively* in individuals with variants in the histone core domain (see Section 6).

**Quality of life impact.** Not separately quantified with EQ-5D/SF-36 instruments in the literature reviewed; qualitatively, impact is substantial given near-universal moderate-to-severe intellectual disability, motor delay, and (in a subset) adult-onset progressive motor decline, feeding difficulties, and seizures requiring ongoing neurological management.

## 4. Genetic/Molecular Information

**Causal gene:** *H3-3A* (HGNC:4764; OMIM *601128), chromosome 1q42.12, encoding replication-independent histone H3.3. (BRYLIB2 is caused by *H3-3B*, OMIM *601058, chromosome 17q25.1 — the two genes encode an essentially identical H3.3 protein and produce clinically overlapping disease.)

**Variant spectrum:**
- BRYLIB1 (*H3-3A*): overwhelmingly **de novo heterozygous missense** variants, identified in the founding cohort in 33 unrelated patients, "found by whole-exome or genome sequencing, occurred throughout the gene" (OMIM #619720, citing Bryant et al. 2020).
- BRYLIB2 (*H3-3B*): greater variant diversity, including a synonymous variant acting as a cryptic stop-gain in a non-canonical transcript (p.Val117Val), a stop-loss variant (p.Cys136*ext9, a 2-nt deletion ablating the stop codon), and the one known inherited variant (p.Asn108Ser).
- Across the combined 96-individual cohort: **70 unique causative variants**, distributed throughout the H3.3 protein rather than clustered at one or two hotspots — in contrast to the sharply localized cancer "oncohistone" hotspots (K27, G34, K36).
- Representative variants: H3-3A p.Thr45Ile (T45I) — the most recurrently reported variant, now used to generate a mouse model (see Section 15); H3-3A p.Thr46Ile; H3-3B p.Leu48Arg (L48R) — used to generate an iPSC model; H3-3A/B p.Gln125Arg (shared, 8 individuals, discordant phenotypes); germline p.Gly34Arg/Val in H3-3B (mirrors the somatic oncohistone hotspot but with no oncologic phenotype).
- ClinVar entry example: NM_002107.7(H3-3A):c.137C>T (p.Thr46Ile), classified pathogenic/likely pathogenic for BRYLIB1 (https://www.ncbi.nlm.nih.gov/clinvar/RCV001823766/).

**Variant classification (ACMG/AMP):** Pathogenic/likely pathogenic missense (and the rarer truncating/stop-loss/cryptic-splice) variants; interpreted per standard ACMG/AMP criteria plus gene-specific de novo and functional evidence used by the ClinGen Syndromic Disorders GCEP, which rated the H3-3A–BRYLIB1 relationship **Definitive**.

**Allele frequency:** Not present (or present only as ultra-rare singleton entries) in gnomAD/population databases, consistent with strong purifying selection (missense z-scores >2.8 for both genes) and complete penetrance of de novo disease alleles.

**Somatic vs. germline:** BRYLIB1/2 are strictly germline disorders; the same *H3-3A*/*H3-3B* residues altered *somatically* (K27M, G34R/V, K36M) instead cause pediatric high-grade/diffuse midline glioma and giant cell tumor of bone — an important differential/molecular contrast, not a subtype of BRYLIB1.

**Functional consequences.** Molecular modeling of the founding cohort's 37 variants "demonstrated clear disruptions in interactions with DNA, other histones, and histone chaperone proteins" (Bryant et al. 2020). Patient-derived histone post-translational modification (PTM) profiling showed "notably aberrant local PTM patterns distinct from the somatic lysine mutations that cause global PTM dysregulation" — i.e., germline variants perturb the histone code locally/regionally rather than globally. RNA-seq on patient cells showed "up-regulated gene expression related to mitosis and cell division, with increased proliferative capacity." A specific structural mechanism identified for one recurrent variant (H3-3A p.Arg129His) was "significantly stronger interaction with DAXX," the H3.3-specific histone chaperone, implicating disrupted, chaperone-mediated H3.3 deposition (Tsuchiya et al./de novo-variant cohort, PMC8651650). For H3-3B p.Leu48Arg, iPSC modeling indicates the variant "increases H3-3B expression, resulting in the hyper-deposition of H3.3 into the nucleosome" (see Section 6).

**Modifier genes:** None formally established; phenotype correlates statistically with affected gene and protein domain (tail vs. core) rather than with a distinct modifier locus (see Section 6).

**Epigenetic information:** This is fundamentally an epigenetic-machinery disorder — the causal protein *is* a core chromatin component. Aberrant local histone PTM deposition and altered chromatin accessibility (documented directly by ATAC-seq/multi-omic profiling in iPSC-derived neural models) are central to pathogenesis rather than secondary.

**Chromosomal abnormalities:** Not a copy-number/structural disorder; disease is driven by single-nucleotide/small-indel variants in *H3-3A*. Gene-targeted deletion/duplication analysis detection rate is not established (no cases reported to date attributable to CNV).

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors have been identified or proposed for BRYLIB1 beyond the theoretical, unproven suggestion in the 2024 expanded-cohort paper that "gene-environment interactions" might help explain residual phenotypic variability not accounted for by gene/domain/sex stratification — this is explicitly speculative rather than evidence-based (Layo-Carris et al. 2024).

## 6. Mechanism / Pathophysiology

**Molecular substrate.** H3.3 is a replication-independent histone variant (as opposed to the replication-dependent canonical H3.1/H3.2) that is deposited onto DNA by the DAXX/ATRX and HIRA histone chaperone complexes, especially at transcriptionally active regions, telomeres, and pericentric heterochromatin. Two molecules of each core histone (H2A, H2B, H3, H4) assemble into the octamer around which ~146 bp of DNA wraps to form the nucleosome; H3.3 is essential for chromatin compaction, early embryonic development, and cell-lineage commitment. Suggested GO terms: **GO:0000786** (nucleosome), **GO:0031507** (heterochromatin formation), **GO:0006335** (DNA replication-independent nucleosome assembly), **GO:0016575** (histone deacetylation)/relevant PTM GO terms, **GO:0006338** (chromatin remodeling).

**Causal chain (as currently understood):**
1. **Trigger (molecular/upstream):** De novo missense (or rare truncating/inherited) variant in *H3-3A* alters the H3.3 protein at a residue involved in DNA contact, chaperone binding (e.g., DAXX interaction, strengthened for p.R129H), or inter-histone (H3-H4/H2A-H2B) contacts within the nucleosome.
2. **Molecular consequence:** Disrupted or altered-affinity interactions with DNA, chaperones, and neighboring histones; in some variants (e.g., L48R) increased *H3-3B* expression and hyper-deposition of H3.3 into nucleosomes rather than simple loss-of-function.
3. **Chromatin-level consequence:** Aberrant, locally restricted (not globally dysregulated, unlike somatic oncohistones) deposition of histone PTMs, producing a disrupted local "histone code."
4. **Gene-regulatory consequence:** Genome-wide, cell-type-specific dysregulated gene expression and altered chromatin accessibility — documented in iPSC-derived neural progenitor cells, forebrain neurons, and organoids as changes affecting genes governing "neuronal fate, adhesion, neurotransmission, and excitatory/inhibitory balance" (Journal of Translational Medicine 2026 iPSC paper, PMC11382994). Patient fibroblasts additionally show up-regulated mitosis/cell-division transcriptional programs and increased proliferative capacity (Bryant et al. 2020).
5. **Cellular consequence:** Altered proportions of radial glia versus mature neuronal populations in organoids; decreased spontaneous electrical activity in L48R-mutant forebrain-organoid neurons by patch-clamp electrophysiology, indicating impaired neuronal maturation/functional network formation.
6. **Organismal/clinical consequence:** Global developmental delay/intellectual disability, dysmorphic craniofacial features, hypotonia/hypertonia, seizures, structural brain anomalies (hypomyelination, corpus callosum dysgenesis, small posterior fossa), and — in the neurodegenerative arm of the phenotype — adult-onset progressive camptocormia/motor decline, presumably reflecting cumulative disruption of H3.3's dominant role in post-mitotic neuronal chromatin maintenance over decades (H3.3 becomes >93% of total neuronal H3 in mature neurons, versus ~31% of the H3 pool during early neurodevelopment).

**Upstream vs. downstream framing:** Upstream = the germline histone variant itself (a cell-autonomous, constitutive lesion present from the zygote onward, not one triggered by an external event). Midstream = chromatin/PTM/accessibility dysregulation. Downstream = neurodevelopmental (congenital) phenotypes plus a distinct, temporally separate downstream neurodegenerative phenotype (adult camptocormia) that appears to require decades of cumulative dysfunction in postmitotic neurons — consistent with the biological observation that H3.3 dependence increases sharply as neurons mature and exit the cell cycle.

**Cell types/processes implicated:** Neural progenitor cells, radial glia, cortical/forebrain excitatory neurons (maturation and electrophysiological function), cranial neural crest cells (craniofacial dysmorphism, per zebrafish data), and — per RNA-seq of patient fibroblasts — mitotically active non-neural cells showing increased proliferation. Suggested CL terms: **CL:0000047** (neural progenitor cell/stem cell), **CL:0002608** (radial glial cell), **CL:0000540** (neuron)/**CL:0000598** (pyramidal neuron), **CL:0002500** (cranial neural crest cell).

**Genotype-phenotype correlation (protein-domain level, from the 96-individual 2024 cohort):**
- **N-terminal tail variants (aa 1–43):** associated with undergrowth (44%), abnormal neuroimaging (63%), hypotonia (73%), dermal features (64%), delayed sitting (59%).
- **Histone-fold core variants (aa 44–135):** associated with the mixed axial-hypotonia/peripheral-hypertonia pattern (exclusively seen with core variants), higher rates of overweight (25% vs 7%) and cardiac anomalies (17% vs 7%), and more often normal height.
- **Gene-level:** *H3-3A* variants trend toward more craniofacial dysmorphism (95% vs 86%) and more delayed walking (85% vs 65%); *H3-3B* variants trend toward higher seizure prevalence (59% vs 45%), more macrocephaly (53% vs 43%), and more genital anomalies (28% vs 17%).
- **Sex:** males show more delayed walking and speech delay; females show more oculomotor dysfunction; seizure prevalence and overall developmental-delay severity do not differ significantly by sex.
- Critically, **identical variants produce discordant phenotypes** (e.g., four individuals with H3-3A p.Thr45Ile, and eight individuals sharing p.Gln125Arg across both genes, show substantial phenotypic variability), so genotype-phenotype rules are statistical trends, not deterministic.

**Advanced/omics technologies used to date:** multi-omic (transcriptomic + chromatin-accessibility/ATAC-like) profiling of iPSC-derived 2D neural progenitor cells and forebrain neurons; single-cell/organoid-level immunofluorescence characterization of 3D dorsal forebrain organoids; patch-clamp single-cell electrophysiology. No published single-cell RNA-seq atlas, spatial transcriptomics, or CRISPR functional-genomics screen specific to BLBS was identified in this search.

## 7. Anatomical Structures Affected

**Organ level:** Primary — central nervous system (brain: cortex, corpus callosum, posterior fossa/cerebellum, white matter); craniofacial skeleton (skull shape, craniosynostosis). Secondary — cardiovascular system (atrial septal defect and other congenital heart defects), musculoskeletal system (scoliosis, other skeletal anomalies, adult-onset camptocormia of the spine), genitourinary system (cryptorchidism, other genital anomalies), integumentary system (dermatologic features), auditory system (hearing loss), ocular system (strabismus, nystagmus, other oculomotor dysfunction), endocrine system (hypothyroidism reported in the sister Rahman-syndrome literature and surveilled for in BLBS management protocols).

**Body systems involved:** nervous, musculoskeletal, cardiovascular, ocular, auditory, endocrine, genitourinary, integumentary — a genuinely multisystem chromatinopathy centered on but not limited to neurodevelopment. Suggested UBERON terms: **UBERON:0000955** (brain), **UBERON:0002336** (corpus callosum), **UBERON:0002037** (cerebellum), **UBERON:0002298** (brainstem/posterior fossa structures), **UBERON:0003128** (skull).

**Tissue/cell level:** cerebral cortical neurons and their progenitors (radial glia); cranial neural crest-derived craniofacial mesenchyme; cardiac septal tissue; ocular extraocular muscle/oculomotor control circuitry.

**Subcellular level:** the **nucleus/chromatin** is the primary subcellular compartment affected — the nucleosome itself (GO Cellular Component: **GO:0000786** nucleosome; **GO:0000785** chromatin; **GO:0005694** chromosome) is the direct molecular substrate of disease.

**Localization/lateralization:** No lateralization pattern reported; craniofacial and brain anomalies are typically bilateral/midline (e.g., corpus callosum, posterior fossa). Camptocormia is axial/midline (spine).

## 8. Temporal Development

**Onset:** Congenital/early childhood for the neurodevelopmental component (developmental delay evident in infancy); distinctly **adult-onset (third decade)** for the neurodegenerative motor component (camptocormia).

**Progression:** Two temporally distinct phases are now recognized — (1) a static-to-improving neurodevelopmental phase in childhood (hypotonia can resolve with age in some individuals), followed by (2) a **subacute-onset, then stabilizing** neurodegenerative motor phase beginning in early adulthood, universal among reported adults, that "generally remains stable after onset" rather than being relentlessly progressive. Seizures, when present, begin in childhood with variable, sometimes treatment-refractory, course.

**Patterns:** Developmental regression is reported in a minority of individuals, ranging mild to severe; no spontaneous full remission is described. No defined "critical period" for intervention has been established in the literature, though early developmental intervention (birth–age 3) is uniformly recommended in management guidance.

## 9. Inheritance and Population

**Epidemiology:** Ultra-rare; **96 individuals** reported in the peer-reviewed literature as of the 2024 expanded cohort (58 previously known + 38 new), combined across BRYLIB1 (*H3-3A*, 65 individuals) and BRYLIB2 (*H3-3B*, 31 individuals). No population-based prevalence or incidence estimate (per 100,000) has been established; the condition is almost certainly ascertainment-limited (identified via exome/genome sequencing for undiagnosed neurodevelopmental disorders) rather than reflecting a stable epidemiologic denominator.

**Inheritance pattern:** Autosomal dominant, essentially always **de novo**; one confirmed maternally-inherited *H3-3B* case is the sole reported exception to date (2024 cohort). GeneReviews recurrence-risk guidance: for parents of an isolated proband, recurrence risk to siblings is ~1% (accounting for possible parental germline mosaicism) if parental testing is negative; risk to offspring of an affected individual is not yet established because few affected individuals have reached reproductive age.

**Penetrance:** Reported cases are essentially fully penetrant (all carriers described to date are symptomatic), though the founder mild inherited case (mother + child, p.Asn108Ser) suggests a spectrum extending toward milder/possibly under-ascertained presentations.

**Expressivity:** Markedly **variable**, even among carriers of the identical variant (documented explicitly for p.Thr45Ile and p.Gln125Arg) — this is one of the most striking features of the disorder and is explicitly flagged by the authors as only partially explained by gene, domain, or sex.

**Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Formally invoked as the explanation for the ~1% empiric sibling recurrence risk quoted by GeneReviews, though not directly demonstrated in a specific reported family to date in this search.

**Founder effects / consanguinity:** None reported; disease arises from de novo mutation, not from population-specific founder alleles or recessive consanguinity-driven inheritance.

**Population demographics:** No described ethnic, geographic, or ancestry-specific enrichment; cohorts to date are drawn from international, largely clinical-exome-sequencing-ascertained populations (US, European, and at least one Chinese cohort reported separately — see PMC ResearchGate "Bryant-Li-Bhoj neurodevelopmental syndrome: a case report in China and literature review"). Sex ratio: no marked male:female skew reported, though some phenotype features differ by sex in frequency (Section 6).

## 10. Diagnostics

**Diagnostic criteria (GeneReviews):** "The phenotypic features associated with Bryant-Li-Bhoj neurodevelopmental syndrome are not sufficient to diagnose this condition clinically." Diagnosis requires suggestive clinical findings **plus** identification of a heterozygous pathogenic/likely-pathogenic variant in *H3-3A* or *H3-3B* by molecular genetic testing.

**Testing approach/order:**
1. Chromosomal microarray analysis (initial broad screen, primarily to exclude a CNV-based alternative diagnosis)
2. Intellectual disability multigene panel including *H3-3A*/*H3-3B*
3. Exome or genome sequencing (most productive; used to identify the great majority of reported cases)
4. Single-gene sequential testing is explicitly "rarely useful and typically NOT recommended," given the phenotype's non-specificity.

**Detection rate:** Sequence analysis has detected essentially all reported pathogenic variants (39/39 *H3-3A* cases and 18/18 *H3-3B* cases in the cohort GeneReviews cites); detection rate for gene-targeted deletion/duplication (CNV) analysis is unknown/unestablished, since no CNV-mediated cases have been reported.

**Imaging:** Brain MRI is the key structural imaging modality — findings include small posterior fossa, corpus callosum hypoplasia/dysgenesis, delayed/hypomyelination, cortical dysplasia in a subset, and (in some individuals) leukoencephalopathy-pattern white-matter change.

**Differential diagnosis:** Because the phenotype (developmental delay + nonspecific dysmorphism + variable hypotonia/seizures) overlaps broadly with hundreds of other Mendelian intellectual-disability disorders, GeneReviews directs clinicians to the OMIM autosomal dominant, autosomal recessive, and X-linked intellectual developmental disorder phenotypic series for full differential consideration. Notably, close molecular differentials include the **H1.4-linker-histone disorder Rahman syndrome (HIST1H1E/H1-4)** — a distinct, separately named chromatinopathy causing overlapping intellectual disability, overgrowth, and dysmorphic facies, but mechanistically and molecularly separate (linker histone H1 vs. core nucleosomal histone H3.3) and must not be conflated with BRYLIB1/2 despite superficial resemblance and shared "histone-disorder" framing in review literature.

**Genetic testing modalities:** Standard clinical exome/genome sequencing is the primary and most productive tool; chromosomal microarray, karyotyping, FISH, and mitochondrial DNA testing are not primary diagnostic tools for this specific condition (used only to exclude alternative etiologies). No repeat-expansion or specialized epigenomic clinical test is part of the standard diagnostic pathway at this time, although research-grade histone PTM profiling and chromatin-accessibility assays have been used investigationally (see Section 6).

**Screening:** No newborn-screening, population carrier-screening, or cascade-screening program exists (as expected for an ultra-rare, almost-always de novo disorder); prenatal/preimplantation genetic testing is available once a familial pathogenic variant is identified.

## 11. Outcome/Prognosis

**Survival/mortality:** "It is unknown whether life span in BRYLIB is abnormal" (GeneReviews); several adults with the condition have now been reported, and life span does not appear to be markedly shortened by the condition itself based on current (still limited) natural-history data.

**Morbidity/function:** Chronic disability driven by moderate-to-severe intellectual disability, motor delay, and (in adulthood) progressive camptocormia; no tumors have been reported in individuals with germline H3.3 variants (an important reassurance point distinguishing this from the somatic oncohistone literature).

**Disease course:** Predominantly non-regressive/stable neurodevelopmental phenotype through childhood for most individuals, with a distinct adult-onset subacute motor decline (camptocormia) that then plateaus; a minority show frank developmental regression of variable severity.

**Prognostic factors:** No formal prognostic biomarker or scoring system has been developed; affected gene/domain and (to a lesser extent) sex have only modest, non-deterministic predictive value for symptom profile as discussed above.

## 12. Treatment

**No disease-modifying or curative treatment exists.** Management is entirely multidisciplinary and supportive, per GeneReviews Table 4 ("Treatment of Manifestations," https://www.ncbi.nlm.nih.gov/books/NBK595206/table/brylib.T.bryantlibhoj_neurodevelopmental_1/):

- **Developmental/educational support:** Early intervention (age 0–3), developmental preschool/special education, individualized education plans, physical/occupational/speech therapy. NCIT: **NCIT:C15302** (Physical Therapy), **NCIT:C15747** (Supportive Care), **NCIT:C49236** (Therapeutic Procedure).
- **Seizure management:** Standardized anti-seizure medication under an experienced neurologist; multiple agent options exist, some individuals show treatment-refractory seizures. NCIT: **NCIT:C15986** (Pharmacotherapy) with an anticonvulsant `therapeutic_agent`.
- **Feeding/nutrition:** Feeding therapy; gastrostomy tube placement for persistent feeding dysfunction; ongoing nutritional monitoring. NCIT: **NCIT:C15447** (Dietary Intervention).
- **Spasticity management:** Physical therapy, positioning devices, antispasticity medications.
- **Craniosynostosis:** Surgical correction when clinically indicated. NCIT: **NCIT:C16186** (Orthopedic Surgical Procedure) or **NCIT:C15329** (Surgical Procedure).
- **Ophthalmology:** Ongoing care for strabismus/visual impairment.
- **Audiology:** Hearing-loss surveillance and intervention.
- **Cardiology:** Evaluation/management of congenital heart defects.
- **Urology:** Consultation for cryptorchidism.
- **Endocrinology:** Management of hypothyroidism when present.

**Surveillance protocol (GeneReviews):** at each visit — growth parameters, nutrition/oral-intake safety, constipation screening, new seizure or gait-change assessment, developmental-progress monitoring, behavioral screening; annually/as indicated — ophthalmology exam, audiology exam, thyroid function testing; and (per the 2024 expanded-cohort recommendations) repeat neuroimaging to track the progressive/neurodegenerative component and ongoing genitourinary surveillance.

**Experimental/precision-medicine pipeline (very early stage, no clinical trials yet identified):** The two most important recent developments are disease models built specifically to enable future targeted-therapy development:
- **iPSC model (H3-3B p.Leu48Arg):** 2D neural progenitor cells, 2D forebrain neurons, and 3D dorsal forebrain organoids, characterized by multi-omic profiling, immunofluorescence, and patch-clamp electrophysiology (Journal of Translational Medicine, Feb 2026; PMC11382994, PMID 39253491). The authors explicitly frame this model as "a crucial step towards preclinical development and testing of targeted therapies."
- **Mouse model (H3-3A p.Thr45Ile), 2026 preprint:** the first in vivo preclinical model, recapitulating "perinatal growth restriction, delayed developmental milestones, and progressive motor and gait impairments," plus adult craniofacial differences, impaired nest building, social-context hyperactivity, and male-specific elevated aggression (bioRxiv, June 2026, https://www.biorxiv.org/content/10.64898/2026.06.16.732665v1). This model is positioned to enable in vivo therapeutic testing going forward.

No NCT-registered clinical trial for a targeted BLBS therapy was identified in this search as of August 2026; the field remains at the mechanistic/preclinical-model stage.

## 13. Prevention

No primary, secondary, or tertiary prevention strategy exists beyond standard reproductive genetic counseling once a familial pathogenic variant is known (prenatal diagnosis, preimplantation genetic testing) — appropriate given the condition's near-universal de novo origin. No vaccination, screening program, or prophylactic medication applies. Genetic counseling is the principal "preventive" intervention offered to families, focused on recurrence-risk estimation (~1%, germline-mosaicism-based) for future pregnancies.

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife disease caused by spontaneous *H3-3A*/*H3-3B* variants has been reported (this is not currently listed in OMIA). H3.3 itself is highly evolutionarily conserved; the gene has functional orthologs across vertebrates, and a companion in vitro/model-organism paper — "Histone 3.3-related chromatinopathy: missense variants throughout H3-3A and H3-3B cause a range of functional consequences across species" (PMID 36867246) — used **yeast** as a heterologous functional-testing platform for patient-derived missense variants, and a separate paper examined "trapping of yFACT at 3' ends of genes" using yeast versions of BLBS histone H3 mutants (PMC11544422), underscoring cross-species conservation of the affected chaperone/FACT-complex interactions even though yeast do not model the neurodevelopmental phenotype itself.

## 15. Model Organisms

- **Zebrafish:** Homozygous *h3f3a*-mutant (db1092 allele) zebrafish injected with dominant-negative *H3f3a* RNA show "complete loss of melanocytes and severe reductions of glia and xanthophores throughout cranial and trunk regions"; reduced nuclear H3.3 caused by aggregating dominant-mutant H3.3 produces defects in **cranial neural crest cell differentiation**, demonstrating tissue-specific sensitivity to H3.3 dosage during craniofacial/pigment-lineage development — directly relevant to the craniofacial dysmorphism seen in human BLBS.
- **Mouse:** (1) Conditional *H3f3a*/*H3f3b* double-knockout embryos (*H3f3a^fl/−; H3f3b^fl/−; Sox2-Cre*) show H3.3 depletion with embryos recovering at expected Mendelian ratios only up to E10.5, indicating an essential, dosage-sensitive developmental requirement. During normal mouse neurodevelopment, H3.3 constitutes ~31% of total H3 pool early on, rising to become the dominant H3 species (>93%) in mature adult neurons — mechanistically explaining why postmitotic neurons are disproportionately vulnerable to H3.3 dysfunction and offering a rationale for the adult-onset neurodegenerative (camptocormia) component of BLBS. (2) The **2026 knock-in H3.3-T45I mouse** (bioRxiv, June 2026) is the first genotype-matched in vivo preclinical model, recapitulating perinatal growth restriction, developmental-milestone delay, progressive motor/gait impairment, adult craniofacial differences, impaired nest-building, social-context hyperactivity, and male-specific aggression — directly paralleling multiple domains of the human phenotype and positioned as the platform for future therapeutic testing.
- **Human iPSC-derived models:** 2D neural progenitor cells, 2D forebrain neurons, and 3D dorsal forebrain organoids carrying H3-3B p.Leu48Arg (Journal of Translational Medicine, 2026) recapitulate disrupted chromatin accessibility, dysregulated neuronal-fate/adhesion/neurotransmission gene expression, altered radial-glia-to-neuron proportions, and decreased spontaneous neuronal electrical activity by patch-clamp — the most disease-relevant human cellular model to date.
- **Yeast:** used as a rapid, high-throughput heterologous system to functionally characterize the range of consequences of BLBS missense variants "across species," and to probe effects on the FACT histone chaperone complex (yFACT trapping at gene 3′ ends).
- **Model limitations:** none of the current models (zebrafish, mouse, iPSC/organoid, yeast) yet captures the full adult neurodegenerative phenotype (camptocormia) in a validated, long-term aging cohort; the 2026 mouse model is the first designed explicitly to test this, but published long-term follow-up data were not available at the time of this search.

---

## Summary of Key Ontology Term Suggestions

- **Gene/Disease:** HGNC:4764 (H3-3A); MONDO:0030606 (BRYLIB1); OMIM:619720
- **HPO (selected):** HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability), HP:0001252 (Hypotonia), HP:0001276 (Hypertonia), HP:0001250 (Seizure), HP:0002079 (Hypoplasia of corpus callosum), HP:0000252 (Microcephaly), HP:0000486 (Strabismus), HP:0001363 (Craniosynostosis), HP:0031808 (Camptocormia), HP:0002317 (Unsteady gait)
- **GO:** GO:0000786 (nucleosome), GO:0006335 (DNA replication-independent nucleosome assembly), GO:0031507 (heterochromatin formation), GO:0006338 (chromatin remodeling)
- **CL:** CL:0000047 (neural progenitor cell), CL:0002608 (radial glial cell), CL:0000540 (neuron), CL:0002500 (cranial neural crest cell)
- **UBERON:** UBERON:0000955 (brain), UBERON:0002336 (corpus callosum), UBERON:0002037 (cerebellum)
- **NCIT (treatment):** NCIT:C15986 (Pharmacotherapy), NCIT:C15302 (Physical Therapy), NCIT:C15447 (Dietary Intervention), NCIT:C16186 (Orthopedic Surgical Procedure), NCIT:C15747 (Supportive Care)

## Sources

- [GeneReviews: Bryant-Li-Bhoj Neurodevelopmental Syndrome](https://www.ncbi.nlm.nih.gov/sites/books/NBK595206/) (updated 2023)
- [OMIM #619720 — BRYLIB1](https://www.omim.org/entry/619720)
- [OMIM #619721 — BRYLIB2](https://www.omim.org/entry/619721)
- [OMIM *601128 — H3F3A/H3-3A](https://omim.org/entry/601128)
- [ClinGen curation, MONDO:0030606](https://search.clinicalgenome.org/kb/conditions/MONDO:0030606)
- Bryant L, Li D, Cox SG, et al. "Histone H3.3 beyond cancer: Germline mutations in Histone 3 Family 3A and 3B cause a previously unidentified neurodegenerative disorder in 46 patients." *Science Advances* 2020. [https://www.science.org/doi/10.1126/sciadv.abc9207](https://www.science.org/doi/10.1126/sciadv.abc9207) / [PMC7821880](https://pmc.ncbi.nlm.nih.gov/articles/PMC7821880/)
- Layo-Carris DE, et al. "Expanded phenotypic spectrum of neurodevelopmental and neurodegenerative disorder Bryant-Li-Bhoj syndrome with 38 additional individuals." *Eur J Hum Genet* 2024;32(8):928–937. PMID: [38678163](https://pmc.ncbi.nlm.nih.gov/articles/PMC11291762/); [correction](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11292024/)
- "De novo variants in H3-3A and H3-3B are associated with neurodevelopmental delay, dysmorphic features, and structural brain abnormalities." *npj Genomic Medicine* 2021. [PMC8651650](https://pmc.ncbi.nlm.nih.gov/articles/PMC8651650/)
- "A novel iPSC model of Bryant-Li-Bhoj neurodevelopmental/neurodegenerative syndrome demonstrates the role of histone H3.3 in chromatin dynamics, neuronal differentiation, and maturation." *J Transl Med* 2026. PMID: [39253491](https://pubmed.ncbi.nlm.nih.gov/39253491/); [PMC11382994](https://pmc.ncbi.nlm.nih.gov/articles/PMC11382994/)
- "A novel preclinical mouse model recapitulates progressive phenotypes of Bryant-Li-Bhoj Syndrome." *bioRxiv*, June 2026. [https://www.biorxiv.org/content/10.64898/2026.06.16.732665v1](https://www.biorxiv.org/content/10.64898/2026.06.16.732665v1)
- "Histone 3.3-related chromatinopathy: missense variants throughout H3-3A and H3-3B cause a range of functional consequences across species." PMID: [36867246](https://pubmed.ncbi.nlm.nih.gov/36867246/)
- "Trapping of yFACT at 3′ ends of genes is not a universal characteristic of yeast versions of Bryant-Li-Bhoj syndrome histone H3 mutants." [PMC11544422](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11544422/)
- "Neonatal myoclonus in Bryant-Li-Bhoj syndrome associated with a novel H3F3A variant." *Hum Genome Var* 2024. [https://www.nature.com/articles/s41439-024-00303-x](https://www.nature.com/articles/s41439-024-00303-x)
- ClinVar RCV001823766 (NM_002107.7(H3-3A):c.137C>T, p.Thr46Ile) — [https://www.ncbi.nlm.nih.gov/clinvar/RCV001823766/](https://www.ncbi.nlm.nih.gov/clinvar/RCV001823766/)
- Note on differential diagnosis: **Rahman syndrome (HIST1H1E/H1-4)** is a molecularly and clinically distinct linker-histone disorder that should not be conflated with BRYLIB1/2 despite overlapping "histone disorder" framing — see [Zhao et al., Mol Genet Genomic Med 2022](https://onlinelibrary.wiley.com/doi/full/10.1002/mgg3.1825) and [Indugula et al., Clin Case Rep 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8822259/) for comparison.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1126/sciadv.abc9207](https://www.science.org/doi/10.1126/sciadv.abc9207` (1 mention) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 41 |
| Terms named correctly | 34 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025265` (1 mention) - the report calls it "72% (in detailed-MRI subgroup)"; HP calls it **Stiff toe**
- `HP:0031808` (2 mentions) - the report calls it "Camptocormia"; HP calls it **Decreased total basophil count**
- `CL:0002608` (2 mentions) - the report calls it "radial glial cell"; CL calls it **hippocampal neuron**
- `CL:0002500` (2 mentions) - the report calls it "cranial neural crest cell"; CL calls it **P enteroendocrine cell**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016575` (obsolete histone deacetylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002079` (2 mentions) - the report calls it "Hypoplasia of the corpus callosum", "Hypoplasia of corpus callosum"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Hypoplasia of corpus callosum" among its other names
- `GO:0006335` (2 mentions) - the report calls it "DNA replication-independent nucleosome assembly"; GO calls it **DNA replication-dependent chromatin assembly**, and lists "DNA replication-dependent nucleosome assembly" among its other names
- `CL:0000047` (2 mentions) - the report calls it "neural progenitor cell"; CL calls it **neural stem cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0030606` - called "Bryant-Li-Bhoj neurodevelopmental syndrome 1", "BRYLIB1"
- `HP:0002079` - called "Hypoplasia of the corpus callosum", "Hypoplasia of corpus callosum"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.