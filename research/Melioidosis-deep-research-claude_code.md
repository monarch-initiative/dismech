---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-08T14:30:50.655565'
end_time: '2026-08-08T14:36:17.929750'
duration_seconds: 327.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Melioidosis
  mondo_id: ''
  category: Infectious Disease
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
  num_turns: 27
  total_cost_usd: 2.182402700000001
  session_id: ff620c32-2ced-52ed-8018-b974aee9b2fc
  stop_reason: end_turn
citation_count: 62
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Melioidosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Melioidosis** covering all of the
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

# Melioidosis: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Melioidosis is a life-threatening infectious disease caused by *Burkholderia pseudomallei*, a Gram-negative, motile, facultative intracellular saprophytic bacillus that lives naturally in tropical/subtropical soil and fresh water. It is acquired via percutaneous inoculation, inhalation, or ingestion of the organism from contaminated environmental sources, and can affect virtually any organ system, ranging from localized cutaneous abscess to fulminant septic shock. Wiersinga et al. (Nat Rev Dis Primers 2018) note it is "a life-threatening infection that is estimated to account for approximately 89,000 deaths per year worldwide," with disease that "can vary greatly and may mimic those of tuberculosis or common forms of pneumonia" (Nature Reviews Disease Primers, 2018; PMID for the primer series generally cited as 29388606). A more recent mechanistic and epidemiological update is Meumann et al., *Burkholderia pseudomallei and melioidosis*, Nat Rev Microbiol 2024;22:155-169 (PMID:37749352).

**Key identifiers:**
- **MONDO:** MONDO:0017775
- **Disease Ontology:** DOID:5052
- **OMIM:** 615557 ("MELIOIDOSIS, SUSCEPTIBILITY TO" — a susceptibility-locus entry, not a Mendelian disease entry; OMIM notes host TLR/TNF variants as susceptibility modifiers, not causal mutations, since the causal agent is infectious, not genetic)
- **Orphanet:** ORPHA:31202
- **ICD-11:** 1C42 (Melioidosis)
- **ICD-10:** A24.0 (Melioidosis, general); A24.1 (Acute/fulminating melioidosis); A24.2 (Subacute and chronic melioidosis); A24.3 (Other melioidosis); A24.4 (Melioidosis, unspecified)
- **MeSH:** D008554 (Melioidosis)
- **NCBI Taxonomy (causative organism):** *Burkholderia pseudomallei*, Taxonomy ID 28450

**Synonyms/alternative names:** Whitmore's disease (after Alfred Whitmore, who first described it in Rangoon, Burma, in 1911–1912); "Nightcliff gardener's disease" (Darwin, Australia, regional term); pseudoglanders; Vietnamese time bomb / Vietnamese time-bomb disease (referring to reactivation years after exposure).

**Data source type.** Most published knowledge is derived from **aggregated disease-level clinical cohorts and registries** (e.g., the 20+ year Darwin Prospective Melioidosis Study in Australia's Northern Territory, the Sunpasitthiprapa Hospital cohort in Thailand, and India's national melioidosis case series), rather than individual-EHR mining — reflecting its status as an endemic infectious disease of low/middle-income tropical regions with limited EHR infrastructure. Global burden modeling (Limmathurotsakul et al. 2016; Birnie et al. 2019) is ecological/geospatial, combining environmental suitability modeling with reported incidence.

---

## 2. Etiology

### Disease Causal Factor
Melioidosis is a **purely infectious disease** — there is no genetic or purely mechanistic causal pathway independent of infection by *B. pseudomallei*. Transmission routes are:
- **Percutaneous inoculation** — the dominant route in most series — through skin abrasions/wounds contacting contaminated soil or water.
- **Inhalation** of aerosolized bacteria/contaminated dust, notably during severe weather events (typhoons, monsoons) — associated with more severe, rapidly fulminant pneumonic disease.
- **Ingestion** of contaminated water — implicated especially in pediatric suppurative parotitis in Thailand.
- Rare **nosocomial**, **laboratory-acquired**, and **person-to-person** transmission (the latter is exceptionally rare; melioidosis is fundamentally a **sapronosis**, not a classic zoonosis — "both animals and humans can independently be infected by this endemic soil and water bacterium" rather than transmitting to one another) (Merck Veterinary Manual; *Aust Vet J* 2025 review).

### Risk Factors

**Genetic/host risk factors** (susceptibility loci, not causal mutations):
- **TLR4 region variants**: TLR4 −1196C>T associated with *protection*; other TLR4-region SNPs associated with susceptibility (Genes Immun 2011; PMID for the TLR4 study is commonly cited as West et al., PMID 21430785).
- **TLR5 R392X nonsense polymorphism**: paradoxically *protective* against in-hospital death and organ failure in a cohort of ~600 Thai patients — "hypofunctional TLR5 was associated with decreased organ failure and improved survival," though the same allele increases susceptibility to invasive aspergillosis and Legionnaires' disease (tradeoff/pleiotropy).
- **TNF and NOD2 polymorphisms** linked to disease severity.
- Cellular GWAS approaches (lymphoblastoid cell lines infected with *B. pseudomallei*) are being used to identify additional host regulators (grant: NIH R21-AI133171, T. West).
- **HLA associations** are less well characterized than for many other infections; the strongest and most replicated genetic signal remains the TLR/TNF innate-immunity axis rather than an adaptive-immunity HLA locus.

**Environmental/behavioral/comorbidity risk factors** (these dominate over genetic risk in melioidosis, unusually for an infectious disease):
- **Diabetes mellitus (mostly type 2)** — the single strongest risk factor; diabetic patients have **~3-fold to 12-fold increased risk** across studies (meta-analysis RR 3.40, 95% CI 2.92–3.87; Nat Rev Dis Primers cites up to 12-fold), and diabetes is present in roughly **half of all culture-confirmed cases** (51% in one 321-patient cohort).
- **Hazardous alcohol use** — present in ~32% of a representative cohort.
- **Chronic kidney disease** — ~13% of cases; mechanistically, "in the milieu of advanced chronic kidney disease, neutrophils display impaired chemotaxis, reduced phagocytic ability, decreased generation of reactive oxygen intermediates during oxidative burst."
- **Chronic lung disease.**
- **Thalassemia / iron-overload states** — "conditions with increased iron stores, such as thalassemia, are considered to increase the risk to acquire melioidosis," and *B. pseudomallei* actively "modulates host iron homeostasis to facilitate iron availability and intracellular survival" (PLOS NTD, PMID 29228001).
- **Corticosteroid/immunosuppressive therapy.**
- **Occupational/behavioral exposure**: rice farming, gardening, other soil/water contact occupations; agricultural, laboratory, healthcare, veterinary, and construction workers; drinking untreated water; open wounds contaminated with soil/water; outdoor exposure during/after severe weather (typhoons increase incidence because "the bacteria would spread more easily with strong wind and storms").
- **Male sex** and **older age (>45 years)** are consistently overrepresented in adult cohorts.
- Notably, **HIV/immunosuppression from HIV is not a major reported risk factor** in most endemic-region series (in contrast to many other opportunistic infections), though this varies by cohort.

### Protective Factors
- The **TLR5 R392X** and **TLR4 −1196C>T** variants noted above.
- No validated dietary/lifestyle protective factor is established; primary prevention (below) centers on exposure avoidance rather than an identified protective exposure.

### Gene-Environment Interactions
The dominant G×E pattern in melioidosis is host **metabolic/iron dysregulation (diabetes, thalassemia) interacting with environmental exposure dose and route**: hyperglycemia impairs neutrophil function and intracellular bacterial killing, so an environmental inoculum that a healthy host would clear establishes invasive infection in a diabetic host. Innate-immunity SNPs (TLR4/TLR5) modulate the inflammatory response magnitude once infection is established, influencing whether an exposure event progresses to septic shock versus a milder/localized course.

---

## 3. Phenotypes

Melioidosis has an extraordinarily protean presentation ("the great mimicker" in the literature), spanning localized cutaneous disease to fulminant multi-organ septic shock. Of 624 culture-confirmed patients in one large series, **51% presented with pneumonia as the primary diagnosis** — the single most common organ manifestation.

### Symptoms/Clinical Signs (Phenotype type: symptom/sign)
| Phenotype | Suggested HP term |
|---|---|
| Fever | HP:0001945 |
| Sepsis | HP:0100806 |
| Septic shock / Shock | HP:0031273 |
| Acute infectious pneumonia | HP:0200114 |
| Lung abscess | HP:0031367 |
| Liver abscess | HP:0410033 (or "Hepatic abscess") |
| Splenic abscess | HP:0100804 (Abnormality of the spleen) / splenic abscess (specific term may require search) |
| Cutaneous abscess | HP:0031292 |
| Cellulitis | HP:0100658 |
| Osteomyelitis (incl. foot osteomyelitis) | HP:0002754 |
| Septic arthritis | HP:0002718 |
| Parotitis / suppurative parotitis (pediatric hallmark, Thailand) | HP:0100786 (Parotitis) |
| Prostatitis | related genitourinary abnormality term |
| Brain abscess | HP:0007183 |
| Encephalitis / rhombencephalitis / brainstem encephalitis | HP:0002383 (Encephalitis) |
| Hepatitis | HP:0012115 |
| Lymphadenitis | HP:0100827 (or general lymphadenopathy term) |
| Cough | HP:0012735 |
| Headache | HP:0002315 |
| Myalgia | HP:0003326 |
| Arthralgia | HP:0002829 |

### Phenotype Characteristics

- **Age of onset**: Any age; adult predominance overall, but with distinct pediatric syndrome (below). In endemic zones, cases cluster in the wet/monsoon season — 80% of pediatric Australian cases presented during the wet season.
- **Severity**: Highly variable — from indolent chronic ulcerative skin disease to fulminant septic shock with death within 24–48 hours.
- **Progression pattern**: **Acute** presentation in ~88% of cases; **chronic** (symptoms >2 months, often mimicking tuberculosis) in ~22% — note these can overlap/co-occur in the literature's classification. Notorious for **relapse** after treatment if eradication-phase therapy is inadequate.
- **Frequency/regional variation** (a distinctive feature of melioidosis phenotype epidemiology — presentation differs qualitatively by geography):
  - **Northern Australia (adults)**: pneumonia is the most common organ presentation (~51% in the large series above); genitourinary involvement (especially prostatic abscess) more prominent than in SE Asia.
  - **Thailand (adults)**: bacteremia in ~64%, pneumonia ~62%, internal-organ abscess ~49%, soft tissue ~22%, joint ~7%.
  - **Northern Australia (children)**: cutaneous manifestation is the most common presentation (60% vs. 13% in adults); bacteremia less common than in adults (16% vs. 59%); brainstem encephalitis occurred in 3/45 children in a 24-year Northern Territory series (*Clin Infect Dis* 2015;60:21, PMID 25234519).
  - **Thailand (children)**: acute suppurative parotitis in ~one-third of pediatric cases, plus liver abscess, likely from ingestion of contaminated water.
- **Neurological melioidosis** (an important, distinct sub-phenotype): unusual overall but a recognized encephalomyelitis syndrome with variable brainstem, cerebellar, and spinal cord involvement. Brainstem (34%) and frontal lobe (34%) are the most affected locations; rim-enhancing lesions on contrast MRI in 78%; CSF shows mononuclear pleocytosis (64%), elevated protein (93%), normal glucose (66%); mortality ~20% (systematic review, *PLoS Negl Trop Dis* 2019, PMID 30870428; and Meumann et al., *Clin Infect Dis* 2024, PMID 37788335, on the bimABm allele's influence on CNS presentation/outcome).

### Quality of Life Impact
Direct disease-specific QoL instrument data (EQ-5D/SF-36) for melioidosis specifically was not identified in this search; QoL burden is inferred indirectly from the very high DALY estimates (see Epidemiology, below) driven by mortality and by long courses of IV/oral antibiotic therapy (up to 20 weeks total), amputation/debridement for severe cutaneous/osteoarticular disease, and neurological sequelae after CNS melioidosis.

---

## 4. Genetic/Molecular Information

Melioidosis is **not a Mendelian genetic disease**; there is no single causal gene. The "genetic" dimension relevant to a knowledge-base entry is (a) host susceptibility variants and (b) pathogen virulence-factor genetics.

### Host Susceptibility Variants (not disease-causing, but modify risk/severity)
- **TLR4** (HGNC:11850) region SNPs, including −1196C>T (protective) and other TLR4-region variants (susceptibility-associated) — Genes Immun 2011.
- **TLR5** (HGNC:11851) R392X nonsense polymorphism — protective against organ failure/death, at the cost of increased susceptibility to *Aspergillus* and *Legionella*.
- **TLR1** and **TLR2** coding variants — studied but a large multicenter cohort found *no* association between TLR1/TLR5 coding variants and mortality (PMC11066355), illustrating cohort-dependent heterogeneity in this literature.
- **TNF** (HGNC:11892) promoter polymorphisms — linked to severity.
- **NOD2** (HGNC:5331) polymorphisms — linked to severity.
- These are best modeled in dismech schema terms as **susceptibility/modifier genetic context** (`relationship_type: SUSCEPTIBILITY` or `MODIFIER`), not causal, consistent with OMIM's own framing of entry 615557 as "MELIOIDOSIS, SUSCEPTIBILITY TO."

### Variant Classification / Population Frequency
Because these are common regulatory/coding SNPs in innate-immunity genes rather than rare Mendelian variants, ACMG pathogenicity classification, gnomAD rare-variant framing, and somatic/germline distinctions are not directly applicable in the usual dismech sense — allele frequencies for these SNPs should instead be sourced from population-genetics/GWAS literature (dbSNP/1000 Genomes) if precise curation is required.

### Pathogen Genetics (arguably more central to "genetic/molecular information" for an infectious disease entry)
- ***B. pseudomallei*** genome: two chromosomes (~7.2 Mb total), notable for encoding **three Type III Secretion Systems (T3SS-1, -2, -3)** and **six Type VI Secretion Systems**. T3SS-3 (the *bsa* locus, homologous to *Salmonella* SPI-1-type systems) is the one required for pathogenesis in mammals.
- **T3SS-3 regulatory hierarchy**: `bspR` (BPSL1105) → `bprP` (BPSS1553) → `bsaN`/`bicA` (BPSS1546/BPSS1533) → effector operons `bopC`, `bopE`, `bopA`, and `bapA/bapB/bapC` (organized BPSS1516–BPSS1552).
- **Key effector proteins**: **BopE** (a Rho-GTPase-mimicking GEF that promotes actin-dependent invasion and, per recent work, suppresses the Rab32-dependent host defense pathway — *mSphere* 2024); **BopA** (mediates evasion of LC3-associated phagocytosis/autophagy; *PMC3055895*); **BipC** (actin modulation and translocation).
- **Capsular polysaccharide loci** (at least two of four described polysaccharide structures contribute to virulence — Type I O-PS is implicated in serum resistance/anti-phagocytosis).
- **Quorum sensing**: three acyl-homoserine-lactone (AHL) synthase genes (*bpsI1*, *bpsI2*, *bpsI3*) plus five regulator genes; principal AHLs are N-octanoyl-HSL and N-(3-hydroxy-decanoyl)-HSL; quorum sensing negatively regulates multinucleate giant cell formation during intracellular growth.
- **bimA** gene (actin-based motility, VirG/BimA family) — the **bimABm allele** specifically has been shown to influence CNS presentation and outcome of neurological melioidosis (*Clin Infect Dis* 2024, PMID 37788335).

### Functional Consequences / Mechanistic Framing for dismech
For a dismech entry, host TLR4/TLR5/TNF/NOD2 variants map cleanly to `GeneticContext.functional_impact_category` (e.g., TLR5 R392X = truncating/`LOSS_OF_FUNCTION` variant with a paradoxically protective phenotype), while the pathogen virulence apparatus (T3SS-3, quorum sensing, capsule) is best modeled as `biological_processes`/`molecular_functions` on pathophysiology nodes (see Mechanism section) rather than as host genetic context, since it is bacterial rather than host biology.

### Epigenetics / Chromosomal Abnormalities
No epigenetic or chromosomal-abnormality mechanism specific to melioidosis was identified in this search; this section is not applicable beyond the innate-immune SNP framework above.

---

## 5. Environmental Information

- **Primary environmental reservoir**: *B. pseudomallei* is a **saprophytic soil and freshwater organism**, endemic in a band across tropical/subtropical latitudes, especially Southeast Asia (Thailand, especially the northeast; Malaysia; Singapore; Vietnam; Laos; Cambodia; Myanmar) and northern Australia, with increasing recognition in South Asia (India — "highest total burden," 1.6 million DALYs), sub-Saharan Africa, and parts of the Americas.
- **Environmental exposure routes**: contact with contaminated soil/mud/surface water via skin abrasions; inhalation of aerosolized soil dust or water droplets, particularly during severe weather (typhoons, monsoon storms — "infection cases are more common after typhoons or storms"); ingestion of contaminated (especially untreated) water.
- **Occupational/behavioral exposures**: rice-paddy farming, gardening, other agriculture, construction/soil excavation, veterinary work, laboratory work with the organism (BSL-3 required for virulent strains).
- **Climate change and epidemiological transition**: emerging literature (*PMC10128909*, "Drivers of melioidosis endemicity: epidemiological transition, zoonosis, and climate change") links expanding endemic range and case counts to climate-driven changes in soil/water ecology and extreme-weather frequency.
- **Suggested ECTO term**: exposure to contaminated soil/water (an ECTO term analogous to other soil/water-sapronosis exposures used elsewhere in dismech, e.g. the arsenic-water exposure pattern) — exact ECTO CURIE should be verified via OAK lookup at curation time.
- **Infectious agent**: *Burkholderia pseudomallei* (NCBI Taxon:28450), Gram-negative bacillus, family Burkholderiaceae. Recognized biothreat status: **CDC Tier 1 Select Agent** and a **Category B, Tier-1 biothreat agent**, owing to environmental persistence, aerosol infectivity, and intrinsic resistance to many first-line antibiotics.

---

## 6. Mechanism / Pathophysiology

### Overall Causal Chain
Environmental inoculation (percutaneous/inhalational/ingestion) → local bacterial adherence and invasion of host cells (phagocytic and non-phagocytic) → phagosomal/endosomal escape mediated by T3SS-3 → intracellular replication and cell-to-cell spread via actin-based motility → host innate immune sensing (TLR4/TLR5, inflammasome) → either **effective early containment** (localized abscess, chronic granulomatous disease) or **immune dysregulation and systemic dissemination** (bacteremia, septic shock, multi-organ abscess formation) depending on host factors (diabetes, iron overload, TLR/TNF genotype) and bacterial inoculum/virulence factors.

### Molecular Pathways / Cellular Processes
1. **Adhesion and invasion**: *B. pseudomallei* adheres to and invades both phagocytic (macrophages, neutrophils) and non-phagocytic cells (epithelial cells, fibroblasts) using flagella and adhesins.
2. **T3SS-3-mediated vacuolar escape**: Following endocytosis/phagocytosis, T3SS-3 (bsa locus) delivers effectors (BopE, BipD, BipC) that trigger actin rearrangement and disrupt the phagosomal membrane, allowing bacterial escape into the cytosol before lysosomal fusion — "T3SS-3 mutants exhibit delayed vacuolar escape phenotypes" (*Infect Immun* 2008, PMID 18443088).
3. **Autophagy evasion**: BopA disrupts LC3-associated phagocytosis (a form of xenophagy); *bopA* mutants show increased LC3 co-localization and reduced intracellular survival (PMC3055895).
4. **Actin-based intracellular/intercellular motility**: BimA nucleates host actin at one bacterial pole, propelling the organism through the cytoplasm and into adjacent cells, producing characteristic **multinucleated giant cells (MNGCs)** via cell-cell fusion — a histopathological hallmark. Quorum sensing negatively regulates MNGC formation (PMC3660431).
5. **Inflammasome activation**: Cytosolic *B. pseudomallei* activates the **NLRC4 inflammasome** early in macrophage infection (caspase-1-dependent, NLRC4-dependent), transitioning to **NLRP3-dependent, NLRC4-independent** activation at later time points, producing IL-1β/IL-18 and **pyroptotic** macrophage death (*PLoS Pathog* 2014, PMID 24626296). A non-canonical **caspase-11** pathway in lung epithelial cells drives protective epithelial pyroptosis distinct from macrophage caspase-1-mediated pyroptosis (*PLoS Pathog* 2018, "Caspase-11-dependent pyroptosis of lung epithelial cells protects from melioidosis while caspase-1 mediates macrophage pyroptosis and production of IL-18").
6. **Systemic cytokine response**: Severe/septic melioidosis is characterized by a **Th1-polarized cytokine storm** — elevated IFN-γ and the IFN-γ-inducing cytokines IL-18, IL-12, IL-15, alongside TNF-α and IL-6; **APACHE II score together with IL-6 or IL-10 concentration are independent predictors of mortality** (PMID 10669346).
7. **Iron acquisition/host iron manipulation**: The organism actively modulates host iron homeostasis to increase iron availability for intracellular survival (*PLoS Negl Trop Dis* 2018, PMID 29228001) — mechanistically linking the thalassemia/iron-overload risk factor above to bacterial nutritional virulence.
8. **Capsule- and LPS-mediated serum resistance**: Type I capsular O-polysaccharide confers resistance to complement-mediated killing and phagocytosis, permitting bacteremic dissemination.
9. **Quorum sensing (AHL-mediated)**: Coordinates biofilm formation, virulence factor expression, and (as above) restrains excessive giant-cell formation, implying a role in balancing acute cytotoxicity against sustained chronic/latent infection.

### Cell Types Involved (suggested CL terms)
- Macrophage (CL:0000235) — primary intracellular replicative niche and site of pyroptosis.
- Neutrophil (CL:0000775) — first responder, impaired function in diabetes/CKD hosts.
- Epithelial cell, respiratory (CL:0000082 or more specific alveolar epithelial terms) — site of caspase-11-dependent protective pyroptosis.
- Dendritic cell (CL:0000451) — antigen presentation, Th1 polarization.
- Fibroblast (CL:0000057) — non-phagocytic host cell also invaded.

### Biological Processes (suggested GO terms)
- Phagocytosis (GO:0006909)
- Actin filament-based movement / actin-based cell motility (GO:0030036)
- Inflammasome complex assembly (GO:0131015)
- Pyroptosis (GO:0070269)
- Positive regulation of interferon-gamma production (GO:0032729)
- Response to lipopolysaccharide (GO:0032496)
- Iron ion homeostasis (GO:0055072)
- Quorum sensing (GO:0009372)

### Tissue Damage Mechanisms
Direct cytotoxicity from intracellular replication and pyroptotic cell death; abscess formation via neutrophilic/granulomatous containment attempts; multinucleated giant cell formation as a histopathological correlate of cell-to-cell spread; septic shock physiology (vasodilation, capillary leak, disseminated intravascular coagulation in the most severe cases) in bacteremic disease.

### Molecular Profiling
Specific transcriptomic/proteomic/metabolomic datasets for human melioidosis were not deeply catalogued in this search pass; the *PepSeq* multiplexed antigen-discovery platform (*Front Immunol* 2025) represents a relevant proteomics-adjacent effort for vaccine/diagnostic antigen discovery.

---

## 7. Anatomical Structures Affected

- **Organ level (primary)**: Lung (pneumonia — most common single-organ presentation), skin/soft tissue (cellulitis, cutaneous abscess), liver (abscess), spleen (abscess), prostate (prostatic abscess — a distinctive and diagnostically useful finding, more common in Australian cohorts), kidney (renal abscess), bone/joint (osteomyelitis, septic arthritis), parotid gland (suppurative parotitis, especially pediatric Thailand), brain/CNS (abscess, brainstem encephalitis/encephalomyelitis), lymph nodes (lymphadenitis).
- **Body systems involved**: Respiratory, integumentary, hepatobiliary, genitourinary, musculoskeletal, central nervous, and (in severe disease) the vascular/hematologic system via sepsis/DIC.
- **Suggested UBERON terms**: lung (UBERON:0002048), liver (UBERON:0002107), spleen (UBERON:0002106), prostate gland (UBERON:0002367), parotid gland (UBERON:0001832), brain stem (UBERON:0002298), skin of body (UBERON:0002097), bone tissue (UBERON:0002481).
- **Tissue/cell level**: Alveolar epithelium and macrophages (pulmonary disease); hepatic/splenic parenchyma with microabscess formation; synovium (septic arthritis); bone marrow/cortical bone (osteomyelitis).
- **Subcellular level (GO Cellular Component)**: phagosome (GO:0045335), cytosol (GO:0005829, site of intracellular replication post-vacuolar escape), inflammasome complex (GO:0061702).
- **Localization/laterality**: Generally not laterality-specific in the classic congenital-anomaly sense; CNS disease has a distinctive predilection for the brainstem/rhombencephalon.

---

## 8. Temporal Development

- **Onset**: Any age; incubation period estimated at **1–21 days** from inoculating injury in most acute presentations, though this is highly variable with inoculum/route/host factors.
- **Latency controversy — the "Vietnamese time bomb"**: Melioidosis acquired notoriety during the Vietnam War (an estimated 225,000 U.S. personnel potentially exposed; 343 confirmed cases in U.S. troops by 1973) for apparently reactivating **years to decades** after the exposure ended, with case reports of activation after 18 years (Vietnam veteran) and 28 years (WWII veteran), and extreme outlier claims of latency up to 62 years. However, a 2024 reassessment (*Am J Trop Med Hyg* 2024;111:156, PMID 38806042) concludes the "Time Bomb" phenomenon has largely **not materialized** at the scale predicted, and argues many historically reported "reactivation from latency" cases more likely represent **undiagnosed chronic, relapsing-remitting melioidosis** rather than truly dormant, asymptomatic infection.
- **Progression/course pattern**: Acute fulminant presentation (~88% of cases) with rapid progression to sepsis/septic shock over hours to days, vs. chronic presentation (~22%, symptoms >2 months) mimicking tuberculosis with indolent pulmonary or cutaneous disease.
- **Relapse**: A defining clinical feature — relapse after treatment is common if eradication-phase (oral) antibiotic therapy is inadequate in dose or duration; optimized co-trimoxazole regimens (1920 mg twice daily) reduce relapse to as low as ~3.2% monotherapy / 4.6% combination with doxycycline, versus substantially higher rates historically with shorter or lower-dose regimens.
- **Critical periods for intervention**: Early recognition and initiation of appropriate IV antibiotics (ceftazidime or meropenem) within the acute phase is the single greatest modifiable determinant of survival, since delayed diagnosis (a common failure mode given the nonspecific presentation) drives the high case-fatality rates seen outside specialist centers.

---

## 9. Inheritance and Population

Melioidosis is an **acquired infectious disease with no Mendelian inheritance pattern**; the OMIM entry (615557) explicitly frames genetics as *susceptibility*, not inheritance of the disease itself. Penetrance/expressivity/anticipation/germline mosaicism/founder-effect/carrier-frequency concepts (as classically defined for monogenic disease) are not applicable; "carrier frequency" instead corresponds to population allele frequency of the TLR4/TLR5/TNF/NOD2 susceptibility SNPs discussed in Section 4.

### Epidemiology
- **Global burden (2015 estimate, Limmathurotsakul et al. 2016; refined by Birnie et al., Lancet Infect Dis 2019, PMID 31285144)**: an estimated **165,000 cases and ~89,000 deaths per year worldwide** — comparable in mortality burden to measles (~95,600 deaths/year) and exceeding leptospirosis (~50,000/year) and dengue (~12,500/year).
- **Regional burden**: The WHO South-East Asia region accounts for >60% of the estimated global burden; **India carries the highest total burden**, estimated at 1.6 million DALYs.
- **Incidence**: Median annual incidence across endemic-area studies is **20.5 cases per 100,000 population**; the highest reported subgroup incidence is in **Indigenous Australians, at 103.6 per 100,000 in 2011–12**.
- **Mortality rate**: Highly setting-dependent, ranging **9%–70%** globally; state-of-the-art care (early diagnosis, ICU support, appropriate antibiotics) can reduce mortality to <10%, whereas resource-limited settings without ceftazidime/meropenem access see mortality >40%.

### Population Demographics
- **Sex ratio**: Male predominance is consistently reported across adult endemic-area cohorts (reflecting occupational/behavioral exposure patterns — agriculture, outdoor labor).
- **Age distribution**: Adult predominance, typically >45 years, correlating with peak prevalence of diabetes/comorbidities; pediatric cases represent a minority (~5% in the 24-year Northern Territory series) but have a distinct clinical phenotype (Section 3).
- **Geographic distribution**: Core endemic "melioidosis belt" — Southeast Asia (Thailand, especially Ubon Ratchathani/northeast region; Malaysia; Singapore; Vietnam; Laos; Cambodia; Myanmar) and northern Australia (Darwin/Northern Territory, Far North Queensland); increasingly recognized in South Asia (India), sub-Saharan Africa, and parts of Central/South America and the Caribbean as surveillance and diagnostic capacity improve; environmental suitability modeling suggests substantial under-recognition in Africa.

---

## 10. Diagnostics

### Clinical/Laboratory Tests
- **Culture (gold standard)**: Blood, sputum, urine, pus/wound swabs, or throat swab cultured on selective media — **Ashdown's agar** (Trypticase soy agar + 4% glycerol, neutral red indicator, crystal violet, gentamicin as selective agents) is the classic selective medium enabling identification from non-sterile sites. **Blood culture sensitivity is only ~60%** in latent-class diagnostic-accuracy modeling, meaning a negative blood culture does not exclude disease.
- **Molecular (PCR)**: Real-time PCR targeting the **TTS1 (T3SS-1)** locus for direct detection from clinical specimens; automated molecular platforms are now being evaluated for point-of-care/near-patient use.
- **Serology**: IgG/IgM ELISA and polysaccharide-based latex agglutination assays exist but "serological diagnosis of melioidosis remains challenging" due to background seropositivity in endemic populations and variable in-house/commercial assay performance; primarily useful as an adjunct, not a stand-alone diagnostic.
- **Environmental/soil detection**: Culture- and PCR-based soil testing methods are used for environmental surveillance/source-tracing in endemic regions.

### Genetic Testing
Not applicable in the conventional sense (no causal human gene); TLR4/TLR5/TNF/NOD2 genotyping is a research tool for risk/prognosis stratification, not a clinical diagnostic test.

### Imaging
CT/MRI for organ abscess detection (liver, spleen, prostate, brain); **contrast-enhanced MRI with T2-weighted sequences is the modality of choice for suspected CNS melioidosis**, showing hyperintense brainstem/frontal lobe lesions with a characteristic rim-enhancing pattern in 78% of cases.

### Clinical Criteria / Differential Diagnosis
No single validated clinical scoring system for diagnosis exists (diagnosis is microbiological); the key clinical challenge is that melioidosis mimics **tuberculosis** (chronic pulmonary cavitary disease), **community-acquired pneumonia**, and **other causes of multi-organ abscess/sepsis**, making a high index of suspicion in returning travelers or residents of endemic areas essential.

### Screening
No population-level screening program exists; risk-based prevention counseling (below) substitutes for screening in high-risk groups (diabetics in endemic areas).

---

## 11. Outcome/Prognosis

- **Mortality**: 9–70% depending on setting; <10% achievable with optimal care; historically cited overall figure "up to 40%."
- **Prognostic factors/biomarkers**: **APACHE II score**, **IL-6** and **IL-10** plasma concentrations (and their ratios to TNF-α), plasma lactate, presence of bacteremia/septicemia, pneumonia as the presenting focus, older age, elevated serum urea and bilirubin, low lymphocyte count, low bicarbonate, and low serum albumin are each independently associated with mortality (PMID 10669346 and related cohort literature).
- **CNS melioidosis-specific mortality**: ~20% in the systematic IPD review (PMID 30870428).
- **Relapse as a distinct "morbidity" outcome**: 3–5% with modern optimized eradication-phase co-trimoxazole regimens; historically higher with suboptimal dosing/duration — relapse functions almost as a second disease phase in the natural history rather than a rare complication.
- **Recovery potential**: Full recovery is achievable with prompt, adequate combined acute-phase IV and eradication-phase oral therapy; delayed or inadequate treatment is associated with both higher acute mortality and higher relapse-driven long-term morbidity.
- **Complications**: Amputation/disfigurement from severe cutaneous/osteoarticular disease; neurological sequelae from CNS involvement (cranial nerve deficits from brainstem lesions); chronic organ abscess recurrence.

---

## 12. Treatment

Melioidosis treatment follows a well-established **two-phase regimen** (summarized in the LSHTM review "Treatment and prophylaxis of melioidosis," PMC4236584, and updated network meta-analyses).

### Acute (Intensive) Phase — parenteral, ≥10–14 days (often 2–4 weeks)
- **Ceftazidime** 2 g IV every 8 hours (40 mg/kg/dose in children) — mainstay first-line agent.
  - Suggested NCIT: `NCIT:C15986` (Pharmacotherapy) + `therapeutic_agent` CHEBI term for ceftazidime (CHEBI:471415 or similar — verify via OAK).
- **Meropenem** 1 g IV every 8 hours (25 mg/kg) — used preferentially in severe/septic-shock presentations or as second-line after treatment failure; carbapenems reserved for the most severe infections.
- **Co-amoxiclav (amoxicillin-clavulanate)** — second-line/alternative acute-phase agent, particularly in pregnancy or where cephalosporins/carbapenems are unavailable.

### Eradication Phase — oral, total antibiotic course to ~20 weeks
- **Co-trimoxazole (trimethoprim-sulfamethoxazole)** — preferred eradication-phase agent; optimal dosing (1920 mg twice daily in adults) minimizes both relapse and mortality; typical duration 3–6 months (minimum duration for low relapse risk ≈ 3 months).
  - Suggested NCIT: `NCIT:C15986` (Pharmacotherapy) + CHEBI therapeutic_agent for co-trimoxazole components (sulfamethoxazole CHEBI:9328, trimethoprim CHEBI:9679).
- **Doxycycline** as an alternative or combination eradication agent, though co-trimoxazole monotherapy shows lower relapse rates than combination regimens in recent network meta-analysis (*PLoS Negl Trop Dis* 2023, PMID 37585472).
- **Co-amoxiclav** as an alternative eradication-phase drug where co-trimoxazole is contraindicated (e.g., sulfa allergy, pregnancy, renal impairment).

### Surgical/Interventional
Drainage of large abscesses (splenic, hepatic, prostatic, soft-tissue) is often required as an adjunct to antibiotics; debridement for severe cutaneous/soft-tissue disease.

### Supportive Care
ICU-level sepsis management (fluid resuscitation, vasopressor support, mechanical ventilation) is central to reducing mortality in septic-shock presentations; this is reflected in the strong prognostic value of APACHE II scoring.

### Experimental/Investigational
No approved vaccine or targeted immunotherapy exists yet; treatment remains purely antimicrobial + supportive.

### Treatment Outcomes / Pharmacogenomics
Direct pharmacogenomic (drug-metabolism-variant) data specific to melioidosis antimicrobial dosing was not identified in this search; dosing adjustments are driven by renal function (relevant given CKD is itself a risk factor) rather than germline pharmacogenomic variants.

---

## 13. Prevention

### Primary Prevention
- **Exposure avoidance**: protective clothing (boots, gloves) for occupational soil/water contact in endemic areas; avoidance of soil/water exposure during and after severe weather events; immediate and thorough cleaning of any soil/water-contaminated skin wounds.
- **Water safety**: avoiding consumption of untreated water; ensuring safe drinking water infrastructure in endemic communities.
- **Targeted diabetic prevention programs**: The **PREMEL trial** (stepped-wedge cluster-randomized controlled trial) tested a multifaceted prevention program specifically for diabetics in an endemic area, reflecting the recognition that diabetes-focused prevention messaging is a rational primary-prevention strategy given the outsized attributable risk of diabetes.
- **No vaccine currently licensed** (see below).

### Secondary Prevention / Screening
No population-based screening program for melioidosis exists (unlike genetic or cancer screening); the closest analogue is targeted health education for identified high-risk groups (diabetics, agricultural workers) in endemic regions, and clinician education to raise diagnostic suspicion (reducing time-to-treatment, which is itself a major secondary-prevention lever against mortality).

### Tertiary Prevention
Adequate-duration eradication-phase antibiotics (above) to prevent relapse constitutes the primary tertiary-prevention intervention in this disease.

### Vaccine Development (active area, no licensed product as of 2025–2026)
- **Leading subunit candidate**: **CPS-CRM197/Hcp1** glycoconjugate (capsular polysaccharide conjugated to CRM197 carrier, plus Hcp1 protein antigen), developed at University of Nevada, Reno, with a planned/ongoing **Phase I trial in Oxford, UK**, in ~36 healthy adult volunteers (with and without diabetes), with a planned Phase 1b extension in Ubon Ratchathani, Thailand.
- A second promising candidate emerged from a multi-institution collaboration (Tulane University, Northern Arizona University, UC Irvine, Charles Darwin University), reported to show preclinical promise (late-2025 press coverage).
- **PepSeq antigen-discovery platform** (*Front Immunol* 2025) is being used for rational antigen selection for next-generation candidates.
- Stakeholder-attitude research in Thailand (Ubon Ratchathani) has specifically assessed community and clinician readiness for future melioidosis vaccine trials (PMC10646340).
- An active observational natural-history study (**NCT06089668**, "An Observational Study to Evaluate Clinical Characteristics of Adult Patients With Suspected or Confirmed Melioidosis") is ongoing to characterize the modern clinical spectrum, likely to inform future trial endpoints.

### Public Health / Biosecurity
Because *B. pseudomallei* is a **CDC Tier 1 Select Agent / Category B biothreat agent**, public health prevention also intersects with biosecurity: laboratory-acquired infection monitoring programs exist for occupational exposures (PMID 36776750), and BSL-3 containment is mandated for research with virulent strains.

---

## 14. Other Species / Natural Disease

- **Taxonomy of causative organism**: *Burkholderia pseudomallei* (NCBI Taxon:28450).
- **Naturally susceptible species**: Melioidosis occurs naturally and commonly in **sheep, goats, and pigs** (the three most commonly affected livestock species); also reported in cattle, buffalo, horses, mules, deer, camels, alpacas, dogs, cats, dolphins, wallabies, koalas, nonhuman primates, birds, tropical fish, and reptiles (Merck Veterinary Manual; *Aust Vet J* 2025 companion-animal case series, PMID pending/DOI 10.1111/avj.70097 — 45 Australian cases: 24 dogs, 21 cats, 1997–2025).
- **Species-specific presentation**: In **goats**, mastitis or pneumonia is most common, with aortic aneurysm also reported; in **sheep**, respiratory tract involvement predominates (fever, severe cough, respiratory distress, mucopurulent nasal/ocular discharge). Sheep and goats' particular susceptibility drives the requirement for **pasteurization of tropical commercial goat's milk**.
- **Veterinary/One Health relevance**: A 2025 IJID One Health review frames melioidosis explicitly as a "One Health" issue given shared environmental exposure across species (*IJID One Health* 2025, S2949-9151(25)00040-X).
- **Transmission mode across species**: Infection is **sapronotic** (environmental-source-driven) rather than classically zoonotic — animal-to-human and human-to-human transmission are both extremely rare; each host species acquires infection independently from the shared soil/water reservoir. This is an important point for accurate dismech curation: melioidosis should not be modeled with an animal-to-human transmission edge, but rather with parallel independent-exposure edges from a shared environmental reservoir.
- **Comparative pathology**: The multinucleated giant cell / actin-based intracellular motility mechanism (Section 6) is conserved across the mammalian hosts studied (mice, hamsters, and natural livestock/companion-animal infection), supporting cross-species mechanistic conservation despite phenotypic (organ-tropism) variation.

---

## 15. Model Organisms

### Mouse Models (the dominant experimental system)
- **BALB/c mice** — highly susceptible; recapitulate **acute human melioidosis**: rapidly progressive bacteremia leading to death by ~96 hours post-infection; LD50 as low as **4 organisms**.
- **C57BL/6 mice** — relatively resistant; recapitulate **chronic human melioidosis**: typically remain asymptomatic for up to 6 weeks post-infection; LD50 ≈ **2.5 × 10⁴ organisms**. Peritoneal exudate cells (PEC) from C57BL/6 mice show greater microbicidal efficiency against *B. pseudomallei* than BALB/c PECs, and resistance is proposed to have "a genetic basis," making this strain pair a classic acute-vs-chronic comparative model (*Immunol Cell Biol* 1998, PMID 9600859; and follow-up characterization studies PMC5325312, PMC3123849).
- **Low-dose aerosol C57BL/6 exposure** specifically models **chronic human melioidosis** (PMC3123849), useful for studying the latency/chronicity question raised in Section 8.
- Sex and age significantly modulate outcome in these models (PMC7168040, "The Impact of Age and Sex on Mouse Models of Melioidosis") — an important covariate for translational interpretation, and a candidate `HUMAN_MODEL_MISMATCH` consideration if mouse-model conclusions about sex/age effects are extrapolated directly to the strongly male-skewed human epidemiology.
- Both **inhalational** and **intraperitoneal** challenge routes are used and produce differing kinetics/severity (PMID 28182634/PMC5325312).

### Other Model Systems
- **Hamster models**: used for capsule-mutant attenuation studies (PMID 26836271) and are generally considered highly susceptible, acute-lethality models useful for vaccine/therapeutic efficacy screening.
- **RAW 264.7 murine macrophage-like cell line** and **J774.2 murine macrophages**: the standard in vitro cellular infection models for dissecting T3SS-3-dependent vacuolar escape, intracellular replication, and autophagy evasion (BopA) mechanisms.
- **Human primary macrophage-based infection models**: used specifically to confirm that canonical NLRP3/NLRC4 inflammasome activation observed in mouse/cell-line systems is recapitulated in human cells (*PLoS Negl Trop Dis* 2020).
- **Avirulent/attenuated strains for biosafety**: e.g., the ΔpurM strain with atypical type B LPS (PMC5461690), engineered specifically to permit non-BSL-3 study of aspects of melioidosis biology — a useful "model limitation" note, since findings from attenuated-strain studies may not fully generalize to virulent-strain pathogenesis.

### Model Limitations
The BALB/c-acute/C57BL/6-chronic dichotomy is a well-validated and widely used proxy for the human acute/chronic clinical spectrum, but (a) inbred mouse LD50 values are many orders of magnitude apart from typical human environmental inoculum estimates, (b) the pronounced human comorbidity-driven risk architecture (diabetes, thalassemia, CKD) is not fully recapitulated in standard inbred immunocompetent mouse challenge models without additional metabolic-disease mouse-model crossing, and (c) the human "Vietnamese time bomb" multi-decade latency question (Section 8) has no validated long-duration animal model equivalent — the closest surrogate (low-dose C57BL/6 chronic aerosol exposure) models weeks, not years, of latency.

---

## Sources

- [Melioidosis | Nature Reviews Disease Primers](https://www.nature.com/articles/nrdp2017107)
- [Burkholderia pseudomallei and melioidosis | Nature Reviews Microbiology](https://www.nature.com/articles/s41579-023-00972-5)
- [Melioidosis: insights into the pathogenicity of Burkholderia pseudomallei - PubMed](https://pubmed.ncbi.nlm.nih.gov/16541135/)
- [molecular and cellular basis of pathogenesis in melioidosis | FEMS Microbiology Reviews](https://academic.oup.com/femsre/article/33/6/1079/509558)
- [Global burden of melioidosis in 2015: a systematic review and data synthesis - PubMed](https://pubmed.ncbi.nlm.nih.gov/31285144/)
- [Global Burden and Challenges of Melioidosis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6136634/)
- [Drivers of melioidosis endemicity: epidemiological transition, zoonosis, and climate change - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10128909/)
- [Understanding The Mimicker: Epidemiological Pattern and Determinant of Melioidosis Mortality in Negeri Sembilan, Malaysia](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11098469/)
- [Melioidosis and the kidney - Jabbar - 2013 - Nephrology](https://onlinelibrary.wiley.com/doi/10.1111/nep.12024)
- [Clinical Overview of Melioidosis | CDC](https://www.cdc.gov/melioidosis/hcp/clinical-overview/index.html)
- [Melioidosis in people living with diabetes; clinical presentation, clinical course and implications for patient management](https://www.sciencedirect.com/science/article/pii/S0001706X25000385)
- [Melioidosis in Critical Care: A Review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8327795/)
- [Type III Secretion in the Melioidosis Pathogen Burkholderia pseudomallei - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5471309/)
- [Burkholderia pseudomallei type III secretion system mutants exhibit delayed vacuolar escape phenotypes - PubMed](https://pubmed.ncbi.nlm.nih.gov/18443088/)
- [The Burkholderia pseudomallei Type III Secretion System and BopA Are Required for Evasion of LC3-Associated Phagocytosis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3055895/)
- [Melioidosis | About the Disease | GARD](https://rarediseases.info.nih.gov/diseases/9546/melioidosis)
- [Clinical features and epidemiology of melioidosis pneumonia - PubMed](https://pubmed.ncbi.nlm.nih.gov/22057702/)
- [Splenic abscesses complicating acute septicemic melioidosis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10550210/)
- [Treatment and prophylaxis of melioidosis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4236584/)
- [Efficacy and safety of co-trimoxazole in eradication phase of melioidosis; systematic review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10436656/)
- [Efficacy of drug treatment for severe melioidosis and eradication treatment: network meta-analysis | PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0011382)
- [Toll-like receptor 4 region genetic variants are associated with susceptibility to melioidosis | Genes & Immunity](https://www.nature.com/articles/gene201149)
- [Lack of Association of TLR1 and TLR5 Coding Variants with Mortality - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11066355/)
- [Entry #615557 - MELIOIDOSIS, SUSCEPTIBILITY TO - OMIM](https://www.omim.org/entry/615557)
- [Cellular GWAS of the host-pathogen interaction in melioidosis - Grantome](https://grantome.com/grant/NIH/R21-AI133171-01)
- [Characterization of pathogenesis and immune response to Burkholderia pseudomallei K96243 in BALB/c and C57BL/6 mice | PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0172627)
- [BALB/c and C57Bl/6 mice infected with virulent Burkholderia pseudomallei - PubMed](https://pubmed.ncbi.nlm.nih.gov/9600859/)
- [The Impact of Age and Sex on Mouse Models of Melioidosis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7168040/)
- [Low-Dose Exposure of C57BL/6 Mice to Burkholderia pseudomallei Mimics Chronic Human Melioidosis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3123849/)
- [Laboratory diagnosis of melioidosis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12677508/)
- [Human Melioidosis | Clinical Microbiology Reviews](https://journals.asm.org/doi/10.1128/cmr.00006-19)
- [CDPH IDB Guidance for Managing Select Communicable Diseases: MELIOIDOSIS](https://www.cdph.ca.gov/Programs/CID/DCDC/CDPH%20Document%20Library/IDBGuidanceforCALHJs-Melioidosis.pdf)
- [Effectiveness of a multifaceted prevention programme for melioidosis in diabetics (PREMEL)](https://www.medrxiv.org/content/10.1101/2020.12.18.20248448.full.pdf)
- [Activities of Daily Living Associated with Acquisition of Melioidosis in Northeast Thailand - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3578767/)
- [Melioidosis in Animals - Merck Veterinary Manual](https://www.merckvetmanual.com/infectious-diseases/melioidosis/melioidosis-in-animals)
- [Melioidosis in companion animals: Analysis of 45 Australian cases - Australian Veterinary Journal](https://onlinelibrary.wiley.com/doi/full/10.1111/avj.70097)
- [Melioidosis in humans and animals: a One Health perspective - IJID One Health](https://onehealth.ijidonline.org/article/S2949-9151(25)00040-X/fulltext)
- [Role of quorum sensing in the pathogenicity of Burkholderia pseudomallei | Microbiology Society](https://www.microbiologyresearch.org/content/journal/jmm/10.1099/jmm.0.45661-0)
- [Quorum Sensing Negatively Regulates Multinucleate Cell Formation - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3660431/)
- [Melioidosis and Activation from Latency: The "Time Bomb" Has Not Occurred - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11229659/)
- [Melioidosis: the Vietnamese time bomb - Trends in Urology & Men's Health](https://onlinelibrary.wiley.com/doi/full/10.1002/tre.753)
- [Neurological melioidosis - PubMed](https://pubmed.ncbi.nlm.nih.gov/10674643/)
- [Central nervous system melioidosis: A systematic review of individual participant data - PubMed](https://pubmed.ncbi.nlm.nih.gov/31022232/)
- [Melioidosis of the Central Nervous System: Impact of the bimABm Allele | Clinical Infectious Diseases](https://academic.oup.com/cid/article/78/4/968/6523821)
- [Mondo Disease Ontology](https://mondo.monarchinitiative.org/)
- [1C42 Melioidosis - ICD-11 MMS](https://www.findacode.com/icd-11/code-2129350166.html)
- [Melioidosis Vaccines (MeVa): Attitudes to vaccines, melioidosis and clinical trials - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10646340/)
- [First vaccine shows promise in protecting from deadly melioidosis infection](https://medicalxpress.com/news/2025-12-vaccine-deadly-melioidosis-infection.html)
- [PepSeq as a highly multiplexed platform for melioidosis antigen discovery | Frontiers in Immunology](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1605758/full)
- [An Observational Study to Evaluate Clinical Characteristics of Adult Patients With Suspected or Confirmed Melioidosis - ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06089668)
- [Clinical Presentation and Medical Management of Melioidosis in Children - Clinical Infectious Diseases](https://academic.oup.com/cid/article/60/1/21/2895591)
- [Mortality among hospitalized children with melioidosis in Thailand - The Lancet Regional Health Southeast Asia](https://www.thelancet.com/journals/lansea/article/PIIS2772-3682(25)00178-7/fulltext)
- [Prognostic value of cytokine concentrations in severe melioidosis - PubMed](https://pubmed.ncbi.nlm.nih.gov/10669346/)
- [Caspase-1-Dependent and -Independent Cell Death Pathways in Burkholderia pseudomallei Infection of Macrophages - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3953413/)
- [Caspase-11-dependent pyroptosis of lung epithelial cells protects from melioidosis | PLOS Pathogens](https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1007105)
- [Burkholderia pseudomallei triggers canonical inflammasome activation in a human primary macrophage-based infection model | PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0008840)
- [Taxonomy browser (Burkholderia pseudomallei) - NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=info&id=28450)
- [Burkholderia pseudomallei modulates host iron homeostasis to facilitate iron availability and intracellular survival | PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0006096)
- [Burkholderia pseudomallei BopE suppresses the Rab32-dependent defense pathway | mSphere](https://journals.asm.org/doi/10.1128/msphere.00453-24)
- [Characterization and analysis of the Burkholderia pseudomallei BsaN virulence regulon - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4236580/)
- [Attenuation of a select agent-excluded Burkholderia pseudomallei capsule mutant in hamsters - PubMed](https://pubmed.ncbi.nlm.nih.gov/26836271/)
- [An avirulent Burkholderia pseudomallei ΔpurM strain with atypical type B LPS - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5461690/)