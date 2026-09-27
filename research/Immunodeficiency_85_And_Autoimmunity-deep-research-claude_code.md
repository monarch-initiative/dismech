---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-22T04:31:57.830202'
end_time: '2026-08-22T04:35:27.089599'
duration_seconds: 209.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 85 and Autoimmunity
  mondo_id: ''
  category: Immunological
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
  web_search_requests: 8
  num_turns: 13
  total_cost_usd: 1.2407757999999998
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 14
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 85 and Autoimmunity
- **MONDO ID:**  (if available)
- **Category:** Immunological

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 85 and Autoimmunity** covering all of the
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

Now I have comprehensive data. Here is the full research report.

# Immunodeficiency 85 and Autoimmunity (IMD85): Comprehensive Research Report

## 1. Disease Information

**Overview:** Immunodeficiency 85 and autoimmunity (IMD85) is an ultra-rare, autosomal dominant primary immunodeficiency/immune dysregulation disorder caused by a heterozygous missense mutation in *TOM1* (Target Of Myb1 Membrane Trafficking Protein). It is characterized by early-onset (first decade of life) atopic eczema and recurrent respiratory infections, progressing to multi-organ autoimmunity (autoimmune enteropathy, oligoarthritis, interstitial pneumonitis), hypogammaglobulinemia, and combined T- and B-cell dysfunction. To date it has been described in a single two-generation family (mother and son) (OMIM 619510; Keskitalo et al. 2019, PMID:31263572).

**Key Identifiers:**
- **OMIM:** 619510 (IMMUNODEFICIENCY 85 AND AUTOIMMUNITY; IMD85)
- **Causal gene OMIM:** *604700 (TARGET OF MYB1 MEMBRANE TRAFFICKING PROTEIN; TOM1)
- **HGNC:** TOM1, HGNC:11982
- **Ensembl:** ENSG00000100284 (chr22:35,299,275–35,347,995, GRCh38)
- **Chromosome location:** 22q12.3
- **Mondo:** Not independently confirmed to have a distinct MONDO ID in this search pass; would map via OMIM:619510 cross-reference — verify with `runoak -i sqlite:obo:mondo` before curating a `disease_term` binding.
- **Orphanet:** No dedicated Orphanet entry was found distinct from the OMIM/gene page (`orpha.net/en/disease/gene/TOM1` lists the gene-disease association).
- **Synonyms:** IMD85; "TOM1 deficiency"; "Dominant TOM1-associated combined immunodeficiency and autoimmunity"

**Source basis:** This entire disease concept derives from a single aggregated case report of one family (2 affected individuals across 2 generations) plus a 2025 follow-up mechanistic study on cells from the *same* two patients — not from population-level EHR or registry data. All prevalence/frequency statements below should be read as "reported in 1 family" rather than population estimates.

---

## 2. Etiology

**Disease Causal Factor:** Heterozygous, autosomal dominant, gain-of-interference (likely dominant-negative) missense mutation in *TOM1*.

**Genetic risk factor (causal variant):**
- Variant: **c.920G>A, p.Gly307Asp (p.G307D)** — genomic position chr22:35,728,994 G>A (note: this coordinate as reported may reflect an older genome build; cross-check against current GRCh38 TOM1 coordinates during curation)
- Located in the **GAT (GGA and TOM1) domain** of TOM1, which mediates ubiquitin-binding and TOLLIP interaction
- SIFT: "deleterious"; PolyPhen-2: "probably damaging"
- Affects a conserved residue
- Segregates with disease in a mother (Patient 1, II.2) and her son (Patient 2, III.1) — autosomal dominant transmission, heterozygous in both.

**No environmental, infectious, or additional genetic risk/protective factors** have been reported for this ultra-rare monogenic disorder; EBV viremia is a *consequence* of the immunodeficiency (impaired immune control), not a causal trigger. The authors explicitly note: *"phenotypic heterogeneity is common in monogenic immune diseases and points to additional genetic modifiers"* (PMID:31263572) — i.e., they flag but do not identify specific modifier loci, as onset age and severity differed markedly between mother and son.

**Gene-Environment Interactions:** None reported/studied.

---

## 3. Phenotypes

Onset, in order of typical appearance, drawn from the two reported cases (mother onset in early teens; son onset at 6 months of age — illustrating that onset is highly variable even within one family):

| Phenotype | Type | HPO Suggestion | Notes/Frequency (2/2 patients unless noted) |
|---|---|---|---|
| Atopic eczema | Symptom/sign | HP:0001047 (Atopic dermatitis) | Both; son's progressed to generalized dermatitis by age 6 |
| Recurrent respiratory tract infections | Symptom | HP:0002205 (Recurrent respiratory infections) | Both |
| Seronegative/autoimmune oligoarthritis | Sign | HP:0031370 (Oligoarthritis) or HP:0002829 (Arthritis) | Mother — diagnosed age 16 |
| Autoimmune enteropathy (vomiting, chronic diarrhea) | Sign | HP:0005263 (Autoimmune enteropathy); HP:0002014 (Diarrhea) | Son (infantile onset); mother developed chronic diarrhea in her 30s |
| Failure to thrive / profound growth failure (–4.5 SD) | Sign | HP:0001508 (Failure to thrive); HP:0004325 (Decreased body weight) | Son, onset 6 months |
| Lymphocytic interstitial pneumonitis (LIP) | Sign | HP:0006515 (Interstitial pneumonitis) / HP:0002205 | Son |
| Treatment-resistant psoriasis vulgaris | Sign | HP:0003765 (Psoriasiform dermatitis) | Son |
| Persistent low-copy EBV viremia (200–800 copies/mL) | Lab abnormality | HP:0032101 (Abnormal susceptibility to viral infections) | Mother |
| Hypogammaglobulinemia (↓IgG, IgA, IgM) | Lab abnormality | HP:0004313 (Hypogammaglobulinemia) | Both |
| Lymphopenia | Lab abnormality | HP:0001888 (Lymphopenia) | Mother (660/µL vs. 1300–3600 ref) |
| Reduced switched memory B cells (0%) | Lab abnormality | HP:0005404 (Decreased proportion of switched memory B cells) | Both |
| Reduced NK cells | Lab abnormality | HP:0011037 (Decreased NK cell count) | Both |
| Reduced plasmacytoid/monocytoid dendritic cells | Lab abnormality | HP:0002846 (abnormal dendritic cell) — check specificity | Both |
| Impaired T-cell maturation (↑naive, ↓TEM/TEMRA) | Lab abnormality | HP:0005403 (Impaired T cell function) | Both |
| Impaired Treg suppressive function | Lab abnormality | — | Son (mother's Tregs were functionally normal despite normal numbers) |
| Poor IFN-γ / IL-17 secretion on stimulation | Lab abnormality | — | Both |
| Pulmonary fibrosis (progressive, post-transplant) | Sign | HP:0002206 (Pulmonary fibrosis) | Son, terminal event |

**Severity/progression:** Highly variable between the two patients despite an identical variant — the mother's course was comparatively indolent (survives to at least age 32 at publication), while the son had a fulminant infantile-onset multi-organ course, received an allogeneic HSCT around age 9, rejected the graft within 6 months, and died approximately one year post-transplant from progressive pulmonary fibrosis. This intrafamilial variability is explicitly discussed by the authors as evidence for unidentified modifiers.

**Quality of life impact:** Not formally measured (no EQ-5D/SF-36 data); qualitatively, the son's disease was fatal, and the mother required chronic immunosuppression (prednisolone, methotrexate) and immunoglobulin replacement (subcutaneous, after IVIG was discontinued for adverse effects).

---

## 4. Genetic/Molecular Information

**Causal Gene:** *TOM1* (HGNC:11982; OMIM *604700), located 22q12.3.

**Pathogenic Variant:**
- c.920G>A; p.(Gly307Asp), heterozygous, missense
- ACMG classification not explicitly stated in the source, but functionally characterized as pathogenic via multiple orthogonal assays (interactome, autophagy, apoptosis, signaling)
- Not present in population databases at appreciable frequency (implied by rarity; not explicitly quoted with a gnomAD frequency in the sources retrieved)
- **Functional consequence: dominant-negative / loss-of-interaction.** The mutant protein is expressed at normal levels (confirmed by Western blot) but is functionally crippled at the protein-interaction level — this is *not* a simple loss-of-function null allele, since TOM1 is expressed and heterozygosity with presumably one WT allele still yields dominant disease, consistent with dominant-negative interference or haploinsufficiency-plus-modifier effects.

**Modifier Genes:** None identified; authors explicitly call for additional families to establish modifiers explaining intrafamilial severity variation.

**Somatic vs. Germline:** Germline (heritable, present in both mother and son).

**Chromosomal Abnormalities:** None — this is a single-nucleotide missense variant, not a structural rearrangement.

**Suggested annotation:** `functional_impact_category: DOMINANT_NEGATIVE` (per dismech's GeneticContext guidance) is the best-supported categorical fit, since the mutant protein is expressed normally but interferes with a specific protein-protein interaction (TOM1–TOLLIP) required for normal pathway function.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious triggering factors are described as causal. EBV is present as an opportunistic/uncontrolled infection secondary to the immunodeficiency (i.e., a *consequence*, not a *cause*) — this should be modeled as a phenotype/complication, not an `environmental` entry with a `TRIGGERS` edge.

---

## 6. Mechanism / Pathophysiology

### Molecular Function of TOM1 (Wild-Type)
TOM1 is a multimodular endosomal adaptor protein containing VHS and GAT domains. It binds ubiquitinated cargo and, via its GAT domain, interacts with **TOLLIP** (Toll-interacting protein), clathrin, and myosin VI to regulate:
- Endosomal sorting/trafficking of ubiquitinated cargo (ESCRT-associated pathway)
- Autophagosome maturation and autophagosome–lysosome fusion
- Negative regulation of Toll-like receptor (TLR)/IL-1 receptor (PAMP) signaling
- Receptor recycling

### Causal Chain (Molecular → Cellular → Clinical)

1. **Molecular lesion:** p.G307D destabilizes the GAT domain's interaction surface.
   - AP-MS interactome: mutant TOM1 shows markedly reduced binding to **ubiquitin C** (2.8% vs. 5.7% in WT) and **TOLLIP** (11.2% vs. 22.0% in WT).
   - Follow-up mechanistic study (PMID:40936361, 2025) refines this: the mutant fails to properly release TOLLIP from PI3P-bound endosomal membranes, "impairing cargo trafficking commitment," and specifically **delays autophagosome clearance rather than blocking autophagosome formation** — LC3B–LAMP1 colocalization (a marker of autophagosome-lysosome fusion) was reduced to 54% of control.

2. **Cellular consequence — impaired autophagy:** Patient lymphocytes show decreased LC3 staining (low autophagosome count); rapamycin (an autophagy inducer) fails to rescue autophagosome number in patient cells, indicating a block downstream of induction (at the fusion/maturation step).

3. **Cellular consequence — dysregulated signaling:** 
   - Baseline: ERK1/2 phosphorylation significantly downregulated; STAT1 and STAT5 phosphorylation impaired (p38, S6 relatively preserved) — quote: *"ERK1/2 phosphorylation was significantly downregulated in both patients...indicating dysfunctional MAPK signaling."*
   - Under acute stimulation (LPS/IL-1β), the 2025 follow-up found the opposite direction — **more robust ERK1/2 phosphorylation** after LPS/IL-1β stimulation in patient fibroblasts than controls — consistent with **loss of the normal negative-regulatory ("braking") function TOM1/TOLLIP exert over innate immune signaling**, i.e., a switch from tonic under-signaling to stimulus-triggered over-signaling. Curators should note this apparent directionality difference between the 2019 and 2025 papers reflects different cell types/conditions (baseline vs. acute PAMP stimulation) rather than a contradiction, and both should be captured as distinct pathophysiology nodes.

4. **Cellular consequence — enhanced apoptosis:** PBMCs from both patients show elevated apoptotic/dead-cell fractions (~50% of the son's lymphocytes showed an apoptotic phenotype).

5. **Immune cell consequences:**
   - Impaired T-cell maturation: increased naive, decreased effector memory (TEM) and TEMRA subsets; poor IFN-γ and IL-17 secretion upon stimulation.
   - Regulatory T cells: normal numbers but impaired suppressive function (notably in the son).
   - B cells: severely reduced switched memory B cells (0% in both, vs. 6.5–29.2% reference) and hypogammaglobulinemia (IgG, IgA, IgM all low).
   - NK cells and plasmacytoid/monocytoid dendritic cells: markedly reduced in both patients.

6. **Clinical manifestation:** The combination of (a) impaired autophagy/autophagosome clearance, (b) dysregulated (both tonic-low and stimulus-triggered-high) MAPK/JAK-STAT signaling, (c) enhanced lymphocyte apoptosis, and (d) broad lymphoid subset abnormalities (T, B, NK, DC) together produce a **combined immunodeficiency with concurrent multi-organ autoimmunity** — impaired pathogen clearance/antibody production coexisting with loss of normal negative regulation of inflammatory signaling and defective Treg function, permitting autoimmune tissue damage (skin, gut, lung, joints).

### Suggested Ontology Terms
- **GO Biological Process:** GO:0016236 (macroautophagy), GO:0000045 (autophagosome assembly), GO:1901097 (negative regulation of autophagosome maturation — for the mutant defect), GO:0034249 (negative regulation of cellular amide metabolic process; consider more specific TLR-signaling terms), GO:0034141 (positive regulation of toll-like receptor 3 signaling pathway) as a starting point for TLR/PAMP regulation, GO:0006915 (apoptotic process), GO:0007265 (Ras protein signal transduction)/ERK cascade terms (GO:0070371, ERK1 and ERK2 cascade), GO:0006355/JAK-STAT terms
- **GO Molecular Function:** GO:0043130 (ubiquitin binding)
- **GO Cellular Component:** GO:0005768 (endosome), GO:0005771 (multivesicular body), GO:0000421 (autophagosome membrane)
- **Cell types (CL):** CL:0000542 (lymphocyte), CL:0000236 (B cell), CL:0000818 (switched memory B cell), CL:0000625 (CD8+ T cell), CL:0000895 (naive thymus-derived CD4-positive T cell), CL:0000815 (regulatory T cell), CL:0000623 (natural killer cell), CL:0000784 (plasmacytoid dendritic cell)
- **CHEBI:** N/A (no small-molecule mechanism per se, though rapamycin/tacrolimus are relevant to treatment)

---

## 7. Anatomical Structures Affected

- **Primary organ systems:** Skin (eczema, psoriasis), gastrointestinal tract (autoimmune enteropathy), respiratory system (lung — interstitial pneumonitis/fibrosis; also recurrent infections), musculoskeletal (joints — oligoarthritis), immune system (lymphoid compartment broadly)
- **UBERON suggestions:** UBERON:0002097 (skin of body), UBERON:0002108 (small intestine), UBERON:0002048 (lung), UBERON:0000982 (joint), UBERON:0002193 (hemolymphoid system)
- **Tissue/cell level:** Lymphocytes (T, B, NK), dendritic cells, epithelial cells of gut and lung
- **Subcellular level (GO CC):** Early/late endosome, autophagosome, lysosome — the primary subcellular site of the molecular defect
- **Laterality:** Not applicable (systemic/multi-organ disease, not lateralized)

---

## 8. Temporal Development

- **Onset:** Highly variable within the single reported family — infantile (6 months, son) to early-teen (mother). No population-level onset statistics exist given the single-family basis.
- **Onset pattern:** Insidious/progressive in both cases, punctuated by acute complications (e.g., graft rejection in the son).
- **Progression:** Progressive and severe in the son (death ~1 year post-HSCT from progressive pulmonary fibrosis); more indolent/chronic in the mother, who was alive and on chronic immunosuppression/Ig replacement at age 32 at time of publication.
- **Disease course pattern:** Chronic, progressive, with episodic flares (e.g., eczema/respiratory flares triggered by an mTOR-inhibitor trial in the son).
- **Remission:** Temporary — HSCT produced "temporary resolution of autoimmune symptoms" in the son, but this was lost within 6 months due to graft rejection, after which "the disease returned."
- **Critical periods:** Infancy appears to represent a high-risk window for the most severe, multi-organ, rapidly progressive presentation, based on the son's course.

---

## 9. Inheritance and Population

- **Epidemiology:** Reported in exactly one family (2 affected individuals) worldwide as of the literature retrieved — true prevalence/incidence cannot be estimated; this is an ultra-rare "N-of-1 family" monogenic disease.
- **Inheritance pattern:** Autosomal dominant (heterozygous mutation, vertical transmission mother→son).
- **Penetrance:** Appears complete in this family (both carriers affected) but expressivity is markedly variable (see below).
- **Expressivity:** Highly variable — same p.G307D variant produced a comparatively milder, later-onset course in the mother versus a severe, fatal, infantile-onset course in the son. Authors explicitly attribute this to likely unidentified genetic modifiers.
- **Genetic anticipation:** Potentially suggested by the pattern (later/milder in mother vs. earlier/more severe in son), but this cannot be distinguished from stochastic/modifier effects with an n=2 pedigree; not formally established.
- **Germline mosaicism, founder effects, consanguinity, carrier frequency:** Not applicable/not reported — this is a de novo-type autosomal dominant single-family report, not a population-level recessive or founder disease.
- **Population demographics:** Not established (single Northern European-ancestry family per source institution context — precise ancestry not stated in retrieved excerpts). Sex ratio: 1 female (mother), 1 male (son) — no inference possible from n=2.

---

## 10. Diagnostics

**Laboratory/Immunophenotyping (as performed in the index family):**
- Complete blood count with lymphocyte subsets (flow cytometry): CD19+ B cells, switched memory B cells, CD4+/CD8+ T cells, NK cells, plasmacytoid and monocytoid dendritic cells
- Quantitative immunoglobulins (IgG, IgA, IgM) — both patients markedly hypogammaglobulinemic
- T-cell functional assays: cytokine secretion (IFN-γ, IL-17) upon stimulation; Treg suppression assays
- Phospho-flow cytometry for STAT1, STAT5, ERK1/2, p38, S6 signaling
- LC3 immunostaining (autophagosome quantification) in lymphocytes/fibroblasts
- Apoptosis assays (annexin V/PI or equivalent) on PBMCs

**Genetic Testing:**
- Whole-exome or targeted sequencing identified the heterozygous *TOM1* c.920G>A (p.G307D) variant; Sanger confirmation and familial segregation testing would be standard practice for a suspected combined immunodeficiency with autoimmunity phenotype.
- Given the phenotypic overlap with other combined immunodeficiency/immune dysregulation syndromes (e.g., CVID, ALPS, IPEX-like disorders), a **primary immunodeficiency/monogenic IBD gene panel** is the practical diagnostic entry point — *TOM1* is listed on the PanelApp (Genomics England) "Primary immunodeficiency or monogenic inflammatory bowel disease" panel and the PanelApp Australia "Autoinflammatory Disorders" panel.

**Functional/Research-Level Confirmatory Testing (not yet clinical-grade):**
- AP-MS interactome analysis (TOM1–TOLLIP, TOM1–ubiquitin binding)
- LC3B–LAMP1 colocalization imaging (autophagosome-lysosome fusion assay)
- Response of ERK1/2 phosphorylation to LPS/IL-1β stimulation in patient-derived fibroblasts

**Clinical Criteria:** No formal consensus diagnostic criteria exist (single-family disease); diagnosis is genotype-driven with immunophenotypic and functional corroboration.

**Differential Diagnosis:** Should include other genetic causes of combined immunodeficiency with autoimmune enteropathy (e.g., IPEX/FOXP3, LRBA deficiency, CTLA4 haploinsufficiency, STAT3 GOF), CVID with autoimmune features, and other autophagy-pathway immune dysregulation disorders. Notably, the 2019 paper specifically tested and found normal CTLA4, IL-1R, and IL-6R expression, ruling out a primary receptor-expression defect and supporting a trafficking/autophagy-centric mechanism instead.

**Screening:** No population or newborn screening applicable (ultra-rare, private family variant).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** The son (severe, infantile-onset presentation) died approximately 1 year after allogeneic HSCT, from progressive pulmonary fibrosis following graft rejection — total lifespan to age ~10. The mother remained alive at age 32 at the time of reporting, managed on chronic immunosuppression and immunoglobulin replacement.
- **Morbidity:** Substantial — chronic autoimmune enteropathy, growth failure, recurrent infections, interstitial lung disease, and treatment-refractory skin disease.
- **Complications:** EBV viremia, treatment-resistant psoriasis, graft rejection post-HSCT, progressive pulmonary fibrosis (fatal in the reported case).
- **Recovery potential:** HSCT achieved only *temporary* resolution of autoimmune symptoms before graft rejection at 6 months; this single data point suggests HSCT may not be reliably curative for this genotype, though n=1 limits generalization.
- **Prognostic factors:** Age of onset (infantile vs. teenage) appeared associated with severity in this family, though this cannot be statistically validated given n=2.

---

## 12. Treatment

**Pharmacotherapy used in the reported family (NCIT terms suggested):**
- **Prednisolone** (oral corticosteroid) — mother; ongoing — NCIT:C15986 (Pharmacotherapy) + therapeutic_agent CHEBI (prednisolone)
- **Methotrexate** — both patients — NCIT:C15986
- **Tacrolimus** (oral) — son — NCIT:C15986
- **Everolimus** (mTOR inhibitor) — trialed in the son specifically to target autoimmunity (rationale: mTOR/autophagy pathway involvement) but **caused adverse flares** of eczema and respiratory distress — an important negative treatment-response finding worth capturing as a `NO_EVIDENCE`/adverse-effect annotation rather than a recommended therapy
- **Intravenous immunoglobulin (IVIG)** — mother; discontinued due to adverse effects — NCIT (immunoglobulin replacement therapy term)
- **Subcutaneous immunoglobulin replacement** — both patients, ongoing — better tolerated than IVIG

**Cell therapy:**
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — son, at approximately age 9 — NCIT:C15431 (Hematopoietic Cell Transplantation) → `therapeutic_modality: CELL_THERAPY`. Achieved temporary resolution of autoimmune symptoms; graft rejected within 6 months; disease recurred; patient died ~1 year post-transplant of progressive pulmonary fibrosis.

**Treatment strategy/algorithm:** No established treatment algorithm exists given the single-family basis; management to date has been empirically immunosuppressive/replacement-based (corticosteroids, methotrexate, calcineurin inhibitor, Ig replacement) with HSCT attempted as a potentially curative but ultimately unsuccessful option in the most severe case. The failed everolimus trial is a notable cautionary data point suggesting mTOR inhibition is not an effective/safe strategy despite the pathway's mechanistic proximity (autophagy regulation).

**Experimental treatments:** None in formal clinical trials (no NCT identifiers found; this is far too rare for a registered trial).

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies are described or applicable — this is a private autosomal dominant germline variant in a single known family. The only relevant preventive consideration would be **genetic counseling** for at-risk relatives (NCIT:C15240, Genetic Counseling) and prenatal/preimplantation testing if desired by family members, given the 50% transmission risk from an affected parent, though none of this is explicitly documented in the retrieved sources.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring TOM1-associated disease has been reported in non-human species in the sources retrieved.
- **Orthologous gene:** *Tom1* — mouse ortholog MGI:1338026 (chromosome 8C1); zebrafish ortholog *tom1* (ZFIN ZDB-GENE-060721-1). TOM1-family genes are evolutionarily conserved (TOM1, TOM1L1, TOM1L2 paralogs in humans; original TOM1 gene family first mapped via similarity to endosomal proteins HGS and STAM, PMID:10329004).
- **Comparative biology:** No OMIA (Online Mendelian Inheritance in Animals) entry or veterinary case series identified. No evidence of naturally occurring veterinary TOM1-associated immunodeficiency.
- **Transmission/zoonotic potential:** Not applicable — this is a monogenic, non-infectious, non-transmissible-between-species disorder.

---

## 15. Model Organisms

- **No animal (mouse, zebrafish) or invertebrate models of the specific p.G307D variant or of TOM1 loss-of-function immunodeficiency were identified** in the literature retrieved. Both key papers (Keskitalo et al. 2019, PMID:31263572; the 2025 Disease Models & Mechanisms follow-up, PMID:40936361) explicitly used **only human patient-derived material and cell-line systems** — no animal models:
  - **Patient-derived primary cells:** PBMCs and dermal fibroblasts from the two affected family members
  - **Cell lines:** Flp-In T-REx 293 cells (inducible WT vs. G307D TOM1 overexpression for interactome studies), HeLa cells (immunofluorescence/localization), HEK293A cells, U2OS cells (localization studies in the 2025 paper)
  - **Techniques:** AP-MS (affinity purification–mass spectrometry) interactome profiling, BioID proximity labeling, phospho-flow cytometry, LC3B/LAMP1 immunofluorescence colocalization
- **Model limitations:** As the field currently has *no* in vivo (mouse) model of TOM1 G307D or *Tom1* knockout immune phenotype, all mechanistic claims rest on ex vivo human patient cells and heterologous overexpression systems — a notable gap for future work, and a `HUMAN_MODEL_MISMATCH`/`KNOWLEDGE_GAP` framing does not directly apply here since there is *no* model organism data to be mismatched against; rather this is an outright absence of an animal model, worth flagging as a knowledge gap for curation purposes (no in vivo confirmation of causality/mechanism exists beyond the patient-cell/cell-line data).
- **Resources:** MGI:1338026 (mouse *Tom1*), ZFIN ZDB-GENE-060721-1 (zebrafish *tom1*) exist as gene records but no disease-phenotype model entries were found associated with them in this search.

---

## Summary of Key Citations

| PMID | Citation | Content |
|---|---|---|
| **31263572** | Keskitalo S, et al. "Dominant TOM1 mutation associated with combined immunodeficiency and autoimmune disease." *NPJ Genomic Medicine.* 2019 Jun 27;4:14. | Primary disease-defining report; index family, variant identification, immunophenotyping, interactome/autophagy/signaling mechanism, treatment/outcome |
| **40936361** | (Disease Models & Mechanisms, 2025 Sep 30;18(9):dmm052140), DOI: 10.1242/dmm.052140 | "A TOM1 variant impairs interaction with TOLLIP, autophagosome-lysosome fusion and regulation of innate immunity" — mechanistic follow-up on the same two patients; refines autophagosome-lysosome fusion defect and shows enhanced (not just reduced) ERK1/2 signaling upon acute LPS/IL-1β stimulation |
| **10329004** | (background) TOM1 gene family chromosomal mapping and homology to HGS/STAM | Gene-family background, not disease-specific |

**Curator's note on evidence discipline:** Given the disease rests on a single published family, every evidence item added to a `kb/disorders/` entry should cite PMID:31263572 (primary) and/or PMID:40936361 (mechanistic follow-up) with exact abstract/text quotes verified via `just fetch-reference` — do not extrapolate population-level prevalence, penetrance, or treatment-efficacy claims beyond what these two case-based papers report, since no larger cohort, registry, or model-organism confirmation currently exists for IMD85.

**Sources:**
- [619510 - IMMUNODEFICIENCY 85 AND AUTOIMMUNITY - OMIM](https://www.omim.org/entry/619510)
- [*604700 - TOM1 - OMIM](https://www.omim.org/entry/604700)
- [Dominant TOM1 mutation associated with combined immunodeficiency and autoimmune disease - PMC (PMID:31263572)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6597545/)
- [Dominant TOM1 mutation... - npj Genomic Medicine](https://www.nature.com/articles/s41525-019-0088-5)
- [A TOM1 variant impairs interaction with TOLLIP, autophagosome-lysosome fusion and regulation of innate immunity - PMC (PMID:40936361)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12519566/)
- [A TOM1 variant impairs interaction with TOLLIP... - Disease Models & Mechanisms](https://doi.org/10.1242/dmm.052140)
- [TOM1 Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=TOM1)
- [Gene: TOM1 (ENSG00000100284) - Ensembl](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100284)
- [Gene: TOM1 (Primary immunodeficiency or monogenic inflammatory bowel disease) - PanelApp Genomics England](https://panelapp.genomicsengland.co.uk/panels/398/gene/TOM1/)
- [TOM1 (Autoinflammatory Disorders) - PanelApp Australia](https://panelapp-aus.org/panels/238/gene/TOM1/)
- [TOM1 genes map to human chromosome 22q13.1... - PubMed (PMID:10329004)](https://pubmed.ncbi.nlm.nih.gov/10329004/)
- [Orphanet: TOM1-target of myb1 membrane trafficking protein](https://www.orpha.net/en/disease/gene/TOM1)
- [Tom1 MGI Mouse Gene Detail - MGI:1338026](https://www.informatics.jax.org/marker/MGI:1338026)
- [ZFIN Gene: tom1](https://zfin.org/ZDB-GENE-060721-1)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.