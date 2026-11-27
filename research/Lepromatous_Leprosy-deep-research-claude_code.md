---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-27T00:50:04.566369'
end_time: '2026-11-27T00:56:15.731796'
duration_seconds: 371.17
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Lepromatous Leprosy
  mondo_id: MONDO:0005127
  category: Infectious Disease
  causal_genes: not recorded
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 33
  num_turns: 41
  total_cost_usd: 1.81644
  session_id: 270def6b-1978-411b-a367-1ee3ede71a7e
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  tool_calls: 39
  retrieval_calls: 34
  assistant_text_blocks: 3
citation_count: 57
reference_validation:
  total_references: 35
  verified: 34
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.029
  quotes_checked: 0
  quotes_valid: 0
  quotes_not_checkable: 1
  relevance_assessed: 34
  on_topic: 9
  unresolved_references:
  - DOI:10.1242/dmm.010215/2032116/dmm_010215.pdf
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 28
  verified: 9
  not_found: 0
  obsolete: 0
  unverifiable: 19
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 3
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0000460
    reported_labels:
    - abnormal nasal morphology
    ontology_label: Narrow nose
  labels_variant: 1
  service_unreachable: 19
  obsolescence_unchecked: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lepromatous Leprosy
- **MONDO ID:** MONDO:0005127 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Lepromatous Leprosy** covering all of the
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

Let me write the script with the Write tool and run it separately.

I've gathered core sources on immunology, genetics, epidemiology and treatment. Next I'm searching for animal models, genetic loci, and prevention trials, then I'll write the report.

I have gathered sufficient sourced material across the key domains. I'll now write the report inline.

---

# Comprehensive Research Report: Lepromatous Leprosy (MONDO:0005127)

**Interpretation note (stated up front per instructions):** This template lists "Causal gene(s): not recorded." Lepromatous leprosy is an **infectious disease**, not a monogenic disorder; it has **no human causal gene**. Its cause is the obligate intracellular bacterium ***Mycobacterium leprae*** (and, in a subset, ***Mycobacterium lepromatosis***). The human genetic factors described below are **susceptibility/modifier loci**, not causal genes. I treat the "causal factor" of this entry as the pathogen, and report human genetics as risk/susceptibility. Identifiers given (MONDO:0005127, ICD-10 A30.5, MeSH D015440) were confirmed and are used to anchor the entry.

A note on evidence source types is given throughout: (human clinical), (model organism), (in vitro), (computational/genomic). Where I could not retrieve a primary source in this session, I say so rather than fill from memory. Several landmark papers (e.g., the 2008 Han *M. lepromatosis* paper, the 1966 Ridley–Jopling paper) were confirmed only through citing/secondary sources because their full text or abstract was not retrievable in this session; these are flagged inline.

---

## 1. Disease Information

**Overview.** Lepromatous leprosy (LL) is the "low-resistance," multibacillary pole of the leprosy (Hansen's disease) clinical spectrum. It is a chronic granulomatous infection of skin and peripheral nerves caused by *M. leprae*, occurring in individuals who mount an **ineffective cell-mediated immune response**, permitting uncontrolled bacillary proliferation. The U.S. CDC describes the lepromatous pole as the end of the spectrum where "the patient has essentially no cell-mediated immunity to the infection and the bacilli multiply uncontrollably. The highest concentrations of bacilli are found in the skin and nerves" ([CDC Clinical Overview of Leprosy](https://www.cdc.gov/leprosy/hcp/clinical-overview/)).

**Key identifiers (confirmed this session):**
- **MONDO:** MONDO:0005127 ("lepromatous leprosy"), a subtype of leprosy ([SAIL Concept Library/MONDO](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0005127/)).
- **ICD-10-CM:** A30.5 ([Disease Ontology DOID:10887](https://disease-ontology.org/term/DOID:10887); cross-referenced from MONDO).
- **MeSH:** D015440 ("Leprosy, Lepromatous"), scope note: "A chronic communicable infection which is a principal or polar form of LEPROSY" ([MeSH record D015440](https://meshb.nlm.nih.gov/record/ui?ui=D015440)).
- **Disease Ontology:** DOID:10887 (synonym "type L leprosy") ([DO](https://disease-ontology.org/term/DOID:10887)).
- **ICD-11:** parent code **1B20** (Leprosy). *(I did not retrieve the exact ICD-11 subcode for the lepromatous form in this session; do not treat a specific ICD-11 extension code as verified.)*

**Synonyms / alternative names:** type L leprosy; lepromatous Hansen's disease; MeSH entry terms include "Leprosy, Cutaneous" and "Leprosy, Nodular" ([MeSH D015440](https://meshb.nlm.nih.gov/record/ui?ui=D015440)). In the Ridley–Jopling scheme the polar form is **LL**; borderline-lepromatous is **BL**; **diffuse lepromatous leprosy (DLL)** is a variant strongly associated with *M. lepromatosis* ([CDC EID systematic review](https://wwwnc.cdc.gov/eid/article/29/7/23-0024)).

**Information provenance:** Content here is derived from **aggregated disease-level resources** (ontologies, WHO/CDC surveillance, systematic reviews, GWAS, lesion-transcriptomics studies), not from individual EHR records.

---

## 2. Etiology

**Primary cause (infectious).** The causal agent is ***Mycobacterium leprae***, an acid-fast, obligate intracellular bacillus with extreme tropism for Schwann cells and macrophages and a doubling time of ~14 days; it cannot be grown in axenic culture. Its genome has undergone **massive reductive evolution**: Cole et al. sequenced a 3.27-Mb genome (vs. 4.41 Mb in *M. tuberculosis*) containing ~1,604 protein-coding genes and ~1,116 pseudogenes (vs. 6 in *M. tuberculosis*), with downsizing attributed to recombination between dispersed repeats ([Cole et al., *Nature* 2001, PMID 11234002](https://pubmed.ncbi.nlm.nih.gov/11234002/)). This gene decay underlies the obligate intracellular lifestyle, loss of many catabolic/respiratory functions, and culture failure ([Genome Biology spotlight](https://genomebiology.biomedcentral.com/articles/10.1186/gb-spotlight-20010222-03)).

A **second species, *Mycobacterium lepromatosis***, was identified in 2008 from two patients of Mexican origin who died of **diffuse lepromatous leprosy** and is strongly associated with DLL and **Lucio's phenomenon** (Han XY et al., *Am J Clin Pathol* 2008 — *attribution via citing sources; the original abstract was not retrieved this session*) ([CDC EID systematic review 2023](https://wwwnc.cdc.gov/eid/article/29/7/23-0024)).

**Why the *lepromatous* pole specifically.** LL is not simply "infection"; it is the outcome in hosts whose immune response fails to contain the organism. This immunological determinant is the organizing principle of the whole spectrum ([CDC](https://www.cdc.gov/leprosy/hcp/clinical-overview/)).

### Genetic risk factors (susceptibility; host, not causal)
Leprosy is one of the most heritable infectious diseases, and human genetics strongly influences both susceptibility and per-pole outcome:
- **PARK2/PACRG** regulatory-region variants — identified by positional cloning in Vietnamese families and replicated in Brazil as **common risk factors for leprosy** (Mira et al., *Nature* 2004) ([Nature 427:636-640](https://www.nature.com/articles/nature02326.pdf)). Replication is population-dependent (not confirmed in some Chinese/Indian samples).
- **NOD2, RIPK2, TNFSF15, CCDC122/C13orf31, HLA-DR, LRRK2** — Zhang et al. GWAS: variants in the **NOD2-mediated innate-immunity signaling pathway** confer susceptibility; associations at *C13orf31, LRRK2, NOD2, RIPK2* were **stronger in multibacillary than paucibacillary disease** (i.e., tilt toward the lepromatous pole) (Zhang FR et al., *N Engl J Med* 2009;361:2609-18) ([NEJM/JCI scholar](https://www.jci.org/references/scholar/29056/B56)). HLA-DR–DQ SNP rs602875 OR 0.67 (P=5.35×10⁻²⁷); NOD2 rs9302752 OR 1.59.
- **Additional loci:** Liu et al. added **BATF3, CCDC88B, CIITA-SOCS1** (three-stage Chinese GWAS, 8,313 cases/16,017 controls; "Discovery of six new susceptibility loci…", *Nat Genet* 2015) ([Nat Genet ng.3212](https://www.nature.com/articles/ng.3212.pdf)); Wang et al. added **SYN2 (3p25.2), BBS9 (7p14.3), CTSB (8p23.1), MED30 (8q24.11)** (*Nat Commun* 2016) ([ncomms13760](https://www.nature.com/articles/ncomms13760.pdf)); **IL23R/RAB32** were implicated earlier (2011). *HLA-B/C* region also appears (see §4 for its distinct role in drug hypersensitivity).

### Environmental risk factors
- **Prolonged close/household contact** with an untreated multibacillary case is the dominant exposure (transmission requires "prolonged, close contact … over many months") ([CDC transmission page](https://www.cdc.gov/leprosy/transmission/)).
- **Zoonotic/animal reservoirs:** nine-banded armadillos in the southern U.S. (*M. leprae* strain 3I-2-v1) — whole-genome evidence of near-identical strains in armadillos and locally-acquired U.S. patients (Truman RW et al., *N Engl J Med* 2011;364:1626-33, **PMID 21524213**) ([PMC3138484](https://pmc.ncbi.nlm.nih.gov/articles/PMC3138484)); red squirrels in the British Isles (*M. leprae* and *M. lepromatosis*) (Avanzi C et al., *Science* 2016;354:744-747, [PMID 27846605](https://pubmed.ncbi.nlm.nih.gov/27846605)).
- **Sex:** male predominance (~61% of patients male in a 32-study systematic review; males over-represented in multibacillary/lepromatous disease) ([PMC6686771](https://pmc.ncbi.nlm.nih.gov/articles/PMC6686771)).
- Lifestyle correlates of MB/lepromatous disease (higher alcohol use, hunting) reported in a 2025 NE-Brazil cohort ([PMC10404493 table](https://pmc.ncbi.nlm.nih.gov/articles/PMC10404493/table/tbl0015)).

### Protective factors
- **BCG vaccination:** meta-analysis of experimental studies gives **26% protection (95% CI 14–37%)**; observational studies overestimate at 61%; a second BCG dose adds protection (Setia MS et al., *Lancet Infect Dis* 2006;6:162-70, [PMID 16500597](https://pubmed.ncbi.nlm.nih.gov/16500597/)).
- **Single-dose rifampicin post-exposure prophylaxis (SDR-PEP):** 57% reduction in incidence over 2 years among contacts (COLEP trial, Moet FJ et al., *BMJ* 2008;336:761-764) ([PMC2287265](https://pmc.ncbi.nlm.nih.gov/articles/PMC2287265)).
- **Genetic protective alleles:** protective-direction ORs at HLA-DR–DQ (rs602875 OR 0.67) ([JCI scholar](https://www.jci.org/references/scholar/29056/B56)). I did not retrieve a dedicated gnomAD-based protective-variant analysis specific to LL this session.

### Gene–environment interactions
The COLEP editorial noted a subgroup signal that chemoprophylaxis "is less effective in household contacts who are genetically related to the index case," i.e., shared host genetics modifies the environmental (exposure + prophylaxis) effect ([BMJ editorial via PMC2287231](https://pmc.ncbi.nlm.nih.gov/articles/PMC2287231)). The core gene–environment axis is: innate-sensing genotype (NOD2 pathway, PARK2/PACRG) × *M. leprae* exposure → whether infection is cleared, contained (tuberculoid), or disseminates (lepromatous) ([NEJM 2009](https://www.jci.org/references/scholar/29056/B56); [Nature 2004](https://www.nature.com/articles/nature02326.pdf)).

---

## 3. Phenotypes

LL is multibacillary, symmetric, and disseminated. Suggested HPO anchors are given (some are general; exact HPO IDs should be verified against the HPO browser before ingestion — I did not query the HPO API directly this session).

| Phenotype | Type | Characteristics | Suggested HPO |
|---|---|---|---|
| Multiple symmetric skin macules/papules/nodules, poorly defined | clinical sign / physical | adult-onset; progressive; near-universal in LL | HP:0011121 (abnormal skin morphology)/HP:0200039 (papule) |
| **Leonine facies** (thickened, drooping facial skin) | physical | late manifestation | — |
| **Madarosis** (loss of eyebrows/eyelashes) | physical sign | late | HP:0000561 (absent eyebrow); HP:0000653 (sparse eyelashes) |
| **Saddle-nose / nasal collapse** (nasal mucosa + bone infiltration) | physical | late, severe | HP:0000460 (abnormal nasal morphology) |
| **Peripheral neuropathy**, symmetric glove-and-stocking sensory loss | sign/symptom | progressive; leads to painless injury | HP:0009830 (peripheral neuropathy); HP:0000763 (sensory neuropathy) |
| Nerve thickening | sign | progressive | HP:0009830 |
| **Hypogonadism / testicular involvement** | lab/physical | late infiltration | HP:0000135 (hypogonadism) |
| Ocular involvement (uveitis, corneal) | sign | often reaction-associated | HP:0000554 (uveitis) |
| High serum **anti-PGL-I IgM** | laboratory abnormality | ~80–100% seropositive in LL; tracks bacterial index | — |

([Wikipedia/clinical reviews and DermNet for leonine facies, madarosis, saddle-nose](https://pro.dermnetnz.org/topics/leprosy); [StatPearls NBK559307](https://www.ncbi.nlm.nih.gov/books/NBK559307/); CDC for the uncontrolled-bacilli skin/nerve distribution [CDC](https://www.cdc.gov/leprosy/hcp/clinical-overview/); anti-PGL-I seropositivity [SciELO RSBMT systematic review](https://scielo.br/j/rsbmt/a/CzygXLbBGkNZdYP8BCMTQgP/?lang=en)).

**Reactional phenotypes (immunologic flares):**
- **Erythema nodosum leprosum (ENL / Type 2 reaction):** crops of painful subcutaneous nodules, fever, systemic inflammation; neutrophil/TNF-α/immune-complex driven. Affects a large fraction of LL patients — classic teaching ~50% of LL (and ~10% of BL), though a pooled analysis (Voorend) gives lower incidences of 15.4% in LL and 4.1% in BL ([Walker/Lockwood review, Frontiers Immunol 2017](https://www.frontiersin.org/articles/10.3389/fimmu.2017.00233/pdf)).
- **Lucio's phenomenon:** necrotizing vasculitis / type III hypersensitivity occurring in **diffuse lepromatous leprosy**, usually untreated, associated with *M. lepromatosis* ([PMC4775876](https://pmc.ncbi.nlm.nih.gov/articles/PMC4775876/)).

**Quality-of-life impact:** multibacillary patients are ~4× more likely to have physical (Grade 2) disability than paucibacillary patients ([PMC6686771](https://pmc.ncbi.nlm.nih.gov/articles/PMC6686771)); disability drives stigma, loss of function, and employment impact. I did not retrieve LL-specific EQ-5D/SF-36 scores this session.

---

## 4. Genetic/Molecular Information

Because LL is infectious, "pathogenic variants" fall into two distinct categories:

**(a) Host susceptibility/modifier loci** (see §2): *NOD2, RIPK2, TNFSF15, CCDC122, HLA-DRB1/DQ, LRRK2, PARK2/PACRG, BATF3, CCDC88B, CIITA-SOCS1, IL23R, RAB32, SYN2, BBS9, CTSB, MED30*. These are **germline** common variants (mostly regulatory/intronic; some missense, e.g., IL23R rs76418789 G149R). The NOD2-pathway signal is enriched in MB/lepromatous disease ([NEJM 2009](https://www.jci.org/references/scholar/29056/B56); [Nat Genet 2015](https://www.nature.com/articles/ng.3212.pdf)). Functional consequence is altered innate antimycobacterial sensing/response rather than classical loss/gain-of-function of a single protein.

**(b) Pharmacogenomic variant — clinically actionable:**
- **HLA-B\*13:01** is a strong risk factor for **dapsone hypersensitivity syndrome (DHS)** in leprosy patients (OR 20.53; P=6.84×10⁻²⁵; sensitivity 85.5%, specificity 85.7%) (Zhang FR et al., *N Engl J Med* 2013, [PMID 24152261](https://pubmed.ncbi.nlm.nih.gov/24152261)). Allele frequency ~2–20% in Chinese, 1–12% in Indians, ~2–4% in SE Asians, near-absent in Europeans/Africans. An Indonesian/Papua validation gave OR 233.64 (sensitivity 91.2%, specificity 96.2%) ([PMC7592909](https://pmc.ncbi.nlm.nih.gov/articles/PMC7592909)). CPIC/PharmGKB-style use: pre-therapy screening. Suggested NCIT/pharmacogenomic annotation applies here.

**(c) Pathogen genomics:** *M. leprae* reductive genome with ~1,116 pseudogenes (Cole 2001, [PMID 11234002](https://pubmed.ncbi.nlm.nih.gov/11234002/)); drug-resistance determinants are somatic-equivalent pathogen mutations in **rpoB** (rifampicin), **folP1** (dapsone), **gyrA** (ofloxacin) — see §10/§12 ([Cambau et al. WHO surveillance, *Clin Microbiol Infect* 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6286419/)).

**Modifier genes:** HLA-DR–DQ and the MB-enriched loci act as outcome modifiers pushing toward the lepromatous pole ([NEJM 2009](https://www.jci.org/references/scholar/29056/B56)). LTA (lymphotoxin-α) was reported as a major risk factor for **early-onset** leprosy (Alcaïs et al., *Nat Genet* 2007, cited via [Mira 2004 follow-up summary](https://pubmed.ncbi.nlm.nih.gov/16973374/)).

**Epigenetics:** A Brazilian leukocyte methylome study (GEO GSE197331, Illumina EPIC array, n=35) reported a "deregulated methylation profile" in leprosy vs. controls, but did not stratify by lepromatous subtype ([OmicsDI GSE197331](https://omicsdi.org/dataset/geo/GSE197331)). LL-specific methylation data were not retrievable this session (reported as a gap).

**Chromosomal abnormalities:** Not applicable (infectious disease).

Suggested ontology/gene annotations: HGNC symbols above; GO: **GO:0032495** (response to muramyl dipeptide / NOD2), **GO:0045087** (innate immune response).

---

## 5. Environmental Information

- **Environmental factors:** principal determinant is human exposure to *M. leprae*/*M. lepromatosis* via respiratory secretions; possible soil/water and amoebic environmental persistence is studied but I did not retrieve a primary source this session.
- **Lifestyle:** male sex, alcohol use, and hunting associated with MB/lepromatous presentation ([PMC10404493](https://pmc.ncbi.nlm.nih.gov/articles/PMC10404493/table/tbl0015)).
- **Infectious agents (CHEBI/taxon):** *Mycobacterium leprae* (NCBI Taxon **1769**); *Mycobacterium lepromatosis* (NCBI Taxon **480418**). *(Taxon IDs provided from standard taxonomy; I did not re-query NCBI Taxonomy this session — verify before ingestion.)* Transmission is thought to be predominantly nasal/respiratory droplet with close contact ([CDC](https://www.cdc.gov/leprosy/transmission/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating event → clinical manifestation)

1. **Inhalation/close-contact exposure** to *M. leprae* (respiratory droplets) **leads to** entry and hematogenous dissemination, with tropism for cooler body sites (skin, superficial nerves, nasal mucosa) ([CDC](https://www.cdc.gov/leprosy/transmission/)). *(well-established clinically)*
2. In a host with **permissive innate-sensing genotype** (NOD2-pathway/PARK2–PACRG variants), *M. leprae* **results in** failure to trigger an effective Th1/antimicrobial program ([NEJM 2009](https://www.jci.org/references/scholar/29056/B56); [Nature 2004](https://www.nature.com/articles/nature02326.pdf)). *(genetic association; mechanism partly inferred)*
3. Lesional cytokine milieu **shifts toward Th2/regulatory** — IL-4, IL-5, **IL-10** predominate in multibacillary lesions (vs. IFN-γ/IL-2 in tuberculoid), **leading to** suppressed macrophage killing (Yamamura/Modlin/Bloom, *Science* 1991;254:277-279) ([meddean PDF](https://www.meddean.luc.edu/lumen/meded/hostdef/UseofGeneticProfilingleprosy%20array.pdf)). *(human lesion mRNA, in situ)*
4. **Type I interferon (IFN-β) program induces IL-10**, which **inhibits the IFN-γ–driven antimicrobial response** in macrophages — demonstrated in disseminated (lepromatous) lesions (Teles RMB et al., *Science* 2013;339:1448-53) ([PMC3671607](https://pmc.ncbi.nlm.nih.gov/articles/PMC3671607)). *(human lesion + in vitro)*
5. Macrophage program **diverges**: **IL-10 drives a phagocytic/scavenger program** (CD209, CD163, scavenger receptors) that ingests mycobacteria and oxidized LDL but does not kill, **whereas IL-15 drives the vitamin-D–dependent antimicrobial program**; the phagocytic pathway predominates in progressive multibacillary disease (Montoya D et al., *Cell Host Microbe* 2009;6:343-353, [PMID 19837374](https://www.pubmed.gov/19837374/)). *(human lesion + in vitro)* — **this is the branch point** between the lepromatous (phagocytic, non-killing) and tuberculoid/reversal (antimicrobial, killing) poles.
6. Non-killing macrophages accumulate bacilli and **host-derived oxidized phospholipids (e.g., PEIPC)**, becoming **foamy macrophages ("lepra cells")**; oxidized phospholipids further suppress innate immunity, reversible by normal HDL but not LL-patient HDL — a lipid pattern "strikingly similar to atherosclerosis" (Cruz D et al., *J Clin Invest* 2008;118:2917-28) ([PMC2467381](https://pmc.ncbi.nlm.nih.gov/articles/PMC2467381)). *(human lesion + in vitro)*
7. Unchecked bacillary load (**high bacterial index**) **results in** disseminated symmetric skin infiltration and high anti-PGL-I IgM titers ([SciELO RSBMT](https://scielo.br/j/rsbmt/a/CzygXLbBGkNZdYP8BCMTQgP/?lang=en)).
8. **Nerve-damage branch:** *M. leprae* **binds ErbB2 receptor tyrosine kinase** on myelinated Schwann cells, activating MEK→Erk1/2 **leading to early demyelination** independent of neuregulin (Tapinos N, Rambukkana A, *Nat Med* 2006;12:961-966) ([nm1433 PDF](https://www.nature.com/articles/nm1433.pdf)); *in vivo* (zebrafish), **PGL-1 reprograms infected macrophages to overproduce nitric oxide (iNOS)**, and reactive nitrogen species **injure axonal mitochondria → demyelination**, even before glial infection (Madigan CA et al., *Cell* 2017) ([PMC5848073](https://pmc.ncbi.nlm.nih.gov/articles/PMC5848073)). *(in vitro + model organism)*
9. **Niche-expansion branch:** *M. leprae* **reprograms adult Schwann cells to a progenitor/stem-like (pSLC), mesenchymal state**, which secrete chemokines and disseminate bacteria to other tissues (Masaki T et al., *Cell* 2013;152:51-67 — *via Nature news summary; original abstract not retrieved this session*) ([Nature news](https://www.nature.com/articles/nature.2013.12239)). *(model organism/in vitro)*
10. Progressive sensory **neuropathy → painless trauma, secondary infection, deformity and disability**; late infiltration **leads to** leonine facies, madarosis, saddle-nose, hypogonadism ([DermNet](https://pro.dermnetnz.org/topics/leprosy)).
11. **Reactional branches:** immune-complex deposition + neutrophil/TNF-α influx **causes ENL (Type 2)**; in DLL, necrotizing vasculitis **causes Lucio's phenomenon** ([Frontiers Immunol 2017](https://www.frontiersin.org/articles/10.3389/fimmu.2017.00233/pdf); [PMC4775876](https://pmc.ncbi.nlm.nih.gov/articles/PMC4775876/)).

**Upstream vs downstream:** Upstream = host innate-sensing genotype + IFN-β/IL-10 axis → macrophage program divergence (steps 2–5). Downstream = foamy-macrophage bacterial persistence, nerve demyelination, dissemination, disability (steps 6–10). Reactions (step 11) are superimposed immunologic events.

**Cell types (CL) involved:** macrophage (CL:0000235), foamy/lepra macrophage, Schwann cell (CL:0002573), T cell (CL:0000084), keratinocyte, fibroblast, neutrophil (CL:0000775, in ENL). **GO processes:** GO:0045087 (innate immune response), GO:0032606 (type I interferon production), GO:0032623/IL-10 signaling, GO:0002244 regulation; demyelination GO:0032289. **Pathways:** NOD-like receptor signaling (KEGG hsa04621), vitamin-D antimicrobial pathway, ErbB/MAPK (Erk1/2), IFN/IL-10 signaling.

---

## 7. Anatomical Structures Affected

- **Primary organs:** **skin** (UBERON:0002097) and **peripheral nerves** (UBERON:0000044 peripheral nervous system); nasal mucosa (UBERON:0001707). Highest bacillary concentrations are in skin and nerves ([CDC](https://www.cdc.gov/leprosy/hcp/clinical-overview/)).
- **Secondary/system involvement:** eyes (uveitis/keratitis; UBERON:0000970), testes (UBERON:0000473; hypogonadism), upper respiratory tract, reticuloendothelial system (liver/spleen in heavy multibacillary load), bone (facial/nasal destruction).
- **Tissue/cell level:** dermal macrophages become foamy "lepra cells"; **Schwann cells** of peripheral nerves are the signature neural target (demyelination, reprogramming) ([Nat Med 2006](https://www.nature.com/articles/nm1433.pdf); [Cell 2013](https://www.nature.com/articles/nature.2013.12239)).
- **Subcellular (GO Cellular Component):** bacilli reside in macrophage **phagosome/phagolysosome** (GO:0045335); axonal **mitochondria** (GO:0005739) are the injury target in PGL-1/NO-mediated nerve damage ([Cell 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5848073)).
- **Localization/lateralization:** LL is characteristically **symmetric and bilateral/diffuse** (contrasting with the asymmetric, localized tuberculoid pole), with predilection for cooler acral and facial sites ([CDC](https://www.cdc.gov/leprosy/hcp/clinical-overview/)).

---

## 8. Temporal Development

- **Onset:** adult-onset most common; **long incubation**, longer for lepromatous/MB disease (~**10 years average** for MB vs ~4 years for PB per NSW guideline; ranges 9 months–20+ years across sources) ([NSW Health leprosy control guideline](https://www.health.nsw.gov.au/Infectious/controlguideline/Pages/leprosy.aspx)). Onset pattern is **insidious/chronic**.
- **Progression:** untreated LL is **slowly progressive** with uncontrolled bacillary multiplication; chronic lifelong without treatment ([CDC](https://www.cdc.gov/leprosy/hcp/clinical-overview/)).
- **Course pattern:** chronic-progressive baseline, punctuated by **episodic reactions** (ENL/Type 2; Lucio's). **Reversal reactions** represent upgrading from the lepromatous toward the tuberculoid pole, spontaneously or during chemotherapy, with acquisition of effective antimicrobial responses (Ma F et al., *Nat Immunol* 2021;22:839-850, [DOI 10.1038/s41590-021-00956-8](https://www.nature.com/articles/s41590-021-00956-8)).
- **Remission:** treatment-induced bacteriologic cure with MDT; nerve damage and deformity may be irreversible. Critical intervention window is **before fixed nerve damage** ([WHO treatment page](https://www.who.int/teams/control-of-neglected-tropical-diseases/leprosy/treatment)).

---

## 9. Inheritance and Population

- **Epidemiology:** WHO reported **172,717 new leprosy cases globally in 2024** (9,397 children; 9,157 with Grade-2 disability; −5.5% vs 2023's 182,815); 188 countries reporting ([WHO WER "Global leprosy update 2024"](https://www.who.int/publications/i/item/who-wer10037-365-384); figures via [ILEP summary](https://ilepfederation.org/?p=18545)). Burden concentrated in SE-Asia > Americas > Africa (African Region 19,171 cases, 11.1%) ([WHO AFRO](https://www.afro.who.int/health-topics/leprosy)). The lepromatous/MB pole is a subset of this total. *(I did not retrieve LL-specific global prevalence or GBD DALY figures this session — reported as a gap.)*
- **Inheritance:** Not Mendelian. Susceptibility is **multifactorial/polygenic** with strong host-genetic and HLA contributions; pole determination (lepromatous vs tuberculoid) is itself partly genetically modified ([NEJM 2009](https://www.jci.org/references/scholar/29056/B56); [Nature 2004](https://www.nature.com/articles/nature02326.pdf)).
- **Penetrance/expressivity:** most infected individuals never develop disease; among those who do, the clinical pole varies — i.e., highly **incomplete penetrance and variable expressivity** of susceptibility genotypes.
- **Consanguinity/founder:** COLEP data suggest genetic relatedness to index case modifies risk/prophylaxis response ([BMJ editorial](https://pmc.ncbi.nlm.nih.gov/articles/PMC2287231)).
- **Demographics:** **male predominance** (~61% overall; males over-represented in lepromatous/MB disease; ~2:1 in some series) ([PMC6686771](https://pmc.ncbi.nlm.nih.gov/articles/PMC6686771); [Nigeria study PMID 12449892](https://pubmed.ncbi.nlm.nih.gov/12449892/)).
- **Geographic:** endemic in India, Brazil, Indonesia and other tropical regions; autochthonous zoonotic cases in southern U.S. (armadillo-linked) ([Truman 2011, PMID 21524213](https://pmc.ncbi.nlm.nih.gov/articles/PMC3138484)). *M. lepromatosis* is concentrated in the Americas (Mexico) but also reported in Asia ([CDC EID review](https://wwwnc.cdc.gov/eid/article/29/7/23-0024)).

---

## 10. Diagnostics

- **Clinical/laboratory:**
  - **Slit-skin smear** with Ziehl-Neelsen/Fite stain → **high bacterial index** defines multibacillary/lepromatous disease; WHO notes slit-skin smears as a common technique ([WHO 2018 guidelines summary](https://www.sfdermato.org/upload/files/fichiers/groupes-thematiques/Leprosy%20guidelines%202018.pdf)).
  - **Skin biopsy / histopathology:** dermal foamy macrophages (lepra cells) packed with acid-fast bacilli, grenz zone, scant lymphocytes (contrast with tuberculoid epithelioid granulomas).
  - **Serology:** **anti-PGL-I IgM** seropositive in ~80–100% of LL patients and correlates with bacterial index; useful for bacterial-load monitoring but not for paucibacillary detection ([SciELO RSBMT review](https://scielo.br/j/rsbmt/a/CzygXLbBGkNZdYP8BCMTQgP/?lang=en); [PMC96023](https://pmc.ncbi.nlm.nih.gov/articles/PMC96023)).
  - **PCR** for *M. leprae*/*M. lepromatosis* DNA (species discrimination, drug-resistance genotyping).
- **Genetic/resistance testing (pathogen):** PCR-sequencing of **rpoB (rifampicin), folP1 (dapsone), gyrA (ofloxacin)** drug-resistance-determining regions — WHO surveillance network ([Cambau 2018, PMC6286419](https://pmc.ncbi.nlm.nih.gov/articles/PMC6286419/)).
- **Host pharmacogenetic testing:** **HLA-B\*13:01** screening before dapsone to prevent DHS ([Zhang 2013, PMID 24152261](https://pubmed.ncbi.nlm.nih.gov/24152261)).
- **Clinical criteria:** WHO cardinal signs — hypopigmented/reddish anesthetic skin lesion, thickened peripheral nerve, and/or positive slit-skin smear; operational classification MB vs PB. Ridley–Jopling classifies the immunologic spectrum (TT–BT–BB–BL–LL) (Ridley DS, Jopling WH, *Int J Lepr* 1966;34:255-73 — [PMID 5950347](https://pubmed.ncbi.nlm.nih.gov/5950347); *title only, no abstract available*).
- **Differential diagnosis:** other causes of nodular/infiltrative dermatoses, cutaneous leishmaniasis, sarcoidosis, mycosis fungoides, syphilis, neurofibromatosis.
- **Screening:** WHO does **not** recommend testing asymptomatic people; contact tracing + SDR-PEP is the operational approach ([WHO 2018 guidelines](https://www.who.int/news/item/28-06-2018-who-to-publish-first-official-guidelines-on-leprosy-diagnosis-treatment-and-prevention)).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** leprosy itself is rarely directly fatal with treatment; mortality is driven by complications and by **treatment of reactions**. In an Ethiopian ALERT cohort, ENL carried significant mortality (8 ENL deaths vs 2 Type-1 reaction deaths, p=0.0168), attributed largely to **chronic corticosteroid therapy** (Walker SL et al., *PLoS Negl Trop Dis* 2014) ([PMC3953021](https://pmc.ncbi.nlm.nih.gov/articles/PMC3953021/)).
- **Morbidity/disability:** multibacillary/lepromatous disease → ~4× odds of Grade-2 physical disability vs paucibacillary ([PMC6686771](https://pmc.ncbi.nlm.nih.gov/articles/PMC6686771)); irreversible nerve damage, deformity, blindness, stigma.
- **Recovery:** MDT achieves bacteriologic cure; **nerve/function deficits present at diagnosis are often permanent**, making early treatment the key prognostic lever.
- **Prognostic factors:** bacterial index/anti-PGL-I titer (load), extent of nerve involvement at diagnosis, occurrence of reactions, drug resistance. **Drug resistance** (rifampicin in 5.1% of relapse / 2.0% of new MB cases in WHO survey) worsens prognosis ([Cambau 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6286419/)).
- **Complications:** recurrent ENL, Lucio's phenomenon (in DLL), secondary infection of anesthetic limbs, ocular damage. GBD DALY figures not retrieved this session (gap).

---

## 12. Treatment

**Standard WHO multidrug therapy (MDT)** — for multibacillary/lepromatous disease: **rifampicin + dapsone + clofazimine for 12 months** (three-drug regimen now recommended for all patients; PB = 6 months) ([WHO 2018 guidelines](https://www.sfdermato.org/upload/files/fichiers/groupes-thematiques/Leprosy%20guidelines%202018.pdf); [WHO NTD treatment page](https://www.who.int/teams/control-of-neglected-tropical-diseases/leprosy/treatment)).
- **Rifampicin** (NCIT: rifampin; bactericidal, RNA polymerase/rpoB), **dapsone** (dihydrofolate/folate pathway, folP1), **clofazimine** (anti-inflammatory riminophenazine).
- **Pharmacogenomics:** screen **HLA-B\*13:01** before dapsone (DHS risk) ([Zhang 2013](https://pubmed.ncbi.nlm.nih.gov/24152261)).

**Drug-resistant disease:** WHO recommends two of {clarithromycin, minocycline, a quinolone} + clofazimine ×6 months, then clofazimine + one ×18 months; avoid fluoroquinolone if ofloxacin resistance present (expert-opinion based) ([WHO 2018 guidelines summary](https://www.sfdermato.org/upload/files/fichiers/groupes-thematiques/Leprosy%20guidelines%202018.pdf)).

**Reaction management:**
- **ENL (Type 2):** **thalidomide** rapidly controls ENL and is superior to aspirin/pentoxifylline, but is teratogenic and restricted (Walker SL, Waters MFR, Lockwood DNJ, *Lepr Rev* 2007) ([LSHTM record](https://researchonline.lshtm.ac.uk/7920/); [Mahmoud & Walker 2019 review](https://researchonline.lshtm.ac.uk/id/eprint/4654740)); corticosteroids and clofazimine also used (steroid toxicity is a mortality driver, [Walker 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC3953021/)).
- **Type 1/reversal reaction:** corticosteroids.

**Advanced/experimental:** No gene/cell/RNA therapies apply (infectious disease). **Vaccines:** BCG (partial protection, [Setia 2006](https://pubmed.ncbi.nlm.nih.gov/16500597/)); **LepVax (LEP-F1 + GLA-SE)** subunit vaccine — Phase 1 safe and well tolerated, 24 volunteers (*Vaccine* 2020;38:1700-1707; [PMID 31899025](https://www.pubmed.gov/31899025/); trial **NCT03302897**); Phase 1b/2a **NCT03947437**; Phase 1b **NCT06627257** (Brazil).

**Supportive/rehabilitative:** wound/ulcer care for anesthetic limbs, physiotherapy, reconstructive surgery for deformity, ophthalmologic care, disability prevention and stigma/psychosocial support.

**Treatment strategy / outcomes:** MDT is highly effective bacteriologically; adherence and early initiation (before nerve damage) determine functional outcome. Suggested NCIT terms: Rifampin, Dapsone, Clofazimine, Thalidomide, Minocycline, Clarithromycin, Ofloxacin, BCG Vaccine.

---

## 13. Prevention

- **Primary prevention:**
  - **Chemoprophylaxis (SDR-PEP):** single-dose rifampicin to contacts ≥2 years → 57% reduction over 2 years (COLEP, [Moet 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2287265)); WHO recommends it for contacts ([WHO 2018](https://www.who.int/news/item/28-06-2018-who-to-publish-first-official-guidelines-on-leprosy-diagnosis-treatment-and-prevention)). **Single-dose rifapentine** gave an 84% reduction over 4 years in a Chinese cluster-RCT (Wang L et al., *N Engl J Med* 2023;388:1843-1852, [PMID 37195940](https://www.qxmd.com/r/37195940)) — a notable advance over rifampicin's ~2-year effect.
  - **BCG vaccination** (~26% protection experimentally; second dose adds benefit) ([Setia 2006](https://pubmed.ncbi.nlm.nih.gov/16500597/)).
- **Secondary prevention:** contact tracing/screening, early diagnosis and prompt MDT to interrupt transmission and prevent disability. WHO does not recommend screening asymptomatic persons with a test.
- **Tertiary prevention:** disability prevention (self-care, footwear, ulcer management), early reaction treatment, ocular protection.
- **Counseling/public health:** contact surveillance, health education, stigma reduction; **HLA-B\*13:01 pharmacogenetic counseling** before dapsone in high-frequency populations ([Zhang 2013](https://pubmed.ncbi.nlm.nih.gov/24152261)).
- **Caveat on PEP:** cost-effectiveness is debated — Lockwood and colleagues argued SDR "protects those who need it least" ([Nepalese commentary citing the debate, PMC8031444](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8031444/)).

---

## 14. Other Species / Natural Disease

- **Taxonomy of hosts:** Humans (*Homo sapiens*); **nine-banded armadillo** (*Dasypus novemcinctus*) — the principal non-human natural host and a zoonotic reservoir in the southern U.S. ([Truman 2011, PMID 21524213](https://pmc.ncbi.nlm.nih.gov/articles/PMC3138484)); **red squirrel** (*Sciurus vulgaris*) in the British Isles ([Avanzi 2016, PMID 27846605](https://pubmed.ncbi.nlm.nih.gov/27846605)). *(NCBI Taxon IDs for these hosts not re-queried this session.)*
- **Natural disease/comparative pathology:** armadillos develop **extensive neurological involvement**, uniquely among lab animals, with bacilli on progressively demyelinating Schwann cells and electrophysiologically demonstrable nerve deficits — making them the premier model of leprosy **neuropathy** (Sharma R, …, Truman R, *Dis Model Mech* 2013 "The armadillo: a model for the neuropathy of leprosy") ([DMM dmm.010215](https://cob.silverchair.com/dmm/article-pdf/doi/10.1242/dmm.010215/2032116/dmm_010215.pdf)); red squirrels show both overt and subclinical infection ([Avanzi 2016](https://pubmed.ncbi.nlm.nih.gov/27846605)).
- **Transmission/zoonosis:** direct armadillo→human zoonotic transmission is supported by near-identical whole genomes; ~⅓ of U.S. patients report no foreign residence ([Truman 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3138484)). Squirrel→human risk is considered low ([EPFL/press coverage of Avanzi 2016](https://news.epfl.ch/news/red-squirrels-in-the-british-isles-are-infected-wi)).
- **Evolutionary note:** British *M. leprae* strains resemble medieval European strains; British/Irish *M. lepromatosis* diverged from Mexican human strains ~27,000 years ago ([Avanzi 2016](https://pubmed.ncbi.nlm.nih.gov/27846605)).

---

## 15. Model Organisms

- **Mouse footpad (Shepard, 1960):** *M. leprae* replicates in the mouse footpad but infection stays **localized without nerve involvement** — the standard model for drug-susceptibility/viability testing, not neuropathy ([DMM 2013 review](https://cob.silverchair.com/dmm/article-pdf/doi/10.1242/dmm.010215/2032116/dmm_010215.pdf)). Nude/immunodeficient mice support higher bacterial yields.
- **Nine-banded armadillo:** the key model recapitulating **disseminated multibacillary disease and peripheral neuropathy**; used for antigen/bacillus production, pathogenesis, and nerve-function-impairment intervention studies ([DMM 2013](https://cob.silverchair.com/dmm/article-pdf/doi/10.1242/dmm.010215/2032116/dmm_010215.pdf); [armadillo NFI model, PMC9259846](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9259846/)). Limitations: outbred, long timelines, limited genetic tools, no inbred reagents.
- **Zebrafish (*Danio rerio*) larvae:** transparent model used to show, in vivo, that **infected macrophages (via PGL-1 → iNOS/NO) initiate demyelination**, enabling real-time imaging of nerve damage ([Madigan 2017, PMC5848073](https://pmc.ncbi.nlm.nih.gov/articles/PMC5848073); [ZFIN ZDB-PUB-170827-7](https://zfin.org/ZDB-PUB-170827-7)).
- **In vitro / primary cells:** human primary **Schwann cells** (ErbB2 demyelination model, Herceptin/PKI-166 blockade; [Nat Med 2006](https://www.nature.com/articles/nm1433.pdf)); **Schwann-cell reprogramming to pSLCs** ([Cell 2013](https://www.nature.com/articles/nature.2013.12239)); **monocyte-derived macrophages** for IL-10/IL-15 program divergence ([Montoya 2009](https://www.pubmed.gov/19837374/)); human lesion **single-cell + spatial transcriptomics** defining the granuloma antimicrobial network and reversal reaction (Ma et al., *Nat Immunol* 2021; 21,318 cells/10 biopsies; [DOI 10.1038/s41590-021-00956-8](https://www.nature.com/articles/s41590-021-00956-8)).
- **Phenotype recapitulation summary:** armadillo = best for systemic + neural LL phenotype; mouse footpad = bacillary viability/drug testing only; zebrafish = early macrophage-driven nerve injury mechanism; human lesion omics = authentic immunologic poles.
- **Resources:** MGI (mouse), ZFIN (zebrafish); no dedicated armadillo genetic-model database (natural-host colonies at NHDP/USA).

---

## Summary of key evidence gaps (not retrievable this session)
- LL-specific global prevalence and **GBD DALY** figures.
- LL-subtype-stratified **DNA-methylation** data (only whole-leprosy methylome GSE197331 found).
- Original abstracts of **Han 2008** (*M. lepromatosis*), **Ridley–Jopling 1966**, and **Masaki 2013** — reported via citing/secondary sources and flagged as such.
- Exact **ICD-11 subcode** and re-verified **NCBI Taxon IDs** for host species.

---

### Consolidated primary-source list (PMIDs/DOIs cited above)
Cole 2001 (PMID 11234002); Mira 2004 (DOI 10.1038/nature02326); Zhang 2009 NEJM (leprosy GWAS); Liu 2015 (Nat Genet ng.3212); Wang 2016 (Nat Commun 13760); Teles 2013 (Science, DOI 10.1126/science.1233665); Yamamura/Modlin/Bloom 1991 (Science 254:277); Montoya 2009 (PMID 19837374); Cruz 2008 (DOI 10.1172/JCI34189); Tapinos/Rambukkana 2006 (Nat Med 12:961); Madigan 2017 (DOI 10.1016/j.cell.2017.07.030); Masaki 2013 (Cell 152:51, via secondary); Ma 2021 (DOI 10.1038/s41590-021-00956-8); Truman 2011 (PMID 21524213); Avanzi 2016 (PMID 27846605); Zhang 2013 HLA-B*13:01 (PMID 24152261); Moet 2008 COLEP (BMJ 336:761); Wang 2023 rifapentine (PMID 37195940); Setia 2006 (PMID 16500597); Walker 2014 ENL mortality (PLoS NTD, PMC3953021); Cambau 2018 (Clin Microbiol Infect, PMC6286419); LepVax 2020 (PMID 31899025); Sharma/Truman 2013 (DMM dmm.010215); Ridley–Jopling 1966 (PMID 5950347, title only).

**Note:** Earlier in this session the drafting of this report was interrupted once by an automated safety classifier; the content above was produced fresh and all factual claims are tied to sources retrieved during this session.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 0 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 34 |
| On topic | 9 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1242/dmm.010215/2032116/dmm_010215.pdf` (4 mentions) - Identifier did not resolve to a record

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMC:PMC8031444`: "protects those who need it least"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 19 |
| Terms whose name was checked | 5 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000460` (1 mention) - the report calls it "abnormal nasal morphology"; HP calls it **Narrow nose**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `DOID:10887` (5 mentions) - the report calls it "synonym "type L leprosy"; DOID calls it **lepromatous leprosy**, and lists "type L leprosy" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002097` - called "skin", "Primary organs:** **skin"

### Terms the ontology service could not be reached for

19 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `HP:0000561` (1 mention)
- `HP:0000763` (1 mention)
- `GO:0032495` (1 mention)
- `GO:0045087` (2 mentions)
- `CL:0000235` (1 mention)
- `CL:0002573` (1 mention)
- `CL:0000084` (1 mention)
- `CL:0000775` (1 mention)
- `GO:0032606` (1 mention)
- `GO:0032623` (1 mention)
- `GO:0002244` (1 mention)
- `GO:0032289` (1 mention)
- `UBERON:0002097` (1 mention)
- `UBERON:0000044` (1 mention)
- `UBERON:0001707` (1 mention)
- `UBERON:0000970` (1 mention)
- `UBERON:0000473` (1 mention)
- `GO:0045335` (1 mention)
- `GO:0005739` (1 mention)

### Terms whose obsolescence could not be checked

2 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0009830` (2 mentions)
- `HP:0000554` (1 mention)