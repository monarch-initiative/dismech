---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T07:18:17.090245'
end_time: '2026-08-20T07:23:15.708950'
duration_seconds: 298.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Microcephaly, Short Stature, and Impaired Glucose Metabolism 1
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
  web_search_requests: 13
  num_turns: 24
  total_cost_usd: 2.1551834999999997
  session_id: 89bcf1cf-dd88-5c4b-bfe9-0ebc81ebad46
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 14
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 9
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microcephaly, Short Stature, and Impaired Glucose Metabolism 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Microcephaly, Short Stature, and Impaired Glucose Metabolism 1** covering all of the
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

I'll research this condition using web search to verify facts and gather accurate citations before compiling the report.

I have enough verified material to compile a comprehensive, well-cited report. For the Gillis et al. 2014 paper I'll cite by DOI since I could not independently confirm its PMID through the tools available.

# Research Report: Microcephaly, Short Stature, and Impaired Glucose Metabolism 1 (MSSGM1)

## 1. Disease Information

**Overview.** Microcephaly, short stature, and impaired glucose metabolism 1 (MSSGM1) is a rare, autosomal recessive multisystem Mendelian syndrome characterized by primary (congenital or early-postnatal) microcephaly with intellectual disability, proportionate short stature, and disturbed glucose homeostasis — typically hyperinsulinemic hypoglycemia in infancy/early childhood evolving into young-onset diabetes mellitus in adolescence or young adulthood ([OMIM #616033](https://omim.org/entry/616033); [MedGen C4014997](https://www.ncbi.nlm.nih.gov/medgen/863434)). It is caused by biallelic (homozygous or compound heterozygous) loss-of-function mutations in **TRMT10A** (tRNA methyltransferase 10 homolog A), located at chromosome 4q23 ([OMIM *616013](https://omim.org/entry/616013)).

**Key identifiers:**
- **OMIM phenotype:** #616033 (MSSGM1); gene locus OMIM *616013 (TRMT10A)
- **MONDO:** MONDO:0000208 (per NCBI MedGen cross-reference)
- **MedGen:** C4014997 / UID 863434
- **Orphanet:** ORPHA:391408 — "Primary microcephaly-mild intellectual disability-young-onset diabetes syndrome"
- **HGNC:** HGNC:28403 (TRMT10A)
- **Gene location:** 4q23; **Ensembl:** ENSG00000145331
- **Note:** A phenotypically overlapping but molecularly and nosologically **distinct** entity exists — MSSGM2 (OMIM #616817), caused by biallelic mutations in **IGF2BP1** — and NSMCE2-related primordial dwarfism (OMIM #617253) also has overlapping features (short stature, microcephaly, insulin resistance) but is a separate gene/disorder. These should not be conflated with MSSGM1/TRMT10A.

**Synonyms:** MSSGM1; TRMT10A deficiency; TRMT10A-related syndrome; "microcephaly, intellectual disability, short stature, and diabetes"; young-onset diabetes with microcephaly.

**Data provenance:** Knowledge is derived almost entirely from **aggregated case reports and small case series** (individual patients and consanguineous families) rather than large population-level cohorts or EHR-based studies — consistent with an ultra-rare Mendelian disease with an estimated total of only ~15–20 published cases across the literature to date (multiple independent kindreds: Moroccan, Uzbek Jewish, Israeli/Bedouin, Scottish, Chinese, Turkish).

Sources:
- [OMIM #616033](https://omim.org/entry/616033)
- [OMIM *616013 TRMT10A](https://omim.org/entry/616013)
- [MedGen C4014997](https://www.ncbi.nlm.nih.gov/medgen/863434)
- [Orphanet TRMT10A](https://www.orpha.net/en/disease/gene/TRMT10A)

---

## 2. Etiology

**Disease-causal factor:** MSSGM1 is a monogenic, autosomal recessive disorder caused exclusively by biallelic loss-of-function variants in **TRMT10A**. There is no known environmental, infectious, or polygenic contribution to the core syndrome — it is a purely genetic/mechanistic disease. TRMT10A encodes a nucleolar tRNA methyltransferase (the human ortholog of yeast Trm10) that catalyzes N1-methylation of guanosine 9 (m¹G9) in the D-loop of multiple cytoplasmic tRNAs.

**Genetic risk factors (causal variants reported across kindreds):**
- **c.379G>A (p.Arg127Ter/R127X)** — homozygous nonsense mutation, first-described Moroccan consanguineous family (3 siblings) (Igoillo-Esteve et al. 2013, PMID: [24204302](https://pmc.ncbi.nlm.nih.gov/articles/PMC3814312/))
- **c.616G>A (p.Gly206Arg/G206R)** — homozygous missense mutation at a highly conserved catalytic residue, consanguineous Uzbek Jewish family (3 siblings); in vitro methyltransferase activity assays showed the mutant enzyme had **>10⁴-fold reduced methylation activity** compared to wild type (Gillis et al. 2014, *J Med Genet* 51:581–586, DOI: 10.1136/jmedgenet-2014-102282)
- **p.Glu27Ter (c.79G>T)** — homozygous nonsense mutation, Scottish siblings with milder, adult-onset phenotype (Yew et al. 2016, PMID: [26526202](https://pmc.ncbi.nlm.nih.gov/articles/PMC4995728/))
- **c.496-1G>A** — homozygous canonical splice-acceptor mutation, first reported Chinese/Asian patient (Lin et al. 2020, *BMJ Open Diabetes Res Care* 8:e001601)
- **Homozygous contiguous gene deletion** encompassing TRMT10A, causing a more severe multisystem phenotype including failure to thrive and delayed puberty (Zung et al. 2015, *Am J Med Genet A*, DOI: 10.1002/ajmg.a.37341)
- Additional homozygous/compound heterozygous TRMT10A variants reported in subsequent case reports (e.g., a case with hypoplastic kidneys, PMID: [33448213](https://pubmed.ncbi.nlm.nih.gov/33448213/); a 2024 case report of microcephaly/diabetes/epilepsy, PMID: [38302348](https://pubmed.ncbi.nlm.nih.gov/38302348/))

All disease-causing variants are inherited in an autosomal recessive pattern, and virtually all reported cases arose in the setting of parental consanguinity, consistent with a rare recessive founder/private-mutation disease.

**Environmental/lifestyle risk factors:** None established — this is not modified by known environmental exposures; disease expression is driven by genotype (complete vs. partial loss of TRMT10A methyltransferase activity), which correlates with phenotypic severity (see below).

**Protective factors:** None specifically documented. No modifier genes or protective alleles have been reported. Heterozygous carriers (parents of affected probands) are clinically unaffected, consistent with fully recessive inheritance without a dominant-negative or haploinsufficiency mechanism.

**Genotype-phenotype/severity correlation (an important "gene-environment"-adjacent theme):** Emerging literature (including a 2026 study on "TRMT10A-Related Neurodevelopmental Disorder Without Metabolic Findings," Ülker Üstebay et al., *Human Mutation* 2026) suggests **residual enzymatic activity of the mutant allele** modulates phenotype severity — some hypomorphic alleles produce a neurodevelopmental phenotype (intellectual disability, microcephaly) **without** the metabolic (diabetes/hypoglycemia) component, broadening the recognized phenotypic spectrum beyond the "full" MSSGM1 triad.

Sources:
- [Igoillo-Esteve et al. 2013, PLOS Genetics (PMC3814312)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3814312/)
- [Gillis et al. 2014, J Med Genet](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.37341) (DOI 10.1136/jmedgenet-2014-102282)
- [Yew et al. 2016, Diabetic Medicine (PMC4995728)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4995728/)
- [Lin et al. 2020, BMJ Open Diabetes Res Care (PMC7569974)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7569974/)
- [Zung et al. 2015, Am J Med Genet A](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.37341)
- [TRMT10A Mutation in a Child with Diabetes... Hypoplastic Kidneys, PMID 33448213](https://pubmed.ncbi.nlm.nih.gov/33448213/)
- [A rare syndrome: Microcephaly, diabetes mellitus, and epilepsy, PMID 38302348](https://pubmed.ncbi.nlm.nih.gov/38302348/)
- [TRMT10A-Related Neurodevelopmental Disorder Without Metabolic Findings, Human Mutation 2026](https://onlinelibrary.wiley.com/doi/10.1155/humu/8058409)

---

## 3. Phenotypes

The MSSGM1 phenotype (compiled from MedGen's HPO-term listing and the primary case-series literature) spans neurodevelopmental, growth/skeletal, endocrine-metabolic, and immune domains.

### Neurological/developmental
| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Intellectual disability | HP:0001249 | Present in nearly all reported cases; ranges mild–moderate |
| Global developmental delay | HP:0001263 | Congenital-onset |
| Motor delay | HP:0001270 | |
| Seizures / epilepsy | HP:0001250 | Reported in multiple kindreds (Gillis 2014; Yew 2016; 2024 case report) |
| Generalized non-motor (absence) seizure | HP:0011147 | |
| Primary microcephaly | HP:0011451 | Congenital onset; core diagnostic feature |
| Microcephaly (postnatal/progressive in some) | HP:0000252 | Some patients show normalization of head circumference with age (Yew 2016) |

### Growth/skeletal
| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Short stature | HP:0004322 | Proportionate; core diagnostic feature |
| Short neck | HP:0000470 | |
| Wide/broad nose | HP:0000445 | |
| Low anterior hairline | HP:0000294 | |
| Dorsocervical fat pad | HP:0009806 | Reported in association with insulin resistance |
| Scoliosis | HP:0002650 | |
| Joint hypermobility | HP:0001382 | |
| Osteoporosis | HP:0000939 | |
| Hypoplastic kidneys | HP:0000089 | Reported in one case (PMID 33448213), possibly expands phenotype |

### Endocrine/metabolic (the defining "impaired glucose metabolism" component)
| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Hyperinsulinemic hypoglycemia | HP:0000825 | Typical early-childhood presentation; ketotic and non-ketotic events described (Gillis 2014) |
| Diabetes mellitus (young/adolescent-onset) | HP:0000819 | Onset ranges early adolescence (Igoillo-Esteve cohort, age 14–22) to young adulthood (Yew cohort, age 24–28) |
| Insulin resistance | HP:0040270 | Documented directly via Matsuda index in Yew 2016 (Matsuda 1.46 vs. controls ~14.2) and in the Chinese case (Lin 2020) |
| Delayed puberty | HP:0000823 | |
| Delayed thelarche | HP:0025499 | |
| Primary amenorrhea | HP:0000786 | |
| Anti-GAD65 antibody | — (laboratory finding, not core autoimmunity) | Reported but disease is not classically autoimmune in mechanism |

**Age of onset / progression:** Congenital microcephaly and short stature are apparent from birth/infancy. Glucose dysregulation frequently begins as **hyperinsulinemic hypoglycemia in infancy or early childhood**, transitioning over years to **overt diabetes mellitus** in the second or third decade — proposed to reflect progressive β-cell loss via apoptosis (see Mechanism section). Severity and the specific metabolic phenotype (hypoglycemia-predominant vs. insulin-resistant diabetes-predominant, vs. purely neurodevelopmental with no metabolic disease) vary by allele and possibly by residual enzymatic activity, per the 2026 phenotype-expansion report. Epilepsy/seizures appear to be a variably penetrant feature rather than universal.

**Frequency across the literature:** Because MSSGM1 is known from fewer than ~20 published probands, "frequency" data (e.g., % of patients with a given feature) should be treated as descriptive of the small reported case series rather than population-level statistics; frequency qualifiers in a knowledge base entry should be sourced to specific cohort counts (e.g., "3/3 siblings" in a given family report) rather than generalized percentages.

**Quality of life impact:** Not formally studied with standardized instruments (no EQ-5D/SF-36 data identified); qualitatively, affected individuals face lifelong intellectual disability, need for insulin/metabolic management, and growth-related morbidity, but no dedicated QOL study was found in the literature reviewed.

Sources:
- [MedGen C4014997 — clinical feature listing](https://www.ncbi.nlm.nih.gov/medgen/863434)
- [Igoillo-Esteve et al. 2013 (PMC3814312)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3814312/)
- [Gillis et al. 2014, J Med Genet](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.37341)
- [Yew et al. 2016 (PMC4995728)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4995728/)
- [Lin et al. 2020 (PMC7569974)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7569974/)

---

## 4. Genetic/Molecular Information

**Causal gene:** TRMT10A (HGNC:28403), chromosome 4q23, Ensembl ENSG00000145331. Gene-level OMIM entry: *616013.

**Protein:** tRNA methyltransferase 10 homolog A — a nucleolar enzyme, mammalian ortholog of *S. cerevisiae* Trm10, that catalyzes formation of **N1-methylguanosine at position 9 (m¹G9)** in the D-loop of multiple cytoplasmic tRNAs. TRMT10A localizes to the nucleolus in both β-cells and non-β-cells, the site of tRNA processing/modification (Igoillo-Esteve et al. 2013). TRMT10A is **ubiquitously expressed but enriched in brain and pancreatic islets**, directly consistent with the two principal affected tissues in MSSGM1 (Igoillo-Esteve et al. 2013; OMIM *616013).

**Reported pathogenic variants (all biallelic, loss-of-function or severely hypomorphic):**
- p.Arg127Ter (c.379G>A) — complete loss via nonsense-mediated decay (NMD); no detectable mRNA/protein (Igoillo-Esteve 2013)
- p.Gly206Arg (c.616G>A) — missense at a conserved catalytic residue; methylation activity reduced >10⁴-fold in vitro (Gillis 2014)
- p.Glu27Ter (c.79G>T) — nonsense, presumed NMD (Yew 2016) — associated with a **milder** phenotype (adult-onset diabetes, normalized head circumference, minimal dysmorphism), suggesting some genotype-severity correlation
- c.496-1G>A — canonical splice acceptor variant (Lin et al. 2020)
- Contiguous gene deletion encompassing TRMT10A (Zung et al. 2015) — more severe multisystem phenotype

**Variant classification:** Per ACMG/AMP framework, the nonsense and canonical splice-site variants are consistently classified pathogenic (complete loss of function); the G206R missense is functionally validated as pathogenic via direct enzymatic assay. Genes/variants are catalogued in ClinVar and GenCC (TRMT10A: [GenCC HGNC:28403](https://search.thegencc.org/genes/HGNC:28403)).

**Functional consequence:** Loss-of-function — all characterized variants abolish or nearly abolish tRNA m¹G9 methyltransferase activity, leading to hypomodified tRNAs.

**Allele frequency:** TRMT10A biallelic pathogenic variants are each private/family-specific (found in single consanguineous kindreds); no common population founder allele has been reported. Carrier frequency has not been systematically estimated in large population databases (e.g., gnomAD) for any specific pathogenic allele given the rarity and family-specific nature of variants identified to date.

**Origin:** Germline (constitutional), consistent with a classic autosomal recessive Mendelian disease — not a somatic/cancer-associated gene.

**Modifier genes/epigenetics:** None specifically identified for MSSGM1. No DNA methylation, histone modification, or chromatin-level disease mechanism has been reported for TRMT10A-related disease; the pathology is a direct enzymatic (RNA-modification) loss-of-function, not an epigenetic-regulatory mechanism.

**Chromosomal abnormalities:** One reported case involved a **homozygous contiguous gene deletion** spanning the TRMT10A locus (Zung et al. 2015), rather than a point mutation — illustrating that both intragenic pathogenic variants and larger structural deletions of the locus can cause the syndrome.

Suggested ontology terms: **HGNC:28403** (TRMT10A); **GO:0002939** (tRNA N1-guanine methylation) / **GO:0160104** (tRNA (guanine-N1)-methyltransferase activity, if applicable term exists) for molecular function; **GO:0005730** (nucleolus) for subcellular localization.

Sources:
- [OMIM *616013 TRMT10A](https://omim.org/entry/616013)
- [Igoillo-Esteve et al. 2013 (PMC3814312)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3814312/)
- [Gillis et al. 2014](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.37341)
- [GenCC TRMT10A](https://search.thegencc.org/genes/HGNC:28403)
- [GeneCards TRMT10A](https://www.genecards.org/card/TRMT10A)

---

## 5. Environmental Information

No environmental toxin, radiation, pollutant, occupational exposure, infectious agent, or lifestyle factor has been implicated as a cause or trigger of MSSGM1 in the literature reviewed. This is a purely monogenic disease. No infectious-agent association applies. Not applicable for this disorder beyond standard supportive-care/diet management of secondary diabetes (see Treatment).

---

## 6. Mechanism / Pathophysiology

**Core molecular defect → cellular consequence → organ phenotype causal chain:**

1. **Molecular lesion:** Biallelic TRMT10A loss-of-function → loss of nucleolar tRNA m¹G9 methyltransferase activity → accumulation of **hypomodified cytoplasmic tRNAs**.
2. **Cellular consequence (pancreatic β-cells):** Igoillo-Esteve et al. (2013) demonstrated directly that "**TRMT10A silencing induces rat and human β-cell apoptosis**" — i.e., loss of TRMT10A function triggers programmed cell death specifically in insulin-producing β-cells, likely via unresolved translational/proteostatic stress from hypomodified tRNAs impairing translational fidelity/efficiency.
3. **Cellular consequence (neurons):** The same mechanistic principle is proposed to operate in the developing brain — "**TRMT10A deficiency negatively affects β-cell mass and the pool of neurons in the developing brain**" (Igoillo-Esteve et al. 2013) — i.e., reduced neuronal progenitor pool/survival during neurodevelopment, producing primary microcephaly and the associated intellectual disability.
4. **Organ/systemic consequence — glucose homeostasis:** Progressive β-cell apoptosis initially manifests as **hyperinsulinemic hypoglycemia** (proposed to reflect dysregulated/excessive insulin release from stressed or dying β-cells in early life) and evolves over time, as β-cell mass is progressively lost, into **insulin-deficient/insulin-resistant diabetes mellitus** in adolescence/young adulthood (Gillis et al. 2014: "TRMT10A deficiency accounts for abnormalities in glucose homeostasis initially manifesting both ketotic and non-ketotic hypoglycaemic events with transition to diabetes in adolescence, perhaps as a consequence of accelerated β cell apoptosis"). A separate arm — peripheral **insulin resistance** — is also directly documented (low Matsuda index in Yew 2016; marked insulin resistance responsive to metformin in Lin et al. 2020), suggesting the metabolic phenotype has both a β-cell-apoptotic/insulin-secretory component and a peripheral insulin-sensitivity component.
5. **Organ/systemic consequence — CNS:** Impaired neuronal pool generation during development → primary microcephaly, global developmental delay, intellectual disability, and (in a subset) epilepsy.
6. **Growth:** Short stature is proportionate and likely reflects a combination of the systemic translational-stress mechanism (affecting growth-plate chondrocytes and other proliferating tissues generally) plus downstream endocrine dysfunction (delayed puberty), though a specific growth-hormone-axis lesion has not been demonstrated.

**Upstream vs. downstream:** The TRMT10A enzymatic defect is the single upstream initiating lesion; β-cell apoptosis/dysfunction and impaired neurodevelopmental neuron pool are parallel (not sequential) downstream consequences occurring in different tissues due to the same ubiquitous but tissue-enriched enzyme loss — i.e., a "single-gene, two-tissue convergent phenotype" pattern (analogous in structure to modules like `metabolic_intoxication_decompensation` but distinct in that here the same molecular lesion independently damages two enriched-expression tissues rather than one metabolic block causing a toxic cascade).

**Cell types/tissues involved:**
- Pancreatic islet β-cells (insulin-secreting)
- Neural progenitor cells / developing cortical neurons

**Suggested ontology terms:**
- **GO:0006915** apoptotic process (β-cell apoptosis)
- **GO:0002943** tRNA dihydrouridine synthesis / **GO:0030488** tRNA methylation (general parent term; more specific m¹G9 term may need verification via OAK)
- **CL:0000169** type B pancreatic cell (β-cell)
- **CL:0011020** neural progenitor cell / **CL:0000540** neuron
- **UBERON:0000006** islet of Langerhans
- **UBERON:0000955** brain / **UBERON:0001851** cortex

**Molecular profiling:** No transcriptomic, proteomic, or single-cell datasets specific to human TRMT10A-deficient tissue were identified in this search; the primary functional evidence is (a) direct in vitro enzymatic methyltransferase assays on recombinant mutant protein (Gillis 2014) and (b) siRNA-knockdown apoptosis assays in rat/human β-cell lines (Igoillo-Esteve 2013). No CRISPR screen or multi-omics human-tissue dataset for this specific gene/disease was found.

Sources:
- [Igoillo-Esteve et al. 2013, PLOS Genetics (PMC3814312)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3814312/) — direct quotes above
- [Gillis et al. 2014, J Med Genet](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.37341) — direct quote above
- [Yew et al. 2016 (PMC4995728)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4995728/) — Matsuda index data

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Brain (microcephaly, structural under-development), pancreas (endocrine islets — β-cell loss)
- **Secondary/complication-related:** Kidney (hypoplastic kidneys reported in one case), skeletal system (short stature, scoliosis, osteoporosis), reproductive/endocrine axis (delayed puberty, primary amenorrhea)
- **Body systems:** Nervous system, endocrine system, skeletal system, and (in one case) renal system

**Tissue/cell level:**
- Pancreatic islet β-cells (CL:0000169)
- Neural progenitor cells / cortical neurons during development
- Bone (osteoporosis) — osteoblast/osteoclast balance not specifically studied

**Subcellular level:**
- **Nucleolus** (GO:0005730) — the specific subcellular site where TRMT10A functions and where tRNA modification occurs, per Igoillo-Esteve et al. 2013 ("TRMT10A localizes to the nucleolus of β- and non-β-cells")
- Cytoplasm — the ultimate site of action of the modified tRNAs during translation

**Localization/laterality:** No lateralization is described; microcephaly and short stature are symmetric/systemic findings; hypoplastic kidney was reported without specified laterality detail in the abstract reviewed.

Suggested UBERON terms: UBERON:0000955 (brain), UBERON:0001264 (pancreas), UBERON:0000006 (islet of Langerhans), UBERON:0002113 (kidney), UBERON:0001474 (bone element).

---

## 8. Temporal Development

- **Onset:** Congenital/perinatal for microcephaly and short stature (present from birth); infancy/early childhood for hyperinsulinemic hypoglycemia; adolescence to young adulthood for overt diabetes mellitus (reported range: age 14–22 in the original Moroccan family vs. mid-20s in the milder Scottish family, per Yew 2016) — i.e., a **chronic, congenital-onset, progressive disorder** with a delayed/evolving metabolic phenotype.
- **Progression:** The metabolic axis specifically shows a **biphasic progression** — early hypoglycemia (proposed β-cell dysregulation/early apoptosis phase) transitioning to diabetes (progressive β-cell loss) over years. Neurodevelopmental features (intellectual disability, microcephaly) are generally static/non-progressive once established, though in some patients head circumference "normalized" with growth (Yew 2016), suggesting variable postnatal catch-up in milder alleles.
- **Disease course pattern:** Chronic, lifelong; not relapsing-remitting. No spontaneous remission of the metabolic or neurodevelopmental features has been described.
- **Critical periods:** Neurodevelopment (prenatal through early childhood) appears to be the critical window during which loss of TRMT10A most directly determines the eventual degree of microcephaly/intellectual disability, given the mechanism operating on the developing neuronal progenitor pool.

Sources: as above (Igoillo-Esteve 2013; Gillis 2014; Yew 2016).

---

## 9. Inheritance and Population

- **Epidemiology:** MSSGM1 is an ultra-rare disease. No formal prevalence or incidence estimate (per 100,000) has been published; the disease is known from approximately **15–20 reported probands worldwide** across independent kindreds (Moroccan, Uzbek Jewish/Israeli, Scottish, Chinese, Turkish, and others), consistent with Orphanet-level "ultra-rare" classification. A knowledge-base entry should record `prevalence_class: NOT_YET_DOCUMENTED` or a qualitative `ULTRA_RARE` band rather than a specific numeric rate, given the absence of a published epidemiological study.
- **Inheritance pattern:** Autosomal recessive (AR) — confirmed across every reported kindred (biallelic variants, unaffected heterozygous parents, consanguinity in essentially all reported families).
- **Penetrance:** Appears complete for the core phenotype (microcephaly, short stature) among biallelic carriers reported to date, though the specific metabolic sub-phenotype (hypoglycemia vs. diabetes vs. isolated neurodevelopmental disease without metabolic findings, per the 2026 report) is variable/genotype-dependent.
- **Expressivity:** Variable — e.g., the p.Glu27Ter Scottish family had a substantially milder, later-onset phenotype (adult-onset diabetes, normalized head circumference, minimal dysmorphism) compared with the original Moroccan R127X family and the Uzbek Jewish G206R family (severe congenital microcephaly, childhood-onset hyperinsulinemic hypoglycemia, seizures).
- **Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically reported.
- **Founder effects:** Each reported pathogenic variant appears to be family/population-specific (Moroccan founder R127X; Uzbek Jewish founder G206R), consistent with **multiple independent founder mutations** in geographically/ethnically distinct consanguineous populations rather than one recurring global founder allele.
- **Consanguinity:** A major contributing factor — nearly every published kindred involved first-cousin or otherwise consanguineous unions, as expected for a fully recessive ultra-rare disease.
- **Carrier frequency:** Not established in population reference databases for any specific allele (each variant is private/rare).
- **Population demographics:** Reported cases span Moroccan, Israeli/Uzbek Jewish, Scottish/European, and Chinese/East Asian populations, indicating the disease is not restricted to a single ethnic group, though each specific pathogenic allele so far has been population/family-specific.
- **Sex ratio:** No skewed sex ratio has been reported; both males and females affected across kindreds (though some phenotypes like delayed thelarche/primary amenorrhea are necessarily reported in affected females).
- **Age distribution:** Presentation from birth (microcephaly, short stature) through childhood (hypoglycemia) to adolescence/young adulthood (diabetes diagnosis); no adult-onset-only presentation has been described absent the childhood neurodevelopmental features.

---

## 10. Diagnostics

**Laboratory tests:**
- Fasting glucose, insulin, C-peptide (to characterize hyperinsulinemic hypoglycemia in early presentation)
- HbA1c (for diabetes monitoring — e.g., decreased from 14.4% to 6.8% with metformin in the Lin et al. 2020 case)
- Oral glucose tolerance testing with Matsuda index calculation for insulin sensitivity (used in Yew 2016)
- Anti-GAD65 antibody (reported feature; may be used to help exclude autoimmune/type 1 diabetes in differential diagnosis)
- Insulinogenic index / disposition index for β-cell function assessment

**Genetic testing:**
- **Targeted gene testing / gene panel** for TRMT10A is the primary recommended approach once the clinical triad (microcephaly + short stature + glucose dysregulation) is recognized; several diagnoses were made via **targeted next-generation sequencing panels** for monogenic diabetes (Yew 2016; Lin 2020).
- **Whole-exome sequencing (WES)** was the discovery method in the original families (Igoillo-Esteev 2013; Gillis 2014) and remains appropriate when the phenotype is not immediately recognized as monogenic-diabetes-related.
- **Chromosomal microarray (CMA)** is relevant given at least one reported case involved a contiguous gene deletion encompassing TRMT10A (Zung et al. 2015) rather than a point mutation — CMA/deletion analysis should be considered when sequencing is negative but phenotype is compatible.
- Standard monogenic-diabetes gene panels (e.g., MODY panels) may include TRMT10A in comprehensive versions; clinicians are advised (per Yew et al. 2016) that "**TRMT10A sequencing should be considered in children or adults with young-onset diabetes who have a history of intellectual disability, microcephaly and epilepsy.**"

**Imaging:** Head circumference/growth charting for microcephaly; brain MRI to characterize any structural abnormality (specific MRI findings were not detailed in the sources reviewed here, and would need per-case verification before citing generically).

**Clinical criteria:** No formal consensus diagnostic criteria/society guideline was identified (consistent with the disease's rarity); diagnosis rests on the clinical triad (microcephaly + short stature + glucose dysregulation) plus confirmatory molecular genetic testing.

**Differential diagnosis:** Should include other monogenic diabetes/growth-microcephaly syndromes — notably **MSSGM2 (IGF2BP1)**, **NSMCE2-related primordial dwarfism**, **Wolcott-Rallison syndrome**, and other syndromic causes of congenital hyperinsulinism/primordial dwarfism with microcephaly (e.g., MOPD II/PCNT). Molecular confirmation is essential to distinguish these overlapping phenotypes.

**Screening:** No population newborn-screening or carrier-screening program specifically targets TRMT10A (disease too rare); targeted carrier testing may be offered within consanguineous families with a known proband variant.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No specific survival statistics or life-expectancy data were identified in the sources reviewed; the disease has not been characterized as immediately life-threatening in reported cases, though severe/prolonged hypoglycemic episodes in infancy carry inherent neurological risk if unrecognized/untreated, and uncontrolled diabetes carries the usual long-term complication risk.
- **Morbidity:** Lifelong intellectual disability and short stature are essentially fixed; ongoing management burden from diabetes/insulin resistance, and skeletal complications (scoliosis, osteoporosis) may accrue over time.
- **Complications:** Diabetes-related complications (standard long-term diabetic complications would be expected if poorly controlled, though not specifically documented in this small case literature); seizure disorder in a subset; renal hypoplasia in at least one reported case.
- **Recovery potential:** The neurodevelopmental component (microcephaly, intellectual disability) is not reversible; the metabolic component is **manageable** with standard diabetes therapy, and in at least one case responded very well to **metformin** (HbA1c improved from 14.4% to 6.8% within 3 months; Lin et al. 2020), indicating meaningful treatment-responsive disease course for the insulin-resistant subtype.
- **Prognostic factors:** Genotype severity appears to correlate with phenotype severity (complete loss-of-function alleles like R127X and G206R associated with more severe congenital phenotype vs. the milder p.Glu27Ter Scottish kindred) — this is the closest available "prognostic biomarker," i.e., genotype itself, though small numbers preclude a rigorous prognostic model.

---

## 12. Treatment

There is **no disease-modifying or curative therapy** for the underlying TRMT10A enzymatic defect; management is entirely **symptomatic/supportive**, targeted at the metabolic and neurodevelopmental manifestations.

**Pharmacotherapy (metabolic management):**
- **Insulin therapy** — for hypoglycemia management in infancy (in the hyperinsulinemic-hypoglycemia phase) and/or for insulin-deficient diabetes later in disease course. NCIT term: `NCIT:C15986` (Pharmacotherapy) generically, or a more specific insulin/glucose-management term if available.
- **Metformin** — demonstrated highly effective for the insulin-resistance-predominant metabolic phenotype (HbA1c 14.4%→6.8% in 3 months in the Chinese case; Lin et al. 2020). `therapeutic_agent`: CHEBI:6801 (metformin); `treatment_term`: NCIT:C15986 Pharmacotherapy.
- Standard diabetes monitoring and dietary management for glucose control (dietary intervention, `NCIT:C15447`).

**Supportive/rehabilitative:**
- Physical therapy, occupational therapy, and special-education/developmental support for intellectual disability and motor delay (`NCIT:C15302` Physical Therapy; general developmental/rehabilitation services `NCIT:C15315`).
- Management of seizures with standard antiepileptic therapy where epilepsy is present (specific agent not detailed per-case in sources reviewed).
- Endocrine management of delayed puberty (e.g., hormone replacement as clinically indicated).
- Orthopedic monitoring/management for scoliosis and osteoporosis.

**Genetic counseling:** Recommended for affected families given the autosomal recessive inheritance and typically consanguineous presentation (`NCIT:C15240` Genetic Counseling).

**Experimental/advanced therapeutics:** No gene therapy, RNA-based therapy, or targeted molecular therapy specific to TRMT10A deficiency has been reported or is in clinical trials, based on the sources reviewed. No NCT-registered trial specific to this disease was identified.

**Treatment strategy:** Because the metabolic phenotype has (at least) two distinct pathophysiological arms — β-cell apoptosis/insulin deficiency vs. peripheral insulin resistance — treatment should be individualized based on which pattern predominates (insulin therapy vs. insulin-sensitizing agents like metformin), as illustrated directly by the divergent management needs and metformin responsiveness reported across cases.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (monogenic recessive disease); the only "primary prevention" avenue is **genetic counseling and reproductive risk communication** in consanguineous families with a known TRMT10A pathogenic variant, including discussion of carrier testing, prenatal diagnosis, or preimplantation genetic diagnosis (PGD) where desired and available (`NCIT:C15240` Genetic Counseling).
- **Secondary prevention:** Early recognition of the clinical triad (microcephaly + short stature + hypoglycemia/diabetes) enables earlier initiation of metabolic management, potentially preventing acute hypoglycemic neurological injury in infancy.
- **Screening:** No population-level newborn or carrier screening program exists for this ultra-rare gene; targeted familial cascade testing is the only applicable "screening" approach once a proband is identified.
- **Behavioral/public health interventions:** Not applicable — no modifiable environmental risk factor has been identified.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal disease caused by TRMT10A mutation was identified in the sources searched (no OMIA entry surfaced). This appears to be a disease characterized essentially exclusively through human clinical genetics to date; a systematic OMIA search was not exhaustively completed in this pass and should be verified independently before asserting a negative finding in the knowledge base.

---

## 15. Model Organisms

**Cellular/in vitro models:**
- **siRNA knockdown of TRMT10A in rat and human β-cell lines** — directly demonstrated increased β-cell apoptosis upon TRMT10A silencing, providing the primary functional/mechanistic evidence for the β-cell-loss arm of pathophysiology (Igoillo-Esteve et al. 2013). Evidence source classification: `IN_VITRO`.
- Recombinant enzyme assays quantifying loss of m¹G9 methylation activity for the G206R mutant (>10⁴-fold reduction vs. wild type) (Gillis et al. 2014). Evidence source: `IN_VITRO` (biochemical/`COMPUTATIONAL`-adjacent enzymatic assay).

**Animal models:**
- **IMPC (International Mouse Phenotyping Consortium) Trmt10a knockout mouse** (MGI:1920421) — systematic phenotyping identified significant abnormalities across multiple physiological systems, specifically including **homeostasis/metabolism**, **growth/size/body region**, **skeleton**, **behavior/neurological**, and **vision/eye** systems, with 11 significant phenotypes reported and 2 associated diseases linked to the gene in the IMPC database. This provides model-organism-level support (fidelity: likely MODERATE, given it is a systematic phenotyping-pipeline knockout rather than a disease-mechanism-focused study) for the growth, metabolic, and neurological dimensions of the human syndrome. Evidence source: `MODEL_ORGANISM`.
- No detailed IMPC phenotype table (specific glucose-tolerance-test results, body-weight curves, etc.) was retrievable in this pass due to dynamically loaded content; a curator populating a knowledge-base `animal_models` block should fetch the full IMPC data table directly (https://www.mousephenotype.org/data/genes/MGI:1920421) before finalizing specific readout values, rather than relying on this summary alone.

**Notable limitation:** No zebrafish, Drosophila, or C. elegans model specific to TRMT10A/MSSGM1 was identified in the sources reviewed (contrast with NSMCE2, where a zebrafish knockdown model exists — but that is a different, non-orthologous disease gene, and should not be conflated with TRMT10A model-organism evidence in the knowledge base).

**Applications:** The β-cell siRNA-knockdown model directly supports research into the apoptotic mechanism underlying the hypoglycemia-to-diabetes transition; the IMPC mouse knockout supports broader phenotype-recapitulation (growth, metabolism, neurological) but has not yet been used, per the sources found here, for a dedicated mechanistic dissection of the neurodevelopmental (microcephaly) arm of the human disease.

---

## Summary of Key Ontology Term Suggestions for Knowledge-Base Curation

| Category | Term |
|---|---|
| Disease (MONDO) | MONDO:0000208 |
| Disease (OMIM) | 616033 |
| Disease (Orphanet) | ORPHA:391408 |
| Gene | HGNC:28403 (TRMT10A) |
| Phenotype (HP) | HP:0011451 (primary microcephaly), HP:0004322 (short stature), HP:0000825 (hyperinsulinemic hypoglycemia), HP:0000819 (diabetes mellitus), HP:0040270 (insulin resistance), HP:0001249 (intellectual disability), HP:0001250 (seizures), HP:0000823 (delayed puberty) |
| Biological process (GO) | GO:0006915 (apoptotic process), tRNA methylation-related GO term (verify exact m¹G9 term via OAK) |
| Cell type (CL) | CL:0000169 (type B pancreatic cell), CL:0000540 (neuron) / neural progenitor cell |
| Anatomy (UBERON) | UBERON:0000955 (brain), UBERON:0000006 (islet of Langerhans), UBERON:0002113 (kidney) |
| Chemical/drug (CHEBI) | CHEBI:6801 (metformin) |
| Treatment (NCIT) | NCIT:C15986 (Pharmacotherapy), NCIT:C15240 (Genetic Counseling), NCIT:C15302 (Physical Therapy) |

**Important curation note:** Before final entry, all PMIDs above should be re-verified against `just fetch-reference` and cached abstracts per the dismech evidence SOP — in particular, this research pass was unable to independently confirm the exact PMID for **Gillis et al. 2014** (*J Med Genet* 51:581–586; DOI: 10.1136/jmedgenet-2014-102282) through the tools available and it is cited here by DOI/journal citation rather than a verified PMID; a curator should resolve this PMID via PubMed/`just fetch-reference` before use, and must independently verify NEC risk against the two similarly-named but distinct entities (MSSGM2/IGF2BP1 and NSMCE2-related primordial dwarfism) given their overlapping phenotype and eponym-adjacent naming pattern.

**Sources (consolidated):**
- [OMIM #616033 — MSSGM1](https://omim.org/entry/616033)
- [OMIM *616013 — TRMT10A](https://omim.org/entry/616013)
- [MedGen C4014997](https://www.ncbi.nlm.nih.gov/medgen/863434)
- [Orphanet — TRMT10A](https://www.orpha.net/en/disease/gene/TRMT10A)
- [Igoillo-Esteve et al. 2013, PLOS Genetics, PMID 24204302 (PMC3814312)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3814312/)
- [Gillis et al. 2014, J Med Genet 51:581–586](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.37341) (DOI 10.1136/jmedgenet-2014-102282)
- [Yew et al. 2016, Diabetic Medicine, PMID 26526202 (PMC4995728)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4995728/)
- [Lin et al. 2020, BMJ Open Diabetes Res Care (PMC7569974)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7569974/)
- [Zung et al. 2015, Am J Med Genet A](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.37341)
- [TRMT10A Mutation... Hypoplastic Kidneys, PMID 33448213](https://pubmed.ncbi.nlm.nih.gov/33448213/)
- [A rare syndrome: Microcephaly, diabetes mellitus, and epilepsy, PMID 38302348](https://pubmed.ncbi.nlm.nih.gov/38302348/)
- [TRMT10A-Related Neurodevelopmental Disorder Without Metabolic Findings, Human Mutation 2026](https://onlinelibrary.wiley.com/doi/10.1155/humu/8058409)
- [IMPC Trmt10a knockout mouse, MGI:1920421](https://www.mousephenotype.org/data/genes/MGI:1920421)
- [GenCC TRMT10A](https://search.thegencc.org/genes/HGNC:28403)
- [GeneCards TRMT10A](https://www.genecards.org/card/TRMT10A)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.