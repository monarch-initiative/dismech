---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-31T15:43:55.888878'
end_time: '2026-08-31T15:48:21.640924'
duration_seconds: 265.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: TMEM199-CDG
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 17
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 17
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0012159
    reported_labels:
    - Abnormal transferrin glycosylation
    ontology_label: Internal carotid artery dissection
  - term_id: HP:0003119
    reported_labels:
    - Elevated serum cholesterol
    ontology_label: Abnormal circulating lipid concentration
  - term_id: GO:0030148
    reported_labels:
    - regulation of organelle pH
    ontology_label: sphingolipid biosynthetic process
  - term_id: CL:0002078
    reported_labels:
    - hepatic stellate cell
    ontology_label: meso-epithelial cell
  labels_variant: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TMEM199-CDG
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TMEM199-CDG** covering all of the
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

# TMEM199-CDG (Congenital Disorder of Glycosylation Type IIp): Clinical, Genetic, and Mechanistic Characterization

TMEM199-CDG, also known as congenital disorder of glycosylation type IIp (CDG2P), is an ultra-rare autosomal recessive metabolic liver disease caused by biallelic pathogenic variants in the TMEM199 gene, a mammalian orthologue of the yeast vacuolar ATPase assembly factor Vma12p.[2][4][6][10] The disorder is characterized by chronically elevated serum aminotransferases and alkaline phosphatase, hepatic steatosis with mild fibrosis, hypercholesterolemia, and a distinctive combined defect of N- and O-glycosylation suggestive of a Golgi homeostasis disturbance.[1][2][3][6][13][16] Clinically, TMEM199-CDG is remarkable among Golgi-related CDGs for its largely non-encephalopathic presentation with liver-predominant involvement and a non-progressive or very slowly progressive hepatic course in most reported patients, in contrast to many other CDGs that feature severe multisystem and neurodevelopmental manifestations.[3][6][8][16] Mechanistically, TMEM199 functions as a V-ATPase assembly factor localized mainly to the endoplasmic reticulum (ER), and its deficiency disrupts endosomal, lysosomal, and Golgi acidification, leading to defective glycosylation, impaired lipophagy, hepatic steatosis, and altered lipid handling.[10][13] To date, fewer than ten affected individuals have been described worldwide, with a notable clustering of the recurrent c.92G>C (p.Arg31Pro) missense variant in southern Mediterranean populations and a growing recognition of TMEM199-CDG as an important diagnostic consideration in patients with unexplained chronic liver enzyme elevations, low ceruloplasmin, and type II transferrin isoelectric focusing patterns mimicking Wilson disease.[3][6][7][11][16]  

## 1. Disease Information

### 1.1 Overview and Clinical Definition

TMEM199-CDG is classified within the broader group of congenital disorders of glycosylation (CDGs), which encompass genetically and clinically heterogeneous monogenic conditions marked by impaired biosynthesis, processing, or trafficking of glycoconjugates, including glycoproteins and glycolipids.[7][13] Within this group, TMEM199-CDG is a subtype of type II CDGs, characterized by defects in the processing and maturation of glycan chains rather than their initial assembly, and specifically associated with a Golgi homeostasis disturbance affecting both N- and O-linked glycosylation.[2][3][6][13] Orphanet describes TMEM199-CDG as a rare congenital glycosylation anomaly characterized by chronic, non-progressive liver disease, manifesting as mild hepatic steatosis, increased serum transaminases and alkaline phosphatase, hypercholesterolemia, decreased coagulation factors, and reduced ceruloplasmin, with a transferrin glycosylation profile indicative of a type II CDG.[1] OMIM summarizes CDG type IIp (CDG2P) as an autosomal recessive metabolic disorder with mild liver dysfunction often detected incidentally in adolescence and characterized by elevated liver enzymes, alkaline phosphatase, coagulation factor deficiencies, hypercholesterolemia, and low ceruloplasmin, alongside a combined defect of N- and O-glycosylation.[2]  

The initial description of TMEM199 deficiency by Jansen and colleagues established the entity as a disorder of Golgi homeostasis presenting with elevated aminotransferases, alkaline phosphatase, and cholesterol, steatosis, and abnormal glycosylation, with serum protein isoelectric focusing showing combined N- and O-glycosylation defects.[6] Subsequently, Vajro and co-workers expanded the clinical spectrum by reporting three additional patients with similar biochemical and hepatic phenotypes and confirmed the long-term benign, non-progressive course of liver disease over more than two decades in some individuals.[3][8] More recent case reports, including the first Chinese patient described by Fang and colleagues and a Sicilian patient described by Fiumara and collaborators, have added findings such as strabismus, mild psychomotor delay, and cirrhosis in one case, but overall support the notion that TMEM199-CDG is predominantly a liver-limited or liver-predominant glycosylation disorder.[7][11][16]  

### 1.2 Key Identifiers and Classification Codes

TMEM199-CDG is associated with several major disease identifiers in international genetic and rare disease databases. OMIM assigns the phenotype entry “Congenital disorder of glycosylation, type IIp” the number **616829**, and links it to the TMEM199 gene locus entry **616815**, located on chromosome 17q11.2.[2][4] Orphanet lists TMEM199-CDG with the disease identifier Orpha number **466703** and includes ICD-10 coding under E77.8 (“Other disorders of protein metabolism”), consistent with other CDGs.[1] Orphanet further indicates a prevalence of less than 1 per 1,000,000 and specifies autosomal recessive inheritance.[1] ClinVar and the Genetic Testing Registry (GTR) reference CDG type IIp (616829) as a condition for which clinical genetic testing is offered, although specific clinical validity and utility assessments are noted as “not provided” in the GTR summary.[9]  

At present, a specific MONDO (Mondo Disease Ontology) identifier for TMEM199-CDG or CDG type IIp was not clearly retrieved from the available search results, although MONDO likely contains a term such as “congenital disorder of glycosylation type IIp” aligned with the OMIM entry.[2][14] MeSH does not appear to have a unique heading specifically dedicated to TMEM199-CDG, and the condition would generally be indexed under broader MeSH terms such as “Glycosylation Disorders” or “Liver Diseases, Metabolic,” in parallel with other CDGs. From an ontology perspective, an appropriate MONDO term name would be *“congenital disorder of glycosylation type IIp”*, while the overarching category is a Mendelian inborn error of metabolism, corresponding to MONDO’s class of inherited metabolic disorders and OMIM’s classification as a metabolic CDG.[2][6][13]  

### 1.3 Synonyms and Alternative Names

Several synonyms and alternative designations for TMEM199-CDG have been used in the literature and rare disease databases, reflecting both the gene-based and glycosylation-based naming conventions. Orphanet lists the following synonyms: *“Anomalie congénitale de la glycosylation type 2p”*, *“Anomalie congénitale de la glycosylation type IIp”*, *“CDG-IIp”*, *“CDG2P”*, *“Syndrome CDG type IIp”*, and *“Syndrome des glycoprotéines déficientes en hydrates de carbone IIp.”*[1] OMIM uses “Congenital disorder of glycosylation, type IIp” as its preferred name, and recent clinical papers commonly use “TMEM199-CDG” to emphasize the causative gene, consistent with the trend in CDG nomenclature to link subtype names to gene symbols.[2][3][6][11][13] In English-language clinical and mechanistic reports, “TMEM199 deficiency” and “TMEM199-congenital disorder of glycosylation” are also used, particularly in the context of experimental models and mechanistic investigations.[6][10][13][16]  

### 1.4 Nature of Information and Data Sources

Information about TMEM199-CDG is currently derived primarily from aggregated disease-level resources and a very small number of detailed case reports and mechanistic studies rather than from large cohort or population-level datasets. Orphanet and OMIM provide synthesized descriptions based on published case series and mechanistic work, summarizing key clinical features, inheritance, and molecular pathogenesis.[1][2][4] The primary clinical data originate from at least three small series or individual case reports: the initial description by Jansen et al. that identified TMEM199 deficiency as a disorder of Golgi homeostasis,[6] the three unreported cases with long-term follow-up described by Vajro et al.,[3][8] the Chinese boy reported by Fang et al.,[11][16] and the Sicilian case analyzed by Fiumara and collaborators.[7]  

These human clinical reports provide detailed biochemical, histological, and genetic data, including transferrin glycosylation patterns, liver biopsies, and TMEM199 protein expression. They are complemented by mechanistic work in cell lines and mouse models, particularly the eLife study by Miles and colleagues, which characterized TMEM199 as a V-ATPase assembly factor and explored its role in HIF1α stabilization and iron metabolism,[10] and the lipid droplet–lysosome interaction study by Larsen et al., which developed a mouse knock-in model carrying the human Ala7Glu TMEM199 mutation and hepatocyte models with siRNA-mediated TMEM199 knockdown.[13] Collectively, these sources constitute the basis for current understanding of TMEM199-CDG at clinical, genetic, and mechanistic levels.  

## 2. Etiology

### 2.1 Genetic Causal Factors

The primary and defining cause of TMEM199-CDG is biallelic germline pathogenic variants in the TMEM199 gene, which encodes a transmembrane protein homologous to the yeast V-ATPase assembly factor Vma12p and is involved in Golgi homeostasis and V-ATPase assembly.[2][4][6][10] OMIM states that a number sign (#) is used with the CDG2P entry because congenital disorder of glycosylation type IIp is caused by homozygous or compound heterozygous mutations in TMEM199 located at chromosome 17q11.2.[2] In the original series, Jansen et al. identified homozygous or compound heterozygous TMEM199 mutations in four patients from three unrelated families, and showed in patient fibroblasts a generalized defect in Golgi processing of protein-linked glycans that could be rescued by transduction with wild-type TMEM199, providing compelling evidence for causality and a loss-of-function mechanism.[2][6]  

Subsequent clinical series have expanded the allelic heterogeneity. Vajro et al. reported three novel TMEM199-CDG patients who all carried the same compound heterozygous constellation of variants—c.13-14delTT (p.Ser4Serfs*30), an early frameshift variant, and c.92G>C (p.Arg31Pro), a missense variant previously described.[3][8] Western blot analysis confirmed reduced levels of TMEM199 protein in patient fibroblasts, and all patients showed similar glycosylation defects, supporting a consistent phenotype for these variants.[3] Fang et al. described a Chinese boy with TMEM199-CDG harboring a frameshift variant c.128delA/p.Lys43Argfs*25 along with another missense allele, and documented reduced expression of TMEM199 by immunohistochemistry in liver tissue.[11][16] Fiumara et al. reported a Sicilian girl homozygous for the c.92G>C (p.Arg31Pro) variant, further cementing this missense variant as a recurrent pathogenic allele in southern Mediterranean populations.[7]  

Together, these reports indicate that TMEM199-CDG is caused by germline biallelic TMEM199 variants leading to reduced or absent functional TMEM199 protein, typically through missense changes near the N-terminus, early truncating frameshift mutations, or other loss-of-function alleles.[2][3][6][7][11][16] Mechanistic studies in human cells and mouse models reinforce the view that TMEM199 functions as an ER-localized assembly factor for the V-ATPase complex, and that its deficiency disrupts acidification of Golgi and endo-lysosomal compartments, causing secondary defects in glycosylation and lipid homeostasis.[10][13]  

### 2.2 Environmental and Non-Genetic Factors

To date, no consistent environmental, toxic, infectious, or lifestyle factors have been identified as primary causes of TMEM199-CDG, and the disease is universally described as a Mendelian autosomal recessive condition caused by inborn errors of metabolism.[1][2][3][6][11][16] The reported cases belong largely to non-consanguineous or mildly consanguineous families in European and Chinese populations, and there is no evidence that environmental exposures such as hepatotoxic medications, alcohol, or toxins play causal roles, although such factors might theoretically modulate disease severity in individual patients. Vajro et al. emphasize that TMEM199-CDG patients were misdiagnosed for years as having idiopathic liver disease, but there is no indication that environmental hepatotoxins were involved.[3][8] Fang et al. explicitly characterize TMEM199-CDG as a rare autosomal recessive inherited disease, and their patient’s liver manifestations were not linked to exogenous factors.[11][16]  

In the mouse model described by Larsen and colleagues, a knock-in of the human Ala7Glu TMEM199 mutation on a chow diet was sufficient to cause marked hepatic steatosis and glycosylation defects in the absence of special dietary or toxic challenges, underscoring that TMEM199 deficiency alone is sufficient to drive key aspects of the phenotype in a physiological context.[13] The authors note that plasma N-glycans were hypogalactosylated and hepatic triglyceride content was significantly increased, yet plasma lipid abnormalities were relatively modest, which may reflect species differences rather than environmental influences.[13]  

### 2.3 Genetic Risk Factors Beyond Causative Variants

Because TMEM199-CDG is extremely rare, with fewer than ten reported patients worldwide, there is currently no robust evidence for additional genetic susceptibility loci, modifier genes, or polygenic contributions beyond the primary TMEM199 variants.[1][2][3][7][11][16] The clustering of the c.92G>C (p.Arg31Pro) variant in southern Mediterranean populations, with cases from Greece and southern Italy including Campania and Sicily, suggests a possible founder effect or regional enrichment of this allele, but large-scale population genetics analyses are lacking.[7] Fiumara et al. report that TMEM199-CDG is an ultra-rare CDG that appears relatively frequent in the southern Mediterranean area, with 7 of 9 patients (77%) in their review carrying the c.92G>C variant.[7] This observation raises the possibility that carrier frequency for this variant may be elevated in specific subpopulations, thereby increasing local disease incidence, but precise frequencies have not been determined through gnomAD or similar databases in the available sources.[7]  

Modifier genes that influence the severity of glycosylation defects or liver disease have not been systematically studied in TMEM199-CDG. However, mechanistic work implicating TMEM199 and its partner CCDC115 as V-ATPase assembly factors suggests that variants in other genes involved in V-ATPase function, Golgi pH regulation, or lipophagy might modulate disease expression.[10][13] For example, Miles et al. identify TMEM199 and CCDC115 as part of the mammalian orthologous complex to yeast Vma12p-Vma22p, and show that disruption of these factors stabilizes HIF1α and perturbs iron metabolism.[10] Larsen et al. demonstrate that TMEM199 and CCDC115 deficiency in hepatocytes leads to increased lysosomal lipid accumulation and impaired autophagic capacity, pointing to potential interactions with other autophagy and lysosomal regulatory genes.[13] Nevertheless, such potential modifier effects remain speculative and have not been documented in human TMEM199-CDG cohorts.  

### 2.4 Protective Factors and Gene–Environment Interactions

No specific genetic protective variants or environmental protective factors have been identified for TMEM199-CDG in the current literature, and there is no evidence that particular diets, medications, or lifestyles provide direct protection against disease onset in genetically susceptible individuals.[1][2][3][6][7][11][13][16] The generally mild and non-progressive nature of liver disease in most reported patients, as documented by Vajro et al. with clinical stability over two decades, suggests that some intrinsic protective mechanisms may limit tissue damage, possibly via partial residual TMEM199 function or compensatory V-ATPase assembly pathways.[3] However, these mechanisms have not been formally elucidated.  

Gene–environment interactions could theoretically influence phenotypic expression, especially given that hepatocellular steatosis and hyperlipidemia are sensitive to environmental factors such as diet, obesity, and alcohol consumption. In the mouse model, TMEM199-Ala7Glu homozygotes on a standard chow diet already show marked hepatic steatosis and glycosylation defects, indicating that environmental stressors are not required for disease expression.[13] The authors did not report the effects of high-fat diet or other nutritional manipulations, and human case reports do not systematically evaluate lifestyle factors, so the role of gene–environment interactions in modulating disease severity remains largely unexplored.  

Overall, TMEM199-CDG should currently be considered a pure Mendelian inborn error of metabolism driven by biallelic TMEM199 variants, with no established non-genetic causal factors and only hypothetical gene–environment interactions of uncertain significance.[1][2][3][6][11][13][16]  

## 3. Phenotypes

### 3.1 Clinical Signs and Symptoms

The core phenotype of TMEM199-CDG is a non-encephalopathic liver disorder with chronic, mildly elevated liver enzymes, hepatic steatosis, sometimes mild fibrosis, and biochemical evidence of abnormal glycosylation, accompanied by hypercholesterolemia and low serum ceruloplasmin and copper.[1][2][3][6][7][11][13][16] Orphanet characterizes TMEM199-CDG as a chronic, non-progressive liver disease presenting with mild steatosis, increased transaminases and alkaline phosphatase, hypercholesterolemia, and decreased coagulation factors and ceruloplasmin.[1] OMIM similarly notes mild liver dysfunction, elevated liver enzymes and alkaline phosphatase, coagulation factor deficiencies, hypercholesterolemia, and low ceruloplasmin, alongside combined N- and O-glycosylation defects.[2]  

In the initial series by Jansen et al., patients exhibited hepatic steatosis on biopsy, elevated aminotransferases (ATs), elevated alkaline phosphatase (ALP), increased cholesterol, and low ceruloplasmin, with abnormal transferrin isoelectric focusing patterns indicative of a type II CDG and combined N- and O-glycosylation defects.[6] Their paper emphasized that TMEM199 deficiency is a disorder of Golgi homeostasis characterized by elevated aminotransferases, alkaline phosphatase, and cholesterol and abnormal glycosylation.[6] Vajro et al. described three unreported TMEM199-CDG patients who all presented with liver disease featuring steatosis, elevated serum transaminases, cholesterol, and alkaline phosphatase, as well as abnormal transferrin glycosylation; importantly, these patients did not show encephalopathy and their liver disease remained non-progressive over long-term follow-up.[3][8] Fang et al.’s Chinese boy demonstrated abnormal liver function with chronically elevated serum transaminases, steatosis and fibrosis progressing to cirrhosis on liver biopsy, decreased serum ceruloplasmin, and abnormal protein glycosylation.[11][16] Fiumara et al.’s Sicilian girl manifested mild, stable hepatopathy with persistent elevations of serum transaminases, low ceruloplasmin and copper, hepatic steatosis and periportal fibrosis, and abnormal N- and O-protein glycosylation, with a liver echo structure that was largely unremarkable on ultrasound.[7]  

Extrahepatic manifestations have been relatively limited but are noteworthy in a few cases. Orphanet notes that patients are generally asymptomatic, though isolated cases of psychomotor developmental delay and hypotonia have been reported.[1] Fang et al. report novel findings such as strabismus and mild psychomotor delay in their Chinese boy, along with cirrhosis.[11][16] Vajro et al. emphasize the absence of encephalopathy in their patients, distinguishing TMEM199-CDG from other Golgi-related CDGs that typically involve both liver and brain.[3][8] There is no consistent report of severe neurodevelopmental disability, seizures, or structural brain anomalies in TMEM199-CDG, which underscores its relative organ specificity.  

Suggested HPO (Human Phenotype Ontology) terms for these phenotypes include: *Elevated serum aminotransferase level* (HP:0002910) for chronic hypertransaminasemia; *Elevated alkaline phosphatase of hepatic origin* (HP:0003155); *Hepatic steatosis* (HP:0001397); *Fibrosis of liver* (HP:0001395); *Cirrhosis* (HP:0001394) for the Chinese case; *Hypercholesterolemia* (HP:0003124); *Reduced serum ceruloplasmin* (HP:0012308); *Abnormal transferrin glycosylation* (HP:0012159); *Strabismus* (HP:0000486); *Mild global developmental delay* (HP:0011343); and *Generalized hypotonia* (HP:0001290).[1][2][3][7][11][16]  

### 3.2 Laboratory Abnormalities

Laboratory abnormalities are central to the recognition of TMEM199-CDG and include both liver biochemistry and specialized glycosylation assays. Elevated serum transaminases (AST and ALT) and increased alkaline phosphatase have been consistently reported in all described patients.[1][2][3][6][7][11][16] Hypercholesterolemia, particularly elevated total and LDL cholesterol, is another hallmark, although some patients may have relatively normal plasma lipid levels despite hepatic steatosis, as noted in the mouse model.[6][13] Low serum ceruloplasmin and copper levels are striking biochemical features that can suggest Wilson disease, yet urinary copper excretion remains normal and neuropsychiatric features of Wilson disease are absent.[6][7][11][16]  

Transferrin isoelectric focusing (Tf-IEF) reveals a type II CDG pattern, with decreased sialylation and altered glycoform distribution indicative of abnormal glycan processing rather than assembly.[3][6][7][11][13][16] Fiumara et al. note that matrix-assisted laser desorption/ionization mass spectrometry (MALDI-MS) of N- and O-proteins showed abnormal glycosylation patterns consistent with a defect in Golgi processing, further underscoring TMEM199’s role in Golgi homeostasis.[7] Vajro et al. emphasize that a hallmark finding in TMEM199-CDG and related disorders affecting Golgi homeostasis is deficiency in protein glycosylation, both in N- and O-linked types.[3][8]  

Suggested HPO laboratory terms include *Abnormal liver function tests* (HP:0002910 broadened), *Elevated serum cholesterol* (HP:0003119), *Decreased serum ceruloplasmin* (HP:0012308), *Decreased serum copper* (HP:0002902), and *Abnormal transferrin glycosylation* (HP:0012159).[1][2][3][6][7][11][16]  

### 3.3 Age of Onset, Severity, and Progression

TMEM199-CDG typically manifests during infancy, childhood, or adolescence, although symptoms may be subtle and the diagnosis often delayed until adolescence or adulthood due to the mildness of clinical manifestations.[1][2][3][7][11][16] Orphanet indicates that age of onset ranges from early infancy to childhood and adolescence.[1] OMIM notes that mild liver dysfunction may be discovered incidentally during adolescence.[2] Vajro et al. reported that one patient’s liver enzyme abnormalities were detected in childhood and persisted over more than two decades without significant clinical deterioration, highlighting a chronic yet non-progressive course.[3][8] Fiumara et al.’s Sicilian patient presented with elevated transaminases since early childhood, and at age 12 still had mild, stable hepatopathy with unremarkable liver ultrasound findings aside from periportal fibrosis.[7]  

Severity is generally mild to moderate for liver disease, with most patients being clinically asymptomatic or minimally symptomatic despite biochemical abnormalities.[1][3][6][7] However, Fang et al. report a more severe phenotype with cirrhosis on liver biopsy in their Chinese boy, indicating that progression to advanced liver disease can occur in some cases.[11][16] Psychomotor delay and strabismus in this patient are also relatively mild compared to severe neurological manifestations in many other CDGs, and no encephalopathy has been reported in TMEM199-CDG cohorts.[3][8][11][16] Overall, symptom progression is typically stable or very slowly progressive for hepatic manifestations, with possible variability in fibrosis progression among individuals.  

From a quality-of-life perspective, the impact of TMEM199-CDG appears relatively limited compared to multisystem CDGs, as most patients maintain normal daily functioning and lack significant neurodevelopmental impairment.[1][3][8][11][16] Liver disease has not led to liver failure or need for transplantation in the published cases, though the presence of cirrhosis in one patient underscores the potential for more serious consequences if fibrosis advances.[11][16] Formal quality-of-life assessments (e.g., EQ-5D or SF-36) have not been reported specifically for TMEM199-CDG, but the clinical narratives suggest near-normal functional status in most patients, with disease burden largely reflected in chronic medical surveillance and biochemical abnormalities rather than overt disability.[3][7][11][16]  

### 3.4 Phenotype Frequency and Variability

Given the extremely small number of reported patients, precise quantitative frequencies of individual phenotypic features cannot be robustly established. Nonetheless, some features are present in nearly all described cases and can be considered typical. Chronic elevation of serum transaminases and alkaline phosphatase, hepatic steatosis, abnormal transferrin glycosylation with a type II pattern, and low ceruloplasmin are consistently reported across Jansen’s initial cohort, Vajro’s three patients, Fang’s Chinese patient, and Fiumara’s Sicilian case.[3][6][7][11][16] Hypercholesterolemia is common but not universal, with some species differences observed in mouse models.[6][13]  

Extrahepatic features such as strabismus, mild psychomotor delay, and hypotonia appear in only a minority of patients and may represent variable expressivity rather than core manifestations.[1][11][16] The presence of cirrhosis in one patient indicates variability in fibrosis progression, potentially influenced by allelic differences, modifier factors, or environmental influences, though these remain speculative.[11][16] Expressivity is therefore variable but biased toward liver-predominant disease with limited systemic involvement. Penetrance is presumed to be high for biochemical liver abnormalities in individuals with biallelic TMEM199 loss-of-function, based on mouse lethality of full knockout and consistent hepatic phenotypes in human patients, but the exact penetrance across unreported carriers is unknown.[2][4][13]  

## 4. Genetic and Molecular Information

### 4.1 Causal Gene and Basic Gene Information

The causal gene for TMEM199-CDG is **TMEM199** (transmembrane protein 199), which OMIM designates under the gene entry number **616815**.[4] TMEM199 is located on chromosome 17q11.2, with genomic coordinates on GRCh38 at 17:28,357,647–28,363,683.[4] TMEM199 encodes a multi-pass transmembrane protein homologous to the yeast vacuolar ATPase assembly factor Vma12p (also known as Vph2p), and appears to be involved in Golgi homeostasis and V-ATPase assembly.[4][10][12] Miles et al. note that TMEM199 is a putative transmembrane protein with 24% sequence identity to yeast Vma12p, and that TMEM199 associates with V-ATPase subunits ATP6V0D1 and ATP6V0A2, forming part of the mammalian orthologous assembly complex to Vma12p-Vma22p.[10] GeneCards and related resources describe the yeast VMA12 gene as encoding a vacuolar ATPase assembly factor that supports assembly of the vacuolar proton-transporting V-type ATPase complex, underscoring the evolutionary conservation of TMEM199’s function.[12]  

From a Gene Ontology (GO) perspective, TMEM199 is associated with GO terms such as *“vacuolar proton-transporting V-type ATPase complex assembly”* (GO:0070072), *“endoplasmic reticulum membrane”* (GO:0005789), and *“Golgi organization”* (GO:0007030), reflecting its role as an ER-localized assembly factor that influences the function and localization of V-ATPase complexes in endo-lysosomal and Golgi compartments.[4][10][13] Suggested HGNC nomenclature is the approved symbol **TMEM199** with name “Transmembrane protein 199,” as indicated in OMIM.[4]  

### 4.2 Pathogenic Variants and Variant Types

Reported pathogenic TMEM199 variants in TMEM199-CDG include both missense and frameshift mutations, generally clustered near the N-terminal portion of the protein and predicted to result in loss of function through impaired protein stability or truncated protein products.[2][3][7][11][16] The recurrent missense variant c.92G>C (p.Arg31Pro) has been identified in multiple unrelated families from southern Italy and Greece and is considered a pathogenic allele based on its segregation with disease, predicted deleterious impact on protein structure, and associated glycosylation defects.[3][7] Jansen et al. reported several missense and truncating variants in their initial cohort, though details beyond the four specific allele numbers (616815.0001–616815.0004) are summarized rather than fully enumerated in the OMIM entry.[2][6]  

Vajro et al. describe three patients carrying compound heterozygous TMEM199 variants c.13-14delTT (p.Ser4Serfs*30), an early frameshift that introduces a premature stop codon, and c.92G>C (p.Arg31Pro), a missense change that substitutes proline for arginine at position 31.[3][8] The authors deemed the frameshift variant pathogenic due to its early disruption of the coding sequence, and western blot analysis confirmed reduced levels of TMEM199 protein in patient fibroblasts.[3] Fang et al. report a frameshift variant c.128delA/p.Lys43Argfs*25 in their Chinese patient, again introducing a premature termination and resulting in truncated TMEM199, and demonstrate reduced expression of TMEM199 on liver immunohistochemistry.[11][16] Fiumara et al.’s Sicilian patient carried the homozygous c.92G>C (p.Arg31Pro) variant, reinforcing its pathogenicity and suggesting a founder effect in the southern Mediterranean region.[7]  

The variant classification according to ACMG/AMP guidelines is not explicitly detailed in the available sources, but the combination of segregation data, functional evidence (reduced TMEM199 protein levels and glycosylation defects rescued by wild-type TMEM199), and consistent phenotype strongly supports classification of these variants as **pathogenic**.[2][3][6][11][13][16] Allele frequencies in population databases such as gnomAD are not reported, though Fiumara et al. infer a higher frequency of c.92G>C in southern Mediterranean populations based on the concentration of cases.[7] All reported variants are germline and inherited in an autosomal recessive manner, with affected individuals being homozygous or compound heterozygous; no somatic TMEM199 mutations have been associated with TMEM199-CDG.[2][3][6][7][11][16]  

Functionally, these variants lead to loss of TMEM199 function, either through truncation or through destabilization of the protein, and result in impaired V-ATPase assembly, decreased acidification of Golgi and endo-lysosomal compartments, and downstream glycosylation and lipid homeostasis defects.[6][10][13] Jansen et al. highlight that patient fibroblasts show generalized defects in Golgi processing of protein-linked glycans compared to controls, which were rescued after transduction with wild-type TMEM199, directly demonstrating the functional consequences of the pathogenic variants.[2][6]  

### 4.3 Modifier Genes and Epigenetic Information

No specific modifier genes have been reported for TMEM199-CDG, and epigenetic contributions such as DNA methylation or histone modifications have not been studied in this ultra-rare disorder.[1][2][3][6][7][11][13][16] Given the mechanistic link between TMEM199 and CCDC115 as V-ATPase assembly factors, mutations in CCDC115 cause a related glycosylation disorder with liver storage disease phenotype, and it is conceivable that concurrent or interacting variants in CCDC115 or other V-ATPase subunits could modify disease expression, but no such cases have been documented.[6][10][13] Epigenomic databases like ENCODE or Roadmap Epigenomics have not specifically profiled TMEM199-CDG, and thus epigenetic data remain unavailable.  

Chromosomal abnormalities such as large deletions, duplications, or translocations involving the TMEM199 locus have not been reported as causes of TMEM199-CDG in the literature surveyed, and disease-causing variants appear to be point mutations or small indels rather than structural variants.[2][4][6][11][13][16]  

## 5. Environmental Information

### 5.1 Environmental and Lifestyle Contributors

As a Mendelian autosomal recessive congenital disorder of glycosylation, TMEM199-CDG is fundamentally genetic in origin, and current evidence does not identify specific environmental toxins, radiation exposures, occupational hazards, or infectious agents as causative factors.[1][2][3][6][7][11][16] Patients described in Jansen’s, Vajro’s, Fiumara’s, and Fang’s studies did not have histories of significant hepatotoxic exposures or infections that could explain their liver phenotypes, and TMEM199-CDG was ultimately diagnosed on the basis of genetic and glycosylation analyses.[3][6][7][11][16]  

Lifestyle factors such as diet, exercise, alcohol consumption, and smoking might influence liver fat content and fibrosis progression in general, but these have not been systematically evaluated in TMEM199-CDG cohorts. The mouse model carrying the Ala7Glu TMEM199 mutation developed marked hepatic steatosis on a standard chow diet without the need for high-fat feeding or other environmental stressors, indicating that TMEM199 deficiency alone is sufficient to drive fatty liver disease in this context.[13] While additional environmental insults (e.g., high-fat diet, alcohol, viral hepatitis) might theoretically exacerbate liver disease in TMEM199-CDG, such interactions have not been studied or reported.  

No infectious agents are implicated as triggers for TMEM199-CDG; the condition does not resemble autoimmune or infectious hepatitis, and serologic investigations in the reported patients did not identify viral hepatitis or other infectious causes.[3][7][11][16] Thus, environmental and lifestyle information currently plays a minimal role in the etiological framework of TMEM199-CDG, although standard advice to minimize general hepatotoxic exposures is prudent in clinical care.  

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation

Step 1: Biallelic pathogenic variants in TMEM199 lead to reduced or absent TMEM199 protein function in hepatocytes and other cells.[2][3][6][11][16]  

Step 2: TMEM199 deficiency impairs assembly and trafficking of the vacuolar H\(^+\)-ATPase (V-ATPase) complex in the endoplasmic reticulum, leading to defective proton pump localization and function in Golgi, endosomal, and lysosomal membranes.[6][10][13]  

Step 3: Impaired V-ATPase function results in reduced acidification of Golgi and endo-lysosomal compartments, causing disturbance of Golgi homeostasis and lysosomal dysfunction.[6][10][13]  

Step 4: Golgi deacidification disrupts the activity and localization of glycosyltransferases and glycosidases, leading to combined defects in N- and O-linked glycosylation of secretory and membrane proteins, including transferrin and other serum glycoproteins.[2][3][6][7][11][13][16]  

Step 5: Lysosomal deacidification and impaired autophagic flux, particularly lipophagy, lead to accumulation of lipid droplets and lysosomal lipid, resulting in hepatic steatosis and altered lipid droplet–lysosome interactions.[13]  

Step 6: Altered lipid handling and hepatic steatosis promote increased secretion of apoB-containing lipoprotein particles, contributing to hypercholesterolemia and hyperlipidemia in many patients.[6][13]  

Step 7: Golgi dysfunction and glycosylation defects affect the synthesis, trafficking, and stability of ceruloplasmin and copper-handling proteins, leading to low serum ceruloplasmin and copper with normal urinary copper excretion, a biochemical profile mimicking Wilson disease without its neurologic features.[3][6][7][11][16]  

Step 8: Chronic but relatively mild hepatocellular injury and cholestatic disturbance, driven by steatosis, lysosomal dysfunction, and glycosylation defects, result in persistent elevation of aminotransferases and alkaline phosphatase, mild periportal fibrosis, and in rare cases progression to cirrhosis.[3][7][11][16]  

Step 9: In cell culture models, TMEM199 deficiency stabilizes HIF1α via intracellular iron depletion secondary to V-ATPase inhibition, resulting in hypoxia-inducible factor activation, although the extent to which this contributes to clinical manifestations in TMEM199-CDG patients remains inferred rather than directly demonstrated.[10]  

Step 10: The predominantly hepatic expression of the pathophysiological cascade, coupled with partial residual TMEM199 function in hypomorphic alleles, leads to a non-encephalopathic, liver-predominant phenotype with minimal brain involvement, distinguishing TMEM199-CDG from other Golgi-related CDGs that feature severe neurodevelopmental pathology.[3][6][8][11][16]  

### 6.2 Molecular Pathways and Protein Dysfunction

At the molecular level, TMEM199 participates in the assembly and function of the vacuolar H\(^+\)-ATPase (V-ATPase), a multi-subunit proton pump responsible for acidifying endosomes, lysosomes, and Golgi compartments.[6][10][12][13] Miles et al. performed a genetic screen for factors regulating HIF1α stability and identified TMEM199 as a previously uncharacterized V-ATPase accessory protein required for V-ATPase function.[10] They showed that TMEM199 interacts with V-ATPase subunits ATP6V0D1 and ATP6V0A2, and localizes predominantly to the endoplasmic reticulum, suggesting a role in V-ATPase assembly rather than in the mature complex.[10] They further demonstrated that TMEM199 and CCDC115 depletion prevents acidification of endosomes in HeLa cells, similar to pharmacologic inhibition of V-ATPase, and leads to intracellular iron depletion and HIF1α stabilization in normoxia.[10]  

In TMEM199-CDG patients, TMEM199 protein levels are reduced or absent due to truncating or destabilizing missense variants, resulting in impaired V-ATPase assembly and trafficking to Golgi and endo-lysosomal membranes.[2][3][6][11][13][16] Jansen et al. hypothesized that failure to acidify the Golgi apparatus affects the complex glycosylation machinery, leading to abnormal glycosylation, and confirmed that patient fibroblasts showed generalized defects in Golgi processing of protein-linked glycans that were rescued by wild-type TMEM199 transduction.[6] TMEM199 deficiency is therefore a prototypical example of a disorder of Golgi homeostasis, where the primary molecular defect lies in the proton pump assembly rather than in glycosyltransferases themselves.[6][13]  

From a structural perspective, TMEM199 mutations such as Ala7Glu, Arg31Pro, and early frameshift variants likely disrupt transmembrane helices or luminal domains required for interaction with V-ATPase subunits, resulting in misfolding, ER retention, or degradation of TMEM199.[3][7][11][13][16] The loss-of-function nature of these variants is supported by western blot and immunohistochemistry data showing markedly reduced TMEM199 protein in patient fibroblasts and mouse livers.[3][11][13] The functional consequences align with GO terms like *“vacuolar proton-transporting V-type ATPase complex assembly”* and *“regulation of organelle pH”* (GO:0030148), linking TMEM199 function to organelle acidification and downstream glycosylation processes.[4][10][13]  

### 6.3 Cellular Processes: Golgi Homeostasis, Autophagy, and Lipid Metabolism

TMEM199 deficiency affects several key cellular processes: Golgi homeostasis and glycosylation, lysosomal function and autophagy, and lipid droplet handling. Jansen et al. emphasize that in a subgroup of CDGs, abnormal glycosylation of serum proteins is caused by disturbance of Golgi homeostasis, and TMEM199 deficiency exemplifies this subgroup.[6] Loss of TMEM199 impairs V-ATPase–mediated acidification of Golgi stacks, which is essential for the proper function of Golgi-located glycosylation enzymes, including glycosyltransferases and glycosidases that require specific pH optima.[6][13] The resulting glycosylation defect manifests as hypogalactosylation and altered sialylation of N-glycans and O-glycans, as documented in plasma N-glycan profiles of TMEM199-deficient mice and human patients.[13]  

Larsen et al. investigated the consequences of TMEM199 deficiency in hepatocyte models and a mouse knock-in model carrying the human Ala7Glu variant.[13] They found that TMEM199 and CCDC115 deficiency caused increased numbers and size of lipid droplets, including abnormally large droplets that co-localized with lysosomes, suggesting impaired lipid droplet–lysosome interaction and lipophagy.[13] Importantly, they did not observe excessive de novo lipogenesis, failing oxidative capacity, or elevated lipid uptake, indicating that the hepatic steatosis observed in TMEM199 deficiency arises primarily from impaired lysosomal degradation of lipid droplets rather than increased lipid synthesis.[13] Mechanistically, they observed impaired lysosomal acidification, reduced autophagic capacity, and increased lysosomal lipid accumulation, highlighting the importance of lipophagy in fatty liver disease and linking TMEM199 deficiency to autophagy-related GO processes such as *“macroautophagy”* (GO:0016236) and *“lipid catabolic process”* (GO:0016042).[13]  

Their data further suggested that hypercholesterolemia in TMEM199 and CCDC115 deficiency is due to increased secretion of apoB-containing lipoproteins, possibly secondary to hepatic steatosis and altered lipid droplet dynamics.[13] The mouse model, in which full Tmem199 knockout was embryonic lethal, showed that homozygous Ala7Glu mice had marked hepatic steatosis, hypogalactosylation of plasma N-glycans, and impaired Golgi and lysosomal function, but surprisingly no clear plasma lipid abnormalities, underscoring differences between species and suggesting that hyperlipidemia may not be as prominent in mice as in humans.[13]  

These findings place TMEM199-CDG within a conceptual framework where defects in organelle acidification and glycosylation intersect with autophagy and lipid metabolism, contributing to liver-specific pathology. Suggested GO terms for the involved biological processes include *“Golgi organization”* (GO:0007030), *“lysosomal lumen acidification”*, *“regulation of autophagy”* (GO:0010506), and *“lipid storage”* (GO:0019915).[6][10][13]  

### 6.4 Biochemical Abnormalities and Metabolic Changes

Biochemically, TMEM199-CDG features several interrelated abnormalities: defective glycosylation of serum proteins, altered lipid metabolism, and disturbed copper and ceruloplasmin handling. Glycosylation defects arise from disruption of Golgi pH regulation and enzymatic activity, leading to combined N- and O-glycosylation defects manifested as abnormal transferrin glycoform patterns (type II CDG pattern) and hypogalactosylation of plasma N-glycans.[2][3][6][7][13][16] In patients and mice, glycan profiling reveals reduced terminal galactose and sialic acid residues and increased underprocessed structures, consistent with impaired glycan maturation.[13]  

Lipid metabolic changes include hepatic triglyceride accumulation (steatosis) and increased secretion of apoB-containing lipoproteins leading to hypercholesterolemia.[6][13] Larsen et al. report that hepatic triglyceride levels were approximately 80% higher in Tmem199-Ala7Glu mice than in controls, and that hepatocyte models with TMEM199 knockdown showed increased lysosomal lipid accumulation, indicating failure of lipid catabolism.[13] They note that excessive de novo lipogenesis, failing oxidative capacity, and elevated lipid uptake were not observed, suggesting that the primary defect lies in lysosomal lipid clearance rather than in upstream lipid synthesis.[13]  

Copper and ceruloplasmin metabolism is also affected. TMEM199-CDG patients consistently show low serum ceruloplasmin and copper levels, yet urinary copper excretion remains normal, distinguishing them from Wilson disease.[3][6][7][11][16] The mechanism is not fully elucidated but likely involves defective glycosylation and Golgi processing of ceruloplasmin and copper-transporting proteins such as ATP7B, resulting in altered protein stability, secretion, or function.[6][7][16] These biochemical abnormalities correspond to CHEBI entities such as “triglyceride,” “cholesterol,” “copper(II) ion,” and “ceruloplasmin,” and highlight how a single defect in an organelle assembly factor can ripple across multiple metabolic systems.  

### 6.5 Upstream and Downstream Mechanisms

The upstream mechanism in TMEM199-CDG is the genetic loss-of-function of TMEM199, which impairs V-ATPase assembly and organelle acidification.[2][4][6][10][13] This upstream lesion is followed by intermediate mechanisms involving Golgi homeostasis disruption, glycosyltransferase dysfunction, and lysosomal autophagy impairment.[6][10][13] Downstream mechanisms include hepatic steatosis, hyperlipidemia, altered copper and ceruloplasmin metabolism, chronic hepatocellular injury, and fibrosis.[3][7][11][13][16] The absence of significant brain involvement suggests that downstream effects are preferentially expressed in hepatocytes and perhaps other liver-resident cell types such as Kupffer cells and hepatic stellate cells, aligning with the observed liver storage disease phenotype.[6][13][16]  

Cell types involved include hepatocytes (CL:0000182), which are the primary cells exhibiting steatosis, glycosylation defects, and altered lipoprotein secretion; liver sinusoidal endothelial cells; Kupffer cells (liver-resident macrophages); and hepatic stellate cells (CL:0002078), which participate in fibrosis.[13][16] At the subcellular level, key compartments affected are the endoplasmic reticulum (GO:0005783), Golgi apparatus (GO:0005794), endosomes (GO:0005768), and lysosomes (GO:0005764).[6][10][13]  

### 6.6 Advanced Technologies and Molecular Profiling

Advanced technologies such as CRISPR/Cas9 genome editing, mass spectrometry-based glycomics, and confocal microscopy have been applied to study TMEM199 deficiency. Larsen et al. used CRISPR/Cas9-mediated knock-in to generate mice carrying the Ala7Glu TMEM199 mutation observed in patients, and applied Western blotting and RT-qPCR to show that Tmem199 mRNA expression was reduced by approximately 52% and that virtually no TMEM199 protein could be detected in mouse livers.[13] They also used matrix-assisted laser desorption/ionization (MALDI) mass spectrometry to analyze plasma N-glycans, revealing hypogalactosylation consistent with patient phenotypes.[13] Confocal microscopy and live-cell imaging were used to visualize lipid droplet–lysosome interactions and autophagic structures, demonstrating colocalization and impaired lysosomal lipid clearance.[13]  

Miles et al. employed CRISPR knockout of TMEM199 in HeLa cells, combined with immunoprecipitation and mass spectrometry, to identify TMEM199-interacting proteins and confirm its association with V-ATPase subunits.[10] They used immunofluorescence to show that TMEM199 localizes predominantly to the ER and that its depletion prevents acidification of endosomes, thus providing a cellular mechanistic framework.[10] These studies integrate proteomics, functional genomics screens, and imaging, but large-scale transcriptomic or metabolomic profiling of TMEM199-CDG patients has not yet been reported.  

Single-cell analysis, spatial transcriptomics, and multi-omics integration specific to TMEM199-CDG have not been described, reflecting the nascent stage of research in this ultra-rare disorder. However, the available mechanistic data highlight the potential for future multi-omics studies to further dissect cell-type specific mechanisms and identify potential therapeutic targets, particularly in pathways related to autophagy, organelle biogenesis, and lipid metabolism.  

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

The primary organ affected in TMEM199-CDG is the **liver**, corresponding to UBERON term *UBERON:0002107 (liver).* Hepatic involvement is evident in all reported patients through chronic elevation of liver enzymes, hepatic steatosis, fibrosis, and, in one case, cirrhosis.[1][2][3][6][7][11][16] Jansen et al. describe a hepatic phenotype with steatosis and abnormal glycosylation, and Vajro et al. confirm a non-progressive liver disorder with steatosis and hypertransaminasemia.[3][6][8] Fiumara et al. report periportal fibrosis and steatosis, while Fang et al. observe cirrhosis on liver biopsy.[7][11][16]  

Secondary organ involvement appears limited. The brain and nervous system, which are frequently affected in many CDGs, show minimal involvement in TMEM199-CDG. Orphanet notes that patients are generally asymptomatic, with only isolated cases of psychomotor delay and hypotonia.[1] Fang et al.’s patient had mild psychomotor delay and strabismus but no severe encephalopathy.[11][16] The cardiovascular, respiratory, and endocrine systems are not prominently involved in published cases, although hyperlipidemia could have long-term cardiovascular implications if unmanaged. The digestive system is affected primarily at the hepatic level, without reported enteropathy or pancreatitis.[3][7][11][16]  

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, TMEM199-CDG predominantly affects hepatic parenchyma, including hepatocytes, as well as the sinusoidal microenvironment comprising endothelial cells, Kupffer cells, and stellate cells. Hepatic tissue shows steatosis (accumulation of lipid droplets in hepatocytes), mild to moderate fibrosis (periportal and perisinusoidal collagen deposition), and in rare cases cirrhotic nodular architecture.[3][7][11][13][16] These changes correspond to histopathological entities recognizable in SNOMED CT and pathology classification systems, such as “fatty change of liver” and “hepatic fibrosis.”  

Cell Ontology terms relevant to TMEM199-CDG include *CL:0000182 (hepatocyte)* for the primary parenchymal cells showing glycosylation defects and steatosis; *CL:0002078 (hepatic stellate cell)* for cells involved in fibrogenesis; and *CL:0000731 (Kupffer cell)* for liver-resident macrophages that participate in autophagy and lipid handling.[13][16] In the mouse model, hepatocytes exhibited enlarged lipid droplets co-localized with lysosomes, and lysosomal acidification was impaired, highlighting hepatocyte involvement in the pathophysiology.[13]  

### 7.3 Subcellular Compartments

Subcellular compartments critically involved in TMEM199-CDG include the endoplasmic reticulum (ER), Golgi apparatus, endosomes, and lysosomes. TMEM199 localizes predominantly to the ER membrane (GO:0005789), where it functions as an assembly factor for the V-ATPase complex.[4][10] Golgi stacks (GO:0005794) rely on V-ATPase-mediated acidification to maintain pH gradients necessary for sequential glycosylation reactions, and TMEM199 deficiency leads to Golgi deacidification and disruption of glycosyltransferase activity.[6][13] Endosomes (GO:0005768) and lysosomes (GO:0005764) also depend on V-ATPase for acidification, and TMEM199 deficiency impairs lysosomal function and autophagic flux, as shown by Larsen et al. in hepatocyte models.[13]  

These subcellular compartments are integral to the secretory and endocytic pathways, and their dysfunction explains the glycosylation defects and lipid storage phenomena observed in TMEM199-CDG. Suggested GO Cellular Component terms thus include *“endoplasmic reticulum membrane”* (GO:0005789), *“Golgi membrane”* (GO:0000139), *“lysosome”* (GO:0005764), and *“endosome”* (GO:0005768).[4][6][10][13]  

### 7.4 Localization and Lateralization

Anatomically, TMEM199-CDG does not exhibit lateralization in the sense of unilateral or asymmetric organ involvement. Liver pathology is diffuse, involving the organ globally rather than focal segments, as is typical for metabolic liver disease.[3][7][11][16] Psychomotor delay and strabismus, when present, do not suggest lateralized brain lesions but rather mild global functional impairment. There is no evidence of localized lesions in imaging or histopathology that would indicate particular anatomical sites within the liver beyond periportal predominance of fibrosis.[7][11][16]  

## 8. Temporal Development

### 8.1 Onset and Course

TMEM199-CDG is a congenital condition in the sense that the genetic defect is present from conception, but clinical manifestations typically become apparent in childhood or adolescence through detection of persistent liver enzyme abnormalities.[1][2][3][7][11][16] Orphanet lists age of onset as infancy, childhood, or adolescence, reflecting variability in the timing of clinical recognition.[1] OMIM notes that mild liver dysfunction may be found incidentally during adolescence, emphasizing the often-subclinical nature of early disease.[2] Vajro et al. describe patients whose liver enzyme elevations were noted in childhood and persisted for decades without major clinical deterioration, suggesting a chronic, indolent course.[3][8]  

Onset pattern is insidious rather than acute; patients do not present with fulminant hepatitis or acute liver failure but rather with chronic hypertransaminasemia discovered during routine medical evaluation or investigation of nonspecific symptoms such as fatigue.[3][7][11][16] Fang et al.’s patient showed abnormal liver function since early childhood, with progression to cirrhosis over time, indicating that while disease is often stable, some individuals may experience slow progression to advanced fibrosis.[11][16]  

### 8.2 Disease Progression and Staging

Formal staging systems have not been developed specifically for TMEM199-CDG, but liver disease progression can be conceptualized in terms of standard hepatic staging: steatosis, steatohepatitis, fibrosis, and cirrhosis. Most reported TMEM199-CDG patients fall within the steatosis and mild fibrosis stages, with no evidence of portal hypertension or liver failure.[3][6][7][16] Vajro et al. explicitly note that their patients’ liver disease was non-progressive over decades, with stable steatosis and hypertransaminasemia.[3][8] Fiumara et al.’s Sicilian patient exhibited periportal fibrosis but a relatively unremarkable liver echo structure on ultrasound and stable hepatopathy, aligning with early-stage disease.[7]  

Fang et al.’s patient, who had cirrhosis on biopsy, represents a more advanced stage, suggesting that TMEM199-CDG can occasionally progress to end-stage liver disease.[11][16] The rate of progression appears slow, and there is no evidence of rapid or episodic exacerbations like those seen in autoimmune hepatitis or viral hepatitis. Disease duration is chronic and lifelong, as there is no cure or spontaneous resolution of the underlying genetic defect, though biochemical abnormalities may remain stable and not necessarily translate into severe clinical symptoms.[3][7][11][16]  

### 8.3 Patterns of Remission and Critical Periods

Remission patterns are not well characterized, as TMEM199-CDG is not typically described in terms of active versus inactive phases. Persistent elevations of liver enzymes and stable steatosis are the norm, with no documented spontaneous remission of biochemical abnormalities.[3][7][11][16] The absence of progression in many cases could be viewed as a stable disease course rather than remission. Treatment-induced changes, such as improvements in transaminases or lipids through lifestyle or medications, have not been systematically reported.  

Critical periods of vulnerability or opportunity for intervention might include childhood and adolescence, when liver disease begins to manifest, and early adulthood, when lifestyle factors such as diet and alcohol use could compound underlying metabolic defects. However, there is no evidence that early treatment alters long-term outcomes in TMEM199-CDG, given the absence of targeted therapies and the generally benign course in most patients.[3][7][11][16]  

## 9. Inheritance and Population

### 9.1 Inheritance Pattern and Genetic Features

TMEM199-CDG is inherited in an **autosomal recessive** manner, as consistently described by Orphanet, OMIM, and all clinical case reports.[1][2][3][7][11][16] Affected individuals carry homozygous or compound heterozygous pathogenic TMEM199 variants, while heterozygous carriers are asymptomatic.[2][3][6][11][16] Orphanet explicitly notes autosomal recessive inheritance and a prevalence of less than 1 per 1,000,000, reflecting its ultra-rare status.[1] OMIM also lists autosomal recessive inheritance for CDG type IIp.[2]  

Penetrance appears to be high for biochemical liver abnormalities in individuals with biallelic TMEM199 loss-of-function, as all reported patients exhibited elevated transaminases and glycosylation defects.[3][6][7][11][16] However, given the small number of cases, incomplete penetrance cannot be entirely excluded, especially for more advanced manifestations such as cirrhosis or neurodevelopmental findings. Expressivity is variable, with some patients showing only mild biochemical changes and steatosis, while others develop fibrosis, cirrhosis, or mild psychomotor delay.[1][3][7][11][16] Genetic anticipation, germline mosaicism, and repeat expansions are not relevant, as TMEM199-CDG is caused by standard loss-of-function variants rather than dynamic mutations.[2][4]  

Consanguinity has not been strongly emphasized in the reported families, though autosomal recessive inheritance suggests that consanguinity could increase disease risk in certain populations. Founder effects are implicated in the southern Mediterranean region, where the c.92G>C (p.Arg31Pro) variant is relatively frequent among TMEM199-CDG cases.[7] Carrier frequency has not been quantified through population datasets, but Fiumara et al.’s estimate that 77% of nine patients carried this variant suggests regional enrichment.[7]  

### 9.2 Epidemiology and Demographics

TMEM199-CDG is extremely rare, with Orphanet estimating a prevalence of less than 1 per 1,000,000.[1] Fiumara et al. note that, up to their report in 2023, only eight individuals with TMEM199-CDG had been documented worldwide, including seven Europeans (from Greece and Italy) and one from China, and they add a ninth patient from southern Italy, specifically Sicily.[7] Fang et al. report the Chinese boy, reinforcing that TMEM199-CDG occurs in non-European populations as well.[11][16] The geographical distribution shows a cluster in the southern Mediterranean area, with several patients from Campania and Sicily in Italy and one from Greece carrying the c.92G>C variant, suggesting a local founder mutation.[7]  

Sex distribution is not clearly skewed; both male and female patients have been reported, though the small numbers preclude meaningful sex ratio analysis.[3][7][11][16] Age distribution among diagnosed individuals ranges from childhood through adolescence and young adulthood, reflecting both age of onset and diagnostic delay.[3][7][11][16] There is no evidence of ethnic or racial predilection beyond the Mediterranean clustering of specific variants, and global prevalence remains extremely low.  

## 10. Diagnostics

### 10.1 Clinical and Laboratory Tests

Diagnosis of TMEM199-CDG relies on integrating clinical suspicion with specialized biochemical and genetic testing. Clinically, the condition should be considered in individuals with unexplained mildly elevated serum aminotransferases, elevated alkaline phosphatase, hepatic steatosis, hypercholesterolemia, and low serum ceruloplasmin, especially when transferrin glycosylation studies reveal a type II CDG pattern.[3][6][7][11][16] Jansen et al. suggest screening for abnormal glycosylation in individuals with these features and emphasize that TMEM199 deficiency should be considered in the differential diagnosis of chronic hypertransaminasemia and steatosis.[6] Vajro et al. reiterate that TMEM199-CDG patients do not show encephalopathy but chronic, non-progressive liver disease, highlighting the importance of biochemical profiling for diagnosis.[3][8]  

Laboratory tests include standard liver function tests (AST, ALT, ALP, GGT), lipid profiles (total cholesterol, LDL, HDL, triglycerides), serum ceruloplasmin and copper levels, and 24-hour urinary copper excretion to exclude Wilson disease.[3][6][7][11][16] A characteristic pattern of low serum ceruloplasmin and copper with normal urinary copper supports TMEM199-CDG over Wilson disease.[3][7][11][16] Transferrin isoelectric focusing (Tf-IEF) is crucial for detecting CDG patterns; TMEM199-CDG shows a type II pattern with combined N- and O-glycosylation defects, suggesting a Golgi-related CDG.[2][3][6][7][11][13][16] MALDI-MS of N- and O-glycoproteins can further characterize glycan abnormalities.[7][13]  

Imaging studies such as liver ultrasound and MRI typically reveal hepatic steatosis and sometimes mild fibrosis but may be unremarkable, as in Fiumara et al.’s Sicilian patient.[7] Liver biopsy provides definitive assessment of steatosis, inflammation, fibrosis, and cirrhosis; it has shown mild, non-progressive fibrosis in some patients and cirrhosis in the Chinese boy.[3][7][11][16] Histopathology often reveals macrovesicular steatosis and periportal fibrosis, while immunohistochemistry for TMEM199 protein can demonstrate reduced expression in hepatocytes.[11][16]  

From a diagnostic ontology standpoint, LOINC codes would correspond to liver enzyme tests, ceruloplasmin assays, copper measurement, and transferrin IEF. NCIT terms for clinical interventions include *“Liver Biopsy”* and *“Genetic Testing”*, which are central to confirmation of TMEM199-CDG.  

### 10.2 Genetic Testing Strategy

Genetic testing is essential for definitive diagnosis of TMEM199-CDG. Approaches may include targeted sequencing of TMEM199, CDG gene panels, whole exome sequencing (WES), or whole genome sequencing (WGS). The Genetic Testing Registry lists “Congenital disorder of glycosylation, type IIp, 616829, Autosomal recessive; CDG2P” as a condition for which testing is available, though details of the test methodology are not provided.[9] Given the rarity and allelic heterogeneity of TMEM199-CDG, WES or comprehensive CDG panels are particularly useful in patients with unexplained glycosylation defects and liver disease.[2][3][6][11][16]  

Single gene testing of TMEM199 may be appropriate in settings where clinical and biochemical features strongly suggest TMEM199-CDG, especially in regions with known founder variants such as c.92G>C in southern Mediterranean populations.[7] WGS could detect noncoding variants or structural changes, but currently, all described pathogenic variants are coding missense or frameshift changes identifiable by WES.[2][3][7][11][16] Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat expansion analysis are not relevant in TMEM199-CDG, as the disease is not associated with chromosomal rearrangements, mitochondrial defects, or repeat expansions.[2][4][11][16]  

### 10.3 Clinical Criteria and Differential Diagnosis

Standardized diagnostic criteria for TMEM199-CDG have not yet been formalized by professional societies, but a practical clinical picture can be derived from published reports: chronic mild elevation of liver enzymes; hepatic steatosis; low serum ceruloplasmin and copper with normal urinary copper; hypercholesterolemia; abnormal transferrin IEF with type II pattern; and biallelic TMEM199 variants.[3][6][7][11][16]  

Differential diagnosis includes several conditions. **Wilson disease** is a key differential due to the low ceruloplasmin and copper; however, Wilson disease features increased urinary copper excretion, neurological manifestations, and Kayser–Fleischer rings, which are absent in TMEM199-CDG.[3][7][11][16] Other CDGs, particularly those affecting Golgi homeostasis such as CCDC115-CDG and COG complex CDGs (e.g., COG1-CDG), can present with glycosylation defects and liver disease but usually have more systemic involvement and neurodevelopmental impairment.[5][6][8][11][16] Orphanet describes COG1-CDG as characterized by microcephaly, growth retardation, psychomotor delay, and facial dysmorphism, distinguishing it from TMEM199-CDG’s liver-predominant phenotype.[5] Non-alcoholic fatty liver disease (NAFLD) is also a consideration, but transferrin glycosylation is normal and TMEM199 mutations absent in NAFLD.[13]  

### 10.4 Screening and Early Detection

There are no established population-based screening programs for TMEM199-CDG, and newborn screening does not currently include TMEM199-CDG or other CDG type II subtypes.[1][2][3][7][11][16] Early detection relies on clinical vigilance in patients with chronic unexplained liver enzyme elevation, steatosis, and low ceruloplasmin, and consideration of glycosylation studies and genetic testing.[6][7][11][16] Carrier screening and cascade testing in families with known TMEM199-CDG may be considered, especially in regions with founder mutations, but guidelines specific to TMEM199-CDG have not been published.  

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

No deaths directly attributable to TMEM199-CDG have been reported in the published case series, and survival appears to be good, with patients living into adulthood with stable liver disease.[3][7][11][16] Vajro et al. explicitly note that two of their three patients were clinically assessed over two decades without deterioration, indicating that life expectancy is likely near normal in many cases, at least when liver disease remains non-progressive.[3][8] There are no data on five- or ten-year survival rates or disease-specific mortality due to the small number of cases and relatively benign course.  

In the case of Fang et al.’s patient with cirrhosis, long-term outcome is less clear, but there is no mention of liver failure or transplantation at the time of reporting.[11][16] Overall, TMEM199-CDG does not appear to be associated with high mortality, although advanced fibrosis could theoretically predispose to complications such as portal hypertension or hepatocellular carcinoma, which have not yet been documented.  

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in TMEM199-CDG is primarily related to chronic liver disease and potential metabolic complications rather than overt disability. Patients may require long-term monitoring of liver function, lipid profiles, and glycosylation status, and may be at increased risk for cardiovascular disease due to hypercholesterolemia, though this has not been systematically studied.[3][6][7][11][13][16] Disability outcomes, in terms of functional impairments, appear minimal; most patients have normal or near-normal daily functioning, with mild psychomotor delay in some cases but no severe intellectual disability or motor impairment.[1][11][16]  

Formal quality-of-life measures have not been reported specifically for TMEM199-CDG, but the non-encephalopathic nature of the disease and absence of severe systemic involvement suggest that quality of life is only modestly impacted, primarily by the need for medical follow-up and potential anxiety about liver disease.[3][8][11][16] The favorable long-term course described by Vajro et al. is crucial information for patients and families at diagnosis, as it distinguishes TMEM199-CDG from other Golgi homeostasis disorders with more severe outcomes.[3][8]  

### 11.3 Disease Course and Prognostic Factors

Disease course in TMEM199-CDG is generally stable or very slowly progressive for hepatic manifestations, with chronic steatosis and mild fibrosis in most patients and cirrhosis in rare cases.[3][7][11][16] Complications such as liver failure, hepatic encephalopathy, or severe neurological deficits have not been reported, suggesting that prognostic outlook is favorable in most individuals.[3][6][8][11][16]  

Potential prognostic factors may include the specific TMEM199 variants (e.g., hypomorphic versus null alleles), coexisting liver or metabolic conditions, and environmental exposures such as diet and alcohol, but these have not been systematically studied. The presence of cirrhosis in Fang et al.’s patient may indicate a more severe variant or longer duration of disease, but detailed genotype–phenotype correlation is lacking.[11][16] Hypercholesterolemia could serve as a biomarker of more pronounced lipid handling defects and might predict cardiovascular risk, though evidence is limited.[6][13]  

## 12. Treatment

### 12.1 Pharmacotherapy and Supportive Management

There is currently **no disease-specific pharmacotherapy** targeting the underlying TMEM199 defect or directly correcting Golgi pH and glycosylation in TMEM199-CDG. Treatment is therefore supportive and focused on managing liver disease and metabolic complications.[3][6][7][11][16] Patients may receive standard care for non-alcoholic fatty liver disease, including lifestyle interventions such as weight management, dietary modification, and exercise, though these approaches have not been evaluated specifically in TMEM199-CDG.[13] Lipid-lowering medications (e.g., statins) might be considered for hypercholesterolemia, but there are no published data on their use or efficacy in TMEM199-CDG patients.[6][7][11][13][16]  

Given the resemblance of TMEM199-CDG biochemical profiles to Wilson disease, it is critical to avoid misdiagnosis and inappropriate copper-chelating therapy in TMEM199-CDG patients, as they do not have copper overload but rather normal urinary copper and low ceruloplasmin.[3][7][11][16] NCIT clinical intervention terms applicable here include *“Dietary Therapy”*, *“Lipid-Lowering Agent Administration”*, and *“Liver Disease Management.”*  

### 12.2 Advanced Therapeutics and Experimental Approaches

No gene therapy, cell therapy, or targeted molecular therapy has yet been developed or tested for TMEM199-CDG. The rarity of the disease and the complexity of its pathophysiology pose challenges for therapeutic development. However, TMEM199’s role as a V-ATPase assembly factor and its involvement in autophagy and lipophagy suggest conceptual targets: modulation of autophagy, enhancement of lysosomal function, or correction of organelle pH might ameliorate some downstream effects.[10][13]  

RNA-based therapies such as antisense oligonucleotides or mRNA replacement have not been explored in TMEM199-CDG, but in principle, gene replacement therapy via AAV-mediated delivery of functional TMEM199 to hepatocytes could be envisioned, similar to emerging gene therapies for other monogenic liver diseases. No clinical trials (e.g., NCT identifiers) were identified in the available search results for TMEM199-CDG, indicating that treatment remains at a conceptual stage.[1][2][3][7][11][13][16]  

### 12.3 Surgical and Interventional Therapies

Liver transplantation has not been reported for TMEM199-CDG. Given the generally benign course and non-progressive nature of liver disease in most cases, transplantation would not usually be indicated, except potentially in rare individuals with advanced cirrhosis and liver failure.[3][7][11][16] Surgical interventions specific to TMEM199-CDG are not described; standard hepatic interventions such as biopsy are used for diagnosis rather than treatment.  

### 12.4 Treatment Outcomes and Personalized Medicine

Because no targeted treatments exist, treatment outcomes focus on stability of liver disease and avoidance of complications. Vajro et al.’s long-term follow-up suggests that supportive management and watchful waiting can be compatible with stable health over decades.[3][8] Personalized medicine approaches may eventually be possible by tailoring treatments to specific TMEM199 variants or to individual autophagy and lipid metabolism profiles, but current evidence does not support specific genotype-guided therapies.  

Pharmacogenomics has not been studied in TMEM199-CDG; however, clinicians should be aware of potential hepatotoxicity of certain drugs (e.g., some statins, antiepileptics) and monitor liver function accordingly, as TMEM199-CDG patients may be more vulnerable to additional insults.  

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of TMEM199-CDG, in the sense of preventing disease occurrence, would rely on preventing conception of affected individuals via carrier screening, preimplantation genetic diagnosis (PGD), or prenatal testing in families known to carry pathogenic TMEM199 variants.[2][7][11][16] There are no population-based initiatives for TMEM199-CDG due to its extreme rarity, but targeted carrier screening could be considered in high-risk populations such as families from southern Italy and Greece with a history of TMEM199-CDG or known c.92G>C carriers.[7]  

Secondary prevention focuses on early detection and intervention to prevent progression of liver disease. This may include regular monitoring of liver enzymes, ultrasound for fibrosis and steatosis, and lifestyle counseling to minimize additional hepatic risks (e.g., obesity, alcohol).[3][7][11][16] Screening for abnormal transferrin glycosylation in patients with unexplained chronic hypertransaminasemia and low ceruloplasmin, as suggested by Jansen et al., can facilitate early diagnosis.[6]  

Tertiary prevention aims to prevent complications in patients with established TMEM199-CDG, such as progression to cirrhosis or cardiovascular disease due to hypercholesterolemia. This involves careful management of lipid levels, monitoring for fibrosis progression, and standard supportive care for chronic liver disease.[7][11][13][16]  

### 13.2 Genetic Counseling and Risk Stratification

Genetic counseling is an important component of prevention and family planning in TMEM199-CDG. Counselors should explain autosomal recessive inheritance, carrier risks, and options for prenatal or preimplantation testing.[1][2][7][11][16] In families with known TMEM199-CDG, cascade testing of siblings and extended family members can identify carriers and inform reproductive decisions. Risk stratification in a broader public health context is limited by the rarity of TMEM199-CDG, but in specific populations with founder variants, such as southern Mediterranean communities, awareness and targeted counseling may be beneficial.[7]  

Behavioral interventions, such as promoting healthy diet and avoidance of excessive alcohol intake, are relevant to general liver health but do not specifically prevent TMEM199-CDG, as the genetic defect is inborn.[3][7][11][13][16]  

## 14. Other Species and Natural Disease

### 14.1 Orthologous Genes and Comparative Biology

Orthologous genes to TMEM199 exist in multiple species, reflecting the conserved role of V-ATPase assembly factors. In yeast, the ortholog is **VMA12**, encoding a vacuolar ATPase assembly factor that supports assembly of the vacuolar proton-transporting V-type ATPase complex.[12] In zebrafish, the gene vma12 (also previously named tmem199) is identified in ZFIN as a vacuolar ATPase assembly factor located in the endoplasmic reticulum membrane and active in the endomembrane system; human TMEM199 is recognized as its ortholog.[14] Echinobase lists tmem199 across several echinoderm species (e.g., Strongylocentrotus purpuratus, Pisaster miniata) as a conserved gene, highlighting evolutionary conservation in marine organisms.[15]  

These orthologs suggest that species ranging from yeast to fish and mammals share TMEM199/VMA12-mediated V-ATPase assembly mechanisms, which implies that TMEM199-related disease mechanisms might be studied in diverse model organisms, even if natural disease has not been described outside humans.[10][12][14][15] GO family IPR021013, “ATPase, vacuolar ER assembly factor, Vma12,” encompasses these orthologs.[14]  

### 14.2 Natural Disease in Animals and Zoonotic Potential

No naturally occurring TMEM199-CDG-like disease has been reported in companion animals, livestock, or wildlife, and OMIA or veterinary databases have not yet described analogous conditions linked to TMEM199 or VMA12 mutations.[14][15] The disease is not infectious and has no zoonotic potential; it is strictly a human Mendelian inborn error of metabolism.[1][2][3][6][11][16] Comparative pathology across species therefore focuses on experimental models rather than naturally occurring animal disease.  

## 15. Model Organisms

### 15.1 Mouse Models

Larsen et al. developed a mouse model of TMEM199 deficiency using CRISPR/Cas9-mediated knock-in of the human Ala7Glu mutation into the Tmem199 gene.[13] Full TMEM199 knockout proved embryonic lethal, as no viable homozygous knockout pups were recovered, indicating that complete loss of TMEM199 function is incompatible with embryonic development in mice.[13] Homozygous Tmem199-Ala7Glu mice, however, showed normal embryonic viability with Mendelian genotype distribution and no obvious gross abnormalities or neuromotor disabilities, paralleling the absence of severe neurological manifestations in human TMEM199-CDG.[13]  

These mice exhibited marked hepatic steatosis on a chow diet, with hepatic triglyceride levels approximately 80% higher than in controls, and plasma N-glycans showed hypogalactosylation, consistent with patient phenotypes.[13] Western analysis revealed virtually no TMEM199 protein in mouse livers, confirming the hypomorphic nature of the Ala7Glu mutation.[13] Despite the glycosylation and hepatic lipid abnormalities, plasma lipid profiles were not significantly altered, underscoring species differences and highlighting the limitations of the model in recapitulating human hypercholesterolemia.[13]  

From a phenotypic recapitulation standpoint, the mouse model successfully reproduces key features of TMEM199-CDG: TMEM199 protein deficiency, glycosylation defects, hepatic steatosis, and lysosomal dysfunction. It does not, however, fully capture human plasma hyperlipidemia, nor does it model human histological fibrosis or cirrhosis.[13] Applications of this model include studying lipophagy, lysosomal function, autophagy pathways, and potential therapeutic interventions aimed at restoring organelle acidification or autophagic flux.[13]  

### 15.2 Cellular Models

Cellular models include TMEM199 knockout HeLa cells used by Miles et al. to investigate V-ATPase assembly and HIF1α regulation.[10] These cells, in which TMEM199 was genetically disrupted, showed impaired acidification of endosomes, intracellular iron depletion, and HIF1α stabilization in normoxia, establishing TMEM199’s role in V-ATPase function and linking it to hypoxia signaling.[10] HepG2 hepatocyte models with siRNA-mediated TMEM199 knockdown, as used by Larsen et al., exhibited increased numbers and sizes of lipid droplets, lysosomal lipid accumulation, and impaired autophagic capacity, mirroring key aspects of TMEM199-CDG’s hepatic phenotype.[13]  

These in vitro models allow detailed dissection of cell-type specific mechanisms and are valuable for high-throughput screening of potential modulators of autophagy, lysosomal function, or glycosylation. They also demonstrate that TMEM199 deficiency alone, without systemic factors, can produce organelle dysfunctions central to the disease.  

### 15.3 Other Model Organisms

Zebrafish and echinoderm models have not yet been reported for TMEM199 deficiency, but given the presence of orthologous genes such as vma12 and tmem199 in these organisms, future work could leverage them to study developmental roles or tissue-specific functions of TMEM199/VMA12.[14][15] Yeast models involving VMA12 and VMA22 have long been used to understand V-ATPase assembly and function, and these foundational studies inform the mechanistic interpretation of TMEM199 in humans.[10][12]  

Model organism databases such as ZFIN, Echinobase, and yeast genetic repositories document TMEM199 orthologs and could support future comparative studies, but to date, TMEM199-CDG research relies mainly on mouse and human cell models.  

## Conclusion

TMEM199-CDG, or congenital disorder of glycosylation type IIp (CDG2P), represents a paradigmatic example of a Golgi homeostasis disorder caused by disruption of organelle acidification machinery rather than direct glycosyltransferase defects.[1][2][3][6][13][16] Biallelic pathogenic variants in TMEM199, a transmembrane ER-localized V-ATPase assembly factor homologous to yeast Vma12p, lead to impaired assembly and function of the vacuolar H\(^+\)-ATPase, resulting in reduced acidification of Golgi and endo-lysosomal compartments.[2][4][6][10][13] This organelle pH disturbance disrupts the activity and localization of glycosylation enzymes, producing combined N- and O-glycosylation defects, and impairs lysosomal autophagic processes, particularly lipophagy, which drives hepatic steatosis and altered lipid droplet–lysosome interactions.[6][10][13]  

Clinically, TMEM199-CDG is characterized by chronic, mild elevation of liver enzymes, hepatic steatosis, mild fibrosis or periportal fibrosis, hypercholesterolemia, low serum ceruloplasmin and copper with normal urinary copper, and a type II transferrin isoelectric focusing pattern indicative of abnormal glycosylation.[1][2][3][6][7][11][16] Most patients are asymptomatic or minimally symptomatic, with non-encephalopathic liver-predominant disease and a relatively benign, non-progressive course over decades, although rare cases such as the Chinese boy reported by Fang et al. exhibit cirrhosis and mild psychomotor delay.[3][8][11][16] The disease’s biochemical resemblance to Wilson disease underscores the importance of careful differential diagnosis and avoidance of inappropriate chelation therapy, while its glycosylation profile and genetic basis align it with other CDGs.[3][6][7][11][16]  

From a genetic and population perspective, TMEM199-CDG is an ultra-rare autosomal recessive disorder, with fewer than ten patients reported worldwide and a notable clustering of the c.92G>C (p.Arg31Pro) variant in southern Mediterranean populations, where a founder effect is suspected.[1][2][3][7][11][16] Pathogenic variants include early truncating frameshifts and missense changes near the N-terminus that destabilize the protein, and functional studies confirm that TMEM199 deficiency leads to generalized defects in Golgi processing of protein-linked glycans, which are rescued by wild-type TMEM199.[2][3][6][11][13][16]  

Mechanistic work in mouse and cell models reveals that TMEM199 deficiency impairs organelle acidification, autophagic flux, and lipid catabolism, resulting in hepatic triglyceride accumulation, hypogalactosylated plasma N-glycans, and lysosomal lipid accumulation without excessive de novo lipogenesis or failing oxidative capacity.[10][13] These findings highlight lipophagy and lysosomal function as key downstream processes and suggest potential therapeutic targets, though no disease-specific treatments currently exist.[13]  

Diagnostic strategies hinge on recognizing the characteristic constellation of chronic hypertransaminasemia, steatosis, low ceruloplasmin, and abnormal transferrin glycosylation, followed by genetic confirmation of biallelic TMEM199 variants.[3][6][7][9][11][16] While screening programs do not exist, clinicians are encouraged to consider TMEM199-CDG in patients with unexplained liver disease and glycosylation defects, especially in regions with known founder mutations.[6][7][11][16]  

Prognosis is generally favorable, with most patients demonstrating stable liver disease and good quality of life, though careful monitoring is warranted to detect fibrosis progression or metabolic complications such as cardiovascular risk from hypercholesterolemia.[3][7][11][16] Research applications of TMEM199-CDG extend beyond this rare disease, providing insights into V-ATPase assembly, organelle pH regulation, autophagy, and lipophagy in liver physiology and pathology.[10][13] As more cases are identified and mechanistic studies expand, TMEM199-CDG will likely continue to inform broader understanding of glycosylation disorders and metabolic liver disease, and may eventually yield to targeted therapies aimed at correcting organelle homeostasis and glycosylation.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 28 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012159` (2 mentions) - the report calls it "Abnormal transferrin glycosylation"; HP calls it **Internal carotid artery dissection**
- `HP:0003119` (1 mention) - the report calls it "Elevated serum cholesterol"; HP calls it **Abnormal circulating lipid concentration**
- `GO:0030148` (1 mention) - the report calls it "regulation of organelle pH"; GO calls it **sphingolipid biosynthetic process**
- `CL:0002078` (2 mentions) - the report calls it "hepatic stellate cell"; CL calls it **meso-epithelial cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002910` (2 mentions) - the report calls it "Elevated serum aminotransferase level"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Elevated serum transaminases" among its other names
- `HP:0003155` (1 mention) - the report calls it "Elevated alkaline phosphatase of hepatic origin"; HP calls it **Elevated circulating alkaline phosphatase concentration**, and lists "Elevated alkaline phosphatase" among its other names
- `HP:0001395` (1 mention) - the report calls it "Fibrosis of liver"; HP calls it **Hepatic fibrosis**, and lists "Liver fibrosis" among its other names
- `HP:0012308` (2 mentions) - the report calls it "Reduced serum ceruloplasmin", "Decreased serum ceruloplasmin"; HP calls it **Decreased circulating complement C9 concentration**, and lists "Decreased serum complement C9" among its other names
- `HP:0011343` (1 mention) - the report calls it "Mild global developmental delay"; HP calls it **Moderate global developmental delay**
- `HP:0002902` (1 mention) - the report calls it "Decreased serum copper"; HP calls it **Hyponatremia**, and lists "Decreased sodium(1+) concentration" among its other names
- `CL:0000731` (1 mention) - the report calls it "Kupffer cell"; CL calls it **urothelial cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0012308` - called "Reduced serum ceruloplasmin", "Decreased serum ceruloplasmin"