---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T02:01:49.338018'
end_time: '2026-11-26T02:05:00.621718'
duration_seconds: 191.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cardiac Tuberculosis
  mondo_id: MONDO:0000813
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
  - claude-opus-5-5
  web_search_requests: 22
  num_turns: 27
  total_cost_usd: 1.1202261
  session_id: b937322d-e1ce-45f6-b158-c2f1117675d5
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 26
  retrieval_calls: 23
  assistant_text_blocks: 2
citation_count: 42
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 8
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMC:PMC5703416
  - PMC:PMC9692124
  - PMC:PMC8432788
  quotes_not_checkable: 3
  relevance_assessed: 32
  on_topic: 16
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiac Tuberculosis
- **MONDO ID:** MONDO:0000813 (if available)
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

Please provide a comprehensive research report on **Cardiac Tuberculosis** covering all of the
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

Gathering sources on cardiac TB (pericarditis, myocarditis, diagnosis, trials); a few more searches next, then the report.

# Cardiac Tuberculosis (MONDO:0000813): Disease Characteristics Report

**How I read the request:** "Cardiac tuberculosis" here means tuberculous infection of the heart and its coverings: tuberculous pericarditis (TBP), which is by far the most common and best studied form, and tuberculous myocarditis, which is rare. Valvular and endocardial disease are rarer still.

**Causal gene:** None. This is an infectious disease caused by *Mycobacterium tuberculosis* complex organisms. The template records no causal gene and no OMIM entry, and no Mendelian gene for it was found. The genetics sections below therefore cover only general host susceptibility to tuberculosis.

**Method and limits:**
- PubMed E-utilities could not be called in this session, so all evidence comes from web search results. These were mostly PubMed, PMC and journal abstracts or snippets, not full texts.
- PMIDs are given only where a retrieved source showed them. PMC IDs or DOIs are given where no PMID was retrieved.
- Ontology terms (HPO, GO, CL, UBERON, NCIT, CHEBI) are offered as **labels only**. Their numeric IDs were not looked up in this session and must be checked before entry into the knowledge base.

---

## 1. Disease Information

**Overview.** TBP is infection of the pericardium by *M. tuberculosis*. It shows up as pericardial effusion, effusive-constrictive pericarditis or constrictive pericarditis. In TB-endemic regions it causes most large pericardial effusions, while in high-income countries it causes only a small share ([Wikipedia overview, secondary source](https://www.wikipedia.org/wiki/Tuberculous_pericarditis)).

The 2015 ESC pericardial guideline summary states that tuberculosis is "the most common cause of pericardial diseases all over the world and especially relevant in developing countries" ([ESC 2015, PMID 26320112](https://pubmed.ncbi.nlm.nih.gov/26320112/); [ESC summary](https://www.escardio.org/Working-groups/Working-Group-on-Myocardial-and-Pericardial-Diseases/Publications/Paper-of-the-Month/2015-esc-guidelines-on-the-diagnosis-and-management-of-pericardial-diseases)).

**Identifiers.**
- MONDO: MONDO:0000813, as given in the template.
- Not retrieved in this session: OMIM (not applicable), Orphanet, ICD-10, ICD-11 and MeSH codes. These need to be looked up.

**Synonyms.** Tuberculous pericarditis; pericardial tuberculosis (written "PCTB" in immunology papers, [PMC9692124](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9692124/)); tuberculous myocarditis; tuberculous constrictive pericarditis; tuberculous pericardial effusion.

**Data source type.** The evidence comes from aggregated clinical cohorts, registries and trials (for example the IMPI registry and the IMPI trial), plus pooled case reports for myocarditis. It does not come from EHR-derived patient data.

## 2. Etiology

**Causal factor.**
- The cause is infection with *M. tuberculosis*.
- Bacilli reach the pericardium by three routes ([Isiguzo et al. 2020, PMID 31940097](https://rd.springer.com/content/pdf/10.1007%2Fs11886-020-1254-1.pdf)):
  - retrograde lymphatic spread from mediastinal or peribronchial lymph nodes;
  - spread through the blood;
  - rarely, direct extension from nearby disease.

**Risk factors.**
- **HIV co-infection** is the main modifier.
  - In the Cape Town series, the authors note that "the prevalence of TB confounded by HIV co-infection is steadily increasing" ([Reuter et al. 2005, PMID 15962545](https://pmc.ncbi.nlm.nih.gov/articles/PMC2870262)).
  - In the IMPI registry, HIV-positive patients had more cardiomegaly and more haemodynamic instability ([BMC Infect Dis 2006](https://bmcinfectdis.biomedcentral.com/articles/10.1186/1471-2334-6-2)).
- **Living in a high-TB-burden setting** is the other key risk. All seven trials in the 2017 Cochrane review were run in sub-Saharan Africa ([Cochrane CD000526](https://www.cochrane.org/CD000526)).
- **Age and sex.** These are reported only for myocarditis. In pooled case reports, 81% of patients were under 45, and about twice as many were male as female ([Michira et al. 2015, PMID 26327955](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4546727/)).

**Genetic risk factors.** No genetic risk factor specific to cardiac TB was identified.
- For TB in general, candidate-gene and GWAS results "are largely inconsistent" ([PMC5965286](https://pmc.ncbi.nlm.nih.gov/articles/PMC5965286)).
- HLA-DRB1 and VDR are the most studied candidate genes, with population-specific associations such as DRB1*04 in East Asian populations ([PMC10262011](https://pmc.ncbi.nlm.nih.gov/articles/PMC10262011); [PMC8903186](https://pmc.ncbi.nlm.nih.gov/articles/PMC8903186)).
- Mendelian susceptibility to mycobacterial disease (the IFN-γ/IL-12 axis) has "started to reveal human vulnerabilities against tuberculosis" ([PMC5703416](https://pmc.ncbi.nlm.nih.gov/articles/PMC5703416)). No link to pericardial disease was found.

**Protective factors.**
- No genetic protective factors were identified.
- A paradoxical clinical finding: HIV infection was associated with *less* constriction. The study's conclusion: "HIV infection is associated with a lower incidence of pericardial constriction in patients with presumed tuberculous pericarditis" ([Ntsekhe et al. 2008, PLoS One, PMID 18523576](https://pmc.ncbi.nlm.nih.gov/articles/PMC2386966)).

**Gene–environment interactions.** None were documented for cardiac TB specifically. The HIV × host-immunity interaction is covered in Section 6.

## 3. Phenotypes

Frequency data are sparse. Values are given where they were retrieved.

| Phenotype | Type | Frequency / notes | Suggested HPO label |
|---|---|---|---|
| Pericardial effusion (large) | Sign / imaging | Defining feature. TB caused 69.5% of large effusions in Cape Town (PMID 15962545) | Pericardial effusion |
| Cardiac tamponade | Sign | Part of the IMPI composite outcome (PMID 25178809) | Cardiac tamponade |
| Constrictive pericarditis | Sign | 30–60% before anti-TB therapy; 5–25% in modern prospective cohorts (PMID 31940097); 4.4% with prednisolone vs 7.8% with placebo in IMPI | Constrictive pericarditis |
| Effusive-constrictive physiology | Haemodynamic | "Occurs in half of cases of tuberculous pericardial effusion" ([Ntsekhe 2013, PMC3796485](https://pmc.ncbi.nlm.nih.gov/articles/PMC3796485)) | Pericarditis; Elevated right atrial pressure |
| Fever, night sweats, weight loss | Symptoms | Scored in the Tygerberg score (PMID 17121764) | Fever; Night sweats; Weight loss |
| Raised serum globulin (>40 g/L) | Lab | Tygerberg score item | Hypergammaglobulinemia |
| Blood leukocytes <10×10⁹/L | Lab | Tygerberg score item | — |
| Cardiomegaly / haemodynamic instability | Sign | More common with HIV (IMPI registry 2006) | Cardiomegaly |
| Ascites, pleural effusion | Sign | Predict worse pericardiectomy outcome ([PMC9023633](https://pmc.ncbi.nlm.nih.gov/articles/PMC9023633)) | Ascites; Pleural effusion |
| Myocardial involvement: LV 68%, RV 43%, right atrium 37% | Pathology | Myocarditis case series (PMID 26327955) | Myocarditis |
| Sudden cardiac death | Outcome | 31% of myocarditis cases (PMID 26327955) | Sudden cardiac death |

- **Onset:** mostly in adulthood.
- **Severity:** moderate to life-threatening.
- **Course:** subacute or chronic, and can progress to constriction.
- **Quality of life:** no EQ-5D or SF-36 data specific to cardiac TB were found. Functional limitation is captured indirectly by NYHA class, which improves significantly one year after pericardiectomy ([PMC8544905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8544905/)).

## 4. Genetic/Molecular Information

- **Not applicable:** causal genes, pathogenic variants (ACMG/ClinVar), allele frequencies, somatic or germline origin, and chromosomal abnormalities. Cardiac TB is an infectious disease.
- **Modifier genes:** none established for pericardial disease. General TB susceptibility loci (HLA-DRB1, VDR) are described in Section 2.
- **Epigenetics:** no data were found for cardiac TB.

## 5. Environmental Information

- **Infectious agent:** *Mycobacterium tuberculosis*, an acid-fast bacillus of the *M. tuberculosis* complex. The NCBI Taxon ID was not retrieved in this session.
- **Global TB burden:** an estimated 10.8 million people fell ill with TB in 2023 (134 per 100,000) and there were 1.25 million TB deaths ([WHO Global TB Report 2024](https://www.who.int/publications/m/item/top-findings-and-messages-in-the-2024-report)). The 2025 report gives 10.7 million cases in 2024 ([WHO 2025](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-disease-burden/1-1-tb-incidence)).
- **Co-factor:** HIV-1 infection.
- **Lifestyle and toxic exposures:** no data specific to cardiac TB were retrieved.

## 6. Mechanism / Pathophysiology

**Causal chain**

1. *M. tuberculosis* in the lungs or mediastinal lymph nodes **spreads to** the pericardium by retrograde lymphatic or blood-borne routes (PMID 31940097). This step comes from clinicopathological inference, not direct demonstration.
2. Bacilli in the pericardium **trigger** a dry stage of fibrinous inflammation with granulomas. The classic four stages (dry, effusive, absorptive, constrictive) come from 1940s–50s case series and were not demonstrated prospectively ([Walzl et al. 2019 review](https://core.ac.uk/download/288394373.pdf)).
3. A Th1-driven delayed-hypersensitivity response, with mainly lymphocytes and preferential CD4 T-cell recruitment and high pericardial IFN-γ, **leads to** an exudative effusion. Effusions show "lymphocyte dominance, significantly elevated levels of gamma-interferon (IFN-γ) and undetectable levels of interleukin-4" ([Reuter thesis](https://core.ac.uk/download/37319601.pdf); [PMC9692124](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9692124/)).
4. The effusion builds up and **results in** raised intrapericardial pressure, which leads to tamponade.
5. **Branch A (fibrosis):** a compartmentalized profibrotic response **drives** fibrin organization and pericardial thickening.
   - Pericardial fluid and blood separate into two compartments, with fibrosis-associated genes prominent in pericardial fluid, "irrespective of HIV-1 infection" ([Matthews et al. 2015, AJRCCM, PMID 26669475](https://pmc.ncbi.nlm.nih.gov/articles/PMC4731721)).
   - Fluid shows low AcSDKP and high IFN-γ and IL-10; blood shows high TGF-β and IL-10 ([Isiguzo 2020](https://rd.springer.com/content/pdf/10.1007%2Fs11886-020-1254-1.pdf)).
   - Higher pericardial and serum IL-10 goes with effusive-constrictive disease ([PMC3796485](https://pmc.ncbi.nlm.nih.gov/articles/PMC3796485)).
6. Fibrosis **leads to** effusive-constrictive and then constrictive pericarditis. This causes impaired diastolic filling, raised right-sided pressures, ascites and heart failure.
7. **Branch B (HIV):** HIV co-infection **is associated with** less constriction (PMID 18523576). The proposed explanation is that fewer IL-13-secreting CD4⁺ Th2 cells means less TGF-β1 production by macrophages. This explanation is inferred, not proven.
8. **Branch C (myocardium):** infiltration of the myocardium (diffuse infiltrative, miliary, or nodular with caseation, [PMC8971110](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8971110/)) **leads to** arrhythmia and sudden cardiac death (PMID 26327955).
9. **Drug-penetration factor:** poor pericardial penetration of rifampicin may **allow** bacilli to persist.
   - The pericardial-to-serum ratio was 0.19 ± 0.33.
   - Unbound pericardial rifampicin was about 4-fold below the MIC ([Shenje et al. 2015, EBioMedicine, PMC4740291](https://pmc.ncbi.nlm.nih.gov/articles/PMC4740291)).

**Suggested ontology labels**
- GO: type II interferon (IFN-γ) production; granuloma formation; T-helper 1 type immune response; fibrinolysis; extracellular matrix organization; transforming growth factor beta receptor signaling pathway; interleukin-10 production.
- CL: CD4-positive alpha-beta T cell; CD8-positive alpha-beta T cell; macrophage; epithelioid cell; multinucleated giant cell; fibroblast; mesothelial cell; cardiac muscle cell.

**Omics.** The only data found were the blood versus pericardial-fluid gene-expression compartmentalization study (PMID 26669475). No single-cell, spatial or CRISPR-screen studies were found.

## 7. Anatomical Structures Affected

Suggested UBERON labels:
- **Primary:** pericardium (parietal and visceral layers, pericardial cavity).
- **Secondary:** myocardium (left ventricle most often, then right ventricle and right atrium); mediastinal lymph nodes; lung.
- **Downstream complications:** peritoneal cavity (ascites) and pleural cavity.
- **System:** cardiovascular.
- **Cell level:** mesothelium, fibroblasts, immune infiltrate.
- **Laterality:** not applicable.

## 8. Temporal Development

- **Onset:** adult. In myocarditis, 81% of patients were under 45. Onset is subacute to insidious.
- **Course:** progressive staging from dry to effusive to absorptive to constrictive.
- **Critical period:** the effusive phase, when adjunctive steroids can reduce constriction (IMPI).
- **Remission:** follows anti-TB treatment (ATT). Constriction can develop despite treatment.

## 9. Inheritance and Population

- **Inheritance:** not applicable; the disease is not Mendelian.
- **Annual cases:** an estimated 80,000–160,000 TBP cases per year worldwide ([Ntsekhe & Mayosi 2013, Heart Fail Rev](https://link.springer.com/content/pdf/10.1007/s10741-012-9310-6.pdf)).
- **Geography:** concentrated in sub-Saharan Africa and Asia. TB caused 69.5% (162 of 233) of large effusions at Tygerberg Hospital, versus 9.4% for malignancy (PMID 15962545).
- **Sex ratio:** reported only for myocarditis, at about 2:1 male to female (PMID 26327955).

## 10. Diagnostics

**Pericardiocentesis and fluid analysis.**
- Pericardiocentesis, where the effusion is over 1 cm, "remains an essential part of the approach" (PMID 31940097).
- Accuracy of pericardial fluid tests in a Cape Town cohort of 151 patients ([Pandie et al. 2014, BMC Med, PMC4073812](https://pmc.ncbi.nlm.nih.gov/articles/PMC4073812)):

| Test (cut-off) | Sensitivity | Specificity |
|---|---|---|
| Unstimulated IFN-γ (≥44 pg/mL) | 95.7% | 96.3% |
| ADA (≥35 IU/L) | 95.7% | 84% |
| Xpert MTB/RIF | 63.8% | 100% |

  - The authors concluded that "uIFNγ offers superior accuracy... compared to the ADA assay and the Xpert MTB/RIF test."
- In an earlier cohort, IFN-γ ≥50 pg/mL had 92% sensitivity and 100% specificity, and ADA ≥40 U/L had 87% sensitivity and 89% specificity ([Reuter 2006, QJM, PMID 17121764](https://read.qxmd.com/read/17121764/diagnosing-tuberculous-pericarditis)).
- ADA meta-analyses:
  - pooled sensitivity 0.90 and specificity 0.86 across 11 studies with 938 subjects ([Eur Rev Med Pharmacol Sci](https://www.europeanreview.org/?p=9865));
  - an earlier meta-analysis gave 88% and 83% ([PMID 16950165](https://pubmed.ncbi.nlm.nih.gov/16950165/)).
- Xpert meta-analyses report "robust specificity but unsatisfactory sensitivity" ([PMC7417956](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7417956/); [PMC8432788](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8432788/)). No accuracy study specific to Xpert Ultra was found.

**Other diagnostic elements.**
- **Reference standard:** culture and/or pericardial histology showing granulomas (Pandie 2014).
- **Clinical score:** the Tygerberg score assigns fever 2, night sweats 1, weight loss 1, globulin >40 g/L 3, and leukocytes <10×10⁹/L 3. A score of 6 or more suggests TB, with about 86% sensitivity and 85% specificity (PMID 17121764; [Tygerberg score summary](https://en.wikipedia.org/wiki/Tygerberg_score)).
  - Sources disagree on whether the cut-off is ≥6 or >6.
  - It is prone to misdiagnosing patients with other constitutional illnesses ([CDT review](https://cdt.amegroups.org/article/view/30287/html)).
- **Imaging:** echocardiography, CT and CMR. Specific accuracy data were not retrieved.
- **Genetic testing:** not applicable.
- **Differential diagnosis:** malignant effusion, idiopathic or viral pericarditis, bacterial (purulent) pericarditis, and uraemic pericarditis (PMID 15962545).

## 11. Outcome/Prognosis

- **Mortality in the IMPI registry:** 26% overall; 40% with clinical HIV features versus 17% without ([Mayosi et al. 2008, SAMJ](https://scholar.sun.ac.za/items/ed9dae71-8770-4a98-b742-d73994832e03/full)).
- **IMPI trial composite outcome** (death, tamponade or constriction): about 24% in both arms (PMID 25178809).
- **Tuberculous myocarditis:** 68% responded to ATT, and 31% died of sudden cardiac death (PMID 26327955).
- **Pericardiectomy for TB constriction:**
  - mean in-hospital mortality about 7% across 12 studies with 859 patients ([PMC8544905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8544905/));
  - one series reported 8.6% perioperative mortality, with ascites and symptom duration predicting death ([PMID 16776460](https://www.pubmed.gov/16776460/)).
- **Prognostic factors:** HIV status, ascites or pleural effusion, and advanced NYHA class.

## 12. Treatment

Suggested NCIT labels are given in brackets.

**Anti-tuberculosis therapy** [Antitubercular agent]: standard four-drug therapy (rifampicin, isoniazid, pyrazinamide, ethambutol) for 6 months ([Mayosi 2005 review, PMID 16330703](https://pubmed.ncbi.nlm.nih.gov/16330703)).

**Adjunctive prednisolone** [Corticosteroid] — IMPI trial, 1,400 patients, NCT00810849 (PMID 25178809):
- No effect on the composite outcome: HR 0.95 (95% CI 0.77–1.18).
- Less constriction (4.4% vs 7.8%) and fewer hospitalizations (20.7% vs 25.2%).
- More HIV-associated cancers.

**2017 Cochrane review** (7 trials, 1,959 patients, 54% HIV-positive, [CD000526](https://www.cochrane.org/CD000526)):
- In HIV-negative patients, steroids probably reduce deaths from pericarditis: RR 0.39 (95% CI 0.19–0.80), moderate certainty.
- Constriction: RR 0.55 (95% CI 0.26–1.16), low certainty.

**Immunotherapy with *M. indicus pranii*** [Immunotherapy]: no benefit, and increased cancer risk (IMPI).

**Pericardiocentesis or pericardial drainage** [Pericardiocentesis]: used for tamponade.

**Pericardiectomy** [Pericardiectomy]: used for constriction. NYHA class improves after surgery (PMC8544905).

**Experimental:** IMPI-3 ([NCT04521803](https://clinicaltrials.gov/study/NCT04521803)) compares high-dose rifampicin (35 mg/kg) with standard dosing (10 mg/kg). Its outcomes are pericardial drug exposure and bacillary load. No results were found.

**Pharmacogenomics:** no data specific to cardiac TB were retrieved.

## 13. Prevention

**Primary prevention** is general TB control: case finding, HIV testing and antiretroviral therapy, TB preventive therapy, and BCG vaccination. No sources specific to cardiac TB were retrieved for these.

**Tertiary prevention** of constriction:
- adjunctive prednisolone in suitable patients (IMPI; Cochrane);
- complete drainage of the effusion (mentioned in reviews; not quantified here).

**Not applicable:** genetic counselling and carrier screening.

## 14. Other Species

- **Cattle:** *M. bovis* lesions have been reported in the heart, but pericardial involvement was not described ([Vet Med 2004, DOAJ](https://doaj.org/article/fb5c54caa1c84eab9731777cffc76d8d)).
- **Dog:** a case report describes fibrinous pericarditis and epicarditis caused by *M. tuberculosis* ([BMC Vet Res 2016, PMC4908798](https://pmc.ncbi.nlm.nih.gov/articles/PMC4908798)).
- **Zoonotic potential:** *M. bovis* is zoonotic ([CFSPH factsheet](https://www.cfsph.iastate.edu/Factsheets/pdfs/bovine_tuberculosis.pdf)).
- **OMIA:** not applicable.

## 15. Model Organisms

- **No dedicated animal model of tuberculous pericarditis was found.**
- **Closest analogue:** a guinea pig model of tuberculous pleuritis, made by injecting heat-killed *M. tuberculosis* into the pleural cavity of BCG-vaccinated animals ([PMC302698](https://pmc.ncbi.nlm.nih.gov/articles/PMC302698)).
- **General TB models:** guinea pig (disseminated disease) and mouse (mechanistic studies). Rabbit models are used for other forms of extrapulmonary TB, such as meningitis ([PMC7078415](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7078415/)).
- **Implication:** pericardial fibrosis and constriction have not been reproduced in an animal model. Mechanistic understanding rests on human pericardial fluid studies.

---

### Main gaps
- ICD, Orphanet and MeSH codes were not retrieved.
- No quality-of-life data or animal models specific to cardiac TB exist in the sources found.
- No published IMPI-3 results were found.
- Ontology IDs need to be looked up.
- Several figures come from abstracts or snippets and should be checked against the full texts.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 3 |
| Quoted claims with nothing to check against | 3 |
| References weighed for topical relevance | 32 |
| On topic | 16 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC5703416` *(abstract only)*: "started to reveal human vulnerabilities against tuberculosis"
  - closest text in source: "This short review aims to summarize recent advances and to provide a link with results of previous human genetic studies of tuberculosis susceptibility"
- `PMC:PMC9692124` *(abstract only)*: "lymphocyte dominance, significantly elevated levels of gamma-interferon (IFN-γ) and undetectable levels of interleukin-4"
  - closest text in source: "Upon ATT completion, HLA-DR, Ki-67 and GrB expression was significantly decreased, and relative IL-2 production was increased in peripheral Mtb-specific CD4 T cells"
- `PMC:PMC8432788` *(abstract only)*: "robust specificity but unsatisfactory sensitivity"
  - closest text in source: "CONCLUSIONS: The sensitivity of Xpert MTB/RIF for diagnosing TBP was moderate and the specificity was good; thus, Xpert MTB/RIF can be used in the initial diagnosis of TBP."

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:26320112`: "the most common cause of pericardial diseases all over the world and especially relevant in developing countries"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:26669475`: "irrespective of HIV-1 infection"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC4731721`: "irrespective of HIV-1 infection"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.