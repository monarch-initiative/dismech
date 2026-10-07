---
provider: claude_code
model: claude-fable-5, claude-haiku-4-5-20251001
cached: true
start_time: '2026-09-18T20:44:04.623367'
end_time: '2026-09-18T20:44:04.627676'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Usmani-Riazuddin Syndrome, Autosomal Dominant
  mondo_id: MONDO:0859174
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
  - claude-fable-5
  - claude-haiku-4-5-20251001
  web_search_requests: 3
  num_turns: 12
  total_cost_usd: 4.813130999999999
  session_id: 51685240-3187-4840-8fcf-416a99444b53
  stop_reason: end_turn
  assistant_text_blocks: 6
citation_count: 10
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - PMID:10811610
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 46
  verified: 45
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 15
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0859174
    reported_labels:
    - MONDO
    ontology_label: Usmani-Riazuddin syndrome, autosomal dominant
  - term_id: UBERON:0000955
    reported_labels:
    - Primary organ:** brain
    ontology_label: brain
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Usmani-Riazuddin Syndrome, Autosomal Dominant
- **MONDO ID:** MONDO:0859174 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Usmani-Riazuddin Syndrome, Autosomal Dominant** covering all of the
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

I'll research Usmani-Riazuddin Syndrome, Autosomal Dominant (AP1G1-related). Let me start by loading web research tools and checking local curated resources in parallel.

I have the curated KB entry's first section. Let me read the rest and run web searches in parallel to fill in details (OMIM identifiers, variant spectrum, epidemiology, recent literature).

The local curated entry gives me verified evidence with exact quotes. Let me pull OMIM detail on the clinical synopsis and variant list, plus gene-level info, to round out the report.

OMIM blocks direct fetches. Let me get the variant-level detail from the open-access primary papers instead.

Excellent detail. Two more quick checks: gene–disease validity classifications (GenCC/ClinGen) and the mouse gamma-adaptin knockout literature for the model-organism section.

# Research Report: Usmani-Riazuddin Syndrome, Autosomal Dominant (USRISD)

**MONDO:0859174 · OMIM #619467 · Gene: AP1G1 (hgnc:555) · Report date: 2026-09-18**

---

## 1. Disease Information

**Overview.** Usmani-Riazuddin syndrome, autosomal dominant (USRISD) is an ultra-rare Mendelian neurodevelopmental disorder caused by heterozygous, almost always *de novo*, variants in **AP1G1**, which encodes the gamma-1 adaptin subunit of the heterotetrameric clathrin adaptor protein complex 1 (AP-1). The disorder was delineated in 2021 by Usmani, Riazuddin and colleagues (PMID:34102099), who reported de novo heterozygous and biallelic AP1G1 variants across eleven families: *"De novo and bi-allelic variants in AP1G1 are associated with neurodevelopmental disorder in diverse populations."* Core features are mild-to-severe intellectual disability, global developmental delay, speech delay, and aggressive behavior (each present in 100% of the founding cohort), with variable epilepsy, hypotonia, spasticity, autistic features, limb defects, and facial dysmorphism (PMID:34102099; PMID:41226632).

**Key identifiers.**
| Resource | Identifier |
|---|---|
| OMIM (disease) | #619467 (USRISD) |
| OMIM (gene) | *603533 (AP1G1) |
| MONDO | MONDO:0859174 |
| HGNC | hgnc:555 (AP1G1) |
| Sibling disorder | Usmani-Riazuddin syndrome, autosomal recessive — OMIM #619548, MONDO:0859196 |
| Orphanet | No dedicated ORPHA code identified for USRISD as of this report |
| ICD-10 | No specific code; coded under manifestations (e.g., F70–F79 intellectual disability, G40 epilepsy) |

Important nosological note: MONDO treats the dominant (MONDO:0859174) and recessive (MONDO:0859196) forms as **sibling terms**, both asserting causation by AP1G1, with no umbrella term above them. The follow-up literature describes them as showing *"overlapping clinical features"* (PMID:41226632), but no systematic phenotype comparison between the two forms has been published, and functional data separate their allele mechanisms (see §6).

**Synonyms.** AP1G1-related neurodevelopmental disorder; USRISD; "adaptinopathy" is used in the zebrafish literature as an umbrella mechanism term for AP-complex subunit disorders (PMID:37108275).

**Data provenance.** All information derives from aggregated case reports and small cohort studies in the primary literature (11 founding families plus single subsequent probands — at least 13 patients total across both inheritance forms as of late 2025, per PMID:41226632). No EHR-derived, registry, or population-level data exist. **No GeneReviews or StatPearls chapter exists for this disorder** (verified against the NCBI Bookshelf index snapshot of 2026-09-10, 958 GeneReviews chapters).

---

## 2. Etiology

**Causal factor.** Monogenic: heterozygous pathogenic variants in **AP1G1** (16q22.2). All published dominant probands carried **de novo** variants; no transmitted dominant pedigree has been reported. Reported dominant allele classes: missense (clustered in the N-terminal adaptin domain), splice-site, frameshift, and one whole-gene deletion (PMID:34102099; PMID:38840441; PMID:41226632).

**Two mechanistic allele classes coexist under the dominant label:**
1. **Haploinsufficiency** — frameshift alleles produce no detectable protein (proteasomally degraded), and a de novo whole-gene deletion at 16q22.2 produced the syndrome with *"a mild but consistent phenotype"* (PMID:38840441), the cleanest human evidence that halving dosage alone suffices. Consistent with this, AP1G1 is highly constrained: **pLI = 1, LOEUF = 0.2** (PMID:34102099).
2. **Dominant-negative missense** — full-length misfolded gamma-1 adaptin interferes with the wild-type protein (see §6). *"The observed phenotype is likely due to a dominant-negative effect or a toxic gain-of-function of the mutant AP1G1, impairing the activity or recruitment of the wild-type protein"* (PMID:41226632).

**Risk factors.** No environmental, lifestyle, or infectious risk factors are known or plausible for this de novo monogenic disorder. Advanced paternal age is a generic risk factor for de novo point mutations but has not been specifically studied in USRISD. No modifier genes, protective variants, or gene–environment interactions have been reported. Consanguinity is relevant only to the sibling recessive form (the biallelic Pakistani family; PMID:34102099).

---

## 3. Phenotypes

Frequencies derive from the 2021 founding cohort of 11 patients and the 2025 cohort synthesis (PMID:34102099; PMID:41226632): *"11 unrelated patients were described with mild to severe intellectual disability, speech delay, and aggressive behavior in 100% of the patients, while other aspects (including autism, epilepsy, hypotonia, spasticity, and limb defects) were variably expressed."*

| Phenotype | HPO term | Frequency | Onset / course |
|---|---|---|---|
| Intellectual disability | HP:0001249 | 100% (mild→severe) | Childhood; static-to-slowly-evolving |
| Global developmental delay | HP:0001263 | 100% | Infancy |
| Delayed speech and language development | HP:0000750 | 100% | Early childhood |
| Aggressive behavior | HP:0000718 | 100% (founding cohort) | Childhood; persistent |
| Seizure | HP:0001250 | ~70% of de novo patients | Variable; types not systematically reported |
| Hypotonia | HP:0001252 | ~60% | Infancy |
| Autistic behavior | HP:0000729 | ~50% | Childhood |
| Spasticity | HP:0001257 | Variable | — |
| Hyperactivity | HP:0000752 | Variable | Childhood |
| Self-injurious behavior | HP:0100716 | Reported (individual cases) | Infancy-onset in one proband |
| Abnormality of limbs | HP:0040064 | Variable | Congenital |
| Abnormal facial shape | HP:0001999 | Variable/preliminary | Congenital |
| Abnormal vertebral morphology | HP:0003468 | Variable | Congenital |
| Hearing impairment | HP:0000365 | Individual case (frameshift proband) | — |

**Additional per-patient detail.** In the 2025 proband (c.196G>A, p.Gly66Arg): 12-year-old girl, independent walking at 18 months, <10 words at age 3, verbal IQ 53 / performance IQ 59 / full-scale 49, aggression toward peers and adults, hyperactivity, obsessive-compulsive behaviors, one febrile seizure at age 2 with normal EEG and brain MRI (PMID:41226632). The whole-gene-deletion patient presented at 5–10 years with *"developmental delay, behavioural difficulties, possible infantile spasms, left hemiplegia, and toe walking"* (PMID:38840441).

**Facial gestalt (preliminary).** A single 2024 report proposed a recognizable gestalt — synophrys, hypotelorism, upslanted palpebral fissures, broad nasal tip, thick lip vermilion: *"this is the first description of likely distinctive facial features in a patient with Usmani-Riazuddin syndrome"* (PMID:38665048). This rests on one patient; the founding series described the facial gestalt as "unspecified."

**Quality of life.** No formal QoL instrument (EQ-5D, SF-36, PROMIS) has been applied. The universal aggressive behavior represents a substantial family burden independent of cognitive severity; no formal caregiver-burden study exists.

---

## 4. Genetic/Molecular Information

**Gene.** AP1G1 (adaptor related protein complex 1 subunit gamma 1), hgnc:555, OMIM *603533, chromosome 16q22.2. Encodes gamma-1 adaptin, one of four subunits (γ, β1, μ1, σ1) of the AP-1 clathrin adaptor. Constraint: **pLI = 1.0, LOEUF = 0.2** — *"AP1G1 is highly intolerant to variations"* (PMID:34102099).

**Reported dominant (de novo heterozygous) variants** (PMID:34102099, plus later reports):

| cDNA | Protein | Type | Origin | Notes |
|---|---|---|---|---|
| c.44G>A | p.Arg15Gln | Missense | De novo | Moderate ID, epilepsy, aggression, hypotonia |
| c.103C>T | p.Arg35Trp | Missense | De novo (2 families) | Recurrent; mild–moderate ID, epilepsy |
| c.104G>A | p.Arg35Gln | Missense | De novo | ASD, self-injurious behavior |
| c.196G>A | p.Gly66Arg | Missense | De novo | 2025 proband; dominant-negative evidence (PMID:41226632) |
| c.229delC | p.Gln77Lysfs*11 | Frameshift | De novo | Mild ID, hearing loss, depression/anxiety |
| c.399_400del | p.Glu133Aspfs*37 | Frameshift | De novo | Moderate ID, hypotonia, aggression/autism |
| c.747G>T | p.Gln249His | Missense | De novo | Patient died at 22 days (phenotype otherwise unavailable) |
| c.928−2A>C | p.? | Splice acceptor | De novo | Mild ID, autism, hyperactivity |
| c.1969C>G | p.Leu657Val | Missense | De novo | Likely pathogenic per ACMG (PMID:38665048) |
| c.2459C>G | p.Pro820Arg | Missense (C-terminal) | De novo | Moderate ID, aggression |
| 16q22.2 whole-gene deletion | — | CNV | De novo | Mild phenotype; WGS-diagnosed (PMID:38840441) |

Pathogenic dominant missense variants **cluster in the N-terminal adaptin domain at highly conserved residues** (Arg15, Arg35, Gly66) with two exceptions (Gln249, Pro820, Leu657) (PMID:41226632). Classification followed ACMG/AMP criteria in all recent reports.

**Allele frequency.** Dominant pathogenic variants are absent from gnomAD, dbSNP, and ESP (PMID:41226632); only the recessive c.1105A>G allele appears in gnomAD (7 heterozygous carriers, AF ≈ 1.67 × 10⁻⁵) (PMID:34102099).

**Functional consequences by class.** Immunoblot in heterologous cells: p.Arg15Gln, p.Arg35Trp show decreased protein levels; frameshift alleles produce undetectable, proteasomally degraded protein; de novo missense proteins form aggregates or show diffuse cytoplasmic localization, versus normal perinuclear clathrin-colocalized distribution for the recessive missense proteins (PMID:34102099). *"In silico analysis and 3D protein modeling simulation predicted alteration of AP1γ1 protein folding for missense variants, which was consistent with the observed altered AP1γ1 levels in heterologous cells"* (PMID:34102099).

**Germline vs somatic.** All variants are germline, arising de novo. Germline (gonadal) mosaicism has not been reported but is the standard residual recurrence-risk consideration. No epigenetic mechanisms, modifier genes, or larger chromosomal rearrangements (beyond the single-gene deletion) are described.

**Gene–disease validity (GenCC, accessed 2026-09-18):** AP1G1–USRISD (AD) is classified **Strong** by Labcorp Genetics (2023) and G2P (2025); ClinGen classifies AP1G1–complex neurodevelopmental disorder (AD) as **Strong** (2026); PanelApp Australia lists it as semidominant (Strong, 2026). The AR association is Strong (Labcorp) but Limited per G2P and ClinGen.

---

## 5. Environmental Information

Not applicable. USRISD is a fully penetrant-appearing de novo monogenic disorder with no known environmental, lifestyle, or infectious contributors. One anecdotal observation — behavioral improvement during antibiotic therapy extending beyond acute infections in the 2025 proband (PMID:41226632) — is uninterpreted and should not be read as an environmental mechanism.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (dominant form):**

1. **De novo heterozygous AP1G1 variant** — either (branch A) a truncating/splice/whole-gene-deletion allele that eliminates one gene copy (**haploinsufficiency**; demonstrated), or (branch B) an N-terminal missense allele producing a misfolded gamma-1 adaptin that **interferes with the wild-type protein** (dominant-negative vs. toxic gain-of-function not yet separated; inferred from rescue-failure assays) —
2. → leads to **AP-1 adaptor complex dysfunction** (GO:0030121; reduced AP-1-mediated cargo loading into clathrin-coated vesicles, GO:0035653). *"The AP1γ1-mediated adaptor complex is essential for the formation of clathrin-coated intracellular vesicles"* (PMID:34102099); AP-1 and AP-2 are the only clathrin-coat-forming adaptors, so loss is not buffered (PMID:37108275).
3. → results in **trans-Golgi network cargo-sorting failure** (GO:0005802; GO:0006895). Demonstrated in patient fibroblasts: *"although GM130 labeling remained comparable to that in the controls, the organization of the trans-Golgi cisternae appeared more diffuse and disorganized"*; the mutant protein *"disrupts membrane association and impairs vesicular trafficking at the trans-Golgi level"* (PMID:41226632).
4. → (parallel branch, demonstrated only for recessive alleles) **endosomal recycling impairment** (GO:0032456): *"Functional studies of the recessively inherited missense variants revealed no apparent impact on the interaction of AP1γ1 with other subunits of the AP-1 complex but rather showed to affect the endosome recycling pathway"* (PMID:34102099). Whether dominant alleles engage this step is untested — an inferred, not demonstrated, branch for USRISD.
5. → leads to **impaired polarized somatodendritic protein sorting in neurons** (GO:0036477; CL:0000540): *"Adaptor protein (AP) complexes mediate selective intracellular vesicular trafficking and polarized localization of somatodendritic proteins in neurons"* (PMID:34102099). The brain is *"the tissue with the most active vesicular protein transport"* (PMID:37108275) — explaining why a ubiquitous trafficking lesion presents neurologically.
6. → in parallel, **cadherin mis-sorting and adherens junction instability** (GO:0044331; GO:0034332): heterozygous ap1g1 zebrafish show *"dysregulated cadherin-mediated cell adhesion"* and impaired *"cadherin protein sorting and adherent junction (AJ) formation"* (PMID:37108275) — the best-characterized individual cargo defect.
7. → results in **perturbed neurodevelopment and reduced brain growth** (GO:0007420; GO:0030182; UBERON:0000955): in heterozygous zebrafish, *"the heterozygous fish displayed abnormalities in specific brain areas and spinal cord neurons, and the brain volume is reduced"* (PMID:37108275); mutant human mRNA in wild-type embryos causes *"severe developmental abnormalities and increased lethality"* (PMID:34102099).
8. → clinically manifests as **intellectual disability, developmental/speech delay, aggression, seizures, hypotonia, spasticity, autistic features** (all links from step 7 to specific clinical features are inferred — no intermediate circuit-level mechanism has been measured in humans).

**Dominant-negative evidence in detail** (PMID:41226632): wild-type human AP1G1 mRNA rescues ap1g1⁻/⁻ zebrafish lethality; mutant (p.Gly66Arg) mRNA does not; and critically, *"the phenotype was also not rescued when ap1g1-/- zebrafish embryos were co-injected with both human wild-type and mutated mRNAs, supporting the dominant-negative effect."* The same design in 2021 showed the founding de novo alleles (p.Arg15Gln, p.Arg35Trp, p.Arg35Gln) failed rescue and were toxic in wild-type fish, while the recessive alleles gave partial rescue (hypomorphs) (PMID:34102099). Both groups explicitly leave dominant-negative vs toxic gain-of-function unresolved — a key knowledge gap, with therapeutic implications (allele-selective knockdown vs dosage restoration).

**Molecular profiling.** No patient transcriptomics, proteomics, metabolomics, single-cell, or spatial data exist. Zebrafish heterozygote mRNA marker profiling identified the cadherin-adhesion signature (PMID:37108275).

---

## 7. Anatomical Structures Affected

- **Primary organ:** brain (UBERON:0000955), with spinal cord involvement in the animal model (UBERON:0002240); affected regions in the zebrafish heterozygote include telencephalon, midbrain, midbrain-hindbrain boundary, and spinal cord neuronal populations (PMID:37108275).
- **Secondary/variable:** skeleton — limbs and vertebrae (UBERON:0002101, UBERON:0002412); face (UBERON:0001456); musculature via tone abnormalities. The zebrafish heterozygote additionally shows gonadal and intestinal epithelial changes not reported in humans (PMID:37108275).
- **Cell types:** neurons (CL:0000540); patient dermal fibroblasts (CL:0000057) as the demonstrated cellular substrate; epithelial cells in the model.
- **Subcellular:** trans-Golgi network (GO:0005802), clathrin-coated vesicles (GO:0030136), recycling endosomes (GO:0055037), AP-1 adaptor complex (GO:0030121), somatodendritic compartment (GO:0036477). The cis-Golgi is spared (GM130 normal; PMID:41226632).
- **Lateralization:** generally bilateral/symmetric; one patient (deletion case) had left hemiplegia (PMID:38840441).

---

## 8. Temporal Development

- **Onset:** congenital lesion; clinical recognition in **infancy to early childhood** via delayed milestones (walking at 18 months, <10 words at age 3 in the 2025 proband). One founding-cohort patient (p.Gln249His) died at 22 days, suggesting the severe end can present neonatally (PMID:34102099).
- **Course:** chronic, lifelong. Intellectual disability appears largely static, though one patient (p.Pro820Arg) was described with decreasing cognitive scores through adolescence (PMID:34102099). Behavioral features (aggression, hyperactivity) persist into adolescence. Epilepsy course is variable and not systematically characterized. No remission pattern, staging system, or natural-history study exists.
- **Critical periods:** by mechanism, prenatal/early postnatal neurodevelopment — zebrafish data show *"normal expression of ap1g1 at early stages of neurodevelopment is required for determination and/or differentiation of specific neuronal populations"* (PMID:37108275). Early developmental therapy is the corresponding intervention window (inference, not trial-based).

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006), with **all reported dominant probands arising de novo**. No transmitted pedigree; no anticipation; no founder effect; no documented germline mosaicism. Sibling recurrence risk is low but non-zero (gonadal mosaicism). Distinguish carefully from the AR sibling disorder (25% sibling recurrence): zygosity, not the gene, settles the counseling.
- **Penetrance/expressivity:** apparently complete penetrance in reported cases (ascertainment-limited); **variable expressivity** is marked — ID spans mild to severe, epilepsy present in only ~70%, and the whole-gene deletion produced a mild phenotype, hinting that dominant-negative missense alleles may be more severe than pure dosage loss (inference from small numbers; PMID:38840441).
- **Epidemiology:** ultra-rare; **≥13 patients across both forms** reported in the world literature through 2025 (PMID:41226632); *"Usmani-Riazuddin syndrome (USRISR, MIM# 619548; USRISD, MIM#619467) is a very rare genetic condition"* (PMID:38665048). No prevalence or incidence estimate exists.
- **Demographics:** reported families span Germany, Poland, the Netherlands, the USA, and Italy for the dominant form — *"diverse populations"* (PMID:34102099). No sex bias is evident (both sexes affected); numbers are far too small for ratios.

---

## 10. Diagnostics

- **Primary modality: molecular.** There is no biochemical or imaging biomarker; every published proband was diagnosed by **trio or singleton exome sequencing** with ACMG interpretation (NCIT:C101295, Whole Exome Sequencing). Example: *"clinical exome disclosed AP1G1: c.1969C>G (p.Leu657Val), de novo, likely pathogenic variant, according to ACMG classification criteria"* (PMID:38665048).
- **Genome sequencing for CNVs** (NCIT:C101294): exome misses whole-gene deletions. In the deletion case, array CGH placed *"only 1 out of 4 array CGH probes"* over AP1G1, leaving a VUS for years until trio WGS resolved the breakpoints (PMID:38840441). WGS is the follow-on test for suspected 16q22.2 CNVs.
- **Gene panels:** AP1G1 appears on neurodevelopmental-disorder panels (PanelApp Australia lists it, semidominant, Strong).
- **Supportive workup:** EEG for seizures, brain MRI (normal in the 2025 proband; agenesis of the corpus callosum was reported in a *recessive* patient), standardized cognitive testing (Wechsler-type IQ), behavioral assessment. Karyotype, FISH, mtDNA, repeat-expansion, and omics-based diagnostics have no specific role.
- **Differential diagnosis:** other monogenic NDDs with ID + aggression + variable epilepsy; other "adaptinopathies" (AP1S2 X-linked ID/Pettigrew syndrome, AP4 deficiency spectrum, AP3 Hermansky-Pudlak type 2, AP2M1 epilepsy); distinction is molecular. The proposed facial gestalt (PMID:38665048) may eventually aid recognition but needs multicenter confirmation.
- **Screening:** none applicable (de novo disorder; no newborn or carrier screening). Prenatal/PGT testing is technically possible for a known familial variant.

---

## 11. Outcome / Prognosis

- **Survival:** no mortality data published. Most patients survive to adolescence/young adulthood (oldest reported dominant patients ~18 years at description); one neonatal death at 22 days occurred in a p.Gln249His proband, cause-specific attribution unclear (PMID:34102099).
- **Function/morbidity:** lifelong intellectual disability (mild–severe), communication impairment, and behavioral disturbance dominate morbidity. Aggression in 100% of the founding cohort is the major determinant of family burden. Hemiplegia, toe-walking, spasticity, and hearing loss add motor/sensory disability in individual patients.
- **Prognostic factors (provisional, small-N inference):** allele class may matter — the whole-gene deletion produced *"a mild but consistent phenotype"* (PMID:38840441), while dominant-negative missense alleles associate with moderate–severe presentations. No validated prognostic biomarker exists.
- **QoL measures:** none published.

---

## 12. Treatment

**No disease-modifying or AP1G1-specific therapy exists.** Management is entirely symptomatic and supportive (no clinical trials identified on ClinicalTrials.gov for this indication):

| Intervention | NCIT term | Target |
|---|---|---|
| Antiseizure medication (agent per general epilepsy practice; no AP1G1-specific response data) | NCIT:C64172 Anticonvulsant Therapy | Seizures (HP:0001250) |
| Developmental/rehabilitative therapy — physical, occupational, speech-language | NCIT:C15315 Rehabilitation; NCIT:C159273 Speech Therapy | GDD, speech delay, hypotonia |
| Behavioral intervention for aggression, hyperactivity, autistic features | NCIT:C181743 Behavioral Counseling | Aggression (HP:0000718), autistic behavior |
| Genetic counseling (de novo recurrence risk; AD-vs-AR disambiguation) | NCIT:C15240 Genetic Counseling | Family |

**Future directions (preclinical only):** the zebrafish platform is explicitly positioned for therapeutic development — *"zebrafish...holds promise for identifying genetic and molecular targets"* (PMID:41226632). Mechanistically, the unresolved dominant-negative vs haploinsufficiency question bifurcates future strategy: allele-selective knockdown (ASO/siRNA) for interfering missense alleles versus dosage restoration for null alleles. Nothing of the kind has entered even preclinical pipelines. No pharmacogenomic data exist.

---

## 13. Prevention

- **Primary prevention:** none possible (sporadic de novo variants).
- **Secondary:** early molecular diagnosis via exome/genome sequencing in undiagnosed NDD enables early developmental intervention and ends the diagnostic odyssey (the deletion case sat as a VUS for years; PMID:38840441).
- **Tertiary:** seizure control, behavioral management, and rehabilitation to limit complications.
- **Reproductive:** genetic counseling for parents of an affected child (low recurrence risk with a gonadal-mosaicism caveat); prenatal diagnosis or PGT feasible for the known variant. Cascade screening is not relevant for de novo dominant alleles.

---

## 14. Other Species / Natural Disease

No naturally occurring AP1G1 disease is documented in companion animals or wildlife (no OMIA phene identified). The gene is deeply conserved across vertebrates (NCBITaxon:7955 zebrafish and NCBITaxon:10090 mouse orthologs used experimentally; mouse *Ap1g1*, NCBI Gene 11765). Comparative biology insight comes from engineered models (§15): conservation is strong enough that **human wild-type AP1G1 mRNA rescues the zebrafish ap1g1 null** (PMID:41226632), directly demonstrating functional orthology. Zoonotic transmission is not applicable.

---

## 15. Model Organisms

**Zebrafish (Danio rerio):**
1. **CRISPR/Cas9 ap1g1 knockout** (PMID:37108275): homozygous nulls arrest at the blastula stage (in the 2021 line, ~84% lethality by 10 dpf with severe edema; PMID:34102099); **heterozygotes are the informative genotype, matching the human dominant state** — they survive with reduced brain volume, missing neuronal populations (telencephalon, midbrain, midbrain-hindbrain boundary, spinal cord), reduced fertility, and dysregulated cadherin-mediated adhesion: *"heterozygosity causes disease phenotypes."* Limitations: gut/gonadal phenotypes lack human counterparts; models dosage only, not the missense alleles.
2. **mRNA rescue/co-injection assay** (PMID:34102099; PMID:41226632): human WT mRNA rescues the null (p<0.0001); patient missense mRNAs fail to rescue; recessive alleles partially rescue (hypomorphs); **WT + mutant co-injection fails to rescue** — the operational dominant-negative test. Limitation: transient supraphysiological mRNA, cannot separate dominant-negative from toxic gain-of-function.

**Mouse (Mus musculus):**
3. **γ-adaptin knockout** (Zizioli et al. 1999, PMID:10026148): homozygous null embryos die by E3.5, before implantation — *"AP-1 is essential for viability"*; notably, **heterozygous mice show reduced growth during nursing**, an early mammalian signal of dosage sensitivity consistent with human haploinsufficiency.
4. **Hypomorphic Ap1g1 mouse ("fitful" allele)** (PMID:27090238): causes inner ear, retina, thyroid, and testes abnormalities — partial-function phenotypes that broaden the adaptinopathy spectrum, though they diverge from the human neurodevelopmental picture.
5. Comparative: μ1A-adaptin-deficient mice are also embryonic lethal with mannose-6-phosphate receptor rerouting (PMID:10811610), confirming subunit-level essentiality of AP-1.

**Cellular models:** patient dermal fibroblasts (trans-Golgi disorganization, loss of membrane-associated AP1G1; PMID:41226632) and heterologous expression systems (protein levels, aggregation, clathrin colocalization, transferrin-recycling assays; PMID:34102099). No iPSC-derived neuronal or organoid model has been published — a clear gap given the neuronal locus of disease.

---

## Key Knowledge Gaps

1. **Dominant-negative vs toxic gain-of-function** for the missense alleles — explicitly unresolved by both functional groups (PMID:41226632); determines the rational therapeutic strategy.
2. **One disease or two?** No systematic phenotype comparison of the AD and AR forms exists; only the qualitative statement that features "overlap."
3. Whether dominant alleles impair **endosomal recycling** (measured only for recessive alleles).
4. No natural-history study, prevalence estimate, mortality data, QoL measurement, seizure phenotyping, or human neuronal model.
5. The proposed **facial gestalt** rests on a single patient and awaits multicenter confirmation (PMID:38665048).

## Primary Citations

- Usmani MA, Riazuddin S, et al. *Am J Hum Genet* 2021 — founding cohort. **PMID:34102099**
- Zizioli D, et al. *Int J Mol Sci* 2023 — ap1g1 KO zebrafish. **PMID:37108275**
- Gnazzo M, et al. *Clin Genet* 2024 — facial gestalt, p.Leu657Val. **PMID:38665048**
- (WGS CNV study) *2024* — whole-gene deletion case. **PMID:38840441**
- (Functional study of c.196G>A) *Int J Mol Sci* 2025 — dominant-negative characterization. **PMID:41226632**
- Zizioli D, et al. *J Biol Chem* 1999 — γ-adaptin-null mouse. **PMID:10026148**
- Johnson KR, et al. *Mamm Genome* 2016 — hypomorphic Ap1g1 mouse. **PMID:27090238**

Sources:
- [OMIM #619467 — Usmani-Riazuddin syndrome, autosomal dominant](https://omim.org/entry/619467)
- [OMIM #619548 — Usmani-Riazuddin syndrome, autosomal recessive](https://www.omim.org/entry/619548)
- [OMIM *603533 — AP1G1](https://www.omim.org/entry/603533)
- [Usmani et al. 2021, AJHG (PMC8322935)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8322935/)
- [2025 IJMS c.196G>A functional study (PMC12610428)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12610428/)
- [Gnazzo et al. 2024, Clinical Genetics](https://onlinelibrary.wiley.com/doi/10.1111/cge.14531)
- [GenCC — AP1G1 gene-disease validity](https://thegencc.org/genes/HGNC:555)
- [Zizioli et al. 1999, JBC — γ-adaptin-deficient mice (PubMed)](https://pubmed.ncbi.nlm.nih.gov/10026148/)
- [Johnson et al. 2016, Mammalian Genome — hypomorphic Ap1g1 mouse](https://pubmed.ncbi.nlm.nih.gov/27090238/)
- [μ1A-adaptin-deficient mice (PubMed)](https://pubmed.ncbi.nlm.nih.gov/10811610/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 9 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:10811610` (3 mentions) - mu1A-adaptin-deficient mice: lethality, loss of AP-1 binding and rerouting of mannose 6-phosphate receptors.
  - shared terms: gene

Weighed against this report's own most characteristic terms: `dominant`, `patient`, `ap1g1`, `novo`, `allele`, `dominant-negative`, `phenotype`, `gene`, `proband`, `missense`, `zebrafish`, `deletion`, `recessive`, `exist`, `syndrome`, `variant`, `aggression`, `epilepsy`, `usrisd`, `clinical`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859174` (3 mentions) - the report calls it "MONDO"; MONDO calls it **Usmani-Riazuddin syndrome, autosomal dominant**
- `UBERON:0000955` (2 mentions) - the report calls it "Primary organ:** brain"; UBERON calls it **brain**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005802` (2 mentions) - the report calls it "Subcellular:** trans-Golgi network"; GO calls it **trans-Golgi network**
- `GO:0032456` (1 mention) - the report calls it "endosomal recycling impairment"; GO calls it **endocytic recycling**
- `CL:0000540` (2 mentions) - the report calls it "Cell types:** neurons"; CL calls it **neuron**
- `NCIT:C101294` (1 mention) - the report calls it "Genome sequencing for CNVs"; NCIT calls it **Whole Genome Sequencing**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000718` - called "Aggressive behavior", "Aggression"
- `HP:0001250` - called "Seizure", "Seizures"