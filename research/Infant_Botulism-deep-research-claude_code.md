---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-26T19:02:42.242166'
end_time: '2026-11-26T19:07:29.767829'
duration_seconds: 287.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Infant Botulism
  mondo_id: MONDO:0015804
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: infantile botulism; infant intestinal toxemia botulism
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
  web_search_requests: 12
  num_turns: 20
  total_cost_usd: 1.0408457
  session_id: 95b63c37-3a7c-45b6-86ed-3d6d10bc1d64
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 18
  retrieval_calls: 15
  assistant_text_blocks: 4
citation_count: 28
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 9
  validator_version: 0.8.0
term_validation:
  total_terms: 35
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 22
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 4
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CHEBI:38164
    reported_labels:
    - botulinum toxin, if present in ontology; verify
    ontology_label: organic heteropentacyclic compound
  service_unreachable: 21
  obsolescence_unchecked: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infant Botulism
- **MONDO ID:** MONDO:0015804 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** infantile botulism; infant intestinal toxemia botulism
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Infant Botulism** covering all of the
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

Bash is unavailable; switching to WebSearch.

I have substantial material. Let me gather a few remaining specifics with well-formed queries.

Let me verify the mortality figure and get the national treatment-outcome data.

I have enough well-sourced material to write the report. One interpretive note first: the template lists "Causal gene(s): not recorded" and asks me to name the causal gene — **infant botulism has no human causal gene.** It is an acquired infectious/toxin-mediated disease (MONDO:0015804), so I state that explicitly and treat gene-centric sections as not applicable, redirecting to the relevant bacterial toxin genes (*bont/A*, *bont/B*). I prioritized retrieval; every specific claim below carries the source I retrieved it from, and I flag where I could not retrieve support.

---

# Comprehensive Research Report: Infant Botulism (MONDO:0015804)

## Interpretation and scope note

**Infant botulism is not a Mendelian/genetic disorder and has no human causal gene** — the template's "Causal gene(s): not recorded" is correct and reflects the disease's true nature. It is an **acquired, infectious, toxin-mediated disease**: *Clostridium botulinum* (or, rarely, neurotoxigenic *C. baratii* or *C. butyricum*) colonizes the infant large intestine and produces botulinum neurotoxin *in situ*, which is absorbed and causes the illness. The only "genes" relevant to causation are the **bacterial neurotoxin genes (*bont/A*, *bont/B*, and rarely *bont/E*, *bont/F*)**, discussed in Section 4. Sections of this template that presuppose a human germline/somatic genetic etiology (causal genes, pathogenic variants, inheritance pattern, penetrance, model-organism knockouts, etc.) are therefore **marked Not Applicable**, with the infectious-disease analog provided where one exists. This interpretation is stated here so the knowledge-base entry is not mistakenly populated with human gene annotations.

A note on evidence quality: much of the foundational epidemiology and mechanism literature on this disease is from the 1970s–1990s, and I was able to retrieve several of those only as citations, not as retrievable abstracts. Where I give a specific number from a source I actually retrieved, I cite it; where a figure is "commonly cited" but I could not retrieve primary support in this session, I say so explicitly.

---

## 1. Disease Information

**Overview.** Infant botulism is an acute, potentially life-threatening flaccid paralytic illness of infants (classically 1–12 months old; cases defined as occurring from ~28 days to 1 year of life per NORD) caused by intestinal colonization with toxigenic clostridia and in-vivo production and absorption of botulinum neurotoxin. It is a form of "intestinal toxemia botulism" — unlike foodborne botulism, preformed toxin is not ingested; rather, spores are ingested, germinate, and produce toxin in the gut lumen. The CDC describes the hallmark as **"progressive muscle weakness, beginning with muscles controlled by the cranial nerves"** followed by symmetric, descending, flaccid paralysis ([CDC Clinical Overview of Infant Botulism](https://www.cdc.gov/botulism/hcp/clinical-overview/infant-botulism.html)). It is the most common form of human botulism in the United States ([CDC National Botulism Surveillance](https://www.cdc.gov/botulism/php/national-botulism-surveillance/2021.html)).

**Key identifiers.**
- **MONDO:** MONDO:0015804 (as given)
- **Orphanet:** ORPHA:178478 ("Infant botulism"); the general-botulism parent is ORPHA:1267 (per a Qeios Orphanet-citing definition, [Qeios](https://www.qeios.com/read/UDPO2E/pdf)) — I was not able to open the Orphanet record directly in this session to confirm.
- **ICD-10-CM:** **A48.51** "Infant botulism" (a distinct billable code, [ICD-10-CM A48.51](https://www.unboundmedicine.com/icd/view/ICD-10-CM/881535/all/A48_51___Infant_botulism)). Note: some Orphanet-derived mirrors map botulism to the general code **A05.1** ("Botulism food poisoning"); A48.51 is the infant-specific code and is the one to prefer ([mirror listing](https://iegext02.helmholtz-munich.de/phenodis/disease/show/1410)).
- **ICD-11:** botulism is coded under "1C13" (bacterial intestinal/foodborne — I could not retrieve the exact infant subcode in this session; verify before populating).
- **MeSH:** "Botulism" (D001906); there is no separate MeSH descriptor for infant botulism (it is indexed under Botulism). *Not retrieved directly this session — verify.*
- **MedGen:** CUI referenced at [MedGen 14204](https://https.ncbi.nlm.nih.gov/medgen/14204) (not opened this session).

**Synonyms / alternative names.** Infantile botulism; infant intestinal toxemia botulism; intestinal botulism (infant form). The provided synonyms are consistent with usage in the literature.

**Information source type.** This entry is populated almost entirely from **aggregated disease-level resources** (CDC national surveillance, review articles, a randomized controlled trial, and case series), not individual EHR-derived patient data.

---

## 2. Etiology

**Primary causal factor (infectious/toxin-mediated).** The disease is caused by **ingestion of spores of neurotoxigenic clostridia → germination and transient colonization of the infant colon → in-situ production of botulinum neurotoxin → absorption → systemic cholinergic blockade.** The responsible organism is usually *Clostridium botulinum* producing toxin type A or type B; rarely *C. baratii* (type F) or *C. butyricum* (type E) ([Hall/Aureli-type findings summarized via case literature](https://pubmed.ncbi.nlm.nih.gov/15730901/); [CDC surveillance 2021](https://www.cdc.gov/botulism/php/national-botulism-surveillance/2021.html)). A 2024 review states **"honey is the most well-known risk factor for infant botulism"** and that *C. botulinum* was found in **42/587 (7%)** of U.S. honey samples across nine surveys ([2024 review, PMID 39138824 / Springer](https://link.springer.com/article/10.1007/s00284-024-03828-0)).

**Risk factors — environmental/host.**
- **Honey ingestion** — the classic, avoidable dietary risk factor; the basis for the universal recommendation not to feed honey to infants <12 months ([2024 review, PMID 39138824](https://link.springer.com/article/10.1007/s00284-024-03828-0); [UF/IFAS "Infant Botulism and Honey"](https://ask.ifas.ufl.edu/pdf/AA/AA14200.pdf)).
- **Environmental spore exposure / soil & dust.** In an Israeli case series (2007–2021, 8 cases), **6/8** had possible environmental exposures (living near rural/construction areas, dust exposure, father working as a farmer), while honey was reported in only **1/8** ([Israeli series, PMID 36692296](https://pmc.ncbi.nlm.nih.gov/articles/pmid/36692296)). This illustrates that in many regions soil/dust exposure, not honey, dominates.
- **Age.** Peak susceptibility is ~**3–5 months**, coinciding with post-weaning gut-microbiota changes ([2024 review, PMID 39138824](https://link.springer.com/article/10.1007/s00284-024-03828-0)).
- **Breastfeeding/feeding transitions** — included among risk factors in the large 1976–1983 U.S. case-control study (see Protective Factors; the role is debated).
- **Geography** — regional soil spore load (notably high in parts of California, Utah, Pennsylvania).

**Genetic risk factors.** **Not applicable** — no human susceptibility locus, modifier gene, or causal variant is established for infant botulism. (No GWAS/ClinVar/ClinGen entry applies.)

**Protective factors.**
- **A mature/competitive gut microbiota** is the central protective factor: the disease window corresponds to the period when the infant gut flora is immature and cannot competitively exclude *C. botulinum*. Germ-free and limited-flora mouse work (Moberg & Sugiyama; Wells, Sugiyama & Bland) showed that a full/defined adult flora reduces or prevents colonization — **"these floras did not prevent infection … however, death rates among the mice with defined floras were significantly lower than those among germfree mice"** ([Microbial ecological basis of infant botulism, PMID 385503](https://pubmed.ncbi.nlm.nih.gov/385503)).
- **Breast milk / breastfeeding** — historically proposed as protective against fulminant/sudden death (Arnon et al., *J Pediatr* 1982, "Protective role of human milk against sudden death from infant botulism," cited in [infantbotulism.org](https://infantbotulism.org/parent/prevention.php)); however the role is **contested** — breastfeeding also appears as a risk factor in the 1976–1983 case-control study, and the net effect (possibly slowing onset, allowing earlier hospitalization) remains unsettled ([infantbotulism.org prevention page](https://infantbotulism.org/parent/prevention.php)). *I could not retrieve the 1982 paper's abstract directly; this rests on the citing sources.*
- **Genetic protective factors:** **Not applicable.**

**Gene–environment interactions.** **Not applicable** in the human-genetic sense. The analogous interaction is **host-microbiome × environmental spore exposure × age**: the same spore dose produces disease only during the narrow developmental window of microbiota immaturity, directly demonstrated by age-dependent susceptibility in suckling mice (resistant <7 days or >15 days; susceptible 8–11 days) ([PMID 385503](https://pubmed.ncbi.nlm.nih.gov/385503)).

---

## 3. Phenotypes

Evidence source: human clinical case series and reviews. Frequencies below are from a presenting-signs table summarized in clinical references and the 2002 AAFP review ([AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html)) and Merck/MSD ([Merck Manual](https://www.merckmanuals.com/professional/infectious-diseases/anaerobic-bacteria/infant-botulism)).

| Phenotype | Type | Frequency | Suggested HPO |
|---|---|---|---|
| Constipation (often the first sign, may precede weakness by weeks) | Symptom/sign (GI/autonomic) | ~**90%** initially (Merck); ~65% as presenting sign in one table | HP:0002019 Constipation |
| Generalized weakness / "floppiness" (hypotonia) | Clinical sign | ~**88%** | HP:0001290 Generalized hypotonia; HP:0003808 Abnormal muscle tone |
| Poor feeding / poor suck | Symptom/sign | ~**79%** | HP:0011968 Feeding difficulties; HP:0002033 Poor suck |
| Lethargy | Symptom/sign | ~**60%** | HP:0001254 Lethargy |
| Weak/altered cry | Clinical sign | ~**18%** (as presenting) | HP:0001612 Weak cry |
| Respiratory difficulty / respiratory failure (late) | Clinical sign | ~**11%** at presentation; up to **~50–70%** eventually require ventilation | HP:0002093 Respiratory insufficiency; HP:0002878 Respiratory failure |
| Ptosis | Clinical sign (cranial nerve) | common on exam | HP:0000508 Ptosis |
| Facial weakness | Clinical sign | common | HP:0010628 Facial palsy |
| Reduced/absent gag reflex | Clinical sign | common | HP:0030906 Reduced gag reflex |
| Poor head control | Clinical sign | common | HP:0002421 Poor head control |
| Hyporeflexia/areflexia (reduced muscle stretch reflexes) | Clinical sign | common | HP:0001265 Hyporeflexia |
| Ophthalmoplegia / sluggish pupils | Clinical sign (autonomic/cranial) | variable | HP:0000602 Ophthalmoplegia |

Supporting quote (CDC): the hallmark is **"progressive muscle weakness, beginning with muscles controlled by the cranial nerves,"** with paralysis that is **symmetric, descending, and flaccid** ([CDC Clinical Overview](https://www.cdc.gov/botulism/hcp/clinical-overview/infant-botulism.html)).

**Characteristics.**
- **Age of onset:** infancy, peak ~3–5 months ([PMID 39138824](https://link.springer.com/article/10.1007/s00284-024-03828-0)); a type F case presented as early as 54 hours of life ([PMID 15730901](https://pubmed.ncbi.nlm.nih.gov/15730901/)).
- **Severity:** variable — **"from mild lethargy and slowed feeding to severe hypotonia and respiratory insufficiency"** ([Merck Manual](https://www.merckmanuals.com/professional/infectious-diseases/anaerobic-bacteria/infant-botulism)).
- **Progression:** acute-to-subacute, **descending** and symmetric; typically progressive over days then plateau, then slow recovery (self-limited once motor endplates regenerate).
- **Quality of life:** acute illness imposes prolonged hospitalization (mean untreated ~5.7 weeks, see §12) and often mechanical ventilation; most survivors recover fully, though residual neck weakness during convalescence is noted ([CDC](https://www.cdc.gov/botulism/hcp/clinical-overview/infant-botulism.html)). I did not retrieve a formal EQ-5D/PROMIS dataset — none is standard for this acute pediatric disease.

---

## 4. Genetic / Molecular Information

**Human causal genes: Not applicable.** No human gene, pathogenic variant, modifier gene, chromosomal abnormality, or disease-specific epigenetic signature is established. gnomAD/ClinVar/HGMD/DECIPHER queries are not relevant.

**Relevant molecular agent — the bacterial neurotoxin genes.** The causative molecule is **botulinum neurotoxin (BoNT)**, a ~150 kDa di-chain protein (100 kDa heavy chain + 50 kDa light chain joined by a disulfide bond), encoded by *bont* genes carried on the clostridial genome/phage/plasmid:
- ***bont/A*** → toxin type A (most common serotype in U.S. infant cases some years)
- ***bont/B*** → toxin type B (predominant in several recent U.S. years)
- ***bont/E*** (often in *C. butyricum*) and ***bont/F*** (often in *C. baratii*) → rare infant cases ([case literature, PMID 15730901](https://pubmed.ncbi.nlm.nih.gov/15730901/); [2024 review PMID 39138824](https://link.springer.com/article/10.1007/s00284-024-03828-0)).

**Toxin-target molecular specificity (functional consequence).** Each serotype's light chain is a **zinc-dependent metalloprotease** cleaving a specific SNARE protein: **types A, C, E cleave SNAP-25; types B, D, F, G cleave synaptobrevin (VAMP); type C additionally cleaves syntaxin** ([mechanism review, PMID 10865130](https://pubmed.ncbi.nlm.nih.gov/10865130/); figure legend summarized in [toxin reviews](https://pmc.ncbi.nlm.nih.gov/articles/PMC6070880)). Classic demonstration: **"BoNT/B inhibited acetylcholine release by proteolytic cleavage of synaptobrevin between E76 and F77"** (Schiavo et al., summarized in [PMID 10865130](https://pubmed.ncbi.nlm.nih.gov/10865130/)).

Suggested CHEBI: CHEBI:38164 (botulinum toxin, if present in ontology; verify). Suggested protein targets (human genes affected functionally by the toxin, not mutated): **SNAP25** (HGNC:11132), **VAMP1/VAMP2** (synaptobrevin), **STX1A** (syntaxin).

---

## 5. Environmental Information

- **Environmental factors:** soil- and dust-borne *C. botulinum* spores; **honey** as a recognized vehicle (7% of U.S. honey samples positive, [PMID 39138824](https://link.springer.com/article/10.1007/s00284-024-03828-0)). Proximity to agricultural/construction/soil-disturbance areas associated with cases ([Israeli series, PMID 36692296](https://pmc.ncbi.nlm.nih.gov/articles/pmid/36692296)).
- **Lifestyle/feeding factors:** honey feeding; feeding/weaning transitions altering gut flora.
- **Infectious agent (CHEBI/NCBI Taxonomy):**
  - *Clostridium botulinum* — **NCBI:txid1491** (anaerobic, spore-forming, Gram-positive rod).
  - *Clostridium baratii* — **NCBI:txid1561** (rare type F infant cases).
  - *Clostridium butyricum* — **NCBI:txid1492** (rare type E infant cases).
  *(Taxon IDs from standard NCBI assignments; I was not able to open the NCBI Taxonomy records in this session — verify the exact txids before populating.)*
  The non-*botulinum* species association was established when **"two unusual neurotoxigenic clostridia isolated from fecal specimens from patients with type F and type E infant botulism"** were identified as *C. baratii* and *C. butyricum* ([case/strain literature summarized](https://pubmed.ncbi.nlm.nih.gov/15730901/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating event → clinical manifestation)

1. **Ingestion of clostridial spores** (from honey, soil, or dust) → spores reach the infant large intestine. *(Demonstrated epidemiologically; [PMID 39138824](https://link.springer.com/article/10.1007/s00284-024-03828-0).)*
2. Because the **infant gut microbiota is immature** (peak vulnerability 3–5 months), the normal competitive exclusion is absent → **spores germinate and the organism transiently colonizes the colon.** *(Demonstrated in germ-free/age-restricted mouse models; [PMID 385503](https://pubmed.ncbi.nlm.nih.gov/385503).)*
3. Vegetative *C. botulinum* **produces botulinum neurotoxin in situ** in the gut lumen (intestinal toxemia) → **toxin is absorbed** across the intestinal epithelium into the circulation. *(Mechanistically inferred from toxemia model; directly supported by detectable gut toxin in mouse models, [PMID 385503](https://pubmed.ncbi.nlm.nih.gov/385503).)*
4. Circulating BoNT **binds presynaptic receptors at peripheral cholinergic nerve terminals** (neuromuscular junctions and autonomic ganglia) via its heavy-chain binding domain → receptor-mediated **endocytosis** into the terminal. *(Demonstrated; [Winner/Bodt/McNutt review, PMID 33218099](https://pubmed.ncbi.nlm.nih.gov/33218099).)*
5. The **light chain translocates into the cytosol** and acts as a **Zn²⁺-metalloprotease**, cleaving a SNARE protein — **SNAP-25 (types A/E) or synaptobrevin/VAMP (type B/F)**. *(Demonstrated; [PMID 10865130](https://pubmed.ncbi.nlm.nih.gov/10865130/).)*
6. SNARE cleavage **blocks Ca²⁺-triggered synaptic-vesicle fusion** → **acetylcholine release is prevented**: **"BoNT cleavage prevents interaction of the T-SNARE and V-SNARE, preventing acetylcholine release"** ([toxin review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6070880)).
7. Loss of cholinergic transmission at the NMJ → **flaccid muscle paralysis**; loss at autonomic cholinergic synapses → **autonomic signs (constipation, poor pupillary response, reduced secretions).** Branch: cranial-nerve-innervated muscles affected first (clinically the descending pattern).
8. Progressive involvement of bulbar and then respiratory musculature → **respiratory insufficiency/failure** (the main life threat).
9. **Recovery** occurs only as the toxin is cleared and **new motor nerve terminals/endplates sprout and regenerate** — hence slow, spontaneous recovery over weeks: **"spontaneous recovery … once new motor endplates are regenerated"** ([AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html)).

### Checklist detail
- **Molecular pathway:** SNARE-mediated synaptic vesicle exocytosis (Reactome "Neurotransmitter release cycle"). The lesion is proteolytic disassembly of the SNARE fusion machinery.
- **Cellular process:** blockade of regulated exocytosis / neurotransmitter release; no cell death — paralysis is functional and reversible.
- **Protein dysfunction:** irreversible proteolytic cleavage (loss of function) of SNAP-25 or VAMP; toxin light chain is a gain-of-(enzymatic)-function protease.
- **Immune involvement:** minimal/none directly; infants mount little antibody to the small toxin dose — rationale for passive immunotherapy (BIG-IV).
- **Upstream vs downstream:** colonization + toxin production (upstream) → SNARE cleavage (central) → paralysis/respiratory failure (downstream).

**Suggested GO terms:** GO:0017158 (regulation of calcium-ion-dependent exocytosis), GO:0007269 (neurotransmitter secretion), GO:0016079 (synaptic vesicle exocytosis), GO:0008237 (metallopeptidase activity). **Suggested CL terms:** CL:0000100 (motor neuron), CL:0002305/skeletal muscle cell targets, CL:0000617 (GABAergic not relevant) — key effector cell is the **cholinergic motor neuron terminal**.

---

## 7. Anatomical Structures Affected

- **Organ/system level:** **Peripheral nervous system** — presynaptic cholinergic nerve terminals (primary). **Respiratory system** (secondary, via diaphragm/intercostal paralysis). **Gastrointestinal/autonomic** (constipation, ileus). **Skeletal muscle** (target of denervation, not primarily injured).
- **Tissue/cell level:** **neuromuscular junction** (motor endplate), **autonomic ganglionic cholinergic synapses**. Targeted cell: **motor neuron presynaptic terminal (cholinergic)** — suggested CL:0000100 (motor neuron). The toxin is produced in the **colonic lumen** (large intestine epithelium is the absorption site).
- **Subcellular level:** **presynaptic cytosol / synaptic-vesicle membrane and plasma-membrane SNARE complex** (GO cellular component GO:0031201 SNARE complex; GO:0008021 synaptic vesicle; GO:0042734 presynaptic membrane).
- **Localization (UBERON):** neuromuscular junction (UBERON:0002409 / GO:0031594 neuromuscular junction), skeletal muscle tissue (UBERON:0001134), large intestine/colon (UBERON:0001155) as colonization site, diaphragm (UBERON:0001103).
- **Lateralization:** **symmetric/bilateral** descending paralysis ([CDC](https://www.cdc.gov/botulism/hcp/clinical-overview/infant-botulism.html)).

---

## 8. Temporal Development

- **Onset:** infancy, peak ~3–5 months ([PMID 39138824](https://link.springer.com/article/10.1007/s00284-024-03828-0)); onset pattern typically **subacute** — constipation first, sometimes **preceding weakness by days to weeks**, then progressive descending weakness over days.
- **Progression/stages:** (early) constipation/feeding decline → (intermediate) cranial-nerve palsies, hypotonia → (advanced) generalized flaccid paralysis ± respiratory failure → (recovery) gradual improvement.
- **Course:** **self-limited but prolonged**; recovery requires motor-endplate regeneration. In an Israeli series, median time to resolution was **75 days (range 16–180)** ([PMID 36692296](https://pmc.ncbi.nlm.nih.gov/articles/pmid/36692296)).
- **Duration:** acute illness/hospitalization measured in **weeks** (mean untreated ~5.7 weeks; ~2.2–2.6 weeks with early BIG-IV, see §12) ([Arnon 2006, PMID 16452558](https://pubmed.ncbi.nlm.nih.gov/16452558/); [Payne 2018, PMID 29229452](https://pubmed.ncbi.nlm.nih.gov/29229452/)).
- **Remission:** spontaneous (toxin clearance + reinnervation); treatment accelerates recovery but does not change the fundamental self-limited biology.
- **Critical window for intervention:** early — the benefit of BIG-IV is **time-dependent**: treatment on hospital days 0–3 reduced mean length of stay by **3.7 weeks**, vs **2.6 weeks** on days 4–7 ([Payne 2018, PMID 29229452](https://pubmed.ncbi.nlm.nih.gov/29229452/)).

---

## 9. Inheritance and Population

- **Inheritance:** **Not applicable** — acquired infectious disease, not heritable. Penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, carrier frequency: all **Not Applicable**.
- **Epidemiology (U.S., CDC surveillance):**
  - Infant botulism is the **most common form of human botulism in the U.S.** In 2021, **181 laboratory-confirmed infant cases** were reported — the highest annual count since the disease was characterized in 1976; toxin **type B = 107 (59%), type A = 72 (40%)**, with rare Ba/Bf ([CDC 2021](https://www.cdc.gov/botulism/php/national-botulism-surveillance/2021.html)).
  - 2020: **159** infant cases, ~70% of all U.S. botulism that year ([CDC 2020](https://www.cdc.gov/botulism/php/national-botulism-surveillance/2020.html)).
  - 2019: **152** cases ([CDC 2019](https://www.cdc.gov/botulism/surv/2019/index.html)).
  - 2018: **162** infant cases (67% of botulism) ([CDC 2018](https://www.cdc.gov/botulism/surv/2018/index.html)).
  - 2017: infant toxin types A=52 (37%), B=88 (62%), Ba=1 ([CDC 2017](https://www.cdc.gov/botulism/php/national-botulism-surveillance/2017.html)).
  - Approximate recent annual range: **~140–180 cases/yr** in the U.S.
- **Geographic distribution:** clusters in high-spore-soil states (California, Utah, Pennsylvania historically); California reports the most cases ([CDC 2017](https://www.cdc.gov/botulism/php/national-botulism-surveillance/2017.html)). Serotype A tends to predominate west of the Mississippi, B to the east (classic pattern — not re-verified this session).
- **Sex ratio / age:** disease of infancy (≤1 year), peak 3–5 months; no strong sex predilection established in retrieved sources.

---

## 10. Diagnostics

- **Clinical diagnosis is primary** — treatment should not await laboratory confirmation: **"Treatment of infant botulism is started as soon as the diagnosis is suspected; waiting for confirmatory test results … is dangerous"** ([AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html); [CDC](https://www.cdc.gov/botulism/hcp/clinical-overview/infant-botulism.html)).
- **Laboratory confirmation:** **"Confirmation requires both a stool culture and a direct toxin assay. The toxin assay may be performed on stool, serum, or gastric contents"** ([AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html)). Stool culture sensitivity ~**60%** ([AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html)).
- **Gold-standard toxin detection:** **mouse inoculation/lethality bioassay** performed by CDC/state labs — described as "the most reliable diagnostic test" ([AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html)); positive in **7/8** tested patients in the Israeli series ([PMID 36692296](https://pmc.ncbi.nlm.nih.gov/articles/pmid/36692296)).
- **Electrophysiology:** EMG can support early diagnosis; in botulism the characteristic finding is a facilitating (incremental) response to repetitive high-frequency nerve stimulation and brief, small-amplitude, abundant motor unit potentials ("BSAP"). EMG was positive in **3/4** tested in the Israeli series ([PMID 36692296](https://pmc.ncbi.nlm.nih.gov/articles/pmid/36692296)). *(The specific incremental-response pattern is classic teaching; I did not retrieve a primary electrophysiology paper this session.)*
- **Imaging:** no diagnostic role; used to exclude differentials.
- **Omics/liquid biopsy:** not applicable clinically.
- **Differential diagnosis:** sepsis, meningoencephalitis, spinal muscular atrophy, congenital muscular dystrophy, hypothyroidism, benign congenital hypotonia, myasthenia gravis, Guillain–Barré/metabolic disease ([Merck Manual](https://www.merckmanuals.com/professional/infectious-diseases/anaerobic-bacteria/infant-botulism)). Infants are **often initially misdiagnosed as sepsis or meningoencephalitis** ([AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html)).
- **Screening:** no population screening; honey avoidance is the main preventive counseling. Genetic/newborn screening: **Not applicable.**
- Suggested LOINC: use toxin-assay and culture LOINC codes (not retrieved specifically).

---

## 11. Outcome / Prognosis

- **Mortality:** generally reported as **very low (<1% of hospitalized U.S. cases)** in the broader literature — **I could not retrieve a primary source confirming the exact <1% figure in this session**, so this should be verified against a CDC surveillance summary or the 2021 MMWR guidelines before populating. Retrieved sources confirm the illness is "potentially life-threatening" but survivable with modern supportive care ([MedlinePlus](https://medlineplus.gov/ency/article/001384.htm)).
- **Recovery:** typically **complete**; **"Neurologic sequelae are seldom seen"** ([AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html)). Transient residual neck weakness during convalescence is noted ([CDC](https://www.cdc.gov/botulism/hcp/clinical-overview/infant-botulism.html)).
- **Morbidity:** major morbidity is prolonged hospitalization and the need for mechanical ventilation: **"more than 70 percent of these infants will eventually require mechanical ventilation"** (2002 review; [AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html)); a StatPearls-type source puts intubation at **~50% regardless of BIG-IV** ([StatPearls](https://www.statpearls.com/point-of-care/23473)). Median time to resolution 75 days (16–180) in one series ([PMID 36692296](https://pmc.ncbi.nlm.nih.gov/articles/pmid/36692296)).
- **Prognostic factors:** **time to BIG-IV administration** is the key modifiable prognostic factor (earlier = shorter stay, [Payne 2018, PMID 29229452](https://pubmed.ncbi.nlm.nih.gov/29229452/)); toxin type and severity at presentation also matter.

---

## 12. Treatment

- **Specific therapy — Human Botulism Immune Globulin Intravenous (BIG-IV, "BabyBIG").** FDA-licensed in **2003** ([CIDRAP](https://www.cidrap.umn.edu/botulism/antitoxin-infant-botulism-slashes-hospital-stays)). Single IV dose over 30 minutes; human-derived neutralizing antibody against toxin types A and B. Pivotal RCT (Arnon et al., *NEJM* 2006; 5-year double-blind placebo-controlled California trial): BIG-IV reduced **mean hospital stay from 5.7 to 2.6 weeks** (primary outcome); early open-label treatment → 2.2 weeks; **"Prompt treatment of infant botulism type A or type B with BIG-IV was safe and effective"** ([Arnon 2006, PMID 16452558](https://pubmed.ncbi.nlm.nih.gov/16452558/)).
- **Post-licensure effectiveness (first 12 years):** BIG-IV treated **~93%** of U.S. lab-confirmed infant botulism patients since 2003; reduced mean length of stay from 5.7 → 2.2 weeks; time-dependent benefit (days 0–3: −3.7 wk; days 4–7: −2.6 wk); mean reduction in hospital charges **~$88,900/patient** ([Payne 2018, J Pediatr, PMID 29229452](https://pubmed.ncbi.nlm.nih.gov/29229452/)). Suggested NCIT: botulism immune globulin / immunoglobulin therapy.
- **Supportive care (mainstay):** meticulous **respiratory support** (including mechanical ventilation in ~50–70% of cases) and **nutritional support** (NG/enteral feeding) until reinnervation ([AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html); [StatPearls](https://www.statpearls.com/point-of-care/23473)). NCIT: respiratory support, enteral nutrition.
- **Drugs to AVOID:** **aminoglycoside antibiotics** — they potentiate neuromuscular blockade: **"Aminoglycosides should be strictly avoided, as these medications can exacerbate neuromuscular weakness"** ([StatPearls](https://www.statpearls.com/point-of-care/23473)). Antibiotics are generally not used to treat the gut colonization (lysis could release more toxin) except for concurrent infections.
- **Not indicated:** equine botulinum antitoxin (used for adult/foodborne botulism) is generally not used for infants given BIG-IV availability and serum-sickness risk.
- **Pharmacogenomics / gene / cell / RNA / targeted / immunotherapy (checkpoint):** **Not applicable.**
- **Clinical trial identifier:** the original BIG-IV study is registered as [NCT00004401](https://clinicaltrials.gov/study/NCT00004401).

---

## 13. Prevention

- **Primary prevention:** **avoid feeding honey to infants <12 months** — the single actionable dietary measure ([UF/IFAS](https://ask.ifas.ufl.edu/pdf/AA/AA14200.pdf); [2024 review PMID 39138824](https://link.springer.com/article/10.1007/s00284-024-03828-0); [CDC](https://www.cdc.gov/botulism/hcp/clinical-overview/infant-botulism.html)). Reducing exposure to disturbed soil/dust is suggested but hard to implement.
- **Secondary prevention:** early clinical recognition and prompt BIG-IV (treat on suspicion); 24/7 consultation via the California Department of Public Health **Infant Botulism Treatment and Prevention Program (510-231-7600)** ([CDPH/IBTPP](https://infantbotulism.org/parent/prevention.php)).
- **Tertiary prevention:** aggressive respiratory/nutritional support to prevent aspiration, ventilator-associated complications, and nosocomial infection.
- **Immunization:** **no vaccine** is available or recommended for infant botulism.
- **Genetic screening / carrier screening / counseling:** **Not applicable** (non-genetic disease).
- **Public health:** honey-labeling warnings; surveillance by CDC/state health departments.

---

## 14. Other Species / Natural Disease

- **Causative organisms (NCBI Taxonomy):** *Clostridium botulinum* (**txid1491**), *C. baratii* (**txid1561**), *C. butyricum* (**txid1492**) — *verify txids against NCBI Taxonomy before populating.*
- **Natural disease in animals:** An analogous **intestinal toxico-infectious (toxemic) botulism** occurs naturally in animals — classically **"toxico-infectious botulism" / shaker foal syndrome in foals** (an equine intestinal-colonization form of botulism analogous to human infant botulism), and gut-colonization botulism in poultry and other species. *This analogy is well established in veterinary medicine but I did not retrieve an OMIA/primary source in this session — flag for verification.*
- **Comparative biology / models:** the germ-free and conventional **suckling-mouse and infant-rat models** directly recapitulate the age- and microbiota-dependent intestinal colonization central to the human disease ([Moberg & Sugiyama, PMID 385503](https://pubmed.ncbi.nlm.nih.gov/385503); rat comparability noted in the same body of work).
- **Zoonotic potential:** not a zoonosis in the person-to-person or animal-to-person transmissible sense; shared environmental spore source rather than cross-infection.

---

## 15. Model Organisms

- **Primary model — the infant/germ-free mouse model of intestinal colonization** (Sugiyama group): germ-free and age-controlled mice reproduce the key feature that only developmentally/microbiota-susceptible animals can be colonized. Findings: **"intestinal monoassociation could not be developed in germfree infant mice younger than 7 days"**; in conventional suckling mice, animals **<7 or >15 days were resistant, while toxin was detected in the intestine of mice challenged at 8–11 days"** ([PMID 385503](https://pubmed.ncbi.nlm.nih.gov/385503)). Defined-flora mice: adult flora reduced death rates and, when complete, prevented infection at 10⁵-spore challenge ([Wells, Sugiyama & Bland, summarized](https://pubmed.ncbi.nlm.nih.gov/385503)).
- **Infant-rat model:** susceptibility comparable to mice (Moberg & Sugiyama).
- **Phenotype recapitulation:** models reproduce the **microbiota-dependent, age-restricted colonization** and in-gut toxin production (the defining pathophysiology), making them excellent for studying colonization resistance; they are **less used** for the paralytic/neuromuscular endpoint, which is studied with purified toxin in standard neuromuscular/mouse-bioassay systems.
- **Limitations:** the narrow mouse susceptibility window and species differences in gut flora limit direct translation; models emphasize the ecological (colonization) arm rather than human-equivalent clinical course.
- **Genetic/knockout models:** **Not applicable** (no human causal gene); relevant genetic tools instead target the bacterial *bont* genes or host SNARE proteins in neuromuscular toxin-mechanism studies.
- **Resources:** organism records in NCBI Taxonomy; no MGI/ZFIN disease-model allele applies because the disease is not gene-based.

---

## Key citations (PMIDs retrieved this session)
- Arnon SS et al. Human Botulism Immune Globulin for the Treatment of Infant Botulism. *N Engl J Med* 2006;354(5):462–471 — **PMID 16452558** ([link](https://pubmed.ncbi.nlm.nih.gov/16452558/))
- Payne JR et al. Efficacy of Human Botulism Immune Globulin … The First 12 Years Post Licensure. *J Pediatr* 2018 — **PMID 29229452** ([link](https://pubmed.ncbi.nlm.nih.gov/29229452/))
- Rosow LK, Strober JB. Infant botulism: review and clinical update. *Pediatr Neurol* 2015 — **PMID 25882077** ([link](https://pubmed.ncbi.nlm.nih.gov/25882077/))
- Moberg LJ, Sugiyama H. Microbial ecological basis of infant botulism as studied with germfree mice — **PMID 385503** ([link](https://pubmed.ncbi.nlm.nih.gov/385503))
- (mechanism) How botulinum and tetanus neurotoxins block neurotransmitter release — **PMID 10865130** ([link](https://pubmed.ncbi.nlm.nih.gov/10865130/))
- Winner BM, Bodt SML, McNutt PM. BoNT uptake/trafficking review, *Int J Mol Sci* 2020 — **PMID 33218099** ([link](https://pubmed.ncbi.nlm.nih.gov/33218099))
- Israeli infant botulism case series 2007–2021 — **PMID 36692296** ([link](https://pmc.ncbi.nlm.nih.gov/articles/pmid/36692296))
- Infant botulism, type F, presenting at 54 hours of life — **PMID 15730901** ([link](https://pubmed.ncbi.nlm.nih.gov/15730901/))
- 2024 review of infant botulism risk factors — **PMID 39138824** ([Springer](https://link.springer.com/article/10.1007/s00284-024-03828-0))

## Items I flag as unverified / needing direct source confirmation
1. **Case-fatality <1%** — widely cited but not retrieved from a primary source this session.
2. **Exact Orphanet↔ICD mapping** (A48.51 vs A05.1) and **ICD-11 subcode** — confirm on Orphanet and WHO ICD-11.
3. **MeSH descriptor** specifics and **NCBI Taxon IDs** (txid1491/1561/1492) — verify on the source databases.
4. **Arnon 1982 "protective role of human milk"** — rests on citing sources, not the retrieved abstract.
5. **Veterinary analog (shaker foal syndrome / OMIA)** — asserted from domain knowledge, not an OMIA retrieval.

**Sources:**
- [CDC National Botulism Surveillance 2021](https://www.cdc.gov/botulism/php/national-botulism-surveillance/2021.html), [2020](https://www.cdc.gov/botulism/php/national-botulism-surveillance/2020.html), [2019](https://www.cdc.gov/botulism/surv/2019/index.html), [2018](https://www.cdc.gov/botulism/surv/2018/index.html), [2017](https://www.cdc.gov/botulism/php/national-botulism-surveillance/2017.html)
- [CDC Clinical Overview of Infant Botulism](https://www.cdc.gov/botulism/hcp/clinical-overview/infant-botulism.html)
- [AAFP Infant Botulism 2002](https://www.aafp.org/pubs/afp/issues/2002/0401/p1388.html)
- [Merck/MSD Manual — Infant Botulism](https://www.merckmanuals.com/professional/infectious-diseases/anaerobic-bacteria/infant-botulism)
- [StatPearls Infant Botulism](https://www.statpearls.com/point-of-care/23473)
- [CIDRAP — Antitoxin for infant botulism](https://www.cidrap.umn.edu/botulism/antitoxin-infant-botulism-slashes-hospital-stays)
- [NCT00004401](https://clinicaltrials.gov/study/NCT00004401)
- [UF/IFAS — Infant Botulism and Honey](https://ask.ifas.ufl.edu/pdf/AA/AA14200.pdf)
- [Infant Botulism Treatment & Prevention Program](https://infantbotulism.org/parent/prevention.php)
- [MedlinePlus — Infant Botulism](https://medlineplus.gov/ency/article/001384.htm)
- [Qeios Orphanet-citing definition](https://www.qeios.com/read/UDPO2E/pdf), [ICD-10-CM A48.51](https://www.unboundmedicine.com/icd/view/ICD-10-CM/881535/all/A48_51___Infant_botulism)
- PMIDs as listed above.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 22 |
| Terms whose name was checked | 5 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CHEBI:38164` (1 mention) - the report calls it "botulinum toxin, if present in ontology; verify"; CHEBI calls it **organic heteropentacyclic compound**

### Terms the ontology service could not be reached for

21 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:0015804` (3 mentions)
- `ORPHA:178478` (1 mention)
- `ORPHA:1267` (1 mention)
- `HP:0001290` (1 mention)
- `HP:0002033` (1 mention)
- `HP:0001254` (1 mention)
- `HP:0002093` (1 mention)
- `HP:0002878` (1 mention)
- `HP:0030906` (1 mention)
- `HP:0002421` (1 mention)
- `GO:0008237` (1 mention)
- `CL:0002305` (1 mention)
- `CL:0000617` (1 mention)
- `GO:0031201` (1 mention)
- `GO:0008021` (1 mention)
- `GO:0042734` (1 mention)
- `UBERON:0002409` (1 mention)
- `GO:0031594` (1 mention)
- `UBERON:0001134` (1 mention)
- `UBERON:0001155` (1 mention)
- `UBERON:0001103` (1 mention)

### Terms whose obsolescence could not be checked

4 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0003808` (1 mention)
- `HP:0001612` (1 mention)
- `HP:0000602` (1 mention)
- `GO:0016079` (1 mention)