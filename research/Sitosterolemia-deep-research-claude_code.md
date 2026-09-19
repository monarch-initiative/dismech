---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-29T19:02:51.407400'
end_time: '2026-07-29T19:07:32.576666'
duration_seconds: 281.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sitosterolemia
  mondo_id: MONDO:0008863
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 16
  total_cost_usd: 1.6067379999999998
  session_id: 5dd887df-f66e-565b-8209-dadd5bf74d40
  stop_reason: end_turn
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sitosterolemia
- **MONDO ID:** MONDO:0008863 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sitosterolemia** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Sitosterolemia (Phytosterolemia): Comprehensive Research Report

## Executive Summary

Sitosterolemia is a rare autosomal recessive sterol-storage disorder caused by biallelic loss-of-function variants in *ABCG5* or *ABCG8*, which together encode the heterodimeric "sterolin" ABC half-transporter (ABCG5/ABCG8) responsible for effluxing dietary plant sterols (and excess cholesterol) from enterocytes into the intestinal lumen and from hepatocytes into bile. Loss of this transporter causes massive intestinal hyperabsorption and defective biliary/fecal excretion of plant sterols (sitosterol, campesterol, stigmasterol) and shellfish sterols, producing hypercholesterolemia, tendon/tuberous xanthomas, premature atherosclerosis, and a distinctive hematologic phenotype (hemolytic anemia with stomatocytes, macrothrombocytopenia, splenomegaly). It is a key mimic of familial hypercholesterolemia (FH) that is treated very differently — first-line therapy is dietary sterol restriction plus ezetimibe, not statins.

---

## 1. Disease Information

**Overview:** Sitosterolemia (also called phytosterolemia) is an inborn error of sterol metabolism in which plant-derived (xeno)sterols accumulate in plasma and tissues owing to failure of the intestinal/hepatic sterol efflux pump. It was first molecularly characterized in 2000–2001 when mutations in the adjacent, divergently transcribed genes *ABCG5* and *ABCG8* on chromosome 2p21 were identified as causative (Berge et al., *Science* 2000, PMID:11060012; Lee et al., *Nat Genet* 2001, PMID:11138003; Lu et al., *Am J Hum Genet* 2001, PMID:11499225).

**Key identifiers:**
- **OMIM:** Sitosterolemia 1 (STSL1), **#210250** — caused by *ABCG8* (gene *605460*); Sitosterolemia 2 (STSL2), **#618666** — caused by *ABCG5* (gene *605459*) ([OMIM #210250](https://omim.org/entry/210250), [OMIM #618666](https://www.omim.org/entry/618666))
- **MONDO:** MONDO:0020748 (per current MONDO lookups) — note: the prompt's suggested MONDO:0008863 should be independently reconciled against the live MONDO release before KB entry, since search-based lookup returned MONDO:0020748 for "sitosterolemia" as the parent grouping term; both STSL1/STSL2-specific and umbrella MONDO IDs should be checked with `runoak -i sqlite:obo:mondo` before committing.
- **Orphanet:** ORPHA:65282 (Sitosterolemia)
- **ICD-10:** E75.6 (Lipidosis, unspecified) — no dedicated sitosterolemia code exists; ICD-11 similarly lacks a specific code, falling under disorders of lipoprotein metabolism
- **MeSH:** Sitosterolemia (D032169)
- **Gene:** *ABCG5* (HGNC:13886), *ABCG8* (HGNC:13887)

**Synonyms:** Phytosterolemia; β-sitosterolemia; sitosterolemia with xanthomatosis; STSL

**Data provenance:** Nearly all published information derives from aggregated case reports/series and small cohort natural-history studies (GeneReviews estimates **~110 molecularly confirmed cases reported worldwide** as of its most recent update, though this is acknowledged to be an underestimate — [GeneReviews, NBK131810](https://www.ncbi.nlm.nih.gov/books/NBK131810/)), rather than large EHR-derived cohorts, reflecting the rarity and under-recognition of the disease.

---

## 2. Etiology

**Disease causal factors:** Sitosterolemia is a monogenic, purely genetic disorder — biallelic (homozygous or compound heterozygous) pathogenic variants in *ABCG5* or *ABCG8* are necessary and sufficient to cause disease; there is no known environmental or infectious primary cause. However, dietary plant sterol intake is the essential environmental trigger that converts the genetic lesion into the clinical phenotype — sterol accumulation and its sequelae are directly proportional to dietary exposure.

**Genetic risk factors:**
- Loss-of-function missense, nonsense, frameshift, and splice-site variants in *ABCG5* or *ABCG8* disrupting formation or trafficking of the obligate ABCG5/ABCG8 heterodimer.
- No deletions/duplications of these genes have been reported as pathogenic mechanisms in sitosterolemia (GeneReviews).
- Founder variants raise local carrier frequency in specific populations (see §9).
- Emerging evidence that **monoallelic (heterozygous) variants** may confer a milder, incompletely penetrant phenotype with modestly elevated plant sterols — an active area of genotype-phenotype research (2026 Frontiers in Nutrition review, "Molecular genetic basis and clinical heterogeneity of sitosterolemia").

**Environmental risk factors:**
- High dietary intake of plant sterol-rich foods: vegetable oils, margarine/spreads fortified with plant sterols or stanols, nuts, seeds, avocado, chocolate.
- Shellfish consumption (shellfish sterols are structurally similar xenosterols also normally excluded by ABCG5/ABCG8).
- Parenteral nutrition containing plant sterol-derived lipid emulsions can precipitate/unmask hypersterolemia, particularly in infants.
- Formula feeding in infants — immature ABCG5/G8 expression in neonates can produce transient plant-sterol elevation that is a diagnostic confounder (false positive), distinct from the fixed genetic disease.

**Protective factors:**
- No genetic protective variants specific to sitosterolemia have been described (unlike, e.g., *PCSK9* loss-of-function variants in general hypercholesterolemia).
- Environmentally, strict avoidance of dietary plant sterols/stanols and shellfish is the principal modifiable protective factor and is the mainstay of lifelong management.
- Plant stanol-containing products (campestanol, sitostanol), often recommended for general hypercholesterolemia, are **specifically contraindicated** and exacerbate sterol accumulation in sitosterolemia patients — an important clinical counter-intuitive point (GeneReviews).

**Gene-environment interactions:** This is the paradigm case of a "hyperabsorber" gene-diet interaction: in unaffected individuals, dietary plant sterols are absorbed at <5% and rapidly re-excreted by ABCG5/G8; in biallelic-variant carriers, absorption efficiency rises toward that of cholesterol (~40–60%) and biliary/fecal re-excretion is essentially abolished, so that identical dietary sterol intake produces a 30- to 100-fold difference in plasma sterol concentration between affected and unaffected individuals. Intrafamilial phenotypic variability among individuals with identical genotypes is attributed largely to differences in dietary sterol exposure (GeneReviews).

---

## 3. Phenotypes

### Clinical signs and symptoms

| Phenotype | Type | Onset | Frequency/Notes | Suggested HPO term |
|---|---|---|---|---|
| Tendon/tuberous xanthomas | Physical sign | Childhood (atypical distribution: heels, knees, elbows, buttocks) | Common presenting feature, often the first sign in children (PMC9563796) | HP:0100678 (Tendon xanthomatosis) / HP:0010741 (Tuberous xanthomas) |
| Hypercholesterolemia | Laboratory abnormality | Childhood | Marked, but paradoxically responds to diet/bile-acid sequestrants, poorly/not to statins | HP:0003124 (Hypercholesterolemia) |
| Premature/accelerated atherosclerosis | Clinical sign | Childhood through young adulthood (documented onset ages 5–33y) | Risk of angina, MI, sudden cardiac death if untreated | HP:0100762 (Coronary artery atherosclerosis) / HP:0001677 (Coronary artery disease) |
| Hemolytic anemia (with stomatocytes) | Laboratory/clinical | Any age; can be presenting feature | Chronic or episodic | HP:0004870 (Chronic hemolytic anemia) / HP:0004446 (Stomatocytosis) |
| Macrothrombocytopenia | Laboratory abnormality | Any age; may be isolated presenting finding | Giant platelets on smear, surrounded by vacuole halo | HP:0001902 (Giant platelets) / thrombocytopenia HP:0001873 |
| Impaired platelet aggregation / bleeding tendency | Clinical/lab | Variable | Paradoxical bleeding despite membrane sterol-driven "hyperreactivity" | HP:0003540 (Impaired platelet aggregation) |
| Splenomegaly | Clinical sign | Variable | Associated with hemolysis | HP:0001744 |
| Arthralgia/arthritis | Symptom | Variable, often childhood | Reported in a substantial minority | HP:0002829 (Arthralgia) / HP:0001369 (Arthritis) |
| Abnormal liver function tests | Laboratory | Variable | Can be occult; some hepatic steatosis/impairment reported | HP:0002910 (Elevated hepatic transaminase) |
| Neonatal/infantile presentation | Variable | Neonatal-infantile | Can mimic other pediatric hypercholesterolemia/hemolytic syndromes | — |

**Phenotype characteristics:**
- **Age of onset:** Predominantly childhood (xanthomas and hypercholesterolemia often detected in the first decade); hematologic presentation can occur at any age and is sometimes the sole presenting feature in adults (e.g., PMC10951126: a child presenting with hemolytic anemia/thrombocytopenia before other stigmata appeared).
- **Severity/progression:** Highly variable even within families with identical genotype — attributed to dietary sterol intake differences. Untreated disease is progressive with respect to atherosclerosis and xanthoma burden; treatment leads to xanthoma regression and normalization/improvement of hematologic indices.
- **Frequency among affected individuals:** Xanthomas and hypercholesterolemia are near-universal in classically ascertained cases; hematologic abnormalities (stomatocytic hemolysis, macrothrombocytopenia) are common but not universal, and some patients present with hematologic findings alone, without xanthomas or overt hypercholesterolemia (per GeneReviews and multiple case reports, e.g., PMID:24166850).
- **Quality of life impact:** Chronic hemolytic anemia and bleeding tendency, disfiguring xanthomas, arthralgias, and anxiety around premature cardiovascular events affect daily functioning; no disease-specific QoL instrument data were identified in the literature searched, though ASCVD risk-related morbidity (per general dyslipidemia QoL literature) applies.

---

## 4. Genetic/Molecular Information

**Causal genes:**
- ***ABCG8*** (chr 2p21; HGNC:13887; OMIM *605460) — biallelic variants cause **Sitosterolemia 1 (STSL1, OMIM #210250)**.
- ***ABCG5*** (chr 2p21, immediately adjacent to *ABCG8*, transcribed in a head-to-head/divergent orientation; HGNC:13886; OMIM *605459) — biallelic variants cause **Sitosterolemia 2 (STSL2, OMIM #618666)**.
- The two genes together account for essentially all molecularly confirmed cases; published case-series estimates of the relative proportion of *ABCG5* vs *ABCG8* cases vary by cohort/ancestry (a 2026 review reports population-dependent skew; see population section).

**Pathogenic variants:**
- **Variant types:** missense (most common), nonsense, frameshift, splice-site; sequence analysis detects >95% of pathogenic alleles; no causative large deletions/duplications reported (GeneReviews).
- **Classification:** ACMG/AMP pathogenic/likely pathogenic variants are catalogued in ClinVar for both genes (e.g., ClinVar RCV000005255 *ABCG8* c.1083G>A p.Trp361Ter; RCV000269126 *ABCG8* c.55G>C p.Asp19His).
- **Functional consequence:** Loss-of-function — disrupted heterodimer assembly/trafficking to the apical (canalicular/brush-border) membrane, or loss of ATPase/transport activity, abolishing selective sterol efflux.
- **Founder alleles** (see §9) reach carrier frequencies of several percent in isolated populations, making compound heterozygosity and homozygosity locally more frequent than the global rarity of the disease would suggest.
- **Germline vs somatic:** Exclusively germline; no somatic mosaicism or cancer-related somatic mutation relevance reported.

**Modifier genes:** No formally validated modifier genes are established; *NPC1L1* (Niemann-Pick C1-Like 1), which mediates apical intestinal cholesterol/sitosterol uptake and is the molecular target of ezetimibe (Altmann et al., *Science* 2004, PMID:15044802), is mechanistically upstream/complementary rather than a genetic modifier per se, but its pharmacologic inhibition is the basis of first-line therapy.

**Epigenetic information:** No disease-specific epigenetic (DNA methylation/histone) mechanism has been reported; sitosterolemia is a straightforward loss-of-function Mendelian disorder.

**Chromosomal abnormalities:** None reported; disease is due to intragenic point/small-indel variants, not large chromosomal rearrangements.

**Suggested ontology terms:** `hgnc:13886` (ABCG5), `hgnc:13887` (ABCG8); GO molecular function `GO:0034632` (retinol transmembrane transporter activity — analog class) is not exact; more precisely GO:1901664 (sterol transmembrane transporter activity, ABC-type) / GO:0034041 (sterol-transporting ATPase activity) should be verified via OAK before curation.

---

## 5. Environmental Information

- **Environmental factors:** Not a toxin/pollution-mediated disease; the sole relevant "environmental" input is dietary sterol load (see §2).
- **Lifestyle factors:** Diet composition (plant-sterol-rich vegetable oils, margarines, nuts, seeds, avocado, chocolate, shellfish) is the dominant modifiable lifestyle determinant of phenotype severity. No smoking/alcohol-specific interactions were identified in the literature reviewed, though these would be expected to compound general atherosclerotic risk as in any dyslipidemia.
- **Infectious agents:** Not applicable — sitosterolemia has no infectious etiology or trigger.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular lesion:** Biallelic loss-of-function variants in *ABCG5* or *ABCG8* prevent formation of a stable, functional ABCG5/ABCG8 heterodimeric ATP-binding cassette (ABC) half-transporter ("sterolin-1"/"sterolin-2") ([PMC7961684](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7961684/), 20-year review of ABCG5/G8 function).
2. **Transporter dysfunction:** ABCG5/G8 normally localizes to the apical membrane of enterocytes and the canalicular membrane of hepatocytes, where it acts as the primary, ATP-dependent, bile-salt-facilitated efflux pump exporting cholesterol and (preferentially) non-cholesterol/plant sterols into the intestinal lumen and bile, respectively. Structural work has defined a "transmembrane polar relay" that allosterically couples ATP hydrolysis to sterol translocation and confers plant-sterol-over-cholesterol substrate preference (PMC7699580).
3. **Loss of selective sterol efflux:** With the transporter absent/non-functional, dietary plant sterols (sitosterol, campesterol, stigmasterol) and shellfish sterols — which are normally absorbed at <5% efficiency and aggressively re-excreted — are instead retained and absorbed at cholesterol-like efficiency (~40–60%), while biliary/fecal excretion of both cholesterol and plant sterols is markedly reduced.
4. **Systemic and tissue accumulation:** Untreated patients show 30- to 100-fold elevation of plasma sitosterol (versus healthy controls), with sterol deposition in plasma membranes, tendon, skin (xanthomas), red cells, and platelets.
5. **Downstream cellular/tissue consequences (parallel branches):**
   - **Vascular/atherogenic branch:** Elevated total/LDL cholesterol plus phytosterol incorporation into lipoprotein particles and vascular tissue drives accelerated foam-cell formation and premature atherosclerotic plaque development (relevant to the dismech `atherogenesis` module pattern) — Current Atherosclerosis Reports 2023 review ("Update on Sitosterolemia and Atherosclerosis").
   - **Erythrocyte branch:** Incorporation of excess sterol into the red-cell membrane alters membrane fluidity/shape, producing stomatocytic red cells and chronic hemolysis with reticulocytosis and splenomegaly.
   - **Platelet branch:** Plant sterol accumulation in the platelet membrane induces **platelet hyperreactivity**; a murine model demonstrated internalization of the αIIbβ3 (GPIIb/IIIa) integrin complex and **filamin A degradation**, driving macrothrombocytopenia and a paradoxical bleeding phenotype despite baseline hyperreactivity (*Blood* 2013, "Platelet hyperreactivity explains the bleeding abnormality and macrothrombocytopenia in a murine model of sitosterolemia"). A 2024 platelet proteomics study (*Blood Advances* 8(10):2466) found the platelet proteome is longitudinally stable pre/post treatment and concluded thrombocytopenia is "driven by lipid disorder and not [primary] platelet aberrations" — supporting a lipid-membrane-mediated rather than intrinsic megakaryocytic mechanism.
   - **Hepatic branch:** Reduced biliary cholesterol/sterol secretion causes hepatic sterol retention; mouse knockout studies show "failure to secrete biliary cholesterol" as a direct consequence of Abcg8 loss (PMC394351), and human patients can show occult hepatic transaminase elevation.

**Cell types involved:** enterocyte (`CL:0000584`, absorptive cell of intestinal epithelium), hepatocyte (`CL:0000182`), erythrocyte (`CL:0000232`), platelet/thrombocyte (`CL:0000233`), macrophage/foam cell (`CL:0000235` / foam cell context), vascular smooth muscle cell.

**Suggested GO biological process terms:** GO:0032367 (intracellular cholesterol transport), GO:0033344 (cholesterol efflux), GO:0010875 (positive regulation of cholesterol efflux — inverse applies as loss), GO:0034381 (plasma lipoprotein particle clearance), GO:0006febris — verify exact plant-sterol transport GO term via OAK (candidate: GO:0034191, apolipoprotein-mediated... not exact; recommend `runoak -i sqlite:obo:go search "sterol transport"` during curation).

**Molecular profiling / advanced technologies:** The 2024 platelet proteomics paper (Blood Advances) is the most direct "omics" dataset identified; no transcriptomic/spatial/single-cell atlas specific to sitosterolemia tissue was found in this search — an evidence gap worth flagging in a KB `discussions`/`KNOWLEDGE_GAP` entry.

---

## 7. Anatomical Structures Affected

- **Organ level:**
  - Primary: small intestine (enterocyte apical membrane), liver (hepatocyte canalicular membrane) — the two sites of normal ABCG5/G8 expression and action.
  - Secondary/complication organs: cardiovascular system (coronary arteries — atherosclerosis), skin/tendons (xanthomas), spleen (splenomegaly from hemolysis), joints (arthritis/arthralgia), bone marrow (reactive/compensatory changes to hemolysis).
  - Body systems: digestive, cardiovascular, hematologic/lymphoid, musculoskeletal, integumentary (dermatologic).
- **Tissue/cell level:** intestinal absorptive epithelium; hepatobiliary canalicular epithelium; vascular endothelium/intima (atheroma); erythrocyte membrane; platelet/megakaryocyte membrane; xanthoma histiocytes/foam cells in tendon and skin.
- **Subcellular level:** plasma membrane (apical enterocyte membrane, canalicular hepatocyte membrane, erythrocyte/platelet membrane) is the principal subcellular site of ABCG5/G8 localization and sterol accumulation (GO Cellular Component candidate: `GO:0016324` apical plasma membrane; `GO:0016323` basolateral plasma membrane for contrast; `GO:0005903` brush border).
- **Localization (UBERON):** small intestine (`UBERON:0002108`), liver (`UBERON:0002107`), coronary artery (`UBERON:0001621`), tendon (`UBERON:0000043`), spleen (`UBERON:0002106`).
- **Lateralization:** Not applicable — systemic/bilateral disease process, no laterality preference.

---

## 8. Temporal Development

- **Onset:** Typically pediatric — xanthomas and hypercholesterolemia usually detected in childhood; hematologic presentation can occur from infancy through adulthood. Documented atherosclerotic onset ages range from 5 to 33 years in untreated patients (GeneReviews).
- **Onset pattern:** Insidious/chronic for the sterol-accumulation and xanthoma phenotype; the hemolytic anemia can be chronic or episodic (HP:0004802, Episodic hemolysis).
- **Progression:** Untreated disease is progressive with respect to xanthoma burden and atherosclerotic disease; treated disease shows xanthoma regression and stabilization/improvement of lipid and hematologic parameters.
- **Disease course pattern:** Chronic lifelong metabolic disorder requiring ongoing dietary/pharmacologic management; not self-limited.
- **Remission patterns:** No spontaneous remission; treatment-induced improvement (xanthoma regression, normalization of platelet count/hemolysis markers) is well documented with dietary restriction plus ezetimibe.
- **Critical periods:** Early diagnosis and treatment initiation (ideally before significant atherosclerotic burden accrues) is emphasized as critical to prognosis; treatment experience in children <2 years is limited (GeneReviews notes this explicitly as a management caveat).

---

## 9. Inheritance and Population

**Epidemiology:**
- Historically reported as exceedingly rare, with wide-ranging prevalence estimates: sources cite figures from ~1 in 200,000 to 1 in a million; a more recent gnomAD-based allele-frequency analysis suggested population studies imply a range of roughly **1/384 to 1/48,076** carriers/cases (95% CI) once under-ascertainment is accounted for, and a separate estimate placed global prevalence at "at least 1 in 2.6 million" for an ABCG5 mutation and "1 in 360,000" for an ABCG8 mutation (search-sourced NORD/derivative summary) — these figures are inconsistent across sources and should be treated cautiously/flagged as an evidence gap; the recurring theme across essentially all recent literature is that the disease is substantially **under-recognized and under-diagnosed**, particularly in hypercholesterolemic children misclassified as FH (PMC7449458: "High prevalence of increased sitosterol levels in hypercholesterolemic children suggest underestimation of sitosterolemia incidence").
- ~110 molecularly confirmed cases reported worldwide per GeneReviews, though this substantially understates true prevalence.

**Inheritance pattern:** Autosomal recessive. Parents of an affected individual are obligate heterozygous carriers (typically asymptomatic or only mildly biochemically affected); siblings of an affected individual have a 25% chance of being affected, 50% chance of being an unaffected carrier, and 25% chance of being unaffected/non-carrier.

**Penetrance:** Biallelic pathogenic variants are considered highly (though not perfectly) penetrant for biochemical hypersterolemia; clinical penetrance (xanthomas, hematologic disease, atherosclerosis) is modulated by diet, producing variable expressivity even at fixed genotype.

**Expressivity:** Variable — intrafamilial phenotypic variability with identical genotypes is well documented and attributed chiefly to differing dietary sterol exposure (GeneReviews); some patients present solely with hematologic abnormalities without xanthomas/hypercholesterolemia.

**Genetic anticipation / germline mosaicism:** Not reported as a feature of this disorder (it is not a repeat-expansion disease).

**Founder effects:**
- ***ABCG8* p.Ser107Ter** — Hutterite population, carrier frequency ~8%.
- ***ABCG8* p.Gly574Arg** — Old Order Amish, carrier frequency ~4%.
- High prevalence also reported in inhabitants of **Kosrae (Micronesia)**, with a founder-variant carrier frequency cited around 13%, and in some South African and Finnish population groups (per multiple case-series/GeneReviews summaries).
- **Ancestry-related gene skew:** Northern European/white individuals more frequently carry *ABCG8* variants, while Chinese, Japanese, and Indian individuals more frequently carry *ABCG5* variants (GeneReviews; corroborated by multiple East/South Asian case series).

**Consanguinity:** As an autosomal recessive disorder, consanguineous unions elevate risk, consistent with reported case clusters in populations with high intra-community marriage rates (Amish, Hutterite, certain Middle Eastern/South Asian cohorts).

**Sex ratio / age distribution:** No strong sex predilection is reported in the literature reviewed; age at diagnosis spans neonatal/infantile through adult, with pediatric ascertainment (via xanthomas or incidental hypercholesterolemia/hematologic workup) predominating in published series.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Plasma phytosterol quantification** (sitosterol, campesterol, stigmasterol) via **gas chromatography, GC/MS, HPLC, or LC-MS/MS** — the essential first-line biochemical test, since **routine cholesterol panels do not distinguish plant sterols from cholesterol**. Untreated sitosterolemia patients show sitosterol concentrations 30- to 100-fold above normal (roughly 10–65 mg/dL vs. a normal reference of ~0.21 ± 0.7 mg/dL); >1 mg/dL is generally considered diagnostic (GeneReviews).
- Complete blood count and peripheral blood smear: macrothrombocytopenia (giant platelets with a vacuolated halo) and stomatocytic red cells are characteristic morphologic clues.
- Liver function tests (transaminases) as part of surveillance.
- Coronary artery calcium scoring/angiography in long-standing untreated cases to assess atherosclerotic burden.

**Genetic testing:**
- Multigene panel testing including *ABCG5*, *ABCG8*, and differential-diagnosis genes (e.g., *LDLR*, *APOB*, *PCSK9* for FH; *CYP27A1* for cerebrotendinous xanthomatosis; *ABCA1* for Tangier disease; *LCAT*) is the recommended first-tier approach when clinical suspicion is high.
- Exome/genome sequencing when the phenotype is atypical or sitosterolemia was not initially suspected.
- Sequence analysis (Sanger/NGS) detects >95% of pathogenic variants; no deletion/duplication (CNV) analysis is typically needed given no reported pathogenic CNVs.
- Diagnosis is formally established by the combination of **markedly elevated plasma plant sterols PLUS biallelic pathogenic/likely pathogenic *ABCG5*/*ABCG8* variants**.

**Diagnostic pitfalls:**
- False-positive mild elevation in formula-fed infants (immature transporter expression).
- Confounding from parenteral nutrition (plant-sterol-containing lipid emulsions).
- Heterozygous carriers may show mildly elevated sitosterol, complicating interpretation without genetic confirmation.

**Differential diagnosis (critical clinical distinction):**

| Disorder | Overlap with Sitosterolemia | Key Distinguishing Feature |
|---|---|---|
| Heterozygous FH | Childhood xanthomas, hypercholesterolemia | LDL-C typically >190 mg/dL in adults; no macrothrombocytopenia/hemolysis; responds well to statins |
| Homozygous FH | Severe xanthomatosis, marked hypercholesterolemia | LDL-C often >500 mg/dL; both parents typically hypercholesterolemic; statin-responsive (with PCSK9i/lomitapide adjuncts) |
| Cerebrotendinous xanthomatosis | Tendon xanthomas from childhood | Elevated cholestanol, chronic diarrhea, cataracts, progressive neurologic disease; caused by *CYP27A1* |
| Tangier disease | Stomatocytosis | Extreme HDL-C reduction (<1–2 mg/dL); caused by *ABCA1* |
| LCAT deficiency | Stomatocytosis | Extreme HDL-C reduction (<10 mg/dL), elevated VLDL/triglycerides, corneal opacities |

Misdiagnosis of sitosterolemia as FH (and vice versa) is a recurring, well-documented clinical pitfall with real patient-safety implications, since **statins — the standard FH therapy — are typically ineffective in sitosterolemia and the two conditions require different management** (multiple 2024–2026 case reports: PMID:38707657 "Two Cases of Sitosterolemia Falsely Diagnosed as Familial Hypercholesterolemia: Could Digging Deeper Have Avoided Harm?"; additional case reports of sitosterolemia misdiagnosed as Evans syndrome plus FH, and as homozygous FH).

**Screening:** No formal population-based newborn screening program for sitosterolemia was identified; case-finding is currently opportunistic (via pediatric hypercholesterolemia or hematology workups). Cascade family testing is recommended once a proband's variants are known; a familial hypercholesterolemia cascade-screening program has been used as a vehicle to also screen for *ABCG5*/*ABCG8* variants (Circ Genom Precis Med, AHA journals).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No population-level survival statistics (5-/10-year survival) specific to sitosterolemia were identified in a rare-disease registry format; the dominant mortality risk described in case literature is **premature cardiovascular death from accelerated atherosclerosis** (documented sudden cardiac death cases; atherosclerotic disease onset as early as age 5–33 years in untreated individuals per GeneReviews).
- **Morbidity:** Chronic hemolytic anemia, bleeding tendency from platelet dysfunction, arthritis/arthralgia, disfiguring xanthomas, and premature coronary artery disease constitute the principal morbidity burden.
- **Prognostic factors:** Age at diagnosis/treatment initiation, degree of dietary sterol restriction adherence, and pre-treatment atherosclerotic burden are the main prognostic modifiers described qualitatively in the literature; no formal validated prognostic scoring system specific to sitosterolemia was found.
- **Recovery potential:** With early diagnosis and sustained dietary/pharmacologic treatment, xanthomas regress, hematologic parameters normalize or improve substantially, and cardiovascular risk trajectory is markedly reduced — supporting a generally favorable prognosis when treated, contrasted with a poor, potentially lethal prognosis if the condition remains undiagnosed/untreated or is mismanaged (e.g., treated as FH with statins alone, which do not address the underlying sterol-absorption defect).

---

## 12. Treatment

**Pharmacotherapy (first line):**
- **Ezetimibe** (10 mg/day in adults) — a cholesterol/sterol absorption inhibitor acting on the intestinal **NPC1L1** transporter; FDA-approved specifically for sitosterolemia since **October 2002**, and is the current treatment of choice. It reduces gastrointestinal absorption of both cholesterol and plant sterols, lowering plasma phytosterol concentrations, and has also been reported to **increase platelet count and decrease mean platelet volume** (potentially reducing bleeding risk) and to improve VLDL/HDL subfraction distribution. Suggested MAXO/NCIT annotation: `treatment_term` NCIT:C15986 (Pharmacotherapy) + `therapeutic_agent` CHEBI (ezetimibe) — verify exact CHEBI ID via OAK.
- **Bile acid sequestrants** (cholestyramine 8–15 g/day, colestipol, colesevelam) as second-line/add-on therapy for incomplete ezetimibe response; typically reduce plant sterol levels by ~30% and can decrease xanthoma size. Combined dietary + pharmacologic treatment achieves an overall 10–50% reduction in plasma cholesterol and sitosterol concentrations.
- **Statins are generally ineffective** as monotherapy in sitosterolemia (a key point differentiating management from FH) since the primary defect is one of absorption/excretion, not endogenous cholesterol synthesis.
- **Contraindicated:** plant stanol-fortified products (campestanol, sitostanol margarines/spreads), which paradoxically worsen sterol accumulation despite being generally beneficial in ordinary hypercholesterolemia.

**Dietary intervention (foundational):** Restriction of plant sterol-rich foods (vegetable oils, margarine, nuts, seeds, avocados, chocolate) and shellfish. This is described as the foundational management approach and is typically combined with pharmacotherapy.

**Surgical/interventional:** **Partial ileal bypass surgery** has been used as a last-resort option in maximal-therapy failures, achieving >50% sterol reduction, but is reserved given its invasiveness.

**Supportive care:** Arthritis, anemia, thrombocytopenia, and splenomegaly are generally managed by treating the underlying sterol excess (which improves all these secondary manifestations) rather than by disease-specific symptomatic therapy.

**Emerging/experimental therapies:** No sitosterolemia-specific gene therapy, RNA-based therapy, or targeted biologic was identified as approved or in late-stage trials in this search. Broader cholesterol-lowering pipeline developments (oral PCSK9 inhibitors achieving ~65% LDL-C reduction, bempedoic acid, PPRH-based PCSK9 gene-suppression approaches) are advancing rapidly in general dyslipidemia/FH but were not identified as being specifically studied in or indicated for sitosterolemia; this represents a potential future-therapy knowledge gap worth flagging rather than asserting.

**Treatment outcomes:** A published case series with clinical, genetic, and therapeutic data reported favorable outcomes with varying combinations of dietary treatment and ezetimibe across 55 children and 5 adults with sitosterolemia (cited via search aggregation; original primary-literature citation should be independently verified/fetched before KB use — likely Tada et al. or a related Japanese cohort study, to be confirmed with `just fetch-reference`).

**Pregnancy:** No adequate controlled studies of ezetimibe in pregnancy exist; use only if benefit outweighs fetal risk, with close monitoring (e.g., via MotherToBaby) recommended (GeneReviews).

**Suggested MAXO/NCIT terms:** MAXO:0000088 (dietary intervention) for the sterol-restricted diet; NCIT:C15986 (Pharmacotherapy) + therapeutic_agent for ezetimibe and bile acid sequestrants; MAXO:0000004/NCIT:C15329 (surgical procedure) for partial ileal bypass.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (this is a genetic disorder present from conception), but dietary avoidance of plant sterols/stanols and shellfish from infancy in genetically confirmed individuals functions as primary prevention of the clinical phenotype (xanthomas, atherosclerosis, hematologic disease) even though it cannot prevent the genotype itself.
- **Secondary prevention:** Early biochemical/genetic diagnosis in at-risk families (siblings of an index case, or children/relatives in high-founder-frequency populations) enables treatment before significant atherosclerotic or hematologic morbidity accrues. Cascade genetic testing following identification of a proband's variants is recommended.
- **Tertiary prevention:** Ongoing surveillance (annual plasma sterol panels, CBC/platelet counts, liver enzymes, xanthoma assessment, and periodic non-invasive cardiac imaging in previously untreated/long-standing cases) aims to detect and mitigate complications (progressive atherosclerosis, worsening cytopenias) in individuals with established disease.
- **Genetic counseling:** Recommended for families of affected individuals — informing them of the 25%/50%/25% recurrence risk pattern for future pregnancies, discussing prenatal/preimplantation genetic testing options once family-specific variants are known (GeneReviews notes differing family perspectives on utilizing this option), and offering carrier testing in high-prevalence populations (e.g., Hutterite, Amish communities) for founder variants.
- **Screening programs:** No dedicated national/international sitosterolemia newborn screening program was identified; screening currently relies on clinical suspicion (pediatric hypercholesterolemia, unexplained hemolytic anemia/macrothrombocytopenia) triggering targeted biochemical/genetic testing, and FH cascade-screening programs opportunistically capturing sitosterolemia cases.
- **Public health/environmental interventions:** Not applicable in the traditional sanitation/vector-control sense; the relevant "environmental" intervention is individualized dietary counseling.

---

## 14. Other Species / Natural Disease

- No naturally occurring veterinary/companion-animal sitosterolemia analog was identified in this search (no OMIA entry surfaced). This disease is primarily studied via engineered rodent models rather than naturally occurring animal disease.
- **Orthologous genes:** Mouse *Abcg5*/*Abcg8* (NCBI Gene) are the direct orthologs used in essentially all animal modeling.
- **Comparative biology:** The ABCG5/ABCG8 heterodimer and its sterol-selectivity mechanism are evolutionarily conserved across mammals, underpinning the validity of mouse knockout models for mechanistic study (see §15).

---

## 15. Model Organisms

**Genetic models:**
- ***Abcg5⁻/⁻*, *Abcg8⁻/⁻*, and combined *Abcg5/Abcg8⁻/⁻* knockout mice** are the principal disease models.
  - Yu et al., *PNAS* 2002 ("Disruption of Abcg5 and Abcg8 in mice reveals their crucial role in biliary cholesterol secretion") established that these transporters are essential for biliary cholesterol/sterol secretion.
  - A related model paper ("A mouse model of sitosterolemia: absence of Abcg8/sterolin-2 results in failure to secrete biliary cholesterol," PMC394351) confirmed loss of biliary cholesterol secretion in *Abcg8*-null mice.
  - Under standard chow, *Abcg5/Abcg8*-null mice show no overt gross phenotype but have **markedly increased plasma phytosterol concentrations** and very low biliary cholesterol content compared to wild-type.
  - **Phytosterol Feeding Causes Toxicity in ABCG5/G8 Knockout Mice** (PMID:23380580, *Am J Pathol* 2013): a high-phytosterol diet is well tolerated by wild-type mice but produces severe toxicity (premature death, hepatic abnormalities, severe cardiac lesions) in knockout mice — directly modeling the gene-diet interaction central to human disease and supporting dietary sterol restriction as mechanistically causal, not merely correlative, in disease severity.
  - **Platelet hyperreactivity model:** *Blood* 2013 study using the murine sitosterolemia model demonstrated that plant sterol incorporation into the platelet membrane drives platelet hyperreactivity, αIIbβ3 integrin internalization, and filamin A degradation, mechanistically explaining the human macrothrombocytopenia/bleeding phenotype.

**Phenotype recapitulation:** The mouse models successfully recapitulate the core biochemical lesion (hypersterolemia, defective biliary sterol secretion) and, under phytosterol challenge, the cardiac/hepatic toxicity and platelet abnormalities seen in humans. They do not spontaneously recapitulate human xanthoma formation or overt atherosclerotic plaque under standard chow without additional dietary/genetic sensitization (e.g., combination with atherogenic diets or apoE-null backgrounds would likely be needed — not confirmed in this search and should be flagged as a `HUMAN_MODEL_MISMATCH`-type consideration if used in KB curation).

**Model limitations:** Baseline (non-phytosterol-challenged) knockout mice lack an overt spontaneous phenotype, meaning the "natural" mouse phenotype under-represents human disease severity unless a high-phytosterol diet is imposed experimentally — an important translational caveat for any curated `mechanistic_hypotheses`/evidence_source annotation (evidence_source: MODEL_ORGANISM should be used, and the diet-dependency explicitly noted).

**Applications:** These models have been used to establish the causal transporter mechanism, define the gene-diet interaction, and dissect the platelet/hematologic mechanism — but not, per this search, to test emerging pharmacologic candidates beyond ezetimibe-class NPC1L1 inhibition.

**Resources:** MGI (Mouse Genome Informatics) for *Abcg5*/*Abcg8* allele records; no zebrafish, *Drosophila*, or *C. elegans* models were identified in this search.

---

## Key Evidence Gaps Identified (for KB `discussions`/`KNOWLEDGE_GAP` consideration)

1. **Prevalence estimates are inconsistent** across sources (ranging over several orders of magnitude) and systematically confounded by under-diagnosis — a `KNOWLEDGE_GAP` rather than a settled `Prevalence` figure.
2. **MONDO ID discrepancy:** the research-template-suggested MONDO:0008863 vs. the MONDO:0020748 surfaced by search should be reconciled with a direct OAK lookup before curation.
3. **Genotype-phenotype correlation is explicitly absent** (per GeneReviews) — variable expressivity is attributed to diet, not genotype, which is itself a citable, curatable claim.
4. **Monoallelic/heterozygous carrier phenotype** is an emerging, not yet fully established, area (2026 Frontiers review) — a candidate for a `MECHANISTIC_HYPOTHESIS`-flagged definition/claim rather than an `ESTABLISHED_CRITERIA` one.
5. **Mouse model baseline phenotype requires phytosterol dietary challenge** to manifest overt pathology — any evidence item citing the knockout mouse model should specify this diet-dependency to avoid overstating spontaneous phenotype recapitulation (a `HUMAN_MODEL_MISMATCH` candidate).
6. **No dedicated newborn screening or formal prognostic/survival registry data** were located — treatment-outcome quotes (e.g., the 55-children/5-adults cohort) should be traced to primary literature and PMID-confirmed via `just fetch-reference` before use, since this report surfaced it only via secondary aggregation.

---

## Sources

- [GeneReviews: Sitosterolemia (NBK131810)](https://www.ncbi.nlm.nih.gov/books/NBK131810/)
- [OMIM #210250 — Sitosterolemia 1 (STSL1)](https://omim.org/entry/210250)
- [OMIM #618666 — Sitosterolemia 2 (STSL2)](https://www.omim.org/entry/618666)
- [OMIM *605460 — ABCG8](https://omim.org/entry/605460) / ABCG5 *605459
- [Frontiers in Nutrition 2026 — Molecular genetic basis and clinical heterogeneity of sitosterolemia](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2026.1857512/full)
- [Sitosterolemia: Twenty Years of Discovery of the Function of ABCG5/ABCG8 (PMC7961684)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7961684/)
- [Transmembrane Polar Relay Drives the Allosteric Regulation for ABCG5/G8 Sterol Transporter (PMC7699580)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7699580/)
- [Specific macrothrombocytopenia/hemolytic anemia associated with sitosterolemia — PubMed PMID:24166850](https://pubmed.ncbi.nlm.nih.gov/24166850/)
- [Sitosterolemia Due to a New Combination of ABCG8 Variants Presenting as Hemolytic Anemia and Macrothrombocytopenia (PMC12508803)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12508803/)
- [Clinical characteristics of sitosterolemic children with xanthomas as the first manifestation (PMC9563796)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9563796/)
- [Child with sitosterolemia initially presenting with hemolytic anemia and thrombocytopenia (PMC10951126)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10951126/)
- [Two Cases of Sitosterolemia Falsely Diagnosed as Familial Hypercholesterolemia — PMID:38707657](https://pubmed.ncbi.nlm.nih.gov/38707657/)
- [High prevalence of increased sitosterol levels in hypercholesterolemic children suggest underestimation of sitosterolemia incidence (PMC7449458)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7449458/)
- [Update on Sitosterolemia and Atherosclerosis — Current Atherosclerosis Reports 2023](https://link.springer.com/article/10.1007/s11883-023-01092-4)
- [Platelet hyperreactivity explains the bleeding abnormality and macrothrombocytopenia in a murine model of sitosterolemia — Blood 122(15):2732](https://ashpublications.org/blood/article/122/15/2732/31895/Platelet-hyperreactivity-explains-the-bleeding)
- [Platelet proteomic profiling in sitosterolemia — Blood Advances 8(10):2466](https://ashpublications.org/bloodadvances/article/8/10/2466/515385/Platelet-proteomic-profiling-in-sitosterolemia)
- [Phytosterol Feeding Causes Toxicity in ABCG5/G8 Knockout Mice — PubMed PMID:23380580](https://pubmed.ncbi.nlm.nih.gov/23380580/)
- [A mouse model of sitosterolemia: absence of Abcg8/sterolin-2 results in failure to secrete biliary cholesterol (PMC394351)](https://ncbi.nlm.nih.gov/pmc/articles/PMC394351)
- [Disruption of Abcg5 and Abcg8 in mice reveals their crucial role in biliary cholesterol secretion — PNAS](https://www.pnas.org/doi/10.1073/pnas.252582399)
- [Screening of ABCG5 and ABCG8 Genes for Sitosterolemia in a Familial Hypercholesterolemia Cascade Screening Program — Circ Genom Precis Med](https://www.ahajournals.org/doi/10.1161/CIRCGEN.121.003390)
- [Sitosterolemia — NORD (rare disease overview)](https://rarediseases.org/rare-diseases/sitosterolemia/)
- [Sitosterolemia — MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/sitosterolemia/)
- [Sitosterolemia (Phytosterolemia): Background, Pathophysiology, Etiology — Medscape](https://emedicine.medscape.com/article/948892-overview)
- [Sitosterolemia (Phytosterolemia) Treatment & Management — Medscape](https://emedicine.medscape.com/article/948892-treatment)