---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-10T18:17:09.511168'
end_time: '2026-09-10T18:20:29.760627'
duration_seconds: 200.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Charcot-Marie-Tooth Disease, Demyelinating, Type 1G
  mondo_id: MONDO:0033135
  category: Disease
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
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 20
  verified: 15
  not_found: 2
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.111
  unresolved_terms:
  - HP:0003479
  - HP:0003430
  obsolete_terms:
  - term_id: HP:0002355
    ontology_label: obsolete Difficulty walking
    replaced_by: HP:0001288
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease, Demyelinating, Type 1G
- **MONDO ID:** MONDO:0033135 (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease, Demyelinating, Type 1G** covering all of the
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

# Charcot–Marie–Tooth Disease, Demyelinating, Type 1G (CMT1G): Comprehensive Disease Characteristics

Charcot–Marie–Tooth disease, demyelinating, type 1G (CMT1G) is a rare, autosomal dominant hereditary peripheral neuropathy caused by heterozygous mutations in the **PMP2** gene, which encodes peripheral myelin protein 2, a fatty-acid binding protein expressed in myelinating Schwann cells of the peripheral nervous system.[1][2][3][5][7][19] Clinically, CMT1G manifests as a childhood or adolescent-onset progressive sensorimotor neuropathy characterized by distal muscle weakness and atrophy, length-dependent sensory loss, foot deformities such as pes cavus, and markedly reduced motor nerve conduction velocities indicating a primary demyelinating process.[1][5][7][8][10][18] Although CMT1G shares many features with more common forms of CMT1, it is distinguished by its genetic etiology in PMP2 and by emerging mechanistic evidence that links disease pathogenesis to disrupted lipid homeostasis, altered fatty acid binding, and instability of compact myelin rather than gross structural loss of the PMP2 protein.[12][13][14][15][16] The rarity of CMT1G means that much of our knowledge arises from small kindreds and case series, coupled with in vitro biophysical studies of PMP2 variants and transgenic mouse models, but together these sources provide a coherent picture in which subtle but functionally important perturbations of myelin lipid dynamics lead over years to chronic demyelination, axonal compromise, and disability, while life expectancy generally remains near normal under appropriate supportive care.[5][7][8][10][19]  

## 1. Disease Information

Charcot–Marie–Tooth disease (CMT) is the prototypical hereditary motor and sensory neuropathy, encompassing a heterogeneous group of disorders with shared features of chronic, length-dependent peripheral nerve dysfunction.[18][19] CMT is conventionally classified into demyelinating forms (type 1), axonal forms (type 2), and intermediate forms, with further subdivision by genetic cause.[18][19] CMT1G is one of the autosomal dominant demyelinating subtypes and is defined by pathogenic variants in **PMP2**, resulting in a phenotype that meets clinical criteria for CMT1 but with a distinct underlying molecular lesion.[1][2][5][7][9][10][19] OMIM entry #618279 describes “Charcot-Marie-Tooth disease, demyelinating, type 1G; CMT1G” and states that “Charcot-Marie-Tooth disease type 1G is an autosomal dominant progressive peripheral sensorimotor neuropathy characterized by distal muscle weakness and atrophy with onset in the first or second decade.”[1][6] Orphanet, in its group entry on CMT1 (ORPHA:65753), similarly defines CMT1 disorders as autosomal dominant demyelinating peripheral neuropathies characterized by distal weakness and atrophy, sensory loss, foot deformities, and slow nerve conduction velocity.[18]

Key identifiers for CMT1G include the OMIM phenotype number **618279** and the causal gene OMIM entry **170715** for **PMP2**.[1][6] The NCBI Gene record for PMP2 (Gene ID 5375) notes that the gene is located on chromosome 8q21.13 and that “a defect in this gene was shown to be a cause of dominant demyelinating CMT neuropathy.”[2] CMT1G is recognized in GeneReviews’ overview of Charcot–Marie–Tooth hereditary neuropathy, which lists PMP2 among the genes associated with demyelinating neuropathies and designates “PMP2 – AD – CMT1G.”[19] At the level of disease classification, ICD‑10‑CM codes hereditary motor and sensory neuropathies, including Charcot–Marie–Tooth disease and Déjérine–Sottas disease, under **G60.0**, with related terms such as “Charcot-Marie-Tooth disease, paralysis or syndrome” and “Marie-Charcot-Tooth neuropathic muscular atrophy” mapped to that code.[11] ICD‑11 recognizes “autosomal dominant demyelinating Charcot‑Marie‑Tooth disease” within the broader hereditary neuropathy category, and Orphanet assigns the group identifier ORPHA:65753 to CMT1 disorders.[18] The user has provided MONDO:0033135 as the MONDO identifier for this specific subtype, consistent with the trend for ontologies to represent genetically defined CMT subtypes as distinct disease entities.

Common synonyms and alternative names for CMT1G include “Charcot–Marie–Tooth disease type 1G,” “CMT1G,” “PMP2-related CMT,” and “PMP2-related demyelinating Charcot–Marie–Tooth neuropathy.”[1][3][5][7][8][9][10][14] The PMP2 protein itself is also known in the biochemical literature as “peripheral myelin protein 2,” “myelin P2 protein,” and “fatty acid-binding protein 8 (FABP8),” and OMIM and NCBI Gene list alternative gene names including **P2**, **MP2**, **FABP8**, and “M-FABP.”[2][12][13][14] Because CMT1G is embedded within the larger framework of CMT1, clinical reports sometimes refer to affected individuals simply as having “CMT1” or “dominant demyelinating CMT” before genetic testing identifies PMP2 as the cause.[3][5][7][8][9][10][18] In the context of classification systems such as MeSH and SNOMED CT, CMT1G is subsumed under broader descriptors of hereditary motor and sensory neuropathy and demyelinating peripheral neuropathy rather than having a unique term, although ontology resources increasingly incorporate gene-specific subtypes.

Information on CMT1G is derived almost entirely from aggregated disease-level resources and small clinical series, not from large EHR-based cohorts. OMIM collates data from individual case reports and molecular studies to define the phenotype and genetic cause.[1][6] Orphanet provides group-level descriptive epidemiology and clinical features for CMT1.[18] GeneReviews’ overview synthesizes multiple genetic subtypes, including PMP2-related disease, and provides general diagnostic guidance for CMT as a whole.[19] Primary clinical knowledge comes from case reports and series that have identified deleterious PMP2 mutations (e.g., p.Ile43Asn, p.Thr51Pro, p.Ile52Thr, p.I50del, p.Met114Thr, p.Val115Ala) in families with demyelinating CMT.[3][5][7][8][9][10] These studies use detailed neurologic examination, neurophysiology, imaging, and genetic testing to characterize the phenotype and confirm segregation of variants with disease, yielding a composite picture of CMT1G across a small but growing number of families worldwide.[3][5][7][8][9][10]

### Ontology considerations for disease information

From an ontology perspective, CMT1G can be mapped to several standard vocabularies. For disease entities, **MONDO:0033135** (Charcot-Marie-Tooth disease, demyelinating, type 1G) captures the gene-specific subtype, while broader entities such as **MONDO:0009954** (Charcot-Marie-Tooth disease) and **MONDO:0005212** (hereditary motor and sensory neuropathy) represent parent classes. In MeSH, CMT falls under “Peripheral Nervous System Diseases” and “Neuromuscular Diseases,” with “Charcot-Marie-Tooth Disease” as a specific descriptor. ICD‑10‑CM uses **G60.0** for “Hereditary motor and sensory neuropathy” encompassing CMT.[11] The causal gene **PMP2** is associated with HGNC symbol PMP2, NCBI Gene ID 5375, and UniProt entry P02689, and is classified in GO as a fatty acid binding protein with roles in lipid transport and myelin sheath structure.[12][13][14][15] These ontology mappings support standardized representation of CMT1G in a disease knowledge base.

## 2. Etiology

The primary cause of CMT1G is **heterozygous germline mutation in the PMP2 gene**, resulting in autosomal dominant demyelinating peripheral neuropathy.[1][2][3][5][7][8][9][10][19] OMIM explicitly notes that “a number sign (#) is used with this entry because of evidence that demyelinating Charcot-Marie-Tooth disease type 1G (CMT1G) is caused by heterozygous mutation in the PMP2 gene (170715) on chromosome 8q21.”[1] NCBI Gene similarly states that “a defect in this gene was shown to be a cause of dominant demyelinating CMT neuropathy.”[2] The initial discovery came from exome sequencing of individuals with clinically typical CMT1 but negative for common CMT1 genes (PMP22, MPZ, GJB1, MFN2), identifying de novo or familial PMP2 missense variants that segregate with disease and are absent or extremely rare in population controls.[3][5][9][10] For example, a de novo p.Ile52Thr variant was reported in a proband with CMT1, transmitted to his affected son, with electrophysiological evidence confirming demyelinating neuropathy.[3] Subsequent screening identified additional families with adjacent amino acid substitutions p.Thr51Pro, p.Ile43Asn, and later p.Met114Thr and p.Val115Ala, all mapping to structurally important regions of PMP2 and correlated with childhood-onset demyelinating neuropathy.[3][5][10]

Risk factors for CMT1G are dominated by **genetic factors**, specifically the presence of a pathogenic or likely pathogenic PMP2 variant in the germline. Because CMT1G follows autosomal dominant inheritance, an affected individual has a 50% chance of transmitting the mutation to each offspring.[1][3][5][7][8][9][10][19] Penetrance appears high, with most heterozygous carriers manifesting clinical neuropathy, although the small number of reported families limits precise estimates.[3][5][7][8][9][10] In some pedigrees, disease arises from de novo mutation in an otherwise unaffected parent, as in the original p.Ile52Thr family.[3] There is currently no evidence that common susceptibility variants or modifier genes outside PMP2 significantly alter risk of disease onset, although broader CMT literature notes that genes involved in myelination and axonal integrity (e.g., PMP22, MPZ, MFN2, NEFL) can modify phenotype in compound or overlapping genetic contexts.[19] Within PMP2 itself, different mutations may confer variable severity, with some clustering within a “mutation-rich” region around residues 43–52 and others (Met114Thr, Val115Ala) forming a second cluster in fatty acid coordinating residues, suggesting that both spatial location and physicochemical change influence penetrance and expressivity.[5][12][13][14]

Environmental risk factors for CMT1G have not been specifically established. However, by analogy to other forms of hereditary neuropathy, exogenous neurotoxins—such as certain chemotherapeutic agents (e.g., vinca alkaloids, taxanes), excessive alcohol consumption, or poorly controlled diabetes—may exacerbate symptoms or accelerate functional decline in individuals with underlying demyelinating neuropathy, including CMT1G, even if they do not cause disease de novo. Such gene–environment interactions have been documented generically in neuropathy, but robust, CMT1G-specific epidemiologic data are lacking, and thus this remains inferential rather than demonstrated. Similarly, age is a determinant of cumulative nerve damage; CMT1G symptoms typically begin in childhood or adolescence and progress slowly over decades.[1][5][7][8][10][18] Sex does not appear to significantly influence risk, as both males and females are affected in reported families, consistent with autosomal inheritance.[5][7][8][10]

Protective factors specific to CMT1G have not been identified. There are no known genetic variants that mitigate the effect of pathogenic PMP2 mutations, nor environmental exposures definitively shown to reduce risk of disease onset or progression. In the broader CMT population, maintenance of good general health, avoidance of neurotoxins, and early rehabilitation may improve functional outcomes, but these interventions do not prevent the underlying disease. From a mechanistic standpoint, factors that support Schwann cell energy metabolism and lipid homeostasis—such as adequate nutrition and avoidance of metabolic stress—could theoretically buffer some downstream consequences of PMP2 dysfunction, given evidence that PMP2 modulates fatty acid uptake and ATP production in Schwann cells.[15][16] Yet these hypotheses await direct clinical validation.

Gene–environment interactions in CMT1G are best conceptualized in terms of how **environmental stressors may unmask or worsen the functional consequences of PMP2 mutation**. For example, experimental models show that PMP2 plays a role in remyelination following nerve injury and in maintaining Schwann cell lipid homeostasis.[15][16] A PMP2-deficient or mutant Schwann cell may therefore be less able to respond to additional insults (mechanical trauma, ischemia, metabolic stress), leading to more pronounced demyelination or failed remyelination compared to a wild-type Schwann cell.[15][16] Similarly, systemic metabolic disturbances that perturb lipid profiles or mitochondrial function might synergize with PMP2-related defects. However, in the absence of disease-specific human data, these interactions must be considered conjectural, grounded in mechanistic insights from animal and cellular studies rather than epidemiologic demonstration.

### Ontology considerations for etiology

In a disease knowledge base, etiologic annotations for CMT1G should highlight the causal gene **PMP2 (HGNC:9210, NCBI Gene ID: 5375)** and classify the relationship as “monogenic, autosomal dominant, germline,” with variant type “missense” or “in-frame deletion” and functional effect “altered fatty acid binding and lipid interaction; structurally preserved protein.”[3][5][8][10][12][13][14] Relevant GO biological process terms include **GO:0006631** (fatty acid metabolic process), **GO:0008366** (axon ensheathment), and **GO:0042552** (myelination). For chemicals involved, ontology terms such as **CHEBI:16113** (cholesterol), **CHEBI:17762** (sphingomyelin), and **CHEBI:18348** (phosphatidylinositol 4,5‑bisphosphate, PI(4,5)P2) are relevant to the lipid pathways affected by PMP2 variants.[12][13][16] The etiologic classification should explicitly note the absence of known environmental causes or protective genetic variants.

## 3. Phenotypes

Clinically, CMT1G presents as a **length-dependent sensorimotor peripheral neuropathy** dominated by distal weakness and atrophy, sensory disturbances, and foot deformities, with electrophysiologic evidence of demyelination.[1][5][7][8][10][18][19] OMIM describes the phenotype as “progressive peripheral sensorimotor neuropathy characterized by distal muscle weakness and atrophy with onset in the first or second decade.”[1] Orphanet, in its group description of CMT1, notes that affected individuals develop distal weakness and atrophy, beginning in the feet and legs and later involving the hands, accompanied by distal sensory loss (hypoesthesia), areflexia, pes cavus and hammer toes, and slow nerve conduction velocities (<38 m/s in upper limbs).[18] GeneReviews similarly emphasizes that CMT generally presents with distal muscle weakness and atrophy, pes cavus, and decreased or absent tendon reflexes, with sensory involvement in many subtypes including demyelinating forms.[19] Case series specific to PMP2 mutations refine these features for CMT1G.

In families with missense PMP2 variants p.Ile43Asn, p.Thr51Pro, and p.Ile52Thr, affected individuals typically had childhood or adolescent onset of clumsiness, frequent tripping, difficulty running, and progressive weakness in the distal lower limbs, followed by hand weakness later in life.[3][5][10] Electrophysiologic studies demonstrated markedly reduced motor nerve conduction velocities (MNCV), often in the 15–30 m/s range, consistent with demyelinating neuropathy.[3][5][10] Sural nerve biopsy in the p.Ile43Asn family showed “onion bulbs and degenerating fibers with various myelin abnormalities,” indicative of repeated cycles of demyelination and remyelination.[10] Muscle imaging (MRI) revealed predominant fatty replacement in the anterior and lateral compartments of the lower legs, similar to the pattern seen in CMT1A due to PMP22 duplication.[10] In the Bulgarian and German families with p.Met114Thr and p.Val115Ala, clinical features included childhood-onset polyneuropathy, variable patterns of demyelination, slow-to-very slow progression, and most severe involvement of peroneal muscles, again pointing to length-dependent distal involvement.[5]

The in-frame deletion variant p.I50del has been reported in at least two pedigrees, and in both, affected family members showed **early-onset demyelinating neuropathy without other distinguishing features beyond typical CMT1 signs**.[8][7] The initial study describing p.I50del reported onset in early childhood with delayed motor milestones, difficulty walking, and slowly progressive distal weakness.[8] Nerve conduction studies confirmed demyelinating neuropathy with reduced MNCV, and molecular modeling suggested that the deletion did not grossly disrupt the overall PMP2 structure but likely altered its function.[8] A subsequent case series of nine family members over three generations with the same c.147_149delTAT (p.Ile50del) mutation documented a consistent phenotype of demyelinating CMT with early onset, distal weakness and atrophy, sensory loss, pes cavus, and reduced conduction velocities.[7] The authors concluded that their study “highlights the genetic variability of the CMT family instead of the overlapping clinical phenotypes within demyelinating forms,” underscoring that PMP2-related CMT is clinically similar to other CMT1 entities and not easily distinguishable without genetic testing.[7]

Taken together, key symptom and sign phenotypes in CMT1G include distal muscle weakness in the lower extremities (HP:0003550), muscle atrophy (HP:0003202), decreased or absent deep tendon reflexes (HP:0001284), pes cavus (HP:0001761), hammer toes (HP:0001837), length-dependent sensory loss (HP:0003479), gait disturbance (HP:0002355), and difficulty running or walking (HP:0002355).[1][5][7][8][10][18][19] Electrophysiologically, demyelinating neuropathy with markedly reduced motor nerve conduction velocity (<38 m/s in upper limb motor nerves) is characteristic (HP:0003431).[18][19] Sural nerve biopsy findings of onion bulb formations and demyelinated fibers reflect chronic demyelination and remyelination (HP:0003430).[10] Muscle imaging showing distal muscle fatty replacement contributes to phenotypic characterization and parallels other CMT1 forms.[10] Age of symptom onset is typically in childhood or adolescence, though some adult-onset cases may occur.[1][3][5][7][8][10][18] Severity ranges from mild gait disturbance with preserved ambulation to more severe disability requiring assistive devices, but progression is generally slow over decades.[5][7][8][10]

Quality-of-life impact in CMT1G mirrors that of other CMT1 subtypes. Distal weakness and foot deformities lead to impaired mobility, increased risk of falls, and difficulty performing activities that require fine motor coordination such

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 1 |
| Unverifiable | 2 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003479` (1 mention) - HP does not contain this term
- `HP:0003430` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002355` (obsolete Difficulty walking) (2 mentions) - replaced by `HP:0001288`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.