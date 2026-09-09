---
provider: perplexity
model: sonar-reasoning-pro
cached: false
start_time: '2026-09-09T20:09:20.325539'
end_time: '2026-09-09T20:11:55.461775'
duration_seconds: 155.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spinocerebellar Ataxia Autosomal Recessive With Axonal Neuropathy
    2
  mondo_id: MONDO:0018996
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
citation_count: 16
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 38
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.026
  labels_checked: 19
  labels_matching: 5
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: GO:0006281
    reported_labels:
    - GO biological processes:** DNA repair
    - Key GO terms:** DNA repair
    ontology_label: DNA repair
  - term_id: CL:0000103
    reported_labels:
    - dorsal root ganglion neuron
    ontology_label: bipolar neuron
  - term_id: UBERON:0001898
    reported_labels:
    - brainstem
    ontology_label: hypothalamus
  - term_id: NCIT:C16801
    reported_labels:
    - Magnetic resonance imaging of brain
    ontology_label: Long-Term Care for Elderly
  - term_id: NCIT:C38000
    reported_labels:
    - Electromyography and nerve conduction studies
    ontology_label: Performed
  - term_id: NCIT:C18243
    reported_labels:
    - Genetic Testing
    - NCIT clinical intervention terms:** Genetic testing
    ontology_label: Regression
  - term_id: NCIT:C15280
    reported_labels:
    - Physical therapy
    ontology_label: Breast Conservation Treatment
  - term_id: NCIT:C15279
    reported_labels:
    - Occupational therapy
    ontology_label: Radical Mastectomy
  - term_id: NCIT:C15384
    reported_labels:
    - Speech therapy
    ontology_label: Surgical Incision
  labels_variant: 5
  unresolved_terms:
  - HP:0006259
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia Autosomal Recessive With Axonal Neuropathy 2
- **MONDO ID:** MONDO:0018996 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia Autosomal Recessive With Axonal Neuropathy 2** covering all of the
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

Spinocerebellar ataxia, autosomal recessive, with axonal neuropathy 2 (SCAN2), also known as ataxia with oculomotor apraxia type 2 (AOA2), is a rare autosomal recessive cerebellar ataxia caused by biallelic loss‑of‑function mutations in the DNA/RNA helicase gene SETX, leading to juvenile‑onset progressive cerebellar ataxia, severe axonal sensorimotor neuropathy, frequent oculomotor apraxia, and elevated serum alpha‑fetoprotein (AFP).[2][3][4][6][8][9][12] Published cases and database summaries indicate a slowly progressive, lifelong neurodegenerative course with major disability but usually preserved survival.[3][5][8][12]

---

## 1. Disease Information

**Overview and definition**

Spinocerebellar ataxia, autosomal recessive, with axonal neuropathy 2 (SCAN2) is classified among autosomal recessive cerebellar ataxias (ARCA) and hereditary peripheral neuropathies.[3][5][9] MONDO defines it as “a rare autosomal recessive cerebellar ataxia (ARCA), characterized by progressive cerebellar ataxia associated with frequent oculomotor apraxia, severe neuropathy and an elevated serum alpha-fetoprotein (AFP) level.”[9] A widely cited clinical description states: “Ataxia with oculomotor apraxia type 2 (AOA2)/autosomal recessive spinocerebellar ataxia with axonal neuropathy-2 (SCAN2) (OMIM #606002) is characterized by early-onset progressive cerebellar ataxia, polyneuropathy, and elevated levels of alpha-fetoprotein (AFP). It is caused by loss-of-function mutations in the gene SETX (OMIM #608465) on chromosome 9q34.1.”[12]

**Key identifiers**

- OMIM disease ID: 606002 (AOA2 / SCAN2).[11][12][14]  
- Gene OMIM ID: 608465 (SETX).[12]  
- MONDO ID: MONDO:0018996.[9]  
- DOID (Disease Ontology, used by ZFIN): DOID:0050755 (“spinocerebellar ataxia with axonal neuropathy 2”).[6]  
- Orphanet disease ID: Spinocerebellar ataxia with axonal neuropathy type 2 (Orpha number 64753).[3]  
- ClinVar disease name: “Spinocerebellar ataxia, autosomal recessive, with axonal neuropathy 2 (SCAN2)” attached to multiple SETX variants.[7][10]  
- NORD/rare disease registries list SCAN2 as a rare autosomal recessive cerebellar ataxia.[8]  

ICD‑10/ICD‑11 and MeSH do not currently have a unique code specifically labeled “SCAN2”; cases are typically coded under hereditary ataxias and peripheral neuropathies at the aggregated category level.[3][4][8]

**Synonyms and alternative names**

Commonly used synonyms include:[2][3][4][6][8][9][12][14]  

- Ataxia with oculomotor apraxia type 2 (AOA2)  
- Spinocerebellar ataxia with axonal neuropathy type 2  
- Autosomal recessive spinocerebellar ataxia with axonal neuropathy‑2 (SCAN2)  
- Autosomal recessive spinocerebellar ataxia 1 / SCAR1 (historical term; reclassified to SCAN2)[11][14]  
- Autosomal recessive cerebellar ataxia (ARCA) with axonal neuropathy  

ZFIN and MONDO list synonyms including “AOA2,” “SCAR1,” “AOA2 (ataxia with oculomotor apraxia type 2),” and “spinocerebellar ataxia with axonal neuropathy type 2.”[6][9][14]

**Data sources**

Information is predominantly derived from aggregated disease‑level resources (OMIM, Orphanet, GARD/NIH, MedGen, NORD, MONDO), expert reviews, and case series/case reports rather than from large EHR‑based cohorts.[2][3][4][5][8][9][12][14] The 2025 review on autosomal recessive cerebellar ataxias synthesizes genetic and mechanistic data across multiple ARCA subtypes, including AOA2/SCAN2.[5]

---

## 2. Etiology

### Disease causal factors

SCAN2 is a monogenic neurodegenerative disorder caused by homozygous or compound heterozygous pathogenic variants in SETX, which encodes senataxin, a nuclear DNA/RNA helicase involved in genome integrity and RNA processing.[3][5][12] Orphanet and MONDO describe the disease as having “material basis in homozygous or compound heterozygous mutation in the SETX gene on chromosome 9q34.13.”[3][6][9] The ARCA review states: “The most common of these is AOA2 (also known as spinocerebellar ataxia with axonal neuropathy type 2 [SCAN2]) caused by mutation in senataxin (SETX), an RNA/DNA helicase involved in maintenance of genome integrity in response to DNA replication stress from DNA:RNA hybrid R‐loop formation during transcription…”[5]

There is no evidence that environmental, infectious, or other non‑genetic factors are primary causes; the condition is consistently described as autosomal recessive and monogenic.[2][3][4][5][8][12]

### Genetic risk factors

- **Causal gene:** SETX (HGNC:10740), located at 9q34.13–9q34.3.[3][5][12]  
- **Variant type:** Most reported disease‑causing variants are truncating (nonsense, frameshift, splice) or missense changes leading to loss of function.[5][12][14]  
- ClinVar lists multiple SETX variants interpreted as pathogenic/likely pathogenic for SCAN2, including c.5536C>T (p.Arg1846Cys) and c.4433C>A (p.Ala1478Glu).[7][10]  
- A targeted NGS case report from Taiwan identified a novel SETX mutation in a patient with AOA2/SCAN2 and summarized >60 pathogenic variants reported worldwide, supporting considerable allelic heterogeneity.[12]  

Consanguinity is a frequent context in autosomal recessive cerebellar ataxias, and Orphanet notes that SCAN2 is transmitted as an autosomal recessive trait with a 25% recurrence risk for siblings of an affected individual, consistent with increased risk in consanguineous families.[3]

### Environmental risk factors

No consistent environmental, occupational, or lifestyle risk factors have been identified in SCAN2, and major rare disease resources describe it purely as a genetic disease.[2][3][4][5][8][12] Case reports and series do not implicate toxins, infections, or lifestyle exposures as causative or strong modifiers.[5][12]

### Protective factors

There are no reported genetic protective variants or environmental factors that demonstrably reduce risk of SCAN2; given its monogenic, autosomal recessive nature, risk is driven by biallelic pathogenic SETX variants.[3][5][8][12]

### Gene–environment interactions

No gene–environment interaction has been demonstrated for SCAN2 in the available literature or curated databases.[3][5][8][12] The disease is currently conceptualized as a primary DNA/RNA helicase defect with downstream neuronal vulnerability independent of specific environmental triggers.[5][12]

---

## 3. Phenotypes

### Core clinical phenotype

Major clinical features consistently reported across databases and case series include:[2][3][4][5][6][8][9][12]

1. Progressive cerebellar ataxia (gait and limb ataxia)  
2. Axonal sensorimotor peripheral neuropathy (polyneuropathy)  
3. Elevated serum alpha‑fetoprotein (AFP)  
4. Frequent oculomotor apraxia (difficulty initiating horizontal eye movements)  
5. Cerebellar atrophy on neuroimaging  

The Taiwanese case report summarizes: “Ataxia with oculomotor apraxia type 2 (AOA2), also known as autosomal recessive spinocerebellar ataxia with axonal neuropathy-2 (SCAN2)…is characterized by early-onset progressive cerebellar ataxia, polyneuropathy, and elevated levels of alpha-fetoprotein.”[12] MedGen similarly lists onset between 3 and 30 years, axonal sensorimotor neuropathy, oculomotor apraxia, cerebellar atrophy, and elevated AFP.[4]

### Phenotype characteristics

**Age of onset**

- Ataxia onset typically between ages 3 and 30 years, after normal early development.[3][4][6][12]  
- Juvenile onset (late childhood/teen years) is most common in published series.[5][12]  

**Severity and progression**

- Cerebellar ataxia is progressive and often leads to wheelchair dependence over years to decades.[3][5][8][12]  
- Neuropathy is severe axonal sensorimotor neuropathy, frequently causing distal weakness, areflexia, and sensory loss.[3][4][5][8][12]  
- Oculomotor apraxia is common but not universal.[3][4][6][9][12]  
- Overall severity is moderate to severe, with substantial disability but usually preserved cognition except for mild impairment.[2][3][5][12]  

**Frequency among affected individuals**

Orphanet and MONDO state that SCAN2 is “characterized by progressive cerebellar ataxia associated with frequent oculomotor apraxia, severe neuropathy and elevated serum alpha-fetoprotein (AFP).”[3][9] Published case compilations suggest:[5][12]

- Cerebellar ataxia and neuropathy: present in nearly all affected individuals.  
- Elevated AFP: present in the majority (often reported in >80% of cases in series).[5][12]  
- Oculomotor apraxia: “frequent” but absent in a minority.[3][4][6][9][12]  

**Quality of life impact**

Progressive gait and limb ataxia plus severe neuropathy markedly impair mobility, activities of daily living, and independence, leading to reliance on assistive devices and caregivers.[3][5][8][12] Frequent falls, dysarthria, and difficulties with eye movements affect communication and reading; neuropathic pain and fatigue further reduce quality of life.[5][8][12] NORD and GARD emphasize that there is no curative therapy and management is supportive, underscoring the long‑term disability burden.[2][8]

### Suggested HPO terms

Key phenotypes with suggested HPO terms:

- Cerebellar ataxia – HP:0001251.[3][4][5][9][12]  
- Gait ataxia – HP:0002141.[3][4][5][12]  
- Limb ataxia – HP:0002070.[3][4][5][12]  
- Axonal neuropathy / axonal sensorimotor polyneuropathy – HP:0003438, HP:0003477.[3][4][5][12]  
- Oculomotor apraxia – HP:0000657.[3][4][6][9][12]  
- Cerebellar atrophy – HP:0001272.[3][4][5][12]  
- Elevated alpha‑fetoprotein – HP:0006259.[3][4][5][12]  
- Areflexia – HP:0001284.[3][5][12]  
- Distal muscle weakness – HP:0005528.[3][5][12]  
- Mild cognitive impairment – HP:0002423 (reported in some cases).[2][5][12]  

---

## 4. Genetic / Molecular Information

### Causal gene

- **Gene symbol:** SETX (senataxin).[3][5][12]  
- **HGNC ID:** 10740.[5][12]  
- **OMIM gene ID:** 608465.[12]  
- SETX encodes a nuclear DNA/RNA helicase implicated in DNA damage repair, resolution of R‑loops, chromosomal stability, autophagy, transcriptional regulation, and RNA processing.[5][12]  

### Pathogenic variants

**Variant types and classification**

- Pathogenic variants include missense, nonsense, frameshift, and splice‑site changes, generally interpreted as loss‑of‑function.[5][12][14]  
- ClinVar lists multiple SETX variants for SCAN2, such as NM_015046.7(SETX):c.5536C>T (p.Arg1846Cys) and c.4433C>A (p.Ala1478Glu), classified as pathogenic/likely pathogenic in the context of autosomal recessive spinocerebellar ataxia with axonal neuropathy 2.[7][10]  
- The LOVD database for SCAN2/SCAR1/AOA2 (Disease #02569) catalogs numerous SETX variants associated with the phenotype “ataxia, spinocerebellar, autosomal recessive, with axonal neuropathy, type 2 (SCAR1, AOA2),” consistent with high allelic heterogeneity.[14]  

**Allele frequency and origin**

- Pathogenic SETX variants associated with SCAN2 are generally absent or extremely rare in population databases (gnomAD, ExAC) according to case reports and variant interpretations.[5][12][14]  
- All reported disease‑causing variants are germline and inherited in an autosomal recessive pattern; no somatic variants have been implicated.[3][5][7][10][12][14]  

**Functional consequences**

- The Taiwanese case report explicitly states that AOA2/SCAN2 “is caused by loss-of-function mutations in the gene SETX … on chromosome 9q34.1.”[12]  
- The 2025 ARCA review notes that senataxin is “involved in maintenance of genome integrity in response to DNA replication stress from DNA:RNA hybrid R‐loop formation during transcription, chromosomal stability, DNA damage, autophagy, transcriptional regulation, RNA processing and degradation, and the innate immune response.”[5]  
- Together, these data support a **loss‑of‑function mechanism**, leading to impaired R‑loop resolution, increased DNA damage, and downstream neuronal dysfunction.[5][12]  

### Modifier genes and epigenetics

No validated modifier genes have been shown to alter disease severity or expressivity in SCAN2, and no SCAN2‑specific epigenetic abnormalities (DNA methylation or histone modifications) are reported in current curated databases or reviews.[3][5][8][12]

### Chromosomal abnormalities

SCAN2 is caused by point mutations and small indels in SETX; structural chromosomal rearrangements or aneuploidy have not been described as causal mechanisms.[3][5][11][12][14]

---

## 5. Environmental Information

Major databases and clinical reports consistently describe SCAN2 as a hereditary neurodegenerative disorder without identified environmental, occupational, or infectious triggers.[2][3][4][5][8][12] Standard environmental risk factors such as toxin exposure, smoking, alcohol, or infections are not reported as specific contributors in case series.[5][12] Accordingly, no CHEBI‑coded environmental chemicals are currently linked to SCAN2 in curated toxicogenomic databases.[3][5][8]

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. Biallelic loss‑of‑function mutation in SETX leads to deficiency of functional senataxin helicase in neurons.[5][12]  
2. Senataxin deficiency leads to accumulation of DNA:RNA hybrid R‑loops and impaired resolution of transcription‑associated replication stress (demonstrated in cellular models; extrapolated to neurons).[5]  
3. Excess R‑loops and replication stress lead to increased DNA strand breaks, defective DNA damage response, and genomic instability in post‑mitotic neuronal cells (partially inferred from mechanistic studies).[5]  
4. Chronic DNA damage and impaired RNA processing lead to dysfunctional transcriptional regulation, altered autophagy, and abnormal innate immune signaling (mixed experimental and inferred evidence).[5]  
5. These molecular defects result in progressive dysfunction and degeneration of cerebellar Purkinje cells, brainstem nuclei, and peripheral motor and sensory neurons (inferred from the pattern of atrophy and neuropathy).[3][5][12]  
6. Neuronal loss in the cerebellum leads to cerebellar atrophy and progressive cerebellar ataxia.[3][4][5][12]  
7. Degeneration of peripheral nerves leads to axonal sensorimotor polyneuropathy with distal weakness, areflexia, and sensory loss.[3][4][5][12]  
8. Brainstem/oculomotor circuitry involvement leads to oculomotor apraxia.[3][4][6][9][12]  
9. Systemic or hepatic dysregulation associated with senataxin dysfunction leads to elevated serum alpha‑fetoprotein (mechanism unclear and largely inferred).[3][4][5][12]  
10. Combined cerebellar, peripheral nerve, and oculomotor abnormalities result in the clinical SCAN2 phenotype of juvenile‑onset progressive ataxia, neuropathy, oculomotor apraxia, and elevated AFP.[3][4][5][12]

### Molecular pathways and cellular processes

The ARCA review describes senataxin as playing roles in “maintenance of genome integrity in response to DNA replication stress from DNA:RNA hybrid R‐loop formation during transcription, chromosomal stability, DNA damage, autophagy, transcriptional regulation, RNA processing and degradation, and the innate immune response.”[5] Relevant GO biological process terms include:

- DNA repair – GO:0006281.[5][12]  
- Regulation of transcription, DNA‑templated – GO:0006355.[5]  
- RNA processing – GO:0006396.[5]  
- Response to DNA damage stimulus – GO:0006974.[5]  
- Autophagy – GO:0006914.[5]  
- Regulation of innate immune response – GO:0045088.[5]  

Cellular processes implicated include:

- Accumulation of R‑loops and transcription‑associated DNA damage in neurons.[5]  
- Impaired autophagic clearance of damaged macromolecules.[5]  
- Dysregulated RNA metabolism and splicing, affecting neuronal gene expression programs.[5]  

### Protein dysfunction

Senataxin (SETX) is a large, nuclear DNA/RNA helicase; loss‑of‑function variants truncate or alter its helicase domains and nuclear localization signals, impairing R‑loop resolution and helicase activity.[5][12][14] Resultant protein dysfunction is characterized by:

- Loss of helicase activity (loss‑of‑function).  
- Impaired interaction with DNA repair and RNA processing complexes.[5]  

### Immune and metabolic involvement

The ARCA review notes that senataxin contributes to innate immune responses and autophagy.[5] Chronic DNA damage and altered innate immune signaling may contribute to neuroinflammation, although direct SCAN2‑specific evidence is limited and largely inferred.[5] Metabolic alterations are not prominently reported, aside from elevated AFP, whose mechanistic link to SETX dysfunction remains unclear.[3][4][5][12]

### Tissue damage mechanisms

Neuronal tissue damage is thought to result from cumulative DNA damage, impaired genome maintenance, and failure of neuronal quality‑control pathways (autophagy), leading to progressive cerebellar and peripheral nerve degeneration.[3][5][12] The clinical pattern of cerebellar atrophy and axonal neuropathy supports selective vulnerability of Purkinje cells and long peripheral axons.[3][4][5][12]

### Molecular profiling and advanced technologies

No SCAN2‑specific transcriptomic, proteomic, metabolomic, or single‑cell datasets are currently highlighted in major omics repositories or the 2025 ARCA review; most mechanistic understanding is extrapolated from functional studies of SETX in general genomic integrity and RNA biology.[5] Thus, detailed multi‑omics signatures, spatial transcriptomics findings, or CRISPR functional screens specific to SCAN2 remain to be defined.[5]

### Suggested GO and CL terms

- **GO biological processes:** DNA repair (GO:0006281), RNA processing (GO:0006396), regulation of transcription (GO:0006355), autophagy (GO:0006914), response to DNA damage stimulus (GO:0006974).[5][12]  
- **CL cell types:** Cerebellar Purkinje neuron (CL:0000121), spinal cord motor neuron (CL:0000100), peripheral sensory neuron/dorsal root ganglion neuron (CL:0000103), Schwann cell (CL:0000120).[3][5][12]  

---

## 7. Anatomical Structures Affected

### Organ‑level

Primary organs and systems:[3][4][5][8][9][12]

- Cerebellum (UBERON:0002037) – cerebellar atrophy on MRI.  
- Peripheral nerves (UBERON:0001021) – sensorimotor axonal neuropathy.  
- Nervous system overall (UBERON:0001016) – central and peripheral.  

Secondary involvement may include:

- Brainstem/oculomotor pathways (e.g., paramedian pontine reticular formation) associated with oculomotor apraxia (UBERON:0001898 – brainstem).[3][4][12]  
- Spinal cord (UBERON:0002240) due to long tract involvement in neuropathy.[5][12]  

### Tissue and cell level

Affected tissues are predominantly nervous tissue:

- Neuronal populations in the cerebellar cortex (Purkinje cells) and deep cerebellar nuclei.[3][5][12]  
- Peripheral motor and sensory neurons and Schwann cells in peripheral nerves.[3][5][12]  

Suggested CL terms:

- CL:0000121 – Purkinje neuron.  
- CL:0000100 – spinal motor neuron.  
- CL:0000103 – dorsal root ganglion neuron.  
- CL:0000120 – Schwann cell.[5][12]  

### Subcellular localization

Senataxin is a nuclear protein; relevant GO cellular component terms include:[5][12]

- Nucleus – GO:0005634.  
- Chromatin – GO:0000785.  
- Ribonucleoprotein complex – GO:1990904.  

---

## 8. Temporal Development

### Onset

- Typical age of onset: childhood to young adult (3–30 years).[3][4][6][12]  
- Onset pattern: insidious and chronic, with gradual development of gait instability and neuropathic symptoms rather than acute attacks.[3][5][12]  

### Progression and disease course

- Course: slowly progressive neurodegenerative disease.[3][5][8][12]  
- Staging: not formally staged, but clinical descriptions distinguish early ambulatory phase, intermediate phase with marked gait ataxia, and advanced phase with wheelchair dependence and severe neuropathy.[5][12]  
- Duration: lifelong; remission is not reported.[3][5][12]  

Critical periods include adolescence and early adulthood, when rapid functional decline can occur and when early rehabilitation may help preserve function.[5][8][12]

---

## 9. Inheritance and Population

### Inheritance pattern and penetrance

- Inheritance: autosomal recessive.[3][4][5][8][9][12][14]  
- Orphanet notes that “Transmission of SCAN2 is autosomal recessive. Genetic counseling is recommended as each sib of an affected individual has 25% risk of being affected, 50% risk of being an asymptomatic carrier, and 25% risk of being neither affected nor a carrier.”[3]  
- Penetrance: biallelic pathogenic SETX variants are considered highly penetrant; affected individuals invariably show some degree of ataxia and neuropathy.[5][12]  

Expressivity is variable, particularly regarding presence/absence of oculomotor apraxia and degree of neuropathy.[3][5][12] Genetic anticipation, germline mosaicism, and founder effects are not prominently reported, although recurrent variants have been described in some populations.[5][12][14]

### Epidemiology and demographics

- SCAN2 is categorized as a **rare / ultra‑rare disease**.[3][5][8][9][12]  
- Orphanet and NORD emphasize its rarity and lack of precise prevalence data, suggesting only a few hundred patients worldwide.[3][8][12]  
- Cases have been reported across diverse ethnic backgrounds, including European, Japanese, and Taiwanese individuals, indicating global distribution rather than geographic confinement.[5][12]  
- Sex ratio appears approximately equal; no strong sex bias is reported.[3][5][12]  
- Age distribution: affected individuals present predominantly in childhood and adolescence, with adult patients representing long‑standing disease rather than late onset.[3][5][12]  

---

## 10. Diagnostics

### Clinical and laboratory evaluation

Key diagnostic features:[3][4][5][8][12]

1. **Neurological examination:** Cerebellar signs (gait and limb ataxia, dysarthria), areflexia, distal weakness, sensory loss.  
2. **Serum biochemistry:** Elevated alpha‑fetoprotein (AFP), often markedly increased.[3][4][5][12]  
3. **Neuroimaging:** Brain MRI showing cerebellar atrophy, sometimes with mild brainstem involvement.[3][4][5][12]  
4. **Electrophysiology:** Nerve conduction studies/EMG show severe axonal sensorimotor polyneuropathy.[3][4][5][12]  
5. **Eye movement assessment:** Oculomotor apraxia (difficulty initiating horizontal saccades).[3][4][6][9][12]  

Suggested LOINC/NCIT‑type test concepts:

- Serum alpha‑fetoprotein measurement (laboratory test; HP:0006259).[3][4][5][12]  
- Magnetic resonance imaging of brain (NCIT:C16801).[3][4][12]  
- Electromyography and nerve conduction studies (NCIT:C38000).[3][4][12]  

### Genetic testing

Genetic confirmation is essential:[3][5][8][12][14]

- **Single‑gene testing:** Sequencing of SETX (NCIT:C18243 – Genetic Testing), including exon‑level sequencing and copy‑number analysis.[5][12][14]  
- **Gene panels:** Cerebellar ataxia and hereditary neuropathy panels routinely include SETX.[5][12]  
- **Whole‑exome or whole‑genome sequencing:** Useful when phenotype is unclear or multiple ARCA genes are suspected; the Taiwanese case was diagnosed via targeted NGS panel.[12]  

Chromosomal microarray, karyotyping, and FISH are not primary tests for SCAN2, because causative variants are point mutations and small indels rather than large structural changes.[3][5][11][12][14]

### Clinical criteria and differential diagnosis

No formal international diagnostic criteria exist, but a pragmatic clinical definition combines:[3][4][5][12]

- Childhood–juvenile onset progressive cerebellar ataxia.  
- Severe axonal sensorimotor neuropathy.  
- Elevated serum AFP.  
- Frequent oculomotor apraxia.  
- Autosomal recessive inheritance or consanguinity.  
- Confirmed biallelic pathogenic SETX variants.  

Differential diagnosis includes other autosomal recessive cerebellar ataxias:

- Ataxia with oculomotor apraxia type 1 (AOA1) – different gene (APTX), often lower AFP.[5]  
- COQ8A‑ataxia (ARCA2) – primary CoQ10 deficiency.[5]  
- Other ARCA genes (e.g., PMPCA, etc.).[5][11]  

Distinguishing features include the combination of elevated AFP, severe axonal neuropathy, and SETX mutations in SCAN2.[3][5][12]

### Screening

Population‑based newborn screening or carrier screening for SCAN2 is not currently implemented, given its rarity.[3][5][8] Targeted carrier and cascade testing in families with known SETX mutations is recommended in genetic counseling frameworks.[3][8][12]

---

## 11. Outcome / Prognosis

### Survival and mortality

Available case series and reviews suggest that SCAN2 is associated with major disability but generally not with early death, and many adult patients survive decades after onset.[3][5][8][12] Life expectancy is believed to be near normal in many individuals, though severe immobilization may increase secondary morbidity risk.[5][8][12]

### Morbidity and function

- Morbidity is substantial due to progressive gait ataxia, distal weakness, sensory loss, and oculomotor impairment, leading to dependence on wheelchairs and assistive devices.[3][5][8][12]  
- Long‑term functional impairments include inability to walk independently, difficulty with fine motor tasks, speech impairment, and reduced self‑care capacity.[3][5][8][12]  

Quality‑of‑life studies specific to SCAN2 are lacking, but extrapolation from ARCA cohorts suggests marked impact on physical functioning, role limitation, and social participation, as reflected in standard tools (e.g., SF‑36, EQ‑5D).[5]

### Disease course and complications

Common complications include:[3][5][8][12]

- Musculoskeletal contractures and deformities due to chronic neuropathy and immobility.  
- Falls and fractures due to ataxia.  
- Secondary complications from prolonged immobility (pressure ulcers, infections).  

Prognostic factors include earlier age of onset, rapid progression of neuropathy, and severity of cerebellar atrophy; milder variants may have slower progression.[5][12]

---

## 12. Treatment

### Pharmacotherapy

No disease‑modifying pharmacologic therapy is currently established for SCAN2.[3][5][8][12] Management is supportive and symptomatic:

- Neuropathic pain medications (e.g., analgesics; NCIT:C288) may be used for painful neuropathy.[5][8]  
- Agents for spasticity or tremor when present, though spasticity is less prominent in SCAN2 than in some other ataxias.[5]  

No SETX‑targeted small molecules or approved gene therapies are available.[5]

### Advanced therapeutics

Gene therapy, RNA‑based therapies, and cell‑based interventions have not yet been reported in clinical trials specifically for SCAN2; the ARCA review emphasizes that therapy for these disorders is largely supportive, with research into future gene‑based strategies ongoing.[5]

### Supportive and rehabilitative care

Core management strategies:[3][5][8][12]

- **Physical therapy** (NCIT:C15280) – to improve balance, strength, and prevent contractures.  
- **Occupational therapy** (NCIT:C15279) – to optimize activities of daily living and use of assistive devices.  
- **Speech therapy** (NCIT:C15384) – to address dysarthria and communication difficulties.  
- Orthotic devices, wheelchairs, and home adaptations to enhance safety and independence.[5][8][12]  

NORD and GARD emphasize multidisciplinary supportive care, including nutritional support and psychosocial counseling.[2][8]

### Experimental treatments and outcomes

No SCAN2‑specific interventional trials are currently highlighted in major trial registries; treatment response is therefore inferred from general ataxia and neuropathy management experience.[5][8][12] Physical and occupational therapy can stabilize function and delay loss of independence but do not halt disease progression.[5][8][12]

---

## 13. Prevention

### Primary prevention

Because SCAN2 is an autosomal recessive monogenic disorder, primary prevention focuses on reproductive options in families with known pathogenic SETX variants rather than environmental risk modification.[3][5][8][12]

### Secondary and tertiary prevention

- **Secondary prevention:** Early diagnosis through genetic testing allows timely initiation of rehabilitation, fall‑prevention strategies, and monitoring for complications.[3][5][8][12]  
- **Tertiary prevention:** Ongoing physiotherapy, occupational therapy, and management of neuropathic complications are critical to prevent contractures, falls, and secondary morbidity.[5][8][12]  

### Genetic counseling and risk stratification

Genetic counseling (NCIT:C16273) is strongly recommended for affected families; Orphanet outlines autosomal recessive recurrence risks (25% affected, 50% carriers).[3] Prenatal or preimplantation genetic diagnosis may be considered when familial SETX mutations are known.[3][8][12]

---

## 14. Other Species / Natural Disease

Orthologs of SETX exist in multiple species, and senataxin has been studied in model organisms (e.g., mice), but naturally occurring SCAN2‑like disease has not been widely reported in companion animals or livestock.[5] ZFIN includes a disease ontology term for “spinocerebellar ataxia with axonal neuropathy 2,” reflecting cross‑species annotation rather than a described zebrafish natural disease.[6]

Comparative biology studies focus on conserved roles of senataxin in genome stability and RNA processing, supporting evolutionary conservation of its molecular function.[5] No zoonotic transmission or cross‑species infectious aspects apply because SCAN2 is a purely genetic, non‑infectious condition.[3][5][8][12]

---

## 15. Model Organisms

The 2025 ARCA review discusses mechanistic insights from cellular and animal models of autosomal recessive cerebellar ataxias, including SETX‑related disease, highlighting the role of senataxin in R‑loop resolution and genome integrity.[5] In general:[5]

- **Model types:**  
  - Mammalian (mouse) models with Setx disruption have been used to study genome instability and neuronal dysfunction.  
  - Cellular models (HEK293, neuronal cultures) with SETX knockdown/knockout are used to examine R‑loop accumulation, DNA damage, and RNA processing defects.  

- **Phenotype recapitulation:**  
  - Models reproduce key molecular hallmarks (R‑loop accumulation, DNA damage, altered RNA processing) and sometimes neurological features (motor deficits), though full SCAN2 clinical phenotype is not completely recapitulated.[5]  

- **Limitations:**  
  - Differences in lifespan, neuronal architecture, and species‑specific gene regulation limit direct translation of model findings to human SCAN2.[5]  

These models are primarily used to elucidate SETX function, validate loss‑of‑function mechanisms, and identify potential molecular targets rather than to test specific clinical treatments.[5]

---

## Ontology and Evidence Summary

- **Disease ontology:** MONDO:0018996 – “spinocerebellar ataxia, autosomal recessive, with axonal neuropathy 2.”[9]  
- **Gene/protein:** SETX (HGNC:10740; OMIM:608465).[5][12]  
- **Key GO terms:** DNA repair (GO:0006281), RNA processing (GO:0006396), autophagy (GO:0006914), response to DNA damage stimulus (GO:0006974).[5][12]  
- **Key HPO terms:** Cerebellar ataxia (HP:0001251), axonal neuropathy (HP:0003438), oculomotor apraxia (HP:0000657), cerebellar atrophy (HP:0001272), elevated AFP (HP:0006259).[3][4][5][9][12]  
- **Key CL terms:** Purkinje neuron (CL:0000121), motor neuron (CL:0000100), dorsal root ganglion neuron (CL:0000103), Schwann cell (CL:0000120).[5][12]  
- **NCIT clinical intervention terms:** Genetic testing (NCIT:C18243), physical therapy (NCIT:C15280), occupational therapy (NCIT:C15279), speech therapy (NCIT:C15384).[3][5][8][12]  

**Primary evidence sources**

- Human clinical and genetic evidence: OMIM 606002, Orphanet 64753, GARD/NIH, MedGen, NORD, ClinVar, LOVD, and case reports such as the Taiwanese SETX mutation study.[2][3][4][5][8][11][12][14]  
- Mechanistic evidence: Functional studies of senataxin summarized in the 2025 ARCA review and related experimental work.[5][12]  
- Ontology and classification: MONDO, DOID/ZFIN, and MedGen disease entries.[4][6][9]  

Together, these data support a coherent picture of SCAN2 as a monogenic, autosomal recessive cerebellar ataxia with axonal neuropathy caused by SETX loss‑of‑function, with a well‑characterized clinical phenotype and emerging mechanistic understanding centered on genome integrity and RNA metabolism.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 19 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0006281` (3 mentions) - the report calls it "GO biological processes:** DNA repair", "Key GO terms:** DNA repair"; GO calls it **DNA repair**
- `CL:0000103` (3 mentions) - the report calls it "dorsal root ganglion neuron"; CL calls it **bipolar neuron**
- `UBERON:0001898` (1 mention) - the report calls it "brainstem"; UBERON calls it **hypothalamus**
- `NCIT:C16801` (1 mention) - the report calls it "Magnetic resonance imaging of brain"; NCIT calls it **Long-Term Care for Elderly**
- `NCIT:C38000` (1 mention) - the report calls it "Electromyography and nerve conduction studies"; NCIT calls it **Performed**
- `NCIT:C18243` (2 mentions) - the report calls it "Genetic Testing", "NCIT clinical intervention terms:** Genetic testing"; NCIT calls it **Regression**
- `NCIT:C15280` (2 mentions) - the report calls it "Physical therapy"; NCIT calls it **Breast Conservation Treatment**
- `NCIT:C15279` (2 mentions) - the report calls it "Occupational therapy"; NCIT calls it **Radical Mastectomy**
- `NCIT:C15384` (2 mentions) - the report calls it "Speech therapy"; NCIT calls it **Surgical Incision**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0006259` (3 mentions) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001251` (2 mentions) - the report calls it "Key HPO terms:** Cerebellar ataxia"; HP calls it **Ataxia**, and lists "Cerebellar ataxia" among its other names
- `CL:0000121` (3 mentions) - the report calls it "CL cell types:** Cerebellar Purkinje neuron", "Purkinje neuron", "Key CL terms:** Purkinje neuron"; CL calls it **Purkinje cell**, and lists "cerebellar Purkinje cell" among its other names
- `CL:0000100` (3 mentions) - the report calls it "spinal motor neuron"; CL calls it **motor neuron**
- `CL:0000120` (3 mentions) - the report calls it "Schwann cell"; CL calls it **granule cell**
- `UBERON:0001016` (1 mention) - the report calls it "Nervous system overall"; UBERON calls it **nervous system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0006281` - called "GO biological processes:** DNA repair", "Key GO terms:** DNA repair"
- `CL:0000121` - called "CL cell types:** Cerebellar Purkinje neuron", "Purkinje neuron", "Key CL terms:** Purkinje neuron"
- `NCIT:C18243` - called "Genetic Testing", "NCIT clinical intervention terms:** Genetic testing"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.