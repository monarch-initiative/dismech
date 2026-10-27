---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-27T11:40:37.996193'
end_time: '2026-10-27T11:45:19.445136'
duration_seconds: 281.45
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Tricho-dento-osseous Syndrome
  mondo_id: MONDO:0008592
  category: Genetic
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 59
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 29
  on_topic: 20
  validator_version: 0.4.0
term_validation:
  total_terms: 41
  verified: 35
  not_found: 1
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.028
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:0111565
    reported_labels:
    - Disease Ontology
    ontology_label: trichodontoosseous syndrome
  unresolved_terms:
  - HP:0002796
  unresolvable_prefixes:
  - Gene
  - OMIM
  - ORPHA
  - OMIA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tricho-dento-osseous Syndrome
- **MONDO ID:** MONDO:0008592 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Genetic

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Tricho-dento-osseous Syndrome** covering all of the
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

# Tricho-dento-osseous syndrome: disease-characteristics research report

**Tricho-dento-osseous syndrome (TDO)** is a rare, highly penetrant autosomal-dominant ectodermal dysplasia caused by heterozygous pathogenic variants in **DLX3** (*distal-less homeobox 3*; HGNC:2916; NCBI Gene:1747; OMIM gene 600525) at **17q21.33**. It principally disrupts epithelial–mesenchymal development of teeth, hair, and bone, producing enamel hypoplasia/hypomineralization, molar taurodontism, congenital curly or kinky hair, and increased skeletal density or cortical thickness. The disease requested here is specifically **MONDO:0008592 / OMIM:190320**, not a similarly named dental dysplasia. [2][12][104]

**Evidence note.** TDO is ultra-rare, so most clinical evidence comes from a few large kindreds, small family studies, and case reports rather than registries or randomized trials. Frequencies are therefore sensitive to ascertainment and publication bias. Unless otherwise stated, this report describes aggregated disease-level evidence, not individual EHR data.

---

## 1. Disease information

### Definition and classification

TDO is an ectodermal-dysplasia syndrome affecting both ectoderm-derived structures—hair, nails, enamel—and mesenchymal/neural-crest-derived dental and skeletal tissues. The core phenotype is generalized defective enamel plus taurodontism, accompanied variably by congenital abnormal hair, nail dystrophy, craniofacial sclerosis, and elevated appendicular or axial bone mineral density. [1][64]

### Identifiers and synonyms

| Resource | Identifier/name |
|---|---|
| MONDO | **MONDO:0008592**, tricho-dento-osseous syndrome |
| OMIM phenotype | **190320**, Trichodontoosseous syndrome |
| Causal-gene OMIM | **DLX3; 600525** |
| Orphanet | **ORPHA:3352** |
| Disease Ontology | **DOID:0111565** |
| MeSH | **C536549**, supplementary concept “Tricho-dento-osseous syndrome” |
| UMLS/MedGen | **C0265333**; MedGen UID 78555 |
| GARD | **7799** |
| ICD-10 | **Q82.4**, ectodermal dysplasia (broad code, not TDO-specific) |
| ICD-11 | **LD27.0Y**, other specified syndromes affecting the skin (broad grouping) |
| Common synonyms | TDO; TDO syndrome; trichodontoosseous syndrome; tricho-dento-osseous dysplasia |
| Historical/phenotypic labels | amelogenesis imperfecta–osteosclerosis syndrome; taurodontism–curly hair–osteosclerosis syndrome |

The ICD codes are broader parent categories and should not be treated as one-to-one TDO-specific mappings. [180][181][183]

---

## 2. Etiology

### Causal factor

The primary and sufficient cause is a **heterozygous germline pathogenic variant in DLX3**. DLX3 encodes a nuclear homeodomain transcription factor that controls terminal differentiation and extracellular-matrix programs in ameloblasts, odontoblasts, osteoblast-lineage cells, and hair-follicle/epidermal cells. The foundational 1998 study found a segregating four-base deletion in six families:

> “identification of a 4 bp deletion in human DLX3 which correlates with the TDO phenotype in six families.”

Human-family genetic evidence; Price et al., published March 1998, PMID [9467018](https://pubmed.ncbi.nlm.nih.gov/9467018/). [17]

### Risk factors

| Factor | Current evidence |
|---|---|
| Pathogenic DLX3 allele | Principal risk factor; typically heterozygous and germline |
| Affected parent | Each pregnancy has a **50%** transmission probability, independent of sex |
| De novo mutation | Documented, including p.Gln178His; recurrence risk to siblings is low but not zero because parental germline mosaicism cannot be excluded |
| Family history | Strong risk indicator, but absence does not exclude a de novo case |
| Modifier genes | No validated clinical modifier has been established. WNT10A and regulatory RNAs are mechanistic candidates, not proven inherited modifiers |
| Sex | No demonstrated sex bias; males and females are affected approximately equally |
| Ethnicity | No inherent ethnic restriction demonstrated |
| Consanguinity | Not a causal risk factor for this dominant disorder |
| Environmental exposure | No toxin, infection, lifestyle, maternal exposure, or occupational cause is established |

The originally studied North Carolina, Virginia, and Tennessee kindreds shared the recurrent **c.571_574delGGGG** allele and a surrounding haplotype, supporting descent from a common ancestor. Phenotypic differences despite the shared allele imply modifier-gene, epigenetic, stochastic, or environmental effects, but none has been definitively identified. [110][117]

### Protective factors and gene–environment interaction

No genetic variant has been demonstrated to protect against penetrance of TDO, and no diet or lifestyle intervention prevents the congenital developmental disorder. Environmental conditions do, however, modify **downstream morbidity**:

- fluoride exposure, excellent oral hygiene, low cariogenic-sugar intake, and early restorative coverage can reduce caries, attrition, pulp exposure, and abscesses;
- delayed dental care increases tissue loss and early edentulism;
- no convincing environmental determinant of hair, nail, or skeletal penetrance has been demonstrated.

Thus, the best-supported gene–environment interaction concerns **complications of abnormal enamel**, not whether TDO itself develops.

---

## 3. Phenotypes

### Core phenotype and natural-history statistics

In the best-described historical cohort of 33 affected people, all dentate individuals had thin and/or pitted generalized enamel hypoplasia and all had taurodontism, although severity varied. Kinky or curly hair was reported at birth in **85%**, remained after infancy in **46%**, and cranial radiographic abnormalities occurred in **97%**, compared with 30% of unaffected relatives. [196]

A 2025 systematic review/meta-analysis, useful as the latest aggregated estimate but affected by heterogeneous case reporting, found taurodontism in 70.5%, enamel hypoplasia in 34.5%, dental infection in 28.7%, and increased bone density/thickness in 43.8%; pooled estimates were approximately 73% for taurodontism and 71% for enamel hypoplasia. These lower figures than the family cohorts probably reflect incomplete reporting and differing diagnostic definitions. [70]

### Phenotype table

| Phenotype type | Manifestation and suggested HPO term | Onset/course and frequency | Functional or quality-of-life effect |
|---|---|---|---|
| Clinical sign—dental | Generalized enamel hypoplasia; **HP:0006297**; enamel pits **HP:0009722** | Primary and permanent dentitions; congenital/developmental; near-universal in classic cohorts; variable thickness/severity | Sensitivity, poor appearance, rapid wear, chewing difficulty |
| Clinical sign—dental | Enamel hypomineralization **HP:0006285** and yellow-brown discoloration | Early childhood when teeth erupt; lifelong | Caries and attrition susceptibility |
| Clinical sign—dental | Taurodontia **HP:0000679** | Developmental; primary and permanent molars, especially mandibular first permanent molars; among the most consistent findings | Enlarged pulp chambers complicate endodontics and facilitate early pulp exposure |
| Clinical sign—dental | Dentin hypoplasia/thin dentin; suggest **HP:0000692, Abnormality of dental hard tissues** | Developmental; variant-dependent | Pulp exposure and technically difficult restoration |
| Clinical sign—dental | Microdontia **HP:0000691** and widely spaced teeth **HP:0000687** | Childhood; variable | Malocclusion and cosmetic effect |
| Clinical sign—dental | Delayed, advanced, or precocious eruption; **HP:0000680 / HP:0006288**, as appropriate | Childhood; direction varies among families | Impacted or retained teeth and altered treatment timing |
| Complication | Dental caries and periapical abscess **HP:0030758** | Progressive after eruption; historical abscess prevalence about 80% | Pain, infection, endodontic treatment or extraction |
| Clinical sign—hair | Curly, kinky, coarse, sparse, woolly, or lanugo-like hair; **HP:0002212**, **HP:0008070**, **HP:0011362** | Present at birth in about 80–85%; approximately half straighten by adolescence | Usually cosmetic/psychosocial; hair can be brittle or shed excessively |
| Clinical sign—nail | Flat, brittle, peeling or dysplastic nails; fragile nails **HP:0001808** | Childhood; intermittent or variable | Usually mild cosmetic and manual inconvenience |
| Imaging/physical sign—bone | Increased bone mineral density **HP:0011001**; osteosclerosis **HP:0002796** | Detectable in childhood, often more conspicuous with age; variable | Usually little physical disability; may complicate radiographic interpretation |
| Imaging sign—skull | Thickened calvarium, obliterated diploë **HP:0030312**, absent frontal sinus or mastoid pneumatization **HP:0000264** | Bone changes evolve into adulthood; reported in 65–97% in classic series | Usually asymptomatic; may contribute to craniofacial shape |
| Craniofacial sign | Dolichocephaly **HP:0000268**, frontal bossing **HP:0002007**, occasional craniosynostosis | Developmental; variable | Usually cosmetic; severe craniosynostosis is uncommon |
| Craniofacial/dental sign | Mandibular prognathism, short ramus, increased jaw trabeculation | Childhood/adolescence; variable | Malocclusion, chewing and esthetic effects |
| Skeletal sign | Long-bone cortical/tubular sclerosis and elevated spine/hip/radius BMD | Slowly evolving; variability increases with age | Generally no proven excess fracture tendency |
| Limb sign | Fifth-finger clinodactyly **HP:0040019** | Congenital; occasional | Usually negligible functional effect |
| Laboratory finding | Routine blood chemistry generally normal | Stable | No characteristic circulating diagnostic biomarker |

Dental morbidity dominates quality-of-life burden: hypersensitivity, pain, loss of occlusal vertical dimension, abscesses, compromised mastication, appearance-related distress, and early tooth loss. Historical reports found dental abscesses in roughly **80%** and complete tooth loss in approximately **40% of affected adults**, although modern preventive restoration should reduce these outcomes. [334][339]

No validated TDO-specific EQ-5D, SF-36, PROMIS, or oral-health quality-of-life cohort was found.

---

## 4. Genetic and molecular information

### Gene annotation

| Field | DLX3 annotation |
|---|---|
| Symbol/full name | **DLX3**, distal-less homeobox 3 |
| HGNC | **HGNC:2916** |
| NCBI Gene | **1747** |
| Ensembl | **ENSG00000064195** |
| OMIM | **600525** |
| Location | **17q21.33** |
| Protein | Homeobox protein DLX-3; nuclear sequence-specific transcription factor |
| Germline/somatic | TDO variants are germline; TDO is not a somatic-neoplasm disorder |
| Disease mechanism | Allele-dependent loss of transcriptional function, dominant-negative interference, or haploinsufficiency |
| Relevant compartment | Nucleus, **GO:0005634** |
| Molecular-function suggestions | DNA-binding transcription-factor activity, RNA polymerase II-specific; sequence-specific DNA binding |

### Disease-associated variants

HGVS descriptions differ among publications because of historical transcript numbering. The table uses **NM_005220.3** where available.

| Variant | Type/classification and population evidence | Reported phenotype or functional consequence |
|---|---|---|
| **c.571_574delGGGG, p.(Gly191Argfs\*66)** | Recurrent frameshift; ClinVar pathogenic; absent from gnomAD in ClinVar evaluations | Classic TDO; founder allele in several southeastern-US families; altered C-terminal domain, deficient DNA binding/transactivation, dominant-negative interference |
| **c.561_562delCT, p.(Tyr188Glnfs\*13)** | Frameshift; ClinVar pathogenic | Attenuated TDO/AI with taurodontism; coarse hair and mild skeletal involvement in some families |
| **c.398G>C, p.Arg133Pro** | Homeodomain missense; reported pathogenic | Severe/variable enamel and hair phenotype |
| **c.524T>G, p.Ile175Ser** | Homeodomain missense | TDO with dental, hair, and skeletal findings |
| **c.533A>G, p.Gln178Arg** | Homeodomain missense | TDO; studied in patient BMSCs and TDO-iPSC-derived MSCs |
| **c.534G>C, p.Gln178His** | Missense; ClinVar pathogenic/likely pathogenic; documented de novo | Typical or incompletely expressed TDO |
| **c.545C>T, p.Ser182Phe** | Homeodomain missense | Severe TDO, including very sparse/lanugo-like hair in a Finnish family |
| **c.476G>T, p.Arg159Leu** | Missense; ClinVar pathogenic | Amelogenesis imperfecta/taurodontism with attenuated systemic TDO features |
| **c.574delG, p.(Glu192Argfs\*66)** | Frameshift; ClinVar likely pathogenic | Attenuated TDO |
| **c.604_605del, p.Ser202\*** | Frameshift described in 2024 | Enamel dysplasia; reduced enamel thickness, hardness and calcium, increased magnesium |
| Whole-gene DLX3 deletion | Copy-number loss | AI/taurodontism with attenuated systemic features; supports haploinsufficiency for some alleles |
| **c.516+1_516+2insA** | First reported pathogenic splice-site variant, 2026 | Two abnormal transcripts; severe dentin hypoplasia/taurodontism in one member, epithelial-predominant enamel/hair findings in relatives |

The recurrent c.571_574del variant is not present in gnomAD according to current ClinVar submissions and has multiple concordant pathogenic assertions. [298][307] The full reported spectrum is broader than this table, and individual variant interpretation should use current ClinVar/ACMG evidence rather than publication labels alone.

### Functional consequence and genotype–phenotype relationship

The c.571_574del protein enters the nucleus but fails to bind canonical DLX3 DNA elements normally and has defective transcriptional activity. Co-expression reduces wild-type DLX3 activity, supporting a **dominant-negative** effect. [PMID 18492670](https://pubmed.ncbi.nlm.nih.gov/18492670/):

> “the transcriptional activity of DLX3WT is significantly reduced in the presence of the mutated isoform.”

[87]

Other alleles, including whole-gene deletion and some homeodomain variants, support **loss of function/haploinsufficiency**. TDO should therefore not be represented by one universal molecular-effect label; mechanism is variant-dependent.

No validated modifier gene, disease-specific DNA-methylation signature, repeat expansion, mitochondrial variant, aneuploidy, or recurrent translocation is known. A heterozygous whole-gene deletion demonstrates that a chromosomal copy-number variant can produce the phenotype, but classic TDO is generally a single-nucleotide or small-indel disorder.

---

## 5. Environmental information

There is no evidence that pollution, radiation, smoking, alcohol, diet, infection, or occupational exposure initiates TDO. It is not infectious or immune-mediated and has no zoonotic transmission.

Environmental factors chiefly influence secondary oral disease:

- fermentable-carbohydrate exposure and poor plaque control promote caries;
- absent preventive restoration permits accelerated attrition and pulp exposure;
- timely fluoride, hygiene, professional cleaning, and crown coverage are protective against complications, not against the underlying developmental defects.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A heterozygous germline DLX3 pathogenic variant leads to** altered dosage, DNA binding, or transcriptional activity of the DLX3 homeodomain protein in developing ectodermal and cranial neural-crest tissues.  
2. **Altered DLX3 activity leads to** dysregulated epithelial–mesenchymal differentiation in ameloblasts, odontoblasts, hair-follicle cells, osteoblast-lineage cells, and osteoclast-supporting stromal cells.  
3. **Dental epithelial dysregulation leads to** reduced transcription of enamel-matrix genes—particularly **AMELX, ENAM, AMBN, ODAM, KLK4**—and abnormal ion-transporter/carbonic-anhydrase expression.  
4. **Reduced matrix production and disturbed pH regulation lead to** thin, pitted, hypomineralized, mechanically weak enamel.  
5. **Odontoblast disorganization and increased apoptosis lead to** reduced dentin matrix/tubule formation and enlarged pulp chambers, resulting in taurodontism.  
6. **Weak enamel plus enlarged pulp chambers leads to** rapid wear, sensitivity, pulp exposure, caries, abscesses, and premature tooth loss.  
7. **In the skeletal branch, altered DLX3 signaling leads to** variant- and age-dependent changes in osteoblast differentiation and, importantly, reduced osteoclastogenesis/resorption through IFN-γ, RANKL/OPG, miR-124, and related pathways.  
8. **Reduced bone resorption and altered formation lead to** increased trabecular bone volume/BMD and cranial or long-bone sclerosis.  
9. **In the hair branch, altered DLX3-dependent follicular differentiation leads to** abnormal inner-root-sheath/hair-shaft formation, producing congenital kinky, curly, sparse, or woolly hair; why hair frequently straightens with age remains **inferred and unexplained**.  
10. **Differences among variants, tissues, developmental timing, and as-yet-unproven modifiers lead to** marked intra- and interfamilial expressivity.

### Dental epithelium and enamel

DLX3 promotes transcription of **AMELX, ENAM, KLK4, and ODAM**. Dental-epithelium-specific *Dlx3* deletion in mice produces chalky hypomineralized enamel, abnormal keratin expression, loss of normal enamel-rod decussation, and disrupted carbonic-anhydrase/ion-transporter programs required for pH oscillations during mineral maturation. Relevant suggested GO terms include:

- amelogenesis — **GO:0097186**;
- enamel mineralization — **GO:0070166**;
- odontogenesis — **GO:0042476**;
- biomineral tissue development — **GO:0031214**.

The 2024 human-family/in-vitro study found **DLX3 c.604_605del** and significantly reduced enamel thickness, hardness, and calcium with increased magnesium. In ameloblast-lineage cells, the allele reduced AMELX, TUFT1, KLK4, AMBN, and ODAM expression and DLX3 transactivation of AMELX/ODAM/KLK4. Published January 2024; PMID [38006713](https://pubmed.ncbi.nlm.nih.gov/38006713/). [32]

### Dentin and taurodontism

Mutant-DLX3 transgenic mice show disrupted odontoblast polarization, increased odontoblast apoptosis, abnormal dentinal tubules and matrix secretion, thin dentin, and enlarged pulp chambers resembling human taurodontism. Human dental-pulp experiments likewise show reduced proliferation, odontogenic differentiation, and mineralization. [48][283]

Suggested terms:

- cell: ameloblast **CL:0000059**; odontoblast **CL:0000060**;
- processes: odontoblast differentiation, dentin-containing tooth development, extracellular-matrix organization;
- products/pathways: DSPP, RUNX2, WNT10A, BMP2 signaling.

A 2026 family study reported that DLX3 directly activates **WNT10A**, proposing disrupted WNT10A regulation as a contributor to dentin defects and taurodontism. This is strong molecular evidence but too recent and limited to three families/cell assays to establish WNT10A as a clinical modifier. [274][289]

### Bone remodeling

Bone findings arise from a balance of effects on formation and resorption rather than simple constitutive osteoblast activation.

- In vitro, c.571_574del enhances mesenchymal commitment toward osteoblasts and increases alkaline phosphatase, mineral deposition, and osteogenic markers. [PMID 17950683](https://pubmed.ncbi.nlm.nih.gov/17950683/). [261]
- In mutant-DLX3 transgenic mice, trabecular volume and BMD increased even though dynamic in-vivo bone-formation rate did not. Osteoclast numbers, TRACP-5b, and CTX decreased, while serum IFN-γ rose about fivefold. IFN-γ mRNA was increased **3.35±1.26-fold** in marrow and **2.36±0.86-fold** in spleen. Human TDO serum also had a greater-than-twofold IFN-γ increase in 25 affected versus 15 unaffected relatives. [PMID 18996110](https://pubmed.ncbi.nlm.nih.gov/18996110/). [311]
- DLX3/Q178R can inhibit osteoclast differentiation through **miR-124/NFATC1**, and patient BMSCs show a reduced RANKL/OPG ratio. [PMID 26836061](https://pubmed.ncbi.nlm.nih.gov/26836061/). [265]
- Q178R and c.571_574del delayed cellular senescence in experimental osteoblast-lineage cells, potentially extending the cells’ functional lifespan despite reduced instantaneous osteogenic potential. [256]

Suggested terms: osteoblast **CL:0000062**, osteoclast **CL:0000092**; osteoblast differentiation **GO:0001649**, ossification **GO:0001503**, bone mineralization **GO:0030282**, osteoclast differentiation and bone resorption.

### 2023–2024 iPSC and molecular developments

A patient-derived TDO iPSC line carrying **c.533A>G/p.Gln178Arg** was reported in 2023/2024. TDO-iPSC-derived mesenchymal stromal cells had weaker osteogenic differentiation, reduced H19 and KDM5B, and increased miR-29c-3p. Perturbation and rescue experiments supported:

**mutant DLX3 → reduced H19 → increased miR-29c-3p → reduced KDM5B → delayed osteogenic differentiation.**

The authors concluded:

> “DLX3(Q178R) suppresses osteogenesis via H19/miR-29c-3p/KDM5B axis in vitro.”

Published online July 3, 2023; collection July 2024; PMID [38481875](https://pubmed.ncbi.nlm.nih.gov/38481875/). This was a one-patient-derived in-vitro model, so it does not by itself explain the whole-body high-BMD phenotype. [142]

### Immune, metabolic and omics interpretation

- **Immune involvement:** IFN-γ influences osteoclastogenesis experimentally, but TDO is not an inflammatory or autoimmune disease.
- **Metabolism:** no disease-specific systemic metabolomic or lipidomic signature is established; mineral abnormalities are tissue-local rather than a recognized circulating calcium/phosphate disorder.
- **Epigenetics:** KDM5B histone-demethylase and noncoding RNA H19/miR-29c-3p are implicated experimentally, but no diagnostic epigenetic signature exists.
- **Single-cell/spatial multi-omics:** no TDO-specific human single-cell or spatial-transcriptomic atlas was identified.
- **Functional screens:** no disease-directed CRISPR screen or clinically actionable dependency has been validated.

---

## 7. Anatomical structures affected

| Level | Principal structures and suggested ontologies |
|---|---|
| Organ/system | Teeth and periodontium; hair and hair follicles; nails; skull/calvarium, mandible, maxilla, spine, radius/ulna, hip and other long bones |
| Dental tissues | Enamel, dentin, dental pulp, tooth root/furcation and alveolar bone |
| Craniofacial sites | Calvarial cortex/diploë, skull base, frontal sinus, mastoid air cells, mandibular ramus |
| Cell populations | Ameloblast **CL:0000059**; odontoblast **CL:0000060**; osteoblast **CL:0000062**; osteoclast **CL:0000092**; osteocyte; mesenchymal stromal cell; hair-follicle keratinocyte |
| Tissue classes | Mineralized extracellular matrix, dental epithelium, cranial neural-crest-derived mesenchyme, epidermal appendages |
| Subcellular site | DLX3 functions primarily in the nucleus **GO:0005634**; downstream enamel proteins are secreted into extracellular matrix |
| Lateralization | Generally bilateral and generalized; no characteristic left–right preference |

Useful UBERON targets for curation include tooth, enamel, dentin, dental pulp, hair follicle, nail, skull, mandible, maxilla, vertebral column, radius, ulna, femur and alveolar bone. Exact versioned UBERON mappings should be validated at database ingestion because some dental terms have changed hierarchy.

---

## 8. Temporal development

- **Onset:** genetic and developmental from conception. Hair can be abnormal at birth; dental abnormalities become clinically apparent with eruption, commonly allowing recognition at approximately 6–12 months.
- **Childhood:** enamel defects, taurodontism, sensitivity and caries emerge; skeletal sclerosis may be visible by about age three.
- **Adolescence:** roughly half of initially curly/kinky hair phenotypes become less apparent or straighten.
- **Adulthood:** bone density and cranial sclerosis may become more conspicuous; unprotected teeth progressively wear, become infected, or are lost.
- **Course:** chronic lifelong, non-relapsing and non-remitting. Individual manifestations differ: dental structural defects are fixed but complications are progressive; hair may improve; skeletal radiographic changes may increase with age.
- **Critical intervention window:** before substantial post-eruptive enamel wear—ideally immediately after tooth eruption—for fluoride, sealants, bonding, or full-coronal coverage.

A prospective DEXA study of 20 affected and 14 unaffected relatives found significantly higher BMD at the distal radius/ulna, femoral neck, and lumbar spine in affected individuals. Published October 2004; PMID [15454107](https://pubmed.ncbi.nlm.nih.gov/15454107/). [197]

There is no recognized staging system, acute crisis, spontaneous remission, or end-stage systemic disease.

---

## 9. Inheritance and population

| Characteristic | Best-supported assessment |
|---|---|
| Inheritance | Autosomal dominant |
| Penetrance | Described as complete or highly penetrant, especially when subtle dental findings are sought |
| Expressivity | Markedly variable within and between families |
| Offspring risk | 50% per pregnancy for an affected heterozygous parent |
| Sex ratio | Approximately equal; male-to-male transmission occurs |
| Prevalence | Orphanet estimate **<1 per 1,000,000**; true prevalence unknown |
| Incidence | Not established |
| Reported families | At least 8 in older Orphanet summaries; approximately 12 kindreds in a 2024 NORD summary |
| Founder effect | c.571_574delGGGG founder haplotype in several Virginia/North Carolina/Tennessee families |
| De novo disease | Documented |
| Anticipation | Not reported; no repeat-expansion mechanism |
| Germline mosaicism | Not demonstrated but cannot be excluded in apparently de novo cases |
| Consanguinity | Not relevant to the usual dominant mechanism |
| Carrier frequency | Not meaningfully established; pathogenic alleles are extremely rare and heterozygous “carriers” are generally affected |
| Geographic/ethnic distribution | Initially concentrated in southeastern-US kindreds; subsequently described in Europe, China and other populations |

Orphanet classifies onset as childhood and prevalence below one per million. [109] In the original North Carolina linkage cohort, 39 of 63 family members were affected. [119]

---

## 10. Diagnostics

### Clinical and radiographic criteria

A commonly cited clinical definition requires:

1. generalized enamel hypoplasia with hypomaturation or hypocalcification;
2. severe taurodontism, particularly of mandibular first permanent molars;
3. an autosomal-dominant pedigree; and
4. at least one minor feature—early curly/kinky hair, nail dystrophy, or radiographic bone sclerosis.

Molecular confirmation is preferable because de novo and attenuated cases may not meet the pedigree or minor-feature criteria. [169][170]

### Recommended work-up

| Test | Role |
|---|---|
| Dental examination and photographs | Enamel thickness, pitting, discoloration, attrition, spacing, sensitivity and abscesses |
| Panoramic dental radiograph | Taurodontism, pulp-chamber/root morphology, impacted or retained teeth, infections |
| Bitewing/periapical imaging | Caries, pulp exposure and periapical disease |
| Lateral cephalogram/skull imaging | Cranial thickness, diploë, frontal sinus/mastoid pneumatization, prognathism |
| DXA | Optional; characterizes systemic BMD when clinically indicated, but is not required for diagnosis |
| Routine chemistry | Usually nonspecific; use to exclude metabolic bone disorders rather than confirm TDO |
| Hair microscopy | May show irregular shafts, grooves or scales, but lacks a pathognomonic pattern |
| Molecular test | Heterozygous pathogenic/likely pathogenic **DLX3** variant confirms diagnosis |

### Genetic-testing strategy

1. **First line:** sequencing of all DLX3 coding exons and splice junctions, with deletion/duplication analysis.
2. **Phenotypically overlapping cases:** amelogenesis-imperfecta or ectodermal-dysplasia panel including **DLX3**.
3. **Unresolved or atypical cases:** trio WES or WGS, with copy-number and splice-region analysis.
4. **CMA:** useful only if a larger deletion/CNV is suspected; it may detect whole-gene loss but misses most small variants.
5. **Karyotype/FISH:** not routine.
6. **Mitochondrial and repeat-expansion tests:** not indicated.
7. **RNA studies:** potentially useful for suspected splice variants but not standard clinical testing.

Postnatal and prenatal full-coding-region DLX3 sequencing tests are listed in the NIH Genetic Testing Registry. [178][321]

### Differential diagnosis

| Disorder | Distinguishing features |
|---|---|
| DLX3-related amelogenesis imperfecta type IV / AI with taurodontism | Allelic spectrum; predominantly dental disease without clear hair or skeletal abnormalities |
| Other amelogenesis imperfecta | Enamel defect but usually lacks the TDO combination of congenital kinky hair and osteosclerosis |
| Oculodentodigital dysplasia | GJA1-related; characteristic eyes, nose, syndactyly and neurologic features |
| Autosomal-dominant osteopetrosis | More generalized osteosclerosis and potential fracture, nerve-compression or marrow complications; no characteristic enamel-hair combination |
| Dentinogenesis imperfecta/dentin dysplasia | Dentin-predominant tooth changes, often with DSPP or collagen-related disease |
| Hypophosphatasia | Low alkaline phosphatase, defective mineralization and early tooth loss rather than high BMD/TDO hair phenotype |
| Other ectodermal dysplasias | May involve hair/nails/teeth but have different enamel, sweating, skin or immune profiles |

Orphanet specifically recommends considering AI with taurodontism, oculodentoosseous/oculodentodigital dysplasia, and autosomal-dominant osteopetrosis. [166]

### Screening

TDO is not included in population newborn screening. Appropriate strategies are:

- targeted examination and testing of at-risk relatives;
- dental assessment beginning with eruption of the primary teeth;
- cascade DLX3 testing after identification of a familial pathogenic variant.

---

## 11. Outcome and prognosis

The general prognosis is **good**, and normal intelligence and life expectancy are expected. No disease-specific mortality, survival curve, or reduced-life-expectancy estimate has been demonstrated. Orphanet reports no apparent predisposition to fracture despite increased BMD, although isolated reports have discussed fractures; the best interpretation is that fracture risk is **not established as elevated**. [344]

Major morbidity is dental:

- hypersensitivity and pain;
- rapid attrition;
- loss of vertical occlusal dimension;
- recurrent pulp exposure and abscesses;
- difficult endodontics because of taurodontism;
- early tooth loss, historically sometimes in the second or third decade;
- malocclusion, compromised chewing, poor growth in severe pediatric cases, and psychosocial effects.

Hair and nail findings are usually medically mild. Skeletal changes are often radiographic rather than disabling. There are no validated prognostic biomarkers; prognosis depends mainly on enamel/dentin severity, timing of preventive treatment, infection burden, and access to restorative dental care.

---

## 12. Treatment

There is **no disease-modifying pharmacotherapy, approved gene therapy, RNA therapy, cell therapy, or immunotherapy** for TDO. ClinicalTrials.gov returned no recruiting TDO-specific studies. [135] Management is age-specific, multidisciplinary, preventive, restorative and supportive.

| Intervention | Indication/implementation | Evidence and suggested NCIT intervention concept |
|---|---|---|
| Frequent dental surveillance | All affected children and adults; assess eruption, attrition, caries, abscesses and impacted teeth | Expert/case-series practice; **Dental Examination**, **Diagnostic Imaging** |
| Oral hygiene and diet counseling | Prevention of secondary caries | **Patient Education**, **Dietary Counseling** |
| Fluoride toothpaste/rinse/varnish | Remineralization, desensitization and caries prevention | Case-based protocols have used 5% sodium-fluoride varnish every three months; **Fluoride Therapy** |
| Chlorhexidine rinse | Selected high-caries/infection-risk patients; avoid indiscriminate prolonged use | Supportive, not TDO-specific; **Chlorhexidine Treatment** |
| CPP-ACP/desensitizing products | Sensitivity or early enamel demineralization | Limited extrapolated evidence; **Supportive Care** |
| Sealants, bonding and composite restoration | Mild localized enamel defects | **Dental Restoration Procedure** |
| Prefabricated stainless-steel crowns | Moderate/severe primary or young permanent molars, as soon as adequate eruption allows | Protects against wear, caries, pulp exposure and loss of vertical dimension; **Dental Crown Placement** |
| Porcelain/ceramic crowns or veneers | Definitive adolescent/adult esthetic and structural rehabilitation | Case-report evidence; **Dental Prosthesis** |
| Endodontic treatment | Pulp exposure, necrosis or periapical infection | Technically challenging in taurodontic teeth; close follow-up required; **Root Canal Therapy** |
| Extraction | Non-restorable or repeatedly infected teeth | **Tooth Extraction** |
| Dentures, bridges or implants | Replacement of missing teeth | **Dental Prosthesis**, **Dental Implantation** |
| Orthodontics/maxillofacial surgery | Malocclusion, prognathism, impaction or severe skeletal discrepancy | Individualized; **Orthodontic Procedure**, **Maxillofacial Surgery** |
| Psychological support | Appearance-related distress, chronic pain, complex rehabilitation | **Psychosocial Support** |
| Genetic counseling | Patient and family risk assessment and reproductive planning | **Genetic Counseling** |

A pediatric case-management report used 0.05% sodium-fluoride and 0.12% chlorhexidine rinses, CPP-ACP paste, quarterly 5% fluoride varnish, and stainless-steel crowns. This is a case-based protocol, not a trial-derived standard. [315]

The latest restorative implementation is a facially driven fully digital implant/prosthodontic workflow, reported online September 5, 2024. The authors reported functional, esthetic and psychosocial improvement, but this remains single-patient evidence; PMID [39237422](https://pubmed.ncbi.nlm.nih.gov/39237422/). [150]

No response-rate statistics or comparative adverse-event data are available.

---

## 13. Prevention

### Primary prevention

The occurrence of TDO cannot be prevented through vaccination, diet or lifestyle. Reproductive options after identification of a familial variant include:

- preconception genetic counseling;
- prenatal diagnostic testing by chorionic-villus sampling or amniocentesis;
- preimplantation genetic testing for monogenic disease;
- donor gametes or other family-planning options.

Testing predicts inheritance of the variant but not exact severity because expressivity is variable.

### Secondary prevention

- cascade testing of first-degree relatives;
- examination of infant hair/nails and early primary dentition;
- early panoramic radiography when clinically appropriate;
- immediate preventive restoration of vulnerable erupted teeth.

### Tertiary prevention

- meticulous plaque control and reduced cariogenic-sugar frequency;
- topical fluoride and regular professional prophylaxis;
- early crowns/bonding to prevent wear and pulp exposure;
- prompt treatment of caries or infection;
- maintenance of occlusal vertical dimension and chewing function;
- long-term radiographic monitoring.

No TDO-specific vaccine, antimicrobial prophylaxis, fracture prophylaxis or population-screening program is indicated.

---

## 14. Other species and naturally occurring disease

A naturally occurring TDO-like disorder has been reported in **one Brown Swiss calf**.

| Field | Animal disease information |
|---|---|
| Species | *Bos taurus*, taurine cattle; NCBI Taxon **9913** |
| Breed | Brown Swiss; **VBO:0000166** |
| OMIA | **OMIA:002109-9913** |
| Gene | Bovine **DLX3**, NCBI Gene **784366**, chromosome 19 |
| Variant | **c.584_585insGGAGCACAGG; p.(Ser198ArgfsTer99)** |
| Origin/inheritance | Heterozygous de novo; inferred autosomal dominant |
| Phenotype | Dull curly/tousled coat, mild hypotrichosis, curly eyelashes, pinna hypotrichosis, dry scaly skin, irregular hair shafts, follicular dysplasia and mild brown incisor discoloration |
| Evidence | Single calf plus unaffected parents; WGS and segregation |
| Publication | Hofstetter et al., 2017, PMID [28670783](https://pubmed.ncbi.nlm.nih.gov/28670783/) |
| Limitation | No population prevalence and no replicated cattle series; full human dental/bone phenotype was not demonstrated |

The bovine allele replaces the normal C-terminal transactivation domain with an abnormal frameshifted peptide, closely paralleling human C-terminal TDO alleles. [240][242]

There is no zoonotic potential or cross-species transmission; these are homologous inherited disorders.

---

## 15. Model organisms and experimental resources

| Model | Genotype/system | Recapitulated findings | Main limitations/applications |
|---|---|---|---|
| Global *Dlx3* knockout mouse | Constitutive null | Demonstrates essential developmental role | Embryonic lethal at approximately E9.5 from placental defects, so unsuitable for postnatal TDO |
| Mutant-DLX3 transgenic mouse | Human-equivalent c.571_574delGGGG under 2.3-kb *Col1a1* promoter | Increased trabecular volume/BMD; reduced osteoclastogenesis; high IFN-γ; thin dentin and taurodontism | Promoter-driven expression is not identical to endogenous heterozygosity; does not reproduce every hair/enamel feature |
| Dental-epithelium conditional knockout | *Dlx3* floxed with epithelial Cre | Chalky hypomineralized enamel, abnormal pH regulation, keratin expression and rod decussation | Models epithelial DLX3 loss rather than every human dominant allele |
| Neural-crest conditional knockout | *Dlx3* deletion in cranial neural crest | Major dentin and craniofacial-bone abnormalities | Tissue-restricted null, not full systemic TDO |
| Osteocalcin-lineage conditional knockout | Osteoblast/osteocyte *Dlx3* deletion | Age-dependent changes in trabecular and cortical bone, increased formation markers and altered resorption genes | Bone-specific loss differs from human developmental expression |
| Zebrafish | Homozygous four-base *dlx3b* deletion | Reduced pharyngeal-tooth enameloid mineralization and spinal curvature; 86/100 mutant larvae versus 3/99 controls showed early curvature | Fish enameloid and duplicated *dlx3* biology are not identical to mammalian enamel; homozygous model |
| Human dental-pulp cells | Wild-type versus mutant DLX3 expression | Reduced proliferation, odontogenic markers and mineralization | In vitro and lacks whole-tissue architecture |
| Patient BMSC/iPSC-MSC model | Human Q178R TDO cells | H19/miR-29c-3p/KDM5B changes and delayed osteogenesis | Derived from one patient; in-vitro findings require replication |
| Ameloblast-lineage cell model | 2024 c.604_605del construct | Reduced enamel-matrix-gene expression and transactivation | Immortalized cell line; preliminary mechanism |
| Naturally affected calf | De novo bovine C-terminal frameshift | Hair-shaft/follicular dysplasia and dental discoloration | Single animal; incomplete skeletal characterization |

In zebrafish, 86 of 100 *dlx3b* mutants versus 3 of 99 controls developed early dorsal spinal curvature; scanning electron microscopy and elemental analysis showed abnormal, less-mineralized pharyngeal-tooth enameloid. PMID [32117623](https://pubmed.ncbi.nlm.nih.gov/32117623/). [238]

NIH resources include **DLX3-floxed mice** and **K14-Cre DLX3 conditional-knockout mice** for studying tooth, hair and epidermal phenotypes. [51][54]

---

## Overall assessment

TDO is best understood as an **allelic, autosomal-dominant DLX3 transcription-factor disorder** in which tooth abnormalities are the most penetrant and clinically consequential features. Human genetic evidence is definitive; dental and skeletal mechanisms are supported by human tissue, patient-derived cells, transgenic/conditional mice and zebrafish. The most important recent advances are the 2023–2024 patient-iPSC H19/miR-29c-3p/KDM5B model, the 2024 c.604_605del enamel study, and expanding recognition of woolly hair and attenuated dental-predominant presentations. No disease-modifying therapy exists; early molecular diagnosis and aggressive preservation of erupted teeth currently provide the greatest practical benefit.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 29 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0111565` (3 mentions) - the report calls it "Disease Ontology"; DOID calls it **trichodontoosseous syndrome**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002796` (1 mention) - HP does not contain this term

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Gene`, `OMIM`, `ORPHA`, `OMIA`.