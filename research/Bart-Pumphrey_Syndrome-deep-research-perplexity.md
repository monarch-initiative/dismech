---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-28T13:09:41.789996'
end_time: '2026-09-28T13:16:11.115647'
duration_seconds: 389.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Bart-Pumphrey Syndrome
  mondo_id: MONDO:0007866
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
citation_count: 18
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 37
  verified: 34
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.029
  labels_checked: 2
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C1222
    reported_labels:
    - Keratolytic Agent
    ontology_label: Miglustat
  unresolved_terms:
  - NCIT:C28125
  unresolvable_prefixes:
  - DO
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bart-Pumphrey Syndrome
- **MONDO ID:** MONDO:0007866 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bart-Pumphrey Syndrome** covering all of the
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

# Bart-Pumphrey Syndrome: Comprehensive Disease Characteristics and Mechanisms

Bart-Pumphrey syndrome is a rare autosomal dominant Mendelian disorder characterized by the constellation of sensorineural hearing loss, palmoplantar keratoderma, knuckle pads, and leukonychia, caused in most documented families by heterozygous missense variants in the *GJB2* gene encoding connexin 26 on chromosome 13q12.11.[1][5][14] The condition occupies a distinctive place within the broader spectrum of *GJB2*-related diseases, which range from nonsyndromic recessive deafness to several overlapping syndromic disorders with cutaneous involvement, including Vohwinkel syndrome, keratitis–ichthyosis–deafness (KID) syndrome, hystrix-like ichthyosis–deafness, palmoplantar keratoderma with deafness, and Bart-Pumphrey syndrome.[5][13][16] Although only a small number of kindreds have been reported worldwide since the original description by Bart and Pumphrey in 1967, the disorder is now firmly linked to dominant missense mutations in evolutionary conserved regions of connexin 26 that exert pleiotropic effects on epidermal homeostasis and cochlear function.[5][11][12] Clinical expression is notably variable, even within families, with differences in severity and distribution of palmoplantar keratoderma, presence or absence of knuckle pads or leukonychia, and degree of hearing loss, underscoring the importance of careful phenotyping and genetic confirmation.[2][4][6][14] Disease management is primarily supportive and symptomatic, focusing on audiological rehabilitation and dermatologic care (including retinoids for keratoderma), while genetic counseling addresses recurrence risk and the wider implications of *GJB2*-related conditions.[6][16]  

## 1. Disease Information

### 1.1 Definition and Overview

Bart-Pumphrey syndrome (BPS), also known as Bart-Pumphrey syndrome (OMIM 149200) or “knuckle pads–leukonychia–sensorineural deafness–palmoplantar keratoderma syndrome,” is a rare autosomal dominant genetic deafness syndrome characterized by the combination of symmetric or asymmetric knuckle pads, diffuse palmoplantar keratoderma, leukonychia, and congenital mild-to-moderate sensorineural hearing loss.[1][2][7][14] Orphanet defines the disorder as a “rare, syndromic genetic deafness disease characterized by symmetric or asymmetric knuckle pads (typically located on the distal and interphalangeal joints), leukonychia, diffuse palmoplantar keratoderma, and congenital, mild to moderate sensorineural deafness,” emphasizing its syndromic nature and its association with a specific constellation of cutaneous and auditory phenotypes.[7] The Online Mendelian Inheritance in Man (OMIM) entry 149200 describes BPS as an autosomal dominant disorder with “sensorineural hearing loss, palmoplantar keratoderma, knuckle pads, and leukonychia, which shows considerable phenotypic variability,” and attributes the condition to heterozygous mutations in *GJB2* on chromosome 13q12.[1][5]  

MedlinePlus Genetics similarly defines Bart-Pumphrey syndrome as a disorder “characterized by nail and skin abnormalities and hearing loss,” and notes that affected individuals typically have white discoloration of the nails (leukonychia), thickened skin of the palms and soles (palmoplantar keratoderma), wart-like nodules at the knuckles (knuckle pads), and sensorineural hearing loss.[3][14] Malacards and dermatologic reviews classify BPS among hereditary palmoplantar keratodermas with associated sensorineural deafness and knuckle lesions, reinforcing its membership in the group of *GJB2*-related keratinizing disorders.[8][9][10] Clinically, BPS is therefore best conceptualized as a pleiotropic connexinopathy that combines a hereditary hearing loss phenotype with focal and diffuse hyperkeratosis of acral skin and nail matrix abnormalities, all attributable to altered gap junction function in specific epithelial and inner ear cell types.[3][5][18]  

### 1.2 Key Identifiers and Ontology Mapping

Bart-Pumphrey syndrome is indexed in multiple biomedical databases and ontologies. OMIM lists the condition under entry 149200 with the designation “Knuckle pads, leukonychia, and sensorineural deafness” and specifies *GJB2* (MIM 121011) as the causal gene.[1] Orphanet registers the disorder as Orpha number 2698, with the preferred name “Knuckle pads–leukonychia–sensorineural deafness–palmoplantar hyperkeratosis syndrome” and several recognized synonyms.[7] Malacards catalogs BPS as “Bart-Pumphrey syndrome” and cross-links it with OMIM, Orphanet, and gene-centered resources, also noting a point prevalence <1/1,000,000 worldwide.[2]  

SNOMED CT includes BPS under concept 1271009 (noted in OMIM’s cross-references) as a specific hereditary syndrome combining knuckle pads, leukonychia, and deafness.[1] Disease Ontology (DO) cross-references the OMIM entry as DO:0050658.[1] The user has provided a MONDO identifier, MONDO:0007866, which corresponds to Bart-Pumphrey syndrome in the Mondo disease ontology, although this specific mapping is not explicitly detailed in the provided search results. Based on ontology practices, BPS would be represented as a subclass of “hereditary palmoplantar keratoderma with deafness” and “autosomal dominant disease” in Mondo.[7][16]  

For Human Phenotype Ontology (HPO), the major component phenotypes map to standard terms: sensorineural hearing impairment (HP:0000407), palmoplantar keratoderma (HP:0000982), knuckle pads (HP:0100803), and leukonychia (HP:0001598).[7][8][9][14] Uberon anatomy ontology terms applicable to the disease include skin of palm (UBERON:0002387), skin of sole of foot (UBERON:0002385), nail (UBERON:0001698), finger (UBERON:0001459), toe (UBERON:0001510), and cochlea (UBERON:0001844).[7][16][18] At the gene level, *GJB2* is represented in the HUGO Gene Nomenclature Committee (HGNC) database as HGNC:4284, encodes “gap junction beta-2 protein” (connexin 26), and maps to multiple Gene Ontology terms relating to gap junction channel activity and cell–cell communication.[18][17]  

### 1.3 Synonyms and Alternative Names

Multiple synonymous names for Bart-Pumphrey syndrome are recognized across resources, reflecting historical descriptions and variations in emphasis on particular manifestations. Orphanet lists the following synonyms: “Bart-Pumphrey syndrome,” “Knuckle pads–leukonychia–sensorineural deafness–palmoplantar keratoderma syndrome,” and “Knuckle pads–leukonychia–sensorineural hearing loss–palmoplantar hyperkeratosis syndrome.”[7] MedlinePlus notes “Knuckle pads, deafness, and leukonychia syndrome” as an alternative designation.[14] Dermatologic literature often describes the entity as “palmoplantar keratoderma with knuckle pads and leukonychia and deafness,” emphasizing the cutaneous manifestations and hereditary deafness.[8][10]  

Historically, Bart and Pumphrey’s original 1967 description in the New England Journal of Medicine referred to “Knuckle pads, leukonychia and deafness: a dominantly inherited syndrome,” which has contributed to persistent use of this phrase as a descriptive name.[11][12] Some dermatology texts also use “Schwann syndrome” as a synonym, although this term is less frequent and may be ambiguous in broader neurological contexts.[10] For the purposes of standardized disease knowledge base representation, “Bart-Pumphrey syndrome” and “Knuckle pads–leukonychia–sensorineural deafness–palmoplantar keratoderma syndrome” are the principal preferred names, supplemented by the shorter descriptive synonym “Knuckle pads, deafness, and leukonychia syndrome.”[7][10][14]  

### 1.4 Source Nature: Individual Case Data vs Aggregated Resources

Information on Bart-Pumphrey syndrome is derived from a mixture of individual patient-level case reports, small multigeneration family studies, and aggregated descriptions in gene-centric, dermatologic, and rare disease databases. The original description by Bart and Pumphrey in 1967 was based on a single kindred in which knuckle pads, mixed hearing loss, and total leukonychia segregated as a dominant trait.[11][12] Subsequent case reports and family studies, such as the Polish multigeneration family analyzed by Richard et al. in 2004, the Brazilian father–son pair reported by Marques-de-Faria and colleagues, and other familial and sporadic cases, provide primary clinical data and genotype–phenotype correlations.[4][5][6]  

Aggregated disease-level information is compiled in OMIM, Orphanet, Malacards, MedlinePlus Genetics, NORD’s GJB2-related conditions overview, and dermatology reviews of hereditary palmoplantar keratoderma and knuckle lesions, which synthesize clinical features, inheritance patterns, pathophysiology, and management strategies based on the limited number of published cases.[1][2][7][8][9][10][14][16] These resources are primarily curated from clinical case reports, small series, and mechanistic studies of *GJB2* mutations in vitro and in model systems, rather than from large observational cohorts or EHR-based population datasets, reflecting the extreme rarity of BPS.[2][7][16] No dedicated population registry or large-scale epidemiologic dataset for BPS has been described in the literature to date, and existing prevalence estimates are inferential and rely on Orphanet’s orphan disease categorization.[7]  

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic Basis

Bart-Pumphrey syndrome is unequivocally a genetic condition caused by heterozygous germline variants in *GJB2* encoding connexin 26, a gap junction protein expressed in the inner ear and epidermis.[1][3][5][14][18] OMIM uses a number sign with entry 149200 to indicate that BPS is caused by mutation in *GJB2* (MIM 121011) on chromosome 13q12.[1] MedlinePlus Genetics similarly states that “Bart-Pumphrey syndrome is caused by mutations in the *GJB2* gene,” and that these variants change single amino acids in the connexin 26 protein.[3][14] Richard et al. (2004) provided the first direct genetic evidence by identifying a novel nonconservative missense mutation N54K in *GJB2* segregating with BPS in a multigeneration Northern European family; this variant affects the first extracellular loop of connexin 26, which is important for hemichannel docking and voltage gating.[5]  

Subsequent reports have identified additional *GJB2* missense variants in families with BPS or closely overlapping phenotypes, further cementing the causal role of this gene.[1][2][5] Malacards lists specific *GJB2* amino acid substitutions associated with Bart-Pumphrey syndrome, including p.Asn54Lys (N54K) and p.Gly59Ser (G59S), and notes that BPS is one of several *GJB2*-associated syndromic deafness disorders.[2][5] The pathogenic variants are germline, present in heterozygous state, and transmitted in autosomal dominant fashion with male-to-male transmission documented in at least one family, confirming that BPS is not X-linked or mitochondrial.[1][4][5]  

Mechanistically, the causal factors are alterations in connexin 26 structure and function that lead to disrupted gap junction communication in cochlear supporting cells and epidermal keratinocytes, impairing potassium recycling in the inner ear and coordinated differentiation of acral skin and nail matrix.[3][5][18] This places BPS squarely in the class of “connexinopathies” caused by dominant-negative or gain-of-function effects of mutant connexins, rather than by loss-of-function truncating variants that typically underlie recessive nonsyndromic deafness.[5][16][17] There is no evidence that environmental, infectious, or purely epigenetic factors can cause BPS in the absence of a germline *GJB2* mutation, although environmental or epigenetic modifiers may influence expressivity.[1][2][5][7]  

### 2.2 Genetic Risk Factors: Causal Variants and Susceptibility Loci

At present, *GJB2* is the only gene firmly implicated as a causal locus for Bart-Pumphrey syndrome, although Malacards algorithmically lists several other connexin genes (such as *GJB4*, *GJB6*, *GJA5*) as theoretically associated based on shared pathways and overlapping phenotypes, without direct evidence that these genes cause BPS.[2] The primary genetic risk factor is therefore the presence of a heterozygous pathogenic missense variant in *GJB2* that alters the function of connexin 26 in a manner consistent with dominant syndromic deafness and skin manifestations.[1][3][5][14]  

Richard et al. identified *GJB2*:c.162T>A (p.Asn54Lys, N54K) in a family with Bart-Pumphrey syndrome and demonstrated that this nonconservative substitution lies within a cluster of pathogenic *GJB2* mutations affecting the conserved first extracellular loop of connexin 26.[5] This region is critical for connexon–connexon docking and voltage gating, and mutations here have been associated with KID syndrome, Vohwinkel syndrome, palmoplantar keratoderma with deafness, and BPS, suggesting a pleiotropic effect of specific alleles.[5][13][17] Malacards lists additional variants, including p.Gly59Ser (G59S), as associated with Bart-Pumphrey syndrome, although primary literature evidence linking this variant specifically to BPS is more limited and may derive from overlapping syndromes with PPK and deafness.[2][8][9]  

Broader *GJB2*-related conditions involve numerous missense and truncating variants, many of which cause autosomal recessive nonsyndromic hearing loss (DFNB1), while a subset cause autosomal dominant nonsyndromic or syndromic hearing loss through dominant-negative mechanisms.[13][16][17] A comprehensive genotype–phenotype review notes that missense variants clustering on the first extracellular loop E1 of connexin 26, such as p.Arg75Trp (R75W) and p.Arg75Gln (R75Q), impair gap junction formation and cause severe prelingual hearing loss with variably penetrant palmoplantar keratoderma.[17][15] Although R75W and R75Q are more classical for “palmoplantar keratoderma with deafness” rather than BPS per se, their existence demonstrates that multiple dominant *GJB2* missense alleles can produce overlapping syndromic phenotypes with different constellations of skin and nail involvement.[13][15][17]  

No modifier genes or susceptibility loci distinct from *GJB2* have been convincingly shown to modulate risk for Bart-Pumphrey syndrome, although intragenic or cis-regulatory variants might conceivably influence expression levels and thereby disease severity. Given the tiny number of reported families, genome-wide association or systematic modifier gene studies are not feasible at present.[2][5][7]  

### 2.3 Environmental and Lifestyle Risk Factors

Current evidence does not support any specific environmental, occupational, lifestyle, or infectious risk factors for Bart-Pumphrey syndrome independent of the underlying genetic mutation. The disorder is rare, highly penetrant within families, and clearly segregates as an autosomal dominant trait with vertical transmission, consistent with a primary monogenic etiology.[1][4][5][7][11] There is no suggestion in the case reports or aggregated resources that exposure to toxins, radiation, specific diets, smoking, alcohol, or infections precipitates or significantly modifies disease onset in carriers of pathogenic *GJB2* variants.[4][5][8]  

Environmental factors may naturally influence nonspecific aspects of symptom expression, such as mechanical stress on the palms and soles affecting callus formation, or trauma to the nails influencing onychodystrophy, but these ubiquitous influences are not disease-specific risk factors and are not discussed in the BPS literature as etiologic contributions.[8][9] Similarly, general risk factors for age-related hearing loss (e.g., noise exposure) may co-exist in affected individuals but are unlikely to be the primary cause of early-onset sensorineural deafness in BPS, which typically presents congenitally or in childhood.[4][7][14][16]  

### 2.4 Protective Factors

No genetic protective variants or environmental protective factors have been identified for Bart-Pumphrey syndrome, largely because the disorder is rare and has not been the subject of large-scale epidemiologic or population genetic studies. In principle, individuals with heterozygous pathogenic *GJB2* variants might exhibit variable expressivity due to protective alleles in other connexin genes, compensatory upregulation of alternative gap junction proteins, or favorable epigenetic configurations that mitigate the impact of the mutant protein, but such hypotheses remain speculative and untested.[2][5][17]  

Similarly, no evidence-based lifestyle or environmental modifications are known to reduce the risk or severity of BPS manifestations beyond general measures for hearing conservation and skin care that apply to many dermatologic and hearing disorders.[8][16] Standard supportive practices, such as avoiding loud noise to preserve residual hearing and using emollients to reduce keratoderma cracking, are helpful but do not act as disease-preventive factors in the strict sense.[8][16]  

### 2.5 Gene–Environment Interactions

Because BPS is a highly penetrant monogenic disorder with clear autosomal dominant transmission, gene–environment interaction studies have not been performed, and there is no specific evidence of environmental factors modifying penetrance or expressivity in carriers of *GJB2* mutations causing Bart-Pumphrey syndrome.[1][4][5] The observed phenotypic variability across and within families appears to be largely intrinsic, possibly reflecting stochastic variation, allele-specific differences, or uncharacterized genetic modifiers rather than clearly defined environmental interactions.[2][5][7]  

Comparative Toxicogenomics Database and similar resources catalog interactions between environmental agents and *GJB2* at a general level, but these are not linked to BPS specifically and often derive from experimental systems unrelated to human disease.[16][17] For purposes of a disease knowledge base entry, Bart-Pumphrey syndrome should therefore be considered an archetypal Mendelian disorder with minimal evidence for clinically relevant gene–environment interactions, while remaining open to future discoveries that may identify modifiers of phenotype severity or timing.  

## 3. Phenotypes

### 3.1 Core Clinical Phenotypes and HPO Mapping

Bart-Pumphrey syndrome is defined by four core clinical phenotypes: sensorineural hearing loss, palmoplantar keratoderma, knuckle pads, and leukonychia.[1][5][7][14] These manifestations span multiple categories of phenotypic types, including symptoms (self-reported hearing difficulties, pain from hyperkeratotic skin), clinical signs (observable palmar/plantar thickening and knuckle nodules), physical manifestations (visible nail discoloration and deformity), and in some cases laboratory or electrophysiologic abnormalities (audiometric defects).[4][5][8]  

Sensorineural hearing loss in BPS is typically congenital, mild to moderate in severity, and may be non-progressive or slowly progressive.[4][5][7][14][16] HPO terms applicable include sensorineural hearing impairment (HP:0000407), congenital hearing impairment (HP:0009794), and prelingual onset (HP:0008527).[7][14][16] Palmoplantar keratoderma presents as diffuse thickening of the stratum corneum on the palms and soles, often with a “honeycomb” appearance and potential fissuring; appropriate HPO terms include palmoplantar keratoderma (HP:0000982), hyperkeratosis (HP:0000962), and possibly painful plantar keratoderma (HP:0005590) when fissures cause pain.[8][9]  

Knuckle pads manifest as well-circumscribed papules or verrucous nodules on the dorsum of the proximal and distal interphalangeal joints of fingers and toes.[4][8][9] HPO provides the term knuckle pads (HP:0100803), describing these hyperkeratotic or fibrotic nodules over joints. Leukonychia in BPS is usually total or near-total whitening of fingernails and toenails, sometimes accompanied by thick, crumbly nail texture; the principal HPO term is leukonychia (HP:0001598), with possible additional terms for nail dystrophy (HP:0008404).[1][2][14]  

Other reported phenotypes in BPS or overlapping *GJB2* syndromes include breast or axillary cysts, acanthosis nigricans, and additional cutaneous findings, although these are not consistently present in Bart-Pumphrey syndrome and may reflect overlap with related disorders.[8][9] Hereditary palmoplantar keratoderma reviews note that BPS patients may exhibit sensorineural hearing loss, knuckle pads, leukonychia, and sometimes cysts in breast and axillary regions, but these additional features are rare and not considered defining.[8] NORD’s GJB2-related conditions overview emphasizes that *GJB2* syndromes can involve multi-system manifestations including skin and hair abnormalities, but for BPS specifically, the core tetrad remains palmoplantar keratoderma, leukonychia, knuckle pads, and audiological involvement.[16]  

### 3.2 Age of Onset, Severity, and Progression

Age of onset of the major BPS phenotypes varies by organ system. Sensorineural hearing loss is typically present at birth or in early infancy, reflecting congenital cochlear dysfunction due to connexin 26 abnormalities.[4][5][7][14][16] Orphanet lists the age of onset for the syndrome as childhood, but the hearing component is often congenital or prelingual.[7][16] Audiometric data from case reports support early-onset hearing impairment, and JAMA Dermatology notes that hearing loss in BPS “typically exists from birth” and may be sensorineural, mixed, or conductive, though sensorineural is most common.[6]  

Palmoplantar keratoderma generally emerges in childhood, with progressive thickening of the palmar and plantar skin over the first years of life.[4][7][8] Knuckle pads often appear in childhood or adolescence as focal nodules, and their development may be gradual as repeated mechanical stress and abnormal keratinocyte signaling contribute to localized hyperplasia.[4][8][9] Leukonychia may be evident from early childhood, although in some cases the extent of nail whitening increases over time, reflecting cumulative abnormalities in nail matrix keratinization.[1][2][14]  

Severity of phenotypes is variable. Hearing loss ranges from mild to moderate in many cases, although some families have members with more severe impairment, and overlapping *GJB2* syndromes such as palmoplantar keratoderma with deafness or Vohwinkel syndrome can show severe-to-profound sensorineural deafness.[5][8][9][15][17] Palmoplantar keratoderma in BPS may be diffuse or focal, mild or pronounced, and can be asymptomatic or cause significant discomfort and functional limitation if fissures develop.[8][9] Knuckle pads are often painless but cosmetically conspicuous; leukonychia is mainly a cosmetic issue but can be associated with brittle or crumbly nails that affect manual function.[2][8][14]  

In terms of progression, sensorineural hearing loss in *GJB2*-related conditions is often stable or slowly progressive.[16][17] Recessive DFNB1 typically involves severe-to-profound congenital hearing loss that is non-progressive, whereas dominant *GJB2* mutations can cause milder or progressive phenotypes depending on the specific allele.[16][17] For Bart-Pumphrey syndrome, the limited data suggest that congenital hearing loss may remain relatively stable, but longitudinal audiometric series are sparse. Palmoplantar keratoderma tends to increase in thickness through childhood and adolescence, then stabilize, while knuckle pads may enlarge gradually or remain static.[4][8][9] Leukonychia is persistent but not known to progress into more destructive nail disease. Overall, BPS can be described as a chronic, lifelong condition with partial progression of cutaneous manifestations in early life and stable or moderately progressive hearing loss.  

### 3.3 Frequency of Phenotypes and Intra-Familial Variability

The relative frequency of core phenotypes among affected individuals is high but not absolute, reflecting variable expressivity. In the original Bart and Pumphrey family, all affected members displayed knuckle pads, total leukonychia, and hearing loss, supporting a strong co-segregation of these traits.[11][12] However, later reports illustrate that some individuals with *GJB2* mutations and the BPS phenotype may lack leukonychia or present with minimal nail involvement, while others show more pronounced palmoplantar keratoderma or knuckle pads.[4][5][8][9][10]  

Marques-de-Faria et al. described a father–son pair with congenital sensorineural deafness, diffuse palmoplantar keratoderma, and knuckle pads but without leukonychia, yet concluded that the case was suggestive of Bart-Pumphrey syndrome based on the combination of features and male-to-male transmission reinforcing autosomal dominance.[4] Richard et al. noted “considerable phenotypic variability” in their N54K *GJB2* family, with differences in severity of skin and nail manifestations among mutation carriers.[5] Malacards also explicitly states that BPS shows “considerable phenotypic variability, even within the same family,” highlighting intrafamilial differences and incomplete penetrance of individual features.[2]  

Thus, while sensorineural hearing loss appears to be highly penetrant and palmoplantar keratoderma and knuckle pads are very common among genetically affected individuals, leukonychia may be absent or mild in some cases.[1][2][4][5][7][14] Quantitative frequency estimates (e.g., percentages) are not available due to small sample sizes, but qualitatively, the combination of hearing loss and at least one of the cutaneous features (PPK, knuckle pads, leukonychia) is nearly universal in reported families.  

### 3.4 Quality of Life Impact

Bart-Pumphrey syndrome affects quality of life primarily through its hearing and dermatologic manifestations. Congenital or early childhood sensorineural hearing loss can significantly impair speech and language development, academic performance, employment opportunities, and social participation.[4][14][16] NORD’s GJB2-related conditions overview emphasizes that early diagnosis and access to hearing aids or cochlear implants can improve communication and quality of life, underscoring the need for prompt audiological intervention in *GJB2*-related deafness.[16] This is equally applicable to BPS, where sensorineural hearing impairment is a core feature.  

Palmoplantar keratoderma may cause pain, tenderness, and difficulty with ambulation, especially if fissures develop in thickened plantar skin, limiting walking, running, or standing for extended periods.[8][9] Individuals may restrict physical activity and occupational tasks requiring manual labor due to discomfort or cosmetic embarrassment about their palms and soles. Knuckle pads, although often painless, can be cosmetically distressing and may be stigmatized, particularly in cultures where visible skin deformities attract social attention.[8][9] Leukonychia, while medically benign, can affect self-image and may be associated with nail brittleness, interfering with fine motor tasks.  

No formal quality of life studies specifically focused on Bart-Pumphrey syndrome are available, but generic instruments such as SF-36 or EQ-5D would likely capture impairments in domains such as physical functioning and social functioning in affected individuals. Extrapolating from broader literature on hereditary palmoplantar keratoderma and congenital deafness, BPS is expected to have moderate impact on quality of life, with severity modulated by the extent of hearing impairment, pain from keratoderma, and psychosocial coping.[8][16][17]  

## 4. Genetic and Molecular Information

### 4.1 Causal Genes and Locus Information

The causal gene for Bart-Pumphrey syndrome is *GJB2* (Gap Junction Beta-2 protein), encoding connexin 26, a 226-amino-acid transmembrane protein that forms gap junction channels.[1][3][5][18] OMIM lists *GJB2* as the locus for BPS, located at chromosome 13q12.[1] MedlinePlus Genetics states that the *GJB2* gene provides instructions for making connexin 26, and pathogenic variants in this gene have been found to cause Bart-Pumphrey syndrome.[3][14] UniProt entry P29033 describes gap junction beta-2 protein as a structural component of gap junctions localized to the cell membrane and gap junction plaques, forming hexameric hemichannels (connexons) that dock to similar hemichannels on adjacent cells to create intercellular channels.[18]  

*GJB2* belongs to the connexin family, beta-type (group I) subfamily, and participates in key biological processes such as cell–cell communication, ion transport, and maintenance of tissue homeostasis.[18][17] In the cochlea, connexin 26 is expressed in supporting cells and is crucial for potassium recycling and endolymph homeostasis. In the epidermis, it is expressed in keratinocytes and contributes to coordinated differentiation and barrier function.[3][16][17] The gene’s HGNC identifier is HGNC:4284, and the OMIM entry for *GJB2* itself is 121011.[1][18]  

### 4.2 Pathogenic Variants: Types and Functional Classification

Bart-Pumphrey syndrome is associated predominantly with missense variants in *GJB2* that alter single amino acids in connexin 26.[1][2][3][5][14] MedlinePlus Genetics notes that pathogenic variants causing BPS involve substitution of one amino acid for another in gap junction beta-2, and that the altered protein disrupts normal function, affecting skin growth and hearing by disturbing the conversion of sound waves to nerve impulses.[3][14] Richard et al. characterized the N54K mutation as a nonconservative missense change in the first extracellular loop of connexin 26, lying within a cluster of pathogenic *GJB2* mutations associated with overlapping syndromes.[5]  

Malacards lists specific BPS-associated *GJB2* sequence changes, including p.Asn54Lys (N54K; VAR_032750; rs104894412) and p.Gly59Ser (G59S; VAR_032751; rs104894410).[2] These variants are non-truncating missense alleles and are classified as pathogenic or likely pathogenic in gene-specific curation efforts, although the exact ACMG/AMP classification is not provided in the search results. Based on genotype–phenotype reviews, missense variants such as N54K, G59S, R75W, and R75Q in *GJB2* are recognized as pathogenic alleles causing autosomal dominant hearing loss with or without skin involvement.[13][15][17]  

Functionally, these missense variants are thought to exert dominant-negative or gain-of-function effects rather than simple loss-of-function.[5][17] UniProt and mechanistic studies note that connexin 26 hemichannels are formed by hexamers of connexin monomers, and that docking of two hemichannels from adjacent cells creates functional gap junction channels.[18] Mutations in critical extracellular domains can impair hemichannel docking, alter voltage gating, or change permeability, resulting in abnormal intercellular communication. Dominant-negative variants can co-assemble with wild-type connexin 26 and reduce gap junction function across the cell population, while some gain-of-function mutations may cause aberrant hemichannel opening and cytotoxic ion flux.[5][17][18]  

Allele frequency in general population databases such as gnomAD is low for pathogenic BPS-associated variants, consistent with the rarity of the syndrome. While specific gnomAD frequencies are not provided in the search results, it is known that common truncating *GJB2* variants such as c.35delG are prevalent in certain populations and cause recessive nonsyndromic deafness, whereas BPS-associated missense alleles like N54K and G59S are much rarer and typically segregate in single families.[17] All known BPS variants are germline and inherited, not somatic; somatic *GJB2* mutations are not implicated in BPS and are more relevant to neoplastic processes, which are outside the scope of this disease.[18]  

### 4.3 Functional Consequences and Mechanistic Categories

At the protein level, BPS-associated *GJB2* variants disrupt connexin 26 structure and function in ways that compromise gap junction coupling in tissues critical for hearing and skin integrity.[3][5][18] The N54K variant, for example, lies in the first extracellular loop and is predicted to alter hemichannel docking and voltage gating, reducing the efficiency of intercellular channels.[5] Functional studies of related *GJB2* variants (such as R75W and R75Q) have shown impaired gap junction formation, reduced dye transfer between cells, and dominant-negative effects on wild-type connexin 26, providing a mechanistic template likely applicable to N54K and other BPS alleles.[17][15]  

From a functional classification standpoint, BPS-associated variants can be considered non-truncating, dominant-negative missense mutations that lead to partial loss of function and aberrant gain of abnormal channel behavior.[5][17] In the cochlea, partial loss of function reduces potassium recycling in the endolymphatic space, causing hair cell dysfunction and sensorineural hearing loss.[3][16][17] In the epidermis and nail matrix, altered channel function disrupts coordinated proliferation and differentiation of keratinocytes, leading to hyperkeratosis (keratoderma and knuckle pads) and abnormal nail matrix keratinization (leukonychia).[5][8][9]  

Gene Ontology (GO) terms relevant to the molecular function of connexin 26 include gap junction channel activity (GO:0005243), ion transmembrane transport (GO:0034220), and cell–cell signaling (GO:0007267).[18][17] Biological process terms include cell communication (GO:0007154), potassium ion transmembrane transport (GO:0071805), and regulation of keratinocyte differentiation (GO:0030216). The cellular component terms include gap junction (GO:0005921), plasma membrane (GO:0005886), and connexon complex (GO:0005922).[18]  

### 4.4 Modifier Genes and Epigenetic Information

No specific modifier genes have been identified that alter the severity or expression of Bart-Pumphrey syndrome, but the broader *GJB2* literature suggests that co-expressed connexins such as connexin 30 (*GJB6*) and connexin 30.3 (*GJB4*) may modulate phenotype, as connexin heteromeric channels exist in the cochlea and epidermis.[18][17] UniProt notes that connexin 26 can form heteromeric channels with GJB4, raising the possibility that variation in *GJB4* could influence the functional impact of BPS-associated *GJB2* mutations.[18] Malacards lists *GJB4*, *GJB6*, and *GJA5* among genes associated with Bart-Pumphrey syndrome, although this is likely an inference from shared connexin function and overlapping phenotypes rather than direct evidence of causality.[2]  

Epigenetic modifications, such as DNA methylation or histone changes affecting *GJB2* expression, have not been studied in the context of BPS specifically. However, epigenetic regulation of connexin gene expression in skin and inner ear is an active area of research, and such mechanisms could theoretically modulate disease expressivity by altering the balance of mutant and wild-type connexin 26 or the expression of compensatory connexins.[17] The absence of empirical data for Bart-Pumphrey syndrome necessitates caution in extrapolation, and for a knowledge base entry, epigenetic contributions should be considered speculative at present.  

### 4.5 Chromosomal Abnormalities

Bart-Pumphrey syndrome is not associated with large-scale chromosomal abnormalities such as aneuploidy, translocations, or inversions; rather, it results from single-gene point mutations in *GJB2*.[1][5][14] DECIPHER, ClinVar, and structural variation databases are more relevant for syndromes caused by chromosomal rearrangements, which are not implicated in BPS. OMIM’s mapping of *GJB2* to chromosome 13q12.11 provides locus information, but BPS itself is not associated with copy number variation at this locus.[1][18]  

## 5. Environmental Information

### 5.1 Environmental Factors

There is no evidence that environmental toxins, radiation, pollution, or specific occupational exposures play a causative role in Bart-Pumphrey syndrome.[1][4][5][7] Case reports of BPS come from diverse backgrounds (Northern European, Polish, Brazilian families), without shared exposure histories suggestive of an environmental etiology.[4][5][6] The pathogenesis clearly revolves around germline *GJB2* mutations, and environmental factors primarily exert nonspecific effects on symptom expression (e.g., mechanical stress influencing keratoderma severity).  

Comparative Toxicogenomics Database and other toxicology resources catalog general interactions between connexin genes and environmental factors, but these are not linked specifically to BPS or *GJB2*-related deafness syndromes.[16][17] Environmental co-factors might influence disease experience (e.g., high-impact activities worsening plantar pain), but they do not cause or qualitatively transform the syndrome.  

### 5.2 Lifestyle Factors

Similarly, lifestyle factors such as smoking, diet, physical exercise, and alcohol consumption have not been implicated as contributors to the onset or severity of Bart-Pumphrey syndrome.[4][5][8] Standard lifestyle advice for individuals with hereditary hearing loss (such as avoiding excessive noise exposure) and keratoderma (using moisturizers, avoiding repetitive trauma) is relevant but not disease-specific.[8][16]  

### 5.3 Infectious Agents

No infectious agents have been associated with Bart-Pumphrey syndrome. Unlike post-infectious or autoimmune forms of hearing loss and nail disease, BPS manifests as a congenital or early-onset condition in the context of familial autosomal dominant inheritance, and there is no evidence that bacterial, viral, fungal, or parasitic pathogens trigger or mimic the full BPS phenotype.[1][4][5][7][14]  

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestations

The pathophysiology of Bart-Pumphrey syndrome can be conceptualized as a sequential causal chain connecting the initiating genetic lesion to the clinical phenotype. In concise form, the sequence is as follows: (1) heterozygous missense mutations in *GJB2* encoding connexin 26 alter the structure and biophysical properties of gap junction channels in cochlear supporting cells and epidermal keratinocytes;[1][3][5][18] (2) these mutant connexin 26 monomers co-assemble with wild-type connexin 26 (and potentially other connexins) into hexameric hemichannels, exerting dominant-negative effects that reduce functional gap junction coupling and may also produce aberrant hemichannels with pathological gating;[5][17][18] (3) in the cochlea, impaired gap junction communication disrupts potassium ion recycling and homeostasis in the organ of Corti and surrounding structures, leading to dysfunction and eventual loss of hair cells and auditory neurons, which results in congenital or early-onset sensorineural hearing loss;[3][16][17] (4) in the epidermis of the palms, soles, and dorsal finger/toe joints, defective gap junction signaling perturbs keratinocyte proliferation, differentiation, and response to mechanical stress, causing diffuse palmoplantar keratoderma and focal knuckle pads;[5][8][9] (5) in the nail matrix, altered connexin-mediated communication among keratinocytes and possibly nail bed fibroblasts leads to abnormal keratin deposition, producing leukonychia and nail dystrophy;[2][14] (6) the combined impact of these tissue-specific manifestations yields the characteristic clinical tetrad of BPS, with variable expressivity modulated by allele-specific effects and uncharacterized genetic or epigenetic modifiers.[2][5][7][16]  

Some steps in this sequence are directly demonstrated by experimental data, particularly the effects of *GJB2* mutations on gap junction function in cell culture and the role of connexin 26 in cochlear potassium recycling, whereas others (such as the precise mechanisms of knuckle pad formation) are inferred from broader knowledge of epidermal biology and connexin function.[17][18]  

### 6.2 Molecular Pathways and Connexin 26 Biology

Connexin 26 belongs to the connexin family of gap junction proteins that mediate intercellular communication by forming channels allowing diffusion of ions and small molecules between adjacent cells.[18][17] UniProt describes gap junction beta-2 protein as a multi-pass membrane protein located at the cell membrane and cell junction, forming hexameric hemichannels that dock to hemichannels on neighboring cells to create gap junctions.[18] These channels play crucial roles in coordinating cellular responses, maintaining tissue homeostasis, and supporting specialized functions such as cochlear potassium recycling and epidermal differentiation.[3][16][17]  

At the molecular pathway level, connexin 26 participates in processes implicated in hearing and skin homeostasis. In the cochlea, gap junction networks composed of connexin 26 and other connexins are essential for the K+ recycling pathway that shuttles potassium ions from hair cells into the supporting cells and then into the endolymph.[3][16][17] Disruption of this pathway leads to depolarization abnormalities and hair cell damage, a mechanism well established in *GJB2*-related hearing loss through animal models and human temporal bone studies.[17] In the epidermis, connexin 26 channels contribute to cell–cell signaling among keratinocytes, supporting coordinated differentiation and response to environmental stress; altered gap junction communication can therefore affect keratinocyte proliferation, apoptosis, and differentiation patterns.[8][17][18]  

Key molecular pathways influenced by connexin 26 dysfunction include ion homeostasis (particularly potassium), apoptotic signaling, and cell adhesion and differentiation programs. GO biological process terms relevant here include regulation of cell communication (GO:0010646), potassium ion transmembrane transport (GO:0071805), and keratinocyte differentiation (GO:0030216).[18][17] While canonical signaling cascades such as MAPK or PI3K-AKT may be secondarily affected by the loss of gap junction-mediated signaling, BPS is not primarily a disease of aberrant kinase signaling but rather of defective intercellular channel function.  

### 6.3 Cellular Processes: Cochlear and Epidermal Dysfunction

At the cellular level, Bart-Pumphrey syndrome involves disruption of specific processes in defined cell populations. In the inner ear, connexin 26 is expressed in supporting cells of the organ of Corti, including Deiters’ cells, pillar cells, and other non-sensory cells that form part of the cochlear epithelium.[16][17] These cells normally participate in potassium ion recycling and provide metabolic support to hair cells. Mutant connexin 26 channels reduce gap junction coupling among these cells, impairing K+ buffering and metabolic cooperation, which triggers hair cell dysfunction and death, culminating in sensorineural hearing loss.[3][16][17] This process involves cellular events such as impaired ion transport, excitotoxic stress, apoptosis of hair cells and neurons, and eventual degeneration of auditory pathways.  

In the epidermis, keratinocytes in the basal and suprabasal layers of palmar and plantar skin depend on gap junctions for synchronized differentiation and response to mechanical stress.[8][18] Mutant connexin 26 may alter calcium signaling and other second messenger exchange between keratinocytes, leading to abnormal proliferation of the stratum corneum (hyperkeratosis), focal nodular hyperplasia (knuckle pads), and changes in barrier function.[8][9] Cellular processes implicated include hyperproliferation, altered terminal differentiation, and potential localized fibrosis or extracellular matrix remodeling in knuckle pads, driven by chronic mechanical forces interacting with a genetically primed epidermis.  

In the nail matrix, epidermal-derived keratinocytes produce nail plate keratin and rely on gap junction-mediated coordination for orderly nail formation. Disrupted connexin 26 may lead to deposition of incompletely keratinized material with altered optical properties, manifesting as leukonychia and nail fragility.[2][14] Here, cellular processes include abnormal keratin packaging, subtle changes in protein composition, and altered microarchitecture of the nail plate.  

CL (Cell Ontology) terms relevant to BPS include keratinocyte (CL:0000075), nail matrix keratinocyte (a subtype of epidermal keratinocyte), cochlear hair cell (CL:0000007), and cochlear supporting cell (e.g., Deiters’ cell, CL terms for supporting cells of the inner ear).[16][17]  

### 6.4 Protein Dysfunction: Structural and Biophysical Effects

The structural and biophysical consequences of BPS-associated *GJB2* mutations focus on the connexin 26 protein. Connexin 26 has four transmembrane domains, two extracellular loops, one cytoplasmic loop, and intracellular N- and C-termini.[18][17] The first extracellular loop (E1) is particularly important for hemichannel docking and voltage gating, and many dominant *GJB2* mutations associated with syndromic deafness and skin disorders cluster in this region.[5][17] N54K, a substitution of asparagine by lysine at position 54, introduces a positively charged residue into an evolutionarily conserved domain, likely altering local structure and interactions required for channel formation.[5]  

Functional classification studies, though not specific to N54K in all cases, have shown that E1 mutants often impair gap junction plaque formation at the plasma membrane, reduce intercellular dye transfer, and cause aberrant hemichannel activity.[17] Some mutant connexin 26 proteins may form hemichannels that open abnormally in nonjunctional membrane regions, allowing uncontrolled flux of ions and small molecules, which can be cytotoxic.[17] Others may fail to traffic correctly to the membrane or fail to dock with partner hemichannels, resulting in reduced gap junction numbers.  

The overall protein dysfunction in BPS can therefore be summarized as a combination of misfolding, abnormal gating, and dominant-negative interference with wild-type connexin 26, ultimately reducing functional gap junction communication and possibly introducing harmful hemichannel activity.[5][17][18] UniProt notes that connexin 26 can form heteromeric channels with other connexins such as GJB4, suggesting that mutant connexin 26 could also perturb the function of these partners.[18]  

### 6.5 Metabolic Changes and Biochemical Abnormalities

The primary metabolic changes in Bart-Pumphrey syndrome relate to ion homeostasis in the cochlea rather than systemic metabolic derangements. Gap junction networks composed of connexin 26 and other connexins facilitate potassium recycling that is essential for hair cell transduction.[16][17] Disruption of this system leads to altered K+ gradients, hair cell depolarization abnormalities, and metabolic stress that ultimately cause hair cell death. This constitutes a specific biochemical abnormality at the level of ion channel and transporter function, rather than enzyme deficiency in classical metabolic disorders.  

In the skin and nail matrix, metabolic changes may include altered calcium signaling and second messenger distribution among keratinocytes, affecting differentiation and keratin synthesis.[8][18] However, these processes are not typically measured in clinical practice, and no specific blood or urine metabolic biomarker has been identified for BPS. BRENDA and other enzyme databases are not directly relevant to BPS, as the core defect lies in gap junction channel proteins rather than enzymatic pathways.  

Biochemical abnormalities can be broadly categorized under GO terms such as abnormal ion homeostasis in inner ear, but specific curated terms are limited. Connexin 26 dysfunction can be considered an “ion channel defect” in the sense that gap junction channels are specialized ion channels, and BPS is therefore part of the broader category of channelopathies affecting cochlear and epidermal physiology.[17][18]  

### 6.6 Immune System Involvement and Tissue Damage

Bart-Pumphrey syndrome is not primarily an immune-mediated disorder. There is no evidence of autoimmunity, immunodeficiency, or chronic inflammatory infiltrates driving the pathophysiology.[1][5][8][9] Histologic studies of palmoplantar keratoderma in hereditary conditions typically show hyperkeratosis, papillomatosis, acanthosis, and hypergranulosis, without distinctive inflammatory patterns.[8] Tissue damage in the cochlea arises from metabolic stress and ion imbalance rather than inflammatory or immune attack; the subsequent degeneration of hair cells and neurons can trigger secondary microglial responses, but these are not the initiating events.  

In the skin, repeated mechanical stress on a genetically predisposed epidermis may cause microtrauma and low-level inflammation contributing to knuckle pad formation, but no autoimmune features such as autoantibody deposition or immune cell infiltration have been documented as central to BPS.[8][9] Thus, immune system involvement in Bart-Pumphrey syndrome is minimal and secondary, and the disease is best classified under non-immune hereditary disorders affecting gap junction function.  

### 6.7 Epigenetic Changes and Molecular Profiling

Epigenetic mechanisms, such as DNA methylation or histone modification affecting *GJB2* expression, have not been directly studied in Bart-Pumphrey syndrome. Similarly, transcriptomics, proteomics, metabolomics, lipidomics, and multi-omics integration specific to BPS are not available in current data.[17] However, *GJB2* expression patterns in normal tissues have been profiled extensively in databases such as GTEx and Human Protein Atlas, confirming high expression in the cochlea and epidermis.[16][18] These expression patterns support the tissue specificity of BPS manifestations.  

Single-cell analyses of inner ear and skin have revealed complex cellular heterogeneity, including distinct subtypes of supporting cells and keratinocytes, but these studies have not focused on BPS. No functional genomics screens (CRISPR or RNAi) targeting *GJB2* in the context of BPS have been reported, although such approaches have been applied to study connexin function more broadly. For a disease knowledge base, it is therefore accurate to state that advanced molecular profiling data for Bart-Pumphrey syndrome are not currently available, and pathophysiologic understanding relies on classical molecular genetics and protein biology.  

### 6.8 Upstream vs Downstream Mechanisms

In the causal hierarchy, *GJB2* missense mutations represent the upstream initiating lesion.[1][5][14] Immediately downstream are protein-level dysfunctions of connexin 26, including misfolding, abnormal gating, dominant-negative interference, and disrupted assembly of gap junction channels.[5][17][18] Further downstream, tissue-specific consequences unfold: cochlear gap junction network failure leads to potassium recycling impairment and hair cell death; epidermal gap junction disruption leads to hyperkeratosis and knuckle pad formation; nail matrix dysregulation leads to leukonychia.[3][8][9][14][16]  

These tissue-level changes produce the clinical manifestations—hearing loss, palmoplantar keratoderma, knuckle pads, leukonychia—which then interact with environmental factors and psychosocial contexts to yield the full lived experience of BPS. Compensatory responses, such as upregulation of other connexins or remodeling of epidermal architecture, may represent intermediate downstream mechanisms that modulate severity but have not been fully characterized.[17][18]  

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

Bart-Pumphrey syndrome involves several organ systems, most prominently the auditory system and the integumentary system. The primary organ affected on the auditory side is the cochlea (UBERON:0001844), located in the inner ear and responsible for transducing mechanical sound vibrations into neural signals.[16][17] Sensorineural hearing loss in BPS reflects dysfunction of cochlear sensory epithelium and/or auditory nerve pathways.[3][14][16] Secondary auditory structures such as the auditory nerve and brainstem nuclei may be affected indirectly due to loss of peripheral input, but these are not primary sites of pathology.  

In the integumentary system, the primary sites are the skin of the palms (UBERON:0002387) and soles of the feet (UBERON:0002385), which exhibit diffuse keratoderma, and the dorsal aspects of the finger and toe joints (e.g., proximal interphalangeal joint region, UBERON:0001461), where knuckle pads develop.[8][9] Nails (UBERON:0001698), including fingernails and toenails, show leukonychia and occasionally thickening and crumbling.[2][14] Other skin sites may show mild hyperkeratosis or normal appearance, with BPS being predominantly an acral and nail-limited dermatosis.  

Body systems involved include the nervous system (specifically the sensory auditory system), the integumentary system (skin and appendages), and the musculoskeletal system insofar as knuckle pads overlie joints and may influence joint function or cosmetic appearance.[3][8][9][14] Cardiovascular, respiratory, digestive, and endocrine systems are not directly affected in Bart-Pumphrey syndrome, differentiating it from multi-organ syndromes with systemic involvement.  

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, cochlear sensory epithelium, including the organ of Corti, stria vascularis, and spiral ligament, is implicated in BPS-related hearing loss.[16][17] These tissues comprise hair cells, supporting cells, fibrocytes, and endothelium, with connexin 26 expressed mainly in supporting cells and non-sensory epithelium. CL terms representing key cochlear cell types include inner hair cell (CL:0000007), outer hair cell, Deiters’ cell, pillar cell, and other supporting cells. Loss of hair cell function and subsequent degeneration of auditory nerve fibers underpin the sensorineural component of hearing loss.[3][16][17]  

In the skin, palmoplantar keratoderma involves the epidermis, particularly the stratum corneum and underlying layers, and may also engage the dermis through secondary changes such as papillary dermal fibrosis.[8][9] Keratinocytes (CL:0000075) are the principal cell type affected, with abnormal proliferation and differentiation leading to thickened stratum corneum. In knuckle pads, localized hyperkeratosis and dermal fibroplasia occur over joints, implicating keratinocytes, fibroblasts (CL:0000057), and perhaps perivascular cells.  

In the nail unit, nail matrix keratinocytes and nail bed epithelium are involved in leukonychia. Nail matrix keratinocytes produce the nail plate; abnormal keratin deposition reflects dysregulated keratinocyte differentiation and protein synthesis. Nail bed connective tissue and vasculature may also contribute to optical properties of the nail, but the primary cellular defect is in keratinocytes.  

### 7.3 Subcellular Involvement

At the subcellular level, Bart-Pumphrey syndrome centers on connexin 26 protein localized to the plasma membrane at gap junction plaques and along nonjunctional membrane sites.[18][17] GO cellular component terms include gap junction (GO:0005921), plasma membrane (GO:0005886), connexon complex (GO:0005922), and cell junction (GO:0030054).[18] Mutant connexin 26 may mislocalize, fail to assemble correctly into connexon complexes, or form abnormal hemichannels at nonjunctional membrane, leading to altered trafficking and subcellular distribution.  

Other subcellular compartments involved include the endoplasmic reticulum (ER) where connexin 26 is synthesized and folded, Golgi apparatus where it is processed and trafficked, and lysosomes or proteasomes where misfolded proteins may be degraded. These compartments are indirectly implicated via the cellular quality control machinery responding to mutant connexin. However, the primary phenotypic consequences arise at the plasma membrane and gap junction plaques where cell–cell communication is lost or altered.[18][17]  

### 7.4 Localization and Lateralization

Anatomically, Bart-Pumphrey syndrome manifests bilaterally and symmetrically in many cases, particularly for hearing loss and palmoplantar keratoderma.[4][7][8] Sensorineural deafness in *GJB2*-related conditions is typically bilateral and symmetric, affecting both ears.[16][17] Palmoplantar keratoderma is usually bilateral and diffuse, involving both palms and both soles.  

Knuckle pads can be symmetric or asymmetric, localized to distal and interphalangeal joints of fingers and toes.[4][7][9] Orphanet notes that knuckle pads in BPS can be symmetric or asymmetric, which reflects variability in local mechanical stress and individual anatomical patterns.[7] Leukonychia tends to affect all fingernails and toenails, although degrees of whitening can vary between digits. Lateralization in the sense of unilateral vs bilateral disease is therefore minimal for the auditory and major cutaneous manifestations, with localized asymmetry mostly limited to knuckle pad distribution.  

## 8. Temporal Development

### 8.1 Onset Patterns

Bart-Pumphrey syndrome features different onset patterns across its core manifestations. Sensorineural hearing loss typically has congenital onset, present at birth or detected in early infancy during newborn hearing screening or early childhood evaluations.[4][5][7][14][16] Orphanet lists childhood as the age of onset for the syndrome, but the hearing component is clearly prelingual in many cases.[7][16] MedlinePlus states that the hearing loss associated with BPS is “typically present from birth,” aligning with a congenital pattern.[14]  

Palmoplantar keratoderma often appears in early childhood, with progressive thickening of the skin during the first years of life as mechanical stress interacts with genetically predisposed keratinocytes.[4][7][8] Knuckle pads usually develop in childhood or adolescence and may enlarge gradually over time.[4][8][9] Leukonychia may be evident from the time the nails fully develop in childhood, but in some individuals, nail whitening becomes more pronounced over time.  

The overall onset pattern of BPS can be described as chronic and insidious, with congenital auditory involvement and early childhood emergence of cutaneous features. There is no acute onset or episodic pattern; rather, manifestations evolve slowly and persist lifelong.  

### 8.2 Disease Progression, Staging, and Duration

In terms of progression, Bart-Pumphrey syndrome is a lifelong condition. Sensorineural hearing loss in *GJB2*-related conditions is typically stable or slowly progressive, depending on the specific variant.[16][17] Recessive DFNB1 often involves profound congenital loss that is non-progressive, whereas dominant *GJB2* variants can cause milder impairment that may progress.[17] For BPS specifically, data are limited, but reported cases generally describe hearing loss as present from birth and persistent, with occasional mention of progression.  

Palmoplantar keratoderma tends to progress during childhood and adolescence as the stratum corneum thickens, then stabilizes at a plateau in adulthood, with fluctuations based on mechanical stress and environmental factors.[8][9] Knuckle pads evolve gradually to a stable size; they are not known to regress spontaneously. Leukonychia is a stable trait, although nail dystrophy can evolve with age.  

Formal disease staging systems do not exist for BPS. Early-stage disease could be conceptualized as congenital hearing loss with mild keratoderma and subtle leukonychia, intermediate-stage as established palmoplantar keratoderma and visible knuckle pads in adolescence, and advanced-stage as fully expressed skin and nail findings with stable hearing impairment in adulthood. However, these stages are descriptive rather than standardized.  

Disease duration is lifelong; BPS does not remit spontaneously and remains present throughout adulthood. With supportive management, individuals can have normal life expectancy, as the syndrome does not involve life-threatening organ dysfunction.[2][7][16]  

### 8.3 Remission, Critical Periods, and Intervention Windows

Spontaneous remission of Bart-Pumphrey syndrome has not been reported. Cutaneous manifestations may fluctuate somewhat with treatment (e.g., topical agents, oral retinoids) and environmental conditions, but underlying genetic predisposition remains.[6][8] Hearing loss in BPS is not reversible; however, early intervention with hearing aids or cochlear implants can dramatically improve functional hearing and language development, representing a critical period for intervention.[16][17]  

Newborn screening for hearing loss provides an opportunity for early detection of *GJB2*-related deafness, including BPS, allowing timely audiological evaluation and genetic testing.[7][16] The first few years of life constitute a critical window during which language acquisition is maximally sensitive to auditory input; failure to intervene during this period may result in lasting delays. For skin manifestations, early dermatologic evaluation and initiation of keratoderma management can reduce pain and functional limitations, but there is no strict critical period analogous to that for hearing and language.  

## 9. Inheritance and Population

### 9.1 Epidemiology: Prevalence and Incidence

Bart-Pumphrey syndrome is an extremely rare disorder. Orphanet estimates the prevalence as <1 per 1,000,000 individuals worldwide, categorizing it as a rare disease.[2][7] Malacards similarly notes a point prevalence <1/1,000,000 globally, consistent with Orphanet’s assessment.[2] No incidence data (new cases per year) are available due to the rarity and lack of dedicated registries. Published cases since 1967 comprise only a handful of families and sporadic cases, underscoring the very low frequency of BPS in the general population.[1][4][5][6][11][12]  

Global Burden of Disease and national registries do not list BPS separately, and its contribution to overall hearing loss and dermatologic disease burden is negligible compared to more common etiologies. Nonetheless, as a prototypical *GJB2*-related syndromic deafness condition, BPS is important for understanding connexin biology and for differential diagnosis in families with similar phenotypes.  

### 9.2 Inheritance Pattern and Genetic Features

Bart-Pumphrey syndrome is inherited in an autosomal dominant manner.[1][4][5][7][11][12][14] OMIM explicitly states that BPS is autosomal dominant, and the multigeneration pedigrees support vertical transmission with affected individuals in successive generations.[1][5] Bart and Pumphrey’s original report documented dominant inheritance of knuckle pads, leukonychia, and deafness in a single family.[11][12] Marques-de-Faria et al. reported male-to-male transmission in a father–son pair, reinforcing autosomal dominant inheritance and ruling out X-linked transmission.[4]  

MedlinePlus Genetics notes that BPS is inherited in an autosomal dominant pattern, meaning one copy of the altered gene is sufficient to cause the disorder, and that in most cases, an affected person has one affected parent.[14] New de novo mutations can occur, leading to BPS in individuals without family history, although specific de novo cases are not extensively documented due to limited numbers.[14]  

Penetrance at the level of the core phenotype (hearing loss plus at least one cutaneous manifestation) appears high, but penetrance of individual features such as leukonychia is incomplete, given reports of mutation carriers with palmoplantar keratoderma and knuckle pads but no leukonychia.[4][5][2] Expressivity is clearly variable, with differing severity and combinations of skin and nail findings among carriers of the same variant.[5][2][7] There is no evidence of genetic anticipation or repeat expansion in BPS; the disorder results from point mutations rather than unstable repeats.[1][5]  

Germline mosaicism has not been reported specifically for BPS, but as with many autosomal dominant disorders, germline mosaicism in a parent could theoretically explain multiple affected offspring in the absence of parental phenotype. Founder effects have not been identified for BPS-associated variants; N54K and other missense alleles have been reported in single families or small series, without evidence of population clustering.[5][2]  

Carrier frequency in the general population is extremely low for BPS-specific *GJB2* variants, consistent with the rarity of disease. By contrast, carrier frequency for common truncating *GJB2* variants causing recessive nonsyndromic deafness (e.g., c.35delG) can be relatively high in specific populations, but these alleles do not cause BPS in heterozygous state.[17] Consanguinity is not a major factor in BPS, which is dominant; however, it is relevant for recessive *GJB2* conditions.  

### 9.3 Population Demographics and Geographic Distribution

Reported Bart-Pumphrey syndrome families have come from diverse geographic regions, including Northern Europe (family studied by Richard et al.), Poland, Brazil, and sporadic cases in other countries, suggesting no strong ethnic or regional predilection.[4][5][6] *GJB2* mutations more broadly have variable distribution, with the c.35delG founder mutation common in European ancestry populations, c.235delC prevalent in East Asian populations, and other variants specific to particular groups.[17] However, BPS-specific variants like N54K appear sporadic rather than concentrated.  

Sex ratio in BPS appears roughly equal, as autosomal dominant conditions typically affect males and females alike. The Marques-de-Faria father–son pair highlights male involvement.[4] Age distribution is biased toward detection in childhood and adolescence due to congenital hearing loss and early cutaneous manifestations, but adults remain affected throughout life.  

No epidemiologic study has quantified the geographic distribution of BPS variants, and given the extremely low prevalence, differences between populations may reflect reporting bias rather than true variation. For a disease knowledge base, it is appropriate to describe BPS as a globally rare, pan-ethnic autosomal dominant syndrome without known population specificity.  

## 10. Diagnostics

### 10.1 Clinical Evaluation and Phenotypic Diagnosis

Diagnosis of Bart-Pumphrey syndrome is based on the recognition of its characteristic clinical tetrad in an individual or family: sensorineural hearing loss, palmoplantar keratoderma, knuckle pads, and leukonychia.[1][5][7][14] Clinical evaluation begins with a detailed history and physical examination. Audiological assessment using pure-tone audiometry and, in children, auditory brainstem response testing confirms the presence and degree of sensorineural hearing loss.[4][6][14]  

Dermatologic examination identifies diffuse or focal keratoderma on the palms and soles, often with a honeycomb appearance and possible fissuring.[8][9] Knuckle pads appear as well-defined papules or nodules over proximal and distal interphalangeal joints; they may be verrucous or smooth.[4][8][9] Nails are inspected for leukonychia, focusing on white discoloration, thickness, and crumbling.[1][2][14]  

Histopathologic examination of palmoplantar keratoderma, when performed, typically shows hyperkeratosis, papillomatosis, acanthosis, and hypergranulosis, consistent with hereditary PPK.[8] In knuckle pads, biopsy reveals hyperkeratosis and dermal fibroplasia. Pathology findings support the clinical diagnosis but are not specific to BPS; they help differentiate from other causes of hyperkeratotic lesions.  

MedlinePlus emphasizes that genetic testing for *GJB2* variants can confirm the diagnosis of BPS by identifying a causative mutation, particularly when the full tetrad is present or when features overlap with other *GJB2* syndromes.[3][14]  

### 10.2 Genetic Testing Strategies

Genetic testing is central to definitive diagnosis and involves analysis of the *GJB2* gene. Given the strong association between BPS and *GJB2*, single-gene testing of *GJB2* by sequencing all coding exons and flanking intronic regions is often sufficient when the clinical phenotype is classical.[1][5][14] Many laboratories offer *GJB2* sequencing as part of hereditary hearing loss panels or targeted tests listed in the Genetic Testing Registry (GTR), including detection of missense, nonsense, frameshift, and splice-site variants.  

In cases where clinical features overlap with other *GJB2* syndromes (KID, HID, Vohwinkel, PPK with deafness), broader gene panels for hereditary palmoplantar keratoderma and deafness may be considered, including *GJB2*, *GJB6*, *GJB4*, and other skin-related genes.[8][9][13][16] Whole exome sequencing (WES) or whole genome sequencing (WGS) may be useful when the phenotype is atypical or when initial gene panel testing is negative, although for classical BPS, targeted *GJB2* sequencing is usually sufficient.[13][17]  

Chromosomal microarray (CMA), karyotyping, FISH, and mitochondrial DNA testing are not indicated for BPS, as the disorder results from point mutations in a nuclear gene.[1][18] Repeat expansion testing is also unnecessary, since BPS does not involve trinucleotide repeat expansions.  

### 10.3 Omics-Based Diagnostics

Omics-based diagnostics such as RNA sequencing, proteomics, metabolomics, and epigenomics are not currently used in routine diagnosis of Bart-Pumphrey syndrome. Their potential use would be research-oriented, for example to study expression changes in *GJB2* and related genes in skin or inner ear, but clinical diagnosis relies on targeted genetic testing and classical clinical criteria.[17] Liquid biopsy approaches and tumor profiling are irrelevant to BPS, as it is not a cancer.  

### 10.4 Differential Diagnosis

Differential diagnosis for Bart-Pumphrey syndrome includes several hereditary palmoplantar keratoderma and deafness syndromes, especially those caused by *GJB2* mutations. Vohwinkel syndrome (OMIM 124500) features diffuse honeycomb palmoplantar keratoderma, starfish-shaped keratoses on dorsal extremities, pseudoainhum, and sensorineural deafness; knuckle pads can be present, and basal cell and squamous cell carcinomas may develop in lesions.[8][9] Keratitis–ichthyosis–deafness (KID) syndrome and hystrix-like ichthyosis–deafness (HID) involve more generalized ichthyosis and keratitis, with severe skin involvement and sensorineural deafness, but do not typically show leukonychia and knuckle pads in the characteristic BPS pattern.[5][8][13]  

Palmoplantar keratoderma with deafness syndrome (OMIM 148350) presents with diffuse transgradient PPK and progressive sensorineural deafness, often associated with *GJB2* variants such as delE42, N54H, G59A, R75Q, H73R, G130V, S183F, and R184Q.[8][13] BPS differs by its specific combination of knuckle pads and leukonychia. Pachyonychia congenita (mutations in keratin genes KRT6A/6B/16/17) features diffuse PPK, nail changes, and oral leukokeratosis, but hearing loss is not a defining feature.[8]  

Idiopathic or familial knuckle pads without hearing loss or leukonychia must also be distinguished; these can be non-syndromic and not linked to *GJB2*.[9] Finally, acquired leukonychia due to trauma, systemic illness, or nutritional deficiencies must be excluded. The presence of autosomal dominant sensorineural deafness, palmoplantar keratoderma, knuckle pads, leukonychia, and a pathogenic *GJB2* variant strongly supports BPS over other entities.[1][2][5][7][14]  

### 10.5 Screening

Screening for Bart-Pumphrey syndrome per se is not performed in the general population, given its extreme rarity. However, newborn hearing screening programs universally test for congenital hearing loss, which can detect *GJB2*-related deafness including BPS.[7][16] When congenital hearing loss is identified, genetic evaluation may include *GJB2* testing, thereby uncovering BPS in families with cutaneous features. Carrier screening for *GJB2* mutations is done in some populations for recessive deafness alleles, but such programs do not typically target BPS-specific missense variants.  

Cascade screening of relatives in a family with known BPS is advisable: once a pathogenic *GJB2* variant is identified, testing of at-risk family members helps clarify their genetic status, enabling anticipatory guidance and early intervention for hearing loss. Preimplantation genetic diagnosis (PGD) and prenatal testing could be offered to families desiring to avoid passing on the mutation, consistent with standard practice for autosomal dominant disorders.[14][16]  

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

Bart-Pumphrey syndrome is not associated with increased mortality or reduced life expectancy. Neither OMIM, Orphanet, nor case reports describe life-threatening complications or elevated mortality risk attributable to BPS.[1][4][5][7][11][12] The organ systems affected—hearing and skin—impact quality of life but not vital function. Orphanet notes that BPS is a rare deafness syndrome but does not indicate decreased survival.[7]  

Thus, individuals with BPS who receive appropriate audiologic and dermatologic care can expect normal lifespan, barring unrelated comorbidities. Five-year and ten-year survival rates would be expected to match those of the general population for similar demographic profiles.  

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in BPS primarily reflects hearing impairment and palmoplantar keratoderma. Sensorineural hearing loss constitutes a significant disability, affecting communication, education, employment, and social integration.[4][14][16] Global Burden of Disease studies highlight hearing loss as a major contributor to years lived with disability, although BPS-specific contributions are small due to rarity.  

Palmoplantar keratoderma can cause chronic pain, especially from fissures on the soles, limiting mobility and occupational activities.[8][9] Knuckle pads and leukonychia are more cosmetic but may contribute to psychological distress. Overall disability outcomes depend on severity of hearing loss and keratoderma, access to assistive devices (hearing aids, cochlear implants), and availability of dermatologic care.  

Although no BPS-specific quality of life studies using SF-36 or EQ-5D exist, extrapolation from hereditary PPK and congenital deafness suggests moderate impairment, particularly in physical functioning and social domains, which can be ameliorated by early intervention.[8][16]  

### 11.3 Disease Course and Complications

The disease course in Bart-Pumphrey syndrome is chronic and relatively stable after early development. Major complications include language delay and educational difficulties if hearing loss is not addressed in childhood.[4][14][16] Skin complications involve painful fissures, secondary infections in cracks, and rare limitations in mobility due to severe keratoderma.[8][9] Knuckle pads may interfere slightly with joint movement or cause discomfort when gripping objects, but severe functional limitation is uncommon.  

Systemic complications such as organ failure or malignancy are not characteristic of BPS. Some *GJB2* syndromes like Vohwinkel syndrome can be associated with skin cancers arising in keratotic lesions, but this has not been reported specifically in BPS.[9] Secondary psychosocial complications, such as social isolation or depression related to deafness, may occur but are not systematically studied.  

### 11.4 Prognostic Factors

Prognostic factors in Bart-Pumphrey syndrome center on the severity of hearing loss and skin disease, and the timing and adequacy of interventions. Individuals with milder hearing impairment and early access to hearing aids or cochlear implants generally have better language development, educational attainment, and psychosocial outcomes.[16][17] Those with severe hearing loss and delayed intervention may experience persistent communication barriers.  

Skin prognosis depends on responsiveness to treatment. JAMA Dermatology notes that oral retinoids can improve skin symptoms in BPS, suggesting that individuals treated with such agents may have reduced keratoderma and fewer fissures.[6] Genetic variant type may also influence prognosis; missense variants with partial preservation of connexin function might cause milder phenotypes than those with severe dominant-negative effects. However, specific variant–prognosis correlations have not been systematically established for BPS due to small numbers.  

Prognostic biomarkers have not been identified for BPS beyond the *GJB2* genotype itself.  

## 12. Treatment

### 12.1 Pharmacological Management

Pharmacotherapy in Bart-Pumphrey syndrome is primarily directed at cutaneous manifestations, especially palmoplantar keratoderma. Oral retinoids, such as acitretin or isotretinoin, have been reported to improve skin symptoms in BPS by reducing hyperkeratosis and softening thickened skin.[6][8] JAMA Dermatology explicitly states that “Treatment with oral retinoids can improve the skin symptoms” in BPS, reflecting clinical experience with systemic retinoid therapy.[6] These agents act by modulating keratinocyte proliferation and differentiation via nuclear retinoic acid receptors, thereby decreasing hyperkeratosis.  

Topical keratolytic agents, including salicylic acid, urea, and lactic acid, can be used to reduce stratum corneum thickness on the palms and soles, while emollients help prevent fissuring.[8] Topical retinoids may also be applied, though their efficacy in palmar/plantar skin is limited compared to oral therapy.  

For knuckle pads, topical keratolytics and retinoids may yield modest improvement, but nodular lesions are often resistant to pharmacologic reduction.[8][9] In some cases, intralesional corticosteroids or other agents have been tried, but these interventions are not standardized and can risk scarring.  

Pharmacotherapy has limited role in managing hearing loss. No drugs specifically improve cochlear function in *GJB2*-related deafness. However, agents for otitis media or other comorbid ear conditions may be used as in general practice.  

NCIT (NCI Thesaurus) terms applicable to these interventions include “Retinoid” (NCIT:C804) for oral and topical retinoids, “Keratolytic Agent” (NCIT:C1222), and “Emollient” (NCIT:C28125).  

### 12.2 Advanced Therapeutics

Advanced therapeutics such as gene therapy and RNA-based approaches targeting *GJB2* are in early research stages for hearing loss but not yet clinically available for Bart-Pumphrey syndrome. Experimental gene therapy strategies for *GJB2*-related deafness using viral vectors to deliver wild-type *GJB2* to the cochlea have been explored in animal models, but no human clinical trials have been conducted specifically for BPS.[17] CRISPR-based editing of *GJB2* mutations is theoretically possible but remains speculative at present.  

Cell therapy, such as stem cell transplantation into the cochlea, is also under investigation for hearing loss more broadly, but not specific to *GJB2* or BPS.[17] RNA-based therapies, such as antisense oligonucleotides targeting specific mutant alleles, might be conceivable for dominant-negative variants, but such approaches have not yet reached clinical trials for *GJB2*.  

Given these limitations, advanced therapeutics are not currently part of BPS management, and treatment remains supportive and symptom-directed.  

### 12.3 Surgical and Audiologic Interventions

Audiologic interventions are crucial for managing hearing loss in Bart-Pumphrey syndrome. Hearing aids are appropriate for individuals with mild to moderate sensorineural loss, amplifying sound and improving communication.[16] In cases of more severe impairment, cochlear implants (NCIT:C15277) can be considered; these devices bypass damaged hair cells and directly stimulate the auditory nerve, providing substantial hearing improvement.[16][17]  

Early implantation in childhood allows better language acquisition and educational outcomes, underscoring the importance of prompt evaluation and intervention. Surgical placement of

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C1222` (1 mention) - the report calls it "Keratolytic Agent"; NCIT calls it **Miglustat**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C28125` (1 mention), reported as "Emollient" - NCIT does not contain this term

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `DO`.