---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T18:02:23.435473'
end_time: '2026-08-19T18:06:41.208544'
duration_seconds: 257.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Vitamin D-Dependent Rickets Type 1B
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
  web_search_requests: 15
  num_turns: 18
  total_cost_usd: 1.6537565
  session_id: 75ec52a1-0e70-502f-850e-ec2680b017b0
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 17
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 12
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vitamin D-Dependent Rickets Type 1B
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Vitamin D-Dependent Rickets Type 1B** covering all of the
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

I'll research Vitamin D-Dependent Rickets Type 1B (CYP2R1 deficiency) using web search to ensure accurate, current citations.

# Vitamin D-Dependent Rickets Type 1B (VDDR1B) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Vitamin D-dependent rickets type 1B (VDDR1B), also called vitamin D 25-hydroxylase deficiency or "selective 25-hydroxyvitamin D deficiency," is an autosomal recessive inborn error of vitamin D metabolism caused by loss-of-function variants in *CYP2R1*, which encodes the principal hepatic microsomal vitamin D 25-hydroxylase (Cheng et al., PNAS 2004, PMID:15128933). Loss of this enzyme activity blocks the first obligatory activation step of vitamin D — hydroxylation of vitamin D3/D2 at carbon-25 to form 25-hydroxyvitamin D [25(OH)D] — producing a phenotype that is clinically and radiographically indistinguishable from nutritional vitamin D deficiency rickets but that fails to respond, or responds only poorly, to conventional-dose vitamin D3 supplementation (Molin et al., *J Bone Miner Res* 2017, PMID:28548312).

**Key identifiers:**
- **OMIM:** #600081 (VDDR1B, phenotype); *608713 (CYP2R1, gene)
- **MONDO:** MONDO:0010810
- **Gene:** CYP2R1 (HGNC:20586), chromosome 11p15.2
- **Orphanet:** ORPHA:289320 (Vitamin D-dependent rickets type 1B)
- **ICD-10:** E55.0 (Rickets, active) is used generically; no VDDR1B-specific code exists
- **MeSH:** Rickets (D012279); Vitamin D Deficiency (D014808)

**Synonyms:** 25-hydroxylase deficiency rickets; vitamin D 25-hydroxylase deficiency; selective 25-hydroxyvitamin D deficiency; CYP2R1 deficiency rickets; hereditary vitamin D-resistant rickets type 1B (this last term is discouraged since VDDR1B is not a vitamin-D-*resistant* disorder but a synthesis defect).

**Data provenance:** Essentially all published knowledge derives from individual patient/family case reports and small case series (the largest being 27 subjects from 9 Saudi families; Alzahrani et al. 2021, PMID:34137732), rather than population/aggregate registries — VDDR1B is exceedingly rare, with fewer than 40 molecularly confirmed patients reported worldwide as of 2024.

---

## 2. Etiology

### Disease Causal Factors
VDDR1B is monogenic: biallelic (homozygous or compound heterozygous) loss-of-function variants in *CYP2R1* abolish or severely reduce hepatic 25-hydroxylase activity (Cheng et al. 2004, PMID:15128933; Thacher et al., *JCEM* 2015, PMID:25942481). A subset of reported heterozygous carriers also show a milder, incompletely penetrant biochemical phenotype (blunted 25(OH)D response to vitamin D3 loading), suggesting semi-dominant/haploinsufficiency effects for some alleles (Thacher et al. 2015, PMID:25942481).

### Genetic Risk Factors
Reported pathogenic variants (all in *CYP2R1*, NM_024514):
- **p.Leu99Pro (L99P, c.296T>C)** — the most recurrent pathogenic allele, first reported homozygous in a Nigerian child (Cheng et al. 2004) and subsequently in Moroccan and additional Nigerian families (homozygous in 3, heterozygous in 6, across 2 generations of 2 Nigerian families; Thacher et al. 2015, PMID:25942481; Molin et al. 2017, PMID:28548312). In vitro expression shows normal protein levels but essentially abolished 25-hydroxylase activity.
- **p.Lys242Asn (K242N)** — identified in a second Nigerian family; markedly reduced (not abolished) enzymatic activity in vitro (Thacher et al. 2015, PMID:25942481).
- **c.367+1G>A (splice donor)** and **c.768dupT (frameshift)** — the two founder-like alleles accounting for the majority of the 27 Saudi Arabian patients from 9 families (12/27 and 15/27 patients respectively; 18 homozygous, 9 heterozygous carriers with biochemical abnormalities) (Alzahrani et al. 2021, PMID:34137732; earlier reported by Al Mutair et al., *JCEM* 2012, PMID:22855339, as compound heterozygous splice-site + frameshift mutations in a Saudi sibship).
- **Deletion/insertion (indel) mutation** — homozygous in a French family reported by Molin et al. 2017 (PMID:28548312), alongside the recurrent L99P allele in a Moroccan family (7 patients, 2 families total).
- **c.50_51insTCGGCGGCGC (p.Leu18ArgfsTer79)** — a novel frameshift variant, homozygous, reported in two siblings from India — the first molecularly confirmed VDDR1B case from Asia (JCEM Case Reports 2024, PMID:38440125).
- Additional novel missense and truncating variants have been reported in isolated case reports through 2021 ("New Variants of the CYP2R1 Gene…", PMC8699237).

**Population/allele frequency:** Because reported alleles are private or regionally clustered (Nigeria, Saudi Arabia/Gulf, Morocco, France, India), none reach appreciable frequency in gnomAD; most pathogenic alleles are absent or present only as rare heterozygotes in population reference databases, consistent with a fully penetrant recessive Mendelian disease.

### Environmental Risk Factors
No independent environmental cause exists for VDDR1B itself (it is monogenic), but the biochemical/clinical severity is strongly modulated by cutaneous vitamin D3 synthesis (sun exposure) and dietary vitamin D intake — because CYP2R1-null patients still retain a minor, CYP2R1-independent route of 25-hydroxylation (via CYP27A1 and other hepatic/extrahepatic P450s), higher substrate (vitamin D3) availability can partially compensate. This is the biochemical rationale for supraphysiologic vitamin D3 dosing as first-line therapy, and it is also why the phenotype can be **misdiagnosed as ordinary nutritional rickets** when a family history or lack of vitamin D3-dose response is not recognized (Molin et al. 2017, PMID:28548312 — explicitly framed as "a rare condition or a misdiagnosed condition").

### Protective Factors
No specific genetic protective alleles have been described for VDDR1B. High cutaneous/dietary vitamin D3 substrate supply is the main modifiable factor mitigating severity, since residual (non-CYP2R1) 25-hydroxylase activity is substrate-driven.

### Gene-Environment Interactions
The core gene-environment interaction is substrate-dependent enzymatic bypass: because a second, lower-affinity/lower-capacity 25-hydroxylation pathway exists (demonstrated definitively in *Cyp2r1*-knockout mice, which retain ~50% of normal serum 25(OH)D3 rather than none; Zhu et al., *PNAS* 2013, PMID:24019477), increasing vitamin D3 intake to supraphysiologic levels can drive meaningful 25(OH)D production even in the near-total absence of CYP2R1 activity. Homozygous L99P patients show a markedly blunted (but not entirely absent) rise in 25(OH)D after oral vitamin D3 loading compared with heterozygotes (Thacher et al. 2015, PMID:25942481), directly demonstrating gene-dose/substrate interaction.

---

## 3. Phenotypes

| Phenotype | Type | HPO term | Onset/Notes |
|---|---|---|---|
| Rickets (radiographic) | Sign/imaging | HP:0002748 (Rickets) | Typically infancy–early childhood; metaphyseal fraying/cupping |
| Tibial bowing | Sign | HP:0002979 (Bowing of the legs) | Reported as early as age 2 y in the Nigerian kindred, symptomatic by 12.5 y (Thacher 2015) |
| Leg pain | Symptom | HP:0002829 (Arthralgia)/HP:0030836 (limb pain, if available) | Presenting complaint in several reports |
| Rachitic rosary (rib beading) | Sign | HP:0000895 (Beading of ribs) | Classic rachitic finding |
| Wrist/metaphyseal enlargement | Sign | HP:0003037 (Metaphyseal widening)/HP:0005034 (wide wrist) | |
| Failure to thrive | Sign | HP:0001508 | More prominent in infantile-onset/severe cases |
| Hypotonia / muscle weakness | Sign | HP:0001324 (Muscle weakness), HP:0001252 (Hypotonia) | |
| Hypocalcemic seizures | Sign | HP:0002917 (Hypocalcemia) → HP:0032669 or HP:0001250 (Seizure) | Reported in severe/early presentations, more typical of VDDR1A but described in VDDR1B too |
| Low serum 25(OH)D | Lab abnormality | HP:0100511 (Abnormality of vitamin D metabolism) — closest available; consider a custom biochemical descriptor | Hallmark, disproportionately low relative to sun/diet exposure and unresponsive to standard-dose vitamin D3 |
| Hypocalcemia | Lab abnormality | HP:0002901 | |
| Hypophosphatemia | Lab abnormality | HP:0002148 | Secondary to hyperparathyroidism-driven renal phosphate wasting |
| Elevated alkaline phosphatase | Lab abnormality | HP:0003155 | |
| Secondary hyperparathyroidism (elevated PTH) | Lab abnormality | HP:0000870 | Compensatory response to hypocalcemia |
| Normal-to-low 1,25(OH)2D | Lab abnormality (distinguishing) | — | Distinguishes from VDDR1A, where 1,25(OH)2D is disproportionately low/undetectable despite normal CYP27B1 substrate |

**Characteristics:**
- **Onset:** Predominantly infantile/early childhood, though several reported cases (Nigerian kindred, Molin et al. 2017 French/Moroccan families) presented in later childhood/adolescence with milder or slowly progressive disease, and at least one adult cohort has been studied for long-term skeletal consequences (Wiedemann et al., *Calcif Tissue Int* 2020, PMID:32430692).
- **Severity/course:** Variable — homozygotes for null alleles (e.g., L99P homozygotes) show more severe biochemical deficiency and more blunted treatment response than heterozygotes; disease is generally described as progressive if untreated, but non-progressive/stable once adequately treated with high-dose vitamin D3.
- **Frequency of individual phenotypes:** Given the very small published cohorts (n≤27), only qualitative/case-count frequencies are available rather than validated percentage estimates; rickets, bowing, and biochemical hypovitaminosis D are near-universal among reported homozygotes, while seizures are less consistently reported.
- **Quality of life:** Not systematically studied with validated instruments (no EQ-5D/SF-36/PROMIS data identified in the literature); qualitatively, adequately treated patients show good clinical/radiographic recovery ("rickets heal" — Thacher et al. 2015), and Wiedemann et al. 2020 (PMID:32430692) specifically found that prolonged 25-OH-vitamin D deficiency in treated adults did **not** impair bone mineral density, suggesting a favorable long-term skeletal prognosis with treatment.

---

## 4. Genetic/Molecular Information

**Causal gene:** *CYP2R1* (cytochrome P450, family 2, subfamily R, polypeptide 1), HGNC:20586, OMIM *608713, chromosome 11p15.2. Encodes a microsomal (endoplasmic-reticulum-anchored) cytochrome P450 monooxygenase expressed predominantly in liver, with lower expression in numerous extrahepatic tissues (skin, testis, adipose, etc.).

**Variant classification/type (per ACMG/AMP, as reported in the literature and ClinVar):**
- Missense: p.Leu99Pro (ClinVar RCV000002216, pathogenic), p.Lys242Asn
- Frameshift: c.768dupT (p.Leu257Serfs*6; ClinVar VCV000977185), c.50_51insTCGGCGGCGC (p.Leu18ArgfsTer79)
- Splice-site: c.367+1G>A (canonical splice-donor loss)
- Indel: the French-family deletion/insertion reported by Molin et al. 2017

**Functional consequences:** In vitro heterologous expression studies (COS-7/HEK293 systems) show that pathogenic missense alleles (L99P) can retain normal protein expression levels while exhibiting **complete loss of 25-hydroxylase catalytic activity**, whereas K242N shows **markedly reduced but not abolished** activity — consistent with the somewhat milder phenotype variability seen clinically (Thacher et al. 2015, PMID:25942481). Frameshift/splice alleles are predicted to cause nonsense-mediated decay or truncated, non-functional protein (Al Mutair et al. 2012, PMID:22855339).

**Allele frequency/population data:** No pathogenic *CYP2R1* allele associated with VDDR1B reaches polymorphic frequency in gnomAD/1000 Genomes/TOPMed; each is essentially private to the reporting family or regional cluster (Nigeria: L99P, K242N; Saudi Arabia: c.367+1G>A, c.768dupT; Morocco: L99P; France: indel; India: p.Leu18ArgfsTer79). This contrasts with **common regulatory/coding CYP2R1 SNPs** (e.g., rs10741657, rs2060793) that are well-studied GWAS hits for population variation in circulating 25(OH)D and are unrelated to the Mendelian disease.

**Somatic vs. germline:** Germline only; VDDR1B is not associated with somatic mosaicism or malignancy.

**Modifier genes:** None formally established; residual 25-hydroxylation via CYP27A1 and other minor hepatic/extrahepatic hydroxylases (demonstrated in the *Cyp2r1*/*Cyp27a1* double-knockout mouse model — Zhu et al. 2013, PMID:24019477) functionally modifies phenotype severity but is not itself a defined "modifier gene" locus in humans.

**Epigenetic information:** Not disease-specific for VDDR1B; general regulatory studies show hepatic *CYP2R1* expression is repressed by obesity/metabolic stress and streptozotocin-induced diabetes in mouse models (unrelated to the Mendelian disorder but relevant to acquired/relative 25(OH)D deficiency).

**Chromosomal abnormalities:** None reported; VDDR1B is caused by intragenic point/small indel variants, not large structural rearrangements.

**Protein structure:** The crystal structure of CYP2R1 in complex with vitamin D3 (Strushkevich et al., *J Mol Biol* 2008, PMID:18511070) shows the canonical CYP fold (12 core α-helices, β-sheet subdomains, heme buried centrally), a closed conformation with the substrate-access channel gated by the B′-helix, and vitamin D3 bound in an elongated pose with its aliphatic side chain oriented toward the heme iron for regiospecific C25 hydroxylation — explaining the enzyme's narrow substrate specificity and the structural basis by which active-site missense variants (e.g., L99P, which lies near a substrate-contacting region) abolish catalysis.

**Suggested ontology terms:** HGNC:20586 (CYP2R1); GO:0034653 (retinoic acid catabolic process — off-target; correct term: GO:0042359, vitamin D metabolic process); GO:0034644 (cellular response to UV); molecular function GO:0004497 (monooxygenase activity), GO:0070576 (vitamin D 25-hydroxylase activity, if available as a specific GO term); UniProt Q6VVW9 (mouse) / Q9UF56 (human CYP2R1); CHEBI:28934 (cholecalciferol/vitamin D3), CHEBI:17933 (25-hydroxyvitamin D3, calcifediol).

---

## 5. Environmental Information

- **Environmental factors:** Not disease-causing (VDDR1B is monogenic), but sunlight (UVB) exposure and dietary vitamin D intake determine substrate availability for the minor CYP2R1-independent 25-hydroxylation pathway and are the basis of the high-dose vitamin D3 treatment strategy.
- **Lifestyle factors:** Reduced sun exposure or low dietary vitamin D intake would be expected to unmask/worsen the phenotype in genetically predisposed individuals, though this has not been rigorously quantified for VDDR1B specifically (unlike common nutritional rickets).
- **Infectious agents:** None implicated.

---

## 6. Mechanism / Pathophysiology

**Causal chain:**
1. **Initial defect (molecular/enzymatic):** Biallelic loss-of-function *CYP2R1* variants abolish or severely impair hepatic microsomal vitamin D 25-hydroxylase activity (GO:0004497 monooxygenase activity; the enzyme catalyzes NADPH-cytochrome P450 reductase-dependent hydroxylation at C25 of the vitamin D side chain).
2. **Biochemical consequence:** Failure to convert vitamin D3 (cholecalciferol, from skin/diet) to 25-hydroxyvitamin D3 [25(OH)D3, calcifediol] — the major circulating vitamin D metabolite and substrate for renal 1α-hydroxylase (CYP27B1). Serum 25(OH)D falls to deficient/near-undetectable levels despite normal or even excess vitamin D3 precursor availability (Cheng et al. 2004, PMID:15128933).
3. **Downstream hormonal consequence:** Reduced 25(OH)D substrate limits renal CYP27B1-mediated production of the active hormone 1,25-dihydroxyvitamin D3 [1,25(OH)2D3, calcitriol], though residual (non-CYP2R1) 25-hydroxylation and compensatory renal 1α-hydroxylase upregulation can partially buffer 1,25(OH)2D3 levels — hence 1,25(OH)2D3 may be low-normal rather than undetectable (distinguishing VDDR1B biochemically from the more profound calcitriol deficiency of VDDR1A/CYP27B1 deficiency).
4. **Cellular/tissue consequence:** Reduced calcitriol-VDR (vitamin D receptor, NR1I1) signaling in intestinal enterocytes decreases active transcellular calcium (and secondarily phosphate) absorption (biological process: GO:0070508, cholesterol import; more relevantly GO:0006816 calcium ion transport and GO:0030299 intestinal cholesterol absorption analogs — the specific relevant GO term is GO:0033280, response to vitamin D).
5. **Systemic consequence — mineral homeostasis:** Reduced intestinal calcium absorption → hypocalcemia → compensatory secondary hyperparathyroidism (elevated PTH) → renal phosphate wasting → hypophosphatemia, and PTH-driven increased bone turnover contributing to elevated serum alkaline phosphatase.
6. **Tissue-level outcome — impaired mineralization:** Combined hypocalcemia/hypophosphatemia impair hydroxyapatite deposition at the growth-plate mineralization front, producing the rachitic growth-plate histology (widened, disorganized hypertrophic chondrocyte zone) and osteomalacic changes in cortical/trabecular bone, manifesting clinically as rickets, bowing, rachitic rosary, and growth-plate widening.

**Cell types involved (CL terms):** hepatocyte (CL:0000182, site of primary enzymatic defect), enterocyte/intestinal absorptive cell (CL:0000584, target of reduced calcitriol signaling), chondrocyte — growth plate hypertrophic chondrocyte (CL:0000138, site of impaired mineralization), osteoblast (CL:0000062) and osteoclast (CL:0000092, bone remodeling/turnover), chief cell of parathyroid gland (CL:1000398, source of compensatory PTH secretion), and renal proximal tubule epithelial cell (CL:1001016, site of CYP27B1 1α-hydroxylation and, secondarily, PTH-driven phosphate wasting).

**Anatomical/organ correlate:** This causal chain maps directly onto dismech's `defective_skeletal_mineralization` module (the calciopenic arm — nutritional-vitamin-D-deficiency-analogous mechanism, converging on "Impaired Hydroxyapatite Deposition at the Mineralization Front") — VDDR1B is a strong candidate conformer to that module's calciopenic trigger arm, entering via a primary hepatic 25-hydroxylation defect rather than dietary/sunlight deficiency, but converging on the same rate-limiting mineralization node.

**Molecular pathways (KEGG/Reactome):** Vitamin D metabolism/activation pathway (Reactome R-HSA-5579022, "Defective CYP2R1 causes vitamin D 25-hydroxylase deficiency" — Reactome has a specific disease pathway entry for this defect); KEGG hsa00140 (Steroid hormone biosynthesis, vitamin D branch).

**Immune involvement:** Not a primary disease mechanism; VDR/calcitriol signaling has broader immunomodulatory roles described in the general vitamin D literature, but no VDDR1B-specific immune phenotype has been reported.

**Molecular profiling / omics:** No transcriptomic, proteomic, or single-cell studies specific to VDDR1B patient tissue have been published (the disease is studied almost exclusively via targeted Sanger/exome sequencing and biochemical phenotyping, not omics).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Liver (site of CYP2R1 deficiency; UBERON:0002107); skeletal system broadly (rickets/osteomalacia).
- **Organ level (secondary):** Kidney (compensatory 1α-hydroxylase activity, renal phosphate wasting; UBERON:0002113); parathyroid glands (compensatory hyperplasia/hypersecretion; UBERON:0001132); small intestine (reduced calcium/phosphate absorption; UBERON:0002108).
- **Body systems:** Skeletal system, endocrine system (calcium-PTH-vitamin D axis), digestive system (hepatic and intestinal components).
- **Tissue/cell level:** Growth plate cartilage (UBERON:0002514) — hypertrophic chondrocyte zone; long bone cortical/trabecular bone (UBERON:0002481); hepatocyte microsomal/ER compartment (site of CYP2R1 localization).
- **Subcellular level:** Endoplasmic reticulum (GO:0005783) — CYP2R1 is an ER-membrane-anchored microsomal P450.
- **Localization/laterality:** Systemic/bilateral — rickets and bowing are bilateral, symmetric skeletal findings (unlike unilateral focal bone lesions).

---

## 8. Temporal Development

- **Onset:** Typically infancy to early childhood (as young as 2 years for radiographic bowing in the index Nigerian family), though later-childhood/adolescent presentation is also reported; onset pattern is insidious/chronic rather than acute.
- **Progression:** Untreated disease is progressive (worsening rachitic deformity, growth impairment); with high-dose vitamin D3 treatment, radiographic healing of rickets is documented (Thacher et al. 2015, PMID:25942481), and adult follow-up (Wiedemann et al. 2020, PMID:32430692) shows preserved bone mineral density despite persistent biochemical 25(OH)D deficiency — suggesting good long-term prognosis with adequate calcium/vitamin D3 management even if full biochemical normalization of 25(OH)D is not achieved.
- **Disease course pattern:** Chronic, lifelong biochemical defect (enzyme deficiency is permanent), but clinically manageable/stable with treatment; relapse on treatment discontinuation has been specifically described as a diagnostic clue distinguishing VDDR1B from self-limited nutritional rickets (JCEM Case Reports 2024, PMID:38440125).
- **Critical periods:** Growth-plate-open childhood/adolescence is the period of clinical vulnerability for rachitic skeletal deformity; after growth-plate closure, the primary residual risk shifts to osteomalacia/bone mineral density, which appears to be less severely affected in treated adults.

---

## 9. Inheritance and Population

- **Epidemiology:** No formal prevalence/incidence estimate exists; VDDR1B is classified as ultra-rare, with the world literature comprising fewer than ~40 molecularly confirmed cases across scattered case reports/small series as of 2024. This maps to `prevalence_class: NOT_YET_DOCUMENTED` or `ULTRA_RARE` in dismech terms, sourced from Orphanet (ORPHA:289320).
- **Inheritance pattern:** Autosomal recessive (biallelic homozygous or compound heterozygous variants). Notably, several reports describe **heterozygous carriers with a milder, incompletely penetrant biochemical phenotype** (subnormal 25(OH)D response to vitamin D3 challenge) — this is a semi-dominant/haploinsufficiency signal worth capturing explicitly (e.g., an `Inheritance` block noting incomplete penetrance in heterozygotes, distinct from the fully penetrant recessive homozygous/compound-heterozygous disease).
- **Penetrance/expressivity:** Homozygous null genotypes show high penetrance for biochemical and clinical rickets; expressivity is variable in severity and age of clinical recognition, likely modulated by sun exposure/diet (substrate availability) as discussed above.
- **Consanguinity:** Multiple reported kindreds (Nigerian, Saudi Arabian, Moroccan) are from populations/family structures with elevated consanguinity, consistent with recessive inheritance and founder alleles; the Saudi cohort (Alzahrani et al. 2021) specifically comprises 9 families with two recurrent founder-like alleles.
- **Founder effects:** L99P recurs across Nigerian and Moroccan families (possibly a mutational hotspot rather than a single founder haplotype, given geographic spread); c.367+1G>A and c.768dupT appear to function as regional founder/recurrent alleles within the Saudi Arabian cohort.
- **Affected populations/geography:** Cases reported from Nigeria, Saudi Arabia (largest series), Morocco, France, and — as of 2024 — India (first Asian case, JCEM Case Reports 2024, PMID:38440125), suggesting global but sporadic distribution rather than strict geographic restriction, with ascertainment likely biased toward regions/populations with active clinical genetics programs and higher consanguinity rates.
- **Sex ratio / age distribution:** No sex predilection has been reported; case series span pediatric through adult ages (Wiedemann et al. 2020 specifically studied adult outcomes).

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- Serum 25-hydroxyvitamin D (25(OH)D) — markedly low/undetectable despite adequate sun/dietary exposure (the key discriminating lab finding); LOINC 62292-8 (25-Hydroxyvitamin D3).
- Serum calcium (low/low-normal), phosphate (low), alkaline phosphatase (elevated), intact PTH (elevated) — the classic secondary-hyperparathyroid rachitic biochemical panel.
- Serum 1,25-dihydroxyvitamin D — typically low-normal (distinguishing from the profoundly low/undetectable 1,25(OH)2D of VDDR1A/CYP27B1 deficiency, where 25(OH)D is normal-to-high but 1α-hydroxylation is blocked).
- Radiographic imaging (long bones, wrists, chest) — classic rachitic metaphyseal fraying/cupping, rib beading, bowing.

**Genetic testing:**
- Targeted *CYP2R1* Sanger sequencing or a rickets/metabolic-bone-disease gene panel is the recommended diagnostic approach once biochemical findings (low 25(OH)D unresponsive to standard vitamin D3 dosing, especially with a positive family history or parental consanguinity) raise suspicion.
- Whole-exome sequencing has been used in several reported cases when the phenotype was initially misattributed to nutritional deficiency.

**Clinical criteria / differential diagnosis:**
- **Nutritional vitamin D deficiency rickets:** distinguished by *response* to standard-dose vitamin D3 and correction of 25(OH)D; VDDR1B does not normalize 25(OH)D with usual doses and requires supraphysiologic dosing or fails to respond to repeated conventional courses (this non-response is the single most important clinical clue prompting genetic testing — emphasized in JCEM Case Reports 2024, PMID:38440125).
- **VDDR type 1A (CYP27B1 deficiency, OMIM #264700):** 25(OH)D is normal-to-elevated but 1,25(OH)2D is low/undetectable (blocked renal 1α-hydroxylation), the inverse biochemical pattern from VDDR1B.
- **VDDR type 2A (VDR mutations, hereditary vitamin D-resistant rickets, OMIM #277440):** elevated 1,25(OH)2D with target-organ resistance (often with alopecia).
- **VDDR type 3 (CYP3A4-mediated accelerated vitamin D inactivation, OMIM #619073):** a distinct hypercatabolic mechanism.
- **Hypophosphatemic rickets (e.g., X-linked, PHEX/FGF23-mediated):** distinguished by normal PTH and normal/high 1,25(OH)2D with isolated renal phosphate wasting, versus the secondary-hyperparathyroid picture of VDDR1B.

**Screening:** No population newborn or carrier screening program exists for VDDR1B given its extreme rarity; case-finding is clinical (family history of rickets, consanguinity, treatment non-response) followed by targeted sequencing.

---

## 11. Outcome/Prognosis

- **Mortality:** No disease-specific mortality has been reported; VDDR1B is not considered a life-limiting condition when diagnosed and treated.
- **Morbidity:** Untreated/undiagnosed disease carries morbidity from progressive skeletal deformity (bowing), growth impairment, and potentially hypocalcemic seizures in severe infantile presentations.
- **Functional/skeletal outcome with treatment:** Radiographic healing of rickets is well documented with high-dose vitamin D3 (Thacher et al. 2015, PMID:25942481; JCEM Case Reports 2024, PMID:38440125). Long-term adult follow-up (Wiedemann et al. 2020, PMID:32430692) found that persistent biochemical 25(OH)D deficiency, once patients are past the growth-plate-vulnerable period and on adequate calcium/vitamin D management, does **not** translate into reduced bone mineral density — a reassuring prognostic finding.
- **Complications:** Growth deformity/bowing if diagnosis is delayed; recurrence/relapse of rachitic biochemistry on treatment discontinuation is a recognized pattern used diagnostically.
- **Prognostic factors:** Genotype severity (null/frameshift/splice vs. hypomorphic missense such as K242N) correlates with degree of biochemical deficiency and blunting of treatment response; early diagnosis and sustained supraphysiologic vitamin D3/calcium therapy are the main modifiable prognostic levers.

---

## 12. Treatment

**Pharmacotherapy (first-line):**
- **High-dose (supraphysiologic) oral cholecalciferol (vitamin D3)** plus calcium supplementation is the mainstay, with dose titrated against serum alkaline phosphatase, 25(OH)D, and PTH to achieve normalization and radiographic healing (JCEM Case Reports 2024, PMID:38440125; Thacher et al. 2015, PMID:25942481). NCIT term: NCIT:C15986 (Pharmacotherapy) as `treatment_term`, with `therapeutic_agent` CHEBI:28934 (cholecalciferol).
- **Calcifediol [25(OH)D3] supplementation** is mechanistically attractive (it bypasses the defective hydroxylation step entirely) and has been used/discussed in the literature, though most published cases relied on high-dose native vitamin D3 with clinical/biochemical response, implying that some residual (CYP2R1-independent) 25-hydroxylation capacity is exploitable at high substrate doses. Where used, calcifediol would map to `therapeutic_agent` CHEBI:17933 (calcifediol/25-hydroxyvitamin D3) under the same NCIT:C15986 Pharmacotherapy `treatment_term`.
- **Calcitriol** [1,25(OH)2D3] is a theoretical option (bypassing both defective hydroxylation steps) but is not the standard reported approach for VDDR1B specifically (contrast with VDDR1A, where calcitriol is first-line because the defect is downstream at the 1α-hydroxylation step).

**Advanced therapeutics:** No gene therapy, cell therapy, or RNA-based therapeutics have been developed or trialed for VDDR1B — the condition is effectively manageable with vitamin D3/calcium supplementation, which has limited the impetus for advanced modality development.

**Surgical:** Orthopedic correction (e.g., osteotomy) may be considered for severe, fixed bowing deformity that does not remodel after biochemical correction, as in other rachitic conditions, though this is not specifically documented in the VDDR1B literature reviewed.

**Supportive care:** Physical therapy/rehabilitation for gait or deformity-related functional impairment (NCIT:C15302, Physical Therapy) may be used adjunctively, per general rachitic-disease management, though not specifically reported for VDDR1B.

**Monitoring/treatment strategy:** Dose titration is driven by serial serum alkaline phosphatase, 25(OH)D, calcium, phosphate, and PTH, aiming for normalization of all markers and radiographic healing; because relapse occurs on treatment discontinuation, long-term/indefinite supplementation is implied rather than a time-limited course (JCEM Case Reports 2024, PMID:38440125).

**Experimental treatments:** No registered clinical trials (ClinicalTrials.gov) specific to VDDR1B were identified — consistent with its extreme rarity and effective management via existing vitamin D formulations.

**Adverse events:** Because supraphysiologic vitamin D3 dosing is used, monitoring for hypercalcemia/hypercalciuria and vitamin D toxicity is an implied but not separately quantified risk in the literature reviewed.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (monogenic recessive disease); genetic counseling for consanguineous families or those with an affected child is the relevant preventive intervention.
- **Screening/early detection:** Prenatal or carrier testing could theoretically be offered in families with a known pathogenic *CYP2R1* variant, though no formal ACMG/professional-society screening recommendation specific to VDDR1B exists given its rarity.
- **Genetic counseling:** Recommended for identified families to inform recurrence risk (25% for future affected offspring of two carrier parents) and to guide early biochemical monitoring/prophylactic vitamin D3 dosing in at-risk siblings.
- **Behavioral/public health:** General population-level vitamin D sufficiency campaigns (sunlight exposure, dietary/supplement fortification) do not prevent VDDR1B itself, but adequate substrate availability mitigates severity in affected individuals and could plausibly delay/reduce clinical presentation.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring VDDR1B-equivalent disease has been reported in companion animals or wildlife (unlike some other Mendelian metabolic bone diseases with veterinary correlates). NCBITaxon:9606 (Homo sapiens) is the sole natural-disease species.
- **Orthologous gene:** Mouse *Cyp2r1* (NCBI Gene: 74790) is the well-characterized ortholog used for functional/model studies (see below); Uniprot Q6VVW9 (mouse Cyp2r1).
- **Comparative biology:** CYP2R1's role as the principal vitamin D 25-hydroxylase is evolutionarily conserved across mammals, supporting cross-species mechanistic relevance of the mouse knockout data to human pathophysiology, though as detailed below the mouse model's phenotype is notably milder than the human disease (a `HUMAN_MODEL_MISMATCH`-relevant point for dismech curation).

---

## 15. Model Organisms

**Mouse — *Cyp2r1* knockout (global):** Zhu, Ochalek, Kaufmann, Jones & DeLuca, *PNAS* 2013 (PMID:24019477), "CYP2R1 is a major, but not exclusive, contributor to 25-hydroxyvitamin D production in vivo." *Cyp2r1*⁻/⁻ mice show **>50% reduction** (not complete loss) in serum 25(OH)D3, with **unchanged serum 1,25(OH)2D3** and **no overt health/skeletal phenotype** reported in the paper — i.e., the mouse model **partially, not fully, recapitulates** the human biochemical defect and does **not** reproduce the rachitic phenotype seen in human null patients. This is an important `HUMAN_MODEL_MISMATCH`/`FAILS_TO_RECAPITULATE`-relevant finding for dismech curation: the residual 25-hydroxylation capacity is proportionally much greater in mouse than appears to be the case in the most severely affected human homozygotes (e.g., L99P homozygotes with profound, blunted-response deficiency).
- A **double knockout of *Cyp2r1* and *Cyp27a1*** (the latter encoding a mitochondrial P450 with minor 25-hydroxylase side activity) was also generated in the same study; circulating 25(OH)D3 and 1,25(OH)2D levels remained similar to the single *Cyp2r1* knockout, indicating that **additional, still-unidentified 25-hydroxylase(s)** contribute to the residual activity — an open mechanistic gap explicitly flagged by the authors and relevant for a `KNOWLEDGE_GAP` discussion node in a dismech pathophysiology model (the identity of the "other" enzyme(s) responsible for the residual ~50% activity in *Cyp2r1*-null mice remains unresolved as of the cited literature).
- **Model limitations:** The mild mouse phenotype (no overt rachitic bone disease reported) limits its use for studying skeletal/clinical endpoints of VDDR1B and suggests either species differences in the relative contribution of alternative hydroxylases, in dietary/husbandry vitamin D substrate availability, or in downstream calcium-handling compensation — none of which have been fully dissected in the literature reviewed.
- **Applications:** The knockout mouse remains the primary tool for studying CYP2R1's biochemical/enzymological role in whole-organism vitamin D activation and for testing alternative-pathway hypotheses (e.g., candidate secondary 25-hydroxylases), but is not an adequate model for the severe/complete human null phenotype or its skeletal consequences.
- **Resources:** MGI accession for *Cyp2r1* (MGI:1919338); IMPC/KOMP repositories may hold additional *Cyp2r1* allele lines beyond the specific knockout described by Zhu et al.

**In vitro models:** Heterologous expression systems (COS-7, HEK293, or yeast/insect-cell expression of recombinant CYP2R1) have been used extensively to functionally characterize individual patient variants (e.g., L99P, K242N) for residual enzymatic activity, as cited above (Thacher et al. 2015, PMID:25942481) — these represent the most direct and best-characterized "model" evidence linking specific human genotypes to loss/reduction of 25-hydroxylase catalytic function, complementing the whole-organism mouse data.

---

## Summary Table of Key Evidence

| Claim | PMID | Evidence type |
|---|---|---|
| CYP2R1 identified as key human vitamin D 25-hydroxylase; first patient variant | 15128933 (Cheng et al., PNAS 2004) | HUMAN_CLINICAL + IN_VITRO |
| Compound heterozygous splice + frameshift CYP2R1 variants, Saudi sibship | 22855339 (Al Mutair et al. 2012) | HUMAN_CLINICAL |
| L99P and K242N functional characterization, 2 Nigerian families, blunted vitamin D3 response | 25942481 (Thacher et al., JCEM 2015) | HUMAN_CLINICAL + IN_VITRO |
| CYP2R1 review of mutations causing vitamin D-deficiency rickets | 27473561 (Thacher & Levine 2017) | Review |
| 7 patients/2 families (Moroccan L99P, French indel); "rare or misdiagnosed" | 28548312 (Molin et al., JBMR 2017) | HUMAN_CLINICAL |
| 27 Saudi patients/9 families; two founder-like alleles | 34137732 (Alzahrani et al. 2021) | HUMAN_CLINICAL |
| Adult BMD preserved despite persistent 25(OH)D deficiency | 32430692 (Wiedemann et al. 2020) | HUMAN_CLINICAL |
| First Asian (Indian) case; novel frameshift variant | 38440125 (JCEM Case Reports 2024) | HUMAN_CLINICAL |
| Cyp2r1 knockout mouse; partial, not full, biochemical recapitulation | 24019477 (Zhu et al., PNAS 2013) | MODEL_ORGANISM |
| CYP2R1-vitamin D3 crystal structure | 18511070 (Strushkevich et al. 2008) | COMPUTATIONAL/structural (IN_VITRO) |

**Sources:**
- [Novel Mutation in CYP2R1 Causing Vitamin D-Dependent Rickets Type 1b (JCEM Case Reports 2024)](https://academic.oup.com/jcemcr/article/2/3/luae024/7618557)
- [OMIM #600081 – VITAMIN D HYDROXYLATION-DEFICIENT RICKETS, TYPE 1B](https://omim.org/entry/600081)
- [OMIM *608713 – CYP2R1](https://omim.org/entry/608713)
- [Vitamin D–Dependent Rickets Type 1B: A Rare Condition or a Misdiagnosed Condition? (JBMR 2017)](https://onlinelibrary.wiley.com/doi/full/10.1002/jbmr.3181)
- [25-Hydroxylase vitamin D deficiency in 27 Saudi Arabian subjects (Endocrine Connections 2021)](https://ec.bioscientifica.com/view/journals/ec/10/7/EC-21-0102.xml)
- [Genetic evidence that the human CYP2R1 enzyme is a key vitamin D 25-hydroxylase (PNAS 2004)](https://www.pnas.org/doi/10.1073/pnas.0402490101)
- [CYP2R1 is a major, but not exclusive, contributor to 25-hydroxyvitamin D production in vivo (PNAS 2013)](https://www.pnas.org/content/110/39/15650)
- [Mutation of the CYP2R1 vitamin D 25-hydroxylase in a Saudi Arabian family (2012)](https://pubmed.ncbi.nlm.nih.gov/22855339/)
- [CYP2R1 mutations causing vitamin D-deficiency rickets (review, 2017)](https://www.sciencedirect.com/science/article/abs/pii/S0960076016302138)
- [vitamin D hydroxylation-deficient rickets, type 1B – MONDO/NORD](https://rarediseases.org/mondo-disease/vitamin-d-hydroxylation-deficient-rickets-type-1b/)
- [Vitamin D Hydroxylation-Deficient Rickets, Type 1b – MalaCards](https://www.malacards.org/card/vitamin_d_hydroxylation_deficient_rickets_type_1b)
- [Structural Analysis of CYP2R1 in Complex with Vitamin D3 (J Mol Biol 2008)](https://pubmed.ncbi.nlm.nih.gov/18511070/)
- [New Variants of the CYP2R1 Gene in Individuals with Severe 25(OH)D Deficiency](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8699237/)
- [Two novel CYP2R1 mutations in a family with vitamin D-dependent rickets type 1b (2021)](https://pubmed.ncbi.nlm.nih.gov/33715104/)
- [Prolonged 25-OH Vitamin D Deficiency Does Not Impair Bone Mineral Density in Adult Patients With CYP2R1 Deficiency (Calcif Tissue Int 2020)](https://pubmed.ncbi.nlm.nih.gov/32430692/)
- [ClinVar VCV000002216 – CYP2R1 c.296T>C (p.Leu99Pro)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000002216/)
- [ClinVar VCV000977185 – CYP2R1 c.768dupT](https://www.ncbi.nlm.nih.gov/clinvar/variation/977185/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.