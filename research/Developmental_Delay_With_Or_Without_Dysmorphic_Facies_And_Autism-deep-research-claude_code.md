---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-12T14:10:22.900868'
end_time: '2026-10-12T14:11:43.133393'
duration_seconds: 80.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: developmental delay with or without dysmorphic facies and autism
  mondo_id: ''
  category: ''
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
  num_turns: 8
  total_cost_usd: 0.7478071000000002
  session_id: c5bca049-79dd-565a-9d58-3e2354d3de80
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 6
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 2
  validator_version: 0.3.0
term_validation:
  total_terms: 21
  verified: 20
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0000077
    reported_labels:
    - coarse; prefer a more specific term
    ontology_label: Abnormality of the kidney
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0016573
    ontology_label: obsolete histone acetylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** developmental delay with or without dysmorphic facies and autism
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **developmental delay with or without dysmorphic facies and autism** covering all of the
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

# Research report: developmental delay with or without dysmorphic facies and autism (TRRAP-related; MONDO:0032760)

**Verification status.** I checked the following in this session: the Cogné 2019 cohort data (via PMC6407527), the ClinGen gene-validity row already in the repo, the repo stub, the PanelApp listing, and the Trrap mouse-knockout lethality (via search snippets). The MIM number #618454 comes from a conference poster and one search snippet, so confirm it in OMIM before binding. Everything else is marked "not verified" or "from memory". No curation entry exists yet. The stub `stubs/Developmental_Delay_With_Or_Without_Dysmorphic_Facies_And_Autism.yaml` is `UNDECIDED` and lists one causal gene, `hgnc:12347` (TRRAP). I have not edited the repo.

## 1. Disease information

- **Overview.** This is an autosomal dominant neurodevelopmental disorder caused by heterozygous, mostly de novo, missense variants in *TRRAP*. Core features are global developmental delay and intellectual disability. Variable features include autism, seizures, facial dysmorphism, and malformations of the brain, heart, kidney, genitalia and palate.
- **Identifiers.**
  - MONDO:0032760.
  - OMIM phenotype #618454. This is secondary-source only, from the [LSU Health case-report poster](https://www.medschool.lsuhsc.edu/genetics/ClaySloanePoster.pdf), and is unconfirmed.
  - The TRRAP gene MIM is 603015, as listed on [PanelApp](https://panelapp.genomicsengland.co.uk/panels/285/gene/TRRAP/).
  - HGNC: `hgnc:12347`.
  - Orphanet, ICD-10 and MeSH: not checked.
- **Synonyms.** DEDDFA (abbreviation not verified). Also described as "TRRAP-related neurodevelopmental disorder".
- **Overlap with ClinGen's broader term.** ClinGen curates TRRAP against a different, broader MONDO term, "complex neurodevelopmental disorder with or without congenital anomalies" (MONDO:0100465). The rating is Definitive, autosomal dominant, from the Intellectual Disability and Autism GCEP, dated 2022-07-19: `CGGV:assertion_03424cde-a847-4bd0-91eb-9707a7e51fa2-2022-07-19T100000.000Z`. This row is in `kb/genes/ingest/clingen_gene_validity.tsv`. The assertion belongs to MONDO:0100465, not to this entry's term. Under the repo's "assertion must be for this entry's disease" rule, record it only if you decide the two terms are the same entity, or map with an `exactMatch`.
- **Source level.** Findings come from individual patients in sequencing cohorts, aggregated by the papers cited below. This is not an EHR-derived resource.
- **Lump/split note.** Cogné et al. describe two genotype-defined phenotypic clusters (see section 3). They are not separate named diseases, so the default is one entry with `has_subtypes` or per-phenotype notes, not two entries.

## 2. Etiology

- **Cause.** Heterozygous missense variants in *TRRAP*. In the primary cohort, 17 distinct variants occurred in 24 individuals, mostly de novo or "apparently de novo" (parentage not confirmed). Source: Cogné et al., *Am J Hum Genet* 2019, [PMID:30827496](https://pmc.ncbi.nlm.nih.gov/articles/PMC6407527).
- **Genetic risk and modifiers.** No modifier genes are known (not found).
- **Environmental risk, protective factors and gene–environment interactions.** None identified.

## 3. Phenotypes (Cogné 2019, Table 2)

The paper compares individuals with variants in the codon 1031–1159 cluster to those outside it.

| Phenotype | In cluster (codons 1031–1159) | Outside cluster | Suggested HPO |
|---|---|---|---|
| Global developmental delay | 13/13 | 11/11 | HP:0001263 |
| Intellectual disability | 11/11 | 6/9 | HP:0001249 |
| Autism spectrum disorder | 0/13 | 5/11 | HP:0000717 |
| Seizures | 1/13 | 4/11 | HP:0001250 |
| Microcephaly | 6/13 | 1/11 | HP:0000252 |
| Cardiac malformation | 9/12 | 1/3 | HP:0001627 |
| Renal malformation | 5/13 | 0/4 | HP:0000077 (coarse; prefer a more specific term) |
| Genital malformation | 5/13 | 0/11 | HP:0000078 |
| Cleft lip/palate | 5/13 | 0/11 | HP:0000202 / HP:0000175 |

- **Facial dysmorphism.** It was present in 19/24 (79%). Features were upslanted palpebral fissures, epicanthus, telecanthus, a wide nasal bridge, a broad smooth philtrum and a thin upper lip. Suggested HPO terms: HP:0000582 (upslanted palpebral fissures), HP:0000286 (epicanthus), HP:0000319 (smooth philtrum). I have not looked these up in this session, so check each CURIE and label against the ontology before binding.
- **Brain MRI.** 7 of 10 scanned cluster individuals had structural anomalies. The most common was cerebellar vermis hypoplasia, in 6/10.
- **Neurology.** Peripheral neuropathy was severe in one individual. Lower-limb hyperreflexia was noted in five others.
- **Two clusters.**
  - Cluster 1 (codons 1031–1159, centred on p.Ala1043Thr) is the multisystem malformation syndrome with ID.
  - The outside-cluster group shows ASD and/or ID with epilepsy.
  - Note the naming tension: the cluster-1 variants carry no ASD in this cohort, while the disease name includes "autism". Ascertainment and sample size limit the conclusion.
- **Later case report.** The LSU poster reports a 9-year-old with a de novo variant in the 1031–1159 region who fits the OMIM phenotype. It is a single case and a poster, so do not cite it as evidence.
- **Onset, progression and quality of life.** Onset is developmental (infancy to childhood). Progression and quality-of-life data were not found.

## 4. Genetic and molecular information

- **Gene.** *TRRAP* (transformation/transcription domain-associated protein, 3q… locus not verified). It is a large pseudokinase scaffold in the SAGA and TIP60 histone acetyltransferase complexes.
- **Variants.**
  - All are missense.
  - Recurrent: p.Ala1043Thr (c.3127G>A) in 5 individuals, and p.Glu1106Lys and p.Gly1883Arg in 2 each.
  - Thirteen individuals carried variants in codons 1031–1159. Clustering was significant (p = 9×10⁻⁸). A second, smaller aggregate sits at codons 1859–1932.
  - No loss-of-function variants and no intragenic deletions (DECIPHER) were reported.
- **Constraint.** Missense z = 10.1 (ExAC), among the top five genes by missense intolerance. pLI = 1.00.
- **Functional consequence.** The authors propose gain-of-function or dominant-negative effects for the clustered variants. They consider haploinsufficiency likely lethal prenatally, since no LoF variants were seen. This is inferred, not demonstrated.
- **Origin.** De novo germline. Two sisters inherited a variant from a mother with low-level mosaicism, and p.Pro1932Leu is listed as germline mosaicism.
- **Epigenetic and chromosomal.** Not applicable. No specific methylation signature has been reported (not found).

## 5. Environmental information

None is established. There are no known infectious or toxic triggers.

## 6. Mechanism and pathophysiology

**Causal chain.**
1. A de novo heterozygous missense variant changes TRRAP. Clustered variants fall near codons 1031–1159 (inferred to be a hotspot domain; the specific domain was not confirmed).
2. The altered protein is thought to act as gain-of-function or dominant-negative in SAGA/TIP60 histone acetyltransferase complexes (inferred, not demonstrated here).
3. Dysregulated chromatin acetylation and transcription follows. This step is also inferred. The only direct data are the fibroblast RNA-seq findings below.
4. Disrupted neurodevelopment results, giving global developmental delay and intellectual disability.
5. The mechanism branches. Variants in the cluster are linked to multisystem malformations (heart, kidney, genitalia, palate, cerebellar vermis). Variants outside it are linked to ASD and seizures. The cause of the branching is unexplained.

**Direct supporting data.**
- Fibroblast RNA-seq from two individuals (p.Leu805Phe and p.Trp1866Cys; both outside the cluster) versus two controls showed mostly upregulated genes. GO enrichment pointed to adrenergic receptor signalling, neuronal function and potassium/ATP-sensitive ion transport. Cogné et al. did not report HAT-activity or p53 assays. They acknowledge that non-HAT TRRAP interactions could account for the signature.
- Suggested ontology terms: GO:0016573 (histone acetylation), GO:0006357 (regulation of transcription by RNA polymerase II), and the SAGA and NuA4 complexes in the GO cellular-component branch. Look all of these up before binding. Candidate Cell Ontology terms are neural progenitor cell or neuron.

**Cell and tissue context.** Neural progenitors are implicated by animal data. A search snippet of a 2021 zebrafish paper says Nestin-Cre conditional deletion of Trrap in mice causes premature differentiation of neural progenitors. I did not retrieve the original mouse paper.

## 7. Anatomical structures affected

Brain (cerebellar vermis), heart, kidney, genitalia, palate and face; occasionally peripheral nerves. Suggested UBERON terms (to be looked up): cerebellar vermis, heart, kidney. Subcellular: nucleus and chromatin, in the SAGA/TIP60 complexes.

## 8. Temporal development

Onset is congenital to infantile. The course appears stable. I found no natural-history, remission or critical-period data.

## 9. Inheritance and population

- **Inheritance.** Autosomal dominant, with de novo variants predominating. HP:0000006 is the mode-of-inheritance term. Mosaic parental transmission is documented (see section 4).
- **Epidemiology.** No prevalence or incidence data found. Penetrance, expressivity, sex ratio and founder effects: not reported.

## 10. Diagnostics

- **Genetic testing.** Exome sequencing, trio where possible, or a gene panel including TRRAP. TRRAP is Green on the PanelApp intellectual disability panel. Cogné et al. found variants mainly by exome sequencing and through GeneMatcher.
- **Imaging.** Brain MRI for cerebellar vermis hypoplasia.
- **Differential diagnosis, screening and criteria.** Not researched. There are no formal criteria.

## 11. Outcome and prognosis

No survival, mortality or quality-of-life data found. Lifelong intellectual disability is expected, based on 100% GDD in the cohort.

## 12. Treatment

No disease-specific therapy. Management is supportive: early intervention, speech, physical and occupational therapy, and seizure treatment where present. Suggested NCIT terms: NCIT:C15747 (Supportive Care), NCIT:C15302 (Physical Therapy), NCIT:C15315 (Rehabilitation). Both are in this repo's list of common NCIT terms. No clinical trials, pharmacogenomics or gene therapy were found.

## 13. Prevention

Genetic counselling is warranted. Recurrence risk is low for de novo cases but not zero, given documented parental mosaicism and germline mosaicism in this cohort.

## 14–15. Other species and model organisms

- **Mouse.** Complete Trrap loss is embryonic lethal. A 2001 study (Herceg et al., *Nat Genet*; I did not retrieve the PMID, so verify before citing) found that null mutation of Trrap causes peri-implantation lethality from blocked blastocyst proliferation. A [figshare record](https://figshare.utas.edu.au/articles/journal_contribution/Disruption_of_Trrap_causes_early_embryonic_lethality_and_defects_in_cell_cycle_progression/22876895) carries a related title.
- **Neural-specific deletion.** Nestin-Cre conditional deletion causes premature differentiation of neural progenitors (second-hand, see section 6).
- **Zebrafish.** A trrap knockout shows craniofacial phenotypes ([PMC8692476](https://pmc.ncbi.nlm.nih.gov/articles/PMC8692476), Sci Rep 2021; I did not read it directly).
- **Fidelity.** Null models test haploinsufficiency, which the human genetics argue is not the disease mechanism. Missense knock-in models of the clustered variants were not found.
- **Yeast.** Tra1 deletion data are cited by Cogné et al. from prior literature.
- **Natural disease in other species (OMIA).** Not checked.

## Curation notes for the entry

1. Evidence snippets must be exact substrings. Run `just fetch-reference PMID:30827496`, then quote from the cached abstract or full text. I did not quote the paper verbatim here, because the fetch tool would not return long verbatim text.
2. Decide how to relate this entry to MONDO:0100465 and the ClinGen assertion (see section 1).
3. Look up every CURIE listed above before writing it into YAML.
4. The gene-disease validity row cannot go on this entry unless the two terms are judged the same.
5. Create a claim issue first: `Curate developmental delay with or without dysmorphic facies and autism (MONDO:0032760)`.
6. Delete the stub and add a history record in the curation PR.

## Sources

- [Cogné et al. 2019, AJHG (PMID:30827496)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6407527)
- [HAL record of Cogné et al. 2019](https://hal-univ-rennes1.archives-ouvertes.fr/hal-02181523)
- [PanelApp intellectual disability panel, TRRAP](https://panelapp.genomicsengland.co.uk/panels/285/gene/TRRAP/)
- [LSU Health case-report poster (OMIM #618454)](https://www.medschool.lsuhsc.edu/genetics/ClaySloanePoster.pdf)
- [Zebrafish trrap, Sci Rep 2021 (PMC8692476)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8692476)
- [Trrap embryonic lethality, figshare](https://figshare.utas.edu.au/articles/journal_contribution/Disruption_of_Trrap_causes_early_embryonic_lethality_and_defects_in_cell_cycle_progression/22876895)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 10 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000077` (1 mention) - the report calls it "coarse; prefer a more specific term"; HP calls it **Abnormality of the kidney**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016573` (obsolete histone acetylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016573` (1 mention) - the report calls it "histone acetylation"; GO calls it **obsolete histone acetylation**