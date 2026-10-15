---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T14:04:45.303546'
end_time: '2026-09-04T14:09:53.057215'
duration_seconds: 307.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Rabson-Mendenhall Syndrome
  mondo_id: ''
  category: Endocrine
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
  num_turns: 24
  total_cost_usd: 1.3984048000000004
  session_id: 4583080c-1cc0-583c-84bf-77d0d31559d4
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rabson-Mendenhall Syndrome
- **MONDO ID:**  (if available)
- **Category:** Endocrine

## Research Objectives

Please provide a comprehensive research report on **Rabson-Mendenhall Syndrome** covering all of the
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

I'll research Rabson-Mendenhall Syndrome comprehensively now, running several searches in parallel across the key topic areas.

I now have comprehensive material to compile the full report.

I have gathered comprehensive information across all major domains. Here is the complete research report.

# Rabson-Mendenhall Syndrome: Comprehensive Research Report

## 1. Disease Information

**Overview.** Rabson-Mendenhall syndrome (RMS) is an ultra-rare autosomal recessive disorder caused by biallelic (homozygous or compound heterozygous) loss-of-function variants in the insulin receptor gene (*INSR*), producing one of the most severe forms of genetically determined insulin resistance in humans. It sits in the middle of a phenotypic continuum of "INSR-related severe insulin resistance syndrome" (INSR-SIRS), between the neonatally lethal **Donohue syndrome** (leprechaunism, the most severe end) and the comparatively milder **Type A insulin resistance syndrome** (NBK476444). Clinically it is defined by extreme hyperinsulinemia, growth retardation, characteristic coarse ("elfin"/senile) facial features, acanthosis nigricans, hypertrichosis, dental and nail abnormalities, and pineal hyperplasia, with progression to insulin-resistant diabetes mellitus and recurrent diabetic ketoacidosis (DKA) in the first two decades of life.

**Key identifiers:**
- **OMIM:** 262190 ("Pineal Hyperplasia, Insulin-Resistant Diabetes Mellitus, and Somatic Abnormalities") — [OMIM 262190](https://www.omim.org/entry/262190)
- **Gene locus (OMIM):** *INSR*, 147670, chromosome 19p13.2
- **Orphanet:** ORPHA:769 — [Orphanet: Rabson-Mendenhall syndrome](https://www.orpha.net/en/disease/detail/769)
- **MONDO:** MONDO:0009874
- **UMLS/MedGen:** C0271695 — [MedGen](https://www.ncbi.nlm.nih.gov/medgen/78783)
- **ICD-10:** E13 (Other specified diabetes mellitus) is the commonly cross-referenced code (no RMS-specific ICD-10 code exists; it is typically coded under syndromic/other diabetes categories)
- **GeneReviews chapter:** "INSR-Related Severe Insulin Resistance Syndrome" (covers both Donohue syndrome and RMS as one continuum) — [GeneReviews NBK476444](https://www.ncbi.nlm.nih.gov/books/NBK476444/)

**Synonyms:** Mendenhall syndrome; insulin resistance with acanthosis nigricans and pineal hyperplasia; INSR-related severe insulin resistance syndrome (intermediate/RMS phenotype).

**Evidence basis.** Nearly all available data derive from aggregated case reports and small case series (individual patients, not large registries or EHR cohorts) — fewer than ~50–100 molecularly confirmed cases have been published worldwide. The largest aggregation to date is a 2024 systematic review/meta-analysis of 42 patients pooled from 33 published articles (PMC11216847), which is the closest the literature has to a "disease-level" resource; otherwise virtually all information is from individual case reports, with GeneReviews and Orphanet providing curated syntheses of that case literature.

---

## 2. Etiology

**Primary cause — genetic.** RMS is caused by biallelic pathogenic variants in *INSR* (insulin receptor gene, 19p13.2), inherited in autosomal recessive fashion with variable expressivity. GeneReviews describes five functional classes of *INSR* pathogenic variants, all converging on loss of receptor function:
1. Impaired receptor biosynthesis
2. Impaired transport of the receptor to the plasma membrane
3. Impaired insulin binding affinity
4. Impaired tyrosine kinase activity
5. Accelerated receptor degradation

The 42-patient analysis (PMC11216847) found 55 distinct *INSR* variants: missense mutations were by far the most common class (72.7%), followed by deletions (10.9%), insertions (1.8%), and nonsense variants (1.8%); the most recurrent single variant was p.Glu238Lys (7.3%, 4/55), and exon 2 was the most frequently affected exon (7 occurrences). Compound heterozygosity is more common than true homozygosity; 52.4% of the 42 patients carried ≥2 distinct variants and 47.6% carried a single (presumed homozygous or the second allele undetected) variant.

**Genotype-phenotype correlation.** GeneReviews states explicitly: "There are no known genotype-phenotype correlations in INSR-SIRS" — variant type/location does not reliably predict Donohue vs. RMS vs. Type A severity, though broadly, variants that abolish receptor function completely tend toward the Donohue end and partial-function variants toward RMS/Type A.

**Founder/recurrent variants documented in the literature:**
- c.167T>C (p.Ile56Thr) — founder variant reported in the Israeli Druze population
- c.3003_3012del10insGGAAG (p.Ser1001ArgfsTer37) — reported in Tunisian families
- A 2024 "genealogical" case series (PMID:40499531) describes a multi-generation kindred with RMS traced through a shared *INSR* variant.

**Risk factors:**
- *Genetic:* biallelic *INSR* variants are necessary and sufficient; parental consanguinity substantially raises recurrence risk in families, and RMS pedigrees are frequently consanguineous (per case-series commentary; no population-based consanguinity rate is published).
- Heterozygous carriers (parents/siblings) are generally asymptomatic but may show a mild phenotype overlapping with **Type A insulin resistance syndrome**, and heterozygous females are described as being at increased risk for gestational diabetes and require glucose monitoring in pregnancy (GeneReviews).
- *Environmental/lifestyle:* no environmental, infectious, dietary, or occupational risk factor is implicated — this is a purely monogenic disorder; standard childhood metabolic stressors (illness, fasting, high-carbohydrate intake) precipitate the glycemic swings and DKA episodes that mark disease progression but do not cause the underlying condition.

**Protective factors:** None specific are described in the literature; there is no known modifier variant or environmental exposure shown to attenuate the phenotype. Because affected individuals retain some residual insulin receptor function (unlike Donohue syndrome), the RMS phenotype itself can be considered a "less severe" position along the allelic severity spectrum, but this is a genotype effect, not an independent protective factor.

**Gene-environment interaction:** Not established beyond the generic observation that infection, illness, and nutritional intake modulate glycemic control and precipitate ketoacidosis in the context of the underlying genetic lesion; no GxE database entries specific to RMS were identified.

---

## 3. Phenotypes

RMS phenotypes span dysmorphic/dermatologic signs, endocrine-metabolic laboratory abnormalities, and organ-specific complications. Frequencies below are drawn from the 42-patient pooled analysis (PMC11216847) unless otherwise noted.

| Phenotype | Frequency | HPO term (suggested) | Notes |
|---|---|---|---|
| Acanthosis nigricans | 69.1% (29/42) | HP:0000956 | Early childhood onset; velvety hyperpigmented, thickened skin at neck, axillae, groin |
| Growth retardation / short stature | 59.5% (25/42) | HP:0001510 (Growth delay) / HP:0004322 (Short stature) | Both prenatal (IUGR) and postnatal growth failure described |
| Dental anomalies (premature eruption, crowding, dysplastic teeth) | 54.8% (23/42) | HP:0000707 (Abnormality of the dentition) | Early tooth eruption is a hallmark diagnostic clue |
| Hirsutism / hypertrichosis | 40.5% (17/42) | HP:0000998 (Hirsutism) / HP:0000998-adjacent HP:0001054 (Hypertrichosis) | Generalized excess body hair, often noted from infancy |
| Enlarged genitalia (clitoromegaly in females; phallic enlargement) | 19.0% (8/42) | HP:0000027 (Abnormality of penis) / HP:0000138 (Ovarian cyst)-related | Related to hyperinsulinemia-driven androgen excess |
| Nail hypertrophy/dystrophy | 14.3% (6/42) | HP:0001807 (Abnormal nail morphology) | |
| Coarse/senile facial appearance, prominent jaw, full lips, large ears, furrowed tongue | Common (qualitative, near-universal in case reports) | HP:0000280 (Coarse facial features) | Descriptive "elfin" or prematurely aged appearance |
| Fasting hypoglycemia with postprandial hyperglycemia | Characteristic early feature | HP:0001943 (Hypoglycemia) / HP:0003074 (Hyperglycemia) | Paradoxical pattern from extreme hyperinsulinemia acting on residual receptor + non-receptor pathways |
| Diabetes mellitus (insulin-resistant) | 75.8% of evaluable cases (25/33) developed by age 23 | HP:0000857 (Insulin-resistant diabetes mellitus) | Mean diagnostic age 9.41 years (range 0–23) |
| Diabetic ketoacidosis (recurrent) | Frequent complication, leading cause of morbidity/mortality | HP:0025187 (or generic) | Emerges as insulin secretion declines in the second decade |
| Pineal hyperplasia | Named in OMIM title; reported in multiple cases | HP:0011912 (Pineal cyst)-adjacent; no exact HPO term for hyperplasia — closest is pineal gland abnormality | Melatonin metabolite excretion is elevated, consistent with disordered pineal function |
| Polycystic/enlarged ovaries with hyperandrogenism | Frequent in postpubertal/pubertal females | HP:0000138 (Ovarian cyst) / HP:0000023 (Hyperandrogenism) | Can require gonadectomy if causing mass effect or malignancy concern |
| Nephrocalcinosis / renal abnormality | "Most individuals" per GeneReviews/GARD summaries | HP:0000121 (Nephrocalcinosis) | Distinct mechanism proposed relating INSR function in the kidney (PMC4369119) |
| Organomegaly (kidney, liver, spleen, tongue, external genitalia) | Reported subset | HP:0002240 (Hepatomegaly) etc. | |
| Lipoatrophy / paucity of subcutaneous fat | Common descriptive feature | HP:0009125 (Lipodystrophy) | Contrasts with obesity-associated insulin resistance; patients are typically underweight, not obese |
| Low BMI / underweight | Mean BMI 16.0 kg/m²; 84.2% (16/19) underweight; no obese patients reported | — | Distinguishes RMS from acquired/metabolic-syndrome insulin resistance |
| Cardiac abnormalities (case reports) | Uncommon but described (ASD, and hypertrophic remodeling in the allelic Donohue phenotype) | HP:0001631 (ASD) | One case report of RMS with atrial septal defect (PMC3628395); cardiomyopathy is more classically described in Donohue syndrome (30% of infants per GeneReviews) |

**Onset/progression pattern:** Symptoms typically begin in infancy with failure to thrive and early dentition; acanthosis nigricans and hypertrichosis emerge in early childhood; the glycemic pattern evolves over time — GeneReviews notes that from birth to about age 1, severe hyperinsulinemia with fluctuating glucose predominates, while from roughly age 1 onward, insulin levels decline, glucose rises, hypoglycemic events lessen, and risk of ketoacidosis increases. Diabetes and its complications (retinopathy, nephropathy, DKA) are the dominant issues of the second decade.

**Quality of life impact:** Not formally studied with validated instruments (no EQ-5D/SF-36/PROMIS data identified for RMS specifically); qualitatively, disease burden is severe — recurrent hospitalizations for DKA, growth failure, dysmorphic features affecting social functioning, and early mortality risk dominate the clinical picture. No disease-specific QOL studies were found.

---

## 4. Genetic/Molecular Information

**Causal gene:** *INSR* (HGNC:6091; OMIM *147670), chromosome 19p13.2. Encodes a heterotetrameric receptor tyrosine kinase: preproprotein of 1,382 amino acids processed into two extracellular α-subunits (731 aa each, encoded by exons 1–11, insulin-binding) and two transmembrane β-subunits (620 aa each, encoded by exons 12–22, intracellular tyrosine kinase domain) linked by disulfide bonds into an α₂β₂ heterotetramer.

**Variant classification (ACMG/AMP context):** Pathogenic/likely pathogenic biallelic variants required for diagnosis per GeneReviews diagnostic criteria (clinical + molecular confirmation). Sequence analysis (missense, nonsense, splice-site, small indels) detects >90% of pathogenic variants; gene-targeted deletion/duplication analysis accounts for <10%.

**Variant types observed (PMC11216847, n=55 variants across 42 patients):**
- Missense: 72.7%
- Deletions: 10.9%
- Insertions: 1.8%
- Nonsense: 1.8%
- (remainder: other/splice-site types not separately itemized in the search-derived summary)
- Most recurrent: p.Glu238Lys (7.3%)
- Exon 2 most frequently mutated

**Allele frequency in population databases:** RMS-causing variants are, as expected for an ultra-rare autosomal recessive disease, present at very low or absent frequencies in gnomAD/1000 Genomes/ExAC; specific allele frequencies were not retrieved in this search pass and should be confirmed per-variant via gnomAD/ClinVar at curation time (e.g., ClinVar entries such as NM_000208.4(INSR):c.2480_2487del (p.Gln827fs) and c.394G>A (p.Gly132Ser) are annotated for RMS — [ClinVar RCV000015828](https://www.ncbi.nlm.nih.gov/clinvar/RCV000015828/), [ClinVar RCV000240670](https://www.ncbi.nlm.nih.gov/clinvar/RCV000240670/)).

**Somatic vs. germline:** Exclusively germline; no somatic mosaicism or acquired-mutation mechanism is described for RMS.

**Functional consequence:** Loss of function (LOF) — reduced receptor number at the cell surface and/or reduced receptor signaling function; GeneReviews' five-class mechanism list (above) captures the range from synthesis defects through accelerated degradation. This is a partial/hypomorphic LOF state compared to Donohue syndrome, which typically reflects near-complete loss of receptor function.

**Modifier genes:** None specifically validated; genotype-phenotype correlation is explicitly stated as absent in GeneReviews, implying that modifying genetic or environmental factors (not yet characterized) must account for phenotypic variability among carriers of similarly severe INSR lesions.

**Epigenetic information:** No RMS-specific DNA methylation, histone modification, or chromatin studies were identified in this search.

**Chromosomal abnormalities:** RMS is caused by point mutations/small indels in *INSR*, not by large-scale chromosomal rearrangements, aneuploidy, or translocation; no DECIPHER/ECARUCA structural variant entries specific to RMS were found in this pass.

**Molecular signaling mechanism (downstream of INSR):** Insulin binding to the extracellular α-subunits induces a conformational change that triggers β-subunit tyrosine kinase autophosphorylation. This recruits insulin receptor substrate (IRS) adaptor proteins, activating two principal downstream cascades:
- **PI3K/AKT pathway** — via IRS docking, mediates the majority of insulin's metabolic effects (GLUT4 translocation, glycogen synthesis, lipogenesis, suppression of gluconeogenesis)
- **Ras/Raf/MEK/MAPK pathway** — via IRS and Shc adaptors, mediates mitogenic/growth-regulatory effects and gene expression control

In RMS, loss-of-function *INSR* variants blunt this signaling cascade at its origin, producing profound peripheral (metabolic) insulin resistance while — paradoxically — some tissues (notably ovarian theca cells) retain enough residual insulin/IGF-1 receptor crosstalk to mediate hyperandrogenism: insulin (at pathologically elevated concentrations) and IGF-1 both stimulate ovarian theca-cell androgen synthesis via cytochrome P450c17α (CYP17A1) upregulation and synergy with LH, explaining the hyperandrogenic/polycystic ovarian phenotype despite systemic insulin resistance — a mechanism paralleled in the broader PCOS literature on "selective insulin resistance" in which the MAPK/mitogenic arm and ovarian steroidogenic insulin sensitivity are relatively preserved even as the PI3K/AKT metabolic arm is impaired.

---

## 5. Environmental Information

RMS is a fully penetrant monogenic disorder; no environmental toxin, occupational exposure, lifestyle factor, or infectious trigger is implicated in disease causation. Environmental/behavioral factors are relevant only as modulators of the clinical course:
- Intercurrent infection and metabolic stress can precipitate diabetic ketoacidosis
- Dietary carbohydrate load and fasting state drive the paradoxical postprandial hyperglycemia / fasting hypoglycemia pattern
- No infectious agent is causally or precipitously linked to RMS in the literature surveyed

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered)

1. **Biallelic loss-of-function variants in *INSR*** (chromosome 19p13.2) → **leads to** reduced number and/or reduced function of cell-surface insulin receptors (via impaired receptor synthesis, membrane trafficking, insulin-binding affinity, tyrosine kinase activity, or accelerated degradation — GeneReviews' five mechanistic classes).
2. Deficient functional insulin receptor at target tissues (adipocyte, myocyte, hepatocyte) → **results in** markedly reduced insulin-stimulated PI3K/AKT signaling → **leads to** impaired GLUT4-mediated glucose uptake in muscle/fat and failure to suppress hepatic gluconeogenesis — the core defect of severe peripheral insulin resistance (inferred from general INSR-IRS-PI3K-AKT pathway biology, extrapolated to RMS by the clinical response pattern).
3. Peripheral insulin resistance → **triggers** compensatory pancreatic beta-cell hypersecretion of insulin → **results in** the extreme hyperinsulinemia that is a biochemical hallmark of RMS (median fasting insulin 300 μIU/mL in the pooled cohort, up to 861 μIU/mL, versus a normal range of 5–20 μIU/mL).
4. In infancy/early childhood, residual insulin action combined with massive hyperinsulinemia produces a **paradoxical glycemic pattern**: fasting hypoglycemia (from insulin's residual/non-canonical suppressive effects, e.g., via IGF-1 receptor cross-activation at supraphysiologic insulin concentrations) alternating with postprandial hyperglycemia (from failure of insulin-stimulated glucose disposal) — this step is well described clinically but its precise molecular basis (differential receptor reserve across tissues/pathways) is partly inferred.
5. Over the first decade, beta-cell secretory capacity declines (a form of "insulin resistance exhaustion" / relative beta-cell failure under chronic hyperstimulation) → **leads to** a shift from hyperinsulinemic hypoglycemia toward sustained hyperglycemia and **overt insulin-resistant diabetes mellitus** (diagnosed in ~76% of evaluable cases by a mean age of 9.4 years).
6. Progressive hyperglycemia, especially with intercurrent illness or reduced caloric intake, → **precipitates recurrent diabetic ketoacidosis**, which is the leading proximate cause of death, typically in the second to third decade of life.
7. **Branch — ovarian axis:** Extreme hyperinsulinemia, acting through residual insulin receptor and cross-reactive IGF-1 receptor signaling in ovarian theca cells (a tissue where the MAPK/steroidogenic arm of insulin/IGF-1 signaling is relatively preserved despite systemic PI3K/AKT-mediated resistance), → **stimulates** CYP17A1 (P450c17α) activity and synergizes with LH → **results in** ovarian hyperandrogenism, enlarged/polycystic ovaries, clitoromegaly, and hirsutism (mechanism extrapolated from the general PCOS/insulin-resistance literature; not RMS-specific mechanistic studies).
8. **Branch — growth axis:** Loss of INSR function, combined with a state of growth hormone resistance (elevated basal GH with low-normal IGF-1 in reported cases, consistent with GH resistance), → **contributes to** severe growth retardation/short stature; IGF-1 receptor signaling (a partially redundant pathway to INSR) is insufficient to compensate fully, and neither exogenous growth hormone nor standard-dose IGF-1 corrects the growth deficit (documented specifically as "lack of effect of growth hormone and insulin-like growth factor-I" in a landmark natural-history report).
9. **Branch — dermatologic/soft tissue overgrowth:** Chronic extreme hyperinsulinemia → **cross-activates** IGF-1 receptors on keratinocytes and dermal fibroblasts (which retain responsiveness to insulin at pathological concentrations) → **produces** acanthosis nigricans (epidermal hyperkeratosis/hyperpigmentation), hypertrichosis, gingival hyperplasia, and soft-tissue/dental overgrowth — the shared mechanistic explanation across the INSR-SIRS spectrum (Donohue, RMS, Type A), inferred from receptor cross-reactivity biology rather than RMS-specific mechanistic proof.
10. **Branch — pineal gland:** Pineal hyperplasia with increased urinary melatonin metabolite excretion is reported, but the precise causal link between INSR loss-of-function and pineal overgrowth is not mechanistically established in the literature reviewed — this remains a descriptive association, not a demonstrated causal step.
11. **Branch — renal:** Nephrocalcinosis and other renal abnormalities occur in a substantial proportion of patients; a dedicated study (PMC4369119, "Insulin Receptor and the Kidney: Nephrocalcinosis in Patients with Recessive INSR Mutations") proposes a direct role for insulin receptor signaling in renal tubular calcium handling, independent of the diabetic state — i.e., a tissue-autonomous consequence of INSR loss rather than a secondary complication of hyperglycemia (a distinguishing mechanistic claim worth flagging as its own pathophysiology node).

### Molecular pathways
- **PI3K/AKT** (KEGG insulin signaling pathway; GO:0043491 protein kinase B signaling) — principal metabolic arm, impaired in RMS
- **Ras/Raf/MEK/MAPK** (GO:0000165 MAPK cascade) — mitogenic/growth arm, relatively spared, implicated in the paradoxical growth-promoting, hyperandrogenic, and soft-tissue overgrowth phenotypes
- **IGF-1 receptor (IGF1R) cross-signaling** — proposed compensatory/pathogenic pathway at supraphysiologic insulin concentrations

### Cellular processes
- Compensatory pancreatic beta-cell hyperinsulin secretion, followed by secretory exhaustion (GO:0030073 insulin secretion)
- Impaired GLUT4 translocation in adipocytes/myocytes (GO:0071384 cellular response to corticosteroid; more precisely GO:0035774 positive regulation of insulin secretion involved in cellular response to glucose stimulus is adjacent — GLUT4 translocation is GO:0071286-adjacent; suggest GO:0044381 glucose import in response to insulin stimulus)
- Ovarian theca cell androgen biosynthesis (GO:0006702 androgen biosynthetic process)
- Keratinocyte/fibroblast hyperproliferation underlying acanthosis nigricans

### Cell types (CL terms, suggested)
- CL:0000169 type B pancreatic cell (beta cell) — compensatory hyperinsulinemia/exhaustion
- CL:0002327 mammary epithelial cell — not relevant; more relevant: CL:0000038 erythroid progenitor — not relevant
- CL:0000499 stromal cell of ovary / theca cell (no precise CL ID retrieved in this pass; note as "ovarian theca cell" free text if no exact term validates)
- CL:0000312 keratinocyte — acanthosis nigricans
- CL:0000057 fibroblast — dermal/gingival overgrowth
- CL:0000182 hepatocyte — hepatic glucose overproduction

### Anatomical involvement (see Section 7 for detail)

### Molecular profiling / omics
No transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial-omics studies specific to RMS patient tissue were identified in this search. This is consistent with the disease's rarity and the case-report-dominated evidence base; RMS mechanism is inferred largely from the well-characterized general insulin-signaling literature (PI3K/AKT, MAPK) rather than disease-specific omics data.

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- Endocrine pancreas (compensatory beta-cell hyperfunction, later failure)
- Adipose tissue (lipoatrophy/paucity of subcutaneous fat)
- Skin/integument (acanthosis nigricans, hypertrichosis)
- Reproductive system — ovaries (enlargement, polycystic change, hyperandrogenism), external genitalia (clitoromegaly/phallic enlargement)
- Kidney (nephrocalcinosis, organomegaly)
- Pineal gland (hyperplasia)
- Dentition/oral cavity (premature/dysplastic teeth, gingival hyperplasia, furrowed tongue)
- Skeletal system (growth retardation, short stature)

**Secondary/complication-level organ involvement:**
- Cardiovascular system (rare congenital defects such as ASD reported; hypertrophic cardiomyopathy more classically part of the Donohue end of the spectrum)
- Liver, spleen (organomegaly in some cases)
- Eyes (diabetic retinopathy as a late microvascular complication)

**Body systems involved:** Endocrine, integumentary, reproductive, renal, dental/craniofacial, skeletal/growth, and (secondarily) cardiovascular and ophthalmologic systems.

**Suggested UBERON terms:**
- UBERON:0001264 pancreas
- UBERON:0001013 adipose tissue
- UBERON:0002097 skin of body
- UBERON:0000992 ovary
- UBERON:0002113 kidney
- UBERON:0002298 pineal gland
- UBERON:0001091 tooth / UBERON:0001754 gingiva
- UBERON:0000948 heart

**Tissue/cell level:** Epidermis/keratinocytes (acanthosis nigricans), ovarian theca cell layer, renal tubular epithelium (nephrocalcinosis), pancreatic islet beta cells, dermal fibroblasts and hair follicles (hypertrichosis).

**Subcellular level:** Plasma membrane insulin receptor (reduced density/trafficking defect — GO:0005886 plasma membrane; GO:0005899 insulin receptor complex); endoplasmic reticulum (receptor biosynthesis/folding defects in some variant classes — GO:0005783).

**Localization/laterality:** Not applicable — RMS manifestations are bilateral/systemic rather than lateralized.

---

## 8. Temporal Development

**Onset:** Congenital/neonatal-to-infantile onset of insulin resistance biochemistry and dysmorphic features; failure to thrive, early dentition, and acanthosis nigricans typically noted in infancy to early childhood. Onset pattern is insidious/chronic rather than acute, though DKA episodes are acute events superimposed on the chronic disease course.

**Progression:**
- **Early stage (infancy–early childhood):** Predominantly hyperinsulinemic with fasting hypoglycemia/postprandial hyperglycemia; dysmorphic and dermatologic features become apparent.
- **Intermediate stage (childhood, mean age ~9.4 years):** Overt diabetes mellitus manifests as beta-cell compensation begins to fail (diagnosed in ~76% of evaluable pooled cases by age 23, most well before that).
- **Late/advanced stage (second–third decade):** Recurrent DKA, microvascular complications (nephropathy, retinopathy), and in females, hyperandrogenic ovarian disease; this stage carries the highest mortality risk.
- Disease course is **progressive** rather than relapsing-remitting, though glycemic control fluctuates episodically (hypoglycemia early, hyperglycemia/DKA later) — a shifting rather than static progressive pattern.
- **Duration:** Chronic, lifelong; RMS patients, unlike those with Donohue syndrome (who typically die before age 1), commonly survive into the second or third decade, with some reaching adulthood.

**Remission patterns:** No spontaneous remission is described; treatment (leptin, IGF-1, insulin, SGLT2 inhibitors) can improve glycemic control (partial biochemical "remission" of hyperglycemia) but does not cure or reverse the underlying receptor defect.

**Critical periods:** The transition around age ~1 year (from a hyperinsulinemic/hypoglycemia-predominant pattern to a hyperglycemia-predominant pattern) and the pubertal transition (onset of hyperandrogenic ovarian disease) are noted as clinically important inflection points warranting intensified monitoring per GeneReviews surveillance recommendations.

---

## 9. Inheritance and Population

**Epidemiology:**
- RMS is exceptionally rare; NORD states "fewer than 50 patients have been reported in the medical literature," and other sources describe an incidence of "less than 1 in 1,000,000." No formal prevalence/incidence estimate from a population registry exists. Donohue syndrome, the more severe allelic disorder, is separately estimated at 1:1,000,000 births (GeneReviews); RMS prevalence is presumed similar or somewhat higher given its comparatively better survival (ascertainment bias toward RMS in the literature).
- The pooled 42-patient cohort's geographic distribution: Asia 33.3%, Europe 33.3%, North America 26.2%, South America 4.8%, Oceania 2.4% — reflecting publication/ascertainment patterns rather than true population prevalence.

**Inheritance pattern:** Autosomal recessive. Siblings of an affected individual have (per GeneReviews) a 25% chance of being affected (biallelic), 50% chance of being heterozygous carriers, and 25% chance of inheriting neither variant.

**Penetrance:** Complete for the biallelic genotype (all reported biallelic *INSR* LOF carriers manifest disease), though severity is variable ("variable expressivity" per NORD).

**Expressivity:** Variable — phenotype ranges along the INSR-SIRS continuum even among patients with severe biallelic variants, and no genotype-phenotype correlation has been established.

**Genetic anticipation:** Not described/applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for RMS in this search pass.

**Founder effects:** Documented founder variants include c.167T>C (p.Ile56Thr) in the Israeli Druze population and c.3003_3012del10insGGAAG in Tunisian families (GeneReviews).

**Consanguinity:** RMS pedigrees are frequently consanguineous, consistent with autosomal recessive inheritance of an ultra-rare allele; several case reports explicitly note parental consanguinity.

**Carrier frequency:** Not established in population databases given the ultra-rarity and allelic heterogeneity of causal *INSR* variants; heterozygous carriers are generally asymptomatic but may show mild features of the allelic Type A insulin resistance phenotype, and heterozygous females have increased gestational diabetes risk.

**Population demographics:**
- Sex ratio: roughly equal, slightly female-predominant in the pooled cohort — 57.1% female (24/42) vs. 42.9% male (18/42); NORD states the condition "affects males and females equally."
- No specific ethnic/geographic endemicity beyond the founder populations noted above; cases have been reported across Asia, Europe, the Americas, and Oceania.
- Age distribution of affected individuals in the literature: diagnosis from birth to early 20s, with a mean diagnostic age (for diabetes specifically) of 9.41 years.

---

## 10. Diagnostics

**Clinical recognition:** Diagnosis is suspected from the combination of extreme fasting hyperinsulinemia (often >100–300+ μIU/mL, orders of magnitude above the normal 5–20 μIU/mL range) with disproportionately modest or fluctuating glucose abnormalities, plus characteristic dysmorphic features (coarse facies, acanthosis nigricans, hypertrichosis, dental anomalies, growth retardation).

**Laboratory tests:**
- Fasting glucose, insulin, C-peptide (markedly elevated insulin/C-peptide with hyperinsulinemia disproportionate to glucose level is the key biochemical signature)
- HbA1c (mean 9.35% in the pooled cohort at diagnosis of diabetes; normal 4–6%)
- Lipid panel — characteristically **low triglycerides and elevated HDL** (distinguishing RMS from acquired/lipodystrophy-type insulin resistance, which typically shows high triglycerides/low HDL)
- Adiponectin — reported elevated in RMS
- Thyroid function (surveillance for hypothyroidism)
- Androgen panel in postpubertal females (testosterone, DHEA-S) for hyperandrogenism workup

**Imaging:**
- Pelvic/ovarian ultrasound (surveillance for ovarian enlargement/cysts, malignancy risk)
- Renal ultrasound (nephrocalcinosis surveillance)
- Echocardiography/cardiac MRI (cardiac surveillance, alternating modalities per GeneReviews protocol)
- Prenatal ultrasound findings (IUGR) can be an early clue in affected pregnancies

**Genetic testing (per GeneReviews):**
- Diagnosis requires characteristic clinical/laboratory/radiographic/prenatal findings **plus** identification of biallelic *INSR* pathogenic variants
- Sequence analysis of *INSR* detects >90% of pathogenic variants (missense, nonsense, splice-site, small indels)
- Gene-targeted deletion/duplication analysis (e.g., MLPA) detects the remaining <10% (larger structural variants)
- Multigene panels including *INSR* and phenocopy genes, or exome/genome sequencing, are used when the clinical presentation is ambiguous
- Genetic Testing Registry (GTR) lists clinical/research testing for this condition — [GTR C0271695](https://www.ncbi.nlm.nih.gov/gtr/conditions/C0271695/)

**Differential diagnosis** (per GeneReviews):
- **Donohue syndrome** — more severe allelic disorder; distinguished by extreme prenatal growth restriction, cardiomyopathy (~30% of infants), and death typically before age 1
- **Type A insulin resistance syndrome** — milder allelic disorder, usually heterozygous *INSR* variant, later onset (puberty+), less severe diabetes, normal survival
- **Silver-Russell syndrome** — IUGR and hypoglycemia but lacks hyperinsulinemia and RMS-characteristic facies
- **Familial hyperinsulinism** — hyperinsulinemic hypoglycemia but lacks dysmorphism/severe growth deficiency, and insulin levels are much lower than in INSR-SIRS
- **Berardinelli-Seip congenital lipodystrophy** — hyperinsulinemia and cardiomyopathy but with hyperlipidemia/hepatic steatosis and distinct fat-loss dysmorphism rather than INSR-driven features
- **IGF1R resistance** — IUGR/developmental delay but no hyperinsulinemia, only mild glucose intolerance

**Screening:** No population-based newborn screening program exists for RMS (it is not detected by standard metabolic newborn screening panels); diagnosis relies on clinical suspicion. Cascade/family genetic testing is appropriate once a proband's biallelic *INSR* variants are identified, and prenatal/preimplantation testing can be offered in known-carrier families.

---

## 11. Outcome/Prognosis

**Survival and mortality:** RMS carries a poor but variable prognosis. Multiple sources converge on death typically occurring in the **second to third decade of life**, most commonly due to **diabetic ketoacidosis and/or severe infection**. In contrast to Donohue syndrome (death usually <1 year), RMS patients commonly survive into the teens or twenties, and some into their third decade — this is the key survival distinction between the two ends of the INSR-SIRS spectrum. Notably, the 42-patient pooled analysis reported that, aside from one 14-year-old who died of **pulmonary hypertension**, all other patients in that cohort were alive at time of reporting — though this reflects a survivorship/publication bias in a predominantly cross-sectional case-report literature rather than a true cohort-based mortality rate.

**Morbidity/complications:**
- Recurrent diabetic ketoacidosis
- Microvascular diabetic complications (retinopathy, nephropathy) emerging in the second decade
- Nephrocalcinosis (renal, potentially INSR-intrinsic rather than purely diabetes-driven)
- Ovarian complications — enlarged/polycystic ovaries, hyperandrogenism, and a documented concern for gynecologic malignancy (endometrial cancer surveillance recommended with abnormal vaginal bleeding per GeneReviews)
- Growth failure/short stature, often refractory to growth hormone or standard IGF-1 therapy
- Recurrent infections (a feature more prominent in Donohue syndrome but relevant across the spectrum)

**Quality of life:** Not formally quantified with validated instruments in the literature reviewed; disease burden is substantial given recurrent hospitalization, chronic dysmorphic features, and the psychosocial impact of a life-limiting rare disease in childhood/adolescence.

**Prognostic factors:** Degree of residual insulin receptor function (genotype severity) is the presumed principal driver of position along the Donohue–RMS–Type A severity spectrum, though no formal genotype-phenotype correlation has been validated. Access to advanced therapies (metreleptin, rhIGF-1, SGLT2 inhibitors) appears to improve glycemic control and may favorably influence long-term outcomes, though no controlled mortality-outcome data exist.

---

## 12. Treatment

There is no curative or disease-modifying therapy that restores insulin receptor function; management is supportive/symptomatic, aimed at glycemic stabilization, growth optimization, and complication prevention. NORD states plainly: "There is no specific treatment for individuals with Rabson-Mendenhall syndrome. The treatment of the disorder is directed toward the specific symptoms," and conventional high-dose insulin and standard insulin sensitizers are typically inadequate long-term.

**Pharmacotherapy:**
- **Insulin sensitizers (metformin, thiazolidinediones/pioglitazone)** — first-line per GeneReviews to reduce HbA1c, though efficacy wanes over time, requiring dose escalation (NCIT:C15986 Pharmacotherapy; therapeutic_agent metformin/pioglitazone)
- **High-dose insulin therapy** — required once oral agents fail; U-500 concentrated insulin recommended once doses exceed 200 units/day; extreme doses (up to 500 U/hour) documented during DKA in limited case reports
- **SGLT2 inhibitors (empagliflozin)** — emerging off-label adjunct; case reports show HbA1c reduction (e.g., 8.5%→7.1% over 10 months in one 11-year-old, with time-in-range improving from 47% to 74%) and improved time-in-range independent of insulin receptor pathway, since SGLT2 inhibition works via renal glucose excretion — [PMC11228259](https://pmc.ncbi.nlm.nih.gov/articles/PMC11228259/), [PMC11999824](https://pmc.ncbi.nlm.nih.gov/articles/PMC11999824/)
- **GLP-1/GIP receptor agonists (tirzepatide)** — a 2026 case report describes two genetically confirmed RMS patients treated with subcutaneous tirzepatide (2.5–3.3 mg weekly) for 3 months, reporting improved glycemic control — [Frontiers in Endocrinology 2026](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1945251/full)

**Advanced/targeted therapeutics:**
- **Metreleptin (recombinant leptin)** — FDA-approved for generalized lipodystrophy, used off-label in RMS. A controlled NIH natural-history comparison (9 metreleptin-treated vs. 7 untreated patients) found the metreleptin group maintained significantly lower HbA1c long-term (LSM difference 1.8%, P=0.007), with a 1.4% ± 1.1% A1c reduction at 12 months (P=0.006) versus a 0.2% increase in untreated controls; effect attributed to appetite suppression and lower BMI/weight (Δweight SDS −1.1±0.5, ΔBMI SDS −1.3±0.6, both P=0.0001) rather than direct insulin-pathway restoration. No significant renal-function benefit or harm was observed (24-hr urine protein/albumin, eGFR unchanged between groups). A tradeoff was noted: lower BMI after metreleptin may worsen growth hormone resistance, yielding a null effect on IGF-1/growth despite improved glycemia — [JCEM 2022](https://academic.oup.com/jcem/article/107/3/e1032/6413714)
- **Recombinant human IGF-1 (rhIGF-1, mecasermin)** — used particularly for DKA/severe metabolic decompensation and to bypass the defective insulin receptor via IGF1R signaling; benefits are variable and often modest, with continuous subcutaneous pump infusion reported as more effective than twice-daily injection in at least one case; does not prevent eventual progression to diabetes; potential adverse effects include theoretical malignancy risk from chronic IGF1R stimulation — [PMC5983765 (mecasermin review)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5983765/), [JCEM 2025 clinical spectrum with rhIGF-1](https://academic.oup.com/jcem/article/111/7/2049/8443987)
- **Growth hormone therapy** — an early natural-history study specifically documented "lack of effect of growth hormone and insulin-like growth factor-I" on the growth deficit in RMS, indicating GH resistance in this condition (JCEM, historical citation; PMID retrieval recommended at curation)

**Hormonal/hyperandrogenism management:**
- Oral contraceptives, antiandrogens (flutamide, spironolactone), 5-alpha-reductase inhibitors (finasteride), and GnRH agonists for ovarian hyperandrogenism (NCIT:C15986 Pharmacotherapy; multiple agent classes)
- Gonadectomy considered for markedly enlarged ovaries causing respiratory compromise or malignancy concern (NCIT:C15329 Surgical Procedure)

**Endocrine surveillance-driven treatment:** Standard levothyroxine replacement for documented hypothyroidism.

**Supportive/rehabilitative care:** Coordinated multidisciplinary management (pediatric endocrinology, dentistry, nutrition, cardiology) is recommended given the multisystem nature of the disease; dietary management (frequent feeding, protein-enriched evening feeds in infancy) mirrors strategies from the more severe Donohue syndrome end of the spectrum to prevent hypoglycemia.

**Experimental/investigational:** No RMS-specific gene therapy, CRISPR, cell therapy, or RNA-based (ASO/siRNA) therapeutic is in clinical development per the literature reviewed; anti-insulin receptor monoclonal antibody strategies have been explored preclinically in mouse models of human insulin receptoropathy (biorxiv preprint) but have not reached human RMS trials.

**Treatment outcomes summary (from the 42-patient pooled cohort):** Among 26 patients with treatment data — oral hypoglycemic agents alone in 57.7% (15/26), combined insulin + oral agents in 34.6% (9/26), and insulin monotherapy in 7.7% (2/26) — reflecting real-world heterogeneity in regimen choice.

**Suggested NCIT terms:** NCIT:C15986 (Pharmacotherapy), NCIT:C93352 (Targeted Therapy) for GLP-1/SGLT2/leptin agents, NCIT:C15329 (Surgical Procedure) for gonadectomy, NCIT:C15240 (Genetic Counseling).

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense — as a monogenic recessive disorder, primary prevention is limited to reproductive genetic counseling and carrier screening in at-risk (especially consanguineous or founder-population) families, rather than modifiable risk-factor reduction.

**Secondary prevention:** Early clinical recognition (dysmorphic features, hyperinsulinemia pattern) and prompt genetic confirmation allow earlier initiation of glycemic surveillance and treatment, potentially reducing the frequency/severity of DKA episodes; GeneReviews' structured surveillance protocol (glucose/HbA1c/insulin/C-peptide every 3 months; thyroid/androgen labs every 6 months; ovarian ultrasound every 3 months until age 2 then every 6 months; cardiac imaging every 6 months until age 2 then annually; renal assessment every 6 months; developmental assessment every 3 months) functions as a structured secondary-prevention framework to catch complications early.

**Tertiary prevention:** Aggressive glycemic management (insulin, adjunctive SGLT2i/GLP-1 agonists/metreleptin) aims to prevent progression to microvascular complications and recurrent DKA in patients who already have the disease.

**Genetic counseling/screening:** Carrier testing and prenatal/preimplantation genetic diagnosis are appropriate in families with a known proband, given the 25% recurrence risk per pregnancy in carrier x carrier matings; genetic counseling should also address the increased gestational diabetes risk in heterozygous *INSR* carrier females.

**Public health/behavioral:** No population-level public health intervention applies given the disease's extreme rarity and purely genetic etiology; there is no vaccine, environmental intervention, or lifestyle-based primary prevention strategy.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife counterpart of RMS specifically was identified in this search (no OMIA entry located in this pass); INSR-related disease in domestic/companion animals was not surfaced by the queries run. This gap should be checked directly against OMIA (Online Mendelian Inheritance in Animals) at curation time, as spontaneous *Insr* loss-of-function disease in animals is not well documented in the general veterinary literature. Given the essential, highly conserved role of the insulin receptor across mammals, a naturally occurring biallelic-null phenotype would be expected to be severe/lethal (paralleling Donohue syndrome), which may explain the absence of reported natural veterinary cases (a plausible inference, not directly evidenced in this search).

**Orthologous gene:** Mouse *Insr* (MGI:96575), rat *Insr* (RGD:2916) — both extensively studied in engineered (not naturally occurring) knockout models (see Section 15).

---

## 15. Model Organisms

**Genetically engineered mouse models (tissue-specific *Insr* knockouts)** — these model components of insulin resistance but do not fully recapitulate the multisystem human RMS phenotype (dysmorphism, pineal hyperplasia, dental anomalies), since global germline *Insr* knockout in mice is neonatally lethal (paralleling Donohue syndrome severity) and most published models are conditional/tissue-specific:

- **Muscle-specific knockout (MIRKO):** >90% decrease in insulin receptor kinase activity and reduced insulin-dependent glucose uptake in muscle, yet mice do **not** develop diabetes — illustrating compensation by other tissues (Physiological Reviews review, JCI review of knockout models)
- **Liver-specific knockout (LIRKO):** Dramatic insulin resistance, severe glucose intolerance, failure of insulin to suppress hepatic glucose output, and marked hyperinsulinemia from both increased secretion and decreased clearance — the closest single-tissue model to the hyperglycemia/hyperinsulinemia biochemistry of RMS
- **Adipose-specific knockout (FIRKO):** Protected from obesity and glucose intolerance — illustrating that adipose *Insr* loss alone does not reproduce human disease severity
- **Beta-cell-specific *Insr*/*Igf1r* double knockout:** Develops diabetes, whereas single-gene knockouts show only mild phenotypes — demonstrating redundancy between insulin and IGF-1 receptor signaling in beta cells, mechanistically relevant to why IGF-1-based therapies (mecasermin) have been tried in human RMS
- **"Humanized" *Insr* knock-in models** carrying patient-derived *INSR* variants have been used preclinically to test anti-insulin-receptor antibody therapeutics as a potential novel approach to insulin receptoropathy (bioRxiv preprint, "Anti-insulin receptor antibodies improve hyperglycaemia in a mouse model of human insulin receptoropathy") — this is the most disease-specific (as opposed to generic tissue-knockout) rodent model identified, though it remains preclinical.

**Model limitations:** No single mouse model reproduces the full RMS phenotype (growth retardation, acanthosis nigricans, pineal hyperplasia, dental/gingival overgrowth, ovarian hyperandrogenism, nephrocalcinosis) — tissue-specific knockouts isolate individual metabolic phenotypes (hepatic, muscle, adipose, beta-cell) but the integrated human syndrome (including its distinctive dermatologic and dysmorphic features driven by cross-reactive IGF1R signaling in skin/ovary/bone) has not been captured in a single validated animal model per the literature surveyed. Global germline *Insr*-null mice die perinatally from diabetic ketoacidosis, mirroring Donohue syndrome rather than the somewhat more viable RMS phenotype, and true patient-variant knock-in models recapitulating hypomorphic (partial-function) RMS-type alleles are not well represented in the literature retrieved.

**Research applications:** Tissue-specific knockout models remain the primary tool for dissecting which organ-specific consequences of INSR loss (hepatic glucose overproduction, muscle glucose uptake failure, adipose dysfunction, beta-cell secretory response) contribute to the integrated human phenotype, and knock-in/humanized models are beginning to support therapeutic antibody development as a potential future RMS treatment strategy.

**Resource databases for follow-up:** MGI (Mouse Genome Informatics) for *Insr* allele catalog; IMPC/KOMP for available knockout/conditional lines.

---

## Summary of Key Ontology Term Suggestions for KB Curation

- **Gene:** hgnc:6091 (INSR)
- **MONDO:** MONDO:0009874
- **OMIM:** 262190
- **ORPHA:** 769
- **HP terms:** HP:0000956 (Acanthosis nigricans), HP:0001510 (Growth delay), HP:0000707 (Dentition abnormality), HP:0000998 (Hirsutism), HP:0000121 (Nephrocalcinosis), HP:0000138 (Ovarian cyst), HP:0000023 (Hyperandrogenism), HP:0001943 (Hypoglycemia), HP:0003074 (Hyperglycemia), HP:0000857 (Insulin-resistant diabetes mellitus), HP:0000280 (Coarse facial features)
- **GO (biological process):** insulin receptor signaling pathway (GO:0008286), PI3K/AKT signaling, MAPK cascade (GO:0000165), androgen biosynthetic process (GO:0006702)
- **CL:** CL:0000169 (type B pancreatic cell), CL:0000312 (keratinocyte), CL:0000057 (fibroblast)
- **UBERON:** UBERON:0001264 (pancreas), UBERON:0000992 (ovary), UBERON:0002113 (kidney), UBERON:0002298 (pineal gland), UBERON:0001013 (adipose tissue)
- **NCIT (treatment):** NCIT:C15986 (Pharmacotherapy), NCIT:C15329 (Surgical Procedure), NCIT:C93352 (Targeted Therapy)

---

## Sources

- [OMIM 262190 — Pineal Hyperplasia, Insulin-Resistant Diabetes Mellitus, and Somatic Abnormalities](https://www.omim.org/entry/262190)
- [OMIM 147670 — INSULIN RECEPTOR; INSR](https://omim.org/entry/147670)
- [Orphanet: Rabson-Mendenhall syndrome (ORPHA:769)](https://www.orpha.net/en/disease/detail/769)
- [GeneReviews — INSR-Related Severe Insulin Resistance Syndrome (NBK476444)](https://www.ncbi.nlm.nih.gov/books/NBK476444/)
- [NORD — Rabson-Mendenhall Syndrome](https://rarediseases.org/rare-diseases/rabson-mendenhall-syndrome/)
- [Rabson-Mendenhall Syndrome: Analysis of the Clinical Characteristics and Gene Mutations in 42 Patients (PMC11216847)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11216847/)
- [Long-Term Effects of Metreleptin in Rabson-Mendenhall Syndrome on Glycemia, Growth, and Kidney Function — JCEM 2022 (PMID/DOI via academic.oup.com)](https://academic.oup.com/jcem/article/107/3/e1032/6413714)
- [Case report: A case of Rabson–Mendenhall syndrome: long-term follow-up and therapeutic management with empagliflozin (PMC11228259)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11228259/)
- [Case Report: Long-term effects of empagliflozin on glycemia and renal function in RMS (PMC11999824)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11999824/)
- [Frontiers in Endocrinology 2026 — Case Report: Tirzepatide improves glycemic control in Rabson–Mendenhall syndrome](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1945251/full)
- [Clinical spectrum of extreme insulin resistance syndromes treated with rhIGF-1 — JCEM 2025](https://academic.oup.com/jcem/article/111/7/2049/8443987)
- [Mecasermin in Insulin Receptor-Related Severe Insulin Resistance Syndromes: Case Report and Review of the Literature (PMC5983765)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5983765/)
- [Insulin Receptor and the Kidney: Nephrocalcinosis in Patients with Recessive INSR Mutations (PMC4369119)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4369119/)
- [Genealogical Rabson-Mendenhall syndrome caused by INSR gene mutation — PubMed 40499531](https://pubmed.ncbi.nlm.nih.gov/40499531/)
- [Syndrome of Extreme Insulin Resistance (Rabson-Mendenhall Phenotype) with Atrial Septal Defect (PMC3628395)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3628395/)
- [Insulin, Insulin Everywhere: A Rare Case Report of Rabson-Mendenhall Syndrome (PMC7936575)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7936575/)
- [MedGen — Rabson-Mendenhall syndrome (C0271695)](https://www.ncbi.nlm.nih.gov/medgen/78783)
- [NIH Genetic Testing Registry — Rabson-Mendenhall syndrome](https://www.ncbi.nlm.nih.gov/gtr/conditions/C0271695/)
- [Insulin Resistance Directly Contributes to Androgenic Potential Within Ovarian Theca Cells — Fertility and Sterility](https://www.sciencedirect.com/science/article/pii/S0015028208005578)
- [The Insulin Receptor and Its Signal Transduction Network — Endotext (NBK378978)](https://www.ncbi.nlm.nih.gov/books/NBK378978/)
- [Mouse Models of Insulin Resistance — Physiological Reviews](https://journals.physiology.org/doi/full/10.1152/physrev.00032.2003)
- [Insights into insulin resistance and type 2 diabetes from knockout mouse models — JCI](https://www.jci.org/articles/view/10830)
- [ClinVar RCV000015828 — NM_000208.4(INSR):c.2480_2487del](https://www.ncbi.nlm.nih.gov/clinvar/RCV000015828/)
- [ClinVar RCV000240670 — NM_000208.4(INSR):c.394G>A](https://www.ncbi.nlm.nih.gov/clinvar/RCV000240670/)
- [ClinVar RCV001128689.2 — NM_000208.4(INSR):c.*2568G>A](https://www.ncbi.nlm.nih.gov/clinvar/RCV001128689.2/)

**Note on evidence quality:** This report is compiled from web search and web-fetch results, not from primary-source PDF retrieval or PMID-level abstract verification. Per dismech's evidence policy, every claim above should be treated as a **lead** requiring verification against the primary source (exact PMID, exact quoted snippet) before being entered into a KB YAML evidence block — several figures (e.g., specific percentages from the 42-patient meta-analysis, the metreleptin trial statistics) were extracted via WebFetch summarization rather than direct primary-text quotation and must be re-confirmed against the original PMC full text with `just fetch-reference` before citing.