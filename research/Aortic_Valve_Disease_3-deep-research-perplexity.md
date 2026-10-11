---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-11T20:05:42.094025'
end_time: '2026-10-11T20:09:52.474507'
duration_seconds: 250.38
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Aortic Valve Disease 3
  mondo_id: MONDO:0032783
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
citation_count: 57
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 27
  on_topic: 15
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 10
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - OMIM
  - Gene
  - PMIDs
  - MGI
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aortic Valve Disease 3
- **MONDO ID:** MONDO:0032783 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Aortic Valve Disease 3** covering all of the
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

# Aortic valve disease 3 (AOVD3): disease-characteristics research report

**Aortic valve disease 3 (AOVD3; MONDO:0032783; OMIM:618496) is a proposed autosomal-dominant, ROBO4-associated cardiovascular disorder.** Its reported manifestations include bicuspid aortic valve (BAV), aortic valve stenosis, aneurysm of the aortic root or ascending aorta, and, in one family, atrial septal defect. The principal evidence is a 2019 study of two families supported by cell and animal experiments. **The gene–disease association should not be entered as unequivocally established:** a GenCC submission classifies *ROBO4*–AOVD3 evidence as **limited**, and interpretation of at least one original familial variant remains disputed. [3][31][47][46]

*Evidence notation used below:* **human** denotes patient, family, or cohort observations; **experimental** denotes cultured-cell or animal findings; **inference** denotes a plausible link not directly established for AOVD3. PMID-linked primary articles are identified alongside citations. General BAV data are explicitly distinguished from ROBO4-specific data.

## 1. Disease information and identifiers

| Identifier or name | Entry and interpretation |
|---|---|
| Preferred name | Aortic valve disease 3; **AOVD3**. [73] |
| MONDO | **MONDO:0032783**. [73] |
| OMIM | **618496**, phenotype; **607528**, *ROBO4* gene. [3] |
| MedGen | **1681142**; UMLS concept **C5193127**. [73] |
| Other names | “Aortic valve disease-3”; MedGen also indexes “aortic valve stenosis” and “bicuspid aortic valve.” The latter two describe **features, not unique synonyms** for this genetic subtype. [73] |
| MeSH | **D000082862**, *Aortic Valve Disease*, a **broader** descriptor; not AOVD3-specific. [286] |
| ICD-10-CM | No verified AOVD3-specific code. Code the documented manifestation: **Q23.81** for BAV, **Q23.0** for congenital aortic-valve stenosis, or **I35.0** for nonrheumatic aortic-valve stenosis when applicable. Q23.81 has been effective since October 1, 2024. Coding depends on the clinician’s documentation; these codes are not interchangeable genetic diagnoses. [316][329][288] |
| ICD-11; Orphanet disease number | No AOVD3-specific identifier verified in the reviewed sources. |

This report synthesizes **aggregated disease resources and published research**, not individual-level electronic health records. Published family descriptions and tissue experiments originate from individual participants, but they do not constitute a population registry. OMIM’s concise description is: “Aortic valve disease-3 (AOVD3) is characterized by aortic stenosis and/or bicuspid aortic valve (BAV), associated in some patients with aneurysm of the aortic root and/or ascending aorta.” [3][31]

**Principal primary source:** Gould and colleagues, *Nature Genetics* **51:42–50** (published online **November 19, 2018**; January 2019 issue), **PMID:30455415**, DOI **10.1038/s41588-018-0265-y**, https://pubmed.ncbi.nlm.nih.gov/30455415/. Its abstract states: “we report the identification of variants in ROBO4 … that segregate with disease in two families.” [32][31]

## 2. Etiology: causes, risks, protection, and interactions

**Proposed initiating cause.** Heterozygous **germline** *ROBO4* variants are the defining genetic hypothesis for AOVD3. In the original families, one variant disrupts exon-13 splicing; another changes the extracellular receptor residue Arg64. The phenotype is not synonymous with every case of BAV: BAV has many genetic and non-genetic contributors, and current *ROBO4* evidence does not justify assigning AOVD3 to a person solely because BAV is present. [31][3][47][84]

| Factor | AOVD3-specific finding or evidence boundary |
|---|---|
| Family history and genotype | Transmission in the two reported families was compatible with autosomal dominance. Two apparently unaffected female carriers in the larger family establish **incomplete observed penetrance**; absence of imaging in some ostensibly unaffected relatives is a general limitation of BAV-family research. **Human; PMID:30455415.** [3][31][110] |
| Sex | Seven of eight affected members of the larger original family were male. This is a **small, ascertainment-dependent family count**, not an AOVD3 population sex ratio. **Human; PMID:30455415.** [3][31] |
| Other genes | *NOTCH1, SMAD6,* and other BAV/aneurysm genes are **alternative etiologies or candidate co-contributors**, not demonstrated AOVD3 modifier genes. A 2024 BAV exome study found multiple candidate variants in some probands, but did not establish an AOVD3-specific modifier. **Human; PMID:39226896.** [21][110] |
| Age, hypertension, smoking, hemodynamic load | Clinically relevant to aortic or valvular disease management; **no quantified interaction with a specific AOVD3 allele** has been established. Blood-pressure control and smoking cessation are general thoracic-aneurysm measures, not demonstrated protection against congenital BAV. [21] |
| Protective genetic or environmental factors | **None validated for AOVD3.** No protective *ROBO4* allele, diet, supplement, or exposure has been shown to prevent this Mendelian phenotype. [31][47] |
| Infection, toxins, radiation, occupation | **Not demonstrated initiating causes of AOVD3.** A 2024 radiation experiment concerned bone-marrow endothelium, **not radiation-induced AOVD3**. **Experimental; PMID:38383474.** [77] |

**Gene–environment interaction:** The family study suggests that unidentified genetic and/or environmental influences may affect penetrance, but it did **not** measure a particular exposure–*ROBO4* interaction. A 2024 study shows how inflammation can expose another ROBO4-dependent endothelial response; extrapolating that response to aortic-valve progression remains an **inference**, not a demonstrated AOVD3 mechanism. **Experimental; PMID:38762541.** [31][107]

## 3. Phenotypes

The table separates **observed AOVD3-family findings** from HPO terms indexed to the condition. Denominators below describe the reported families, **not validated disease-wide frequencies**. Typical symptom-onset ages, quantitative severity distributions, and phenotype-specific quality-of-life scores have not been established for AOVD3. A congenital valve shape can remain clinically silent until later dysfunction; aneurysm may likewise be detected by imaging before symptoms. **Human; PMID:30455415.** [31][73]

| Phenotype; suggested HPO | Type and documented characteristics | Reported frequency, course, and functional impact |
|---|---|---|
| **Aortic-root aneurysm — HP:0002616** | Imaging/anatomical sign; arose in **8/8 described affected members of family 1**. The paper does not establish an AOVD3-wide onset age or growth rate. [3][158] | Four were described as isolated root aneurysms; others had additional ascending-aortic or valve findings. Usually asymptomatic until advanced; surveillance and possible surgery affect daily life. **The latter impact is a clinical inference**, not an AOVD3 QOL measurement. [3][21] |
| **Ascending tubular-aorta aneurysm — HP:0004970** | Imaging/anatomical sign accompanying root and/or valve disease in some family-1 members; severity and progression varied. [3][92] | **No reliable subtype percentage.** Aneurysm carries potential future dissection risk, but the original families do not provide an AOVD3-specific dissection rate. [3][21] |
| **Bicuspid aortic valve — HP:0001647** | Congenital anatomical sign; cusp-fusion patterns differed between the families. [3][70] | Two family-1 members had reported BAV; the affected son in family 2 had BAV. May be asymptomatic or lead to valve dysfunction and activity limitation. **Human; PMID:30455415.** [3][31] |
| **Aortic valve stenosis — HP:0001650** | Clinical/imaging sign of restricted outflow; reported in both families, with some affected members requiring valve replacement. [3][156] | **No disease-wide percentage or onset distribution.** Severe stenosis may cause exertional limitation, syncope, heart failure, or the need for intervention; these are **general stenosis consequences**, not individually quantified AOVD3 symptoms. [3][276] |
| **Atrial septal defect — HP:0001631** | Congenital structural finding in the **mother and son of family 2**; ASD subtype not established. [3][162] | **2 reported individuals**, not a prevalence estimate. Potential effect depends on defect size and shunt; no AOVD3-specific functioning data. [3] |
| **Aortic regurgitation — HP:0001659** | Valve functional abnormality reproduced in *Robo4*-deficient **mice**; not a well-quantified human AOVD3 phenotype in the original pedigrees. [31][157] | Human frequency **unknown**; avoid transferring mouse penetrance to patients. [31] |
| **Ascending aortic dissection — HP:0004933** | Indexed in MedGen’s AOVD3 HPO feature list, but **not established as a recurrent event in the original two pedigrees**. [73][91][3] | A serious potential aneurysm complication; **AOVD3 incidence unknown**. [21] |

Valve thickening/fibroproliferation and medial elastic-fiber abnormalities were **pathology findings in studied tissue**, not measured population phenotypes. No reproducible AOVD3-specific behavioral, psychiatric, biochemical-laboratory, EQ-5D, SF-36, or PROMIS phenotype has been reported. **Human; PMID:30455415.** [31]

## 4. Genetic and molecular information

**Gene annotation:** *ROBO4* (*roundabout guidance receptor 4*), **HGNC:17985**, **NCBI Gene:54538**, **OMIM:607528**, **UniProt:Q8WZ75**, chromosome **11q24.2**. Its encoded endothelial-associated receptor is the proposed affected protein. The familial findings are **germline**, not tumor-acquired somatic variants. **Human and experimental; PMID:30455415.** [61][3][31]

| *ROBO4* variant reported in the discovery study | Evidence and population observation | Interpretation for a knowledge base |
|---|---|---|
| **c.2056+1G>T**, splice-donor-site variant, family 1 | Eight affected and two apparently unaffected carriers; patient-fibroblast cDNA showed exon-13 skipping and an in-frame transcript lacking **36 intracellular amino acids**. Absent from the ExAC dataset used in the study. **Human/functional; PMID:30455415.** [31] | Strongest original segregation-and-splicing example, but evaluate the specific current transcript, ClinVar submission, and gene–disease validity before calling it clinically pathogenic. The **+1** position denotes a *donor* site even though some prose labels it “acceptor.” [31][47] |
| **c.190C>T; p.Arg64Cys**, family 2 and an additional proband | Affected mother and son; altered endothelial-cell behavior in culture; **19/98,998 ExAC alleles** in the original article, approximately **0.00019**. **Human/in vitro; PMID:30455415.** [31][46] | **Conflicting ClinVar interpretations:** one contributing likely-pathogenic submission and one contributing **VUS** submission; a literature-only pathogenic entry does not resolve the conflict. ClinVar variation **560394** reports gnomAD frequency about **0.00019**. Do **not** silently label this variant definitively pathogenic. [46] |
| **c.283G>A; p.Ala95Thr** | Rare discovery-cohort proband variant; **5/117,304 ExAC alleles**. [31] | Candidate association; independent variant-level causation unproven. |
| **c.695C>T; p.Thr232Met** | Rare discovery-cohort variant; **10/121,068 ExAC alleles**. [31] | Candidate; not equivalent to a proven AOVD3 diagnosis. |
| **c.1233T>A; p.His411Gln** | Discovery-cohort variant; absent from the referenced ExAC dataset. [31] | Candidate; variant-level pathogenicity unproven. |
| **c.1702C>T; p.Arg568Ter** | Predicted stop-gain; **12/120,920 ExAC alleles**. [31] | Predicted truncation, but functional consequence and clinical causation require variant-specific assessment. |
| **c.740T>C; p.Val247Ala** | Resequencing-cohort variant; **1/121,370 ExAC alleles**. [31] | Candidate; unproven. |
| **c.839A>C; p.Tyr280Ser** | Resequencing-cohort variant; **5/117,546 ExAC alleles**. [31] | Candidate; unproven. |
| **c.1601_1614del; p.Gly534Glufs*49** | Predicted frameshift; absent from referenced ExAC dataset. [31] | Candidate predicted loss of function; clinical classification needs review. |
| **c.1864G>C; p.Asp622His** | Reported in **two probands**; **4/110,004 ExAC alleles**. [31] | Candidate; recurrence alone does not establish pathogenicity. |
| **c.2245_2246delinsCT; p.Ala749Leu** | Resequencing-cohort candidate; absent from referenced ExAC dataset. [31] | Candidate; unproven. |

The study found filtered rare *ROBO4* variants in **13/736 probands (1.77%)**, versus **one variant among 376 controls** (*P*=0.0432). That is an **enrichment in a selected BAV/ascending-aneurysm cohort**, neither AOVD3 prevalence nor the diagnostic yield of *ROBO4* testing in an unselected population. **Human; PMID:30455415.** [3][31]

**Updated evidence:** In a separate early-complication cohort, *ROBO4* had **three candidate variants among 63 probands** (gene-level comparison *P*=0.062); variants were **not significantly enriched** among the 60 BAV-plus-heritable-aortic-disease probands. **Human; Musfee et al., 2020, PMID:32748548**, https://pubmed.ncbi.nlm.nih.gov/32748548/. A peer-reviewed **2024** exome analysis of **215 early-onset BAV families** identified **one predicted *ROBO4* loss-of-function variant**; it did not establish variant-specific AOVD3 penetrance. **Human; Mansoorshahi et al., published online September 2, 2024, PMID:39226896**, https://pmc.ncbi.nlm.nih.gov/articles/PMC11480851/. [34][301][110][108]

No AOVD3-specific **validated modifier gene, epigenetic signature, recurrent chromosomal rearrangement, or somatic mutation** was established in these sources. Other BAV-associated genes are important for the **differential diagnosis**, not automatically genes causing the OMIM-defined *ROBO4* subtype. [31][110][21]

## 5. Environmental information

AOVD3 is **not an infectious or zoonotic condition**, and no pathogen, toxin, occupational exposure, radiation dose, diet, smoking exposure, or alcohol intake has been demonstrated to initiate the *ROBO4*-defined disorder. Hypertension and smoking remain clinically actionable **general aortic-disease risks**; controlling them should not be represented as reversing a congenital valve malformation. The 2022 ACC/AHA aortic guideline recommends treatment of hypertension in patients with thoracic aortic aneurysm and smoking-cessation efforts in those who smoke. [31][21]

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Heterozygous *ROBO4* sequence variation leads to altered ROBO4 transcript or receptor structure:** exon-13 skipping is **demonstrated** for c.2056+1G>T; p.Arg64Cys changes an extracellular immunoglobulin-like domain. **Human; PMID:30455415.** [31]
2. **Reduced or altered ROBO4 activity leads to weaker endothelial junctions and barrier function:** *ROBO4* silencing or mutant expression reduced **CDH5/VE-cadherin** and **TJP1** and increased dextran passage across cultured aortic-endothelial monolayers. **In vitro; PMID:30455415.** [31]
3. **Barrier disruption leads to a more invasive, mesenchymal-like endothelial state:** cultured cells became elongated, expressed more **SNAI1** and **α-smooth-muscle actin**, and invaded more readily. This is **evidence suggestive of EndMT**, not proof that every human lesion undergoes complete lineage conversion. **In vitro; PMID:30455415.** [31]
4. **Branch A — developing valve:** altered endocardial/endothelial behavior **is inferred to lead to** abnormal valve formation, including BAV; ROBO4 is expressed in developing mouse endocardial cushions, and deficient mice develop valve anomalies. Direct observation of the entire developmental chain in a human embryo is **not available**. **Experimental plus inference; PMID:30455415.** [31]
5. **Branch B — aortic wall:** impaired endothelial barrier and mesenchymal-like remodeling **are inferred to lead to** albumin entry, intimal fibrosis, collagen accumulation, and medial elastin disorganization. These downstream abnormalities were **observed in one patient’s aneurysmal tissue**; their precise order was not experimentally established in that patient. **Human plus inference; PMID:30455415.** [31]
6. **Abnormal valve geometry and/or aortic-wall remodeling results in** stenosis or other valve dysfunction and aortic-root/ascending-aortic aneurysm; consequent ventricular pressure load or future dissection risk is a **clinical extrapolation** when applied to an individual AOVD3 carrier. **Human/experimental/inference; PMID:30455415.** [3][31][21]

**Upstream versus downstream.** The receptor and endothelial-junction abnormalities are upstream hypotheses; fibroproliferation, elastin damage, altered valve flow, and aneurysm are downstream findings. In the studied aneurysmal aorta, investigators observed diminished endothelial ROBO4 staining, albumin beyond the endothelial surface, collagen-rich intimal/superficial-medial remodeling, and fragmented elastic fibers. These are more direct disease-tissue observations than any proposed named signaling cascade. **Human; PMID:30455415.** [31]

| Mechanistic annotation | Supported finding and appropriate ontology suggestion |
|---|---|
| Cell populations | Aortic **endothelial cell, CL:0000115**, is directly studied; developing valve endocardial/endothelial cells are implicated by mouse expression. Aortic medial smooth-muscle and valve interstitial cells participate in tissue remodeling, but were **not proved to be the primary ROBO4-mutant cellular origin**. [31][122] |
| Biological processes | **GO:0061028, establishment of endothelial barrier**; **GO:0007155, cell adhesion**; **GO:0140074, cardiac endothelial-to-mesenchymal transition**, as a **suggested process annotation**, not proof of completed human EndMT. [31][182][185][129] |
| Cellular components | ROBO4-associated **plasma membrane, GO:0005886**; affected junctions **adherens junction, GO:0005912**; remodeled **extracellular matrix, GO:0031012**. These are localization/process suggestions, not demonstrations that the familial variants redistribute ROBO4 to a specific organelle. [31][181] |
| BMP, NOTCH, TGF-β | Original aortic-endothelial experiments found **modest reductions** in BMP- and NOTCH-responsive markers after *ROBO4* silencing, **without altered measured TGF-β responses**. No single predominant cascade was established for AOVD3. **In vitro; PMID:30455415.** [31] |

**Relevant 2024 research, with strict disease boundaries.** In irradiated **bone-marrow** endothelial-cell experiments, ROBO4 depletion augmented endoglin/SMAD, PI3K–AKT–mTOR, and NF-κB-associated responses. **Experimental; PMID:38383474**, published **February 2024**, https://pmc.ncbi.nlm.nih.gov/articles/PMC10881562/. These pathways **must not be entered as demonstrated AOVD3-valve pathways**. In another **2024** study, endothelial ROBO4 promoted TRAF7-associated IQGAP1 ubiquitination, limited prolonged RAC1 signaling and **PTGS2/COX-2** expression, and restrained inflammatory permeability. Its human endothelial RNA-seq experiment is deposited as **GEO:GSE231460**; it did **not** test AOVD3 valves. **Experimental; PMID:38762541**, published **May 18, 2024**, https://pubmed.ncbi.nlm.nih.gov/38762541/. No AOVD3-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or CRISPR-screen signature was verified. [77][107]

## 7. Anatomical structures affected

| Level | Site or cell; suggested ontology | Evidence and localization |
|---|---|---|
| Primary cardiac | **Aortic valve, UBERON:0002137** | Abnormal leaflet/cusp morphology and sometimes stenosis; left-sided valve, not a bilateral organ. [3][213] |
| Primary vascular | **Aortic root, UBERON:0004178**; **ascending aorta, UBERON:0001496**; parent **aorta, UBERON:0000947** | Root or ascending-aortic aneurysm; the original study examined intima and superficial media. These are anatomically localized lesions, not “left-” versus “right-sided” disease. [3][31][205][200] |
| Associated cardiac | **Heart, UBERON:0000948**, including the interatrial septum | ASD was described in family 2; the left ventricle may be affected **secondarily** by significant valve dysfunction. [3][221][135] |
| Tissue and subcellular | Endothelium **CL:0000115**; valve/endocardial tissue; aortic-wall connective tissue, extracellular matrix **GO:0031012**, plasma membrane **GO:0005886** | Human tissue and cultured-cell observations support these annotations. There is **no demonstrated AOVD3-specific mitochondrial, lysosomal, or ER lesion**. [31][122][181] |

## 8. Temporal development

BAV and ASD are **congenital structural abnormalities**; clinically important stenosis or aneurysm may become evident later. The small published AOVD3 families do **not** establish a median diagnosis age, annual aortic-growth rate, time to valve replacement, or age-specific penetrance. The practical course is therefore **potentially lifelong and variably progressive**, rather than a proven fixed-stage syndrome. There is no demonstrated spontaneous remission of a congenital BAV or established aneurysm. **Human; PMID:30455415.** [3][31]

For context **only**, a general prospective BAV cohort cited by the aortic guideline had mean ascending-aortic growth of **0.47 mm/year** over **4.8 years**; those figures **cannot be assigned to ROBO4 carriers**. The key intervention windows are identification of familial structural disease before complications and surveillance while aortic size, growth, and valve severity still permit planned treatment. [21]

## 9. Inheritance and population

| Characteristic | AOVD3-specific conclusion |
|---|---|
| Inheritance | **Autosomal dominant pattern proposed** in the reported families; **HP:0000006** is the relevant inheritance annotation. **Human; PMID:30455415.** [3][47] |
| Penetrance and expressivity | **Incomplete observed penetrance**: two apparently unaffected female carriers of the splice variant; manifestations varied between aneurysm, valve disease, and ASD. A numerical lifetime penetrance is **unavailable**. [3][31] |
| Anticipation, germline mosaicism, founder effect, consanguinity | **None demonstrated for AOVD3.** [3][31] |
| AOVD3 prevalence, incidence, carrier frequency | **Unknown.** The discovery study’s **13/736 (1.77%)** filtered-variant fraction is **not** disease prevalence, incidence, or a population carrier estimate. [3][31] |
| Sex, ancestry, geography | Family 1’s **7 affected males and 1 affected female** do not establish a population ratio or ancestry-specific rate. No AOVD3 geographic distribution is established. [3] |
| Broader BAV comparator | BAV occurs in approximately **1%** of the population and shows about **2:1–3:1 male predominance** in the aortic guideline; neither statistic is specific to AOVD3. [21] |

## 10. Diagnostics and screening

**Clinical diagnosis starts with anatomy and physiology, not a *ROBO4* result.** Transthoracic echocardiography (**TTE**) assesses cusp morphology, stenosis/regurgitation, aortic root and ascending-aortic size, and associated defects. Obtain appropriately gated **CT or MRI** when echocardiography cannot adequately define the thoracic aorta. ECG, symptom assessment, exercise testing in selected valve patients, and BNP when clinically appropriate address functional impact or intervention timing; none is an AOVD3-specific molecular biomarker. Aneurysmal-tissue histology can reveal remodeling but is **not a routine diagnostic biopsy**. [21][276][31]

| Diagnostic approach | Appropriate use and limitation |
|---|---|
| Family history and examination | Obtain multigenerational history of valve disease, thoracic aneurysm/dissection, and unexplained early death; examine for syndromic features suggesting another aortopathy. [21] |
| Targeted cardiovascular imaging | TTE first; CT/MRI if necessary. Screen first-degree relatives of a BAV patient with a dilated root/ascending aorta; screening relatives of a BAV patient without dilation is also considered reasonable. [21] |
| Multigene sequencing panel | For aneurysm/dissection with heritable-aortic-disease risk factors, genetics assessment and an appropriate **multigene panel** are preferable to assuming *ROBO4*. Interpret established HTAD genes and BAV candidates according to each gene–disease evidence level. The guideline names *ROBO4* among BAV-associated-aortopathy genes, but its **confirmed, highly penetrant HTAD-gene list does not include it**. [21][47] |
| Single-gene testing; WES/WGS | Family-variant testing can be considered **after expert classification** of a credible familial variant. WES/WGS may investigate unresolved familial disease, but detection of a rare *ROBO4* variant alone is not diagnostic; WES found the original families and a separate candidate in a 2024 cohort. **Human; PMIDs:30455415, 39226896.** [31][110] |
| CMA, karyotype, FISH, mitochondrial or repeat-expansion testing | **Not established routine tests for isolated AOVD3**; investigate when a different syndromic or chromosomal diagnosis is suspected. [3][21] |
| RNA, protein, and other omics | Patient-fibroblast cDNA confirmed exon-13 mis-splicing in research. No validated AOVD3 clinical RNA-seq, proteomic, metabolomic, epigenomic, or liquid-biopsy assay was identified. **Experimental; PMID:30455415.** [31] |

**Differential diagnosis:** other familial BAV etiologies, syndromic or nonsyndromic heritable thoracic-aortic disease, isolated congenital BAV, and acquired calcific or rheumatic valve disease. Phenotype, family history, aortic imaging, and carefully interpreted molecular findings distinguish them; a **VUS must not direct cascade testing or aortic surgery**. There is no AOVD3 population newborn-screening program. [21][46][47]

## 11. Outcomes and prognosis

**No AOVD3-specific survival curve, five- or ten-year survival percentage, life-expectancy estimate, mortality rate, validated prognostic biomarker, or patient-reported quality-of-life series was found.** In the original family 1, **three members had undergone aortic valve replacement**, demonstrating substantial morbidity in some carriers but not a treatment rate for all AOVD3 patients. **Human; PMID:30455415.** [3]

Risk assessment must instead use the **observed valve and aortic phenotype**: severity of stenosis or regurgitation, symptoms and ventricular function, aortic diameter and growth, family dissection history, and relevant coarctation or root phenotype. Even after isolated valve replacement, patients with BAV-related aortopathy can experience later aortic events; lifelong surveillance may be necessary. General BAV outcome statistics are **not *ROBO4*-specific prognostic estimates**. [21][276]

## 12. Treatment and real-world implementation

**No drug, gene therapy, RNA therapy, cell therapy, or immunotherapy has been shown to correct the *ROBO4* defect or prevent AOVD3 itself.** Care follows the measured valve and aortic abnormalities through a cardiology/valve-and-aorta team; the intervention names below are **suggested NCIT search labels**, not asserted NCIT codes. [21][47]

| Intervention; suggested NCIT label | Clinical use, outcome, and limitation |
|---|---|
| **Echocardiographic surveillance**; “Echocardiography” | Track valve function and root/ascending-aortic diameter. With BAV and a root or ascending aorta **≥4.0 cm**, guideline-recommended lifelong imaging intervals depend on size and growth, including after valve surgery. [21] |
| **Blood-pressure treatment**; “Antihypertensive Therapy” | For thoracic aortic aneurysm with average BP **≥130/80 mm Hg**, antihypertensive medication is recommended; beta blockers are reasonable to reach BP goals, and an angiotensin-receptor blocker may be an adjunct. **No ROBO4 genotype-specific response or pharmacogenomic rule is established.** [21] |
| **Valve repair or surgical aortic-valve replacement**; “Aortic Valve Repair,” “Aortic Valve Replacement” | Consider according to symptomatic severe valve disease, ventricular function, anatomy, and multidisciplinary assessment; three original-family members underwent valve replacement. Surgery treats the lesion **without correcting inherited susceptibility**. **Human; PMID:30455415.** [3][276] |
| **Transcatheter aortic-valve intervention**; “Transcatheter Aortic Valve Replacement” | A possible **general severe-stenosis** option after shared decision-making; BAV morphology, aortopathy, age, operative risk, and durability matter. It is **not an established ROBO4-directed intervention**. [271][278] |
| **Aortic-root/ascending-aorta replacement**; “Aortic Aneurysm Repair” | Under ACC/AHA BAV-aortopathy guidance, recommended at **≥5.5 cm**; reasonable at **5.0–5.4 cm plus a dissection risk factor**, or **≥4.5 cm** when concomitant surgical valve repair/replacement is undertaken at an experienced center. Indexed size and other circumstances can change decisions. These are **BAV guidance, not validated ROBO4-specific thresholds**. [21] |
| **Genetic counseling and relative assessment**; “Genetic Counseling” | Explain uncertain penetrance and gene–disease validity; use expert-classified pathogenic/likely pathogenic variants for appropriate cascade testing while retaining clinically indicated **imaging of relatives even when testing is negative or uncertain**. [21][47][46] |
| **Symptom-directed rehabilitation/support**; “Cardiac Rehabilitation” | Tailor physical activity and recovery support to valve severity, aortic dimensions, and any intervention. No AOVD3-specific rehabilitative trial, response percentage, or adverse-event rate was established. [21][276] |

Surgical and transcatheter procedures have material general risks, including procedural complications and later prosthesis-related follow-up; the reviewed evidence supplies **no AOVD3-stratified response or adverse-event rate**. No verified AOVD3-specific interventional trial or NCT identifier supports an experimental treatment recommendation. [21][31]

## 13. Prevention

**Primary prevention of an inherited valve malformation is not established.** No vaccine or antimicrobial prophylaxis prevents AOVD3, and no proven protective allele or lifestyle regimen prevents transmission or congenital BAV. Genetic counseling can discuss the proposed dominant inheritance and reproductive options **without presenting an unvalidated variant as predictive**. [3][47][21]

**Secondary prevention** consists of imaging the affected person and appropriately screening at-risk first-degree relatives, then following valve severity and aortic size. **Tertiary prevention** consists of BP control, smoking cessation when relevant, planned intervention when guideline criteria are met, and continued post-intervention aortic imaging. There is **no AOVD3-specific population or newborn-screening program**; this is targeted clinical and family surveillance. [21]

## 14. Other species and naturally occurring disease

| Species; NCBI Taxon | Natural disease or ortholog finding | Relevance and evidence boundary |
|---|---|---|
| **Human, *Homo sapiens*; 9606** | Proposed AOVD3 gene *ROBO4*, **NCBI Gene:54538**. [61][31] | The genetically defined condition in this report. |
| **Dog, *Canis lupus familiaris*; 9615** | Rare naturally occurring **BAV** has been reported, including a German Shepherd dog and an English Bulldog; canine *ROBO4* ortholog **NCBI Gene:489306**. [245][243][242] | **No demonstrated canine *ROBO4*-caused AOVD3** and no validated ROBO4-associated breed/VBO designation. Natural BAV is a comparative *phenotype*, not proof of the same molecular disease. |
| **Cat, *Felis catus*; 9685** | OMIA lists a natural **bicuspid aortic valve** entry; feline *ROBO4* ortholog **NCBI Gene:101084985**. [246][242] | A phenotype record, **not** a demonstrated *ROBO4* genotype. |
| **Mouse, *Mus musculus*; 10090** | *Robo4* ortholog **NCBI Gene:74144**; experimentally engineered disease models. [241][31] | Experimental rather than evidence of a naturally occurring *Robo4* breed disease. |
| **Zebrafish, *Danio rerio*; 7955** | *robo4* ortholog **NCBI Gene:560765**; engineered mutant model. [244][31] | Valve-flow phenotype supports conservation, but vascular anatomy limits comparison with human ascending aneurysm. |

There is **no infectious agent, animal-to-human transmission, or zoonotic potential** for the genetic AOVD3 hypothesis. [31]

## 15. Model organisms and experimental systems

| Model and resource | Manipulation and phenotype recapitulation | Limitation or research application |
|---|---|---|
| **Mouse *Robo4* knockout**, **MGI:1921394**; NCBI Gene **74144** | Homozygous mice developed variably penetrant valve thickening, BAV or other valve abnormalities, stenosis/regurgitation, and ascending-aortic aneurysm. At **20 weeks**, cardiovascular findings occurred in **5/28 males** and **2/18 females**, versus **0/22** and **0/19** respective wild-type animals. **Experimental; PMID:30455415.** [31][241] | Human original families were **heterozygous**; a homozygous mouse knockout is not a direct human penetrance model. |
| **Mouse *Robo4* exon-13 splice knock-in** | Engineered **c.2089+1G>T** produced abnormal exon-13 splicing. At 20 weeks, findings occurred in **1/31 heterozygous males**, **4/35 homozygous males**, and **0/18 wild-type males**. **Experimental; PMID:30455415.** [31] | Closest studied splice-lesion model, but incomplete and genotype-dependent penetrance limits prediction for a human carrier. |
| **Zebrafish *robo4* Δ7 frameshift**; NCBI Gene **560765** | Adult ventriculo-bulbar-valve turbulence/regurgitation was reported in **7/26 heterozygotes** and **4/15 homozygotes**, versus **4/45 wild types**. **Experimental; PMID:30455415.** [31][244] | No overt analogous vascular enlargement; fish anatomy and observation period restrict aneurysm inference. |
| **Cultured human aortic endothelial cells** | *ROBO4* siRNA or expression of familial mutant constructs impaired permeability and junctional markers and promoted mesenchymal-like features. **In vitro; PMID:30455415.** [31] | Tests cellular mechanisms, **not** whole-valve development, lifetime penetrance, or therapeutic efficacy. |
| **Patient tissue and fibroblast cDNA** | Aneurysm tissue showed barrier/remodeling abnormalities; fibroblast cDNA established exon-13 mis-splicing. **Human tissue/in vitro; PMID:30455415.** [31] | Tissue came from a limited number of patients; no validated molecular diagnostic or rescue therapy followed. |

**Knowledge-base conclusion:** Record AOVD3 as an **autosomal-dominant-pattern, incompletely penetrant *ROBO4*-associated disease hypothesis with limited curated gene–disease validity**. The strongest disease-specific causal path is altered ROBO4 → impaired endothelial barrier/mesenchymal-like behavior → abnormal valve development and aortic-wall remodeling, with the middle cellular steps experimentally supported and several links to the full human phenotype still **inferred**. Do not import general BAV incidence, prognosis, intervention response, or 2024 non-valvular ROBO4 pathways as if they were measured specifically in AOVD3. [47][31][46][110][107]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 10 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Gene`, `PMIDs`, `MGI`.

21 of 31 terms resolved to a current term; the rest could not be looked up either way.