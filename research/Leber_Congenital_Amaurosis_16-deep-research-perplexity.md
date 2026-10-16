---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T07:16:35.254744'
end_time: '2026-10-15T07:21:19.985355'
duration_seconds: 284.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Leber Congenital Amaurosis 16
  mondo_id: MONDO:0013613
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
citation_count: 58
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 23
  on_topic: 18
  validator_version: 0.3.0
term_validation:
  total_terms: 54
  verified: 49
  not_found: 0
  obsolete: 2
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 9
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0013613
    reported_labels:
    - MONDO
    ontology_label: Leber congenital amaurosis 16
  - term_id: DOID:0110118
    reported_labels:
    - Disease Ontology
    ontology_label: Leber congenital amaurosis 16
  - term_id: HP:0000639
    reported_labels:
    - Infancy; common/defining in published LCA16 cases
    ontology_label: Nystagmus
  - term_id: HP:0000662
    reported_labels:
    - Early childhood onward; common in reports
    ontology_label: Nyctalopia
  - term_id: HP:0000543
    reported_labels:
    - Later-stage
    ontology_label: Optic disc pallor
  - term_id: HP:0007843
    reported_labels:
    - Progressive; reported in several families
    ontology_label: Attenuation of retinal blood vessels
  labels_variant: 1
  obsolete_terms:
  - term_id: HP:0001146
    ontology_label: obsolete Pigmentary retinal degeneration
    replaced_by: HP:0000580
  - term_id: HP:0000487
    ontology_label: obsolete Congenital strabismus
    replaced_by: HP:0000486
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leber Congenital Amaurosis 16
- **MONDO ID:** MONDO:0013613 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leber Congenital Amaurosis 16** covering all of the
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

# Leber Congenital Amaurosis 16 (LCA16): comprehensive disease-characteristics report

**As-of date:** October 15, 2026  
**Target disease:** Leber congenital amaurosis 16  
**MONDO:** MONDO:0013613  
**Disease class:** Mendelian, inherited retinal dystrophy  
**Evidence scope:** Human case reports/small pedigrees, patient-derived iPSC-RPE models, engineered mouse models, and zebrafish models. Because LCA16 is exceptionally rare—apparently **<1% of LCA/EOSRD**—phenotype frequencies, penetrance estimates, epidemiology, and prognosis remain imprecise. [143][176]

---

## Executive summary

LCA16 is a severe, usually congenital or infantile, **autosomal-recessive retinal dystrophy caused by biallelic loss-of-function variants in *KCNJ13***. *KCNJ13* encodes Kir7.1, a tetrameric inwardly rectifying potassium channel concentrated in the apical processes of retinal pigment epithelial (RPE) cells. Loss of Kir7.1 impairs RPE membrane potential and subretinal potassium homeostasis, compromises photoreceptor-outer-segment phagocytosis, and initiates secondary mitochondrial dysfunction, oxidative stress, RPE disorganization, and rod-and-cone photoreceptor degeneration. [25][24][69]

The recognizable phenotype includes profound early visual impairment, congenital/infantile nystagmus, nyctalopia, severely reduced or absent rod-and-cone ERGs, progressive central and peripheral field loss, macular/RPE atrophy, dense or nummular pigment clumps—often prominent at the posterior pole—and cataract in some genotypes. A subset with the M2-domain p.Thr153Ile variant developed retinal neovascularization, diffuse leakage, fibrosis, and vitreous hemorrhage in adolescence. [55][56][58]

There is **no approved KCNJ13-directed treatment**. Care is supportive. HUB-101, an AAV5–*KCNJ13* gene-augmentation candidate, remained publicly listed as preclinical/IND-enabling as of September 2026, with no registered human trial identified. The strongest recent advance is a 2023 preclinical study in which silica-nanocapsule delivery of ABE8e corrected p.Trp53Ter in patient fibroblasts (47%) and iPSC-RPE (17%), restored Kir7.1 currents, and preserved ERG and OCT outcomes in an engineered mouse model. [33][244][256]

---

# 1. Disease information

## 1.1 Definition and overview

LCA16 is the *KCNJ13*-associated form of Leber congenital amaurosis: a severe, bilateral, early-onset retinal dystrophy characterized by profound visual impairment during the first year of life and markedly reduced or absent full-field electroretinographic responses. The disease primarily begins in RPE cells but secondarily causes degeneration of rods, cones, and downstream retinal circuitry. [3][13][66]

The discovery study identified homozygous *KCNJ13* variants in three affected individuals and concluded that they had “a similar early onset of visual loss, suggesting both impaired retinal development and progressive retinal degeneration, involving both rod and cone pathways.” [PMID: 21763485; published July 15, 2011](https://pubmed.ncbi.nlm.nih.gov/21763485/) [58]

## 1.2 Identifiers and terminology

| Resource | Identifier/name | Scope and qualification |
|---|---|---|
| MONDO | **MONDO:0013613** | Leber congenital amaurosis 16; defined as LCA caused by mutation in *KCNJ13*. [5] |
| OMIM phenotype | **614186** | Leber congenital amaurosis 16. [6] |
| OMIM gene | **603208** | *KCNJ13*. [9] |
| Orphanet | **ORPHA:65** | Umbrella Leber congenital amaurosis entry, not a unique LCA16 subtype code. [13] |
| ICD-10 | **H35.5** | Hereditary retinal dystrophy; umbrella mapping used by Orphanet for LCA. [186] |
| ICD-11 | **9B70** | Hereditary retinal dystrophies; umbrella mapping rather than an LCA16-specific code. [186] |
| MeSH | **D057130** | Leber Congenital Amaurosis; no separate LCA16 descriptor located. [181] |
| MedGen | **C3280062 / UID 481692** | Leber congenital amaurosis 16. [3][211] |
| Disease Ontology | **DOID:0110118** | LCA16 cross-reference reported in integrated disease resources. [4] |
| Gene | **HGNC:6259; NCBI Gene 3769; Ensembl ENSG00000115474** | *KCNJ13*. [106] |
| Protein | **UniProt O60928** | Kir7.1/inward rectifier potassium channel 13. [107] |

**Synonyms:** LCA16; Leber congenital amaurosis type 16; KCNJ13 Leber congenital amaurosis; Leber congenital amaurosis caused by mutation in *KCNJ13*; *KCNJ13*-related recessive retinopathy. [5][221]

## 1.3 Data provenance

The evidence is predominantly:

- **Aggregated disease-level resources:** OMIM, MONDO, Orphanet, ClinVar, GenCC/ClinGen-style gene–disease curation, GTR and GeneReviews.
- **Patient-level published evidence:** small pedigrees and case reports, generally with clinical ophthalmic examinations and germline sequencing.
- **Experimental evidence:** patient-derived iPSC-RPE, CRISPR knockout cells, heterologous electrophysiology, conditional/mosaic mice and mutant zebrafish.
- **Not established from routine EHR cohorts:** no large population-level EHR natural-history study specific to LCA16 was found.

---

# 2. Etiology

## 2.1 Disease-causal factors

The established cause is **biallelic germline pathogenic or likely pathogenic *KCNJ13* variants causing reduced or absent Kir7.1 function**. The gene–disease relationship is considered definitive for autosomal-recessive *KCNJ13*-related retinal dystrophy. [28][221]

Pathogenic mechanisms include:

- Premature termination and probable nonsense-mediated decay or severe truncation: p.Trp53Ter, p.Arg166Ter, p.Gln219Ter.
- Nonfunctional or markedly impaired channels despite protein production: p.Ile120Thr, p.Thr153Ile.
- Abnormal folding, localization, glycosylation or channel assembly: p.Leu241Pro and other missense alleles.
- Compound heterozygosity involving one missense and one truncating allele.

The p.Trp53Ter channel produced approximately a **30-mV depolarization and 85% reduction in inward current** in transfected cells; co-expression with wild-type protein did not exert a strong dominant-negative effect, supporting recessive loss of function. [PMID: 25921210; published May 20, 2015](https://pubmed.ncbi.nlm.nih.gov/25921210/) [376][379]

## 2.2 Risk and protective factors

| Factor class | Evidence for LCA16 |
|---|---|
| Biallelic pathogenic *KCNJ13* variants | Necessary and sufficient in established nonsyndromic cases; principal risk factor. |
| Family history | Increases prior probability, although an affected child may be the first recognized case in a family. |
| Parental consanguinity/shared ancestry | Increases the probability that both parents carry the same rare allele; several original families were consanguineous or from geographically restricted populations. [9][58] |
| Sex | No sex-specific risk has been demonstrated; autosomal inheritance predicts broadly equal susceptibility. |
| Age | Age determines manifestation and stage, not acquisition: disease usually manifests in infancy and progresses chronically. |
| Environmental, infectious, toxic or occupational exposure | No exposure is known to cause LCA16 or materially determine penetrance. |
| Protective genetic variants/modifiers | None validated. Heterozygous carriers of recessive loss-of-function alleles were clinically normal in the original families. [58] |
| Protective diet/lifestyle | No intervention prevents the genetic disease. General retinal-health advice is supportive, not proven disease-modifying. |

## 2.3 Gene–environment interaction

No human gene–environment interaction has been established. Oxidative challenge is a plausible **downstream stress amplifier**, not an initiating environmental cause. In *KCNJ13*-knockout human iPSC-RPE, tert-butyl hydroperoxide caused disproportionately increased oxidized glutathione and cell death, indicating that Kir7.1-deficient RPE is unusually vulnerable to oxidative stress. Whether ordinary diet, light, smoking, pollution or occupational exposures alter the human phenotype is unknown. [PMID: 36413373; published November 22, 2022](https://pubmed.ncbi.nlm.nih.gov/36413373/) [228]

---

# 3. Phenotypes

Because fewer than several dozen molecularly characterized patients have been described in detail, the frequencies below are qualitative and should not be interpreted as population estimates.

| Phenotype | Type and characteristics | Onset/course and observed frequency | Suggested HPO term | Functional/QoL impact |
|---|---|---|---|---|
| Severe bilateral visual impairment/blindness | Symptom/sign; acuity ranges from approximately 0.7 logMAR to no light perception in published cases | Congenital or before age 1; usually severe and progressive; defining/near-universal | HP:0000505 Visual impairment; HP:0001141 Severely reduced visual acuity | Major effects on mobility, reading, education, independence and employment |
| Nystagmus | Clinical sign, generally sensory | Infancy; common/defining in published LCA16 cases | HP:0000639 | Impairs fixation and acuity |
| Nyctalopia/poor dark adaptation | Symptom from rod dysfunction | Early childhood onward; common in reports | HP:0000662 | Difficulty navigating in dim light |
| Absent or profoundly reduced ERG | Electrophysiologic abnormality affecting scotopic and photopic responses | Early and usually persistent; defining | HP:0000512 Abnormal electroretinogram; consider HP term for absent rod-and-cone response | Objective evidence of severe global retinal dysfunction |
| Progressive visual-field constriction | Functional sign | Childhood/adulthood; progressive but variable | HP:0001123 Visual field defect; HP:0001133 Constriction of peripheral visual field | Mobility and orientation impairment |
| Macular/RPE atrophy | Structural sign on fundoscopy/OCT | May become conspicuous during childhood or after the first decade; very characteristic | HP:0007401 Macular atrophy; HP:0007722 RPE atrophy | Progressive central-vision loss |
| Dense, clumpy or nummular retinal pigmentation | Fundus sign at RPE level, often posterior-pole predominant | May be subtle early and increase with age; highly characteristic in reported cases | HP:0007703 Abnormal retinal pigmentation; HP:0001146 Pigmentary retinal degeneration | Marker of RPE disorganization and degeneration |
| Outer-retinal loss/disorganization | OCT/pathology sign | Progressive; reported repeatedly | HP:0000548 Cone-rod dystrophy or HP:0000510 Rod-cone dystrophy may be used only when clinically appropriate | Correlates with loss of useful vision |
| Optic-disc pallor | Fundus sign | Later-stage, reported in several families | HP:0000543 | Reflects advanced retinal/optic pathway dysfunction |
| Retinal-vessel attenuation | Fundus sign | Progressive; reported in several families | HP:0007843 | Marker of severe retinal degeneration |
| Cataract | Ocular complication | Juvenile to early adult onset; recurrent but genotype-dependent | HP:0000518 Cataract | Further reduces residual vision; surgically treatable |
| Myopia | Refractive abnormality | Childhood; reported in some patients | HP:0000545 Myopia | Correctable contributor to poor acuity |
| Strabismus | Ocular-motor sign | Infancy/early childhood in some patients | HP:0000486 Strabismus; HP:0000487 if congenital | Cosmetic, fixation and amblyopia implications |
| Retinal neovascularization/leakage | Vascular complication | Not universal; developed around age 17 in two p.Thr153Ile siblings | HP:0007856 Retinal neovascularization, if available locally | Risk of hemorrhage, fibrosis and further visual loss |
| Vitreous hemorrhage | Complication of neovascularization | Adolescence in a subset | HP:0011531 Vitreous hemorrhage | Acute additional visual loss; may require surgery |
| Cataract/neovascular glaucoma after intervention | Treatment/ocular complication | Reported in an intensively treated p.Thr153Ile patient | Corresponding cataract/glaucoma HPO terms | Additional morbidity |

The original p.Arg166Ter siblings had visual acuities of 2.0 logMAR bilaterally and 1.78/1.48 logMAR at ages 34 and 32; the p.Leu241Pro patient had 1.45 logMAR bilaterally, absent rod/cone ERGs at age 10, and severe field loss by age 33. [PMID: 21763485](https://pubmed.ncbi.nlm.nih.gov/21763485/) [58]

A 31-year-old compound heterozygote had childhood nystagmus, acuities of 20/400 and 20/200, bilateral cataract extraction, and striking macular pigment clumps with thickened/disorganized retina. [PMID: 27203561; published 2017](https://pubmed.ncbi.nlm.nih.gov/27203561/) [56][361]

### Quality-of-life evidence

No LCA16-specific validated QoL study was located. Across RP/LCA genotypes, patient interviews identify effects on vision-dependent activities of daily living, mobility and broader HRQoL. The ViSIO-PRO/ObsRO instruments assess visual symptoms, mobility, ADL and distal HRQoL; psychometric validation included 83 adult/adolescent patients and 22 caregivers of children. [PMID: 36847938; published April 2023](https://pubmed.ncbi.nlm.nih.gov/36847938/) [151][157]

---

# 4. Genetic and molecular information

## 4.1 Gene and protein

| Attribute | Value |
|---|---|
| Gene | *KCNJ13* |
| Full name | Potassium inwardly rectifying channel subfamily J member 13 |
| HGNC | HGNC:6259 |
| NCBI Gene | 3769 |
| Ensembl | ENSG00000115474 |
| OMIM gene | 603208 |
| Chromosome | 2q37.1 |
| Protein | Kir7.1; UniProt O60928 |
| Canonical structure | 360 amino acids; cytoplasmic N and C termini, two transmembrane domains, one pore/selectivity loop; functional homotetramer |
| Molecular function | Inward rectifier potassium channel activity, suggested GO:0005242 |
| Core process | Potassium ion transmembrane transport, GO:0071805; potassium ion transport, GO:0006813 |
| Principal compartment | Plasma membrane, GO:0005886; apical plasma membrane, GO:0016324; ion-channel complex, GO:0034702 |

Kir7.1 has low conductance, weak inward rectification, unusual external-potassium dependence, and preferential Rb⁺ permeability; its RPE localization adjacent to Na⁺/K⁺-ATPase supports potassium recycling and subretinal ion homeostasis. [109][320][323]

## 4.2 Reported LCA16-associated variants

The following table lists well-supported published biallelic variants, not every ClinVar submission or VUS.

| Variant, NM_002242.4 | Type/domain | Published zygosity and phenotype | Functional/classification evidence | Population data |
|---|---|---|---|---|
| c.158G>A, p.(Trp53Ter) | Nonsense, N-terminal cytoplasmic | Homozygous LCA16 | ClinVar pathogenic; truncation/mislocalization, approximately 85% current reduction; corrected by readthrough and base editing. [121][376] | Rare; exact current gnomAD AF not established here |
| c.314G>T, p.(Ser105Ile) | Missense | Compound heterozygous with p.Gln219Ter; LCA with pigment clumps | Reported disease-causing; absent from databases in original report | Absent from databases at publication |
| c.359T>C, p.(Ile120Thr) | Missense near pore/selectivity region | Homozygous in two unrelated Saudi patients with congenital vitreoretinal dystrophy and early cataract | Disease-causing/ClinVar record; channel reported to reach membrane but be inactive | Very rare; exact AF unavailable |
| c.431T>C, p.(Leu144Pro) | Missense, M2 | Homozygous severe early-onset retinal dystrophy in UAE families | Likely pathogenic based on segregation, extreme rarity and functional evidence; 2026 validation confirmed impaired current | 2 heterozygotes among 125,455 individuals; AF ≈0.0007971%. [84][135] |
| c.458C>T, p.(Thr153Ile) | Missense, M2 | Homozygous in two families; LCA with adolescent retinal neovascularization in older siblings | Damaging predictions; M2 inner-pore functional impairment; reported pathogenic/likely pathogenic | Rare; exact AF unavailable |
| c.496C>T, p.(Arg166Ter) | Nonsense | Homozygous in Middle Eastern siblings | Pathogenic; predicted loss of almost entire C-terminal intracellular segment; ClinVar pathogenic | gnomAD AF 1.30×10⁻⁵ in one 2025 WES report. [173] |
| c.655C>T, p.(Gln219Ter) | Nonsense | Compound heterozygous with p.Ser105Ile | Truncating, absent from databases in original report; disease-causing | Absent from databases at publication |
| c.722T>C, p.(Leu241Pro) | Missense, C-terminal β-sheet | Homozygous LCA16 | Pathogenic; predicted major conformational disruption; absent from controls in discovery report | Absent from 382 control chromosomes and contemporaneous databases |
| c.859T>C, p.(Ser287Pro) | Missense | Homozygous in later diagnostic cohorts | Reported likely pathogenic using PM2_supporting, PP1_moderate and PP3_strong | Rare; exact AF unavailable [225] |

The variants are **germline**, not somatic. Large structural variants, aneuploidies, repeat expansions and mitochondrial-DNA variants are not established causes of LCA16.

## 4.3 Allelic distinction from dominant disease

Heterozygous p.Arg162Trp and some other alleles cause **autosomal-dominant snowflake vitreoretinal degeneration**, not LCA16. Thus, variant-level mechanism matters: recessive loss-of-function alleles cause LCA16, whereas specific dominant alleles likely alter channel behavior through gain-of-function or dominant effects. [58][292]

## 4.4 Modifiers, epigenetics and chromosomal abnormalities

- **Modifier genes:** none validated.
- **Protective alleles:** none validated.
- **Epigenetic signature:** no reproducible disease-specific DNA methylation, histone or chromatin signature reported.
- **Large chromosomal abnormalities:** none established as a recurrent LCA16 mechanism.
- **Somatic mosaicism:** not established in human LCA16; experimentally engineered RPE mosaicism is used in mouse models.

---

# 5. Environmental information

No toxin, infection, radiation, nutritional deficiency, smoking, alcohol use or occupational exposure is known to cause LCA16. It is a monogenic inherited disorder.

Lifestyle recommendations—balanced diet, appropriate lighting, UV protection and avoidance of repeated eye pressing—are supportive and should not be represented as etiologic or proven disease-modifying interventions. [407][412]

No bacterial, viral, fungal or parasitic trigger has been identified; vaccination and antimicrobial prophylaxis are not disease-specific interventions.

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **Biallelic germline loss-of-function *KCNJ13* variants lead to absent, truncated, mislocalized or nonconducting Kir7.1 channels in apical RPE membranes.**
2. **Loss of Kir7.1 conductance leads to RPE depolarization and impaired potassium recycling/subretinal K⁺ homeostasis**, particularly during light-evoked changes in extracellular K⁺.
3. **Abnormal RPE ion homeostasis leads to impaired epithelial physiology and defective uptake/clearance of shed photoreceptor outer segments.**
4. **Phagosome accumulation and altered RPE metabolism lead to secondary mitochondrial enlargement/dysfunction and reduced ATP**; the causal direction from phagosome failure to mitochondrial dysfunction is supported temporally in zebrafish but remains partly inferred.
5. **Energy deficiency and disturbed intracellular potassium handling lead to oxidative stress and reduced stress tolerance**, with activation of antioxidant pathways followed by RPE cell death in advanced stages.
6. **RPE dysfunction/death leads to failure of trophic and metabolic support for adjacent rods and cones.**
7. **Loss of photoreceptor support results in progressive rod-and-cone dysfunction and photoreceptor degeneration**, producing extinguished ERGs, nyctalopia, visual-field loss and severe acuity reduction.
8. **RPE remodeling and migration result in dense/nummular pigment clumps, macular atrophy and OCT disorganization.**
9. **Branch—selected M2-domain variants:** severe RPE/retinal injury may lead to retinal vascular leakage, neovascularization, fibrosis and vitreous hemorrhage; the variant specificity of this branch remains incompletely demonstrated.

## 6.2 Protein and ion-transport defect

In normal RPE, extracellular K⁺ falls from about 5 mM to 2 mM following photoreceptor light activation. Kir7.1 conductance increases as extracellular K⁺ falls, helping stabilize the RPE membrane and subretinal ionic microenvironment. Patient p.Trp53Ter iPSC-RPE had a membrane potential of −30.6 ±3.7 mV versus −50.0 ±5.1 mV in controls and lacked the characteristic Rb⁺-sensitive Kir7.1 current. [PMID: 30686507; published January 24, 2019](https://pubmed.ncbi.nlm.nih.gov/30686507/) [24]

**Suggested GO terms**

- GO:0005242 — inward rectifier potassium channel activity  
- GO:0071805 — potassium ion transmembrane transport  
- GO:0006813 — potassium ion transport  
- GO:0055085 — transmembrane transport  
- GO:0042391 — regulation of membrane potential  
- GO:0005886 — plasma membrane  
- GO:0016324 — apical plasma membrane  
- GO:0034702 — ion-channel complex  

## 6.3 Phagocytosis and RPE architecture

Patient-derived p.Trp53Ter iPSC-RPE took up substantially fewer photoreceptor outer segments than controls—66.5 ±7.4 versus 169 ±40 after short-term feeding—and processed fewer after prolonged digestion, 80.2 ±11.1 versus 244.2 ±27.6 per sampled field. CRISPR-knockout hiPSC-RPE also showed defective cell alignment and phagocytosis. [PMID: 30686507](https://pubmed.ncbi.nlm.nih.gov/30686507/)[PMID: 32437550](https://pubmed.ncbi.nlm.nih.gov/32437550/) [17][24]

**Suggested GO terms:** GO:0006909 phagocytosis; GO:0038096 Fc-receptor-independent phagocytosis where appropriate; GO:0045494 photoreceptor-cell maintenance; GO:0007043 cell–cell junction assembly.

## 6.4 Mitochondrial and metabolic changes

In *kcnj13* p.Phe168Leu zebrafish, RPE phagosomes accumulated before visible retinal degeneration. At six months, mitochondria were increased 5.5-fold and ATP was reduced 26.2%; at 12 months, mitochondria were increased 6.4-fold, ATP remained reduced, and extensive retinal thinning and degeneration were present. The authors concluded:

> “We propose that the retinal disease in this model is primarily a failure of phagosome physiology with a secondary mitochondrial dysfunction.”

[PMID: 30846767; published March 7, 2019](https://pubmed.ncbi.nlm.nih.gov/30846767/) [69]

**Suggested GO terms:** GO:0007005 mitochondrial organization; GO:0046034 ATP metabolic process; GO:0006091 generation of precursor metabolites and energy; GO:0006979 response to oxidative stress.

## 6.5 Oxidative stress and RPE death

*KCNJ13*-knockout human RPE showed:

- Dead cells: 7.51% versus 1.68% in wild type.
- Dead cells at protrusions: 58.10% versus 1.11%.
- Total glutathione: 6.36 versus 1.60 µmol/L.
- Increased *CAT*, *GPX4* and *GSR* expression.
- Greater oxidized-glutathione accumulation and death after oxidative challenge.

These results support increased oxidative stress and reduced oxidative-stress tolerance, although the exact link from K⁺ accumulation to mitochondrial ROS remains inferred. [PMID: 36413373](https://pubmed.ncbi.nlm.nih.gov/36413373/) [74]

Suggested terms: GO:0006979 response to oxidative stress; GO:0008219 cell death; GO:0097300 programmed necrotic cell death; GO:0006915 apoptotic process, where demonstrated.

## 6.6 Immune involvement

LCA16 is not autoimmune or primarily inflammatory. Reactive Müller-cell GFAP expression in zebrafish indicates secondary retinal stress/gliosis. No consistent systemic immune abnormality is reported. Microglial or inflammatory activation may accompany degeneration but has not been established as an upstream cause.

## 6.7 Molecular profiling and advanced technologies

| Technology | Evidence status |
|---|---|
| Bulk transcript/qPCR | Altered oxidative-stress genes, mitochondrial genes and stress markers in knockout RPE/zebrafish |
| Proteomics | No disease-specific large-scale human proteomic signature identified |
| Metabolomics/lipidomics | No validated patient diagnostic signature; ATP/glutathione changes shown experimentally |
| Single-cell RNA sequencing | No definitive LCA16 patient-retina single-cell atlas found |
| Spatial transcriptomics | No LCA16-specific study found |
| Multi-omics | No validated integrated human LCA16 analysis found |
| CRISPR functional genomics | CRISPR knockout iPSC-RPE, mosaic/conditional mice and mutation-specific base editing have been used |
| iPSC disease modeling | Strong evidence: patient-specific and engineered hiPSC-RPE reproduce electrophysiologic and phagocytic defects |

**Cell Ontology suggestions:** CL:0002586 retinal pigment epithelial cell; CL:0000210 photoreceptor cell; rod photoreceptor cell, cone photoreceptor cell, Müller glial cell and retinal bipolar neuron terms should be mapped to the current CL release.

---

# 7. Anatomical structures affected

| Level | Structures/cells | Ontology suggestions |
|---|---|---|
| Primary organ | Eye, bilaterally | UBERON:0000970 eye |
| Primary tissue | Retina | UBERON:0000966 |
| Initiating tissue | Retinal pigment epithelium/pigment epithelium of eye | UBERON:0007625; CL:0002586 |
| Secondary tissue | Neural retina | UBERON:0003902 |
| Principal secondary cells | Rod and cone photoreceptors | CL photoreceptor subclasses |
| Later secondary cells | Bipolar neurons and Müller glia/reactive retinal glia | Current CL bipolar-neuron and Müller-glial terms |
| Retinal layers | Photoreceptor outer segments, outer nuclear layer, outer plexiform layer; later inner nuclear layer | UBERON retinal-layer terms; parent UBERON:0001781 |
| Macula/posterior pole | Frequent site of dense pigmentation and atrophy | UBERON macula term where supported |
| Optic disc and vessels | Pallor and vascular attenuation; neovascularization in a subset | UBERON optic-disc and retinal-blood-vessel terms |
| Subcellular sites | Apical plasma membrane, ion-channel complex, phagosomes, mitochondria, cell junctions | GO:0016324, GO:0034702, GO:0031410, GO:0005739 |

Disease is **bilateral**. Marked unilateral asymmetry can occur in complications, such as unilateral vitreous hemorrhage or no-light-perception vision, but the inherited retinal dystrophy itself affects both eyes.

No consistent kidney, brain, endocrine or other systemic phenotype is established in recessive LCA16 despite Kir7.1 expression outside the eye.

---

# 8. Temporal development

| Stage | Typical findings |
|---|---|
| Congenital/infantile | Poor vision, nystagmus, strabismus or poor fixation; severely reduced ERG |
| Early childhood | Nyctalopia, severe acuity impairment; fundus may initially be less striking than functional loss |
| Later childhood/first decade | Increasing RPE pigmentation, macular atrophy, vessel attenuation and outer-retinal disorganization |
| Adolescence | Continued visual-field/acuity loss; cataract in susceptible genotypes; possible retinal leakage/neovascularization with p.Thr153Ile |
| Adulthood | Dense pigmentary maculopathy, severe central/peripheral loss, cataract or prior cataract surgery; some individuals retain limited residual vision |

The course is **chronic and lifelong**, usually progressive but variable. The p.Leu241Pro proband reported only mild progression between childhood and age 33, whereas other patients progressed to counting-fingers or no-light-perception vision. [58]

There is no spontaneous remission. Cataract extraction or treatment of neovascular complications may improve or preserve the non-retinal component of vision but does not reverse the underlying dystrophy.

**Critical therapeutic window:** biologically, treatment is most likely to help while RPE and photoreceptors remain structurally viable. This is inferred from retinal gene-therapy principles and animal rescue, not yet demonstrated clinically in LCA16.

---

# 9. Inheritance and population characteristics

## 9.1 Inheritance

- **Mode:** autosomal recessive.
- **Typical recurrence risk:** if both parents are heterozygous carriers, each pregnancy has a 25% chance of an affected child, 50% chance of an unaffected carrier and 25% chance of an unaffected non-carrier.
- **Penetrance:** appears high for individuals with two severe pathogenic alleles, but precise estimates are unavailable.
- **Expressivity:** variable, including age of cataract, rate of progression and vascular complications.
- **Anticipation:** not expected and not reported.
- **Germline mosaicism:** not reported; residual theoretical risk remains when apparently de novo variants are found.
- **Consanguinity:** increases risk by increasing homozygosity for rare familial alleles.
- **Heterozygotes:** carriers of recessive loss-of-function variants were clinically normal in the original pedigrees. [58]
- **Founder effects:** possible for individual variants in geographically restricted or consanguineous populations, but no global founder mutation is established.

## 9.2 Epidemiology

LCA overall occurs in approximately **1 in 30,000–81,000 births**, or roughly 1.2–3.3 per 100,000, accounts for about 5% of inherited retinal dystrophies, and has historically contributed substantially to childhood blindness. [136][138]

LCA16-specific prevalence and incidence are unknown. Current clinical summaries place *KCNJ13* at **<1% of all LCA/EOSRD**, implying an extremely low prevalence, likely far below 1 per 100,000. [143][176]

No reliable sex ratio, carrier frequency, or annual incidence has been calculated. Cases have been reported in Middle Eastern/Jordanian, Saudi Arabian, European, French and Emirati families, demonstrating worldwide potential rather than geographic restriction. Consanguinity can elevate local prevalence. [58][84][392]

---

# 10. Diagnostics

## 10.1 Clinical diagnostic approach

1. **History and examination:** congenital/infantile bilateral poor vision, nystagmus, nyctalopia, family history and consanguinity.
2. **Best-corrected visual acuity and refraction.**
3. **Dilated retinal examination and color photography:** look for macular atrophy, dense/nummular pigment, vessel attenuation and optic-disc pallor.
4. **Full-field ERG:** profoundly reduced or nonrecordable scotopic and photopic responses support LCA; normal ERG makes classic LCA unlikely. [196]
5. **OCT:** outer-retinal loss, disorganization, RPE/Bruch-membrane abnormalities, unusual retinal thickening or hyperreflective deposits.
6. **Fundus autofluorescence:** maps RPE health and residual retina.
7. **Fluorescein angiography:** particularly important in older patients with M2-domain variants or symptoms suggesting leakage/neovascularization.
8. **Molecular confirmation:** two pathogenic/likely pathogenic *KCNJ13* alleles in trans.

There is no routine blood chemistry, enzyme assay or circulating biomarker diagnostic for LCA16.

## 10.2 Genetic testing strategy

| Test | Utility |
|---|---|
| Inherited retinal-dystrophy/LCA multigene panel including *KCNJ13* | Preferred initial molecular test because clinical overlap among LCA genes is extensive; should include copy-number analysis where possible |
| Exome sequencing | Appropriate if panel is negative, phenotype is atypical, or a broader syndromic differential remains |
| Genome sequencing | Useful after negative panel/exome for deep-intronic, regulatory or structural variants; specific incremental yield for LCA16 is unknown |
| Single-gene *KCNJ13* sequencing | Reasonable when the dense pigment-clump phenotype is highly suggestive or for familial variant testing; GTR lists complete coding-region Sanger testing. [211] |
| Segregation testing | Confirm variants are in trans and identify carriers |
| Chromosomal microarray | Not first-line for classic isolated LCA16; consider with developmental anomalies or suspected CNV |
| Karyotype/FISH | Not routinely indicated |
| mtDNA testing | Not routinely indicated for classic LCA16 |
| Repeat-expansion testing | Not indicated |
| RNA sequencing | Research/second-line tool for suspected splice or deep-intronic variants; not a standard LCA16 diagnostic |
| Prenatal/PGT testing | Available once familial pathogenic variants are known |

The GTR LCA panel includes *KCNJ13* along with other LCA genes. [212]

## 10.3 Differential diagnosis

| Differential | Distinguishing points |
|---|---|
| Other nonsyndromic LCA/EOSRD genes—*GUCY2D, CEP290, CRB1, RPE65, AIPL1, RDH12, LCA5, RPGRIP1*, etc. | Molecular testing required; fundus/OCT patterns may guide but are not definitive |
| Achromatopsia | Cone ERG absent but rod responses preserved; photophobia and color-vision defect predominate |
| Congenital stationary night blindness | Nonprogressive; characteristic electronegative ERG with preserved a-wave in common forms |
| Oculocutaneous/ocular albinism | Hypopigmentation, foveal hypoplasia, usually normal full-field ERG and chiasmal misrouting |
| RPE65-related LCA | May show early nyctalopia with comparatively preserved central structure and is eligible for voretigene if biallelic *RPE65*, not *KCNJ13* |
| Joubert/Senior-Løken/Alström syndromes | Neurologic, renal, metabolic or hearing manifestations |
| Infantile neuronal ceroid lipofuscinosis/peroxisomal disease | Progressive neurologic or systemic disease |
| Snowflake vitreoretinal degeneration | Usually autosomal dominant *KCNJ13* allele; vitreous degeneration, snowflake deposits and comparatively preserved vision rather than congenital profound blindness |

Orphanet lists retinitis pigmentosa, Alström, Joubert, Stargardt, Senior-Løken and infantile neuronal ceroid lipofuscinosis among important differentials. [203]

## 10.4 Screening

LCA16 is not included in standard biochemical newborn screening. Appropriate targeted screening includes:

- Cascade carrier testing in relatives after familial variants are known.
- Partner testing for known carriers.
- Prenatal diagnosis or preimplantation genetic testing.
- Early ophthalmic evaluation and molecular testing of at-risk newborn siblings.

---

# 11. Outcome and prognosis

No LCA16-specific mortality, five-year survival or life-expectancy study exists. Available evidence describes an isolated ocular disorder; deaths directly attributable to LCA16 have not been reported.

Visual prognosis is poor:

- Severe impairment is usually present before age one.
- Both central and peripheral function may deteriorate.
- Cataract, retinal neovascularization, fibrosis, hemorrhage or glaucoma can add potentially preventable morbidity.
- Useful residual vision varies by genotype and age; complete blindness is possible.
- Recovery of photoreceptors already lost is unlikely with current supportive care.

The principal disability involves mobility, reading, face recognition, education, employment and independent daily activities. Early educational, orientation/mobility and assistive-technology services can mitigate developmental and QoL consequences, but do not restore retinal function. [151][153]

Potential prognostic factors, not yet validated in formal models, include:

- Baseline OCT evidence of surviving outer retina/RPE.
- Residual ERG or visual-field function.
- Variant class and location.
- Cataract and treatable vascular complications.
- Age at future molecular intervention.

No validated circulating or molecular prognostic biomarker exists.

---

# 12. Treatment

## 12.1 Current standard care

| Intervention | Role | Suggested NCIt concept |
|---|---|---|
| Refraction and corrective lenses | Maximizes residual acuity | Corrective Lens Therapy |
| Low-vision rehabilitation, magnification and electronic aids | Improves reading/ADLs | Low Vision Rehabilitation |
| Orientation and mobility training | Improves safe navigation and independence | Occupational Therapy; Rehabilitation Therapy |
| Educational accommodations/Braille/assistive technology | Supports development and education | Supportive Care |
| Cataract surgery | Treats visually significant lens opacity where retinal potential remains | Cataract Surgery |
| Anti-VEGF, panretinal photocoagulation or vitrectomy | Case-specific management of neovascularization, leakage or vitreous hemorrhage | Antiangiogenic Therapy; Laser Photocoagulation; Vitrectomy |
| Amblyopia management | Appropriate in young children with asymmetric visual input | Amblyopia Therapy |
| Regular retinal surveillance | Detects progression and treatable complications | Ophthalmologic Examination |

GeneReviews recommends yearly acuity, refraction, slit-lamp examination, ophthalmoscopy and OCT, with visual-field/fundus imaging where feasible and ERG approximately every three to five years. [407][409]

There is no evidence-based LCA16-specific pharmacotherapy or pharmacogenomic prescribing guideline.

## 12.2 Approved gene therapy does not apply

Voretigene neparvovec-rzyl (Luxturna) is FDA-approved only for **confirmed biallelic *RPE65*-associated retinal dystrophy with viable retinal cells**. It is not a treatment for *KCNJ13*-LCA16. [421][422]

## 12.3 Experimental treatments

| Strategy | Evidence and outcome | Development status |
|---|---|---|
| NB84 translational readthrough | In p.Trp53Ter patient iPSC-RPE, restored full-length protein, hyperpolarized cells by approximately 26–30 mV and restored Rb⁺-sensitive Kir7.1 currents | In vitro proof of concept; not approved [PMID:30686507] |
| Lentiviral *KCNJ13* augmentation | Restored apical Kir7.1, membrane potential and current in patient iPSC-RPE; approximately 25% normal expression may be sufficient for substantial rescue | In vitro proof of concept |
| HUB-101 AAV5 gene augmentation | AAV5 carrying *KCNJ13* under an RPE-directed VMD2 promoter; dose-dependent RPE transduction reported preclinically | Preclinical/IND-enabling; FDA orphan and rare-pediatric-disease designations reported; no NCT identified as of September 2026. [254][256] |
| ABE8e base editing of p.Trp53Ter | 47% correction in patient fibroblasts, 17% in iPSC-RPE, restored current; up to 16.8% in mouse RPE with ERG/OCT preservation | Preclinical, mutation-specific [PMID:37561581] |
| Suppressor tRNA/readthrough approaches | Small-molecule readthrough, nonsense-mediated-decay inhibition and suppressor tRNAs restored aspects of channel function in experimental systems | Preclinical |
| RPE cell replacement | Conceptually attractive for advanced RPE loss but no LCA16-specific human efficacy evidence | Experimental/not registered for LCA16 |
| Antioxidant/metabolic therapy | Mechanistically plausible from cellular/zebrafish studies but no human efficacy data | Exploratory |

Key 2023 abstract quotation:

> “Editing in both patient fibroblasts (47%) and human induced pluripotent stem cell–derived RPE (LCA16-iPSC-RPE) (17%) showed minimal off-target editing. We detected functional Kir7.1 channels in the edited LCA16-iPSC-RPE.”

[PMID: 37561581; published October 2, 2023](https://pubmed.ncbi.nlm.nih.gov/37561581/) [33]

The 2023 base-editing study was encouraging but not equivalent to clinical safety: it used patient cells and an engineered mouse model, detected low-frequency bystander changes/indels, and could not use viable homozygous mice because complete biallelic loss was neonatal-lethal. [290]

---

# 13. Prevention

## 13.1 Primary prevention

The disease cannot be prevented by vaccination, diet or exposure avoidance. Reproductive options following molecular diagnosis include:

- Carrier testing of relatives.
- Testing reproductive partners.
- Preimplantation genetic testing for monogenic disease.
- Chorionic-villus or amniotic-fluid prenatal diagnosis.
- Use of donor gametes or other family-planning options.

## 13.2 Secondary prevention

- Early diagnosis in at-risk siblings.
- Prompt molecular testing to avoid diagnostic delay.
- Early low-vision/developmental intervention.
- Surveillance for cataract and, particularly for M2-domain disease, vascular leakage or neovascularization.

## 13.3 Tertiary prevention

- Treat cataract, amblyopia, glaucoma and retinal neovascular complications.
- Discourage repeated eye poking/pressing because it can contribute to keratoconus or ocular injury.
- Optimize illumination and mobility training.
- Provide psychosocial, educational and occupational support. [406][412]

No disease-specific vaccine, antimicrobial prophylaxis or preventive medication exists.

---

# 14. Other species and naturally occurring disease

| Species | Taxon/gene resource | Evidence |
|---|---|---|
| Human, *Homo sapiens* | NCBI Taxon 9606; *KCNJ13* Gene 3769 | Natural LCA16 and dominant snowflake vitreoretinal degeneration |
| Mouse, *Mus musculus* | Taxon 10090; *Kcnj13* Gene 100040591; MGI:3781032 | Engineered knockout, conditional knockout, mosaic and p.Trp53Ter models |
| Zebrafish, *Danio rerio* | Taxon 7955; *kcnj13* Gene 555691; ZFIN ZDB-GENE-070129-1 | Naturally isolated/experimental *obelix* p.Phe168Leu mutant used as a retinal model |
| Rat, *Rattus norvegicus* | Taxon 10116; *Kcnj13* Gene 94341 | Ortholog and physiologic studies; no established natural LCA16-equivalent disease |

Orthology is well conserved among human, mouse and zebrafish. [301][302][304]

No confirmed naturally occurring companion-animal breed disorder directly homologous to human *KCNJ13*-LCA16 was found in OMIA-oriented searches. Therefore:

- No VBO breed identifier is applicable.
- There is no zoonotic potential.
- There is no cross-species transmission; this is a genetic channelopathy, not an infection.

---

# 15. Model organisms and experimental models

| Model | Genotype/system | Phenotype recapitulated | Principal use and limitation |
|---|---|---|---|
| Patient-specific hiPSC-RPE | Homozygous p.Trp53Ter | Depolarization, absent Kir7.1 current, defective outer-segment phagocytosis; gross morphology initially preserved | Human genotype-specific mechanism and therapy testing; lacks whole-retina interactions |
| CRISPR *KCNJ13*-KO hiPSC-RPE | Frameshift/knockout | Cell misalignment, defective phagocytosis, oxidative vulnerability, death and protrusion | Dissects RPE-autonomous mechanisms; may not represent every missense allele |
| Heterologous CHO/HEK cells | Expressing mutant Kir7.1 | Channel current, localization, assembly and drug/editing rescue | High-throughput electrophysiology; not mature RPE |
| Mosaic CRISPR mouse | Patchy *Kcnj13* loss in RPE | Local photoreceptor degeneration over mutant RPE; reduced light response | Demonstrates RPE cell autonomy; mosaic and not a natural germline phenotype |
| RPE-conditional mouse | Best1/VMD2-Cre *Kcnj13* deletion | Progressive ONL loss, reduced/extinguished ERG, outer-plexiform and bipolar-cell changes | Strong tissue-specific model; timing and extent of Cre expression vary |
| Germline null mouse | Biallelic knockout | Embryonic or neonatal lethality depending on strain/model | Reveals extraocular developmental requirement but prevents straightforward adult retinal study |
| *Kcnj13* p.Trp53Ter/+ΔR mouse | Knock-in plus RPE disruption of wild-type allele | Reduced ERG c-wave and progressive retinal dysfunction | Used for mutation-specific ABE8e rescue; engineered compound state differs from human homozygosity |
| Zebrafish *obelix* | Homozygous c.502T>C, p.Phe168Leu | Phagosome accumulation, enlarged mitochondria, reduced ATP, retinal thinning and visual decline | Defines temporal mechanism and vasculature; degeneration is late-onset rather than congenital |
| Retinal organoid/spatial models | No mature standardized LCA16 platform identified | — | Potential future tool for RPE–photoreceptor interaction |

In conditional mice, outer-nuclear-layer loss reached approximately 15% at postnatal day 15 and 70% by two months, with detectable structural loss preceding major visual dysfunction. [PMID: 30009826; published July 25, 2018](https://pubmed.ncbi.nlm.nih.gov/30009826/) [271]

The mosaic model showed that RPE cells lacking Kir7.1 could survive while adjacent photoreceptors degenerated, and nearby wild-type RPE could locally preserve photoreceptors—strong evidence that the initiating lesion is RPE-autonomous. [274][275]

**Model resources:** MGI/IMSR/MMRRC for mouse alleles, ZFIN for *obelix/kcnj13*, and patient/CRISPR hiPSC-RPE repositories associated with the cited laboratories. MMRRC identifies mouse *Kcnj13* as NCBI Gene 100040591 and MGI:3781032. [306]

---

# Recent developments and expert assessment

## 2023–2024 priorities

1. **Nonviral base editing, 2023:** ABE8e mRNA/sgRNA silica nanocapsules corrected p.Trp53Ter with meaningful functional rescue and limited measured off-target activity in patient cells and mice. This is the strongest mutation-specific preclinical evidence. [PMID:37561581] [33]
2. **CRISPR VISION program, 2024:** investigators reported continued development of nonviral ocular genome-editing delivery, emphasizing restored Kir7.1 current in human iPSC-RPE and sustained ERG/retinal structure in mice. [438]
3. **Ion-channel/iPSC-RPE synthesis, November 27, 2024:** a review concluded that hPSC-RPE models have accelerated understanding of LCA16 and enabled readthrough and gene-augmentation rescue studies. [60][445]
4. **Clinical manufacturing, October 9, 2024:** Hubble Therapeutics selected Andelyn Biosciences to manufacture clinical-grade AAV for HUB-101. The program subsequently remained publicly described as preclinical/IND-enabling, not an enrolled human trial. [243][256]
5. **Ongoing mechanistic work:** developmental RPE loss in mice confirms that Kir7.1 is required both during retinal development and for long-term photoreceptor maintenance. [75][229]

## Overall expert interpretation

The evidence supports a coherent therapeutic rationale: LCA16 is monogenic, RPE-centered, recessive, and appears amenable to partial restoration of wild-type Kir7.1. Gene augmentation is potentially variant-agnostic and therefore applicable to more patients; base editing offers precise correction but is variant-specific and must address bystander/off-target edits, delivery coverage and durability. The principal translational uncertainty is whether treatment can restore function once extensive macular and photoreceptor atrophy is established. Early molecular diagnosis and quantitative OCT mapping of residual viable retina will therefore be central to eventual trial design.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 23 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 3 |
| Terms whose name was checked | 16 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013613` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Leber congenital amaurosis 16**
- `DOID:0110118` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **Leber congenital amaurosis 16**
- `HP:0000639` (1 mention) - the report calls it "Infancy; common/defining in published LCA16 cases"; HP calls it **Nystagmus**
- `HP:0000662` (1 mention) - the report calls it "Early childhood onward; common in reports"; HP calls it **Nyctalopia**
- `HP:0000543` (1 mention) - the report calls it "Later-stage"; HP calls it **Optic disc pallor**
- `HP:0007843` (1 mention) - the report calls it "Progressive; reported in several families"; HP calls it **Attenuation of retinal blood vessels**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001146` (obsolete Pigmentary retinal degeneration) (1 mention) - replaced by `HP:0000580`
- `HP:0000487` (obsolete Congenital strabismus) (1 mention) - replaced by `HP:0000486`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0034702` (3 mentions) - the report calls it "ion-channel complex"; GO calls it **monoatomic ion channel complex**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.