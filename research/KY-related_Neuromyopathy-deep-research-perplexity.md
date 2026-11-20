---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-06T14:53:52.068983'
end_time: '2026-11-06T15:00:01.876108'
duration_seconds: 369.81
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: KY-related Neuromyopathy
  mondo_id: MONDO:1010194
  category: Mendelian
  causal_genes: KY
  omim_id: not recorded
  synonyms: KY-related myopathy; myofibrillar myopathy 7; kyphoscoliosis peptidase
    deficiency
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 20
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 4
  validator_version: 0.5.1
term_validation:
  total_terms: 5
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  unresolvable_prefixes:
  - MGI
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KY-related Neuromyopathy
- **MONDO ID:** MONDO:1010194 (if available)
- **Causal gene(s):** KY
- **OMIM:** not recorded
- **Synonyms:** KY-related myopathy; myofibrillar myopathy 7; kyphoscoliosis peptidase deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **KY-related Neuromyopathy** covering all of the
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

# KY-related neuromyopathy (KY-related myopathy / myofibrillar myopathy 7)

KY-related neuromyopathy is a rare, autosomal recessive neuromuscular disorder caused by biallelic pathogenic variants in the **KY** gene, which encodes the kyphoscoliosis peptidase, a transglutaminase-like protein involved in muscle development and neuromuscular junction maturation.[1][7][9] Clinically, KY-related neuromyopathy spans a spectrum that includes congenital myopathy, classic myofibrillar myopathy type 7 (MFM7), and hereditary spastic paraplegia presentations, all unified by early-onset, slowly progressive muscle weakness predominantly affecting the lower limbs, frequent foot deformities (notably pes cavus and equinovarus), and multiple joint contractures.[6][11][15] Histopathologically, muscle biopsies show myofibrillar disorganization, thickened Z-discs, nemaline-rod–like material, eosinophilic sarcoplasmic inclusions positive for KY and filamin C, and focal depletion of mitochondria, defining a distinctive **myofibrillar myopathy** phenotype with elements of congenital myopathy.[6][15] The disorder is extremely rare; all reported families to date have arisen in consanguineous backgrounds, and many variants are private or population-specific loss-of-function alleles such as nonsense, frameshift, and splice-site mutations, with more recent reports describing the first disease-causing missense variants and suggesting that KY’s critical function in human muscle is at least partly independent of its predicted catalytic triad.[3][6][16] No disease-modifying treatment currently exists; management is supportive and orthopedic, while mechanistic insights from human cases and the kyphoscoliotic mouse model underscore KY’s role at the sarcomeric Z-disc and neuromuscular junction, providing a basis for future gene- or protein-based therapies.[1][9][17]

## 1. Disease information

### 1.1 Definition and clinical overview

KY-related neuromyopathy is best conceptualized as a KY gene–defined Mendelian neuromuscular disease entity that encompasses myofibrillar myopathy 7 and related KY-deficiency phenotypes, rather than a single narrowly defined clinical syndrome.[6][11] The causal gene is **KY** (HGNC:26576), also known as *kyphoscoliosis peptidase* or MFM7, a protein-coding gene located on chromosome 3q22.2 and encoding a transglutaminase-like protein expressed predominantly in skeletal muscle and heart.[1][9][17] The disease was first recognized in humans in 2016, when Hedberg-Oldfors and colleagues reported a girl with an early-onset neuromuscular disorder due to a homozygous frameshift variant in KY; they wrote, “We describe a new early-onset neuromuscular disorder due to a homozygous loss-of-function variant in the kyphoscoliosis peptidase gene (KY).”[15] Subsequent reports have delineated KY-associated phenotypes ranging from congenital myopathy with structural sarcomeric abnormalities to classic myofibrillar myopathy and hereditary spastic paraplegia with prominent lower limb deformities.[6][11][13]

The most formalized clinical label within this spectrum is **myofibrillar myopathy 7 (MFM7)**, which OMIM designates as “Myopathy, myofibrillar, 7” (MIM 617114) and attributes to homozygous KY mutations.[7][20] MedGen defines MFM7 as “an autosomal recessive muscle disorder characterized by early childhood onset of slowly progressive muscle weakness that primarily affects the lower limbs and is associated with joint contractures.”[3][20] Malacards similarly describes “myopathy, myofibrillar, 7 (MFM7)” as a myofibrillar myopathy with a “material basis in homozygous mutation in the KY gene on chromosome 3q22.”[5] However, as emphasized in a 2025 series, “Homozygous KY variants have been described to cause congenital myopathy, myofibrillar myopathy type 7, and hereditary spastic paraplegia,” underscoring that KY-related neuromyopathy is a heterogeneous but gene-unified spectrum.[6]

Clinically, KY-related neuromyopathy manifests with early-onset difficulties in walking, distal and proximal muscle weakness (most prominent in the lower limbs), pes cavus or equinovarus deformities, reduced deep tendon reflexes, and progressive joint contractures involving ankles, knees, hips, elbows, and sometimes the spine.[6][11][15] Some patients develop kyphoscoliosis or hyperlordosis, while others show relatively spared paraspinal muscles despite marked limb involvement.[11][15][17] The tongue may be atrophic and lateralized, and in severe cases, respiratory involvement and scoliosis may develop, as described in the broader category of myofibrillar myopathies.[20] Muscle biopsies show a characteristic combination of myopathic changes, developmental myosin heavy chain expression in small fibers, thickened Z-discs, nemaline rod–like structures, myofibrillar degeneration, and eosinophilic cytoplasmic inclusions positive for KY and filamin C but negative for desmin.[6][15]

### 1.2 Nomenclature, identifiers, and classification

KY-related neuromyopathy sits at the intersection of gene-based and phenotype-based disease taxonomies. The template designation “KY-related neuromyopathy” appears to correspond to a MONDO disease entity that explicitly couples KY as the causal gene with a neuromuscular clinical category (likely MONDO:1010194 as given by the user), and overlaps with the more phenotype-focused MONDO term “myofibrillar myopathy 7” (MONDO:0014922), which MedGen and ClinVar map to KY.[12][20] OMIM’s primary phenotype entry for KY-related disease is **Myopathy, myofibrillar, 7 (MFM7)**, with MIM number 617114.[7] The corresponding KY gene entry in OMIM is “KY; kyphoscoliosis peptidase” (MIM 605739), which details cloning, expression, and the ky mouse model.[17]

Key identifiers and cross-references include the following. The causal gene **KY** has NCBI Gene ID 339855 and is located at chromosome 3q22.2 with 11 exons.[1][13] UniProt lists the protein as Q8NBH2, “kyphoscoliosis peptidase,” and the Alliance of Genome Resources uses the symbol KY with synonyms including FLJ33207 and MFM7.[8][9] MedGen’s concept ID for MFM7 is C4310711, linked to OMIM 617114 and MONDO:0014922.[3][12][20] The Genetic Testing Registry (GTR) lists “Myofibrillar myopathy 7” as a condition associated with KY and includes it under the alias “MFM7, KY.”[14] The disease is classified as a Mendelian, autosomal recessive myopathy within the broader category of myofibrillar myopathies and congenital myopathies.[3][5][7]

Common synonyms and alternative names include **myofibrillar myopathy 7**, **myopathy, myofibrillar, 7**, **MFM7**, **KY-related myopathy**, **KY-related neuromyopathy**, and **kyphoscoliosis peptidase deficiency**.[3][5][11][20] The term “kyphoscoliosis peptidase deficiency” emphasizes loss-of-function variants and echoes the mouse kyphoscoliosis phenotype, whereas “KY-related myopathy” is increasingly used in literature to encompass congenital myopathy and spastic paraplegia presentations that may not show classic myofibrillar pathology.[6][11][15] Some clinical series still reference the initial descriptive labels such as “novel congenital myopathy with core targetoid defects” for the first Acta Neuropathologica report of KY mutations.[2][7]

From the perspective of coding systems, KY-related neuromyopathy does not yet have a unique ICD-10 or ICD-11 code; patients are typically coded under generic categories such as “other primary myopathies” (for example, ICD-10 G71.2) or “other specified congenital myopathies,” depending on local practice. MeSH and other controlled vocabularies align KY-related neuromyopathy with the general term “Myofibrillar Myopathies,” which covers a heterogeneous group of diseases characterized by myofibrillar disintegration and protein aggregation.[4][20] The information currently available is largely derived from individual patient case reports and small case series, which have then been aggregated into disease-level resources such as OMIM, MedGen, Malacards, and the Alliance of Genome Resources.[3][5][7][9][11][15]

### 1.3 Evidence base and data sources

The knowledge base for KY-related neuromyopathy is built on a relatively small number of primary human clinical studies, supplemented by mechanistic work in mouse models and in vitro systems. The first human case with a KY loss-of-function variant was reported by Hedberg-Oldfors et al. in 2016, describing a 7.5-year-old girl with a homozygous c.1071delG variant.[15] Additional cases were described in two Arab-Israeli brothers with a nonsense variant (Y135X) and in a Kurdish girl with the same frameshift variant as the original Swedish patient, leading to the formal recognition of myofibrillar myopathy 7 as an autosomal recessive KY-related disorder in OMIM.[2][7][11][15] A 2018 Iranian case report identified a novel nonsense variant c.415C>T (p.R139X) in KY, further expanding the allelic spectrum.[13]

More recently, a 2022 study titled “Genotypic and phenotypic spectrum of Myofibrillar Myopathy 7 as a result of Kyphoscoliosis Peptidase deficiency: The first description of a missense mutation in KY and literature review” systematically reviewed published KY-related cases and provided the first evidence of disease-causing missense variants.[16] A 2025 J Neuromuscular Diseases article examined two families with a missense p.Cys243Arg variant and a splice-site variant c.710+1G>A, providing detailed muscle pathology and biochemical characterization of KY-deficient muscle.[6] Finally, a 2026 Human Molecular Genetics paper showed that a myofibrillar myopathy–associated KY protein promotes muscle fiber size rescue independent of its predicted catalytic triad, clarifying aspects of KY’s functional mechanism in muscle.[3]

These primary clinical studies are collated in OMIM, MedGen, and Malacards, which provide concise disease descriptions, inheritance patterns, and gene-disease associations.[3][5][7][20] NCBI Gene and the Alliance of Genome Resources integrate these human data with mouse model findings, while ClinVar catalogs specific KY variants and their clinical interpretations, including the c.1071del variant labeled as pathogenic for MFM7.[1][9][12][17] Advocacy and information sites such as myofibrillarmyopathy.org summarize the literature for patients and families, emphasizing autosomal recessive inheritance, consanguinity, and a spectrum of neuromuscular phenotypes associated with KY loss of function.[11] Overall, the evidence base is robust at the level of individual case documentation and mechanistic plausibility but remains limited in breadth due to the rarity of the condition and the small number of known families.

## 2. Etiology

### 2.1 Primary causal factors: KY gene mutations

The primary etiologic factor in KY-related neuromyopathy is germline, biallelic pathogenic variation in the **KY** gene. KY encodes kyphoscoliosis peptidase, a protein belonging to the transglutaminase-like superfamily, with predicted roles in muscle organ development and neuromuscular junction development.[1][9] NCBI Gene summarizes that “mutations in this gene are associated with myopathy, myofibrillar, 7,” and that the protein “is involved in the function, maturation and stabilization of the neuromuscular junction and may be required for normal muscle growth.”[1][9] OMIM similarly concludes that myofibrillar myopathy-7 “is caused by homozygous mutation in the KY gene on chromosome 3q22.”[7]

All definitively implicated variants to date are germline, autosomal, and inherited in a recessive manner, typically in homozygous form in the context of parental consanguinity.[7][11][13][15] The earliest human case carried a homozygous one-base deletion c.1071delG (p.Thr358Leufs*3), predicted to produce a truncated, nonfunctional protein.[15] In ClinVar, this variant is classified as pathogenic for myofibrillar myopathy 7, and the mutant transcript was shown to be expressed in skeletal muscle, indicating that nonsense-mediated decay does not fully eliminate it.[12][15] Other loss-of-function alleles include nonsense variants such as c.405C>A (p.Tyr135Ter) and c.415C>T (p.Arg139Ter) and a complex insertion causing a frameshift (p.Val18TyrfsTer56) associated with hereditary spastic paraplegia.[7][11][13]

The etiology of KY-related neuromyopathy is therefore fundamentally **genetic and monogenic**, driven by loss of KY function in skeletal muscle and possibly in other tissues such as heart and brain. There is currently no evidence that environmental factors, infectious agents, or acquired insults cause this disease in the absence of a KY mutation. Rather, environmental or lifestyle factors may modulate disease expression or progression in individuals with KY mutations, but these relationships remain speculative and unproven in human cohorts.

### 2.2 Genetic risk factors and variant spectrum

Within the genetic domain, the principal risk factor is being homozygous or compound heterozygous for a pathogenic KY variant. The known spectrum includes nonsense, frameshift, splice-site, and missense variants affecting conserved domains of the protein. The best-characterized alleles include:

A nonsense variant c.405C>A (p.Tyr135Ter) identified in two Arab-Israeli brothers with early-onset myopathy, pes cavus, weakness, and reduced reflexes, and classified as causing MFM7.[7][11] A frameshift c.1071delG (p.Thr358Leufs*3) identified in a Kurdish girl and in the original Swedish index case, both with early-onset generalized muscle weakness and limb-girdle involvement.[12][15] A nonsense variant c.415C>T (p.Arg139Ter) in an Iranian patient with lower limb deformity, muscular weakness, mild scoliosis, and equinovarus deformity, reported as a novel KY nonsense mutation.[13] A complex insertion c.51_52insTATCGACATGTGCTGTATCTATCGACAT (p.Val18TyrfsTer56) in twelve Arab-Bedouin individuals with hereditary spastic paraplegia, demonstrating that KY loss of function can cause a primarily upper motor neuron phenotype.[11] Missense and splice-site variants such as c.727T>C (p.Cys243Arg) and c.710+1G>A identified in recent families with early-onset myopathy, equinovarus deformity, kyphoscoliosis, and contractures.[6][16]

The 2022 spectrum paper emphasized that these variants cluster in functionally important regions of KY and that missense mutations affecting conserved residues can phenocopy truncating mutations, establishing missense KY variants as bona fide causes of MFM7.[16] The 2025 J Neuromuscular Diseases study further showed that the missense p.Cys243Arg variant and the splice-site variant markedly reduce KY protein expression, suggesting that the primary pathogenic mechanism is loss of protein function rather than a dominant-negative effect.[6] The 2026 Human Molecular Genetics paper demonstrated that a KY protein variant associated with MFM7 can still promote muscle fiber size rescue despite disruptions in its predicted catalytic triad, implying that regions outside the catalytic core mediate key structural or scaffolding roles.[3]

Population allele frequency data for KY variants remain limited. Most pathogenic variants are either absent or extremely rare in major databases such as gnomAD, Exome Variant Server, and 1000 Genomes, consistent with their identification in consanguineous families.[11][12][13][15] For example, the c.1071delG variant was not found in dbSNP, 1000 Genomes, Exome Variant Server, or ExAC when first described.[12][15] This scarcity supports their classification as pathogenic or likely pathogenic under ACMG/AMP guidelines, particularly when combined with segregation data, absence in controls, and functional plausibility.

There is currently no evidence for common susceptibility variants or polygenic risk involving KY. The disease appears strictly Mendelian, and the primary genetic risk resides in the presence of biallelic loss-of-function or severely hypomorphic KY mutations. No modifier genes have been conclusively identified, although the broader context of myofibrillar myopathy suggests that variation in other Z-disc or cytoskeletal proteins (for example, FLNC or LDB3) could modulate phenotype severity, as has been described for related diseases.[4][20]

### 2.3 Environmental and lifestyle risk factors

No specific environmental, occupational, or lifestyle risk factors have been identified for KY-related neuromyopathy. The disease presents in early childhood or adolescence in individuals with biallelic KY mutations, often in families with a high degree of consanguinity, and there is no evidence that toxin exposure, physical trauma, or infection triggers disease onset in the absence of genetic predisposition.[7][11][15] This contrasts with some acquired myopathies where infections, medications, or toxins are major etiologic contributors.

Nevertheless, environmental factors could influence disease trajectory in KY mutation carriers. For example, the ky mouse model demonstrates that kyphoscoliosis peptidase deficiency leads to impaired muscle hypertrophic responses to increased demand, even though adaptive fiber type shifts occur.[17] Blanco et al. noted that the ky mutant is “deficient in hypertrophic responses” while still able to shift fiber types under increased load, suggesting that excessive mechanical stress might exacerbate muscle damage in humans with KY deficiency.[17] However, no human studies have systematically correlated physical activity, occupational load, or specific environmental exposures with disease severity or progression.

Lifestyle aspects such as nutrition, exercise regimens, and weight management likely influence overall health and functional capacity in KY-related neuromyopathy, but these are general considerations for neuromuscular disease rather than KY-specific risk factors. There is no evidence that smoking, alcohol use, or particular diets either precipitate or protect against KY-related neuromyopathy beyond their generic effects on cardiovascular and musculoskeletal health.

### 2.4 Protective factors and gene–environment interactions

Given the rarity of KY-related neuromyopathy and the small number of reported families, no genetic protective factors or modifier alleles have been identified that clearly attenuate disease risk or severity. There are no documented cases of individuals with biallelic truncating KY variants who remain entirely asymptomatic into adulthood, though variability in age at onset and severity has been observed across the limited cohort.[6][11][13][15] This suggests high penetrance for severe loss-of-function variants, with expressivity shaped more by allelic heterogeneity (for example, truncating versus missense) and perhaps by uncharacterized modifiers than by known protective alleles.

Gene–environment interactions have not been substantiated in human KY-related neuromyopathy. The most plausible interactions, extrapolated from the ky mouse, involve mechanical load and neuromuscular junction stress. The kyphoscoliotic mouse exhibits a primary degenerative myopathy with deficient muscle hypertrophy in response to increased demand, indicating that elevated mechanical load leads to disproportionate degeneration in the absence of functional KY.[17] If similar mechanisms operate in humans, high-intensity repetitive use of affected muscles could accelerate weakness and structural damage, while carefully titrated, low-impact physiotherapy might support function without exacerbating degeneration. Yet these remain hypotheses, and formal studies have not tested them in patients.

In summary, KY-related neuromyopathy is a paradigmatic Mendelian disorder in which the etiologic architecture is dominated by biallelic KY mutations with minimal contribution from environmental or lifestyle factors, at least based on current evidence. The primary etiologic research focus moving forward is therefore on elucidating the full spectrum of KY variants, understanding genotype–phenotype correlations, and identifying potential genetic or molecular modifiers within muscle and neuromuscular junction pathways.

## 3. Phenotypes

### 3.1 Core neuromuscular phenotype

The core phenotype of KY-related neuromyopathy is a childhood-onset, slowly progressive neuromuscular disorder characterized by muscle weakness, distal limb deformities, and joint contractures. OMIM and MedGen summarize myofibrillar myopathy-7 as “an autosomal recessive muscle disorder characterized by early childhood onset of slowly progressive muscle weakness that primarily affects the lower limbs and is associated with joint contractures.”[7][20] Malacards echoes this description, highlighting lower limb–predominant weakness and mild muscle atrophy.[5] The myofibrillarmyopathy.org site notes that variants in KY cause “MFM7, characterized by pes cavus, muscular weakness and reduced reflexes” in the initial Arab-Israeli brothers and Turkish girl.[11]

Clinically, patients typically present between infancy and early childhood with delayed motor milestones, early fatigue, frequent falls, or difficulty walking, often accompanied by pes cavus or equinovarus deformities. In the Swedish index case, walking difficulties were noted from age 2, and by 7.5 years she had generalized muscle weakness with mild contractures in the shoulders, hips, and feet, and cavus feet.[15] In the Arab-Israeli siblings described by Straussberg et al., weakness started in early childhood with lower limb involvement, pes cavus, areflexia, and progressive walking difficulties, culminating in the description of a “novel congenital myopathy with core targetoid defects.”[2][7] The Iranian patient reported by Ebrahimzadeh-Vesal et al. had early-onset motor disorders and lower limb deformity, including equinovarus feet and mild scoliosis, consistent with the spectrum described in earlier patients.[13]

From a phenotypic ontological perspective, key HPO terms include muscle weakness, particularly **lower limb muscle weakness**, early-onset gait disturbance, **distal muscle atrophy**, and **reduced or absent deep tendon reflexes**. The weakness appears to be both distal and proximal, with some patients showing more pronounced distal involvement of the feet and ankles, while others have generalized limb-girdle weakness.[6][11][15] The progression is generally slow, with gradual worsening of weakness and contractures over years rather than rapid deterioration, consistent with HPO descriptors of “progressive muscular weakness.” Respiratory muscles and bulbar muscles are usually spared in early disease, although MedGen notes that in rare cases of myofibrillar myopathy more broadly, respiratory and cardiac muscles can be affected, leading to fatigue, dyspnea, and respiratory failure.[20]

Electrophysiologic studies in reported KY cases typically reveal a **myopathic pattern** on EMG with short-duration, low-amplitude motor unit potentials and early recruitment, without evidence of neuropathy.[2][15][19] For example, in the Arab-Israeli brothers, nerve conduction studies were normal and EMG findings were consistent with a myopathy, excluding distal hereditary motor neuropathy.[2][19] These findings support the classification of KY-related neuromyopathy as a primary muscle disease rather than a neuropathy. HPO terms such as “myopathic EMG pattern” and “normal nerve conduction studies” are therefore appropriate.

In terms of quality of life, the core neuromuscular phenotype impacts mobility, independence, and participation in daily activities. Children may require orthotics, physical therapy, and orthopedic interventions to maintain ambulation, and adults may experience limitations in walking, climbing stairs, and prolonged standing. The slow progression allows some adaptation, but the combination of weakness and contractures can significantly restrict activities of daily living, particularly in lower-resource settings with limited access to rehabilitation services. Formal quality-of-life assessments specific to KY-related neuromyopathy have not yet been reported, but generic instruments used in other myopathies would likely show impairments in mobility and pain domains.

### 3.2 Skeletal and orthopedic manifestations

Skeletal and orthopedic manifestations are prominent and often represent the most visible features of KY-related neuromyopathy. The myofibrillarmyopathy.org review emphasizes that MFM7 due to KY variants is characterized by **pes cavus**, muscular weakness, and reduced reflexes.[11] Many patients show foot deformities including pes cavus and equinovarus, with Achilles tendon contractures necessitating surgical intervention in some cases.[11][13][15][20] The Swedish index case had cavus feet and underwent Achilles tendon elongation surgery, reflecting significant contractures at an early age.[15] Ebrahimzadeh-Vesal et al. reported equinovarus deformity affecting both legs, with associated muscular weakness and mild scoliosis.[13]

MedGen lists **Achilles tendon contracture**, **lumbar hyperlordosis**, **multiple joint contractures**, **scoliosis**, and **thoracic kyphosis** among the clinical features associated with MFM7.[14][20] These descriptors align with patient reports of flexible or fixed contractures at multiple joints, particularly in the ankles, knees, hips, elbows, and spine. The presence of kyphoscoliosis or hyperlordosis reflects combined involvement of paraspinal musculature and connective tissues; however, not all patients develop spinal deformities. Hedberg-Oldfors et al. noted that their 7.5-year-old patient had lordosis but no scoliosis and that there was no major involvement of paraspinal muscles by that age, contrasting with the ky mouse model’s thoracolumbar kyphoscoliosis.[15][17]

The 2025 J Neuromuscular Diseases study described two families with early-onset myopathy, equinovarus deformity, lateral tongue atrophy, kyphoscoliosis, and contractures.[6] These findings highlight that spinal deformities and tongue involvement are part of the broader KY phenotype, though their frequency remains uncertain due to the small number of cases. The combination of pes cavus, equinovarus, and kyphoscoliosis resembles orthopedic patterns seen in hereditary spastic paraplegia and some congenital myopathies, contributing to diagnostic overlap and emphasizing the importance of genetic testing.

From an ontological standpoint, appropriate HPO terms include **pes cavus**, **equinovarus foot deformity**, **Achilles tendon contracture**, **multiple joint contractures**, **lumbar hyperlordosis**, **scoliosis**, and **thoracic kyphosis**. The frequency of these features appears high for foot deformities and ankle contractures, moderate for spinal curvature abnormalities, and variable for upper limb contractures. These skeletal manifestations substantially affect quality of life, often requiring orthopedic surgery, physical therapy, and assistive devices, and they can contribute to pain, fatigue, and reduced mobility.

### 3.3 Other system involvement: cranial, respiratory, cardiac, and central nervous system

Beyond skeletal muscle and the musculoskeletal system, KY-related neuromyopathy may involve other organ systems, although data are sparse. The 2025 J Neuromuscular Diseases study documented **lateral tongue atrophy** in patients with KY variants, indicating involvement of cranial muscles.[6] MedGen lists **tongue atrophy** as a clinical feature associated with MFM7.[20] These cranial manifestations may lead to difficulties with articulation or swallowing, though detailed assessments of bulbar function have not been systematically reported in KY-related cases.

Respiratory involvement is not well-characterized in KY-specific reports, but the broader myofibrillar myopathy literature notes that “in rare cases, the muscles used for speaking, swallowing, or breathing are affected,” and that when respiratory muscles are involved, patients may experience fatigue, breathing difficulties, and potentially respiratory failure.[20] Given that KY is expressed in skeletal muscle and moderate levels in cardiac and uterine muscles and brain, as shown by RNA panel analysis in the index case, it is plausible that respiratory muscles could be affected in severe or advanced KY-related neuromyopathy.[15] However, no KY-specific case to date has reported overt respiratory failure or the need for chronic ventilatory support.

Cardiac involvement also remains speculative. MedGen notes that some people with myofibrillar myopathy develop cardiomyopathy, sometimes as the first sign of disease.[20] Genes such as FLNC and LDB3, which are implicated in other myofibrillar myopathies, are known causes of cardiomyopathy, but KY has not yet been clearly linked to cardiomyopathy in humans.[4][20] The expression of KY in heart tissue and the presence of kyphoscoliosis and irregular breathing in ky mice may hint at subclinical cardiac or respiratory involvement, but dedicated cardiologic studies in KY patients have not been published.[15][17]

The central nervous system can be involved in KY-related hereditary spastic paraplegia, where upper motor neuron signs, spasticity, and gait disturbance co-occur with distal weakness and deformities.[11] The complex frameshift variant p.Val18TyrfsTer56 was reported in twelve Arab-Bedouin individuals with hereditary spastic paraplegia due to KY deficiency, expanding the phenotype beyond pure myopathy.[11] This suggests that KY has functional roles in corticospinal tracts or central motor pathways, at least in certain allelic contexts. HPO terms such as **spastic paraplegia**, **hyperreflexia**, and **pyramidal signs** would be appropriate for those individuals, although such features have not been reported in the classic MFM7 cases dominated by muscle pathology.[6][11]

Metabolic and laboratory abnormalities include modestly elevated serum creatine kinase levels in some patients, consistent with ongoing muscle fiber degeneration.[13][20] MedGen lists **elevated circulating creatine kinase activity** as a feature, indicating a laboratory phenotype that can support the diagnosis of myopathy.[20] Other laboratory parameters, such as liver enzymes, cardiac biomarkers, or inflammatory markers, have not been systematically described in KY-specific cohorts.

### 3.4 Histopathologic and imaging phenotypes

The histopathologic phenotype of KY-related neuromyopathy is distinctive and central to its classification as a myofibrillar myopathy. In the Swedish index case, muscle biopsy from the vastus lateralis showed variability in fiber size, internalized nuclei, and numerous very small fibers that expressed developmental myosin heavy chain isoforms.[15] Some small fibers exhibited abnormal sarcomeres with **thickened Z-discs** and small **nemaline rods**, linking KY deficiency to both Z-disc pathology and congenital myopathy–like features.[15] Immunohistochemistry revealed abnormal localization of Xin and filamin C, both Z-disc-associated proteins, resembling their altered distribution in ky/ky mouse muscle fibers.[15][17]

The Acta Neuropathologica report of the Arab-Israeli siblings described “core targetoid defects” in muscle fibers, including central areas devoid of oxidative enzyme activity resembling cores, surrounded by zones of preserved activity, alongside myofibrillar disorganization.[2][7] These core-targetoid lesions align with HPO terms such as “central core lesions” and “targetoid fibers” and position KY-related neuromyopathy at the interface of congenital myopathies with core phenomena and myofibrillar myopathies with protein aggregation.

The 2025 J Neuromuscular Diseases article provided perhaps the most detailed pathologic description of KY-deficient muscle to date.[6] They reported a “myopathic pattern in conjunction with fibers containing eosinophilic sarcoplasmic inclusions positive for kyphoscoliosis peptidase and filamin-C but not desmin, myofibrillar degeneration, and focal mitochondrial loss.”[6] These inclusions correspond to myofibrillar pathology in which structurally abnormal proteins aggregate within fibers, a hallmark of myofibrillar myopathies. The focal depletion of mitochondria indicates that mitochondrial distribution and integrity are secondarily disrupted, potentially contributing to weakness and fatigability. KY protein expression levels were markedly reduced in these muscles, and in silico analyses suggested impairment of KY’s catalytic triad by the missense and splice variants.[6]

Imaging phenotypes include selective muscle atrophy and fatty infiltration. Whole-body MRI in the Swedish index case showed atrophy and fatty infiltration in the calf muscles, particularly the gastrocnemius and soleus, consistent with clinically prominent distal weakness.[15] Similar patterns of preferential involvement of lower limb muscles have been reported in other congenital myopathies and myofibrillar myopathies, and MRI can help differentiate KY-related neuromyopathy from purely proximal limb-girdle dystrophies. In some patients, paraspinal muscles appear relatively preserved, explaining the absence of kyphoscoliosis despite generalized weakness, whereas in others, paraspinal involvement may contribute to kyphoscoliosis or hyperlordosis.[15][17]

The combination of histopathologic and imaging features supports the assignment of KY-related neuromyopathy to a specific subset of myofibrillar myopathies that also exhibit elements of congenital myopathy and core myopathy. HPO and pathology ontologies can capture these phenotypes using terms such as **myofibrillar disorganization**, **Z-disc streaming**, **protein aggregates in muscle fibers**, **nemaline bodies**, **core lesions**, and **mitochondrial depletion**, all of which contribute to a refined disease definition suitable for computational disease knowledge bases.

## 4. Genetic and molecular information

### 4.1 KY gene structure, expression, and protein features

KY (kyphoscoliosis peptidase) is a protein-coding gene located on chromosome 3q22.2 with 11 exons and transcriptional evidence of multiple isoforms.[1][13] NCBI Gene lists the gene type as protein-coding and notes that KY belongs to the **transglutaminase-like superfamily**.[1] OMIM’s gene entry describes the identification of the mouse **ky** gene by Blanco et al., who showed that the transcript encodes a novel muscle-specific protein with a domain homologous to human transglutaminase.[17] This transglutaminase-like domain contains a predicted catalytic triad that would typically mediate crosslinking of proteins via isopeptide bonds, but recent human and mouse data suggest that KY’s critical muscle function may be more structural than enzymatic.[3][6][17]

Expression studies indicate that KY is predominantly expressed in skeletal muscle, with moderate expression in heart and uterine muscles and brain.[15][17] Hedberg-Oldfors et al. analyzed an RNA panel and found that KY is “most highly expressed in skeletal muscle and to a moderate level in cardiac and uterine muscles and brain.”[15] NCBI’s expression data show biased expression in skin and prostate in some datasets, but this likely reflects tissue sampling and platform differences; the consensus from functional studies is that KY is a **muscle-enriched protein**.[1][9][15][17] In mice, the ky transcript is detectable only in skeletal muscle and heart, reinforcing its muscle-specific role.[17]

The Alliance of Genome Resources notes that KY is “predicted to be involved in muscle organ development and neuromuscular junction development” and “predicted to be located in the Z disc” and “active in the cytoplasm.”[9] This aligns with immunolocalization data showing KY at or near the sarcomeric Z-disc and within the cytoplasm of muscle fibers, where it may interact with the actin cytoskeleton and Z-disc proteins such as filamin C.[1][9][15] Gene Ontology terms relevant to KY include “muscle organ development,” “neuromuscular junction development,” “Z disc,” and “cytoplasm,” capturing its role in structural organization and NMJ maturation.

At the protein level, UniProt Q8NBH2 describes kyphoscoliosis peptidase as a single-pass cytosolic protein with predicted transglutaminase-like catalytic residues, although its precise enzymatic activity remains unconfirmed.[8] The 2026 Human Molecular Genetics study titled “Myofibrillar myopathy-associated KY protein promotes muscle fibre size rescue independent of its predicted catalytic triad” provides strong evidence that the canonical catalytic triad is not essential for KY’s role in muscle fiber size maintenance.[3] This suggests that KY’s critical function in humans may involve scaffolding interactions with other Z-disc and cytoskeletal proteins rather than transglutaminase catalytic activity, a conclusion supported by the presence of disease-causing missense variants that likely disrupt protein folding or binding rather than classical enzymatic sites.[3][6][16]

### 4.2 Pathogenic variant spectrum and classification

The known pathogenic variant spectrum of KY includes multiple types:

Nonsense variants that create premature stop codons, such as p.Tyr135Ter (Y135X) and p.Arg139Ter, leading to truncated proteins and likely **loss of function**.[7][11][13] Frameshift variants such as p.Thr358Leufs*3 and p.Val18TyrfsTer56, which alter the reading frame and introduce premature termination, producing nonfunctional or unstable proteins.[11][12][15] Splice-site variants such as c.710+1G>A, predicted to disrupt normal RNA splicing and resulting in exon skipping, intron retention, or activation of cryptic splice sites, thereby impairing protein production.[6] Missense variants such as p.Cys243Arg, which substitute one amino acid for another at a conserved position, potentially disrupting protein folding, stability, or interactions with binding partners.[6][16]

ClinVar documents several KY variants interpreted as pathogenic or likely pathogenic for MFM7, including the c.1071del frameshift variant.[12] The c.1071delG variant was shown to be present at the RNA level in patient skeletal muscle, indicating that nonsense-mediated decay is incomplete and that a truncated, nonfunctional protein is likely produced.[12][15] The c.405C>A (p.Tyr135Ter) and c.415C>T (p.Arg139Ter) nonsense variants truncate the protein early in its sequence, eliminating most of the transglutaminase-like domain and any C-terminal binding regions, making a **loss-of-function** mechanism highly plausible.[7][11][13]

The 2022 spectrum paper and the 2025 J Neuromuscular Diseases study highlight that missense and splice-site variants can also cause MFM7.[6][16] The p.Cys243Arg missense variant substitutes a conserved cysteine within or near the transglutaminase-like domain, and in silico analysis suggested that it impairs the catalytic triad or structural integrity of the protein, while experimental data showed markedly reduced KY protein expression.[6] The splice-site variant c.710+1G>A likely results in aberrant splicing and truncated or misfolded protein, supported by reduced protein levels on immunoblot.[6] These variants are classified as pathogenic based on segregation in consanguineous families, absence in population databases, predicted protein impact, and correlation with a consistent clinical phenotype.

In terms of ACMG/AMP classification, most reported KY variants meet multiple criteria for pathogenicity: PVS1 (null variant in a gene where loss-of-function is a known mechanism of disease), PM2 (absent from controls), PP1 (co-segregation with disease in multiple affected family members), and PP4 (patient’s phenotype or family history highly specific for a disease with a single genetic etiology).[12][13][15][16] Missense variants such as p.Cys243Arg additionally meet PM1 (located in a mutational hot spot or critical functional domain), PP3 (multiple lines of computational evidence support a deleterious effect), and PS3 (supporting functional studies), elevating them to pathogenic status.[6][16]

### 4.3 Functional consequences: loss of function and structural disruption

All reported KY variants associated with neuromyopathy are consistent with a **loss-of-function** mechanism, either by truncating the protein or impairing its expression, stability, or function. Hedberg-Oldfors et al. argued that the c.1071delG variant causes disease by introducing a premature stop codon that truncates the protein, and RNA analysis confirmed the presence of the mutant transcript, implying that a truncated nonfunctional protein is produced.[15][12] Ebrahimzadeh-Vesal et al. similarly concluded that their c.415C>T (p.Arg139Ter) variant likely results in loss of function, given its early truncation and absence from population databases.[13]

The 2025 J Neuromuscular Diseases study provided direct evidence of reduced KY protein expression in patients with p.Cys243Arg and c.710+1G>A variants.[6] KY protein levels were markedly reduced on immunoblot, and immunohistochemistry showed that remaining KY localized to eosinophilic sarcoplasmic inclusions alongside filamin C, suggesting misfolding and aggregation of mutant protein or compensatory retention of residual protein at sites of myofibrillar damage.[6] In silico analysis predicted impairment of the catalytic triad by these variants, but the key pathogenic consequence appears to be overall deficiency of functional KY rather than a specific catalytic defect.[6]

The 2026 Human Molecular Genetics study took this further by demonstrating that a KY protein variant associated with MFM7 can promote muscle fiber size rescue independent of its predicted catalytic triad.[3] This indicates that KY’s primary functional role in muscle may be as a structural scaffold at the Z-disc and neuromuscular junction, coordinating interactions with other proteins such as filamin C, Xin, and potentially transmembrane components of the NMJ.[1][3][15][17] The loss of this scaffolding function leads to impaired maturation and stabilization of the neuromuscular junction, defective muscle growth and hypertrophy, and susceptibility to myofibrillar disorganization under mechanical stress.[1][3][17]

Thus, the pathogenic variants in KY can be conceptualized as causing a **structural loss of function**: the absence or severe reduction of KY disrupts the integrity of sarcomeric Z-discs and the NMJ, leading to mislocalization of Z-disc proteins, accumulation of damaged myofibrillar components, and defective mechanotransduction. This aligns with the broader pathogenesis of myofibrillar myopathies, where mutations in Z-disc proteins such as FLNC, LDB3, and DES lead to similar patterns of myofibrillar disintegration and protein aggregation.[4][20]

### 4.4 Modifier genes, epigenetics, and chromosomal abnormalities

No specific modifier genes have been definitively associated with KY-related neuromyopathy. Given the small number of known families, genome-wide association or modifier gene studies have not been feasible. However, the interaction between KY and filamin C, demonstrated in mouse models and inferred in human disease, suggests that variation in FLNC or other Z-disc proteins could modulate disease severity.[1][15][17] NCBI Gene lists a GeneRIF indicating that “Filamin C interacts with the muscular dystrophy KY protein and is abnormally distributed in mouse KY deficient muscle fibres,” pointing to a direct molecular connection.[1] In KY-deficient human muscle, filamin C accumulates in sarcoplasmic inclusions, reinforcing the notion that KY and filamin C operate in a shared pathway.[6][15]

Epigenetic mechanisms such as DNA methylation, histone modifications, or chromatin changes have not been specifically implicated in KY-related neuromyopathy. The disease is clearly Mendelian, and there is no evidence of imprinting, allele-specific expression, or epigenetic silencing of KY beyond the consequences of structural variants. Expression analyses in the Swedish index case showed that the mutant KY transcript with the c.1071delG variant is expressed in skeletal muscle, indicating that no alternative splicing or nonsense-mediated decay had occurred.[15][12] This suggests that transcriptional regulation of KY is largely preserved even in the presence of truncating variants, and pathogenicity arises from the properties of the translated protein rather than epigenetic modulation.

Chromosomal abnormalities such as large deletions, duplications, translocations, or aneuploidies have not been reported as primary causes of KY-related neuromyopathy. All known cases are due to point mutations or small insertions/deletions at the sequence level.[7][11][12][13][15][16] Whole-exome sequencing has been sufficient to detect these variants in most families, and chromosomal microarray or karyotyping has not revealed larger structural variants involving the KY locus. This supports an etiology grounded in single-gene point mutations rather than chromosomal rearrangements.

## 5. Environmental information

### 5.1 Environmental and occupational exposures

There is no evidence that environmental exposures such as toxins, heavy metals, pesticides, radiation, or occupational hazards contribute to the initiation of KY-related neuromyopathy in the absence of KY mutations. None of the reported patients have shared a common environmental exposure, and their geographic and cultural backgrounds are diverse, spanning Arab-Israeli, Kurdish, Swedish, Iranian, and Arab-Bedouin families.[7][11][13][15] The common thread is consanguinity and homozygous KY variants rather than environmental factors.

Comparative toxicogenomics databases and environmental health literature do not list KY-related neuromyopathy as an environmentally induced or modulated condition, and KY itself is not a known target of toxicants. While environmental factors can influence general muscle health, inflammation, and oxidative stress, their role in KY-related neuromyopathy appears to be secondary and nonspecific. Therefore, in the current state of knowledge, environmental exposures are not considered causative or major risk determinants for this disease.

### 5.2 Lifestyle and behavioral factors

Lifestyle and behavioral factors such as physical activity, diet, smoking, and alcohol consumption have not been systematically studied in KY-related neuromyopathy. Patients described in the literature are mostly children or young adults at the time of presentation, limiting the relevance of long-term lifestyle exposures. The main lifestyle-related interventions discussed in case reports involve physical therapy, orthopedic management, and attempts to maintain mobility and flexibility, rather than lifestyle factors as etiologic agents.[11][15]

From a theoretical standpoint, excessive mechanical stress on weakened muscles could exacerbate microtrauma and myofibrillar damage, while moderate, controlled exercise might support muscle function and delay contractures. The ky mouse model, which is “deficient in hypertrophic responses” to increased demand, suggests that mechanical loading is processed differently in the absence of KY, potentially rendering muscles more vulnerable to damage under high load.[17] However, human data linking specific exercise patterns to disease trajectory in KY-related neuromyopathy are lacking.

Nutritional status may influence disease severity by modulating muscle mass and metabolic resilience. Malnutrition could exacerbate weakness and delay recovery from muscle damage, while adequate protein intake and caloric balance might support muscle maintenance. Yet these are general principles for neuromuscular disease care and not KY-specific findings. There is no evidence that particular diets, supplements, or nutraceuticals have targeted efficacy in KY-related neuromyopathy.

### 5.3 Infectious agents and immune factors

No infectious agents have been implicated in the etiology or exacerbation of KY-related neuromyopathy. Unlike post-infectious myositis or autoimmune neuromuscular disorders, KY-related neuromyopathy presents as a chronic, non-inflammatory disease with structural muscle pathology and no evidence of immune-mediated damage.[6][15] Muscle biopsies described in KY-deficient patients do not show significant inflammatory infiltrates, and laboratory markers of inflammation are not emphasized in case reports.[6][15]

Similarly, the immune system does not appear to play a primary pathogenic role. There is no evidence of autoantibodies, complement activation, or T-cell–mediated muscle damage specific to KY-related neuromyopathy. While secondary inflammation could occur in response to chronic muscle fiber degeneration, this has not been a focus of available reports. Therefore, infectious and immune factors are not currently considered relevant etiologic contributors.

In summary, environmental, lifestyle, and infectious factors have not been shown to cause or significantly modify KY-related neuromyopathy, which remains a paradigmatic gene-driven neuromuscular disorder. Future epidemiologic or mechanistic studies may uncover subtle gene–environment interactions, but such relationships are currently speculative and unproven.

## 6. Mechanism and pathophysiology

### 6.1 Causal chain from mutation to clinical phenotype

A mechanistic description of KY-related neuromyopathy can be organized as a causal chain from the initiating genetic lesion to the clinical manifestations, noting where steps are inferred rather than directly demonstrated:

Step 1: Biallelic germline pathogenic variants in KY (nonsense, frameshift, missense, or splice-site) arise in the germline and are present in all skeletal muscle fibers, leading to reduced or absent functional KY protein.[6][7][12][13][15]  

Step 2: Loss of functional KY results in impaired assembly or stability of KY-containing complexes at the sarcomeric Z-disc and neuromuscular junction, disrupting interactions with partners such as filamin C and Xin; this step is supported by mouse and human data but some details are inferred.[1][6][15][17]  

Step 3: Disruption of KY-dependent scaffolding and signaling leads to defective neuromuscular junction maturation and stabilization, and to compromised structural integrity of Z-discs and myofibrils under mechanical load, resulting in myofibrillar disorganization and abnormal sarcomeric structures; this is supported by histopathology and animal models.[6][15][17]  

Step 4: Myofibrillar disorganization and structural instability lead to accumulation of misfolded or damaged proteins in sarcoplasmic inclusions, particularly involving KY and filamin C, and to focal depletion or mislocalization of mitochondria, impairing muscle fiber contractile function and energy metabolism.[6]  

Step 5: At the tissue level, repeated cycles of myofibrillar damage, impaired repair, and deficient hypertrophic responses result in progressive muscle fiber atrophy, replacement by fat and connective tissue, and failure of growth and adaptation, especially in distal lower limb muscles and postural muscles.[15][17]  

Step 6: Clinically, these structural and metabolic defects manifest as early-onset muscle weakness, foot deformities (pes cavus, equinovarus), reduced reflexes, and joint contractures, with potential development of kyphoscoliosis, hyperlordosis, tongue atrophy, and in some allelic contexts, spastic paraplegia due to involvement of central motor pathways; this step is well documented clinically.[6][7][11][13][15][20]  

Step 7: Over time, secondary complications such as orthopedic deformities, functional limitations, and potential respiratory or cardiac involvement (by analogy with other myofibrillar myopathies) may arise, impacting quality of life and long-term prognosis; this step is partly inferred from broader myofibrillar myopathy data.[20]

This chain integrates molecular, cellular, tissue, and clinical levels, providing a coherent pathophysiologic model for KY-related neuromyopathy.

### 6.2 Molecular pathways and KY’s role in muscle and neuromuscular junctions

At the molecular level, KY appears to participate in pathways governing **muscle organ development** and **neuromuscular junction development**, as predicted by the Alliance of Genome Resources and supported by mouse and human studies.[9][17] Gene Ontology terms such as “muscle organ development” and “neuromuscular junction development” capture KY’s involvement in processes that ensure proper formation and maintenance of muscle fibers and synaptic connections between motor neurons and muscle.[9][17] Although detailed biochemical pathways have not been fully delineated, KY’s transglutaminase-like domain suggests potential roles in post-translational modification or crosslinking of structural proteins, while recent functional data highlight a more structural scaffolding role.[3][17]

The ky mouse model provides critical insight. Blanco et al. identified a dinucleotide deletion in the mouse ky gene that leads to a premature stop codon, resulting in a truncated protein and loss of function.[17] Homozygous ky mutant mice exhibit a primary degenerative myopathy with thoracolumbar kyphoscoliosis and irregular breathing, and the histopathology suggests that “ky protein activity is crucial for normal muscle growth and function as well as the maturation and stabilization of the neuromuscular junction.”[17] Notably, ky mice are “deficient in hypertrophic responses” to increased muscle demand, though adaptive fiber type shifts still occur, indicating a specific role in hypertrophy rather than fiber-type determination.[17]

In humans, Hedberg-Oldfors et al. showed that KY is highly expressed in skeletal muscle and that the c.1071delG variant leads to truncated KY protein, resulting in abnormal distribution of Xin and filamin C similar to that observed in ky mice.[15] This suggests that KY participates in a protein complex involving Xin and filamin C at the Z-disc, linking sarcomeric structure to signaling pathways that regulate muscle growth and NMJ stability.[15][17] NCBI Gene references a study showing that filamin C interacts with KY and is abnormally distributed in ky-deficient mouse muscle fibers, reinforcing this connection.[1]

The 2026 Human Molecular Genetics study adds that a KY protein associated with MFM7 can rescue muscle fiber size independent of its predicted catalytic triad.[3] This finding implies that KY’s critical function may be to provide a structural scaffold that organizes or stabilizes protein complexes at the Z-disc and NMJ, rather than to catalyze transglutaminase reactions. If so, KY’s role would align with other Z-disc proteins such as FLNC and LDB3, which link actin filaments, integrins, and signaling molecules to transduce mechanical forces and regulate hypertrophic responses.[4][17] Loss of KY would then dysregulate these pathways, leading to impaired mechanotransduction and growth.

Although specific signaling cascades such as Wnt, MAPK, or PI3K-AKT have not been directly implicated in KY-related neuromyopathy, it is plausible that KY influences these pathways indirectly through its effects on Z-disc organization and NMJ signaling. The failure of hypertrophic responses in ky mice suggests that anabolic signaling pathways downstream of mechanical load and NMJ activity are disrupted.[17] Future transcriptomic or phosphoproteomic studies could clarify which molecular pathways are altered in KY-deficient muscle, potentially revealing therapeutic targets such as mTOR or IGF-1 signaling.

### 6.3 Cellular processes and protein dysfunction

At the cellular level, KY deficiency affects multiple processes, including **sarcomere assembly**, **Z-disc maintenance**, **protein quality control**, and **mitochondrial distribution**. Muscle biopsies from KY-deficient patients show myofibrillar degeneration, abnormal sarcomeres with thickened Z-discs, and nemaline rods, indicating that sarcomere assembly and maintenance are perturbed.[6][15] The presence of thickened Z-discs suggests that Z-disc components accumulate abnormally, while nemaline rods reflect actin-associated protein aggregation, both hallmarks of myofibrillar myopathies and congenital myopathies with structural defects.[15]

The 2025 J Neuromuscular Diseases study observed eosinophilic sarcoplasmic inclusions that were positive for KY and filamin C but negative for desmin, indicating selective accumulation of KY and filamin C within aggregates.[6] This pattern suggests that KY-deficient muscle experiences **protein misfolding and aggregation**, particularly of Z-disc components, and that protein quality control mechanisms such as the ubiquitin–proteasome system and autophagy may be overwhelmed or misdirected. The absence of desmin in inclusions distinguishes KY-related inclusions from those in desminopathies, where desmin aggregates prominently.[4][6]

Mitochondrial involvement is evidenced by **focal depletion of mitochondria** in KY-deficient muscle fibers, as reported in the 2025 study.[6] Loss or mislocalization of mitochondria could impair local ATP production, calcium buffering, and reactive oxygen species handling, contributing to muscle fatigue and fiber degeneration. While mitochondrial DNA mutations have not been implicated, the secondary mitochondrial changes highlight that KY-related neuromyopathy impacts not only structural but also metabolic aspects of muscle function.[6]

At the level of protein dysfunction, KY mutations lead to either absence of the protein (due to truncation or nonsense-mediated decay) or production of unstable or misfolded protein that aggregates or is degraded.[6][12][13][15] The p.Cys243Arg missense variant likely disrupts the structural integrity of the transglutaminase-like domain or a critical binding interface, leading to misfolding and degradation.[6][16] Splice-site variants such as c.710+1G>A could produce mis-spliced transcripts that encode aberrant proteins, also contributing to misfolding and aggregation.[6] The accumulation of KY and filamin C in inclusions suggests that mutant KY may still bind filamin C but fail to integrate properly into functional complexes, trapping both proteins in non-functional aggregates.

Relevant Gene Ontology biological processes for these cellular mechanisms include “sarcomere organization,” “Z disc assembly,” “protein aggregation,” “protein quality control,” and “mitochondrial organization.” The primary affected cell type is the **skeletal muscle fiber**, particularly the multinucleated myofiber (Cell Ontology term corresponding to skeletal muscle cell), which depends on finely tuned sarcomeric and mitochondrial organization for function. Defects in these processes underlie the clinical phenotype of weakness and myopathy.

### 6.4 Metabolic changes and tissue damage mechanisms

Metabolic changes in KY-related neuromyopathy are less well characterized than structural changes, but available data suggest alterations in energy metabolism and oxidative capacity, secondary to structural damage and mitochondrial depletion. The presence of focal mitochondrial loss, as noted in the 2025 J Neuromuscular Diseases study, implies that certain regions of muscle fibers may be deprived of adequate ATP supply, particularly under high energy demand.[6] Combined with myofibrillar disorganization and Z-disc instability, this could exacerbate muscle fatigue and predispose fibers to degeneration under mechanical stress.

Serum creatine kinase elevation in some patients indicates ongoing muscle fiber breakdown and leakage of intracellular enzymes into the circulation.[13][20] This reflects **tissue damage mechanisms** such as microtears in sarcolemma, necrosis of fibers, and inadequate repair. However, KY-related neuromyopathy does not appear to be characterized by massive necrosis or chronic inflammation; rather, it shows a more insidious pattern of fiber atrophy, structural remodeling, and accumulation of protein aggregates.[6][15]

Oxidative stress may contribute to pathogenesis, as in other myofibrillar myopathies, but specific measurements of reactive oxygen species, antioxidant defenses, or lipid peroxidation have not been reported in KY patients. Similarly, no metabolomics studies have profiled metabolite changes in KY-deficient muscle or serum. The metabolic phenotype remains an area for future research, particularly given the potential involvement of mitochondria.

Tissue damage mechanisms can thus be summarized as follow: structural instability of Z-discs and myofibrils leads to localized mechanical failure under contraction, causing microdamage and disassembly of sarcomeres; protein aggregates form as misfolded components accumulate; mitochondria are lost or mislocalized in affected regions; and over time, muscle fibers become atrophic and are replaced by fat and connective tissue. These processes correspond to Gene Ontology terms such as “muscle fiber atrophy,” “muscle tissue remodeling,” and “fibrosis,” and they underlie the clinical manifestations of weakness and contractures.

### 6.5 Neuromuscular junction and central nervous system involvement

KY’s role in **neuromuscular junction development** is highlighted in both mouse and human studies. The ky mouse mutant exhibits abnormal NMJ maturation and stabilization, contributing to kyphoscoliosis and degenerative myopathy.[17] NCBI Gene’s summary notes that KY “is involved in the function, maturation and stabilization of the neuromuscular junction,” and that mutations impair normal muscle growth.[1] Although human NMJs have not been extensively studied in KY-deficient patients, the early-onset weakness and failure of hypertrophic responses likely reflect compromised NMJ function as well as sarcomeric defects.

The functional consequences of NMJ impairment may include reduced synaptic efficacy, altered endplate potentials, and susceptibility to denervation or partial denervation under stress. However, electrophysiologic studies in KY patients have not shown overt neuromuscular transmission defects such as decrement on repetitive nerve stimulation, distinguishing KY-related neuromyopathy from primary congenital myasthenic syndromes.[2][15] It is possible that NMJ defects are more structural and developmental than functional at baseline, leading to a reduced safety margin that manifests primarily as impaired muscle growth rather than fluctuating weakness.

Central nervous system involvement is most evident in KY-related hereditary spastic paraplegia, where a frameshift KY variant leads to upper motor neuron signs and corticospinal tract dysfunction.[11] This suggests that KY is also expressed or required in specific central nervous system cell types, possibly corticospinal neurons or spinal interneurons. The mechanistic link between KY deficiency and spastic paraplegia is not fully known, but could involve disrupted cytoskeletal dynamics or synaptic stabilization in central pathways analogous to those in NMJs. HPO terms such as “spastic paraplegia,” “hyperreflexia,” and “corticospinal tract degeneration” would capture this component of the spectrum.

From a cell ontology perspective, the primary cell type involved in the classic myopathy phenotype is the **skeletal muscle fiber**, while in the spastic paraplegia phenotype, central neurons such as upper motor neurons and spinal motor circuits are implicated. Understanding KY’s role in these diverse cell types will require single-cell and spatial transcriptomics, which have not yet been applied to KY-related neuromyopathy.

### 6.6 Molecular profiling and advanced technologies

To date, there are no published large-scale transcriptomic, proteomic, or metabolomic studies specifically focused on KY-related neuromyopathy. However, individual studies provide insights into KY expression patterns, protein–protein interactions, and functional consequences of mutations. Hedberg-Oldfors et al. used an RNA panel to demonstrate high KY expression in skeletal muscle and moderate expression in heart, uterus, and brain.[15] The 2025 J Neuromuscular Diseases study performed immunoblotting and immunohistochemistry to quantify KY and filamin C levels and localization, showing reduced KY protein and its accumulation in inclusions with filamin C.[6]

Proteomic databases such as iPTMnet list KY as a human kyphoscoliosis peptidase but do not yet provide detailed post-translational modification profiles or interaction networks beyond the known filamin C interaction.[8][1] Multi-omics integration has not yet been applied to KY, but future studies combining RNA-seq, proteomics, and phosphoproteomics could elucidate downstream pathways affected by KY deficiency, including changes in Z-disc protein composition, signaling pathways, and metabolic enzymes.

Advanced functional genomics approaches such as CRISPR screens have not been reported for KY, and there are no large-scale functional genomics datasets targeting KY in human cells. However, the ky mouse model and transgenic rescue experiments described in the 2026 Human Molecular Genetics paper effectively function as targeted genetic models, demonstrating that KY variants can be manipulated to study their effects on muscle fiber size and function.[3][17] These models provide a foundation for future CRISPR-based approaches to dissect KY’s functions and identify pathways that can be targeted therapeutically.

Overall, the pathophysiology of KY-related neuromyopathy is increasingly well understood at the structural and cellular levels, but systems-level molecular profiling and advanced omics approaches remain underdeveloped. As such techniques are applied, they are likely to refine the causal chain and highlight specific pathways that could be modulated to ameliorate the disease.

## 7. Anatomical structures affected

### 7.1 Organ-level involvement

The primary organ system affected in KY-related neuromyopathy is the **skeletal musculature**, particularly the muscles of the lower limbs, feet, and postural trunk.[7][15][20] UBERON terms corresponding to these structures include the lower limb musculature, foot muscles, and paraspinal muscles. Clinically, the calf muscles (gastrocnemius and soleus) are among the most prominently affected, as evidenced by MRI showing atrophy and fatty infiltration.[15] The quadriceps, hip flexors, and other limb-girdle muscles can also be involved, contributing to generalized weakness.

Secondary organ involvement may include the **spine**, where kyphoscoliosis or hyperlordosis develop due to combined muscle weakness and connective tissue changes.[11][14][20] The spine is structurally deformed in some patients, and the thoracolumbar region is particularly affected, mirroring the kyphoscoliosis seen in ky mice.[17] The tongue, part of the oropharyngeal musculature, can also exhibit atrophy, reflecting involvement of cranial muscles.[6][20]

Although not definitively documented in KY-specific patients, heart and respiratory muscles are organs of potential concern given KY expression in heart and the tendency for myofibrillar myopathies to affect cardiomyocytes.[15][20] MedGen notes that myofibrillar myopathy in general can involve cardiomyopathy and respiratory muscle weakness, and KY’s expression in heart suggests that subtle cardiac involvement could occur.[15][20] However, no overt cardiomyopathy has been reported in KY-related cases to date.

### 7.2 Tissue and cell-level involvement

At the tissue level, KY-related neuromyopathy primarily affects **skeletal muscle tissue**, a type of striated muscle characterized by multinucleated fibers and organized sarcomeres. The main tissue pathology is in muscle fibers, where structural and metabolic changes occur, including myofibrillar degeneration, Z-disc abnormalities, and fiber atrophy.[6][15] Connective tissue surrounding muscle fibers, including the endomysium and perimysium, may become fibrotic as muscle is replaced by collagen and fat, particularly in advanced disease.[15][17]

The key cell type is the **skeletal muscle fiber** (myofiber), a multinucleated cell that forms the contractile units of muscle. Cell Ontology terms such as skeletal muscle cell or myofiber capture this. KY is expressed within these fibers, particularly at the sarcomeric Z-disc, where it associates with cytoskeletal and signaling proteins.[9][15][17] Satellite cells (muscle stem cells) may also be affected indirectly, as impaired hypertrophic responses in ky mice suggest that muscle growth and regeneration are compromised.[17] However, direct studies of satellite cell function in KY deficiency have not been reported.

In the hereditary spastic paraplegia phenotype, central nervous system cell types such as **upper motor neurons** and associated glial cells are involved. The corticospinal tract degenerates or fails to develop correctly, leading to spasticity and paraplegia.[11] While the exact cellular expression pattern of KY in the CNS is not fully known, its moderate expression in brain suggests roles in neuronal or glial cells that could be investigated using cell-type–specific transcriptomics.[15]

### 7.3 Subcellular localization and compartments

Subcellularly, KY localizes primarily to the **sarcomeric Z-disc** and the cytoplasm.[9][15][17] Gene Ontology cellular component terms such as “Z disc” and “cytoplasm” capture this localization. The Z-disc serves as a structural anchor for actin filaments and a hub for mechanotransduction and signaling, linking sarcomeres to the sarcolemma and extracellular matrix. KY’s presence at the Z-disc places it in a critical position to influence sarcomeric stability, force transmission, and signaling pathways that regulate muscle growth and NMJ development.[9][15][17]

Within the cytoplasm, KY may interact with other cytoskeletal proteins and chaperones, contributing to protein quality control and structural organization. The presence of KY in sarcoplasmic inclusions in KY-deficient muscle suggests that mutant or residual KY accumulates in aggregated protein complexes, potentially along with filamin C.[6] These inclusions highlight the disruption of normal subcellular compartmentalization and protein trafficking.

Mitochondria are another subcellular compartment indirectly affected, as focal mitochondrial depletion is observed in KY-deficient muscle.[6] While KY does not localize to mitochondria, its role in Z-disc stability and cytoskeletal integrity likely influences mitochondrial positioning and anchoring, which are essential for efficient energy delivery to contractile apparatus. The loss or mislocalization of mitochondria underscores the interconnectedness of structural and metabolic compartments in muscle fibers.

### 7.4 Spatial distribution and lateralization

The anatomical distribution of KY-related neuromyopathy is primarily **bilateral** and symmetric, affecting both lower limbs and, when present, both sides of the spine and upper limbs.[7][11][13][15] However, within this bilateral pattern, some asymmetry may occur in contractures or deformities, especially if orthopedic interventions or differential loading alter progression. For example, equinovarus deformity may be more pronounced on one side initially, though ultimately both feet tend to be affected.[6][11][13]

Spatially, lower limb muscles are more severely affected than upper limb muscles, with calf muscles often showing the greatest atrophy and fatty infiltration.[15] Distal muscles of the feet and ankles are particularly involved, consistent with pes cavus and equinovarus deformities.[11][13][20] In some patients, proximal muscles such as the quadriceps and hip flexors are also affected, leading to a limb-girdle pattern of weakness.[15] The pattern can thus be described as distal-predominant or generalized limb involvement, with emphasis on lower extremities.

Within the CNS, in KY-related hereditary spastic paraplegia, the corticospinal tracts are affected bilaterally, leading to symmetric spasticity and weakness.[11] There is no evidence of lateralized lesions or focal brain pathology; rather, the pattern reflects diffuse or tract-specific involvement consistent with systemic KY deficiency.

## 8. Temporal development

### 8.1 Age of onset and onset pattern

KY-related neuromyopathy typically presents in **early childhood**, with onset ranging from infancy to early school age.[7][11][13][15] OMIM and MedGen describe MFM7 as having “early childhood onset,” and the initial cases support this.[7][20] The Swedish index case had walking difficulties from age 2 and was diagnosed at 7.5 years.[15] The Arab-Israeli brothers and Turkish girl described by Straussberg et al. and Hedberg-Oldfors et al. also had early-onset symptoms, including delayed walking and early weakness.[2][11][15] The Iranian patient reported by Ebrahimzadeh-Vesal et al. presented in childhood with lower limb deformity and motor disorders, though the exact age was not specified.[13]

The general onset pattern is **chronic and insidious** rather than acute. Children may initially appear normal but develop delayed gross motor milestones, frequent falls, or gait abnormalities over months to years, prompting evaluation. There are no reports of acute or subacute onset with abrupt deterioration; instead, symptoms develop gradually as muscles fail to grow and adapt normally, and structural defects accumulate. This pattern is consistent with congenital or early-onset developmental myopathies rather than acquired inflammatory myopathies.

In the hereditary spastic paraplegia phenotype, onset also appears in childhood or adolescence, with progressive gait disturbance and spastic

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 5 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.

3 of 5 terms resolved to a current term; the rest could not be looked up either way.