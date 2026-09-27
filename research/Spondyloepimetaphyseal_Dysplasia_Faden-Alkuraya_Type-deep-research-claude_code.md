---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T07:18:29.139512'
end_time: '2026-08-20T07:23:03.002054'
duration_seconds: 273.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spondyloepimetaphyseal Dysplasia Faden-Alkuraya Type
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
  web_search_requests: 14
  num_turns: 27
  total_cost_usd: 2.1236780000000004
  session_id: e17d57c6-a2ec-5e66-b3cb-4774336cbbe7
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 14
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondyloepimetaphyseal Dysplasia Faden-Alkuraya Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondyloepimetaphyseal Dysplasia Faden-Alkuraya Type** covering all of the
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

I'll research this rare skeletal dysplasia using primary literature sources to ensure accurate gene names, OMIM IDs, and citations.

# Research Report: Spondyloepimetaphyseal Dysplasia, Faden-Alkuraya Type (SEMDFA)

## 1. Disease Information

**Overview:** Spondyloepimetaphyseal dysplasia, Faden-Alkuraya type (SEMDFA) is a rare, autosomal recessive, progressive skeletal dysplasia first clinically delineated by Faden and colleagues and molecularly solved as caused by biallelic loss-of-function mutations in **RSPRY1** (Ring finger and SPRY domain-containing protein 1). It is characterized by progressive vertebral (spondylo-), epiphyseal, and metaphyseal abnormalities, disproportionate short stature, a recognizable facial gestalt, short fourth (and sometimes third) metatarsals, brachydactyly with cone-shaped epiphyses, and variable intellectual disability, with craniosynostosis emerging as a recurrent — though not universal — additional feature in later reports (PMID:26365341; PMID:30063090).

**Key identifiers:**
- **OMIM:** #616723 (phenotype, SEMDFA); *616585 (gene, RSPRY1)
- **MONDO:** MONDO:0014748
- **Orphanet:** ORPHA:457395
- **Gene (HGNC):** RSPRY1, HGNC:29420, chromosome 16q13
- **Inheritance:** Autosomal recessive

**Synonyms:** "SEMDFA"; "Spondyloepimetaphyseal dysplasia, RSPRY1-related"; "RSPRY1-related spondyloepimetaphyseal dysplasia"; occasionally described in early reports as a novel "progressive spondyloepimetaphyseal dysplasia" prior to gene identification.

**Data provenance:** All current knowledge derives from a small number of aggregated case-series publications (not large-cohort epidemiological or EHR-derived data). The literature comprises: (1) the original report of 4 affected siblings in a consanguineous Bedouin Saudi family plus a Peruvian simplex case identified via "matchmaking" (PMID:26365341); (2) a follow-up delineation of 5 additional patients from 2 unrelated families with craniosynostosis (PMID:30063090); (3) a 2024 report of two additional Turkish/other-origin sisters with joint dislocation as a novel feature (PMID from AJMG-A 2024, "Two sisters with RSPRY1-related spondyloepimetaphyseal dysplasia," PMC7616131/AJMG 63601); and (4) a 2025 functional/mechanistic study using patient-derived fibroblasts (PMID:39940902). Fewer than ~15 molecularly confirmed patients have been reported in total.

---

## 2. Etiology

**Disease Causal Factor:** SEMDFA is a monogenic disorder caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in RSPRY1**. There is no known environmental, infectious, or purely mechanistic (non-genetic) cause.

**Genetic risk factors:**
- Homozygosity for pathogenic RSPRY1 variants, typically arising in the context of parental consanguinity (both the original Saudi Bedouin family and subsequent families were consanguineous or from populations with elevated consanguinity) (PMID:26365341).
- Reported pathogenic alleles include:
  - c.377delT; p.(Ile126Argfs*) — homozygous frameshift in exon 2, predicted to trigger nonsense-mediated decay (originally reported as a 1-bp duplication/frameshift in the discovery family; re-described as c.377delT in later papers) (PMID:26365341; PMID:30063090; PMID:39940902)
  - A homozygous splice-site variant at the exon 4/intron 4 border (c.516+2T>A) (PMID:30063090)
  - A likely pathogenic homozygous missense variant identified in the Peruvian simplex case via GeneMatcher-style matchmaking (PMID:26365341)
  - c.1652G>A; p.(Cys551Tyr) — homozygous missense in exon 15, absent from gnomAD v3.1.2 and an in-house cohort of 3,076 exomes, with an AlphaMissense score of 0.999 and cross-species conservation of the affected cysteine (AJMG-A "Two sisters" report)
- RSPRY1 has a gnomAD pLI of 1 and LOEUF of 0.45, consistent with strong intolerance to loss-of-function variation in the general population, supporting pathogenicity of truncating alleles.
- No modifier genes have been reported.

**Environmental risk factors:** None identified; this is a purely Mendelian condition. Consanguinity increases the *probability* of biallelic inheritance but is a population/pedigree risk factor rather than a direct environmental cause.

**Protective factors:** None reported in the literature (no protective alleles or environmental protective factors described for this ultra-rare disorder).

**Gene-environment interactions:** None reported; no evidence of environmental modulation of phenotype severity.

**Suggested ontology terms:** MONDO:0014748 (disease); HGNC:29420 (gene); GENO term for autosomal recessive inheritance (GENO:0000388).

---

## 3. Phenotypes

Phenotype data are drawn from the combined case series (PMID:26365341, PMID:30063090, and the 2024 sisters report).

### Craniofacial features (onset: congenital/early childhood; frequent-to-common across reported cases)
- Microcephaly — HP:0000252
- Broad/prominent forehead — HP:0000337
- Hypertelorism — HP:0000316
- Epicanthal folds — HP:0000286
- Mild ptosis — HP:0000508
- Strabismus / exotropia — HP:0000486
- Malar hypoplasia / midface retrusion — HP:0000272 / HP:0011800
- Depressed nasal bridge, short nose — HP:0005280 / HP:0003196
- Full lips — HP:0012471
- Low-set ears — HP:0000369
- Short neck — HP:0000470
- Square-shaped face reported in one proband

### Skeletal — axial (progressive; worsens with age)
- Platyspondyly — HP:0000926
- Mild scoliosis / progressive kyphoscoliosis — HP:0002751
- Lumbar lordosis — HP:0002938
- Craniosynostosis — HP:0001363 (present in most but not all patients across the case series; "all patients except one were normocephalic" in the 2018 delineation cohort, indicating variable expressivity)
- "Copper-beaten" skull appearance — HP:0002714

### Skeletal — appendicular
- Short stature, disproportionate — HP:0004322 / HP:0001510
- Epiphyseal dysplasia with small/cone-shaped epiphyses — HP:0003046 / HP:0010580
- Metaphyseal cupping and fraying — HP:0003026 / HP:0003026
- Coxa vara — HP:0002812
- Genu valgum — HP:0002857
- Short 4th (and sometimes 3rd) metatarsal bone — HP:0010760
- Brachydactyly / brachymesophalangy with cone-shaped epiphyses — HP:0001156
- Small carpal bones — HP:0100926
- Short femoral neck — HP:0100864
- Pes planus — HP:0001763
- Prominent heels — (no precise HP term; describe qualitatively)
- Pectus deformity — HP:0000766
- Joint laxity / dislocation (novel feature reported in 2024 sisters — elbow subluxation, metatarsal dislocation, "wind-swept" limb deformity) — HP:0001373 / HP:0001386
- Cemento-ossifying fibrous lesion of the maxilla (reported once) — rare associated finding

### Neurodevelopmental
- Global developmental delay — HP:0001263
- Intellectual disability, variable severity (mild to moderate) — HP:0001249
- Generalized hypotonia — HP:0001290
- Seizures (generalized tonic-clonic, reported in one patient) — HP:0002069
- Brain imaging abnormalities: asymmetry of cerebral hemispheres, mild thinning of the corpus callosum — HP:0100542 / HP:0002079

### Other
- Congenital heart disease (patent ductus arteriosus reported in one proband) — HP:0001744 (PDA)

**Onset:** Congenital/prenatal-to-infantile recognition of facial and limb features; skeletal findings are explicitly **progressive** with age (worsening platyspondyly, epiphyseal/metaphyseal changes), which is a defining diagnostic feature distinguishing SEMDFA from static SEMDs.

**Severity/frequency:** Based on small case numbers, most craniofacial and skeletal features are reported in the majority of patients (qualitatively "frequent" to "common"), while craniosynostosis, seizures, congenital heart disease, and joint dislocation are reported in only a subset — precise percentage frequencies cannot be reliably computed from n<15 published cases; use qualitative HPO frequency terms (e.g., FREQUENT, OCCASIONAL) with caution and cite per-patient counts rather than population percentages.

**Quality of life impact:** Not formally studied (no EQ-5D/SF-36/QOL instrument data published); impacts are inferable from reported functional findings — short stature, joint instability, intellectual disability, and progressive spinal deformity would be expected to affect mobility, education, and independence, but this is not directly evidenced in the literature.

---

## 4. Genetic/Molecular Information

**Causal gene:** RSPRY1 (HGNC:29420; OMIM *616585), located at chromosome 16q13, encoding a 576-amino-acid protein.

**Protein domains/function:** RSPRY1 contains a **RING-type (C3HC4) zinc finger domain** and a **SPRY/B30.2 domain**, consistent with predicted E3 ubiquitin-protein ligase architecture, though at the time of its original description it was called "a hypothetical RING and SPRY domain-containing protein of unknown physiological function" (PMID:26365341). It has since been characterized as a secreted protein expressed strongly in **osteoblasts and osteocytes** during mid-to-late embryonic endochondral bone development (PMID:39940902).

**Pathogenic variant types reported:**
| Variant | Type | Zygosity | Predicted consequence | Source |
|---|---|---|---|---|
| c.377delT; p.(Ile126fs*) | Frameshift, exon 2 | Homozygous | Nonsense-mediated decay / null allele | PMID:26365341; PMID:30063090; PMID:39940902 |
| c.516+2T>A | Splice-site, intron 4 | Homozygous | Predicted aberrant splicing | PMID:30063090 |
| Missense (Peruvian proband) | Missense | Homozygous | Likely pathogenic (unspecified residue) | PMID:26365341 |
| c.1652G>A; p.(Cys551Tyr) | Missense, exon 15 | Homozygous | Likely pathogenic; AlphaMissense 0.999; absent from gnomAD v3.1.2 and 3,076 in-house exomes; affected Cys conserved across 5 vertebrate species | AJMG-A 2024 "Two sisters" |

**Variant classification:** ACMG/AMP framework applied in recent reports — missense c.1652G>A classified "likely pathogenic"; frameshift and splice variants are treated as loss-of-function/null alleles by nonsense-mediated decay.

**Population frequency:** RSPRY1 shows strong constraint in gnomAD (pLI = 1, LOEUF = 0.45), consistent with selection against loss-of-function variants in the general population — supportive of pathogenicity for truncating alleles but also indicating that population-level carrier frequency data for specific pathogenic alleles are not available (each reported variant is private/family-specific or found in only 1–2 unrelated families).

**Somatic vs. germline:** All reported variants are germline.

**Functional consequences — molecular mechanism (2025 mechanistic study, PMID:39940902):**
- RNA-seq of patient-derived dermal fibroblasts (homozygous c.377delT) versus controls identified 456 downregulated and 545 upregulated genes (FDR p ≤ 0.001).
- The most significantly enriched pathway was "TGF-β regulation of extracellular matrix" (p = 1.12 × 10⁻²⁴), with key genes including SMAD3, COL1A1, WISP1, and RUNX2.
- CRISPR-Cas9 RSPRY1-knockout fibroblasts showed increased wound-healing motility that was **SMAD3-dependent** (abrogated in RSPRY1+SMAD3 double-knockout cells).
- Exogenous TGF-β1 supplementation accelerated wound closure in control cells but had limited additional effect in RSPRY1-KO cells, suggesting **endogenous TGF-β/SMAD3 signaling is already constitutively activated** in RSPRY1-deficient cells.
- Over 16% of differentially expressed genes were linked to SEMD-relevant phenotypes (mental retardation: 97 DEGs; microcephaly: 64 DEGs; dwarfism: 61 DEGs; short stature: 59 DEGs).
- Conclusion: **"RSPRY1 deficiency leads to overactivation of the TGF-β signaling pathway,"** disrupting extracellular-matrix dynamics required for endochondral ossification and skeletal homeostasis — providing the first mechanistic model linking RSPRY1 loss to the skeletal dysplasia phenotype.

**Modifier genes:** None identified.

**Epigenetic information / chromosomal abnormalities:** None reported for SEMDFA — this is a point-mutation/small-indel disorder, not associated with copy-number or chromosomal rearrangement etiology.

**Suggested GO terms:**
- GO:0007179 (transforming growth factor beta receptor signaling pathway) — UPREGULATED/GAIN_OF_FUNCTION per the 2025 mechanistic data
- GO:0030199 (collagen fibril organization) / GO:0030198 (extracellular matrix organization)
- GO:0001503 (ossification) / GO:0060348 (bone development)
- GO:0004842 (ubiquitin-protein transferase activity) — predicted RING E3 ligase activity (functionally unconfirmed)

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors have been identified or are biologically plausible for this monogenic skeletal dysplasia. There is no ECTO-relevant exposure literature for SEMDFA.

---

## 6. Mechanism / Pathophysiology

**Causal chain (as currently evidenced):**

1. **Trigger (molecular):** Biallelic loss-of-function (or missense) variants in RSPRY1 → loss/reduction of functional RSPRY1 protein in osteoblasts/osteocytes and other cell types (fibroblasts used as a patient-accessible proxy tissue).
2. **Molecular consequence:** Loss of RSPRY1 (a putative RING/SPRY E3-ligase-like secreted regulatory protein) leads to **dysregulated (overactivated) TGF-β/SMAD3 signaling**, evidenced by transcriptomic enrichment of TGF-β–ECM pathway genes and by SMAD3-dependent hypermotility phenotypes in knockout fibroblasts (PMID:39940902).
3. **Cellular consequence:** Altered extracellular matrix gene expression (COL1A1, WISP1) and altered RUNX2 (a master osteoblast transcription factor) expression, implicating disrupted **endochondral ossification** and **cell motility/matrix remodeling** in growth-plate chondrocytes and osteoblasts.
4. **Tissue-level consequence:** Impaired/dysregulated growth-plate cartilage and metaphyseal bone formation → epiphyseal and metaphyseal dysplasia (cupping, fraying, cone-shaped epiphyses), vertebral body dysplasia (platyspondyly), and cranial suture abnormalities (craniosynostosis in a subset).
5. **Organism-level consequence:** Progressive short stature, skeletal deformity (scoliosis, coxa vara, genu valgum), craniofacial dysmorphism, and — via presumed CNS/neurodevelopmental involvement not yet mechanistically dissected — intellectual disability and hypotonia.

**Upstream vs. downstream:** RSPRY1 loss is the sole known upstream initiating lesion; TGF-β/SMAD3 pathway dysregulation is the best-characterized downstream molecular effector; skeletal dysplasia and craniosynostosis are the downstream tissue/organ phenotypes. The neurodevelopmental phenotype's mechanistic link to RSPRY1/TGF-β dysregulation has **not** been directly studied (a knowledge gap — RSPRY1's role in neural tissue is unexplored).

**Cell types involved:** Osteoblasts (CL:0000062), osteocytes (CL:0000138), growth-plate chondrocytes (CL:0000138/CL:1000320 chondrocyte of epiphyseal cartilage), dermal fibroblasts (CL:0000057, used as the experimental proxy cell type in the mechanistic study).

**Biochemical/protein-level abnormality:** Predicted E3-ubiquitin-ligase-like RSPRY1 loss is hypothesized to normally restrain/regulate TGF-β pathway components (e.g., via ubiquitination of a pathway member), though the direct substrate of RSPRY1's putative RING domain has not been identified — this remains an open mechanistic gap.

**Molecular profiling data available:** Bulk RNA-sequencing (transcriptomics) of patient fibroblasts vs. controls (PMID:39940902) is the only omics dataset published for this disease; no proteomics, metabolomics, lipidomics, single-cell, or spatial transcriptomics data exist to date.

**Suggested GO/CL terms:** GO:0007179 (TGFβR signaling), GO:0001501 (skeletal system development), GO:0060350 (endochondral bone morphogenesis), GO:0071711 (basement membrane organization), CL:0000062 (osteoblast), CL:0000138 (chondrocyte), CL:0000057 (fibroblast).

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Skeletal system** (primary): axial skeleton (vertebral column, skull/cranial sutures), appendicular skeleton (long bone epiphyses/metaphyses, carpals, metatarsals, phalanges)
- **Craniofacial skeleton**: cranial sutures (craniosynostosis), facial bones (malar hypoplasia, nasal bridge)
- **Nervous system** (secondary): brain (corpus callosum thinning, cerebral hemisphere asymmetry), reported in a subset
- **Cardiovascular system** (secondary, isolated report): patent ductus arteriosus
- **Ocular system**: strabismus, ptosis (extraocular muscles/lids)

**Tissue/cell level:**
- Growth plate cartilage (epiphyseal/metaphyseal chondrocytes)
- Bone (osteoblasts, osteocytes)
- Cranial suture mesenchyme/osteogenic fronts
- Dermal fibroblasts (studied ex vivo as disease model)

**Subcellular level:** Not directly studied; RSPRY1 is predicted to be secreted, implicating extracellular/ECM compartments (GO:0005576 extracellular region) rather than a specific organelle.

**Localization/UBERON terms:**
- UBERON:0002481 (bone tissue), UBERON:0002050 (growth plate cartilage), UBERON:0001130 (vertebral column), UBERON:0003128 (cranial suture), UBERON:0002417 (skull), UBERON:0002423 (metatarsal bone)

**Lateralization:** Generally bilateral/symmetric skeletal involvement (as with most systemic skeletal dysplasias); no reports of unilateral or strongly asymmetric skeletal findings, though cerebral hemisphere *asymmetry* has been noted on brain imaging in one report.

---

## 8. Temporal Development

- **Onset:** Congenital-to-infantile. Facial dysmorphism and short stature are typically recognized in early childhood; skeletal radiographic abnormalities (platyspondyly, metaphyseal changes) are present from early life but are explicitly described as **progressive**.
- **Onset pattern:** Insidious/chronic — this is not an acute-onset condition.
- **Progression:** Skeletal deformities (scoliosis, epiphyseal/metaphyseal changes) worsen with growth; the disorder is described in its founding publication as a "**progressive** spondyloepimetaphyseal dysplasia," distinguishing it from static/non-progressive SEMD entities.
- **Disease course pattern:** Chronic, progressive, non-remitting; no spontaneous or treatment-induced remission has been described.
- **Disease duration:** Lifelong; no natural history data on adult outcomes, life expectancy, or long-term progression beyond childhood/adolescence have been published (a significant literature gap, given the small number of reported patients and their young ages at publication).
- **Critical periods:** Not formally defined, though early recognition (facial gestalt + short 4th metatarsal + progressive spine/epiphyseal changes) is emphasized in the 2015 and 2018 papers as the basis for clinical diagnosis prior to genetic confirmation.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (GENO:0000388), consistent across all reported families, several of which were consanguineous.
- **Penetrance:** Appears complete among biallelic carriers in reported families (all homozygotes/compound heterozygotes were symptomatic), though with **variable expressivity** — e.g., craniosynostosis and seizures present in only a subset of patients ("all patients except one were normocephalic" in the 2018 cohort).
- **Expressivity:** Variable — severity and specific feature combinations (craniosynostosis, joint dislocation, seizures, congenital heart disease) differ between and within families.
- **Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** Not formally established, but the discovery family (consanguineous Bedouin Saudi) and subsequent Turkish (Simsek-Kiper et al., Hacettepe University) and Peruvian families suggest the condition has been identified across multiple, geographically/ethnically distinct populations rather than being confined to a single founder population; each reported family carries a distinct (private) pathogenic variant.
- **Consanguinity:** Plays a central role — most reported families are consanguineous, consistent with autosomal recessive inheritance of a rare allele.
- **Carrier frequency:** Not established in the general population (no population-based carrier screening data); RSPRY1's gnomAD constraint metrics (pLI=1, LOEUF=0.45) indicate the gene is intolerant of loss-of-function variation, but specific carrier frequencies for the known pathogenic alleles are not published.

**Epidemiology:**
- **Prevalence/Incidence:** Not established — this is an ultra-rare disorder with fewer than ~15 molecularly confirmed cases published to date across 4 case reports/series (PMID:26365341 [5 cases: 4 sibs + 1 Peruvian]; PMID:30063090 [5 cases, 2 families]; 2024 AJMG-A report [2 sisters]; the 2025 mechanistic paper reused patient cells from the original cohort). No population prevalence estimate (e.g., Orphanet prevalence class) has been established; classify as **prevalence_class: NOT_YET_DOCUMENTED** or **ULTRA_RARE** and **measure_type: CASES_IN_LITERATURE**.

**Population demographics:**
- **Affected populations:** Reported in families of Saudi Bedouin, Turkish, and Peruvian origin, indicating no single predominant ethnic association beyond the general enrichment of autosomal recessive disease in consanguineous populations.
- **Geographic distribution:** Saudi Arabia (discovery family), Turkey (Hacettepe University cohort, 2018 delineation and 2025 mechanistic paper), Peru (simplex case), and additional unspecified origin in the 2024 sisters report.
- **Sex ratio:** Both males and females affected across reported families (consistent with autosomal — not sex-linked — inheritance); no skew reported.
- **Age distribution:** All reported patients are pediatric (ages from early childhood to adolescence at publication); no adult-onset diagnoses or long-term adult follow-up published.

---

## 10. Diagnostics

**Clinical/radiographic tests (primary diagnostic modality given rarity):**
- **Skeletal survey/radiography:** Platyspondyly, "copper-beaten" skull appearance, metaphyseal cupping/fraying, cone-shaped epiphyses, coxa vara, genu valgum, short 4th metatarsal, small carpal bones — these radiographic findings, combined with the facial gestalt, form the basis of clinical suspicion prior to molecular confirmation (PMID:26365341; PMID:30063090).
- **Cranial imaging (CT/plain film):** To assess craniosynostosis when present.
- **Brain MRI:** Reported to show cerebral hemisphere asymmetry and mild corpus callosum thinning in a subset.
- **Echocardiography:** Indicated given at least one reported case of PDA.

**Genetic testing (definitive diagnosis):**
- **Recommended approach:** Given the rarity and lack of a commercial single-gene/panel-first pathway, diagnosis has been achieved via **whole-exome sequencing (WES)** in a consanguineous-family/autozygosity-mapping framework (homozygosity mapping combined with WES was the strategy in the discovery family) or **targeted Sanger sequencing** of RSPRY1 once a family's causal gene is suspected/confirmed.
- **Skeletal dysplasia gene panels:** RSPRY1 is included in some commercial skeletal dysplasia and craniosynostosis gene panels (e.g., Invitae Skeletal Disorders Panel; Genomics England PanelApp "Rare syndromic craniosynostosis or isolated multisuture synostosis" panel).
- **Chromosomal microarray/karyotype:** Not informative (RSPRY1 disease is due to point mutations/small indels, not CNVs); not part of the diagnostic algorithm beyond ruling out other differentials.
- **Family/matchmaking approaches:** The original description of a second (Peruvian) family was made possible through **gene-based matchmaking** (e.g., GeneMatcher-style) connecting independently sequenced exomes sharing RSPRY1 variants — an important methodological note for this ultra-rare disease (PMID:26365341).

**Differential diagnosis:** Other spondyloepimetaphyseal dysplasias, notably:
- SEMD, Strudwick type (COL2A1; OMIM #184250)
- SEMD with joint laxity, type 2 (KIF22; OMIM #603546) — distinguished by leptodactylic (slender) rather than brachydactylic digits and joint laxity/dislocation as a core (not incidental) feature
- SEMD, X-linked (OMIM #300106)
- Axial spondylometaphyseal dysplasia (C21orf2; OMIM #602271) — distinguished by retinal dystrophy
- Other craniosynostosis syndromes when craniosynostosis is prominent

**Screening:** No newborn screening, carrier screening panel, or population screening program exists for this ultra-rare disorder; genetic counseling for consanguineous families with an affected child is the primary "screening" relevant to recurrence risk (25% recurrence risk per pregnancy for carrier parents).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No mortality has been reported in the published cohorts; there are no survival statistics, life-expectancy data, or disease-specific mortality figures available, reflecting both the rarity of the condition and the young age of reported patients.
- **Morbidity:** Morbidity centers on progressive skeletal deformity (scoliosis, joint malalignment, short stature) and, in a subset, intellectual disability, seizures, and craniosynostosis-related complications (which, if untreated, can raise intracranial pressure).
- **Quality of life:** Not formally measured; can be inferred to be affected by mobility limitations, orthopedic complications, and developmental delay, but no validated QOL instrument data exist.
- **Complications:** Progressive scoliosis/kyphoscoliosis, coxa vara, joint dislocation/instability (elbow, metatarsal — newly reported feature), craniosynostosis-related complications, and in a subset, seizures and congenital heart disease.
- **Recovery potential:** This is a progressive, non-reversible skeletal dysplasia; there is no described mechanism of spontaneous improvement. Orthopedic and craniofacial surgical interventions (where performed, e.g., craniosynostosis correction) address complications rather than the underlying disease process.
- **Prognostic factors:** No formal prognostic biomarkers or predictors of disease severity have been identified; genotype-phenotype correlation is limited by small case numbers (e.g., it is not yet clear whether frameshift/null alleles produce more severe phenotypes than the missense alleles reported).

---

## 12. Treatment

There is **no disease-specific or targeted pharmacotherapy** for SEMDFA; management is supportive and multidisciplinary, following general skeletal dysplasia care principles (inferred from the disorder's classification as a skeletal dysplasia, though the literature reviewed does not describe a dedicated management protocol specific to RSPRY1-SEMDFA):

- **Orthopedic surgical management:** Correction of scoliosis, coxa vara, genu valgum, and joint instability/dislocation as clinically indicated (NCIT:C15329 Surgical Procedure; NCIT:C16186 Orthopedic Surgical Procedure).
- **Craniofacial surgery:** Craniosynostosis correction where present (NCIT:C15329).
- **Cardiac management:** Standard care for congenital heart disease (e.g., PDA closure) when present.
- **Neurodevelopmental support:** Early intervention, special education, physical/occupational/speech therapy for developmental delay and intellectual disability (NCIT:C15302 Physical Therapy; NCIT:C121351 Occupational Therapy; NCIT:C159273 Speech Therapy).
- **Seizure management:** Standard antiepileptic pharmacotherapy where seizures occur (NCIT:C15986 Pharmacotherapy).
- **Genetic counseling:** Recommended for families, particularly given the autosomal recessive inheritance and consanguinity association (NCIT:C15240 Genetic Counseling).

**Emerging/experimental therapeutic rationale:** The 2025 mechanistic study (PMID:39940902) identifying **SMAD3-dependent TGF-β pathway overactivation** as a downstream consequence of RSPRY1 loss suggests that **TGF-β pathway-targeted therapies** (e.g., TGF-β/SMAD3 inhibitors, by analogy to their investigational use in other connective tissue/skeletal disorders such as Marfan syndrome) represent a plausible, but entirely untested, future therapeutic direction. The authors explicitly frame their findings as identifying "potential therapeutic targets within TGF-β signaling for treating skeletal dysplasias," but **no clinical trials, drug candidates, or NCT-registered studies exist for SEMDFA specifically**.

**Experimental treatments in clinical trials:** None identified (no ClinicalTrials.gov entries specific to RSPRY1-SEMDFA were found).

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (this is a genetic, not preventable, disorder); the closest analog is **reproductive genetic counseling** for consanguineous couples or known carrier couples, including discussion of **prenatal testing** (chorionic villus sampling/amniocentesis for RSPRY1 variant testing once a familial variant is known) and **preimplantation genetic testing (PGT)** as options.
- **Secondary prevention:** Early clinical recognition (facial gestalt, short 4th metatarsal, skeletal survey) to enable early genetic confirmation and initiation of surveillance (e.g., serial spine imaging for scoliosis progression, cranial imaging surveillance for craniosynostosis) — this constitutes early detection rather than disease prevention.
- **Tertiary prevention:** Proactive orthopedic/craniofacial surveillance and timely surgical intervention to prevent secondary complications (e.g., preventing neurological compromise from untreated craniosynostosis or progressive scoliosis).
- **Genetic counseling:** Central to family planning for at-risk (carrier) couples, given the 25% recurrence risk for autosomal recessive inheritance.
- **Population/public health interventions:** None specific (not applicable to this ultra-rare monogenic disorder); no vaccine, environmental, or public-health-level intervention is relevant.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** RSPRY1 orthologs exist across vertebrates (NCBI Taxon comparisons implied by cross-species conservation analysis of the p.Cys551Tyr residue across 5 vertebrate species in the 2024 AJMG-A report), but **no naturally occurring RSPRY1-related skeletal dysplasia has been reported in any non-human species** (no OMIA entry identified in this research pass).
- **Orthologous gene:** Mouse ortholog *Rspry1* (MGI:1914860); human RSPRY1 (NCBI Gene, HGNC:29420).
- **Comparative biology/veterinary relevance:** Not established; no veterinary case reports or naturally occurring animal disease models were found in this research.
- **Zoonotic potential:** Not applicable (non-infectious, monogenic disorder).

---

## 15. Model Organisms

- **Mouse models:** Targeted knockout alleles of *Rspry1* exist in mouse repositories — *Rspry1^tm1Lex^* (MGI:5007310) and *Rspry1^tm1(KOMP)Wtsi^* (MGI:4419609) — generated as part of large-scale knockout mouse programs (Lexicon/KOMP), and the gene has an active International Mouse Phenotyping Consortium (IMPC) entry (MGI:1914860). However, **detailed published phenotyping data specifically characterizing skeletal, craniofacial, or neurodevelopmental phenotypes recapitulating human SEMDFA in these mouse lines were not identified** in this research pass — this represents a **notable gap**: no peer-reviewed report of an *Rspry1*-knockout mouse skeletal phenotype was found, despite the alleles existing in repositories. (This should be flagged as a `HUMAN_MODEL_MISMATCH`/`KNOWLEDGE_GAP`-type consideration if used for curation: allele exists, but recapitulation status is unconfirmed pending IMPC phenotyping data review.)
- **Cellular/in vitro models:** The best-characterized "model system" for this disease is **patient-derived dermal fibroblasts**, used in the 2025 study (PMID:39940902) alongside **CRISPR-Cas9-generated isogenic RSPRY1-knockout and RSPRY1+SMAD3 double-knockout fibroblast lines** (>90% knockout efficiency), which recapitulated key molecular features (TGF-β/ECM pathway dysregulation, SMAD3-dependent hypermotility) and served as the functional validation system for the TGF-β mechanistic hypothesis.
- **Model characteristics/limitations:** Fibroblasts are a patient-accessible surrogate cell type, not the primary disease-relevant cell type (osteoblasts/chondrocytes); the study explicitly notes RSPRY1 is normally concentrated in **osteoblasts and osteocytes** during embryonic skeletal development, so fibroblast-based findings, while mechanistically informative (TGF-β/SMAD3 activation), have **translational-fidelity limitations** for the skeletal phenotype and have not yet been confirmed in bone-lineage cells or an animal model — an appropriate candidate for a `HUMAN_MODEL_MISMATCH` discussion in curation.
- **Applications:** The fibroblast/CRISPR-KO system enables study of RSPRY1's role in TGF-β/SMAD3 signaling and cell motility/ECM regulation, and could support future drug-repurposing or TGF-β-pathway-inhibitor screening relevant to skeletal dysplasia mechanisms.
- **Resources:** MGI (MGI:1914860), IMPC (mousephenotype.org gene page for Rspry1), Taconic Biosciences (Rspry1 knockout mouse research model listing).

---

## Summary of Key Primary Citations

| PMID | Citation | Contribution |
|---|---|---|
| 26365341 | Faden M et al., *Am J Hum Genet* 2015;97(4):608-615 | Original description; WES + autozygome mapping identifies RSPRY1 frameshift in 4-sib Saudi family + Peruvian matchmaking case |
| 30063090 | Simsek-Kiper PÖ et al., *Am J Med Genet A* 2018;176(9):2009-2016 | Further delineation in 5 patients/2 families; establishes craniosynostosis, cono-brachydactyly as recurrent features; new frameshift (c.377delT) and splice (c.516+2T>A) variants |
| (AJMG-A 2024, "Two sisters with RSPRY1-related SEMD," Singh et al.) | *Am J Med Genet A* 2024 | Two additional sisters; novel p.(Cys551Tyr) missense variant; joint dislocation described as a novel clinical feature |
| 39940902 | *Int J Mol Sci* 2025;26(3):1134 | Mechanistic study: patient fibroblast transcriptomics + CRISPR knockout demonstrate RSPRY1 loss drives SMAD3-dependent TGF-β pathway overactivation |

**Data gaps for curation to flag explicitly:** No established population prevalence; no adult natural-history/long-term outcome data; no confirmed in vivo (mouse) skeletal phenotype recapitulation despite existing knockout alleles; no disease-specific treatment trials; genotype-phenotype correlation (frameshift/null vs. missense) not yet established given small case numbers.

Sources:
- [Entry - #616723 - SPONDYLOEPIMETAPHYSEAL DYSPLASIA, FADEN-ALKURAYA TYPE; SEMDFA - OMIM](https://www.omim.org/entry/616723)
- [Entry - *616585 - RING FINGER- AND SPRY DOMAIN-CONTAINING PROTEIN 1; RSPRY1 - OMIM](https://www.omim.org/entry/616585)
- [Identification of a Recognizable Progressive Skeletal Dysplasia Caused by RSPRY1 Mutations - PMC (PMID:26365341)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4596891/)
- [Further delineation of spondyloepimetaphyseal dysplasia Faden-Alkuraya type - PubMed (PMID:30063090)](https://pubmed.ncbi.nlm.nih.gov/30063090/)
- [Two sisters with RSPRY1-related spondyloepimetaphyseal dysplasia - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7616131/)
- [Unraveling the Role of RSPRY1 in TGF-β Pathway Dysregulation - PMC (PMID:39940902)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11817781/)
- [Spondyloepimetaphyseal Dysplasia, Faden-Alkuraya Type - MalaCards](https://www.malacards.org/card/spondyloepimetaphyseal_dysplasia_faden_alkuraya_type)
- [RSPRY1 gene - GeneCards](https://www.genecards.org/card/RSPRY1)
- [RSPRY1 ring finger and SPRY domain containing 1 - NIH Genetic Testing Registry (GTR)](https://www.ncbi.nlm.nih.gov/gtr/genes/89970/)
- [Gene: RSPRY1 - Genomics England PanelApp (Rare syndromic craniosynostosis panel)](https://panelapp.genomicsengland.co.uk/panels/168/gene/RSPRY1/)
- [RSPRY1 curation results - ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:29420)
- [Rspry1 MGI Mouse Gene Detail - MGI:1914860](https://www.informatics.jax.org/marker/MGI:1914860)
- [Rspry1 - IMPC](https://www.mousephenotype.org/data/genes/MGI:1914860)
- [Rspry1<tm1Lex> Targeted Allele Detail - MGI:5007310](https://www.informatics.jax.org/allele/MGI:5007310)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.