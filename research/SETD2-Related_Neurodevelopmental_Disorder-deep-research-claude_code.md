---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-25T15:22:44.136644'
end_time: '2026-11-25T15:30:41.455429'
duration_seconds: 477.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SETD2-Related Neurodevelopmental Disorder
  mondo_id: MONDO:0800477
  category: Mendelian
  causal_genes: SETD2
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
  - claude-opus-5-5
  web_search_requests: 16
  num_turns: 1
  total_cost_usd: 1.9709632349999997
  session_id: e6fd4fbc-2fdc-4275-9843-2686f6665d59
  stop_reason: end_turn
  tool_calls: 55
  retrieval_calls: 55
  assistant_text_blocks: 8
citation_count: 17
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 36
  on_topic: 19
  off_topic: 4
  off_topic_references:
  - PMID:9700202
  - PMID:11214970
  - PMID:16118227
  - PMID:16286007
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 47
  verified: 42
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 11
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0000966
    reported_labels:
    - Other organs in RAPAS:** retina
    ontology_label: retina
  labels_variant: 8
  service_unreachable: 4
  obsolescence_unchecked: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SETD2-Related Neurodevelopmental Disorder
- **MONDO ID:** MONDO:0800477 (if available)
- **Causal gene(s):** SETD2
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

Please provide a comprehensive research report on **SETD2-Related Neurodevelopmental Disorder** covering all of the
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

I'm collecting the main SETD2 papers now and pulling their abstracts and full texts.

I have the main clinical and mouse-model papers. I'm still waiting on the OMIM entries, and in the meantime I'm checking gene identifiers and a couple of other cohort abstracts.

The OMIM lookup agent is still running. I'll write the report once its results arrive.

## Summary

All four pages are OMIM entries served from a mirror at git.lsit.ucsb.edu, not omim.org. WebFetch returned each page in roughly 40,000-character chunks, so I read several chunks per page using the offsets it suggested. Where a section came only from the tool's model-written summary of unread text, I mark it **[summary]**. Everything else is **[verbatim]** page text. Quotes are kept under 125 characters because the source is non-preapproved. Paraphrase is used elsewhere.

**Still unread or summary-only:**
- 616831: characters 79,794 to 139,897 were not read. Parts of the synopsis and description come from summary.
- 620155: the last ~4,800 characters (rest of the clinical synopsis) were not read.
- 620157: the clinical synopsis was never located in verbatim text, so it is summary-only.
- 612778: Description, Cloning, Mapping, Gene Function and the Luscan-Lumish molecular genetics are all summary-only. The H3K36me3, alpha-tubulin K40 and RNA polymerase II statements are therefore not verbatim. The Animal Model section was not found in the text read.

URLs read (base path `https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/`): `616831`, `620155`, `620157`, `612778`, with offsets 39897, 139897, 179794, 219691 and 279794 where needed.

---

## 1. #616831 Luscan-Lumish syndrome (LLS)

**Gene and mapping:** SETD2 (612778), cytogenetic location 3p21.31, autosomal dominant, mapping key 3 (molecular basis known). **[verbatim]**

**Clinical synopsis [verbatim for most categories; the behavioral, endocrine and miscellaneous lines are summary]:**
- Inheritance: autosomal dominant.
- Growth: tall stature, short stature and obesity are all listed.
- Head: macrocephaly.
- Face: malar hypoplasia, long face, pointed chin, prominent mandible.
- Ears: recurrent otitis media. Eyes: downslanting palpebral fissures. Nose: long nose.
- Genitourinary: polycystic ovaries.
- Hands: advanced carpal ossification, hyperlaxity of hands.
- CNS: hypotonia, developmental delay, intellectual disability, speech delay, Chiari malformation, ventriculomegaly, seizures (tonic-clonic or nonfebrile), syringomyelia.
- Behavioral **[summary]**: autism spectrum disorder, anxiety, behavior troubles, hyperphagia, behavioral outbursts, compulsions.
- Endocrine **[summary]**: menstrual irregularity, polycystic ovary syndrome.
- Miscellaneous: variable phenotype; three unrelated patients (last curated February 2016).
- Molecular basis: SETD2 allelic variant 612778.0001.

**Description [verbatim]:** "is characterized by macrocephaly, intellectual disability, speech delay, low sociability, and behavioral problems" (Luscan 2014; Lumish 2015). It adds that "More variable features include postnatal overgrowth, obesity, advanced carpal ossification, developmental delay, and seizures."

**Clinical features [verbatim, condensed]:**
- Luscan 2014: two unrelated individuals with postnatal overgrowth, macrocephaly, obesity, speech delay, advanced carpal ossification, and long, large hands and feet. Facial features included a prominent forehead, downslanting palpebral fissures, long face and nose, malar hypoplasia and prominent mandible. Behavior problems included attention deficit, temper tantrums, aggression and low sociability.
- Lumish 2015: a 17-year-old girl with ASD, intellectual disability, compulsions, anxiety, ADHD, tonic-clonic seizures from age 10, Chiari I, hydrocephalus, progressive macrocephaly, syringomyelia and short stature.
- Van Rij 2018: a 4.5-year-old boy and a 23-year-old woman, both with macrocephaly, speech delay and autism-spectrum features. The woman had a slightly thickened corpus callosum and BMI 32.3.
- Marzin 2019: four new patients, plus a review of nine previous ones. Over 90% had macrocephaly, 83% intellectual disability, 89% ASD and 100% behavioral difficulties.
- Chen 2021: two new patients, plus a review of 14. Intellectual disability in 7/7, speech delay in 11/12, tall stature in 7/12, ASD in 8/14, recurrent otitis media in 5, accelerated bone maturation in 4.

**Inheritance [verbatim]:** The SETD2 variants in the Luscan 2014 and Lumish 2015 patients arose de novo. Segregation in a third patient (Luscan 2014) could not be assessed because that patient was adopted.

**Molecular genetics [verbatim, with PMIDs]:**
- O'Roak 2012 (PMIDs 23160955 and 22495309): exome sequencing of 677 individuals from 209 simplex families. Four individuals with ASD had SETD2 variants: nonsense C94X (paternal) and Q7X (maternal), de novo missense I41F, and a de novo frameshift (patient 12565.p1, which is allele 612778.0001).
- Iossifov 2014 (PMID 25363768): two patients with a 1-bp deletion and a missense variant.
- Luscan 2014 (PMID 24852293): two "Sotos-like" patients with variants 612778.0002 and 612778.0003. Neither was in dbSNP, 1000 Genomes or Exome Variant Server.
- Lumish 2015 (PMID 26084711): a de novo frameshift in the 17-year-old girl, which is allele 612778.0004 on the SETD2 page.
- Van Rij 2018 (PMID 29681085): two de novo frameshifts, c.1647_1667delinsAC (exon 3) and c.6775delG (exon 15).
- Marzin 2019 (PMID 31643139): nonsense K1426X and Y2157X, and missense Y1666C and R1625H, all in the SET2 catalytic domain. Across 13 patients the variants were loss-of-function, 69% truncating and 31% missense, spread through the gene.
- Chen 2021 (PMID 33766796) [verbatim portion]: a missense variant c.3185C>T (P1062L), not in large databases. [summary]: a splice variant, c.4715+1G>A. Of the 19 variants reviewed, 13 were classified pathogenic, 5 likely pathogenic and 1 (missense) VUS.

**Animal model:** not present in the text read.

**Mapping:** 3p21.31 (phenotype table). No separate mapping section.

**References [verbatim, all 8 PMIDs]:**
- Chen 2021: 33766796
- Iossifov 2014: 25363768
- Lumish 2015: 26084711
- Luscan 2014: 24852293
- Marzin 2019: 31643139
- O'Roak 2012, Science: 23160955
- O'Roak 2012, Nature: 22495309
- Van Rij 2018: 29681085

---

## 2. #620155 Rabin-Pappas syndrome (RAPAS)

**Gene and mapping:** SETD2, 3p21.31, autosomal dominant, mapping key 3. **[verbatim]**

**Molecular basis:** a specific heterozygous missense mutation, R1740W, which is allele 612778.0005.

**Clinical synopsis [verbatim through the Eyes section; the rest is summary]:**
- Growth: failure to thrive.
- Head and face: small head circumference with progressive microcephaly, dysmorphic facial features, flat face, small forehead, biparietal narrowing, micrognathia, maxillary and mandibular hypoplasia.
- Ears: sensorineural and conductive hearing loss, forward-facing ears.
- Eyes: hypertelorism, arched eyebrows, short and upslanting palpebral fissures, strabismus, retinal telangiectasia, retinal exudates, retinal detachment, optic nerve coloboma, cataracts.
- Nose **[summary]**: small upturned nose, wide nasal bridge, broad tip, low-hanging columella.
- Cardiovascular **[summary]**: congenital heart defects (septal defects, aortic valve abnormalities).
- Respiratory **[summary]**: respiratory difficulties, hypoventilation, sleep apnea.
- Chest: thoracic dysplasia. Abdomen: feeding difficulties requiring tube feeding.
- Genitourinary: cryptorchidism, multicystic and dysplastic kidneys, dilated collecting system.
- Skeletal: joint contractures, craniosynostosis, scoliosis, hip dysplasia, proximally implanted thumbs and halluces, hypoplastic distal phalanges, camptodactyly. Skin and nails: hypoplastic nails.
- Neurologic: profound global developmental delay, severe to profound intellectual disability, absent speech, inability to walk, seizures in some, corpus callosum hypoplasia, shallow sulci, enlarged ventricles, pontocerebellar hypoplasia.
- Prenatal: premature delivery. Laboratory: hyponatremia in some. Miscellaneous: onset at birth; de novo.

**Description [verbatim]:** RAPAS "is a multisystemic disorder characterized by severely impaired global development apparent from infancy," with feeding difficulties, failure to thrive, small head circumference and dysmorphic features. "they do not achieve walking or meaningful speech." Other organ systems may be involved, including skeletal, genitourinary, cardiac and possibly endocrine.

**Clinical features [verbatim, Rabin 2020]:** 12 unrelated patients (group 1), aged 1 month to 12 years.
- Nine were born preterm, and four of their mothers had preeclampsia.
- All had feeding difficulties and failure to thrive. None had overgrowth, and several had microcephaly down to -4 SD.
- Respiratory insufficiency was common.
- Seven had seizures, many refractory. Brain imaging was abnormal in all.
- All patients over 2 months had ophthalmic abnormalities, including retinal telangiectasia with exudates resembling Coats disease, retinal detachment, optic nerve coloboma and cataracts.
- Eight had mixed hearing loss and eight had infantile hyponatremia.
- Almost all had genitourinary or congenital heart involvement.

**Inheritance [verbatim]:** the mutations were de novo.

**Molecular genetics [verbatim]:** de novo heterozygous R1740W (c.5218C>T, allele 612778.0005) in 12 unrelated patients. The variant was not in gnomAD and was found through clinical genetics services. No functional studies were done. The authors describe the phenotype as more severe than in patients with other SETD2 variants, including R1740Q at the same codon.

**Animal model:** not present in the text read.

**Mapping:** 3p21.31 (phenotype table).

**References [verbatim]:** one entry. Rabin et al., Am J Med Genet 182A:2037-2048, 2020, PMID **32710489**.

---

## 3. #620157 Intellectual developmental disorder, autosomal dominant 70 (MRD70)

**Gene and mapping:** SETD2, 3p21.31, autosomal dominant, mapping key 3. Phenotypic series PS156200 (67 entries). **[summary]**

**Molecular basis:** heterozygous R1740Q (c.5219G>A, allele 612778.0006). **[verbatim]**

**Clinical synopsis [summary only; not found in verbatim text]:**
- Head and face: low-normal head circumference, brachycephaly, hypotonic facies, malar flattening, retrognathia.
- Eyes: upslanting palpebral fissures, straight eyebrows, myopia, strabismus.
- Mouth: high-arched palate, crowded teeth.
- Hands: fifth-finger clinodactyly, camptodactyly.
- Neurologic: global developmental delay, mildly delayed walking, impaired fine motor skills, moderate intellectual impairment, speech delay, hypotonia, behavioral abnormalities.
- Prenatal: polyhydramnios (one patient).
- Miscellaneous: onset in infancy; de novo; three unrelated patients.

**Description [verbatim]:** MRD70 "is characterized by mild global developmental delay, moderately impaired intellectual disability with speech difficulties," with behavioral abnormalities. Hypotonia and dysmorphic features are more variable. Source: Rabin 2020.

**Clinical features [verbatim, Rabin 2020]:** three unrelated patients (group 2) with mild to moderate intellectual impairment. "They had mild global developmental delay and speech delay, but all achieved independent walking."
- Patient 1: a 15-year-old boy at a special school, with behavioral abnormalities and a developmental level of about 6 years. Dysmorphic features included upslanting palpebral fissures, straight upslanting eyebrows, brachycephaly, fifth-finger clinodactyly and camptodactyly.
- Patient 2: a 4.5-year-old boy with poor speech, hypotonia, strabismus and joint hyperlaxity. Brain imaging was normal. The pregnancy was complicated by polyhydramnios.
- Patient 3: an 8-year-old girl with IQ 67 to 76 and behavioral abnormalities. Features included high-arched palate, crowded teeth, retrognathia, myopia, malar flattening, hypotonia and broad eyebrows.

**Inheritance [verbatim]:** de novo.

**Molecular genetics [verbatim]:** de novo heterozygous R1740Q, absent from gnomAD. "Functional studies of the variant and studies of patient cells were not performed." The phenotype is considered distinct from patients with the R1740W variant (612778.0005).

**Animal model:** not present in the text read.

**Mapping:** 3p21.31 (phenotype table).

**References [verbatim]:** one entry, Rabin 2020, PMID **32710489**.

---

## 4. #612778 SETD2 (gene entry)

**Title and aliases [verbatim]:** SET DOMAIN-CONTAINING PROTEIN 2; SETD2. Aliases: SET2; HUNTINGTIN-INTERACTING PROTEIN B (HYPB); HUNTINGTIN-BINDING PROTEIN, 231-KD (HBP231); KIAA1732.

**Cytogenetic location [verbatim]:** 3p21.31. Genomic coordinates (GRCh38): chr3:47,016,436-47,164,840.

**Gene-phenotype relationships [verbatim]:** MRD70 (620157), LLS (616831) and RAPAS (620155), all autosomal dominant, mapping key 3.

**Description [summary]:** H3K36 methylation is linked to transcribed regions. SETD2 is the main methyltransferase for H3K36 trimethylation (H3K36me3). Summary quote: "SETD2 is the primary methyltransferase catalyzing H3K36 trimethylation (H3K36me3)." Xu 2019 is cited, which also links H3K36me3 to transcription fidelity, splicing and DNA repair.

**Cloning and expression [summary]:**
- Faber 1998 (PMID 9700202): partial clone HYPB with a WW domain.
- Nagase 2000 (PMID 11214970): cloned as KIAA1732, predicting 1,325 amino acids.
- Rega 2001 (PMID 11461154): full-length HBP231. Summary quote: "The deduced 2,061-amino acid protein has a calculated molecular mass of about 231 kD." The protein has a SET domain and a C-terminal WW/WWP domain.

**Mapping [summary]:** Rega 2001 placed the gene at 3p21.3-p21.2 by FISH and sequence analysis. The page header gives 3p21.31.

**Gene function [summary; not verbatim]:**
- H3K36 methylation and H3K36me3: Sun 2005 (PMID 16118227) showed that the SET and flanking domains mediate H3K36-specific methyltransferase activity. Xu 2019 (PMID 31040401) found that in mouse oocytes Setd2 is needed to establish maternal imprints, and that Setd2 loss causes female sterility and embryonic lethality.
- Yeast orthologue: Carrozza 2005 (PMID 16286007) and Keogh 2005 (PMID 16286008) showed that yeast Set2 methylates H3K36 and works with the Rpd3 deacetylase complex.
- RNA polymerase II: Sun 2005 reported that a C-terminal fragment associates with hyperphosphorylated RNA polymerase II.
- Alpha-tubulin K40: Park 2016 (PMID 27518565) reported that SETD2 methylates alpha-tubulin at K40, making it a dual-function methyltransferase. Summary quote: "directly methylated both histones and alpha-tubulin."
- Interaction partners: Faber 1998 showed that HYPB binds huntingtin through its WW domain. Rega 2001 showed that HBP231 binds the adenovirus E1A TS2 motif in a sequence-specific way.
- Hacker 2016 (PMID 27528607): the R1625C SET-domain mutation reduces substrate binding and catalytic activity. SETD2-mediated H3K36me3 contributes to double-strand break repair.

**Allelic variants [verbatim; the page lists "6 Selected Examples"]:**
- .0001 LUSCAN-LUMISH SYNDROME: SETD2, 1-BP DEL, 6341A (rs869025569). c.6341delA, frameshift Asn2114IlefsTer33, de novo, in female patient 12565.p1 with ASD (O'Roak 2012, PMID 23160955). Lumish 2015 (PMID 26084711) noted failure to thrive, seizures, motor delay, low-normal IQ and macrocephaly in this patient.
- .0002 LUSCAN-LUMISH SYNDROME: SETD2, LEU1815TRP (rs869025570). c.5444T>G (L1815W), de novo, in a 26-year-old French man with "Sotos-like syndrome" (Luscan 2014, PMID 24852293).
- .0003 LUSCAN-LUMISH SYNDROME: SETD2, GLN274TER (rs869025571). c.820C>T (Q274X), in a 23-year-old woman who was adopted, so her parents could not be tested (Luscan 2014).
- .0004 LUSCAN-LUMISH SYNDROME: SETD2, 1-BP DEL, 2028T (rs869025572). c.2028delT, frameshift Pro677LeufsTer19, de novo, in a 17-year-old girl (Lumish 2015, PMID 26084711).
- .0005 RABIN-PAPPAS SYNDROME: SETD2, ARG1740TRP (rs1057523157). c.5218C>T (R1740W), de novo, in 12 patients (Rabin 2020, PMID 32710489).
- .0006 INTELLECTUAL DEVELOPMENTAL DISORDER, AUTOSOMAL DOMINANT 70: SETD2, ARG1740GLN (rs2107651195). c.5219G>A (R1740Q), de novo, in 3 patients (Rabin 2020).

The full variant table at omim.org/allelicVariants/612778 was not fetched, so there are likely more alleles than these six.

**Animal model:** no animal-model text was found. The page only has external links to model-organism resources (Alliance, FlyBase, IMPC/MGI, MMRRC, WormBase, ZFIN).

**References:** the page lists 18 references. The verbatim tail confirmed nine PMIDs, and the remaining eight come from the summary.
- Verbatim: Nagase 2000 (11214970); O'Roak 2012 Science (23160955); O'Roak 2012 Nature (22495309); Park 2016 (27518565); Rabin 2020 (32710489); Rega 2001 (11461154); Sun 2005 (16118227); Van Rij 2018 (29681085); Xu 2019 (31040401). Marzin 2019 (31643139) is also confirmed by its DOI in the verbatim tail.
- Summary only: Carrozza 2005 (16286007); Chen 2021 (33766796); Faber 1998 (9700202); Hacker 2016 (27528607); Iossifov 2014 (25363768); Keogh 2005 (16286008); Lumish 2015 (26084711); Luscan 2014 (24852293). Chen, Iossifov, Lumish and Luscan are also confirmed in the #616831 reference list.

---

## All PMIDs (unique, across the four entries)

| PMID | Reference | Entries |
|---|---|---|
| 9700202 | Faber 1998 (HYPB) | 612778 (summary) |
| 11214970 | Nagase 2000 (KIAA1732) | 612778 |
| 11461154 | Rega 2001 (HBP231) | 612778 |
| 16118227 | Sun 2005 (H3K36 methyltransferase) | 612778 |
| 16286007 | Carrozza 2005 | 612778 (summary) |
| 16286008 | Keogh 2005 | 612778 (summary) |
| 22495309 | O'Roak 2012, Nature | 616831, 612778 |
| 23160955 | O'Roak 2012, Science | 616831, 612778 |
| 24852293 | Luscan 2014 | 616831, 612778 |
| 25363768 | Iossifov 2014 | 616831, 612778 |
| 26084711 | Lumish 2015 | 616831, 612778 |
| 27518565 | Park 2016 (alpha-tubulin K40) | 612778 |
| 27528607 | Hacker 2016 (R1625C) | 612778 (summary) |
| 29681085 | Van Rij 2018 | 616831, 612778 |
| 31040401 | Xu 2019 (maternal imprinting) | 612778 |
| 31643139 | Marzin 2019 | 616831, 612778 |
| 32710489 | Rabin 2020 | 620155, 620157, 612778 |
| 33766796 | Chen 2021 | 616831, 612778 |

**Scope:** This report covers MONDO:0800477, the SETD2 neurodevelopmental disorders (SETD2-NDD). The causal gene is *SETD2* (OMIM gene *612778, 3p21.31). It treats the disorder as the umbrella term that GeneReviews uses. That umbrella covers three OMIM entities: Luscan-Lumish syndrome (LLS, #616831), Rabin-Pappas syndrome (RAPAS, #620155) and intellectual developmental disorder, autosomal dominant 70 (MRD70, #620157).

**Retrieval limits:**
- Searches did not return the MONDO:0800477 record itself, so the ID could not be confirmed directly.
- GeneReviews (NBK575927), PubMed abstract pages and the PMC page for Lee et al. 2023 were blocked by bot-checks. GeneReviews and Lee 2023 content therefore comes from search-engine snippets of those pages.
- The full text of Rabin et al. 2020 was read from the publisher PDF.
- Ontology IDs that do not appear in a retrieved source are marked *(suggested; verify)*.

---

## 1. Disease Information

**Overview.** GeneReviews (Pappas & Rabin; PMID 34978780; https://www.ncbi.nlm.nih.gov/books/NBK575927/) defines the condition as follows: *"SETD2 neurodevelopmental disorders (SETD2-NDDs) represent a clinical spectrum that most commonly includes various degrees of intellectual disability and behavioral findings (most typically an autism spectrum disorder)."* It adds that *"the most common well-defined phenotype [is] SETD2-NDD with macrocephaly/overgrowth, although not everyone has overgrowth."*

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0800477 (given by the user; not retrieved). Secondary sources give other MONDO IDs for LLS (MONDO:0014791 per MedGen, reported in a search summary; not checked against MedGen). |
| OMIM (gene) | *612778 *SETD2* (https://view.ncbi.nlm.nih.gov/omim/612778) |
| OMIM (phenotypes) | #616831 Luscan-Lumish syndrome; #620155 Rabin-Pappas syndrome; #620157 Intellectual developmental disorder, AD 70 (MRD70) (Parra 2023, PMID 37372360; OMIM 612778) |
| KEGG DISEASE | H02444 Luscan-Lumish syndrome (https://www.kegg.jp/entry/H02444) |
| GeneReviews | NBK575927 / PMID 34978780 |
| NCBI Gene | 29072. Listed aliases include LLS, HYPB, SET2, HIF-1, HIP-1, KMT3A, MRD70, RAPAS (https://www.ncbi.nlm.nih.gov/gene/29072) |
| Orphanet, ICD-10/11, MeSH | Not retrieved. No disease-specific ICD code is expected; use generic ID/ASD codes. |

**Synonyms:** SETD2-NDD; SETD2-related overgrowth syndrome; Sotos-like syndrome (SETD2); Luscan-Lumish syndrome (overgrowth subtype); Rabin-Pappas syndrome (p.Arg1740Trp subtype); MRD70 (p.Arg1740Gln subtype).

**Source of evidence:** All of it is aggregated case reports and case series of individual patients. There are no EHR-based or registry studies.

## 2. Etiology

- **Cause:** Heterozygous germline pathogenic variants in *SETD2*, which are mostly de novo.
  - Luscan et al. 2014 (J Med Genet; PMID 24852293) first described two patients with a "Sotos-like" overgrowth: a de novo p.Leu1815Trp missense change and a p.Gln274* nonsense change. Their shared features were *"overgrowth, macrocephaly, obesity, speech delay, and advanced carpal ossification."*
  - Lumish et al. 2015 (J Autism Dev Disord; PMID 26084711) reported a de novo frameshift in a 17-year-old girl with autism, ID and epilepsy.
- **Genetic risk factors:**
  - Loss-of-function variants anywhere along the gene cause LLS.
  - The recurrent missense changes at codon 1740 cause RAPAS (p.Arg1740Trp) or MRD70 (p.Arg1740Gln) (Rabin 2020, PMID 32710489; Parra 2023, PMID 37372360).
  - *SETD2* is highly constrained in gnomAD: pLI 1.00, LOEUF 0.21 (Developmental Brain Disorder Gene Database, https://dbd.geisingeradmi.org/site/SETD2).
  - ClinGen rates haploinsufficiency as "Sufficient evidence for dosage pathogenicity" (https://dosage.clinicalgenome.org/clingen_gene.cgi?sym=SETD2).
- **Environmental risk factors, protective factors, gene–environment interactions:** None reported. Not applicable to a monogenic de novo disorder.

## 3. Phenotypes

The best quantitative data come from Rabin et al. 2020, Table 1 (PMID 32710489). It compares a literature LLS group with 12 p.Arg1740Trp and 3 p.Arg1740Gln patients; the HPO IDs below are the ones given in the paper. Rabin's LLS column covered only 7–10 earlier patients. Marzin 2019 (PMID 31643139; 13 patients) reports **ID 83%, ASD 89%, behavioural difficulties 100%**, with "nearly all" macrocephalic and about half obese.

| Phenotype (HPO) | LLS (literature) | R1740W (RAPAS) | R1740Q (MRD70) |
|---|---|---|---|
| ID / global developmental delay (HP:0001249 / HP:0001263) | 7/9 (78%) | 12/12 (100%), profound | 3/3 (100%), moderate–severe |
| Autism (HP:0000717) | 7/7 (100%) | 0/12 | 0/3 |
| Seizures (HP:0001250) | 1/6 (17%) | 7/12 (58%) | 0/3 |
| Hypotonia (HP:0001290) | 0/7 | 12/12 | 2/3 |
| Postnatal macrocephaly (HP:0000256) | 8/8 (100%) | 0/12 | 0/3 |
| Microcephaly (HP:0000252) | 0/8 | 12/12 | 0/3 |
| Overgrowth (HP:0001548) / obesity (HP:0001513) | 9/9 (100%) | 0/12 | 0/3 |
| Failure to thrive in infancy (HP:0001531) | 0/10 | 12/12 | 0/3 |
| Feeding difficulties (HP:0011968) | 0/10 | 12/12 | 0/3 |
| Long face (HP:0000276) | 3/5 | 0/12 | 0/3 |
| Large mandible (HP:0000303) / pointed chin (HP:0000307) | 3/5 each | 0/12 | 0/3, 1/3 |
| Hypertelorism (HP:0000316) | 2/5 | 12/12 | 0/3 |
| Micrognathia (HP:0000347) | 0/5 | 12/12 | 0/3 |
| Corpus callosum hypoplasia (HP:0002079) | 0/10 | 9/12 (Table 1 reads "9/12 (100%)", which is internally inconsistent; the text says all scanned patients had structural abnormalities) | 0/3 |
| Pontine hypoplasia (HP:0012110) | 0/10 | 8/12 | 0/3 |
| Cerebellar hypoplasia (HP:0001321) | 0/10 | 12/12 | 0/3 |
| Chiari type 1 (HP:0007099) / hydrocephalus (HP:0000238) | 1/10 each | 0/12 | 0/3 |
| Retinal telangiectasia, Coats-like (HP:0007763) | 0/10 | 8/10 | 0/3 |
| Retinal detachment (HP:0000541) | 0/10 | 5/10 | 0/3 |
| Sensorineural (HP:0000407) / conductive (HP:0000405) hearing loss | 0/10 | 6/8, 7/8 | 0/3 |
| Hypoventilation (HP:0002791) | 0/10 | 9/12 | 0/3 |
| Hyponatremia (HP:0002902) | 0/10 | 8/12 | 0/3 |
| Congenital heart defect (HP:0001627) | 0/10 | 11/12 | 0/3 |
| Genitourinary anomalies (HP:0000119) | 0/7 | 11/12 | 0/3 |
| Skeletal abnormalities (HP:0000924) | 5/6 | 12/12 | 2/3 |

**Other features**
- **LLS** (Luscan 2014; Marzin 2019; OMIM 616831):
  - speech delay (HP:0000750 *suggested*)
  - advanced carpal ossification / advanced bone age
  - tall stature (HP:0000098 *suggested*)
  - behavioural problems
  - OMIM notes that more than 90% of patients have macrocephaly.
- **Additional features listed by GeneReviews:** hypothyroidism, precocious puberty, hypotonia/hypermobility, scoliosis, refractive error/strabismus, hearing loss, congenital heart defects and cryptorchidism.
- **RAPAS-specific features** (Rabin 2020):
  - *"None of the patients in Group 1 achieved speech or independent walking."*
  - Skeletal findings include proximally implanted triphalangeal thumbs, camptodactyly and hip dysplasia.
  - All 5 males had cryptorchidism.
  - Three patients needed tracheostomy.
- **Cohort data, Parra 2023** (PMID 37372360; 18 new patients):
  - Most new patients had the LLS phenotype.
  - The following counts come only from an automated summary of the PMC full text and were not checked against the page: macrocephaly 11/18, ID 9/18, overgrowth 8/18, ASD 6/18, seizures 2/18.
- **Variable expressivity:** Some patients have developmental delay without overgrowth (Wu 2023, PMID 37025455).
- **Possible tumour phenotype:** A 2025 case had normal cognition and multiple tumours, with a SETD2 episignature (Lucain 2025, PMID 40104911). Lee 2023 noted that *"two of 10 cases with a SETD2-NDD had developed a neoplasm"* (PMID 37166351).
- **Severity:** Mild to profound. RAPAS is the most severe form, MRD70 is intermediate and LLS ranges from mild to moderate. Onset is congenital or in infancy.
- **Quality of life:** No formal QoL data. The impact is dominated by ID/ASD, and in RAPAS by total care needs (gastrostomy, tracheostomy, no ambulation).

## 4. Genetic/Molecular Information

- **Gene:** *SETD2* (SET domain containing 2, histone lysine methyltransferase; alias KMT3A), 3p21.31, NCBI Gene 29072, OMIM 612778. HGNC:18420 is *suggested; verify*. The reference transcript is NM_014159.
- **Variant spectrum:**
  - Marzin 2019: truncating ~69% (frameshift, nonsense, splice) and missense ~31%.
  - Parra 2023 new cohort: 9 truncating, 1 in-frame deletion, 8 missense; 8 de novo, 4 inherited, 6 untested.
  - Reported variants include p.Gln274* and p.Leu1815Trp (Luscan 2014); a de novo frameshift in Tlemsani 2016 (PMID 27317772), the only *SETD2* hit among 210 NSD1-negative patients with a Sotos-like phenotype; and c.5835_5836insAGAA (Wu 2023).
- **Recurrent hotspot:**
  - c.5218C>T p.(Arg1740Trp), ClinVar VCV000388568, Pathogenic/Likely pathogenic, recurrent de novo, absent from gnomAD.
  - c.5219G>A p.(Arg1740Gln), absent from gnomAD (Rabin 2020).
  - Some ClinVar records number this residue Arg1696 on an alternative transcript.
- **Population frequency:** Pathogenic variants are essentially absent from gnomAD. One inherited nonsense variant, p.Gln7*, is present at 0.000244 in gnomAD v3.1.2 (Parra 2023), so its pathogenicity and penetrance are uncertain.
- **Germline vs somatic:** The disorder is germline. Somatic *SETD2* loss is common in clear-cell renal carcinoma and other cancers, which is a separate topic.
- **Functional consequence:**
  - LLS: loss of function / haploinsufficiency.
  - Codon 1740: an alternative mechanism. Rabin 2020 wrote *"suggesting an alternative mechanism, such as gain of function, effects on epigenetic regulation, or posttranslational modification of the cytoskeleton."* Lee 2023 *"predict[s] a gain-of-function mechanism for SETD2 codon 1740 pathogenic variants."*
- **Modifier genes:** None reported.
- **Chromosomal abnormalities:** No specific ones. 3p21.31 deletions that include *SETD2* were not reviewed.

**Epigenetic information (Lee 2023, PMID 37166351):**
- LLS (truncating variants) has a hypomethylation episignature: 778 differentially methylated positions (DMPs), 767 hypomethylated and 11 hypermethylated.
- Codon-1740 cases are uniformly hypermethylated (*"All DMPs show hypermethylated across 6 SETD2-1740 cases, whereas all hypomethylated in 4 SETD2-LLS cases"*). The two signatures run in completely opposite directions.
- R1740W cases (4) are more severely hypermethylated than R1740Q cases (2).
- An episignature was used to reclassify the VUS p.Ser1658Leu (Lucain 2025, PMID 40104911).

## 5. Environmental Information

There are no known environmental, lifestyle or infectious contributors. Not applicable.

## 6. Mechanism / Pathophysiology

**Causal chain**
1. A heterozygous germline *SETD2* variant, usually de novo, branches into two routes:
   - **Branch A (LLS):** truncating or loss-of-function variants lead to haploinsufficiency (pLI 1.0; ClinGen haploinsufficiency evidence Sufficient).
   - **Branch B (RAPAS/MRD70):** Arg1740 missense variants are *inferred* to act by gain of function or an altered function (Rabin 2020; Lee 2023).
2. Altered SETD2 activity changes trimethylation of histone H3K36 (H3K36me3) over the bodies of transcribed genes (Rabin 2020 introduction). SETD2 also methylates α-tubulin at K40 (Koenning 2021, PMID 34014281).
3. Changed H3K36me3 leads to changes in genome-wide DNA methylation. This is shown as opposite episignatures (hypomethylation in LLS, hypermethylation at codon 1740; Lee 2023). The link through H3K36me3-guided DNMT3A/B recruitment is *inferred*. Xu 2021 showed DNMT3A/B binding at clustered protocadherin (cPcdh) regulatory regions.
4. In developing cortex, SETD2-dependent H3K36me3 maintains expression of cPcdh genes. Loss of this expression leads to abnormal neocortical arealization and cortico-thalamo-cortical circuit defects (mouse; Xu 2021, PMID 33523829: *"SETD2 maintains the expression of clustered protocadherin (cPcdh) genes in an H3K36me3 methyltransferase-dependent manner"*).
5. In parallel, loss of microtubule methylation leads to shorter axons and less dendritic arborization in neurons, and anxiety/autism-related behaviour, *without* chromatin or expression changes (heterozygous Setd2^SRI/wt mice; Koenning 2021).
6. In adult brain, loss of Setd2 leads to reduced hippocampal volume, altered connectivity and dentate-gyrus neurogenesis defects (Atterton 2025, PMID 41023182).
7. Together these produce the clinical picture: ID, ASD, seizures and behavioural phenotypes.
   - The overgrowth and macrocephaly of LLS are *inferred* to result from dysregulated growth programs shared with NSD1/Sotos (H3K36 pathway convergence; Chen B 2025, PMID 40198378). This has not been demonstrated.
   - In Branch B, the *mechanism is unknown*: altered developmental gene regulation leads to brain malformation (pontocerebellar/callosal hypoplasia), microcephaly and multi-organ anomalies.

**Details**
- **Protein:** SETD2 is the sole H3K36 trimethyltransferase. Its SRI domain binds RNA polymerase II and α-tubulin (Koenning 2021). It also has roles in DNA mismatch repair, splicing and suppressing cryptic transcription (Rabin 2020; review by Mitchell 2023, PMID 37921122).
- **Suggested GO terms (verify):** histone H3K36 methyltransferase activity; histone H3-K36 trimethylation; regulation of DNA methylation; microtubule cytoskeleton organization; cerebral cortex regionalization; neuron projection development; dendrite morphogenesis.
- **Suggested CL terms (verify):** neuron (CL:0000540); radial glial cell / neural progenitor (CL:0000681); excitatory cortical neuron; dentate gyrus granule cell. Hematopoietic stem cell (CL:0000037) is relevant only to the cancer literature.
- **Immune, metabolic and tissue-damage mechanisms:** Not implicated. Hyponatremia in RAPAS is clinically observed but has no mechanism.
- **Omics:** Patient blood DNA-methylation episignatures (Lee 2023). No patient transcriptomics, proteomics or single-cell data were found.

## 7. Anatomical Structures Affected

- **Primary:** brain (UBERON:0000955), including cerebral cortex (UBERON:0000956), corpus callosum (UBERON:0002336), pons, cerebellum (UBERON:0002037) and hippocampus.
- **Other organs in RAPAS:** retina (UBERON:0000966), inner/middle ear, heart (UBERON:0000948), kidney/urinary tract, airway, hands and feet. In LLS, skeletal growth plates (overgrowth, advanced bone age).
- The UBERON IDs are suggested from general knowledge.
- **Subcellular:** nucleus/chromatin (GO:0005634, GO:0000785) and microtubule cytoskeleton (GO:0015630), including neurites and growth cones (Koenning 2021).
- **Laterality:** Bilateral and systemic. Retinal involvement can be asymmetric (Rabin 2020, Figure 4).

## 8. Temporal Development

- **Onset:** Congenital. RAPAS shows up prenatally or neonatally: 9/12 were premature, there was failure to thrive and microcephaly acquired in infancy, and head circumference *"drifted below the third percentile in infancy"* (Rabin 2020). LLS is recognized in infancy or early childhood (developmental delay, postnatal overgrowth).
- **Course:** A static neurodevelopmental disorder. Microcephaly in RAPAS is progressive: *"microcephaly was progressive and was at least 2.5 SD below the mean"*. The 2026 case report in JCEM Case Rep (PMID 42831230) describes endocrine manifestations. Tumours may appear in adulthood (Lucain 2025: tumours from childhood to age 37).
- **Critical periods:** Early childhood intervention. Mouse data place the cortical arealization role in embryonic corticogenesis (Xu 2021).
- **Remission:** None.

## 9. Inheritance and Population

- **Inheritance:** Autosomal dominant. Most cases are de novo; all 15 codon-1740 cases were de novo.
- **Transmission:**
  - GeneReviews: *"transmission of a SETD2 pathogenic variant from a parent to a child has been reported in one family."*
  - Earlier SSC trios had paternally (p.Cys94*) and maternally (p.Gln7*) inherited variants (Rabin 2020 intro), and Parra 2023 reports 4 inherited variants. This implies incomplete penetrance or milder parental expression for some variants. Their pathogenicity is not settled.
- **Expressivity:** Variable.
- **Not applicable:** Anticipation, founder effects and consanguinity have no role.
- **Germline mosaicism:** Not documented in the sources retrieved. Recurrence risk for sibs of a de novo proband is low but above the general population, by analogy with other de novo disorders.
- **Epidemiology:** Prevalence is unknown. By 2023 about 51 patients had been reported (LLS 34, RAPAS 14, MRD70 3; Parra 2023). There is no evidence of ethnic or geographic clustering. Sex ratio: RAPAS 5M:7F (Rabin 2020); no overall imbalance reported.

## 10. Diagnostics

- **Criteria:** GeneReviews says *"No consensus clinical diagnostic criteria … have been published"*. Diagnosis rests on suggestive findings plus a heterozygous pathogenic *SETD2* variant.
- **Genetic testing:**
  - Exome or genome sequencing is first-line in ID/ASD, or multigene panels for overgrowth/Sotos-like or ID.
  - *SETD2* is included in overgrowth and ID panels. Tlemsani 2016 screened 210 NSD1-negative patients with a Sotos-like phenotype.
  - Chromosomal microarray for 3p21.31 copy-number changes.
- **Episignature (DNA methylation array):** Distinguishes LLS (hypomethylation) from codon-1740 (hypermethylation) and helps resolve VUS (Lee 2023; Lucain 2025).
- **Imaging and evaluations:**
  - Brain MRI: Chiari I and hydrocephalus in LLS; pontocerebellar hypoplasia, callosal hypoplasia, mega cisterna magna and posterior-fossa cysts in RAPAS.
  - Bone age.
  - EEG if seizures.
  - Echocardiogram, renal ultrasound, dilated retinal exam (Coats-like vasculopathy) and audiology, especially for R1740W.
  - Thyroid function (GeneReviews).
- **Differential diagnosis:**
  - Sotos syndrome (*NSD1*)
  - Weaver syndrome (*EZH2*)
  - Tatton-Brown–Rahman syndrome (*DNMT3A*)
  - Malan syndrome (*NFIX*)
  - PTEN hamartoma tumour syndrome
  - other ASD/ID-macrocephaly genes
  - for RAPAS: pontocerebellar hypoplasias and Coats-plus spectrum
  
  Sotos, Weaver and Tatton-Brown–Rahman are framed as differentials in Luscan 2014 and Tlemsani 2016.
- **Screening:** No newborn or carrier screening. Prenatal or preimplantation testing is possible once the familial variant is known.

## 11. Outcome/Prognosis

- **Survival:** No survival data for LLS, where life expectancy is presumably near normal (not formally studied). In RAPAS, one infant *"died at 1 month of age"* with hypoventilation and hypoplastic pulmonary vessels (Rabin 2020). Respiratory morbidity is significant: 10/12 had airway or respiratory problems and 3 needed tracheostomy.
- **Morbidity:** Lifelong ID and ASD. In RAPAS, none achieved speech or walking. MRD70 patients achieved speech, and one had a full-scale IQ of 67.
- **Prognostic factors:** Genotype is the strongest predictor (R1740W > R1740Q > loss of function). Episignature severity correlates with clinical severity (Lee 2023).
- **Tumour risk:** Possible neoplasms (2/10 in Lee 2023; Lucain 2025). Not quantified.

## 12. Treatment

There is no disease-specific therapy, and no ClinicalTrials.gov trials were identified. Management is supportive and follows GeneReviews:

| Intervention | Suggested NCIT term (verify) |
|---|---|
| Early intervention, special education | Educational intervention |
| Speech, occupational and physical therapy | Speech therapy / Occupational therapy / Physical therapy |
| Applied behavioural therapy for ASD | Behavioral therapy |
| Antiseizure medication | Anticonvulsant agent |
| Gastrostomy tube feeding (RAPAS: majority) | Gastrostomy |
| Tracheostomy / nocturnal oxygen | Tracheostomy; Oxygen therapy |
| Sodium supplementation for hyponatremia (RAPAS) | — |
| Laser photocoagulation for Coats-like retinopathy | Laser photocoagulation |
| Hearing aids | — |
| Thyroid hormone replacement; GnRH analogue for precocious puberty | Levothyroxine; GnRH agonist |
| Surgery for heart, urogenital, skeletal and scoliosis problems | — |

No pharmacogenomics, gene therapy or RNA therapy has been reported.

## 13. Prevention

- **Primary prevention:** Not applicable (de novo).
- **Genetic counselling:** Each child of an affected individual has a 50% risk (GeneReviews). Parental testing is needed to estimate recurrence. Prenatal or preimplantation diagnosis is possible.
- **Tertiary prevention:**
  - Surveillance of growth, development, seizures, vision (retinal exam), hearing, thyroid and puberty.
  - Echo and renal imaging at diagnosis for codon-1740 cases.
  - Awareness of possible tumour risk. There is no consensus tumour-surveillance protocol.

## 14. Other Species / Natural Disease

No naturally occurring animal disease was found; OMIA was not searched. *SETD2* is highly conserved (yeast Set2 → mammals). Orthologs exist in mouse (*Setd2*), zebrafish and *Drosophila*. Specific ortholog Gene IDs were not retrieved. Not zoonotic.

## 15. Model Organisms

| Model | Phenotype | Source |
|---|---|---|
| Constitutive *Setd2* knockout mouse | Embryonic lethal, indicating a key role in development | Cited in Rabin 2020 introduction |
| *Setd2* Emx1-Cre / Nestin-Cre conditional knockout (dorsal forebrain / neural) | Abnormal neocortical arealization and cortico-thalamo-cortical circuits; *"defects in social interaction, motor learning, and spatial memory"*, recapitulating Sotos-like behaviour; cPcdh dependence | Xu 2021, PMID 33523829 |
| *Setd2^SRI/wt* knock-in (pathogenic SRI-domain mutation; tubulin methylation lost) | Viable; anxiety-like phenotype; reduced axon length and dendritic arborization; homozygous form lethal; no histone or expression changes | Koenning 2021, PMID 34014281 |
| Dorsal telencephalon *Setd2* deletion, adult | Reduced brain volume, especially hippocampus; altered connectivity; dentate-gyrus neurogenesis defects | Atterton 2025, PMID 41023182 |
| Sox1-Cre *Setd2* conditional knockout | Neonatal death with intracerebral haemorrhage and vascular abnormalities (contrast with *Nsd1* knockout: small brain) | Chen B 2025, PMID 40198378 |

**Limitations of these models:**
- The models are knockouts, not heterozygous loss-of-function alleles. Overgrowth and macrocephaly are not recapitulated.
- There is no codon-1740 (R1740W) knock-in model. The proposed gain-of-function mechanism is untested.

---

### Key references
- Luscan A et al. 2014, J Med Genet — PMID 24852293
- Lumish HS et al. 2015, J Autism Dev Disord — PMID 26084711
- Tlemsani C et al. 2016, J Med Genet — PMID 27317772
- van Rij MC et al. 2018, Am J Med Genet A — PMID 29681085
- Marzin P et al. 2019, Am J Med Genet C — PMID 31643139
- Rabin R et al. 2020, Am J Med Genet A 182:2037–48 — PMID 32710489 (doi:10.1002/ajmg.a.61724; full text read)
- Chen M et al. 2021, Eur J Med Genet — PMID 33766796 (abstract not retrieved)
- Pappas J, Rabin R. GeneReviews — PMID 34978780
- Xu L et al. 2021, Sci Adv — PMID 33523829
- Koenning M et al. 2021, Brain — PMID 34014281
- Lee S et al. 2023, Hum Mol Genet — PMID 37166351
- Parra A et al. 2023, Genes — PMID 37372360
- Wu Y et al. 2023, Front Genet — PMID 37025455
- Zhang Y et al. 2023, Front Genet — PMID 36777730
- Mitchell B et al. 2023, J Cell Sci — PMID 37921122
- Lucain M et al. 2025, Am J Med Genet A — PMID 40104911
- Chen B et al. 2025, Hum Genet — PMID 40198378
- Atterton C et al. 2025, Sci Rep — PMID 41023182
- Ünsel-Bolat G et al. 2026, Dev Neurobiol — PMID 41466099
- Huang J et al. 2026, JCEM Case Rep — PMID 42831230

**Web sources:**
- [GeneReviews NBK575927](https://www.ncbi.nlm.nih.gov/books/NBK575927/)
- [OMIM 612778](https://view.ncbi.nlm.nih.gov/omim/612778)
- [OMIM 616831 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/616831)
- [OMIM 620155 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/620155)
- [Rabin 2020 PDF](https://pure.amsterdamumc.nl/ws/files/156919749/Genotypephenotype-correlation-at-codon-1740-of-setd2.pdf)
- [Lee 2023 PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10630252)
- [Parra 2023 PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10297832)
- [Koenning 2021 PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8418347)
- [Xu 2021 PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7775761)
- [ClinVar 388568](https://ncbi.nlm.nih.gov/clinvar/variation/388568/)
- [ClinGen dosage](https://dosage.clinicalgenome.org/clingen_gene.cgi?sym=SETD2)
- [DBD SETD2](https://dbd.geisingeradmi.org/site/SETD2)
- [NCBI Gene 29072](https://www.ncbi.nlm.nih.gov/gene/29072)
- [KEGG H02444](https://www.kegg.jp/entry/H02444)

The OMIM report is complete, so there is nothing partial to add. Here is the condensed version.

**Coverage and caveats:** All four pages are from a mirror at git.lsit.ucsb.edu. Sections marked [summary] come from the tool's model-written summary of unread text, not verbatim page text. Gene function for SETD2 (612778), including the H3K36me3, alpha-tubulin K40 and RNA polymerase II statements, is summary-only. The 616831 chunk from character 79,794 to 139,897 and the last ~4,800 characters of 620155 were not read.

**616831, Luscan-Lumish syndrome:** SETD2, 3p21.31, autosomal dominant. Features include macrocephaly, intellectual disability, speech delay, low sociability and behavioral problems. Variants are de novo, mostly truncating (Marzin 2019 reports 69% truncating, 31% missense). PMIDs: 33766796, 25363768, 26084711, 24852293, 31643139, 23160955, 22495309, 29681085.

**620155, Rabin-Pappas syndrome:** SETD2, 3p21.31, autosomal dominant. Caused by de novo R1740W (allele .0005) in 12 patients. Features include severe global developmental delay, microcephaly, ophthalmic abnormalities, hearing loss, hyponatremia and feeding difficulties. PMID: 32710489.

**620157, MRD70:** SETD2, 3p21.31, autosomal dominant. Caused by de novo R1740Q (allele .0006) in 3 patients with mild to moderate intellectual disability and independent walking. The clinical synopsis is summary-only. PMID: 32710489.

**612778, SETD2:** 3p21.31; GRCh38 chr3:47,016,436-47,164,840. Allelic variants .0001 to .0006 are verbatim:
- .0001: c.6341delA, frameshift (O'Roak 2012)
- .0002: c.5444T>G, L1815W (Luscan 2014)
- .0003: c.820C>T, Q274X (Luscan 2014)
- .0004: c.2028delT, frameshift (Lumish 2015)
- .0005: c.5218C>T, R1740W (Rabin 2020)
- .0006: c.5219G>A, R1740Q (Rabin 2020)

The page lists 6 "selected examples," so the full variant table was not fetched. Gene function covers the H3K36me3 methyltransferase role (Sun 2005, Xu 2019), alpha-tubulin K40 methylation (Park 2016) and association with hyperphosphorylated RNA polymerase II (Sun 2005). These come from summary. The 18 references were confirmed in part, and the rest come from the summary.

Full quotes, section-by-section detail and the PMID table are in my previous message.

# Addendum: OMIM details for SETD2-Related Neurodevelopmental Disorder

The OMIM entries arrived after the main report was written. They come from a mirror of OMIM, not omim.org. Statements marked † were read only in an automated summary of the page, not in the page text itself.

## Section 1: Identifiers

- **OMIM gene entry *612778 *SETD2*:**
  - Location: 3p21.31, GRCh38 chr3:47,016,436–47,164,840.
  - Other names: SET2, HYPB (huntingtin-interacting protein B), HBP231, KIAA1732.
- **Phenotype entries, all autosomal dominant:**
  - #616831 Luscan-Lumish syndrome (LLS)
  - #620155 Rabin-Pappas syndrome (RAPAS)
  - #620157 Intellectual developmental disorder, autosomal dominant 70 (MRD70), part of phenotypic series PS156200†
- **OMIM's definitions:**
  - LLS "is characterized by macrocephaly, intellectual disability, speech delay, low sociability, and behavioral problems," and "more variable features include postnatal overgrowth, obesity, advanced carpal ossification, developmental delay, and seizures."
  - RAPAS "is a multisystemic disorder characterized by severely impaired global development apparent from infancy." Affected people "do not achieve walking or meaningful speech."
  - MRD70 "is characterized by mild global developmental delay, moderately impaired intellectual disability with speech difficulties."

## Section 3: Phenotypes

**Further LLS features from OMIM's clinical synopsis:**
- tall stature, though short stature also occurs
- recurrent otitis media
- polycystic ovaries
- hyperlaxity of the hands
- Chiari malformation, ventriculomegaly and syringomyelia
- tonic-clonic seizures
- anxiety, hyperphagia and compulsions†

**Chen et al. 2021 (PMID 33766796)** reported 2 new patients and reviewed 14 earlier ones (as quoted by OMIM):

| Feature | Frequency |
|---|---|
| Intellectual disability | 7/7 |
| Speech delay | 11/12 |
| Tall stature | 7/12 |
| Autism spectrum disorder | 8/14 |
| Recurrent otitis media | 5 patients |
| Accelerated bone maturation | 4 patients |

**MRD70:**
- Patients had mild to moderate impairment and all of them learned to walk.
- Reported features include brachycephaly, upslanting palpebral fissures, myopia or strabismus, and fifth-finger clinodactyly or camptodactyly.
- One pregnancy was complicated by polyhydramnios.

## Section 4: Allelic variants listed by OMIM (6 selected examples)

| OMIM allele | Variant | Disorder | Details | Source |
|---|---|---|---|---|
| .0001 | c.6341delA, p.Asn2114IlefsTer33 | LLS | de novo; autism patient 12565.p1 | O'Roak 2012, PMID 23160955 |
| .0002 | c.5444T>G, p.Leu1815Trp | LLS | de novo | Luscan 2014, PMID 24852293 |
| .0003 | c.820C>T, p.Gln274Ter | LLS | patient was adopted, so inheritance unknown | Luscan 2014 |
| .0004 | c.2028delT, p.Pro677LeufsTer19 | LLS | de novo; 17-year-old girl | Lumish 2015, PMID 26084711 |
| .0005 | c.5218C>T, p.Arg1740Trp (rs1057523157) | RAPAS | 12 patients, all de novo | Rabin 2020, PMID 32710489 |
| .0006 | c.5219G>A, p.Arg1740Gln (rs2107651195) | MRD70 | 3 patients, all de novo | Rabin 2020 |

**Other variants OMIM cites:**
- **Early autism sequencing studies:**
  - O'Roak 2012 (PMIDs 23160955 and 22495309) found SETD2 variants in four people with autism, including inherited nonsense C94X (paternal) and Q7X (maternal), and a de novo I41F.
  - Iossifov 2014 (PMID 25363768) also reported SETD2 variants.
- **Marzin 2019** reported K1426X, Y2157X, Y1666C and R1625H, mostly in the catalytic domain.
- **Van Rij 2018** reported two de novo frameshift variants, c.1647_1667delinsAC and c.6775delG.
- **Chen 2021** reported P1062L and c.4715+1G>A†. Of the 19 variants they reviewed, 13 were pathogenic, 5 likely pathogenic and 1 of uncertain significance†.
- **Hacker 2016** (PMID 27528607): the SET-domain variant R1625C reduces substrate binding and catalytic activity, which supports loss of function†.

## Section 6: Mechanism (support from OMIM's gene entry, all †)

- **Sun 2005** (PMID 16118227): SETD2 is an H3K36-specific methyltransferase, and a C-terminal fragment associates with hyperphosphorylated RNA polymerase II.
- **Park 2016** (PMID 27518565): SETD2 methylates α-tubulin at K40, so it acts on both histones and microtubules.
- **Xu 2019** (PMID 31040401): in mouse oocytes, Setd2 is needed to establish maternal imprints. Losing it causes female sterility and embryonic lethality.
- **Rega 2001** (PMID 11461154): the full protein, HBP231, is about 2,061 amino acids. It has a SET domain and a C-terminal WW domain, and binds huntingtin (Faber 1998, PMID 9700202).

## Section 15: Model organisms

OMIM has no animal-model text for these entries. The mouse models listed in the main report remain the evidence base.

## Sources

- [OMIM 616831](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/616831)
- [OMIM 620155](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/620155)
- [OMIM 620157](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/620157)
- [OMIM 612778](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/612778)

A second notice from the OMIM lookup agent arrived, but it only repeats a condensed version of what it already sent. Nothing needs to change in the SETD2 neurodevelopmental disorder report or in the OMIM addendum that follows it, and those two remain the final output.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 36 |
| On topic | 19 |
| Off topic | 4 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:9700202` (2 mentions) - Huntingtin interacts with a family of WW domain proteins.
  - shared terms: gene
- `PMID:11214970` (1 mention) - Prediction of the coding sequences of unidentified human genes. XIX. The complete sequences of 100 new cDNA clones from brain which code for large proteins in vitro.
  - shared terms: gene
- `PMID:16118227` (2 mentions) - Identification and characterization of a novel human histone H3 lysine 36-specific methyltransferase.
  - shared terms: gene
- `PMID:16286007` (1 mention) - Histone H3 methylation by Set2 directs deacetylation of coding regions by Rpd3S to suppress spurious intragenic transcription.
  - shared terms: gene

Weighed against this report's own most characteristic terms: `setd2`, `gene`, `patient`, `rabin`, `lls`, `rapas`, `disorder`, `mrd70`, `variant`, `novo`, `developmental`, `overgrowth`, `phenotype`, `clinical`, `delay`, `speech`, `intellectual`, `luscan`, `p21`, `macrocephaly`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 20 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0000966` (1 mention) - the report calls it "Other organs in RAPAS:** retina"; UBERON calls it **retina**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001290` (1 mention) - the report calls it "Hypotonia"; HP calls it **Generalized hypotonia**
- `HP:0000256` (1 mention) - the report calls it "Postnatal macrocephaly"; HP calls it **Macrocephaly**
- `HP:0002079` (1 mention) - the report calls it "Corpus callosum hypoplasia"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Corpus callosum hypoplasia" among its other names
- `HP:0012110` (1 mention) - the report calls it "Pontine hypoplasia"; HP calls it **Hypoplasia of the pons**, and lists "Pontine hypoplasia" among its other names
- `HP:0007763` (1 mention) - the report calls it "Retinal telangiectasia, Coats-like"; HP calls it **Retinal telangiectasia**
- `HP:0001627` (1 mention) - the report calls it "Congenital heart defect"; HP calls it **Abnormal heart morphology**, and lists "Congenital heart defect" among its other names
- `HP:0000119` (1 mention) - the report calls it "Genitourinary anomalies"; HP calls it **Abnormality of the genitourinary system**, and lists "Genitourinary tract anomalies" among its other names
- `UBERON:0000955` (1 mention) - the report calls it "Primary:** brain"; UBERON calls it **brain**

### Terms the ontology service could not be reached for

4 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0800477` (3 mentions)
- `HP:0000541` (1 mention)
- `HP:0000924` (1 mention)
- `GO:0015630` (1 mention)

### Terms whose obsolescence could not be checked

1 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `MONDO:0014791` (1 mention)