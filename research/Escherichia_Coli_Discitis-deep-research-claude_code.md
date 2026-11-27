---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T02:01:43.592376'
end_time: '2026-11-26T02:04:43.125587'
duration_seconds: 179.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Escherichia coli Discitis
  mondo_id: MONDO:8000002
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
  web_search_requests: 19
  num_turns: 27
  total_cost_usd: 1.2817121000000002
  session_id: 8f142ed4-6e49-49e4-8d99-89f8809bc7d5
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  tool_calls: 26
  retrieval_calls: 20
  assistant_text_blocks: 2
citation_count: 31
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 7
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMC:PMC5452335
  - PMC:PMC3282859
  - PMC:PMC4676899
  quotes_not_checkable: 2
  relevance_assessed: 29
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:37288966
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 4
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - GARD
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Escherichia coli Discitis
- **MONDO ID:** MONDO:8000002 (if available)
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

Please provide a comprehensive research report on **Escherichia coli Discitis** covering all of the
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

Bash is blocked here, so I'm moving to web search to find sources.

# Escherichia coli discitis (MONDO:8000002): disease characteristics report

**How I interpreted the request.** MONDO:8000002 is an infectious disease, so it has **no causal human gene**. The cause is the bacterium *Escherichia coli*. Specific *E. coli* literature is scarce: it is mostly case reports, one small literature review, and Gram-negative subgroups inside larger pyogenic spondylodiscitis cohorts. Where only that general evidence exists, I use it and say so.

**How I retrieved sources.** Shell access to PubMed's E-utilities was blocked in this session, so all sources came from web search. Many items are cited by PMC ID or DOI because I could not retrieve their PMIDs, and I did not invent any.

**Ontology identifiers.** Only the MONDO and GARD identifiers below were retrieved. HPO, GO, CL, UBERON, CHEBI and NCIT terms are given as **labels only**. Their IDs need to be looked up and checked before curation.

---

## 1. Disease information

**Overview.** MONDO defines *E. coli* discitis as "discitis caused by infection with Escherichia coli" ([SAIL concept library, MONDO:8000002](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:8000002/)).
- It is an infection of the intervertebral disc space, which in practice almost always spreads to the neighbouring vertebral endplates. That combined form is called spondylodiscitis or vertebral osteomyelitis.
- A 2019 review calls it "a relatively rare disease that usually has a urinary tract infection as its source," with symptoms "not distinguishable from vertebral osteomyelitis caused by other agents" ([Salehi et al., Jundishapur J Microbiol 2019;e99694](https://brieflands.com/articles/jjm-99694.html)).

**Identifiers**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:8000002 "escherichia coli discitis" |
| MONDO parents | infectious discitis (MONDO:8000000); *E. coli* infection (MONDO:0020920); bacterial arthritis |
| GARD | GARD:0028190 |
| OMIM / Orphanet | None (not a Mendelian or rare-disease entity) |
| ICD-10 / ICD-11 / MeSH | No organism-specific code retrieved. Generic codes (infection of intervertebral disc, pyogenic; MeSH "Discitis") apply, but I did not verify them in this session. |

The MONDO parents and the GARD cross-reference are from the [SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:8000002/).

**Synonyms.** None are recorded. Terms used in the literature are:
- *E. coli* spondylodiscitis
- *E. coli* vertebral osteomyelitis
- urogenic spondylodiscitis (when the source is the urinary tract)
- Gram-negative bacillary hematogenous pyogenic spondylodiscitis (GNB-HPS)

**Nature of the evidence.** All evidence comes from individual patients: case reports and retrospective hospital cohorts. There is no aggregated registry specific to this entity.

---

## 2. Etiology

**Causal factor.** Infection with *E. coli*, almost always reaching the spine through the bloodstream (hematogenous spread).
- Pediatric strains have been characterised as extraintestinal pathogenic *E. coli* (ExPEC). One example is an O1:K1, phylogroup B2 strain carrying "virulence factors typical of highly virulent ExPEC strains" ([Gaschignard et al., BMC Infect Dis 2017, DOI 10.1186/s12879-017-2486-6; PMC5452335](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5452335/)).

**Risk factors (all clinical, human evidence)**

- **Genitourinary or intra-abdominal infection is the main risk factor.**
  - A four-hospital Korean cohort found Gram-negative organisms in 18.0% of pyogenic spondylitis cases. *E. coli* was the most common of them (35 cases, 10.2% of all cases).
  - That cohort reported prior or concurrent genitourinary infection in 32.3% of Gram-negative cases versus 2.1% of Gram-positive cases.
  - The authors concluded: "GNB should be considered as the etiologic organism when infectious spondylitis develops in a patient with preexisting or synchronous genitourinary tract and intra-abdominal infection" ([Kang et al., PLoS ONE 2015; PMC4433234](https://pmc.ncbi.nlm.nih.gov/articles/PMC4433234)).
- **Prior symptomatic urinary tract infection (UTI).** In a comparison of 17 Gram-negative and 37 Gram-positive hematogenous cases, a previous symptomatic UTI was found in "41% vs. 3%, respectively; p = 0.03" ([Lee et al., BMC Infect Dis 2016;16:735, DOI 10.1186/s12879-016-2071-4; PMC5139091](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5139091/)).
- **Older age and a history of cancer** were more common in Gram-negative cases in the same study (PMC5139091).
- **Age and sex.** Incidence of pyogenic spondylodiscitis is highest in elderly people ([Kehrer et al., J Infect 2014; PMID 24296494](https://api-pubmed-ncbi.laibokeji.com/24296494)). *E. coli* cases are reported as more common in adults and in males. The 10-patient review had 6 males and 4 females, with a mean age of 52 and a range of 12–69 years ([Salehi 2019](https://brieflands.com/articles/jjm-99694.html)).
- **Comorbidities seen in pyogenic vertebral osteomyelitis generally** include diabetes, renal disease and heart failure (see §11).
- **Host immunosuppression.** Authors recommend looking for it when *E. coli* is found, even though the pediatric index case had a normal immunological work-up (PMC5452335).

**Genetic risk or protective factors.** I found no human susceptibility loci, GWAS hits or protective variants.

**Environmental protective factors.** None specific are documented. Preventing and treating UTIs promptly is the logical protective measure, but this is inferred, not tested.

**Gene–environment interactions.** None documented.

---

## 3. Phenotypes

Frequencies for *E. coli* specifically come only from the 10-patient series, so most are qualitative.

| Phenotype | HPO label (ID to verify) | Type | Evidence and frequency |
|---|---|---|---|
| Back pain (lumbar, thoracic) | Low back pain; Back pain | Symptom | Main presenting complaint in case reports (for example, L2–L3 disease with low back pain, Salehi 2019). In Gram-negative cases, spinal pain is *less often* the first complaint than constitutional symptoms (PMC5139091). |
| Fever | Fever | Sign | Common (Salehi 2019 case; persistent fever with recurrent bacteremia, [PMC12707976](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12707976/)) |
| Weight loss and constitutional symptoms | Weight loss; Malaise | Symptom | "Constitutional symptoms were the primary reasons for initial physician visits in GNB-HPS patients" (PMC5139091) |
| Bacteremia (*E. coli*) | Bacteremia | Laboratory | Positive blood cultures in 7 of 10 reviewed patients (Salehi 2019); can be recurrent (PMC12707976) |
| Concurrent UTI or bacteriuria | Recurrent urinary tract infections; Bacteriuria | Laboratory and history | Positive urine culture in several cases; urinary tract is the origin in at least 50% of reviewed cases |
| Raised ESR and CRP | Elevated erythrocyte sedimentation rate; Elevated C-reactive protein level | Laboratory | Standard diagnostic markers ([PMC3282859](https://pmc.ncbi.nlm.nih.gov/articles/PMC3282859)) |
| Epidural abscess | Spinal epidural abscess | Complication | *Less* frequent in Gram-negative than Gram-positive cases (PMC5139091) |
| Neurological deficit (motor weakness) | Lower limb muscle weakness | Complication | Predicts poor outcome in pyogenic vertebral osteomyelitis generally (see §11) |
| Fever of unknown origin | Fever of unknown origin | Presentation | Multidrug-resistant ESBL *E. coli* case at T11–L1 ([Pan Afr Med J 2025](https://www.panafrican-med-journal.com//content/article/51/27/full)) |

- **Onset:** subacute or insidious. A delay of up to several months before diagnosis is typical because the presentation is nonspecific.
- **Severity:** moderate to severe.
- **Course:** progressive if untreated.
- **Quality of life:** pain and immobility dominate. I retrieved no EQ-5D or SF-36 data specific to *E. coli*.

---

## 4. Genetic / molecular information

**Host side.** Not applicable. There are no causal genes, pathogenic variants (ClinVar), modifier genes, epigenetic findings or chromosomal abnormalities for this infectious entity.

**Pathogen side (*E. coli*)**

- **Phylogroups.** B2 predominates in bone and joint *E. coli* isolates:
  - 53.9% of prosthetic-joint-infection isolates were B2, with ST131 and ST69 the most common sequence types ([PMC12795266](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12795266/)).
  - In diabetic-foot osteomyelitis, "the majority of the strains belonged to the virulent B2 and D phylogenetic groups (82%)" ([PMC7918245](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7918245/)).
- **Virulence genes.** Genes reported in bone-infection isolates include *fimH* (type 1 fimbrial adhesin), *papC*/*papG* (P fimbriae) and *iucC* (aerobactin siderophore). Some isolates were linked to lysis of osteoblasts in vitro ([PMC4626605](https://pmc.ncbi.nlm.nih.gov/articles/PMC4626605)).
  - No virulence signature specific to bone infection has been established. One study found no molecular signature separating these isolates from uropathogenic strains.
- **Resistance genes.** Cases with ESBL-producing strains (for example CTX-M-9) are reported ([Kohlmann et al., BMC Infect Dis 2015; PMC4676899](https://pmc.ncbi.nlm.nih.gov/articles/PMC4676899)).

---

## 5. Environmental information

- **Infectious agent:** *Escherichia coli*, usually from a urinary, and less often intra-abdominal, source. The NCBI Taxonomy ID was not retrieved in this session.
- **Hospital vs community:** cases occur in both. A community-acquired case is reported in [Bull Emerg Trauma 2016](https://doaj.org/article/f7a1c59c39c740458c359673cf0d131c).
- **Lifestyle and toxin factors:** none specific are documented.

---

## 6. Mechanism / pathophysiology

**Causal chain.** Steps marked *inferred* come from general osteomyelitis biology rather than *E. coli*-specific studies.

1. A urinary tract (or intra-abdominal) infection with an ExPEC/uropathogenic *E. coli* strain **leads to** bacteria entering the bloodstream (bacteremia). This is documented in case series: positive blood cultures in 7 of 10 patients, urinary source in at least 50%.
2. Bacteremia **results in** bacteria seeding the vertebral endplate. There are two proposed routes:
   - **Arterial route:** bacteria lodge in endplate end-arterioles. This is *inferred* from general reviews.
   - **Venous route:** retrograde flow through the valveless Batson vertebral venous plexus, which joins the pelvic veins to the internal vertebral venous plexus, especially when intra-abdominal pressure rises. This route is *speculative and contested*: one 2025 case report calls the mechanism "speculative," and an early experimental study concluded "our studies do not support the supposition that infection is likely to spread by this route" ([Batson plexus summary; JBJS 41B:796](https://boneandjoint.org.uk/Article/10.1302/0301-620X.41B4.796)).
3. Bacterial adhesins and iron-scavenging factors (such as fimbriae and aerobactin) **lead to** persistence in bone. Osteoblast lysis has been shown in vitro (PMC4626605). Whether this is the key step in humans is *inferred*.
4. Innate immune recognition of lipopolysaccharide (LPS) **results in** neutrophil and macrophage influx and suppurative inflammation. The cytokine details are *inferred* (I retrieved no disease-specific study).
5. Inflammation and enzymatic and ischemic damage **lead to** destruction of the endplate. The infection then spreads into the avascular disc, which is discitis proper.
6. From there the process **branches**:
   - **6a.** Local pain and loss of spinal stability lead to back pain and immobility.
   - **6b.** Spread into the soft tissues leads to paravertebral, psoas or epidural abscess. Epidural abscess is less common with Gram-negative organisms (PMC5139091). It can compress the cord or nerve roots and cause neurological deficit.
   - **6c.** Systemic signs: persistent or recurrent bacteremia, fever and weight loss.

**Suggested terms (labels only)**
- GO biological processes: neutrophil chemotaxis; inflammatory response; response to lipopolysaccharide; cell adhesion involved in biofilm formation; siderophore biosynthetic process (pathogen); bone resorption.
- CL cell types: neutrophil; macrophage; osteoblast; osteoclast; chondrocyte (nucleus pulposus and annulus fibrosus cells).

**Not available:** transcriptomic, proteomic, metabolomic, single-cell or spatial studies specific to *E. coli* discitis.

---

## 7. Anatomical structures affected

- **Primary site:** intervertebral disc and adjacent vertebral bodies and endplates. Suggested UBERON labels: intervertebral disk; vertebral body; lumbar vertebra; thoracic vertebra.
- **Spinal level:** lumbar disease is typical (L2–L3 in Salehi 2019). Thoracolumbar cases also occur (T11–T12 in PMC5452335; T11–L1 in Pan Afr Med J 2025). Cervical disease is reported with meningitis and retropharyngeal abscess (PMC4676899).
- **Secondary sites:** epidural space; paravertebral and psoas muscles; meninges (rare); the urinary tract as the primary focus.
- **Tissues:** bone, fibrocartilage and bone marrow.
- **Laterality:** midline, so not lateralised. Usually one level is involved; several levels raise mortality (§11).

---

## 8. Temporal development

- **Onset:** mainly adults and the elderly, although pediatric cases exist (12-year-old, PMC5452335). Onset is subacute or insidious, with diagnostic delays of weeks to months.
- **Course without treatment:** progressive destruction and abscess formation.
- **Remission:** induced by treatment. Cure rates are about 90% at one year with 6 weeks of antibiotics (in pyogenic vertebral osteomyelitis overall, §12).
- **Critical window:** early diagnosis before neurological compromise or abscess formation.
- **Relapse:** recurrent bacteremia can occur if the source is not controlled (PMC12707976).

---

## 9. Inheritance and population

**Inheritance.** Not applicable (acquired infection). Penetrance, anticipation, founder effects and carrier frequency do not apply.

**Epidemiology**
- In Funen, Denmark (adults), incidence of all pyogenic spondylodiscitis rose from **2.2 to 5.8 per 100,000 person-years** between 1995 and 2008. It was highest in older patients. The authors note it is unknown whether the rise "is real or is a result of improved diagnostic methods" ([Kehrer 2014, PMID 24296494](https://api-pubmed-ncbi.laibokeji.com/24296494)).
- Gram-negative organisms cause 15–39% of cases in various series. *E. coli* accounted for about 10% of pyogenic spondylitis in the Korean cohort (PMC4433234).
- Urogenic spondylodiscitis is about 6.2% of pyogenic discitis cases (quoted in case-report reviews).
- I retrieved no incidence figure specific to *E. coli*.

**Demographics**
- Sex: male predominance in the small review (6 males, 4 females).
- Age: incidence rises with age.
- Gram-negative infection is suspected more often in women with a urinary source (reviews).
- No geographic or ethnic clustering is reported.

---

## 10. Diagnostics

**Microbiology**
- **Blood cultures** are the key test; 7 of 10 were positive (Salehi 2019).
- **Urine culture** looks for the source.
- **Image-guided or open biopsy** when blood cultures are negative. In an Australian cohort, open biopsy yielded 70%, fine-needle aspirate 41% and core biopsy 30% ([PMC5846292](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5846292/)).
- **Antibiotic susceptibility testing**, including for ESBL production.

**Laboratory and imaging**
- ESR and CRP are useful; white cell count is less so.
- MRI with gadolinium "is considered the best choice for image diagnosis of spondylodiscitis because of its high sensitivity and specificity" ([PMC3282859](https://pmc.ncbi.nlm.nih.gov/articles/PMC3282859)).

**Guidelines**
- The IDSA 2015 native vertebral osteomyelitis guideline says MRI is often needed, plain radiographs are insensitive early on, and empirical antibiotics should be withheld until a microbiological diagnosis unless the patient is septic or neurologically compromised ([Berbari et al., Clin Infect Dis 2015;61:e26–46, PMID 26229122](https://pubmed.ncbi.nlm.nih.gov/26229122/); executive summary [PMID 26316526](https://pubmed.ncbi.nlm.nih.gov/26316526/)).
- An EANM/ESNR/ESCMID consensus on diagnosing spine infection was published in 2019 ([DOI 10.1007/s00259-019-04393-6](https://link.springer.com/10.1007/s00259-019-04393-6)).

**Genetic testing.** Not applicable for the host. Pathogen whole-genome sequencing and serotyping (for example O1:K1, phylogroup B2) are research tools.

**Differential diagnosis**
- *S. aureus* and other pyogenic spondylodiscitis. Gram-negative cases present more with constitutional symptoms and have fewer epidural abscesses (PMC5139091).
- Tuberculous (Pott) and *Brucella* spondylitis.
- Erosive degenerative (Modic) changes.
- Spinal metastasis.

**Screening.** No asymptomatic screening exists.

---

## 11. Outcome / prognosis

**Comparison with Gram-positive disease**
- Outcomes are similar. "The mortality rate and clinical outcomes are not significantly different between pyogenic spondylitis caused by GNB and GPC" (PMC4433234).
- Outcomes with combined surgery and antibiotics were "not different" (PMC5139091).

**Prognostic factors in pyogenic vertebral osteomyelitis generally**
- Adverse outcome occurred in 28% of one cohort. Independent predictors were *S. aureus* infection, motor weakness and a sinus tract ([PMC6680037](https://pmc.ncbi.nlm.nih.gov/articles/PMC6680037)).
- One-year mortality rose with age (OR 1.07) and with the number of vertebral levels involved (OR 2.30).
- In-hospital death was linked to renal disease (OR 1.85) and congestive heart failure (OR 1.52).
- In 9,753 patients, diabetes with complications (OR 1.86) was associated with in-hospital death ([PMC10381366](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10381366/)).

**Mortality and cure**
- Death was the most common adverse event in the Bernard trial: 8% in the 6-week arm and 7% in the 12-week arm ([PMID 25468170](https://pubmed.ncbi.nlm.nih.gov/25468170/)).
- The *E. coli* case reports mostly resolved with medical therapy alone.

**Complications.** Epidural abscess, neurological deficit, spinal instability or deformity, recurrent bacteremia, and meningitis (rare).

**Quality of life.** No *E. coli*-specific data were retrieved.

---

## 12. Treatment

**Antibiotics** (NCIT labels suggested: Antibiotic Therapy; Ceftriaxone; Ciprofloxacin; Meropenem)
- **Third-generation cephalosporins** such as ceftriaxone. French guidance favours a third-generation cephalosporin combined with a fluoroquinolone for *E. coli* spondylodiscitis (PMC5452335).
- **Fluoroquinolones.** Oral ciprofloxacin for a susceptible strain achieved cure after 8 weeks without surgery (Salehi 2019).
- **Carbapenems for ESBL strains.** In a CTX-M-9 ESBL case, meningitis and osteomyelitis resolved "after surgery and meropenem therapy" (PMC4676899).

**Duration**
- Six weeks was non-inferior to 12 weeks in pyogenic vertebral osteomyelitis: risk difference 0.05% (95% CI −6.2 to 6.3); about 90.9% vs 90.8% cured at one year ([Bernard et al., Lancet 2015;385:875–82, PMID 25468170](https://pubmed.ncbi.nlm.nih.gov/25468170/); NCT00764114).
- Longer courses may be needed for drug-resistant organisms, extensive bone destruction or abscesses.

**Route**
- Oral therapy was non-inferior to intravenous therapy in the first 6 weeks of bone and joint infection. Treatment failure was 13.2% oral vs 14.6% IV, and catheter complications were 1.0% vs 9.4% (OVIVA trial, [NEJM 2019;380:425–36, PMID 30699315](https://pubmed.ncbi.nlm.nih.gov/30699315/)).
- Highly bioavailable fluoroquinolones make an early switch to oral therapy practical for susceptible *E. coli*.

**Surgery** (NCIT labels: Debridement; Spinal Fusion; Decompression)
- Indicated for neurological compromise, abscess, instability or failure of medical therapy. The 2025 EANS consensus describes surgery "to debride the infection, decompress neural structures, and stabilize the affected spinal segments."

**Source control and supportive care**
- Treat the urinary or abdominal source.
- Pain control, orthoses and mobilisation or rehabilitation.

**Pharmacogenomics, gene therapy, cell therapy and other advanced therapeutics.** Not applicable. No specific experimental trials were found.

---

## 13. Prevention

- **Primary:** prevent and treat UTIs and intra-abdominal infections promptly. No *E. coli* vaccine is licensed.
- **Secondary:** consider spondylodiscitis in patients with *E. coli* bacteremia plus back pain, or with persistent bacteremia or fever. Get MRI early.
- **Tertiary:** an adequate antibiotic course, source control, and monitoring for relapse.
- **Not applicable:** genetic counselling and screening.

---

## 14. Other species

- **Dogs.** Canine discospondylitis is common in veterinary practice. Staphylococci dominate (23 of 38 positive blood cultures in 386 dogs; Cridge et al., JVIM 2023, [PMID 37288966](https://pubmed.ncbi.nlm.nih.gov/37288966/)). Culture was positive in 42% of 120 dogs and was associated with higher bodyweight ([Liverpool repository](https://livrepository.liverpool.ac.uk/3179460/)). I found no dog-specific *E. coli* counts.
- **Cats.** *E. coli* was isolated (from urine) in a feline discospondylitis series ([PMC11209358](https://pmc.ncbi.nlm.nih.gov/articles/PMC11209358)).
- **Zoonotic potential:** none specific to this disease.
- **Orthologous genes and breeds:** not applicable.

---

## 15. Model organisms

Existing models use **S. aureus**. I found **no *E. coli* intradiscal model**.

| Model | Description | Source |
|---|---|---|
| Rat tail disc, bioluminescent *S. aureus* | In vivo tracking of infection intensity | [PMC5459675](https://pmc.ncbi.nlm.nih.gov/articles/PMC5459675) |
| Rat lumbar *S. aureus* (ATCC 25923) | Mimics primary pyogenic spondylitis; does not reproduce hematogenous spread | [PMC12488691](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12488691/) |
| Rat coccygeal disc with posterior fixation | Studies infection control with instrumentation | [Eur Spine J 2025](https://link.springer.com/article/10.1007/s00586-025-08750-y) |
| Rabbit lumbar disc, *S. aureus* vs *P. acnes* | MRI and histological changes | [PMC4746301](https://pmc.ncbi.nlm.nih.gov/articles/PMC4746301) |
| Review of models (mouse, rat, chicken, rabbit, dog, sheep) | Notes *S. aureus* "followed by Escherichia coli" in human spine infection | [PMC8313152](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8313152/) |

**Main limitation:** none of these models reproduces urinary-tract-to-spine spread of a Gram-negative organism. In vitro osteoblast infection with ExPEC is the only *E. coli*-specific experimental system I found (PMC4626605).

---

## Evidence gaps

- There are no prospective or *E. coli*-specific cohorts. Most specific data come from 10 or fewer case reports.
- There is no host-genetic data.
- The role of Batson's plexus in the mechanism is unresolved.
- No incidence figure specific to *E. coli* was retrieved.
- No *E. coli* animal model was found.
- PMIDs for several sources (Kang 2015, Lee 2016, Gaschignard 2017, Salehi 2019, Zimmerli NEJM 2010, DOI 10.1056/NEJMcp0910753) were not retrieved, so they are cited by PMC ID or DOI.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 3 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 29 |
| On topic | 11 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

2 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC5452335`: "virulence factors typical of highly virulent ExPEC strains"
  - closest text in source: "The strain harboured serogroup O1:K1 and virulence factors common to highly virulent extra intestinal pathogenic E"
- `PMC:PMC3282859` *(abstract only)*: "is considered the best choice for image diagnosis of spondylodiscitis because of its high sensitivity and specificity"
  - closest text in source: "MRI with gadolinium enhancement is the choice for image diagnosis"
- `PMC:PMC4676899` *(abstract only)*: "after surgery and meropenem therapy"
  - closest text in source: "Meningitis and osteomyelitis resolved completely under surgical treatment and meropenem therapy"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:37288966` (3 mentions) - Clinical features, comparative imaging findings, treatment, and outcome in dogs with discospondylitis: A multi-institutional retrospective study.
  - shared terms: disease

Weighed against this report's own most characteristic terms: `coli`, `infection`, `pyogenic`, `vertebral`, `osteomyelitis`, `gram-negative`, `patient`, `urinary`, `spondylodiscitis`, `abscess`, `disease`, `salehi`, `cohort`, `found`, `tract`, `spinal`, `bacteremia`, `gene`, `pmc5139091`, `antibiotic`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1186/s12879-017-2486-6`: "virulence factors typical of highly virulent ExPEC strains"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1186/s12879-016-2071-4`: "41% vs. 3%, respectively; p = 0.03"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `GARD`.

3 of 4 terms resolved to a current term; the rest could not be looked up either way.