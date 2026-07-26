---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-26T13:22:37.604357'
end_time: '2026-07-26T13:28:46.554241'
duration_seconds: 368.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Zellweger Spectrum Disorders
  mondo_id: MONDO:0019609
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
  web_search_requests: 24
  num_turns: 30
  total_cost_usd: 2.0457653999999996
  session_id: f9a4f8a6-559e-5875-b202-2cc5a4e70210
  stop_reason: end_turn
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Zellweger Spectrum Disorders
- **MONDO ID:** MONDO:0019609 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Zellweger Spectrum Disorders** covering all of the
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

# Zellweger Spectrum Disorder (ZSD): Comprehensive Research Report

## 1. Disease Information

**Overview.** Zellweger spectrum disorder (ZSD) is the most common and clinically most severe subgroup of the peroxisome biogenesis disorders (PBDs), a group of autosomal recessive conditions caused by failure to assemble functional peroxisomes. ZSD represents a single biochemical and clinical continuum — historically split into three "distinct" diagnoses (Zellweger syndrome [most severe], neonatal adrenoleukodystrophy [NALD, intermediate], and infantile Refsum disease [IRD, mildest]) that are now recognized as points along one spectrum defined by residual peroxin function ([GeneReviews, NBK1448](https://www.ncbi.nlm.nih.gov/books/NBK1448/); [Klouwer et al. 2015, PMID:26627182](https://pmc.ncbi.nlm.nih.gov/articles/PMC4666198/)). As the GeneReviews summary states, "Zellweger spectrum disorder... spans a phenotypic continuum ranging from a severe neonatal-onset form... to a milder, later-onset form."

**Key identifiers:**
- **MONDO:** MONDO:0013932 (Zellweger syndrome; related MONDO IDs exist per causal gene, e.g., PBD1A, PBD1B)
- **OMIM (phenotype series/individual entries — see §4 below for the full gene-keyed list):** PS214100 (Peroxisome biogenesis disorder, Zellweger syndrome spectrum)
- **Orphanet:** ORPHA:912 (Zellweger syndrome), ORPHA:79189 (Peroxisome biogenesis disorder), with related entries for NALD (ORPHA:44) and IRD
- **ICD-10-CM:** E71.518 (Other disorders of peroxisome biogenesis); Zellweger syndrome is also sometimes captured under Q87.8 (other specified congenital malformation syndromes)
- **ICD-11:** 5C57.0
- **MeSH:** D015211 (Zellweger Syndrome); C536664 (Peroxisome biogenesis disorders)

**Synonyms:** Zellweger syndrome; cerebrohepatorenal syndrome; peroxisome biogenesis disorder–Zellweger syndrome spectrum (PBD-ZSS); neonatal adrenoleukodystrophy (NALD); infantile Refsum disease (IRD); peroxisomal 3-oxoacyl-CoA thiolase deficiency (historically confused with, but distinct from, ZSD).

**Evidence basis of curated information:** The literature is a mixture of aggregated disease-level resources (GeneReviews, Orphanet, OMIM, NORD) and primary clinical cohort/registry studies (natural history studies, caregiver surveys, medical chart reviews) — i.e., largely **aggregated, disease-level** characterizations supplemented by **individual-patient cohort data** (e.g., the NIH/Kennedy Krinstitute Longitudinal Natural History Study, [NCT01668186](https://clinicaltrials.gov/study/NCT01668186); the caregiver cross-sectional study, [PMID:33335840](https://www.sciencedirect.com/science/article/pii/S2214426920301403)).

---

## 2. Etiology

**Disease causal factors — genetic, monogenic.** ZSD is caused exclusively by biallelic pathogenic variants in one of **13 known PEX genes**, which encode "peroxins" required for peroxisomal membrane biogenesis and/or peroxisomal matrix protein import. There is no known environmental, infectious, or purely mechanistic (non-genetic) cause.

**Genetic risk factors (causal genes, ranked by mutation frequency in ZSD cohorts, per GeneReviews):**

| Gene | HGNC symbol | Approx. % of ZSD cases | OMIM gene | Function |
|---|---|---|---|---|
| PEX1 | PEX1 | 60.5% | *602136 | AAA-ATPase, PEX5/PEX7 receptor recycling (with PEX6) |
| PEX6 | PEX6 | 14.5% | *601498 | AAA-ATPase, partner of PEX1 |
| PEX12 | PEX12 | 7.6% | RING-finger peroxin, matrix import | |
| PEX26 | PEX26 | 4.2% | Membrane peroxin, recruits PEX1/PEX6 to peroxisome | |
| PEX10 | PEX10 | 3.4% | RING-finger peroxin, matrix import | |
| PEX2 | PEX2 | 3.1% | RING-finger peroxin, matrix import | |
| PEX5 | PEX5 | 2.0% | PTS1 receptor | |
| PEX13 | PEX13 | 1.5% | Docking-complex peroxin | |
| PEX16 | PEX16 | 1.1% | Membrane biogenesis peroxin | |
| PEX3, PEX19, PEX14, PEX11B | — | <1% each | Membrane biogenesis (PEX3/19/16), division (PEX11B), docking (PEX14) | |

Source: [GeneReviews NBK1448](https://www.ncbi.nlm.nih.gov/books/NBK1448/).

Corresponding OMIM phenotype entries include PBD1A/PBD1B (PEX1, #214100/*601539), PBD2A (PEX5, #214110), PBD3A (PEX12, #614859), PBD4A (PEX6, #614862), PBD5A (PEX2, #614866), PBD6A (PEX10, #614870), PBD7A (PEX26, #614872), PBD13A (PEX13, #614887 — approximate), among others ([OMIM.org](https://omim.org/entry/214100)).

**Risk variant example — PEX1 p.Gly843Asp (c.2528G>A, rs61750420):** This is the single most common ZSD-causing allele in patient cohorts (allele frequency ~0.43 among PEX1-mutant alleles per Steinberg et al. 2006), yet it is rare in the general population (gnomAD/ClinVar general-population allele frequency ≈0.00033, i.e., ~1/3000 chromosomes) ([ClinVar RCV000007946](https://www.ncbi.nlm.nih.gov/clinvar/RCV000007946/)). It retains ~15% of wild-type PEX1 activity in patient fibroblasts, explaining its association with the mildest end of the spectrum. Homozygosity for this hypomorphic allele produces a **mild** phenotype; homozygosity for the null frameshift PEX1 p.Ile700Tyrfs*42 (c.2097_2098insT) produces a **severe** phenotype; compound heterozygosity for the two produces an **intermediate** phenotype — a clean genotype–severity correlation ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1448/); [Mild Zellweger syndrome PEX1 variants, PMC6968987](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6968987/)).

**Founder effects (population-specific risk):**
- French-Canadian (Saguenay–Lac-Saint-Jean, Quebec): a PEX6 founder mutation drives an incidence of ~1/12,000 births, one of the highest in the world ([PMC3483250](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3483250/)).
- PEX6 founder variant also reported causing Zellweger syndrome via possible founder effect in Mixteco (Mexican indigenous) neonates ([PMC10573658](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10573658/)).
- Japan's markedly lower incidence (1/500,000) is attributed to the **absence** of the common European PEX1 founder variants (p.Ile700Tyrfs*42 and p.Gly843Asp).
- Saudi Arabia and other high-consanguinity populations report increased ZSD prevalence attributable to consanguineous unions rather than a single founder allele.

**Environmental/lifestyle risk factors:** None established — ZSD is a fully penetrant monogenic disease; there is no reported gene–environment interaction modulating risk of disease occurrence. (Environmental/nutritional factors, e.g., DHA status, are relevant to secondary disease *severity/management*, not causation — see §12.)

**Protective factors:** None known at the genetic-modifier level beyond residual-activity ("hypomorphic") missense alleles, which are protective **relative to null alleles** in a dose-dependent way but do not prevent disease. No environmental protective exposure has been described.

**Gene–environment interactions:** Not applicable in the causal sense; however, catabolic stress (intercurrent illness, fasting) can unmask or worsen adrenal insufficiency and hepatic decompensation in patients with residual peroxisomal function, an indirect gene-modulated environmental interaction relevant to clinical management.

---

## 3. Phenotypes

ZSD is multisystemic. Below, phenotypes are grouped by type, with suggested HPO terms, and typical onset/severity/frequency data drawn from the largest systematic sources: the Klouwer 2015 review ([PMID:26627182](https://pmc.ncbi.nlm.nih.gov/articles/PMC4666198/)), the 2022 scoping review/meta-analysis/medical chart review by **Berendse et al., "Characterization of Severity in Zellweger Spectrum Disorder by Clinical Findings"** ([PMID:35741019](https://www.mdpi.com/2073-4409/11/12/1891)), and the caregiver cross-sectional study ([Bose et al. 2020, PMID:33335840](https://www.sciencedirect.com/science/article/pii/S2214426920301403)).

### Neurological
- **Hypotonia** (HP:0001252) — near-universal in severe/neonatal presentation; present in ~72% of "intermediate" category patients in the natural-history cohort.
- **Seizures** (HP:0001250) — 100% in severe category (n=23), 41.3% in intermediate (n=63), 16.3% in mild (n=49) — a graded, severity-defining feature.
- **Abnormal EEG** (HP:0002353) — 100% in severe category (n=17 assessed).
- **Global developmental delay** (HP:0001263) — 97.5% in intermediate category (n=40); present in virtually all severe patients; may be absent or mild in the mildest phenotype.
- **Neuronal migration defects** (e.g., polymicrogyria, HP:0002126; pachygyria HP:0001302) — characteristic of the severe/neonatal form, visible on brain MRI.
- **Progressive leukodystrophy/demyelination** (HP:0002352) — reported in a subset, more typical of the "NALD" intermediate presentation, progressive over childhood.
- **Peripheral neuropathy** (HP:0009830) — reported in milder, longer-surviving patients.
- **Ataxia** (HP:0001251) — in milder/longer-surviving phenotypes.

### Craniofacial / Dysmorphic
- **Distinctive facies** (HP:0001999) — flat facies, high forehead, large fontanelles, epicanthal folds — most prominent in the severe neonatal form.

### Hepatic
- **Neonatal cholestasis/jaundice** (HP:0200034 / HP:0001080).
- **Hepatomegaly** (HP:0002240).
- **Abnormal liver function** (HP:0001410) — 92.9% in intermediate category (n=56).
- **Vitamin-K-responsive coagulopathy** — from fat malabsorption/cholestasis.
- **Progression to fibrosis, portal hypertension, esophageal varices**; hepatocellular carcinoma reported in some surviving adults.

### Endocrine
- **Adrenocortical insufficiency** (HP:0000846) — reported by 45% combined prevalence of caregivers (48% living, 40% deceased) in the caregiver survey; 54.2% in the intermediate natural-history category. Often subclinical/evolving and probably underdiagnosed, especially in milder/adult-surviving patients.

### Ocular
- **Progressive retinal dystrophy/retinopathy** (HP:0000556 retinal dystrophy; HP:0000512 nystagmus is often an early sign) — "nearly all patients develop a progressive retinopathy leading to blindness"; 89.1% vision loss in intermediate category (n=55).
- **Cataracts** (HP:0000518) — may be congenital, especially severe form.
- **Glaucoma** (HP:0000501).

### Auditory
- **Sensorineural hearing loss** (HP:0000407) — described as "almost always present" in childhood-onset patients; a core, near-universal feature across the spectrum, worsening with age.

### Skeletal
- **Chondrodysplasia punctata** (stippled epiphyses of patellae and long bones; HP:0002694) — characteristic of the severe neonatal form.
- **Osteopenia/low bone density** (HP:0000939).
- **Amelogenesis imperfecta** (enamel hypoplasia of secondary teeth; HP:0000705).

### Renal
- **Renal cortical cysts** (HP:0000107) — 79% in the severe natural-history category (n=19); a common, often congenital finding.
- **Nephrocalcinosis/urolithiasis** from elevated urinary oxalate (HP:0000121 / HP:0000787).

### Cardiac
- **Cardiac structural abnormalities** — reported in 81.3% of a small severe-category cohort (n=16) in the meta-analysis (e.g., septal defects); less systematically characterized than other organ systems.

### Gastrointestinal/Growth
- **Feeding difficulties/failure to thrive** (HP:0011968/HP:0001508) — 71.9% in intermediate category; **0%** (none) in the mild category cohort — a strongly discriminating feature between severity tiers.

### Functional/Behavioral (milder end of spectrum)
- **Independent ambulation** achieved in 87.8% of mild-category patients; full-sentence speech in 71.7%.

**Phenotype characteristics summary (per severity tier, from the Berendse et al. meta-analysis, PMID:35741019):**
- **Severe:** neonatal onset, near-uniform seizures/abnormal EEG, high renal cyst prevalence, mortality before age 2 in 95.7% (n=23).
- **Intermediate:** childhood onset, high rates of developmental delay (97.5%), vision loss (89.1%), abnormal liver function (92.9%), feeding difficulty (71.9%), adrenal insufficiency (54.2%), lower but still substantial seizure rate (41.3%).
- **Mild:** later childhood/adolescent/adult recognition, seizures in only 16.3%, no feeding difficulties, majority ambulatory and verbal, but progressive sensory (vision/hearing) impairment remains prominent even here.
- Survival differed significantly across the three severity categories by log-rank test (p<0.001).

**Quality-of-life impact:** Combined sensory (vision + hearing) loss plus developmental delay produces major functional impact even in "mild" survivors; caregiver-reported burden is high across the spectrum ([Bose et al. 2020, PMID:33335840](https://www.sciencedirect.com/science/article/pii/S2214426920301403)). No ZSD-specific EQ-5D/SF-36 dataset was identified in this search; QOL data are largely qualitative/caregiver-reported rather than standardized instrument-based.

---

## 4. Genetic/Molecular Information

**Causal genes:** The 13 PEX genes listed in §2, all acting via loss-of-function (biallelic) mechanisms. HGNC symbols: PEX1, PEX2, PEX3, PEX5, PEX6, PEX7 (causes the biochemically related but clinically distinct RCDP1, not classic ZSD — see below), PEX10, PEX11B, PEX12, PEX13, PEX14, PEX16, PEX19, PEX26.

**Variant classification/type:**
- **Null/loss-of-function variants** (large deletions, nonsense, frameshift) — associated with **severe** phenotype (complete absence of peroxin function).
- **Missense/hypomorphic variants retaining residual function** (e.g., PEX1 p.Gly843Asp) — associated with **milder** phenotype.
- Compound heterozygosity of a null + hypomorphic allele → **intermediate** phenotype.
- Clinical severity correlates with **overall genotype/residual peroxin activity rather than which specific PEX gene** is mutated — i.e., genotype (allele combination), not locus identity, is the primary determinant.
- A notable genetic exception to strict autosomal-recessive inheritance: the PEX6 variant p.Arg860Trp can cause disease in a functionally **heterozygous** state via allelic expression imbalance (unusual dominant-like mechanism reported in GeneReviews).

**Allele frequency in population databases:**
- PEX1 p.Gly843Asp (rs61750420): gnomAD/general-population allele frequency ≈0.00033 (≈1/3000 alleles); much higher (0.43) among PEX1-mutant disease alleles specifically ([ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000007946/)).
- A 2025 population-genetics modeling study estimated **PEX1-mediated ZSD births and population prevalence** using allele-frequency data (see [Genetics in Medicine Open, 2025](https://www.gimopen.org/article/S2949-7744(25)01470-0/fulltext)) — useful for refining historical incidence estimates that likely undercount mild/undiagnosed cases.

**Somatic vs. germline:** ZSD is exclusively germline (constitutional) — no somatic/mosaic ZSD-associated malignancy mechanism has been described (distinct from unrelated adult hepatocellular carcinoma occasionally reported as a complication in surviving ZSD patients, which is a disease *complication*, not somatic PEX pathogenesis).

**Functional consequences (molecular mechanism of PEX1/PEX6, illustrative):** PEX1 and PEX6 are AAA-ATPases that assemble into a heterohexameric complex mediating **ATP-dependent extraction and recycling of the ubiquitinated PTS1 receptor PEX5** (and PEX7, the PTS2 receptor) from the peroxisomal membrane back to the cytosol. Loss of PEX1 function traps ubiquitinated PEX5 at the membrane, blocking further rounds of matrix protein import, causing failure to form functional peroxisomes, increased pexophagy, and formation of aberrant "ghost peroxisomes" (membrane remnants devoid of matrix enzymes) ([Frontiers/PMC12626956 zebrafish Pex1 model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12626956/)).

**Modifier genes:** No validated modifier genes beyond the allelic-series (residual-activity) effect described above; ATAD1 has recently been proposed as a candidate modulator of mitochondrial/peroxisomal function in ZSD models (2025 preprint, biorxiv) but is not an established clinical modifier.

**Epigenetic information:** No disease-specific DNA methylation/histone-modification signature for ZSD was identified in this search; this remains an unexplored area relative to other rare monogenic diseases.

**Chromosomal abnormalities:** ZSD is a single-gene (biallelic small-variant) disorder; no recurrent large-scale chromosomal rearrangement (aneuploidy/translocation) mechanism is implicated. Deletion/duplication (CNV) analysis of individual PEX genes is part of standard molecular diagnostic algorithms when sequence analysis alone is uninformative (GeneReviews).

---

## 5. Environmental Information

ZSD has no infectious, toxin, or lifestyle etiology — it is fully genetic. The only "environmental" considerations relevant to the disease are:
- **Nutritional/metabolic stress** (fasting, intercurrent illness) that can precipitate acute decompensation via unmasking adrenal insufficiency or worsening hepatic dysfunction in patients with residual peroxisomal function.
- **Dietary DHA (docosahexaenoic acid) status**, addressed therapeutically (§12) because peroxisomal dysfunction secondarily depletes endogenous DHA synthesis.
No infectious agent is implicated in disease causation or exacerbation.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** Biallelic loss-of-function variant in a PEX gene (peroxin) → failure of peroxisomal membrane biogenesis (PEX3/PEX16/PEX19) **or** failure of the PTS1/PTS2 matrix-protein import machinery (PEX5/PEX7 receptors; PEX13/PEX14 docking complex; PEX2/PEX10/PEX12 RING-peroxin ubiquitination machinery; PEX1/PEX6/PEX26 receptor-recycling AAA-ATPase complex) ([GO:0016561 protein import into peroxisome matrix, translocation](https://amigo.geneontology.org/amigo/term/GO:0016561); [GO:0016562 receptor recycling](https://amigo.geneontology.org/amigo/term/GO:0016562); [Reactome R-HSA-9033241 Peroxisomal protein import](https://reactome.org/content/detail/R-HSA-9033241)).
2. **Cellular consequence:** Absence of functional (import-competent) peroxisomes, or markedly reduced peroxisome number/size ("peroxisomal ghosts") → global loss of peroxisomal enzymatic function (>50 enzymes normally housed in the organelle).
3. **Biochemical consequence (multiple parallel metabolic failures):**
   - Failure of **peroxisomal β-oxidation** of very-long-chain fatty acids (VLCFA) → VLCFA accumulation in plasma and tissues (the primary diagnostic biomarker).
   - Failure of **plasmalogen (ether phospholipid) biosynthesis** (dihydroxyacetone phosphate acyltransferase / alkyl-DHAP synthase are peroxisomal, PTS2-imported enzymes) → plasmalogen deficiency in erythrocyte membranes and, critically, in **myelin**, since peroxisomes are the sole site of plasmalogen synthesis.
   - Failure of **bile acid side-chain oxidation** → accumulation of toxic C27 bile acid intermediates (di- and trihydroxycholestanoic acid, DHCA/THCA) → hepatotoxicity/cholestasis.
   - Failure of **phytanic/pristanic acid α/β-oxidation** → accumulation of branched-chain fatty acids.
   - Impaired **docosahexaenoic acid (DHA)** synthesis (a partially peroxisomal pathway) → DHA deficiency, particularly relevant to retina/brain membrane composition.
   - Elevated **pipecolic acid**.
4. **Cellular/tissue consequence:**
   - Plasmalogen/myelin deficiency + VLCFA-driven membrane lipid abnormality → impaired **oligodendrocyte** myelination and neuronal migration defects (**GO:0007406 negative regulation of neuroblast proliferation**-type processes are affected during migration; cell types: **CL:0000128 oligodendrocyte**, **CL:0000031 neuroblast/radial glia** during migration).
   - Hepatotoxic bile-acid intermediates + VLCFA accumulation → **hepatocyte (CL:0000182)** injury, cholestasis, and progressive fibrosis (feeds a fibrotic-response-type mechanism in the liver).
   - VLCFA incorporation into complex membrane lipids of multiple cell types (retinal photoreceptors [**CL:0000210**], cochlear hair cells [**CL:0000202**], adrenal cortical cells [**CL:1000477 / CL:0002499**], renal tubular/podocyte-adjacent epithelium contributing to cyst formation) → activation of inflammatory signaling, oxidative stress, and cell dysfunction/death in each of these tissues.
   - **Mitochondrial dysfunction**: recent work shows mislocalized peroxins insert into mitochondria and disturb cristae structure directly, and mitochondrial dysfunction/oxidative stress/excess ROS are increasingly recognized as a **secondary, convergent mechanism** contributing to neurotoxicity alongside the primary lipid-metabolism defects ([EMBO Reports, "The biochemical basis of mitochondrial dysfunction in ZSD"](https://www.embopress.org/doi/full/10.15252/embr.202051991); [PMC10652488, MAPK activation & impaired autophagy in ZSD/X-ALD](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10652488/)).
   - Impaired **autophagy** and abnormal **MAPK pathway activation** have been reported in patient-derived cells, suggesting broader proteostasis/signaling disruption beyond lipid metabolism alone.
5. **Organism-level manifestation:** The combined effect of (a) neuronal migration/myelination failure, (b) hepatocellular injury, (c) adrenocortical dysfunction, (d) sensory (retinal/cochlear) degeneration, and (e) skeletal mineralization defects (chondrodysplasia punctata) produces the multisystem clinical phenotype described in §3, with severity determined by the degree of residual peroxin/peroxisome function.

**Suggested GO terms (biological process):** GO:0016561 (protein import into peroxisome matrix, translocation), GO:0016562 (receptor recycling), GO:0044721 (substrate release), GO:0006635 (fatty acid beta-oxidation), GO:0006654 (phosphatidic acid biosynthetic process, upstream of plasmalogen synthesis), GO:0042760 (very-long-chain fatty acid catabolic process), GO:0007041 (lysosomal transport — for the secondary autophagy defect), GO:0006979 (response to oxidative stress).

**Suggested CL terms (cell types):** CL:0000182 (hepatocyte), CL:0000128 (oligodendrocyte), CL:0000210 (photoreceptor cell), CL:0000202 (auditory hair cell), CL:0002499 (adrenal cortex cell) or CL:1000477, CL:0000646 (basal cell / renal tubular epithelial cell as relevant to cyst formation), CL:0000138 (chondrocyte, relevant to chondrodysplasia punctata).

**Suggested UBERON terms (see §7).**

**Molecular profiling / omics:** Lipidomic (plasmalogen/VLCFA) and to a lesser extent transcriptomic/proteomic profiling of patient fibroblasts and animal-model tissues have been used to characterize disease mechanism (e.g., mouse retinal pigment epithelium lipidomics in the PEX1-p.Gly844Asp model, [biorxiv 2024](https://www.biorxiv.org/content/10.1101/2024.09.05.611330.full.pdf)); no large-scale human single-cell or spatial transcriptomic ZSD atlas was identified in this search — this remains a data gap relative to other rare disease areas.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** liver (UBERON:0002107), brain/CNS (UBERON:0000955), adrenal gland (UBERON:0002369), eye/retina (UBERON:0000966 / UBERON:0000970), inner ear/cochlea (UBERON:0001846), kidney (UBERON:0002113), skeleton — long bones and patella (UBERON:0002438 femur; UBERON:0011595 patella).
- **Secondary/complications:** cardiovascular system (structural cardiac anomalies), teeth (enamel — amelogenesis imperfecta), skin (occasionally), gastrointestinal tract (feeding dysfunction as a downstream neuro-motor consequence).
- **Body systems involved:** nervous, hepatobiliary, endocrine, sensory (visual, auditory), skeletal, renal, and — to a lesser, secondary extent — cardiovascular.

**Tissue and cell level:**
- Hepatocytes (CL:0000182) — cholestasis, steatosis, fibrosis.
- Oligodendrocytes/myelin (CL:0000128) — leukodystrophy in the intermediate/progressive forms.
- Neurons undergoing migration (radial glia-guided cortical neuroblasts) — neuronal migration defects (polymicrogyria/pachygyria).
- Retinal photoreceptors and RPE (CL:0000210; CL:0002586 retinal pigment epithelial cell) — progressive retinopathy.
- Cochlear hair cells (CL:0000202) — sensorineural hearing loss.
- Adrenal cortical cells (zona fasciculata/reticularis) — adrenal insufficiency.
- Chondrocytes of the epiphyseal growth plate — chondrodysplasia punctata.
- Renal tubular epithelium — cortical microcysts.

**Subcellular level (GO Cellular Component):**
- **Peroxisome** (GO:0005777) and **peroxisomal membrane** (GO:0005778) — the primary organelle defect.
- **Peroxisomal matrix** (GO:0005782).
- Secondary **mitochondrion** (GO:0005739) involvement via peroxin mislocalization and cristae disruption.
- **Endoplasmic reticulum** contribution to peroxisomal membrane biogenesis (pre-peroxisomal vesicle origin), relevant to PEX3/PEX16/PEX19 mechanism.

**Localization/laterality:** Disease manifestations are bilateral/symmetric and systemic — no lateralization pattern is described (consistent with a metabolic, non-focal-lesion disease process).

---

## 8. Temporal Development

**Onset:**
- **Severe (classic "Zellweger syndrome"):** congenital/neonatal onset — symptomatic at birth or within the first days of life.
- **Intermediate ("NALD"):** infantile/early childhood onset.
- **Mild ("IRD" and beyond):** later childhood, adolescent, or even adult recognition — onset pattern is insidious, often first suspected because of progressive sensory (vision/hearing) decline rather than an acute neonatal presentation.

**Progression:**
- Severe form: **rapid, uniformly fatal** — median survival well under 1 year (mortality before age 2 in 95.7% of a severe natural-history cohort, PMID:35741019).
- Intermediate form: **progressive but slower** — developmental delay, progressive vision/hearing loss, evolving hepatic and adrenal dysfunction over years; ~77% of children who survive the first year with a "non-progressive" trajectory reach school age (GeneReviews).
- Mild form: **slowly progressive**, dominated by sensory (retinal, cochlear) degeneration over years-to-decades; cognition and mobility may remain largely preserved into adulthood, though hearing/vision loss is essentially universal and progressive even here.
- Disease course is best described as **chronic and progressive** across the spectrum, with the rate of progression (not the presence of progression) distinguishing severity tiers; it is not classically relapsing-remitting.

**Patterns:**
- No spontaneous remission is described; symptomatic/supportive treatments (e.g., cholic acid for cholestasis) can produce biochemical and some clinical improvement but do not reverse the underlying peroxisomal defect.
- **Critical periods:** the neonatal/early-infancy window is the critical period for neuronal migration (in utero/early perinatal) — meaning the most severe structural brain malformations are fixed prenatally and not amenable to postnatal intervention, whereas ongoing myelination, retinal, cochlear, hepatic, and adrenal deterioration in milder patients represent a longer therapeutic window potentially targetable by early biochemical/gene-directed intervention (rationale behind newborn-screening-driven early diagnosis efforts, §10 and §13).

---

## 9. Inheritance and Population

**Epidemiology:**
- **US incidence:** ~1/50,000 live births (historical estimate, now understood to likely undercount mild/atypical cases).
- **Recent New York state confirmed incidence (via newborn screening-adjacent surveillance):** ~1/133,000 births.
- **Japan:** ~1/500,000 births (absence of common European PEX1 founder alleles).
- **Saguenay–Lac-Saint-Jean, Quebec (French-Canadian founder population):** ~1/12,000 births — one of the highest reported incidences worldwide, due to a PEX6 founder mutation ([PMC3483250](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3483250/)).
- A 2025 population-genetics modeling paper specifically models **PEX1-mediated ZSD births and population prevalence** to refine these estimates ([GIM Open 2025](https://www.gimopen.org/article/S2949-7744(25)01470-0/fulltext)).
- Roughly **~30% of ZSD patients carry null variants** (nonfunctional PEX protein) with congenital brain malformations and infant lethality; the **majority (~70%)** have an intermediate-to-milder phenotype from residual PEX protein function.

**Inheritance pattern:** **Autosomal recessive** for all 13 PEX genes (with the rare functional-heterozygote exception noted for PEX6 p.Arg860Trp, §4).

**Penetrance:** Effectively complete/full penetrance for biallelic loss-of-function genotypes; expressivity (not penetrance per se) is the major source of variability.

**Expressivity:** Highly **variable**, driven primarily by residual peroxin activity from the specific allele combination (§4), ranging from neonatal-lethal to adult-onset sensory-predominant disease.

**Genetic anticipation:** Not applicable — ZSD is not a repeat-expansion disorder.

**Germline mosaicism:** Not specifically documented as a recurring feature of ZSD in the literature reviewed; standard autosomal-recessive recurrence risk counseling (25% affected, 50% carrier, 25% unaffected per sibling of two carrier parents) applies (GeneReviews).

**Founder effects:** PEX1 p.Gly843Asp and p.Ile700Tyrfs*42 (European founder alleles); PEX6 founder variant (French-Canadian/Quebec, and possibly Mixteco); population-specific allele spectra explain much of the observed geographic incidence variation.

**Consanguinity role:** Significant contributor in high-consanguinity populations (e.g., Saudi Arabia), where ZSD (along with many other autosomal-recessive diseases) is more frequently observed due to increased homozygosity.

**Carrier frequency:** Not precisely established as a single population-wide number in the sources reviewed, but individual founder-allele carrier frequencies can be substantial in specific populations (e.g., the French-Canadian PEX6 founder variant).

**Population demographics:**
- No strong sex predilection is reported (autosomal recessive disease; consistent with a ~1:1 male:female ratio).
- Geographic/ethnic variation is driven by founder-allele distribution (European vs. Japanese vs. French-Canadian vs. Middle Eastern/consanguineous populations) rather than intrinsic biological sex- or ancestry-linked susceptibility beyond allele frequency effects.
- Age distribution of diagnosed individuals spans neonate through adult, reflecting the full severity spectrum, though the **majority of historically diagnosed cases** are neonatal/infantile because biochemical screening (VLCFA) is most sensitive in that group; milder/adult cases are increasingly recognized with molecular testing and newborn screening spillover (§10).

---

## 10. Diagnostics

**Biochemical/clinical laboratory tests:**
- **Plasma/serum very-long-chain fatty acids (VLCFA)** — elevated; the classic first-line screening test, though **normal/equivocal in some mild cases**, a key diagnostic pitfall.
- **Erythrocyte plasmalogen levels** (RBC C16/C18 plasmalogens) — reduced.
- **Phytanic acid and pristanic acid** — elevated.
- **Pipecolic acid** (plasma/urine) — elevated.
- **Bile acid intermediates** (DHCA/THCA) — elevated in plasma and urine.
- **C26:0-lysophosphatidylcholine (C26:0-LPC)** and **C26:0-carnitine** — newer, more sensitive/specific dried-blood-spot biomarkers, notably validated as **secondary findings from X-ALD newborn screening programs**: in California's X-ALD NBS program (screening via C26:0-LPC since 2016), 9 patients screened positive for elevated C26:0-LPC between 2016–2022 who did not have X-ALD, of whom **7 were subsequently diagnosed with ZSD** via biallelic PEX variants — demonstrating C26:0-LPC's utility as an incidental ZSD-detection tool within an ALD-focused screening program ([2024 publication, PMC11275617](https://pmc.ncbi.nlm.nih.gov/articles/PMC11275617/); [Klouwer/Waterham C26:0-LPC and C26:0-carnitine evaluation, PMID:28677031](https://www.ncbi.nlm.nih.gov/pubmed/28677031)).
- **Plasma C24:0- and C26:0-lysophosphatidylcholines** more broadly proposed as reliable biomarkers for peroxisomal β-oxidation disorders generally ([PMC10910329](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10910329/)).

**Genetic testing:**
- **Multigene PEX panel** sequencing is the recommended first-tier molecular approach (rather than single-gene sequential testing), given 13 causal genes.
- **Sequence analysis detects ~98% of PEX1 variants**; deletion/duplication (CNV) analysis captures most of the remainder.
- **Exome/genome sequencing** is appropriate when the clinical presentation does not clearly localize to ZSD (e.g., an atypical/mild presentation overlapping with Usher syndrome or other conditions).
- Diagnosis is established by **biallelic pathogenic/likely-pathogenic variants in a single PEX gene** in the appropriate biochemical/clinical context.

**Imaging:**
- **Brain MRI** — neuronal migration defects (polymicrogyria, pachygyria) in severe neonatal form; progressive white-matter changes (leukodystrophy) in intermediate/childhood forms.
- **Renal ultrasound** — cortical microcysts.
- **Skeletal radiography** — chondrodysplasia punctata (stippled epiphyses).
- **Liver ultrasound/elastography (fibroscan)** — for ongoing hepatic surveillance.

**Functional/electrophysiologic tests:**
- **EEG** — abnormal in virtually all severe-category patients.
- **Audiometry** — for sensorineural hearing loss surveillance (annual, per GeneReviews management recommendations).
- **Electroretinography (ERG)** — documents progressive retinal dystrophy.

**Biopsy/pathology:** Historically, cultured skin fibroblasts were used for biochemical complementation/functional studies (peroxisome import assays, immunofluorescence for peroxisomal marker proteins) — now largely supplanted by molecular sequencing but still useful for variant functional characterization (e.g., confirming pathogenicity of novel PEX1/PEX13 missense variants).

**Clinical diagnostic criteria:** No formal DSM/ICD-style operational criteria beyond the recognized triad of biochemical abnormality + compatible clinical phenotype + confirmatory biallelic PEX genotype (GeneReviews-based diagnostic algorithm).

**Differential diagnosis:**
- **Neonatal hypotonic/dysmorphic infant:** trisomy 21, Prader-Willi syndrome, congenital myopathies (spinal muscular atrophy, congenital myotonic dystrophy type 1, X-linked myotubular myopathy, multiminicore myopathy).
- **Later/milder presentation (progressive sensory loss + mild developmental delay):** Usher syndrome types I/II, Leber congenital amaurosis, Cockayne syndrome, other congenital leukodystrophies — importantly, "mild forms of PBD can be a differential diagnosis of Usher syndrome," and comprehensive mutation screening including PEX genes is recommended in patients with combined cognitive/visual/hearing impairment of uncertain cause ([search synthesis](https://en.wikipedia.org/wiki/Zellweger_spectrum_disorders); GeneReviews).
- Distinct related peroxisomal disorders that must be distinguished biochemically/molecularly: **rhizomelic chondrodysplasia punctata type 1 (RCDP1, PEX7)** — a peroxisomal assembly defect restricted to PTS2-pathway matrix proteins (AGPS, PHYH), with a biochemically, cellularly, and clinically **distinct** phenotype from classic ZSD, despite shared plasmalogen deficiency; **X-linked adrenoleukodystrophy (ABCD1)** — a peroxisomal transporter (not biogenesis) defect causing VLCFA accumulation without global peroxisome loss.

**Screening:**
- **Newborn screening:** ZSD is not yet a primary RUSP (Recommended Uniform Screening Panel) condition in the US, but is being **incidentally detected via X-ALD newborn screening** (C26:0-LPC), an important and expanding secondary-finding pathway (California data above).
- **Carrier/prenatal/preimplantation genetic screening:** Offered to at-risk families once biallelic familial variants are known; prenatal diagnosis is possible by DNA testing (if variants known) or biochemical testing in cultured amniocytes/chorionic villi (if biochemical defect previously confirmed in an affected relative's fibroblasts). Preimplantation genetic diagnosis for Zellweger syndrome has been reported ([ScienceDirect PGD reference](https://www.sciencedirect.com/science/article/abs/pii/S0015028206044402)).

---

## 11. Outcome/Prognosis

**Survival and mortality:**
- **Severe form:** mortality before age 2 in **95.7%** of a natural-history cohort (n=23); classically described as death within the first year of life without significant developmental progress.
- **Intermediate and mild forms:** substantially better survival; **~77% of children surviving the first year with a non-progressive course reach school age** (GeneReviews). Survival differences across severe/intermediate/mild categories were statistically significant (log-rank p<0.001) in the largest meta-analysis/chart-review study (PMID:35741019).
- Some mildly affected individuals survive into adulthood, though with progressive sensory deficits and other systemic complications (Klouwer 2015 "adulthood" cohort, [PMC4710674](https://pmc.ncbi.nlm.nih.gov/articles/PMC4710674/)).

**Morbidity/functional outcomes:**
- Even among longer-surviving (intermediate/mild) patients, **near-universal progressive vision and hearing loss** is the dominant chronic morbidity.
- Developmental delay is common in intermediate disease (97.5%) but much less so (16.3% seizure rate as a proxy) in mild disease, where most patients achieve independent ambulation (87.8%) and full-sentence speech (71.7%).
- Adrenal insufficiency, if undiagnosed, poses an ongoing acute-decompensation/mortality risk across the spectrum and is likely underdiagnosed in adolescents/adults.
- Hepatic disease can progress to fibrosis/portal hypertension in surviving patients; hepatocellular carcinoma has been reported as a rare late complication in adults.

**Complications:** Recurrent infections/aspiration (from hypotonia/feeding dysfunction), fractures (from osteopenia), bleeding (vitamin-K-responsive coagulopathy from cholestasis), adrenal crisis, progressive blindness/deafness.

**Prognostic factors:** The single strongest prognostic determinant is **genotype/residual peroxin activity** (null vs. hypomorphic allele combination), which directly predicts which severity tier (and hence survival/functional trajectory) a patient falls into (§4, §9).

---

## 12. Treatment

There is **no disease-modifying/curative therapy approved for ZSD**; management is supportive/symptomatic, organ-system-directed, with active experimental gene-therapy research.

**Pharmacotherapy:**
- **Cholic acid (Cholbam™, FDA-approved for bile acid synthesis disorders including peroxisomal disorders)** — oral primary bile acid that restores physiologic feedback inhibition on hepatic bile-acid synthesis, thereby **suppressing production of hepatotoxic C27 bile-acid intermediates**. Clinical trials/case series show reduced AST/ALT, reduced plasma/urinary bile-acid intermediates, improved weight gain, and improved survival in treated patients, though **caution is needed in advanced liver disease** due to potential hepatotoxicity of the therapy itself in that setting ([PMID:27469511](https://pmc.ncbi.nlm.nih.gov/articles/PMC5065608/); long-term case reports in *Case Reports in Gastroenterology*). A long-term personalized-dosing safety study is ongoing (planned through Dec 2027).
- **Docosahexaenoic acid (DHA) supplementation** — rationale: peroxisomal DHA-synthesis deficiency. A randomized, double-blind, placebo-controlled trial (100 mg/kg/day, 50 patients enrolled) found DHA supplementation **did not reduce C26:0 levels** and had **inconsistent effects on visual outcomes**, despite earlier small-cohort reports suggesting improved muscle tone/visual function in newborns ([PMC3013498](https://ncbi.nlm.nih.gov/pmc/articles/PMC3013498); [PMID:8729110](https://pubmed.ncbi.nlm.nih.gov/8729110/)). Net evidence is **not strongly supportive** of DHA as an effective disease-modifying agent, though it remains used empirically in some clinical settings.
- **Betaine** — investigated in a clinical trial context for peroxisome biogenesis disorders ([NCT01838941](https://clinicaltrials.gov/study/NCT01838941)), rationale/results not detailed in sources reviewed here.
- **Anti-seizure medications** — standard symptomatic management for the seizure phenotype.
- **Glucocorticoid/mineralocorticoid replacement** — for confirmed adrenal insufficiency.
- **Fat-soluble vitamin supplementation (A, D, E, K)** — for malabsorption secondary to cholestasis.
- **Bisphosphonates/vitamin D** — considered for osteopenia management.

**Advanced/experimental therapeutics (gene therapy — active research, not yet clinically approved):**
- **AAV8-mediated PEX1 gene augmentation (retinal-directed)** in the PEX1-p.Gly844Asp mouse model improved visual function, retinal structure/response, and biochemical metabolites — "the first testing of gene therapy to treat a peroxisome biogenesis disorder," providing proof-of-concept for gene-augmentation approaches; this program had progressed enough by 2024 to attract venture investment and move toward clinical translation ([Mol Ther Methods Clin Dev, PMC8516995](https://pmc.ncbi.nlm.nih.gov/articles/PMC8516995/); [scientist.com webinar](https://www.scientist.com/webinar/developing-retinal-gene-therapy-for-zellweger-spectrum-disorder-zsd)).
- **In vivo gene editing (CRISPR-based correction of a PEX1 mutation)** — a 2025–2026 preclinical program corrected the disease-causing mutation in mouse models and human patient cells, returning liver tissue to near-normal function; this used the same base-editing/gene-editing platform later adapted for the high-profile "Baby KJ" personalized gene-editing case reported in 2025, and researchers are now exploring delivery modalities that extend beyond liver to the CNS for broader multi-organ benefit (hearing, vision) ([JAX news, April 2026](https://www.jax.org/news-and-insights/2026/april/in-mice-gene-editing-repairs-a-mutation-that-causes-rare-liver-disorder); [biorxiv 2026 preprint](https://www.biorxiv.org/content/10.64898/2026.05.11.723906v1.full.pdf)).
- No RNA-based (ASO/siRNA), cell-therapy, or approved small-molecule targeted therapy for ZSD itself was identified in this search (as distinct from the ASO-based therapies used in unrelated peroxisomal-transporter disease X-ALD, which is molecularly distinct — ABCD1, not a PEX biogenesis gene).

**Surgical/interventional:** Cataract extraction; gastrostomy tube placement for feeding difficulty/dysphagia; occasional orthopedic intervention for skeletal complications.

**Supportive/rehabilitative care:**
- Hearing aids/cochlear implantation consideration for sensorineural hearing loss.
- Physical, occupational, and speech therapy.
- Nutritional support/feeding therapy.
- Dental surveillance/intervention for amelogenesis imperfecta (every 6 months per management guidelines).

**Surveillance schedule (per GeneReviews management recommendations):** growth/nutrition at each visit; annual audiology; annual ophthalmology; annual liver function tests + ultrasound/fibroscan; ACTH/cortisol by age 1 year then annually; dental every 6 months; annual urine oxalate-to-creatinine ratio; head MRI as clinically indicated.

**Suggested MAXO terms:** MAXO:0000004 (surgical procedure — cataract extraction), MAXO:0000011 (physical therapy), MAXO:0000088 (dietary intervention — DHA/vitamin supplementation), MAXO:0000950 (supportive care); pharmacotherapy of cholic acid would use the generic NCIT:C15986 (Pharmacotherapy) treatment-term pattern with `therapeutic_agent` bound to the specific compound (cholic acid; CHEBI:16359).

**Treatment strategy/personalized medicine:** Management is explicitly organ-system-by-organ-system and severity-tiered — i.e., a personalized surveillance/intervention algorithm keyed to where a given patient falls on the severity spectrum, rather than a single uniform treatment algorithm, reflecting the absence of a disease-modifying therapy.

---

## 13. Prevention

- **Primary prevention:** Not possible in the traditional sense (no modifiable risk factor); the only "primary prevention" avenue is **reproductive**, via carrier screening and reproductive decision-making (prenatal diagnosis, preimplantation genetic diagnosis) in families with a known PEX pathogenic variant, or in populations with elevated carrier frequency (e.g., pre-conception expanded carrier screening in consanguineous populations, as illustrated by an Afghan-descent consanguineous cohort study referenced in this search — [PMC12167801](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12167801/)).
- **Secondary prevention (early detection):** Incidental detection through **X-ALD newborn screening** (C26:0-LPC, C26:0-carnitine) is an emerging, real-world secondary-prevention pathway that identifies ZSD **before** overt clinical presentation, enabling earlier initiation of supportive therapy (cholic acid, endocrine/audiology/ophthalmology surveillance) and more accurate genetic counseling.
- **Tertiary prevention:** The entire structured surveillance program described in §12 (annual audiology, ophthalmology, hepatic, endocrine, renal, dental monitoring) functions as tertiary prevention — aiming to catch and manage organ-specific complications before they cause irreversible harm (e.g., catching adrenal insufficiency before crisis, catching hearing/vision loss early enough for assistive intervention).
- **Genetic counseling:** Recommended for affected individuals, known carriers, and at-risk relatives, covering recurrence risk (25%/50%/25% per sibling for AR inheritance), reproductive options, and prenatal/preimplantation testing availability once familial variants are known.
- **No immunization/vaccine strategy** is applicable (non-infectious, genetic disease).
- **No specific environmental/public-health intervention** applies beyond population-level carrier-screening programs in high-risk/consanguineous communities.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No well-documented **naturally occurring** (spontaneous) Zellweger-spectrum-equivalent disease was identified in companion animals (dogs/cats) or livestock in the sources reviewed here; OMIA (Online Mendelian Inheritance in Animals) was not directly queryable in this search session, and general veterinary-genetics sources referenced in the search did not specifically document a natural PEX-gene disease in domestic species. This should be treated as **absence of evidence found**, not confirmed absence — a direct OMIA database query is recommended before asserting no natural animal disease exists.
- **Gene orthologs:** PEX1, PEX6, PEX5, PEX2, PEX7, etc. are broadly conserved across vertebrates and even into yeast (where PEX gene biology was originally characterized), reflected in the extensive use of mouse, zebrafish, and even *Drosophila*/yeast models (below) — i.e., the mechanism is deeply evolutionarily conserved even though naturally occurring veterinary disease is not well documented.
- **Comparative biology:** The core peroxisomal biogenesis/import pathway (PTS1/PTS2 receptors, RING-peroxin ubiquitination, AAA-ATPase recycling) is conserved from yeast to humans, which is precisely why yeast and *Drosophila* genetics originally defined much of PEX gene function before human disease genes were identified.
- **Zoonotic potential/transmission:** Not applicable — ZSD is a non-transmissible monogenic disease.

---

## 15. Model Organisms

**Mouse models:**
- **Constitutive knockouts of Pex5, Pex2, and Pex11β** recapitulate the **severe** end of the spectrum but die shortly after birth due to profound hypotonia/respiratory failure, which has historically limited postnatal disease-progression studies ([Nature Genetics 1997, "A mouse model for Zellweger syndrome"](https://www.nature.com/articles/ng0997-49)).
- **PEX1-G844D (Gly844Asp) knock-in mouse** — models the **mild** end of the human spectrum (analogous to the common human p.Gly843Asp hypomorphic allele) and is viable long-term, recapitulating growth retardation, fatty liver, retinopathy, cochlear hair-cell degeneration, and hearing loss — making it "a robust pre-clinical model for mild Zellweger spectrum disorder" used in longitudinal natural-history and therapeutic (AAV gene-therapy) studies ([ScienceDirect longitudinal study](https://www.sciencedirect.com/science/article/pii/S0925443920302489); [AAV-PEX1 gene augmentation study, PMC8516995](https://pmc.ncbi.nlm.nih.gov/articles/PMC8516995/); [2024 RPE lipidomics biorxiv](https://www.biorxiv.org/content/10.1101/2024.09.05.611330.full.pdf); [2025 liver-disease-progression biorxiv](https://www.biorxiv.org/content/10.1101/2025.05.08.652960.full.pdf)).
- A **Pex7-deficient mouse series** exists for the related but distinct disorder RCDP1 (not classic ZSD), correlating biochemical/neurobehavioral markers with genotype severity ([PMC9310236](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9310236/)).

**Zebrafish models:**
- A **Pex1 loss-of-function zebrafish model** was recently shown to be **viable** (unlike the severe mouse knockouts) and to **recapitulate hallmarks of ZSD**, offering a tractable, higher-throughput vertebrate system for mechanistic and drug-screening studies ([Frontiers in Molecular Neuroscience 2025, PMC12626956](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12626956/)).

**Invertebrate/cellular models:**
- ***Drosophila*** models have been used to dissect **substrate-channeling effects on phospholipids and sphingolipids** in peroxisomal biogenesis disorders, complementing vertebrate models for specific lipidomic mechanism questions ([PMC12157166](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12157166/)); *Drosophila* and mouse models have also been used to show that **peroxisomal biogenesis is genetically and biochemically linked to carbohydrate metabolism** ([PMC5480855](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5480855/)).
- **Patient-derived fibroblasts** remain a standard cellular model for functional variant classification (e.g., confirming the ~15% residual activity of PEX1 p.Gly843Asp) and for studying secondary mechanisms such as MAPK pathway activation and impaired autophagy ([PMC10652488](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10652488/)).
- **Yeast** (historically *Saccharomyces cerevisiae*, *Pichia pastoris*) was the original discovery system for most PEX genes and remains used for basic peroxin biochemistry (e.g., PEX14 phosphorylation and matrix-protein import studies).

**Phenotype recapitulation and limitations:**
- Severe-knockout mice (Pex5/Pex2/Pex11β) faithfully model **lethality and hypotonia** but cannot be used to study chronic, progressive organ pathology because of neonatal death — a key **model limitation**.
- The PEX1-G844D mouse is currently the **best-characterized long-term model**, closely recapitulating the human **mild ZSD** phenotype (hearing loss, retinopathy, liver disease) and serving as the primary preclinical platform for the AAV-gene-therapy and gene-editing programs described in §12.
- The new viable **zebrafish Pex1 model** is positioned as a complementary, more scalable system for hallmark-recapitulation and prospective drug/gene-therapy screening.
- No model fully recapitulates the entire human severity spectrum in one organism; researchers instead use **different models for different severity tiers** (severe knockout mice for the lethal end; PEX1-G844D mice and the new zebrafish model for the mild/intermediate end).

**Model databases/resources:** MGI (Mouse Genome Informatics) for Pex-gene mouse alleles; ZFIN for the zebrafish Pex1 model; FlyBase for the *Drosophila* peroxisomal-biogenesis lines referenced above.

---

## Sources

- [Zellweger Spectrum Disorder — GeneReviews®, NCBI Bookshelf (NBK1448)](https://www.ncbi.nlm.nih.gov/books/NBK1448/)
- [Zellweger spectrum disorders: clinical overview and management approach — Klouwer et al. 2015, PMID:26627182, Orphanet J Rare Dis (PMC4666198)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4666198/)
- [Characterization of Severity in Zellweger Spectrum Disorder by Clinical Findings: A Scoping Review, Meta-Analysis and Medical Chart Review — PMID:35741019 (MDPI Cells)](https://www.mdpi.com/2073-4409/11/12/1891)
- [Zellweger spectrum disorder: A cross-sectional study of symptom prevalence using input from family caregivers — Bose et al. 2020, PMID:33335840](https://www.sciencedirect.com/science/article/pii/S2214426920301403)
- [Zellweger spectrum disorders: clinical manifestations in patients surviving into adulthood — PMC4710674](https://pmc.ncbi.nlm.nih.gov/articles/PMC4710674/)
- [Development and validation of a severity scoring system for Zellweger spectrum disorders — Klouwer et al. 2018, PMID:28857144](https://pubmed.ncbi.nlm.nih.gov/28857144/)
- [OMIM #614870 — Peroxisome Biogenesis Disorder 6A (Zellweger); PBD6A](https://omim.org/entry/614870)
- [OMIM #214100 — Peroxisome Biogenesis Disorder 1A (Zellweger); PBD1A](https://omim.org/entry/214100)
- [OMIM *602136 — Peroxisome Biogenesis Factor 1; PEX1](https://omim.org/entry/602136)
- [Orphanet: Zellweger syndrome (ORPHA:912)](https://www.orpha.net/en/disease/detail/912)
- [Orphanet: Peroxisome biogenesis disorder (ORPHA:79189)](https://www.orpha.net/en/disease/detail/79189)
- [Estimation of PEX1-mediated Zellweger spectrum disorder births and population prevalence by population genetics modeling — Genetics in Medicine Open, 2025](https://www.gimopen.org/article/S2949-7744(25)01470-0/fulltext)
- [A founder mutation in the PEX6 gene is responsible for increased incidence of Zellweger syndrome in a French Canadian population — PMC3483250](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3483250/)
- [Zellweger's Syndrome With PEX6 Gene Mutation in Mixteco Neonates Due to Possible Founder Effect — PMC10573658](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10573658/)
- [Genotype–phenotype correlations and disease mechanisms in PEX13-related Zellweger spectrum disorders — PMC9295491](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9295491/)
- [Mild Zellweger syndrome due to functionally confirmed novel PEX1 variants — PMC6968987](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6968987/)
- [NM_000466.3(PEX1):c.2528G>A (p.Gly843Asp) — ClinVar RCV000007946](https://www.ncbi.nlm.nih.gov/clinvar/RCV000007946/)
- [Evaluation of C26:0-lysophosphatidylcholine and C26:0-carnitine as diagnostic markers for Zellweger spectrum disorders — PMID:28677031](https://www.ncbi.nlm.nih.gov/pubmed/28677031)
- [Newborn Screening for X-Linked Adrenoleukodystrophy (X-ALD): Biochemical, Molecular, and Clinical Characteristics of Other Genetic Conditions — PMC11275617 (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11275617/)
- [Plasma C24:0- and C26:0-lysophosphatidylcholines as biomarkers for peroxisomal β-oxidation disorders — PMC10910329](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10910329/)
- [Cholic acid therapy in Zellweger spectrum disorders — PMID:27469511, PMC5065608](https://pmc.ncbi.nlm.nih.gov/articles/PMC5065608/)
- [Docosahexaenoic acid therapy in peroxisomal diseases: Results of a double-blind, randomized trial — PMC3013498](https://ncbi.nlm.nih.gov/pmc/articles/PMC3013498)
- [AAV-mediated PEX1 gene augmentation improves visual function in the PEX1-Gly844Asp mouse model — PMC8516995](https://pmc.ncbi.nlm.nih.gov/articles/PMC8516995/)
- [In mice, gene editing repairs a mutation that causes rare liver disorder — Jackson Laboratory, April 2026](https://www.jax.org/news-and-insights/2026/april/in-mice-gene-editing-repairs-a-mutation-that-causes-rare-liver-disorder)
- [Pex1 loss-of-function in zebrafish is viable and recapitulates hallmarks of Zellweger spectrum disorders — PMC12626956 (2025)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12626956/)
- [Longitudinal study of Pex1-G844D NMRI mouse model: A robust pre-clinical model for mild Zellweger spectrum disorder — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0925443920302489)
- [Drosophila models uncover substrate channeling effects on phospholipids and sphingolipids in peroxisomal biogenesis disorders — PMC12157166](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12157166/)
- [The biochemical basis of mitochondrial dysfunction in Zellweger Spectrum Disorder — EMBO Reports](https://www.embopress.org/doi/full/10.15252/embr.202051991)
- [Abnormal activation of MAPK pathways and inhibition of autophagy in ZSD and X-ALD patients — PMC10652488](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10652488/)
- [Reactome: Peroxisomal protein import (R-HSA-9033241)](https://reactome.org/content/detail/R-HSA-9033241)
- [AmiGO 2: GO:0016561, GO:0016562, GO:0044721 (peroxisomal matrix protein import terms)](https://amigo.geneontology.org/amigo/term/GO:0016561)
- [Rhizomelic Chondrodysplasia Punctata Type 1 — PEX7 gene, distinct from ZSD (Nature Genetics 1997)](https://www.nature.com/articles/ng0497-381)
- [A Pex7 Deficient Mouse Series Correlates Biochemical and Neurobehavioral Markers to Genotype Severity — PMC9310236](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9310236/)
- [ICD10Data: E71.518 Other disorders of peroxisome biogenesis](https://www.icd10data.com/ICD10CM/Codes/E00-E89/E70-E88/E71-/E71.518)
- [Zellweger Spectrum Disorder — StatPearls, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK560676/)
- [Longitudinal Natural History Study of Patients With Peroxisome Biogenesis Disorders (PBD) — ClinicalTrials.gov NCT01668186](https://clinicaltrials.gov/study/NCT01668186)
- [Betaine and Peroxisome Biogenesis Disorders — ClinicalTrials.gov NCT01838941](https://clinicaltrials.gov/study/NCT01838941)
- [Effectiveness of expanded prenatal screening among consanguineous couples of Afghan descent — PMC12167801](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12167801/)
- [A mouse model for Zellweger syndrome — Nature Genetics 1997](https://www.nature.com/articles/ng0997-49)