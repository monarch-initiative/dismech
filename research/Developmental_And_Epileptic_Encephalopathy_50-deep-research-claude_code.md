---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-24T15:47:25.024225'
end_time: '2026-08-24T15:53:41.355869'
duration_seconds: 376.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Developmental and Epileptic Encephalopathy 50
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
  web_search_requests: 16
  num_turns: 26
  total_cost_usd: 1.8620243999999997
  session_id: d5430dc8-cc9c-5a8f-9365-64cb735827c4
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 15
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 5
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMC:PMC10921618
  - PMC:PMC7951104
  relevance_assessed: 9
  on_topic: 9
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental and Epileptic Encephalopathy 50
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy 50** covering all of the
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

I'll research this using web search and fetch tools to gather accurate, citable information.

Now let me gather additional details on OMIM clinical synopsis, gene function/pathway details, and other key papers (Ng 2015 original discovery, expanded cohort paper, GeneReviews/Orphanet, HPO terms).

I now have sufficient primary-literature detail to write the full report.

# Developmental and Epileptic Encephalopathy 50 (DEE50 / CAD Deficiency): Comprehensive Research Report

## 1. Disease Information

**Overview.** Developmental and Epileptic Encephalopathy 50 (DEE50), also known as Early Infantile Epileptic Encephalopathy-50 (EIEE50) or **CAD deficiency**, is an ultra-rare autosomal recessive inborn error of pyrimidine *de novo* biosynthesis. It is caused by biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic variants in the **CAD** gene (chromosome 2p23.3), which encodes the trifunctional/tetrafunctional enzyme catalyzing the first three (some sources say four, counting the glutaminase domain) steps of pyrimidine synthesis. The disease is characterized by early-onset, drug-refractory epilepsy, global developmental delay/regression, dyserythropoietic (typically macrocytic or normocytic) anemia with anisopoikilocytosis, and progressive brain atrophy — but it is one of the relatively few genetic epileptic encephalopathies that is **directly and often dramatically treatable** with exogenous uridine, which bypasses the metabolic block via the pyrimidine salvage pathway (Koch et al., *Brain* 2017, PMID: 28007989; case report/review, PMC10921618).

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM | #616457 |
| MedGen | UID 904125 / UMLS C4225320 |
| Monarch/Mondo | MONDO:0014647 |
| Orphanet | ORPHA448010 |
| Gene (CAD) | HGNC:1424; chr2p23.3; NCBI Gene ID 790 |
| Disease Ontology | DOID:0080419 |

**Synonyms:** Early Infantile Epileptic Encephalopathy 50 (EIEE50); CAD deficiency; CAD-CDG (when framed as a congenital disorder of glycosylation, since UDP-sugar donors are also depleted).

**Data provenance:** Because DEE50 is extremely rare (approximately 40–50 molecularly confirmed patients reported worldwide as of 2024–2025), the evidence base is derived almost entirely from **aggregated case reports and small case series** (individual families identified by exome/genome sequencing) rather than large-cohort EHR or registry data — i.e., this is a "disease-level resource" literature, built up patient-by-patient since the first description in 2015.

Source: [OMIM #616457](https://omim.org/entry/616457), [MedGen DEE50](https://www.ncbi.nlm.nih.gov/medgen/904125), [Malacards DEE50](https://www.malacards.org/card/developmental_and_epileptic_encephalopathy_50)

---

## 2. Etiology

### Disease Causal Factors
DEE50 is **monogenic**, caused exclusively by biallelic pathogenic variants in **CAD**. There is no known environmental, infectious, or purely mechanistic (non-genetic) cause. The gene product is essential for the first steps of *de novo* pyrimidine nucleotide synthesis; loss of activity produces a cellular pyrimidine (UMP/UTP/CTP) and UDP-sugar deficit that is particularly damaging to the developing nervous system and erythropoiesis.

### Risk Factors
- **Genetic:** Biallelic CAD variants are necessary and sufficient. Consanguinity substantially raises risk in affected families — the literature review by PMC10921618 found 5 of 42 published cases had consanguineous parents, and 12 had a positive family history. A **founder mutation** (p.Met33Arg) was identified in unrelated Serbian Roma families in the original description (Koch et al. 2017), consistent with an ethnically enriched allele in that population.
- **Environmental:** None established; this is a purely genetic/metabolic disease.
- **Sex:** No sex-linked susceptibility (autosomal recessive); however, the "Tale of Two Siblings" report (PMC7951104) noted an affected brother had an earlier and more severe course than his affected sister despite identical genotype — attributed to earlier diagnosis/treatment timing rather than sex per se.

### Protective Factors
- **Genetic:** None specific (a wild-type or hypomorphic-but-functional CAD allele on at least one chromosome is fully protective — heterozygous carriers are asymptomatic).
- **Environmental:** Dietary/exogenous pyrimidine (uridine) intake is the key modifiable protective/therapeutic factor, since it engages the salvage pathway independent of the defective *de novo* route.

### Gene-Environment Interactions
The core "interaction" in this disease is pharmacogenomic rather than classically environmental: CAD-deficient cells cannot synthesize sufficient pyrimidines *de novo*, but retain an intact salvage pathway (uridine kinase/UMP synthase route), so **exogenous dietary uridine supplementation functionally substitutes for the genetic lesion**. Cell-based functional assays (Genetics in Medicine 2020, PMID: 32117025-adjacent work, "Cell-based analysis of CAD variants identifies individuals likely to benefit from uridine therapy") explicitly test which variants retain enough salvage-pathway responsiveness to predict clinical benefit — a genotype-driven precision-therapy interaction.

Suggested ontology terms: MONDO:0014647 (disease); HGNC:1424 (gene); GO:0006207 (‘de novo’ pyrimidine nucleobase biosynthetic process).

---

## 3. Phenotypes

DEE50 phenotypes cluster into neurological, hematological, and (less consistently) systemic/metabolic domains. Frequencies below are drawn from the pooled literature review of 42 published cases (PMC10921618) unless otherwise cited.

### Neurological / Developmental
| Phenotype | Frequency | HPO term (suggested) |
|---|---|---|
| Global developmental delay / regression | 95% | HP:0011344 (Progressive developmental regression) / HP:0001263 (Global developmental delay) |
| Refractory/drug-resistant epilepsy | 73% (of the cohort); 64% of those with epilepsy were drug-refractory | HP:0011451 (Drug-resistant epilepsy) |
| Focal seizures | 41% of seizure cases | HP:0007359 (Focal-onset seizure) |
| Generalized tonic-clonic seizures | 37% | HP:0002069 (Bilateral tonic-clonic seizure) |
| Myoclonic seizures | 8% | HP:0032794 (Myoclonic seizure) |
| Status epilepticus | 45% of epilepsy cases | HP:0002133 (Status epilepticus) |
| Heat-sensitive seizures | 13% | HP:0011175 (Fever-induced seizure descriptors) |
| Ataxia | 73% of extrapyramidal cases | HP:0001251 (Ataxia) |
| Tremor | 36% | HP:0001337 (Tremor) |
| Hypotonia | 14% | HP:0001252 (Hypotonia) |
| Dysphagia | 23% | HP:0002015 (Dysphagia) |
| Gait abnormality | 26% | HP:0001288 (Gait disturbance) |
| Extrapyramidal/movement disorder (general) | 33% | HP:0002071 (Abnormality of extrapyramidal motor function) |

- **Onset:** Mean age of first symptoms 1.6 ± 1.8 years; 90% before age 3; some neonatal-onset cases (3/42) and a spectrum extending to milder, later-onset isolated developmental delay/intellectual disability (Rymen et al., *Genetics in Medicine* 2021, "Expanding the clinical and genetic spectrum of CAD deficiency," PMID search via GIM/ScienceDirect S1098360021007607).
- **Severity/progression:** Progressive and, if untreated, can be lethal in early childhood (Koch et al. 2017 abstract: "the natural disease course can be lethal in early childhood"). With uridine treatment the course is frequently arrested or reversed.
- **Diagnostic lag:** Mean age at diagnosis 7.7 ± 10 years vs. mean onset 1.6 years — a roughly 6-year diagnostic delay, reflecting the rarity and non-specific early presentation.

### Hematological
| Phenotype | Frequency | HPO term |
|---|---|---|
| Anemia (typically macrocytic or normocytic; occasionally microcytic hypochromic) | 71% | HP:0001903 (Anemia) |
| Anisocytosis / poikilocytosis (target cells, teardrop cells, acanthocytes) | present in ~1/3 with detailed morphology reported | HP:0011273 (Anisopoikilocytosis) |
| Dyserythropoiesis | reported in original Koch et al. cohort | HP:0012156 (dyserythropoiesis-adjacent term) |
| Elevated hemoglobin A2 (in the hypomorphic/milder allelic series) | isolated report | — |

A distinct, milder **allelic** presentation was described in 2023: biallelic *hypomorphic* CAD variants causing **uridine-responsive macrocytic anemia with elevated hemoglobin-A2** and only mild developmental delay, without epileptic encephalopathy — demonstrating that CAD deficiency is a phenotypic continuum from a primarily hematologic disorder to the classic severe DEE (Br J Haematol 2023, PMID: 37984840).

### Other systemic/metabolic phenotypes (from MedGen clinical synopsis)
- Failure to thrive (HP:0001508)
- Orotic aciduria (HP:0003132) — reflects downstream metabolic consequences
- Hyperammonemia (HP:0001987) and renal tubular acidosis (HP:0001947) — reported metabolic complications
- Abnormal glycosylation (relevant to the "CAD-CDG" framing, since UDP-sugar precursors are also depleted)
- Speech difficulties/absent language (HP:0002465 / HP:0001344)
- Diarrhea (HP:0002014)

### Neuroimaging (a semi-quantitative/imaging phenotype)
57% of cases had abnormal brain MRI; of these, 73% showed brain atrophy (29% whole-brain, 16% cerebellar), 8% hydrocephalus, 8% delayed myelination. Atrophy is progressive — one report noted cerebral/cerebellar atrophy "gradually progressed after 3.5 years of age" (PMC10921618).

### Quality-of-life impact
Not formally studied with standardized instruments (no EQ-5D/SF-36 data identified for this ultra-rare disease); however, functional outcome measures (Vineland/Bayley developmental scales, Coma Recovery Scale in severely affected patients) are used descriptively in case reports to document dramatic improvement after uridine (e.g., Coma Recovery Scale improving from 5 to 16 within 2 months in one Koch et al. patient; PMC10921618 index case achieving self-feeding, eye contact, independent sitting after treatment).

Source: [BMC Pediatrics case report/review (PMC10921618)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/), [MedGen DEE50](https://www.ncbi.nlm.nih.gov/medgen/904125), [Koch et al. 2017, Brain](https://academic.oup.com/brain/article/140/2/279/2731780)

---

## 4. Genetic / Molecular Information

### Causal Gene
- **Gene:** CAD (carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase); HGNC:1424; NCBI Gene ID 790; chromosome 2p23.3; ~44 exons.
- **Protein:** A single 243-kDa, 2,225-amino-acid polypeptide that self-assembles into a large (~1.5 MDa) hexameric multi-enzyme complex carrying four sequential catalytic activities: glutamine amidotransferase (GATase), carbamoyl phosphate synthetase II (CPS-II), aspartate transcarbamylase (ATCase), and dihydroorotase (DHOase). These domains "channel" reaction intermediates (notably glutamine-derived ammonia) directly between active sites without release into bulk solvent — a classic example of metabolic substrate channeling. Zinc (3 Zn²⁺/subunit) is required for DHOase activity; Mg²⁺/Mn²⁺ are cofactors for other domains.
- **Pathway:** CAD catalyzes the first three (of six) steps of the *de novo* pyrimidine biosynthesis pathway, ultimately producing UMP, the precursor of all cellular pyrimidine nucleotides (UTP, CTP) and of UDP-activated sugars needed for glycosylation.

### Pathogenic Variants
- **Variant spectrum:** Across 42 reviewed cases with 80 mutation sites, missense variants predominate (78%), followed by nonsense (15%) and splice-site (6%) variants (PMC10921618).
- **Representative variants reported across the literature:**
  - c.98T>G (p.Met33Arg) — homozygous founder variant in Serbian Roma families (Koch et al. 2017)
  - c.1843-3C>T (splice acceptor) + c.5365C>T (p.Arg1789*) — compound heterozygous (Koch et al. 2017)
  - c.1843-1G>A (in-frame exon 13 deletion) + c.6071G>A (p.Arg2024Gln) — compound heterozygous (Ng et al., *Hum Mol Genet* 2015, PMC4424951)
  - c.5296_5308del13 (frameshift) + c.5429G>A (p.Arg1810Gln) — sibling pair (PMC7951104)
  - c.1252C>T (p.Gln418*) + c.6628G>A (p.Gly2210Ser) — novel compound heterozygous variants, index case (PMC10921618)
  - c.2995G>A (p.Val999Met) — homozygous, novel, three affected/deceased Iranian siblings (PMC8915536)
- **Classification:** Per ACMG/AMP framework, most reported variants are classified pathogenic or likely pathogenic on the basis of segregation, absence/rarity in population databases, and functional (cell-based) rescue assays.
- **Functional consequences:** Predominantly **loss-of-function** (complete or partial); a **hypomorphic** allelic class exists that retains partial enzyme activity and produces a milder, primarily hematologic phenotype (Br J Haematol 2023, PMID 37984840) rather than full DEE.
- **Zygosity:** Autosomal recessive — homozygous (often in consanguineous families or population founder-allele contexts) or compound heterozygous.
- **Somatic vs. germline:** All reported variants are germline.
- **Allele frequency:** Given the rarity of the disease (~40–50 published cases globally since 2015), specific gnomAD-derived carrier-frequency estimates for CAD deficiency were not identified in available resources; individual pathogenic alleles are expected to be very rare/absent in gnomAD, consistent with an ultra-rare recessive disorder, with founder-allele enrichment in specific populations (e.g., Serbian Roma for p.Met33Arg).

### Modifier Genes
None specifically established; phenotypic variability (e.g., the sibling pair with identical genotype but different severity) appears attributable to **age at diagnosis/treatment initiation** rather than a distinct modifier locus, per the "Tale of Two Siblings" report.

### Epigenetic Information
No disease-specific epigenetic (DNA methylation/histone) mechanism has been reported; DEE50 is a straightforward biallelic loss-of-function/hypomorphic Mendelian disorder.

### Chromosomal Abnormalities
Not a copy-number/structural disorder; no aneuploidy, translocation, or microdeletion mechanism reported. Diagnosis is by sequence-level variant detection (trio whole-exome sequencing, WES, is the standard diagnostic route reported across case series).

Suggested ontology terms: HGNC:1424 (CAD); GO:0004070 (aspartate carbamoyltransferase activity); GO:0004087 (carbamoyl-phosphate synthase activity); GO:0004151 (dihydroorotase activity); GO:0006207 ('de novo' pyrimidine nucleobase biosynthetic process).

Source: [Ng et al. 2015, Hum Mol Genet (PMC4424951)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4424951), [Koch et al. 2017, Brain, PMID 28007989](https://pubmed.ncbi.nlm.nih.gov/28007989/), [Br J Haematol 2023, PMID 37984840](https://pubmed.ncbi.nlm.nih.gov/37984840/), [BMC Pediatrics 2024 review (PMC10921618)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/)

---

## 5. Environmental Information

DEE50 has **no known environmental, lifestyle, or infectious causal contribution** — it is a fully penetrant Mendelian metabolic disease driven by biallelic CAD variants. The only "environmental" lever of clinical relevance is **therapeutic**: dietary/pharmacologic uridine supplementation is not a risk-modifying exposure in the traditional sense but a disease-modifying intervention exploiting the intact salvage pathway (see Sections 2 and 12). No toxin, occupational exposure, radiation, or infectious trigger has been implicated in any published case series.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathway
CAD initiates the **six-step *de novo* pyrimidine biosynthesis pathway**: glutamine + HCO₃⁻ + 2ATP → carbamoyl phosphate (CPS-II domain) → carbamoyl aspartate (ATCase domain) → dihydroorotate (DHOase domain) → [downstream, via DHODH, UMPS] → orotate → OMP → **UMP**, the universal precursor for UTP, CTP, and (via reduction) dCTP/dTTP, as well as for UDP-sugars used in glycosylation. Suggested pathway terms: KEGG hsa00240 (Pyrimidine metabolism); Reactome R-HSA-73621 (Pyrimidine biosynthesis).

### Causal Chain (Upstream → Downstream)
1. **Upstream (molecular):** Biallelic pathogenic CAD variant → loss/reduction of GATase-CPS-ATCase-DHOase enzymatic activity → failure of the first three committed steps of *de novo* pyrimidine synthesis.
2. **Cellular consequence:** Depletion of UMP/UTP/CTP pools and of UDP-activated sugars (UDP-glucose, UDP-galactose, etc.). Fibroblast studies from affected patients showed "reduced levels of UDP, UDP-glucose...CTP and UTP compared to control cell line" (Koch et al. 2017), and separately that "CTP, UTP and nearly all UDP-activated sugars that serve as donors for glycosylation were decreased" (Ng et al. 2015). Both defects were corrected by exogenous uridine supplementation in vitro.
3. **Tissue/organ consequence:** Pyrimidine and UDP-sugar deficiency impairs RNA/DNA synthesis and glycosylation capacity. This is proposed to particularly disrupt the **neuronal differentiation process**, "impair[ing] axon and dendrite formation and lead[ing] to neuronal migration disorders" (per the mechanistic synthesis in PMC10921618) — plausibly explaining the epileptogenesis, developmental regression, and progressive brain atrophy. In the erythroid lineage, impaired nucleotide/glycoconjugate synthesis produces dyserythropoiesis, anisopoikilocytosis, and anemia.
4. **Rescue mechanism:** Because the **pyrimidine salvage pathway** (uridine kinase → UMP synthase route) is intact and independent of CAD, exogenous uridine (or its prodrugs UMP, triacetyluridine/TAU) bypasses the defective *de novo* step entirely, restoring cellular UTP/CTP/UDP-sugar pools — the molecular basis for the profound clinical responsiveness described in Section 12.

### Cellular Processes Involved
- Nucleotide biosynthesis and salvage
- Neuronal differentiation, axon/dendrite formation, neuronal migration (proposed downstream consequence of pyrimidine/glycosylation deficit)
- Protein/glycan glycosylation (UDP-sugar-dependent)
- Erythropoiesis (dyserythropoiesis from nucleotide deficiency)
- Excitation/inhibition balance in cortical/cerebellar circuits, culminating in seizure generation and hypersynchrony (a downstream, disease-general convergence consistent with the `epilepsy_excitation_inhibition_imbalance` phenotype module pattern used in this knowledge base)

### Protein Dysfunction
Predominantly **loss-of-function** (reduced/absent catalytic activity across one or more of the GATase/CPS/ATCase/DHOase domains), with a distinguishable **hypomorphic** class of variants that retain partial activity and produce milder, non-encephalopathic phenotypes. Structural work (e.g., "Deciphering CAD: Structure and function of a mega-enzymatic pyrimidine factory in health and disease," and crystallographic study of the DHOase domain with 5-fluorouracil) supports domain-specific functional mapping of variants (e.g., the feline p.Ser2015Asn variant disrupts ATCase-domain oligomerization).

### Metabolic Changes
- Depleted UTP/CTP and UDP-sugar pools (directly measured in patient fibroblasts)
- Orotic aciduria has been reported as a downstream metabolic marker in some patients (HP:0003132), reflecting altered flux through the pathway
- Secondary metabolic complications reported include hyperammonemia and renal tubular acidosis in some patients (per MedGen clinical synopsis)

### Immune System Involvement
Not a primary feature; no autoimmune or immunodeficiency component is described in the literature reviewed.

### Tissue Damage Mechanisms
Progressive **brain atrophy** (cerebral and cerebellar) is the dominant structural/imaging correlate of ongoing neuronal injury, consistent with cumulative nucleotide/glycosylation deficiency-driven neurodegeneration if untreated.

### Molecular Profiling
- **Metabolomics:** The principal profiling modality used to date — targeted nucleotide/UDP-sugar quantification in patient-derived fibroblasts (Ng et al. 2015; Koch et al. 2017), demonstrating both the biochemical lesion and its correction by uridine. No transcriptomic, proteomic, lipidomic, or single-cell/spatial datasets specific to DEE50 were identified in the literature searched.
- **Functional genomics:** A dedicated **cell-based functional assay** platform has been developed and validated to classify patient CAD variants by residual activity/uridine-responsiveness, directly informing which patients are predicted to benefit from uridine therapy ("Cell-based analysis of CAD variants identifies individuals likely to benefit from uridine therapy," *Genetics in Medicine*).

Suggested ontology terms: GO:0006207 ('de novo' pyrimidine nucleobase biosynthetic process); GO:0044211 (CTP salvage); GO:0006213 (pyrimidine nucleoside metabolic process); GO:0030154 (cell differentiation, neuronal); GO:0031175 (neuron projection development); CL:0000540 (neuron); CL:0000764 (erythroid lineage cell); CHEBI:46211 (uridine).

Source: [Koch et al. 2017, Brain (PMID 28007989)](https://academic.oup.com/brain/article/140/2/279/2731780), [Ng et al. 2015, Hum Mol Genet (PMC4424951)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4424951), [BMC Pediatrics 2024 review (PMC10921618)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/)

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary:** Central nervous system (cerebral cortex, cerebellum) — the dominant site of pathology (epilepsy, developmental regression, atrophy). Bone marrow/hematopoietic system — the second major site (dyserythropoiesis, anemia).
- **Secondary/complication-level:** Kidney (renal tubular acidosis reported in some patients); gastrointestinal tract (dysphagia, diarrhea); musculoskeletal/motor system (hypotonia, gait abnormality, extrapyramidal movement disorder).
- **Body systems involved:** Nervous system (primary), hematologic/lymphatic system (primary), and secondarily renal, gastrointestinal, and musculoskeletal systems.

### Tissue and Cell Level
- **Nervous system:** Neurons (cortical and cerebellar), consistent with cerebellar and cerebral atrophy on imaging; Purkinje cell involvement is plausible given the prominence of ataxia and cerebellar atrophy but has not been histopathologically confirmed in the literature reviewed.
- **Hematologic system:** Erythroid precursor cells (dyserythropoiesis); mature erythrocytes show abnormal morphology (target cells, teardrop cells, acanthocytes).

Suggested Cell Ontology terms: CL:0000540 (neuron), CL:0000121 (Purkinje cell), CL:0000764 (erythroid lineage cell), CL:0000232 (erythrocyte).

### Subcellular Level
The CAD enzyme complex itself is **cytosolic** (GO:0005737); pyrimidine biosynthesis occurs in the cytoplasm, distinct from the mitochondrially-housed pyrimidine catabolic pathway. No specific organelle pathology (mitochondrial, ER, lysosomal) has been reported as a primary disease mechanism, though downstream glycosylation defects implicate Golgi-dependent glycoconjugate processing (GO:0005794, Golgi apparatus) secondarily.

### Localization
- **Anatomical sites (UBERON):** UBERON:0000955 (brain) — specifically cerebral cortex (UBERON:0000956) and cerebellum (UBERON:0002037); UBERON:0002371 (bone marrow).
- **Lateralization:** No lateralization pattern reported; brain atrophy is typically diffuse/bilateral (whole-brain or cerebellar), consistent with a systemic metabolic (rather than focal structural) etiology.

Source: [BMC Pediatrics 2024 review (PMC10921618)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/), [MedGen DEE50](https://www.ncbi.nlm.nih.gov/medgen/904125)

---

## 8. Temporal Development

### Onset
- **Typical age:** Mean 1.6 ± 1.8 years; 90% of cases present before age 3. A minority (3/42 in the pooled review) present in the **neonatal period**, and 12/42 between 1–12 months of age. A milder, later-onset spectrum (isolated developmental delay/intellectual disability without severe encephalopathy) has also been described (Rymen et al., *Genetics in Medicine* 2021).
- **Onset pattern:** Typically insidious developmental delay preceding seizure onset, though some patients present acutely with status epilepticus.

### Progression
- **Disease stages:** No formal staging system exists; the clinical course is generally described as progressive neurodegeneration (developmental regression, worsening seizures, progressive brain atrophy) if untreated.
- **Progression rate:** Variable but can be rapid — one case is described as showing "rapid deterioration of cognitive and motor function, and even became comatose" (PMC10921618).
- **Course pattern:** Progressive/degenerative in untreated disease; **can be halted or substantially reversed with uridine treatment**, effectively converting the natural history from progressive-fatal to stable-or-improving.
- **Duration:** Chronic, lifelong if untreated survival occurs; **potentially fatal in early childhood** without treatment (mean age at death in fatal untreated cases: 3.8 ± 1.2 years, per PMC10921618).

### Patterns
- **Remission:** Treatment-induced — seizure freedom achieved in a majority of uridine-treated patients (see Section 12), including rapid (within days) resolution of status epilepticus in some cases; no spontaneous remission is described.
- **Critical periods:** The literature strongly suggests a **critical treatment window** — the sibling-pair study (PMC7951104) demonstrated that earlier uridine initiation (age 5) produced dramatic, durable improvement, whereas delayed initiation in an affected sibling (age 14) produced only modest benefit, with the authors concluding "early diagnosis leading to early treatment is more effective." This motivates calls for inclusion of CAD deficiency in expanded newborn/genetic screening panels.

Source: [PMC10921618](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/), ["Tale of Two Siblings" (PMC7951104)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7951104/)

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence/incidence:** No formal population-based prevalence or incidence estimate exists. The disease is characterized by the total number of published/molecularly confirmed cases — approximately **40–50 patients reported globally since the disease's first description in 2015** (per the Bengal-cat animal-model paper, PMC12008240, which notes "approximately 50 CAD-deficient patients have been documented globally since 2015"). This is consistent with an **ultra-rare disease**.
- No CDC, WHO, or GBD-level burden data exist given the extreme rarity.

### Inheritance Pattern (for the genetic etiology)
- **Pattern:** Autosomal recessive (HP:0000007).
- **Penetrance:** Full penetrance is assumed for biallelic loss-of-function alleles based on consistent case reporting; hypomorphic alleles produce a milder, still fully penetrant but phenotypically distinct (predominantly hematologic) presentation.
- **Expressivity:** Variable — ranging from isolated mild developmental delay/anemia (hypomorphic alleles) to severe, potentially fatal epileptic encephalopathy (classic biallelic loss-of-function). Documented intra-family variability (the affected sibling pair) further illustrates variable clinical trajectory, attributed to treatment timing rather than genotype.
- **Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically reported.
- **Founder effects:** Yes — the p.Met33Arg allele was found homozygously in unrelated Serbian Roma families in the original 2017 description, consistent with a population founder effect.
- **Consanguinity:** A notable risk factor; 5/42 reviewed cases had consanguineous parents, and the Iranian case series (PMC8915536) specifically reports a homozygous novel variant (p.Val999Met) in a family with presumed consanguinity, resulting in three affected/deceased children.
- **Carrier frequency:** Not specifically established in population databases (gnomAD-derived estimate not identified); expected to be very low given the ultra-rare disease frequency, with population-specific enrichment where founder alleles exist.

### Population Demographics
- **Affected populations:** Reported cases span multiple ethnicities/geographies (European/Serbian Roma, Iranian, Chinese, and others), with no single predominant ethnic group apart from the Roma founder-allele cluster.
- **Geographic distribution:** No endemic geographic clustering beyond the founder-population effect noted above; cases have been reported from Europe, the Middle East (Iran), and East Asia (China).
- **Sex ratio:** No sex predilection is reported (autosomal recessive inheritance); both sexes are affected, as illustrated by the mixed-sex sibling pair and multiple single-sex case reports.
- **Age distribution:** Concentrated in infancy/early childhood at diagnosis-eligible presentation, though diagnostic delay commonly extends recognition into later childhood/adolescence (mean diagnostic age 7.7 years vs. mean onset 1.6 years).

Source: [PMC10921618](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/), [Koch et al. 2017 (PMID 28007989)](https://pubmed.ncbi.nlm.nih.gov/28007989/), [Iranian case report (PMC8915536)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8915536/)

---

## 10. Diagnostics

### Clinical Tests
- **Laboratory tests:** Complete blood count with peripheral smear (revealing macrocytic or normocytic anemia with anisopoikilocytosis — target cells, teardrop cells, acanthocytes); the index case in PMC10921618 showed hemoglobin 66 g/L, RBC 3.42×10¹²/L, hematocrit 22%. Urine organic acid analysis may show **orotic aciduria** in some patients, though (unlike some other pyrimidine disorders) CAD deficiency does not have a universally reliable single biochemical screening marker — it is explicitly listed among treatable IMDs "for which no metabolic marker is available," prioritizing genomic sequencing in the diagnostic algorithm (per the Treatable ID App review, *Orphanet J Rare Dis* 2021).
- **Imaging:** Brain MRI showing progressive cerebral and/or cerebellar atrophy, occasionally with delayed myelination or hydrocephalus.
- **Electrophysiology:** EEG showing epileptiform/encephalopathic patterns; notably, EEG normalization has been documented after successful uridine treatment ("encephalopathic pattern disappeared," Koch et al. 2017).
- **Biopsy/functional studies:** Patient-derived skin fibroblasts can be assayed for UTP/CTP/UDP-sugar pool depletion and for uridine-rescue response — increasingly used as a functional diagnostic/prognostic (variant-classification) tool.

### Genetic Testing
- **Recommended approach:** Because no single reliable biochemical marker exists, **trio whole-exome sequencing (WES)** is the diagnostic mainstay reported across essentially all published cases (Koch et al. 2017; PMC10921618; PMC8915536; PMC7951104).
- **WGS:** Not specifically reported as the primary diagnostic modality in the literature reviewed, though it would be expected to detect the same variant classes.
- **Gene panels:** Epilepsy/developmental-encephalopathy gene panels that include CAD would be expected to identify pathogenic variants; specific panel compositions were not detailed in sources reviewed.
- **Single-gene testing:** Feasible once CAD is specifically suspected (e.g., in a sibling of a known proband).
- **Chromosomal microarray/karyotyping/FISH/mitochondrial DNA testing:** Not applicable — DEE50 is a single-gene sequence-level disorder, not a copy-number or mitochondrial disease.
- **Repeat expansion testing:** Not applicable.

### Omics-Based Diagnostics
Targeted fibroblast metabolomics (UTP/CTP/UDP-sugar quantification) functions as a diagnostic-adjacent/confirmatory omics approach; no routine transcriptomic, proteomic, or liquid-biopsy diagnostic method is established for this disease.

### Clinical Criteria
No formal DSM/ICD/society-specific diagnostic criteria exist for this ultra-rare disorder; diagnosis rests on the combination of the clinical triad (developmental delay/regression + refractory epilepsy + anemia with anisopoikilocytosis) plus molecular confirmation of biallelic CAD variants.

**Differential diagnosis** (based on overlapping phenotype: developmental and epileptic encephalopathy + anemia + treatable metabolic mechanism) should include other treatable neurometabolic DEEs — e.g., pyridoxine-dependent epilepsy, biotinidase deficiency, GLUT1 deficiency, creatine deficiency disorders, and other congenital disorders of glycosylation — since CAD deficiency is explicitly grouped among "treatable inherited metabolic disorders causing intellectual disability" in the 2021 Treatable ID App review.

### Screening
CAD deficiency is **not currently part of standard newborn screening panels**, but multiple case reports explicitly recommend its inclusion given the availability of an effective, low-risk treatment and the severe consequences of diagnostic delay: authors of the 2024 review state "CAD should be considered to be included in neonatal genetic screening" (PMC10921618).

Suggested ontology terms: LOINC (CBC with differential, orotic acid urine test — specific LOINC codes not identified in sources reviewed); HP:0003132 (Orotic aciduria); NCIT:C17004 (Whole Exome Sequencing).

Source: [PMC10921618](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/), [Treatable ID App review, Orphanet J Rare Dis 2021](https://link.springer.com/article/10.1186/s13023-021-01727-2)

---

## 11. Outcome / Prognosis

### Survival and Mortality
- **Mortality rate:** 9.5% (4 of 42 pooled cases) in the largest available literature review (PMC10921618).
- **Critical finding:** "All reported deaths occurring in patients without uridine treatment," with mean age at death 3.8 ± 1.2 years — indicating that **mortality is essentially confined to the untreated natural history**, and no deaths or serious adverse events have been reported among uridine-treated patients in this dataset.
- The Iranian case series (PMC8915536) independently documents three affected/deceased siblings, reinforcing that untreated/undiagnosed disease carries substantial early mortality risk, particularly before the treatable nature of the condition was recognized (pre-2017) or where diagnosis is delayed/unavailable.

### Morbidity and Function
- Untreated survivors accumulate progressive neurological disability: developmental regression, loss of acquired skills, worsening seizures, ataxia, dysphagia, and eventual severe functional impairment (e.g., nonverbal, tracheostomy-dependent status in the untreated/late-treated sibling in PMC7951104).
- No standardized quality-of-life instrument data (EQ-5D, SF-36, PROMIS) specific to DEE50 were identified; functional improvement is instead documented via developmental testing (Bayley/Vineland-type domains: fine motor, cognition, language, social-emotional) and disease-specific functional scales (e.g., Coma Recovery Scale in severely affected patients).

### Disease Course
- **Complications:** Status epilepticus (up to 45% of epilepsy cases), aspiration risk from dysphagia, failure to thrive, and (in a subset) renal tubular acidosis/hyperammonemia.
- **Recovery potential:** Substantial and, in several documented cases, dramatic — with treatment. Without treatment, recovery is not observed; the disease is progressive/degenerative.

### Prediction
- **Prognostic factors:** The single most consistently identified prognostic factor across the literature is **age at treatment initiation** — earlier uridine initiation correlates strongly with better long-term neurological outcome, as directly demonstrated in the sibling comparison (PMC7951104) and echoed by the pooled-cohort finding that all 18 treated patients in the PMC10921618 review showed favorable responses when treatment was pursued.
- **Prognostic biomarkers:** Fibroblast-based functional assays of CAD variant activity and uridine-rescue capacity have been proposed as a means to predict which patients/genotypes are most likely to respond to therapy ("Cell-based analysis of CAD variants identifies individuals likely to benefit from uridine therapy," *Genetics in Medicine*).

Source: [PMC10921618](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/), ["Tale of Two Siblings" PMC7951104](https://pmc.ncbi.nlm.nih.gov/articles/PMC7951104/), [Iranian case report PMC8915536](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8915536/)

---

## 12. Treatment

DEE50 is distinctive among genetic developmental and epileptic encephalopathies in having a **specific, mechanism-based, highly effective disease-modifying treatment**: exogenous pyrimidine (uridine) supplementation.

### Pharmacotherapy — Uridine Supplementation (the primary/definitive treatment)
Three clinical formulations are reported in the literature (PMC10921618):
- **Uridine** — ~100 mg/kg/day
- **Uridine monophosphate (UMP)** — 141 ± 36 mg/kg/day
- **Uridine triacetate (triacetyluridine, TAU/Vistogard)** — 110 ± 14 mg/kg/day; reported to be "four to six times more bioavailable" than plain uridine, at higher cost. A dedicated case report/review specifically evaluates triacetyluridine ("Triacetyluridine treats epileptic encephalopathy from CAD mutations: a case report and review," Frederick et al., *Ann Clin Transl Neurol* 2021).

**Mechanism of action:** Bypasses the CAD-catalyzed steps of *de novo* pyrimidine synthesis entirely by feeding the intact pyrimidine **salvage pathway**, restoring intracellular UTP/CTP and UDP-sugar pools.

**Suggested NCIT term:** NCIT:C15986 (Pharmacotherapy), with `therapeutic_agent` bound to CHEBI:46211 (uridine) or the relevant prodrug entities.

### Treatment Outcomes (pooled data, PMC10921618, n=18 treated patients)
- **88% (16/18)** showed significant developmental progress
- **83% (15/18)** had significantly reduced seizure frequency
- **73% (11/18)** achieved complete seizure freedom
- Among 7 patients presenting with **status epilepticus**, all achieved seizure freedom on uridine, with three becoming seizure-free by day 2 of treatment
- **15/18 (83%)** achieved hematologic (anemia) correction, at a mean of ~2.3 months of therapy
- **No deaths or serious adverse events** were reported among uridine-treated patients

**Illustrative individual outcomes:**
- Index case (PMC10921618): seizures "controlled completely" within one week of treatment initiation; at 1-year follow-up, "seizure-free, with normal EEG findings," plus new self-feeding, eye contact, and independent sitting.
- Koch et al. 2017 Patient F1:II.3: no further seizures over 7 months' follow-up; improved fine motor, cognition, language, and social-emotional development; blood morphology normalized within 12 weeks.
- Koch et al. 2017 Patient F2:II.2: transitioned from a bedridden, minimally conscious state to communicative, with Coma Recovery Scale improving from 5 to 16 within 2 months and EEG normalization.
- Sibling study (PMC7951104): early-treated sister (uridine started at age 5) achieved "resolution of generalized tonic-clonic seizures, improved absence seizures, normalized motor development, improved cognition and language...stabilized cerebellar atrophy" over 3 years, whereas her brother, treated much later (age 14), had only modest seizure-frequency reduction (5–10/day to 0–3/day) and remained nonverbal/care-dependent — underscoring the treatment-timing effect described in Section 8.

### Advanced Therapeutics, Surgical, and Other Modalities
- **Gene therapy, cell therapy, RNA-based therapy, targeted molecular therapy, immunotherapy:** None reported or applicable for DEE50 — the disease is managed via direct metabolic substrate replacement rather than genetic or immune-modulatory approaches.
- **Surgical intervention:** Not disease-specific, though in refractory pre-diagnosis cases aggressive standard epilepsy interventions have been used, including pentobarbital-induced coma and epilepsy surgery (temporal lobe resection) in the severely affected, later-diagnosed brother in the sibling case report — interventions that preceded the eventual CAD diagnosis and uridine treatment.
- **Supportive/rehabilitative care:** Standard antiepileptic drug (AED) management is used prior to/alongside diagnosis (with generally limited efficacy against the refractory seizures, consistent with 64% of epilepsy cases being drug-refractory); physical/occupational/speech therapy would be expected to support developmental gains, though not specifically quantified in the sources reviewed.

### Experimental / Investigational
No CAD deficiency-specific registered clinical trials (ClinicalTrials.gov NCT identifiers) were identified in the sources reviewed; management is guided by an accumulating case-report/case-series evidence base rather than randomized trial data, consistent with the disease's ultra-rare status. (Uridine triacetate/Vistogard itself is FDA-approved for an unrelated indication — 5-FU/capecitabine overdose — and is being repurposed off-label for CAD deficiency based on the case-report evidence above.)

### Treatment Strategy
Given the excellent safety profile of uridine and the demonstrated risk of untreated mortality, the literature explicitly recommends an **empiric/pre-emptive treatment strategy**: "uridine treatment should be attempted in patients who show signs of early developmental delay and refractory epilepsy" even before genetic confirmation is complete (PMC10921618) — an unusual and notable "treat first, confirm later" recommendation for a genetic disease, justified by uridine's low risk-to-benefit ratio and the steep cost of diagnostic/treatment delay documented in the sibling comparison.

Source: [PMC10921618](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/), [Koch et al. 2017 (PMID 28007989)](https://academic.oup.com/brain/article/140/2/279/2731780), ["Tale of Two Siblings" PMC7951104](https://pmc.ncbi.nlm.nih.gov/articles/PMC7951104/), [Treatable ID App review](https://link.springer.com/article/10.1186/s13023-021-01727-2)

---

## 13. Prevention

### Prevention Levels
- **Primary prevention:** Not applicable in the vaccination/exposure-avoidance sense, since DEE50 is a fully genetic condition; the closest analog is **reproductive genetic counseling** for known carrier couples (see below) and, prospectively, **newborn/expanded genetic screening** to enable pre-symptomatic or early-symptomatic treatment initiation before irreversible neurological injury occurs.
- **Secondary prevention:** Early recognition and rapid initiation of uridine therapy functions as the disease's central "secondary prevention" lever — converting a potentially fatal, progressively disabling disease into a largely controllable one. This is the single most emphasized preventive theme across the literature reviewed.
- **Tertiary prevention:** Standard supportive management of complications (seizure emergency protocols for status epilepticus, nutritional/feeding support for dysphagia-related aspiration risk, developmental/rehabilitative therapies) in patients with residual disability.

### Screening and Early Detection
- **Population-based screening:** CAD deficiency is not currently included in standard newborn screening panels, but multiple authors explicitly call for its addition given the availability of an effective, low-toxicity treatment (PMC10921618: "CAD should be considered to be included in neonatal genetic screening").
- **Genetic/carrier screening:** In families with a known proband, carrier testing of parents and cascade/prenatal testing of subsequent pregnancies is standard reproductive-genetics practice for autosomal recessive disorders, though this was not separately detailed as CAD-specific guidance in the sources reviewed.
- **Risk stratification:** Consanguinity and known population founder alleles (e.g., Serbian Roma p.Met33Arg) are practical risk-stratification cues that should raise clinical suspicion in a child presenting with the developmental delay + refractory epilepsy + anemia triad.

### Behavioral Interventions / Public Health / Environmental Interventions
Not applicable — DEE50 has no behavioral, lifestyle, or environmental risk-modification component; prevention is entirely genetics- and treatment-timing-driven.

### Counseling
Genetic counseling for parents of an affected child (recurrence risk 25% per pregnancy for two carrier parents) is standard practice for an autosomal recessive disorder, and is implicit in the family-based diagnostic workups reported (e.g., trio WES with parental carrier confirmation in the Iranian case series, PMC8915536).

### Prophylaxis
There is no described "prophylactic" pre-symptomatic use of uridine in genetically confirmed but pre-symptomatic siblings in the literature reviewed, though the strong treatment-timing effect documented in Section 8/11 provides a rationale for considering early/pre-symptomatic treatment in a molecularly confirmed younger sibling of an affected proband.

Source: [PMC10921618](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/), [Treatable ID App review](https://link.springer.com/article/10.1186/s13023-021-01727-2)

---

## 14. Other Species / Natural Disease

### Taxonomy and Natural Disease
A **naturally occurring CAD deficiency has been reported in the domestic cat**, specifically the **Bengal breed** — described as "the first report of a naturally occurring CAD deficiency in animals" (PMC12008240, 2025).

- **Species/breed:** *Felis catus*, Bengal breed (NCBI Taxon: 9685 for *Felis catus*; a Vertebrate Breed Ontology [VBO] identifier for "Bengal" would apply, specific VBO ID not confirmed in sources reviewed).
- **Clinical presentation:** A 4-month-old kitten developed "clusters of generalized tonic seizures with orofacial involvement and abnormal behavior" beginning at 13 weeks of age, with behavioral abnormalities and mild anisocytosis — closely paralleling human DEE50's seizure and hematologic phenotype. The kitten showed only **partial response to conventional antiepileptic drugs** (phenobarbital, levetiracetam), again mirroring the drug-refractory nature of human disease.
- **Genetic variant:** A novel homozygous missense variant, **p.Ser2015Asn**, in the feline CAD gene, shown functionally to disrupt oligomerization of the C-terminal aspartate transcarbamylase (ATCase) domain. Genotyping of 110 unaffected Bengal cats identified 4 additional heterozygous carriers, indicating the variant segregates within the breed — a candidate breed-founder allele analogous to the human Roma founder mutation.
- **Outcome/treatment:** The affected kitten was euthanized before uridine treatment could be trialed, so direct therapeutic proof-of-concept in the feline model is not yet available; however, given the mechanistic parallel to human disease, the authors suggest uridine supplementation "could benefit affected cats."
- **Significance as a model:** The authors propose that **CAD-deficient Bengal cats might serve as a spontaneous, naturally occurring large-animal model** for studying DEE50 pathogenesis and testing uridine (or other) therapeutic strategies — a valuable complement to the case-report-driven human evidence base, since no engineered rodent/zebrafish/Drosophila CAD-deficiency model was identified in the literature reviewed.

### Comparative Biology
CAD and its pyrimidine-biosynthesis function are highly evolutionarily conserved across eukaryotes (the trifunctional CAD gene arrangement itself arose from fusion of ancestral prokaryotic pyrimidine-pathway genes), supporting mechanistic conservation between the feline and human disease phenotypes. No zoonotic or cross-species transmission is relevant, as this is a non-infectious, purely genetic/metabolic disorder.

### Model Organism Databases
Given the extreme rarity of the human disease and the very recent (2025) description of the only known natural animal model, no entries were identified in MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, or similar engineered-model-organism databases specifically for CAD-deficiency disease models; the Bengal cat represents a spontaneous veterinary case rather than a laboratory-engineered model.

Source: ["Epileptic encephalopathy in a young Bengal cat caused by CAD deficiency," PMC12008240](https://pmc.ncbi.nlm.nih.gov/articles/PMC12008240/), [dvm360 summary](https://www.dvm360.com/view/developmental-and-epileptic-encephalopathy-type-50-is-found-in-a-bengal-kitten)

---

## 15. Model Organisms

- **Naturally occurring (spontaneous) model:** The Bengal cat described in Section 14 is, per current literature, the **only reported animal model of CAD deficiency** — a naturally occurring, non-engineered model arising from a breed-associated founder variant.
- **Engineered models (mouse, zebrafish, Drosophila, C. elegans, yeast):** No CAD-knockout, knock-in, transgenic, or conditional engineered animal model specific to DEE50/CAD deficiency was identified in the sources searched. This is notable given CAD's fundamental, universally essential role in pyrimidine biosynthesis — a complete CAD-null mutation would likely be embryonic lethal in most model systems (consistent with the human disease's biallelic-hypomorphic/partial-loss-of-function requirement for survival), which may explain why viable engineered whole-organism models have not been reported; conditional/tissue-specific knockouts would be a logical unmet research need.
- **Cellular/in vitro models:** The primary "model system" used across the literature is **patient-derived dermal fibroblast culture**, used to (a) directly demonstrate depletion of UTP/CTP/UDP-sugar pools, (b) demonstrate rescue of these metabolites by exogenous uridine in vitro, and (c) functionally classify novel CAD variants for pathogenicity and predicted uridine-responsiveness (the "Cell-based analysis of CAD variants" platform, *Genetics in Medicine*). No iPSC-derived neuronal or organoid model of CAD deficiency was identified in the sources reviewed.
- **Model limitations:** Fibroblast-based assays capture the core biochemical lesion (pyrimidine/UDP-sugar depletion and its uridine-rescue) but cannot recapitulate neuronal-specific phenotypes (seizures, developmental regression, brain atrophy) or hematologic phenotypes (dyserythropoiesis), which is the translational gap the Bengal cat model is positioned to fill going forward.
- **Research applications:** The fibroblast platform is used for (i) variant pathogenicity/functional classification and (ii) pre-clinical proof-of-concept for uridine (and potentially alternative pyrimidine-repletion strategies); the Bengal cat model is positioned for in vivo mechanistic and therapeutic (uridine efficacy/dosing) studies not achievable in cell culture.

Source: [Genetics in Medicine — cell-based CAD variant analysis](https://www.nature.com/articles/s41436-020-0833-2), ["Epileptic encephalopathy in a young Bengal cat caused by CAD deficiency," PMC12008240](https://pmc.ncbi.nlm.nih.gov/articles/PMC12008240/)

---

## Summary of Key Ontology Term Suggestions for KB Population

| Category | Term |
|---|---|
| Disease (MONDO) | MONDO:0014647 |
| Disease (OMIM) | #616457 |
| Disease (Orphanet) | ORPHA448010 |
| Causal gene | hgnc:1424 (CAD) |
| Inheritance | HP:0000007 (Autosomal recessive inheritance) |
| Key phenotypes (HP) | HP:0011344 (developmental regression), HP:0011451 (drug-resistant epilepsy), HP:0002133 (status epilepticus), HP:0001903 (anemia), HP:0011273 (anisopoikilocytosis), HP:0001251 (ataxia), HP:0003132 (orotic aciduria), HP:0002015 (dysphagia) |
| Biological process (GO) | GO:0006207 ('de novo' pyrimidine nucleobase biosynthetic process) |
| Molecular function (GO) | GO:0004070 (aspartate carbamoyltransferase activity), GO:0004087 (carbamoyl-phosphate synthase activity), GO:0004151 (dihydroorotase activity) |
| Cell types (CL) | CL:0000540 (neuron), CL:0000764 (erythroid lineage cell) |
| Anatomy (UBERON) | UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0002371 (bone marrow) |
| Treatment agent (CHEBI) | CHEBI:46211 (uridine) |
| Treatment action (NCIT) | NCIT:C15986 (Pharmacotherapy) |
| Model organism (NCBITaxon) | NCBITaxon:9685 (Felis catus) |

---

### Sources
- [OMIM #616457 — DEE50](https://omim.org/entry/616457)
- [MedGen — Developmental and epileptic encephalopathy, 50](https://www.ncbi.nlm.nih.gov/medgen/904125)
- [Malacards — DEE50](https://www.malacards.org/card/developmental_and_epileptic_encephalopathy_50)
- [Novel CAD gene mutations...dramatic response to uridine therapy: case report and literature review, BMC Pediatrics 2024 (PMC10921618)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921618/)
- [Koch J et al. "CAD mutations and uridine-responsive epileptic encephalopathy." Brain 2017;140:279–286 (PMID 28007989)](https://academic.oup.com/brain/article/140/2/279/2731780)
- [Ng BG et al. "Biallelic mutations in CAD, impair de novo pyrimidine biosynthesis and decrease glycosylation precursors." Hum Mol Genet 2015;24(11):3050-3057 (PMC4424951)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4424951)
- ["Uridine-responsive epileptic encephalopathy due to inherited variants in CAD: A Tale of Two Siblings" (PMC7951104)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7951104/)
- ["CAD gene and early infantile epileptic encephalopathy-50; three Iranian deceased patients and a novel mutation" BMC Pediatrics 2022 (PMC8915536)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8915536/)
- ["Biallelic hypomorphic variants in CAD cause uridine-responsive macrocytic anaemia with elevated haemoglobin-A2" (PMID 37984840)](https://pubmed.ncbi.nlm.nih.gov/37984840/)
- ["Expanding the clinical and genetic spectrum of CAD deficiency," Genetics in Medicine](https://www.gimjournal.org/article/S1098-3600(21)00760-7/fulltext)
- ["Cell-based analysis of CAD variants identifies individuals likely to benefit from uridine therapy," Genetics in Medicine](https://www.nature.com/articles/s41436-020-0833-2)
- ["Treatable inherited metabolic disorders causing intellectual disability: 2021 review and digital app," Orphanet J Rare Dis](https://link.springer.com/article/10.1186/s13023-021-01727-2)
- ["Epileptic encephalopathy in a young Bengal cat caused by CAD deficiency" (PMC12008240)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12008240/)
- [dvm360 — Bengal kitten CAD deficiency summary](https://www.dvm360.com/view/developmental-and-epileptic-encephalopathy-type-50-is-found-in-a-bengal-kitten)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 9 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

3 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC10921618` *(abstract only)*: "gradually progressed after 3.5 years of age"
  - closest text in source: "Among them, 90% had onset before 3 years of age, with average of 1.6±1.8 years old"
- `PMC:PMC10921618` *(abstract only)*: "impair[ing] axon and dendrite formation and lead[ing] to neuronal migration disorders"
  - Text part not found as substring: 'impair axon and dendrite formation and lead to neuronal migration disorders' (note: only abstract available for PMID:38454370, full text may contain this excerpt)
- `PMC:PMC7951104`: "Tale of Two Siblings"
  - Text part not found as substring: 'Tale of Two Siblings'
- `PMC:PMC10921618` *(abstract only)*: "CAD should be considered to be included in neonatal genetic screening"
  - closest text in source: "BACKGROUND: Developmental and epileptic encephalopathy-50 (DEE-50) is a rare clinical condition believed to be caused by a mutation in the CAD gene and is associated with a bleak prognosis"