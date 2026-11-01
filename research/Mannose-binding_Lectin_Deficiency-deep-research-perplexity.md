---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-30T11:05:17.616215'
end_time: '2026-10-30T11:09:51.226588'
duration_seconds: 273.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Mannose-binding Lectin Deficiency
  mondo_id: MONDO:0013714
  category: Mendelian
  causal_genes: MBL2
  omim_id: OMIM:614372
  synonyms: mannose-binding protein deficiency
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 53
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 15
  validator_version: 0.4.0
term_validation:
  total_terms: 39
  verified: 35
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mannose-binding Lectin Deficiency
- **MONDO ID:** MONDO:0013714 (if available)
- **Causal gene(s):** MBL2
- **OMIM:** OMIM:614372
- **Synonyms:** mannose-binding protein deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Mannose-binding Lectin Deficiency** covering all of the
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

# Mannose-binding lectin deficiency: comprehensive disease-characteristics report

**Mannose-binding lectin deficiency (MBLD) is caused by low-producing or structurally disruptive variation in the causal gene *MBL2***, which encodes the circulating collectin mannose-binding lectin (MBL). The biochemical phenotype is reduced concentration or function of oligomeric MBL and impaired lectin-pathway complement activation. Although catalogued as a Mendelian disorder—MONDO:0013714 and OMIM 614372—its infection phenotype has **very low and context-dependent penetrance**: most biochemically deficient adults remain healthy, while risk is greatest in young children and people with a second immune stressor such as chemotherapy, transplantation, another immunodeficiency, or severe infection. Thus, MBLD is best understood as a common inherited **susceptibility state**, not a fully penetrant monogenic immunodeficiency. [Web citations below link to the cited sources.] OMIM nevertheless maps “chronic infections due to MBL deficiency” to *MBL2* at 10q21.1 and lists autosomal-dominant inheritance, whereas other authoritative sources regard inheritance as uncertain or functionally codominant because one or two low-producing alleles can lower MBL without reliably causing disease. [1][333][337]

**Scope note.** Evidence specifically published in 2023–2024 is highlighted, but landmark primary studies are retained where they established variants, mechanism, clinical penetrance, or models. “Deficiency” varies markedly among studies—from <50 to <1,000 ng/mL—so apparently conflicting clinical results often reflect different assays, thresholds, populations, and comorbidities. [235][237]

---

## 1. Disease information

### Definition and identifiers

MBL is a liver-derived, calcium-dependent soluble pattern-recognition molecule. It recognizes mannose, fucose, and N-acetylglucosamine-rich arrays on microbes, oligomerizes, associates with MASP-1/MASP-2, and initiates the lectin pathway of complement. MBLD denotes low antigenic MBL, low functional lectin-pathway activity, or a low-producing *MBL2* haplogenotype. A historically common “severe deficiency” definition is **<100 ng/mL**, although no universal threshold exists. [91][149][227]

| Identifier/resource | Identifier or preferred term | URL / status |
|---|---|---|
| MONDO | **MONDO:0013714**, mannose-binding lectin deficiency | Confirmed through MedGen/ClinVar cross-mapping. [2][7] |
| OMIM phenotype | **OMIM:614372**, mannose-binding lectin deficiency | [OMIM phenotype](https://www.omim.org/entry/614372); mapped to *MBL2*. [5] |
| OMIM gene | **OMIM:154545**, *MBL2* | [OMIM gene](https://www.omim.org/entry/154545). [1] |
| NCBI MedGen | **C3280586** | [MedGen](https://www.ncbi.nlm.nih.gov/medgen/482216). [170] |
| SNOMED CT | **703538003**, mannose-binding protein/lectin deficiency | [170] |
| ICD-10-CM | **D84.89**, other immunodeficiencies | Approximate disease-specific mapping; ICD-10 has no uniquely dedicated code. [174] |
| ICD-11 | **4A00.1Y**, other specified defects in the complement system | Listed under primary immunodeficiencies due to innate-immunity disorders. [167][177] |
| MeSH supplementary concept | **C563602**, Mannose-Binding Protein Deficiency | Created November 15, 2011; current supplementary concept. [166] |
| GTR condition | C3280586 | [NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3280586/). [179] |
| Orphanet | No clearly established disease-specific ORPHA number found | Do not confuse this disease with **LMAN1** deficiency, a distinct coagulation disorder. [4] |

**Synonyms:** mannose-binding protein deficiency, mannan-binding lectin deficiency, MBL deficiency, MBL2 deficiency, MBP deficiency, mannose-binding lectin protein deficiency, lectin complement activation pathway defect 1/LCAPD1, and “chronic infections due to MBL deficiency.” [170][171]

**Data provenance:** this report is aggregated at disease level from OMIM, MONDO/MedGen, ClinVar, GTR, ontology resources, cohorts, and primary literature. It does **not** contain individual-level EHR data. Some cited clinical cohorts were assembled retrospectively from hospital records.

---

## 2. Etiology

### Primary causal factors

1. **Structural *MBL2* variants** impair triple-helix formation and assembly of higher-order oligomers.
2. **Promoter/5′ regulatory variants** reduce transcription and serum concentration.
3. Low or dysfunctional MBL reduces microorganism binding, MASP recruitment, C4/C2 cleavage, C3 deposition, and opsonophagocytosis.
4. Clinical infection generally appears only when this biochemical defect intersects with age-related immune immaturity, high pathogen burden, neutropenia, immunosuppression, or another immune defect. [57][160][333]

### Risk, protective, and gene–environment factors

| Factor | Effect and evidence |
|---|---|
| Low-producing *MBL2* haplogenotype | XA/O and O/O commonly produce the lowest functional concentrations; A/O often lowers levels five- to tenfold, while O/O can produce nearly undetectable functional MBL. [84] |
| Infancy/young childhood | The strongest historical window is approximately **6–17 months**, after maternal antibody wanes but before adaptive immunity fully matures. A prospective study found RR 2.92 for acute respiratory infection at 6–17 months, with little or no effect outside that interval. PMID **11255386**. [119] |
| Additional humoral deficiency | The association with recurrent respiratory infection is strongest where impaired humoral immunity coexists. PMID **15086395**. [66] |
| Chemotherapy/neutropenia | Low MBL was associated with serious chemotherapy-related infection in an early leukemia cohort, *p*<0.0001, although later pediatric meta-analysis did not establish it as an independent predictor. PMID **11530153**. [152][155] |
| Solid-organ transplantation | A meta-analysis of 11 studies/1,858 recipients found deficient haplotypes associated with bacterial/fungal infection, RR 1.30; low/null haplotypes gave RR 1.51, mainly in liver recipients. [156] |
| Severe bacterial/pneumococcal disease | Pooled individual-level analysis found mortality OR 2.11 for severe bacterial infection and OR 5.62 for pneumococcal infection, after relevant adjustment. [291] |
| Immunosuppressive drugs, malignancy, cystic fibrosis, chronic lung disease | These reduce compensatory immune redundancy and increase the likelihood that low MBL becomes clinically relevant. [153][226] |
| Sex | No consistent intrinsic sex effect; observed differences probably reflect cohort composition and exposure rather than established sex-linked biology. |
| Lifestyle/toxins | No reproducible disease-specific association with smoking, diet, alcohol, occupation, radiation, or a particular toxin. These can modify respiratory infection generally but are not causes of inherited MBLD. |
| Protective high-producing haplotypes | High-expression HYPA/LYPA/LYQA combinations may improve pathogen recognition. In a 2024 Brazilian COVID-19 cohort, high-production pairs were associated with less invasive ventilation (adjusted OR 0.38) and shock (OR 0.40); this is disease-specific association, not proof that high MBL is universally beneficial. [26] |
| Potential protection from low MBL | Low MBL may reduce complement-assisted entry of intracellular organisms. Meta-analysis suggested rs1800450 and rs1800451 were protective against tuberculosis in African populations, and low MBL has been associated with protection from lepromatous leprosy. [181][183] |

No specific diet, supplement, exercise program, or environmental exposure has been shown to restore genetically deficient MBL. Conversely, reduced MBL can sometimes be protective because excessive lectin-pathway activation contributes to ischemia–reperfusion and inflammatory injury; this is the “MBL paradox.” [241][242]

---

## 3. Phenotypes

Isolated biochemical MBLD is frequently asymptomatic. Percentages therefore cannot be generalized from referral cohorts to all carriers.

| Phenotype type | Clinical characteristics, onset/course and evidence | Suggested HPO term |
|---|---|---|
| Laboratory abnormality | Low serum MBL, congenital/lifelong but concentration can fluctuate as an acute-phase reactant; severity depends on threshold and haplotype. | **Decreased mannose-binding protein level, HP:0032305**. [145] |
| Laboratory abnormality | Low mannan-dependent lectin-pathway activity despite commonly normal CH50/AH50, C3 and C4. | Abnormal complement system physiology; use HP:0032305 plus assay annotation. [227][438] |
| Recurrent respiratory infection | Usually episodic, mild-to-severe, most evident in infancy/early childhood; adults may be affected under immune stress. | **HP:0002205**. [316][321] |
| Bronchiolitis | Pediatric; episodic. In a 1,004-child multicenter cohort, deficient genotypes were associated with bronchiolitis RR 1.95 and recurrent bronchiolitis RR 4.45. | Respiratory tract infection/bronchiolitis; phenotype should be qualified by age. [64][114] |
| Recurrent pneumonia | Variable age and severity; may lead to hospitalization or, in selected cases, bronchiectasis. | **HP:0006532**. [316] |
| Upper-respiratory infection/otitis media | Recurrent, usually childhood and nonprogressive between episodes. | **HP:0002205**; otitis media **HP:0000388**, or recurrent otitis media **HP:0000403**. [322][323] |
| Meningitis/meningococcal infection | Uncommon but potentially severe; historical adult cases include meningococcal meningitis. | Meningitis **HP:0001287**; recurrent meningitis **HP:0006946**; recurrent *N. meningitidis* infection **HP:0005381**. [318][347] |
| Recurrent skin infection/abscesses | Episodic; reported in severe adult cases. | Recurrent skin infections; recurrent infections **HP:0002719**. [141][347] |
| Gastrointestinal infection/chronic diarrhea | Particularly cryptosporidial disease in rare severe cases; can affect growth. | Chronic diarrhea **HP:0002028**; recurrent gastrointestinal infection **HP:0004798**. [322][347] |
| Recurrent *Klebsiella* infection | Rare, potentially severe; fatal lobar pneumonia occurred in the landmark adult series. | **HP:0002742**. [145][347] |
| Recurrent herpes | Reported in severe or combined phenotypes; not specific to MBLD. | Recurrent herpes, if supported in the individual record. [141] |
| Failure to thrive | Secondary to frequent infection/diarrhea, not a direct developmental defect. | **HP:0001508**. [145] |
| Bronchiectasis | Secondary complication rather than defining phenotype. A 2023 follow-up study found no excess compared with symptomatic MBL-sufficient controls. | Bronchiectasis **HP:0002110**. [36] |

### Recent clinical evidence and quality of life

A 2023 retrospective cohort followed 206 children with troublesome respiratory symptoms; 43 (21%) had MBL <0.6 mg/L. At ≥5 years, MBL-deficient and sufficient groups had similar PICU admission (2.3% versus 3.7%), abnormal imaging (23% versus 24%), positive microbiology (32% versus 30%), and bronchiectasis among those scanned. The authors concluded:

> “Children with mannose-binding lectin deficiency and sufficiency showed similar clinical, radiological, and microbiological characteristics.”

PMID **37503644**, published March 1, 2023. [36]

This contrasts with a prospective 2022 multicenter birth cohort of approximately 1,004 children, in which deficient genotypes predicted bronchiolitis (RR 1.95, 95% CI 1.33–2.85) and pneumonia (RR 2.46, 95% CI 1.16–5.22). [106][114]

There is no validated MBLD-specific quality-of-life instrument. Quality-of-life impairment is driven by infection frequency, school/work absence, hospitalization, antibiotic use, and secondary lung disease. In non-CF bronchiectasis, MBL <200 ng/mL correlated with exacerbations, admissions, worse radiological severity, and poorer quality of life, but that evidence concerns MBL as a **modifier of bronchiectasis**, not isolated MBLD. PMID **24429128**. [466]

---

## 4. Genetic and molecular information

### Gene and protein

| Attribute | Value |
|---|---|
| Gene | ***MBL2***, mannose binding lectin 2 |
| HGNC | **HGNC:6922** |
| NCBI Gene | **4153** |
| OMIM gene | **154545** |
| Chromosomal locus | **10q21.1** |
| UniProt | **P11226** |
| Product | Secreted mannose-binding protein C/MBL, a collectin |
| Principal expression | Hepatocytes/liver |
| Protein organization | N-terminal cysteine-rich region, collagen-like domain, neck/coiled-coil, C-terminal C-type carbohydrate-recognition domain |
| Origin of disease variants | Germline |
| Somatic role | Not relevant to inherited MBLD |

These identifiers and liver-restricted expression are supported by NCBI Gene. [91][92]

### Principal structural and regulatory alleles

| Allele/variant | HGVS and rsID | Molecular class and functional consequence | Current interpretation |
|---|---|---|---|
| D | NM_001378373.1:**c.154C>T, p.Arg52Cys**, rs5030737 | Germline missense in collagen-like region; reduces oligomerization, mannan binding, MASP1/MASP2 binding, and complement activation. | Historically disease-associated; ClinVar now has **conflicting** pathogenic, VUS and benign submissions. gnomAD frequency ≈0.0496 is incompatible with a highly penetrant severe disorder. [76][393][364] |
| B | **c.161G>A, p.Gly54Asp**, rs1800450 | Germline missense; distorts collagen triple helix, destabilizes oligomers and reduces functional MBL. | Historical OMIM deficiency allele; current ClinVar submissions include VUS/likely benign/benign. Approximate reported frequency 0.11–0.14 in several populations. [122][125][397] |
| C | **c.170G>A, p.Gly57Glu**, rs1800451 | Germline missense with impaired oligomerization; especially frequent in sub-Saharan Africa. | Historical deficiency allele; ClinVar Miner reports benign submissions; gnomAD frequency ≈0.0763. [121][365] |
| X promoter | rs7096206, −221 Y/X | Regulatory; X strongly lowers transcription, especially in XA/O or XA/XA combinations. | Functional low-expression allele, generally treated as a common susceptibility polymorphism rather than an ACMG pathogenic variant. [26][30] |
| H/L promoter | rs11003125, −550 H/L | Regulatory modulation of transcription. | Common haplotype component. [26] |
| P/Q 5′ region | rs7095891, +4 P/Q | Regulatory modulation. | Common haplotype component. [26] |

The B, C and D alleles are collectively called **O**, with wild type designated **A**. Common extended haplotypes are HYPA, LYQA and LYPA (higher production), LXPA (low), and LYPB, LYQC and HYPD (low/null). [16][385]

**Critical curation warning:** these common variants are functionally real but clinically incompletely penetrant. ClinVar currently lists many MBLD-associated entries—three “pathogenic,” 76 VUS, 13 likely benign and two benign in one compilation—but the canonical variants themselves have discordant assertions. Consequently, genotype should not be interpreted under the same model as a rare, highly penetrant loss-of-function immunodeficiency. [391]

### Other molecular categories

- **Mechanism:** partial loss of function/hypomorphic expression and defective oligomerization, not gain of function or dominant negative disease in the conventional high-penetrance sense.
- **Copy-number/chromosomal abnormalities:** no recurrent deletion, translocation, inversion, or aneuploidy defines MBLD.
- **Somatic variants:** not causal.
- **Modifier genes:** no single validated disease-specific modifier. Candidate interactions include *MASP2*, *FCN2/FCN3*, antibody-deficiency genes, and the underlying genes in cystic fibrosis or other lung disease; most evidence is association-level. [506][510]
- **Epigenetics:** no validated MBLD-specific methylation or histone signature.
- **Disease-specific omics:** no established diagnostic transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic signature beyond serum MBL/lectin-pathway function.

---

## 5. Environmental and infectious information

MBLD is not caused by a toxin, diet, radiation, or occupation. Environmental and acquired factors alter whether the inherited biochemical deficiency becomes clinically visible.

| Category | Relevant factor |
|---|---|
| Medical exposure | Cytotoxic chemotherapy, hematopoietic transplantation, solid-organ transplantation, corticosteroids or other immunosuppressants |
| Physiologic exposure | Loss of maternal antibody during late infancy; immune senescence has not been clearly quantified |
| Comorbidity | Antibody deficiency, cystic fibrosis, bronchiectasis, chronic lung disease, malignancy |
| Bacteria | *Streptococcus pneumoniae*, *Neisseria meningitidis*, *Staphylococcus aureus*, *Klebsiella* spp., and *Pseudomonas aeruginosa* are recurring examples, but none is disease-specific |
| Viruses | Influenza, herpesviruses, SARS-CoV/SARS-CoV-2 and others carry MBL-recognized glycans |
| Fungi/yeasts | *Candida* and *Aspergillus* associations are reported, especially under immunosuppression |
| Parasites | Severe/recurrent cryptosporidiosis has been reported |
| Potential reverse effect | Reduced MBL may impede uptake of intracellular pathogens such as mycobacteria, sometimes producing an apparent protective association |

MBL recognizes numerous bacteria, yeasts, and viruses, but pathogen associations are heterogeneous and population-specific. [12][40]

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Germline structural or promoter variation in *MBL2* leads to** reduced synthesis or defective oligomerization of secreted MBL.
2. **Reduced oligomerization leads to** fewer high-avidity carbohydrate-recognition arrays and impaired binding to microbial mannose/fucose/GlcNAc patterns.
3. **Impaired surface binding and MASP association lead to** reduced MASP-1 autoactivation and reduced MASP-1-mediated activation of MASP-2.
4. **Reduced MASP-2 activity leads to** decreased cleavage of C4 and C2 and reduced formation of C4bC2b, the lectin/classical-pathway C3 convertase.
5. **Reduced C3 convertase activity leads to** less C3b deposition, less opsonization, weaker phagocyte recruitment/uptake and, where relevant, less terminal-complement activation.
6. **Reduced opsonophagocytic clearance leads to** delayed or less efficient control of susceptible extracellular microbes.
7. **In infancy or secondary immune compromise, insufficient compensatory antibody, neutrophil or complement activity leads to** recurrent or unusually severe infection.
8. **Repeated lower-respiratory infection may lead to** pneumonia, hospitalization, and—only in a subset—secondary bronchiectasis or impaired quality of life.
9. **Branch: reduced MBL binding to apoptotic/damaged cells may lead to** altered debris clearance and immune regulation; its contribution to clinical MBLD is inferred rather than established.
10. **Opposing branch: reduced lectin-pathway activation on ischemic or injured self-tissue may result in** less complement-mediated inflammatory injury, explaining possible protection in some ischemia–reperfusion and intracellular-pathogen settings.

### Molecular and cellular detail

Current mechanistic work places **MASP-1 upstream of MASP-2**: target-surface clustering causes MASP-1 autoactivation; activated MASP-1 is the physiological activator of MASP-2; MASP-2 then efficiently cleaves C4 and C2. A 2024 review describes this as the “current model” and notes that inhibiting MASP-1 can prevent MASP-2 activation. [305]

Structural variants compromise assembly of higher-order oligomers, thereby decreasing ligand binding and complement activation—demonstrated directly in vitro (PMID **14764589**):

> “Mutations in the collagenous region of human MBL compromise assembly of higher order oligomers, resulting in reduced ligand binding capacity and thus reduced capability to activate complement.” [57]

MBL also functions as a direct opsonin. In human macrophage experiments, MBL opsonization significantly increased capture and approximately doubled internalization of *N. meningitidis* (PMID **15569696**). [59]

### Suggested ontology annotations

| Level | Suggested terms |
|---|---|
| GO biological process | complement activation, lectin pathway **GO:0001867**; complement activation **GO:0006956**; innate immune response **GO:0045087**; phagocytosis **GO:0006909**; opsonization **GO:0008228**; defense response to bacterium **GO:0042742** |
| GO molecular function | carbohydrate binding **GO:0030246**; calcium-dependent protein binding **GO:0048306**; pattern-recognition receptor activity |
| GO cellular component | extracellular region **GO:0005576**; blood plasma/extracellular space **GO:0005615** |
| Cell Ontology | hepatocyte **CL:0000182**; neutrophil **CL:0000775**; macrophage **CL:0000235**; conventional dendritic cell **CL:0000990**; endothelial cell **CL:0000115** |
| Relevant molecules | MBL2, MASP1, MASP2, C4, C2, C3, C5–C9; D-mannose **CHEBI:16024**; N-acetyl-D-glucosamine **CHEBI:506227** |

The primary producing cell is the **hepatocyte**; downstream effector cells include neutrophils, monocytes/macrophages and dendritic cells. MBL is extracellular rather than a nuclear, mitochondrial, lysosomal or ER-storage disease protein. [414][95]

---

## 7. Anatomical structures affected

There is no fixed structural malformation. The fundamental defect is in a soluble plasma innate-immune protein.

| Level | Structure/cell/compartment | Interpretation and suggested ontology |
|---|---|---|
| Source organ | Liver | MBL is predominantly synthesized by hepatocytes; **UBERON:0002107**, liver; **CL:0000182**, hepatocyte. [91][414] |
| Primary medium | Blood/plasma | Site of circulating MBL–MASP complexes; **UBERON:0000178**, blood; extracellular space **GO:0005615** |
| Common clinical system | Respiratory tract and lung | Infection site rather than constitutively damaged target; respiratory system **UBERON:0001004**, lung **UBERON:0002048**. [418] |
| Secondary sites | Skin, meninges/CNS, gastrointestinal tract | Determined by the infecting organism |
| Effector cells | Neutrophils and macrophages | Reduced C3b/MBL-mediated microbial uptake; CL terms above |
| Subcellular/extracellular | Secretory pathway during synthesis; extracellular plasma after secretion | Deficiency is principally extracellular |
| Lateralization | None | Infections may be focal, but there is no intrinsic left/right preference |

---

## 8. Temporal development

- **Biochemical onset:** congenital and lifelong because the genotype is germline.
- **Clinical onset:** most characteristic from about **6–18 months**, when maternal antibody has waned; childhood infections are episodic rather than steadily progressive. [119][347]
- **Adult course:** most adults remain asymptomatic. Recurrent/severe adult infection is uncommon unless additional immunosuppression, lung disease, or another immune defect exists. [149]
- **Progression:** no formal stages. A practical course is: biochemical deficiency → asymptomatic carrier state or episodic infection → recurrent/severe infection under stress → possible secondary organ damage such as bronchiectasis.
- **Remission:** individual infections resolve spontaneously or with antimicrobials; susceptibility may become less clinically apparent as adaptive immunity matures.
- **Critical periods:** infancy, chemotherapy-induced neutropenia, transplantation, and periods of intensive immunosuppression.
- **Duration:** genotype and low-production tendency are lifelong; symptoms are intermittent and may disappear for years.

---

## 9. Inheritance and population epidemiology

### Epidemiology and inheritance

| Characteristic | Current understanding |
|---|---|
| Prevalence | Using <100 ng/mL, about **5% of European-descended populations** and **10% of sub-Saharan Africans**; estimates vary greatly with threshold. [194] |
| Partial/low levels | Approximately 20–25% carry a low-producing haplotype; broader cutoffs can label 25–30% deficient. [188][230] |
| Incidence | No reliable annual incidence because this is a stable biochemical trait, not a newly acquired disease. |
| Inheritance | OMIM lists autosomal dominant for chronic-infection susceptibility, older IUIS tables have used autosomal recessive, and MedlinePlus calls inheritance unclear. Functionally, alleles are codominant/additive, with one or two low-producing alleles reducing levels. [1][333][535] |
| Penetrance | Very low and context dependent; “most” adults are asymptomatic. [337] |
| Expressivity | Highly variable: undetectable protein without disease through recurrent respiratory infection to rare severe invasive infection |
| Anticipation | Not reported |
| Germline mosaicism | Not established and clinically irrelevant for common alleles |
| Consanguinity | May increase homozygosity but is not required because alleles are common |
| Sex ratio | No consistent male:female difference |
| Life-course distribution | Clinical enrichment in toddlers and secondarily immunocompromised people |

A population study with more than 9,000 adults and up to 24 years of morbidity follow-up found no significant increase in infectious morbidity or mortality, supporting very low penetrance in the general adult population. [475][479]

### Population-specific alleles

- B/Gly54Asp is common in Europeans and several Asian/Arctic populations, commonly around 0.11–0.17.
- C/Gly57Glu is concentrated in sub-Saharan African populations, around 0.23–0.29 in some cohorts.
- D/Arg52Cys occurs in both African and European populations at about 0.05.
- The distribution is compatible with balancing selection, pathogen-specific tradeoffs, drift, or founder effects rather than purifying selection against a severe fully penetrant disease. [376][378]

---

## 10. Diagnostics

### Practical diagnostic approach

1. **Confirm a clinically meaningful phenotype:** recurrent, severe, unusual, or invasive bacterial infection—not merely an incidental low result.
2. **Exclude more consequential causes:** complete blood count/differential; IgG, IgA, IgM and often IgG subclasses; vaccine-specific antibodies; HIV testing when relevant; CH50 and AH50/AP50; C3/C4; neutrophil function or lymphocyte testing as indicated.
3. **Measure serum MBL antigen**, preferably on more than one occasion if the result is borderline or obtained during acute inflammation.
4. **Measure functional lectin-pathway activity** using mannan-coated ELISA/C4b deposition or equivalent; <10% activity with preserved classical and alternative pathways supports a profound MBL-pathway defect.
5. **Use *MBL2* genotyping/haplotyping** when the biochemical defect is reproducible and clinical interpretation requires clarification.
6. Continue investigating cystic fibrosis, primary ciliary dyskinesia, airway obstruction, aspiration, allergy/asthma, antibody deficiency, other complement deficiency and chronic infection as clinically indicated. [236][441][446]

### Laboratory interpretation

| Test | Expected MBLD result | Limitations |
|---|---|---|
| Serum MBL by ELISA/immunoassay | Low; thresholds include <50, <75, <100, <400–500 or <600 ng/mL | No universally accepted cutoff; acute-phase changes and assay differences |
| Lectin-pathway functional assay | Low/absent mannan-dependent C4/C3 activation | Better functional readout but may also reflect MASP or other lectin-pathway defects |
| CH50 | Usually normal | Does not test the lectin pathway directly |
| AH50/AP50 | Usually normal | Excludes major alternative-pathway deficiency but not MBLD |
| C3/C4 | Usually normal between infections | Consumption may occur during acute inflammation |
| Microbiology | Organism-specific cultures/PCR | No MBLD-specific pathogen |
| Imaging | Chest radiograph/CT only when clinically indicated | No diagnostic imaging signature; CT assesses bronchiectasis/complications |

Mayo Clinic interprets **<10% lectin-pathway activity**, with normal classical and alternative pathways, as consistent with very low/absent MBL, while emphasizing that not all such individuals are symptomatic. [227]

ESID’s clinical working definition requires severe recurrent bacterial infection plus one of: MBL <75 µg/L, 75–399.9 µg/L functional deficiency, or 400–1,300 µg/L corresponding to milder heterozygous deficiency. These are registry working criteria rather than universally adopted practice guidelines. [526]

### Genetic testing

| Modality | Utility |
|---|---|
| Targeted common-variant/haplotype testing | Most clinically interpretable approach when biochemical deficiency is already demonstrated |
| Full *MBL2* sequencing | Available by Sanger or NGS; GTR lists coding-region sequencing and sequencing plus deletion/duplication analysis. [421][423] |
| Lectin-pathway panel | *MBL2*, *MASP2*, and *FCN3* panel is available where a broader pathway defect is suspected. [426] |
| WES/WGS | Low yield for isolated low MBL; useful only when a broader or unexplained inborn error of immunity is suspected |
| CMA/karyotype/FISH | Not indicated for isolated MBLD |
| mtDNA/repeat-expansion testing | Not applicable |
| Prenatal/preimplantation testing | Technically possible but generally not justified for common, low-penetrance alleles |

**Differential diagnosis:** antibody deficiency/specific antibody deficiency, common variable immunodeficiency, complement C2/C3/terminal-component or properdin deficiency, MASP2 or FCN3 deficiency, chronic granulomatous disease, neutropenia, HIV, cystic fibrosis, primary ciliary dyskinesia, anatomic airway obstruction, aspiration, and environmental exposure to infection.

**Screening:** not included in newborn screening, routine carrier screening, or population screening. Cascade testing is rarely useful because genotype poorly predicts clinical disease.

---

## 11. Outcome and prognosis

- **Life expectancy:** normal for isolated MBLD; no disease-specific five- or ten-year survival decrement has been established.
- **Mortality:** no excess in large unselected adult population studies. Mortality associations arise mainly in severe pneumococcal infection or major comorbid disease and should not be extrapolated to asymptomatic carriers. [475]
- **Recovery:** individual infections generally recover fully with appropriate treatment.
- **Morbidity:** recurrent antibiotic courses, missed school/work, hospitalization, and occasional secondary bronchiectasis are the main burdens.
- **Prognostic factors:** age under approximately two years; very low functional activity; coexisting antibody deficiency; neutropenia; chemotherapy; transplantation; cystic fibrosis/bronchiectasis; pathogen virulence; and delayed antimicrobial treatment.
- **Prognostic biomarkers:** serum MBL has limited standalone specificity. CRP and procalcitonin generally outperform it in acute pneumonia.

In a 2023 retrospective pneumonia cohort of 204 children, 37 had MBL <450 ng/mL. Low-MBL children had acute respiratory failure in 56.75% versus 11.97%, systemic complications in 83.78% versus 38.92%, ICU admission in 21.62% versus 2.39%, and median antibiotic duration of 14 versus seven days. However, MBL had only 25% specificity at a high-sensitivity ICU threshold, and retrospective acute-illness measurement cannot establish inherited MBLD as the cause. Published October 27, 2023. [481]

---

## 12. Treatment

There is **no approved treatment that routinely replaces MBL** and no genotype-specific pharmacotherapy. Management is phenotype driven.

| Intervention | Indication/strategy | Evidence/status | Suggested NCIt intervention concept |
|---|---|---|---|
| Observation and education | Asymptomatic or mild, infrequent infections | Most people require no regular treatment. [215] | Observation; patient education |
| Prompt organism-directed antimicrobial therapy | Breakthrough bacterial, fungal or viral infection | Standard of care; obtain cultures where feasible | Antibiotic therapy; antifungal therapy; antiviral therapy |
| Low-dose prophylactic antibiotics | Frequent/severe bacterial infections, school/work loss or impaired growth despite routine care | Individualized; no MBLD-specific randomized response rate | Antibiotic prophylaxis |
| Routine vaccination | Standard age-appropriate schedule | Maintains adaptive compensation | Vaccination |
| Annual influenza vaccination | Commonly advised | Expert/patient-organization guidance | Influenza vaccination |
| Pneumococcal, meningococcal and Hib vaccination | Particularly reasonable with severe/recurrent infection or broader complement concern | Extrapolated from complement-deficiency management; verify antibody responses | Pneumococcal vaccination; meningococcal vaccination; Hib vaccination |
| Immunoglobulin replacement | **Not for isolated MBLD** | Consider only if a separate antibody-production defect is demonstrated. [220] | Immunoglobulin replacement therapy |
| Pulmonary care | Bronchiectasis or chronic suppurative lung disease | Airway clearance, physiotherapy and disease-specific antibiotics per pulmonary guidelines | Respiratory therapy; chest physiotherapy |
| Surgery | No surgery treats MBLD | Procedures only for complications such as empyema/abscess or unrelated anatomic disease | Surgical procedure, complication-specific |

### Experimental replacement

A phase I study administered plasma-derived MBL to 20 deficient healthy adults: three weekly 6-mg IV doses produced immediate serum levels of 1,200–4,500 ng/mL without clinical/laboratory adverse effects; mean half-life was 69.6 hours. The investigators estimated that ≥6 mg two or three times weekly would be needed to maintain ~1,000 ng/mL. PMID **14723627**, January 2004. [198]

The pediatric study **NCT00886496** evaluated recombinant human MBL in MBL-deficient patients with chemotherapy-associated fever and neutropenia; it was phase I, nonrandomized, open-label, and designed primarily for safety/dose selection, not definitive clinical efficacy. [207] Plasma-derived replacement in 12 neutropenic children, trial **NCT00138736**, restored functional levels and appeared safe, but no robust infection-reduction endpoint established routine benefit. [208]

There is no established gene therapy, CRISPR therapy, RNA therapy, stem-cell transplant indication, monoclonal-antibody replacement, or MBL-targeted pharmacogenomic algorithm.

---

## 13. Prevention

| Prevention level | Recommendations |
|---|---|
| Primary | Routine hygiene, standard vaccination, annual influenza vaccination where advised, smoking avoidance and ordinary respiratory-health measures; these prevent infection rather than the genotype |
| Secondary | Evaluate patients with severe/recurrent infection early; confirm functional deficiency and look for coexisting antibody/complement defects |
| Tertiary | Prompt culture-directed therapy, prophylactic antibiotics for selected frequent infections, pulmonary monitoring and airway clearance if chronic lung disease develops |
| Peri-immunosuppression | Recognize possible increased risk during chemotherapy/transplantation; standard neutropenic and transplant infection prophylaxis takes priority |
| Genetic counseling | Explain low penetrance, variable inheritance and common population frequency; genotype does not reliably predict whether a relative will be ill |
| Reproductive testing | Usually not indicated because isolated MBLD is common and generally mild |
| Population screening | Not recommended |
| Public health | No MBLD-specific sanitation or vector-control program; ordinary vaccination and infection-control policies apply |

Patients should seek urgent evaluation for fever with toxicity, dyspnea, neck stiffness, altered consciousness, or suspected sepsis. Vaccination is supportive rather than curative; most vaccines are considered safe in isolated MBLD. [211][214]

---

## 14. Other species and naturally occurring disease

| Species | Taxonomy and ortholog | Natural/comparative findings |
|---|---|---|
| House mouse, *Mus musculus* | NCBI Taxon **10090**; *Mbl2* Gene **17195**, plus the distinct *Mbl1* locus | Mice have two functional MBL forms, MBL-A and MBL-C, unlike humans’ single expressed *MBL2* product; double deficiency is therefore required to model human profound MBLD. [457][465] |
| Norway rat, *Rattus norvegicus* | Taxon **10116**; *Mbl2* Gene **64668** | Conserved lectin-pathway biology; mainly experimental rather than recognized natural veterinary syndrome. [455][456] |
| Domestic pig, *Sus scrofa* | Taxon **9823**; *MBL2* Gene **397230** | Promoter polymorphisms lowering hepatic MBL-C expression were more frequent in pigs with pneumonia, enteritis, serositis or septicemia, but this is association rather than a well-defined Mendelian veterinary disease. [279][459] |
| Cattle, *Bos taurus* | Taxon **9913**; *MBL2* Gene **281297** | Variants have been studied for mastitis/infectious-disease susceptibility; North American data did not consistently validate disease association. [276][452][453] |

No established breed-specific VBO annotation or well-validated OMIA entry equivalent to human MBLD was identified. There is no transmission or zoonotic potential: inherited MBLD is a host genotype, not an infectious disease.

---

## 15. Model organisms and experimental systems

| Model | Phenotype recapitulated | Applications and limitations |
|---|---|---|
| *Mbl1/Mbl2* double-knockout mouse | Absent MBL–MASP pathway and increased susceptibility to selected infections | Best-established model of profound deficiency; limitation: mice normally have two MBL genes, humans one |
| IV *S. aureus* challenge in double-knockout mice | 100% mortality by 48 hours versus 45% mortality in wild type; impaired control of bacteremia | Demonstrates causal host-defense function and provides a replacement-therapy model; challenge is more severe than most human exposure. PMID corresponding to J Exp Med 2004 study; DOI 10.1084/jem.20032207. [269] |
| Neutropenic double-knockout mouse | Persistent bacteremia and higher tissue burden after cyclophosphamide plus infection | Recapitulates the human gene–environment interaction with chemotherapy-induced neutropenia. [256] |
| Recombinant-MBL rescue | Recombinant human MBL restores mortality toward wild-type levels in infected knockout mice | Strong evidence that the knockout phenotype is MBL dependent. [262] |
| Influenza, HSV-2 and *P. aeruginosa* challenge | Greater susceptibility in some MBL-null models | Useful for pathogen-specific innate immunity; results are not uniform across organisms or strains. [262] |
| Systemic aspergillosis | No greater susceptibility and, at low inoculum, possible relative protection | Demonstrates pathogen-dependent tradeoffs and limits broad claims that deficiency is uniformly harmful. PMID **20064561**. [260] |
| Ischemia–reperfusion models | Reduced injury in MBL-null kidney, skin, intestine, heart and some brain models | Tests harmful complement activation; e.g., skin necrosis 10.6% in MBL-null versus 43.1% in wild type. [242] |
| Transfected/cell-free MBL variant systems | Measures secretion, oligomerization, mannan binding, MASP binding and C4 activation | Defines molecular effects of B/C/D variants but does not model low clinical penetrance |
| Human macrophage assays | MBL-enhanced uptake of *N. meningitidis* | Directly supports opsonic mechanism but lacks whole-organism immune redundancy. PMID **15569696**. [59] |

No disease-specific human iPSC, organoid, Drosophila, zebrafish, *C. elegans*, yeast, spatial-transcriptomic, or CRISPR-screen model has become standard.

---

## Overall evidence assessment

1. **High-confidence biochemical conclusion:** common *MBL2* structural and regulatory alleles can markedly reduce functional oligomeric MBL and lectin-pathway complement activation.
2. **High-confidence clinical conclusion:** biochemical deficiency is common and usually asymptomatic; clinical penetrance is low.
3. **Moderate-confidence conclusion:** susceptibility becomes clinically relevant in a subset of young children and in people with secondary immunosuppression or another immune defect.
4. **Uncertain/heterogeneous conclusion:** isolated MBLD as a sufficient explanation for recurrent respiratory infection. The positive 2022 multicenter genotype cohort and negative 2023 five-year outcome cohort illustrate the unresolved evidence. [106][36]
5. **Clinical implication:** do not stop the immune work-up after finding low MBL. Confirm functional significance, search for more consequential immune or structural disorders, and treat the patient’s infection phenotype rather than the genotype alone.
6. **Knowledge-base classification recommendation:** retain MONDO:0013714/OMIM:614372 with *MBL2* as the causal gene, but annotate **incomplete/very low penetrance, variable expressivity, common hypomorphic alleles, and strong gene–environment interaction** rather than presenting it as a conventional fully penetrant Mendelian immunodeficiency.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (2 mentions) - replaced by `GO:0005576`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

35 of 39 terms resolved to a current term; the rest could not be looked up either way.