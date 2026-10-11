---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-11T20:05:42.095438'
end_time: '2026-10-11T20:09:27.670472'
duration_seconds: 225.58
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Microcephaly, Growth Restriction, and Increased Sister Chromatid Exchange
    2
  mondo_id: MONDO:0020628
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
citation_count: 53
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 36
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - Gene
  - Taxon
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microcephaly, Growth Restriction, and Increased Sister Chromatid Exchange 2
- **MONDO ID:** MONDO:0020628 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Microcephaly, Growth Restriction, and Increased Sister Chromatid Exchange 2** covering all of the
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

# Microcephaly, growth restriction, and increased sister chromatid exchange 2

**MGRISCE2 (MONDO:0020628; OMIM:618097) is a rare, autosomal-recessive, *TOP3A*-related disorder of prenatal and postnatal growth and genome maintenance.** Its defining combination is fetal growth restriction, persistent short stature and microcephaly, and increased sister-chromatid exchanges (SCEs) in tested cells. Some affected children also develop cardiomyopathy or other evidence of mitochondrial dysfunction. It resembles Bloom syndrome but is genetically distinct; the characteristic Bloom-syndrome malar rash was absent from the original *TOP3A* cohort. The foundational report described **10 affected people from seven families**. [41][41][12]

**Scope of evidence.** Frequencies below describe small, clinically ascertained cohorts—not population frequencies. “MGRISCE2” is used here for the childhood Bloom-like *TOP3A* phenotype, **not** for the distinct, often adult-onset *TOP3A*-associated progressive external ophthalmoplegia/mitochondrial phenotype. Unless stated otherwise, findings are aggregated from publications and disease resources; they are not individual electronic health records. [41][50][12]

## 1. Disease information and identifiers

| Identifier or name | Value and interpretation |
|---|---|
| Preferred name | Microcephaly, growth restriction, and increased sister chromatid exchange 2; abbreviation **MGRISCE2**. [12] |
| MONDO | **MONDO:0020628**. [12][14] |
| OMIM phenotype / gene | **618097** / *TOP3A* **601243**, respectively. [41][107] |
| NCBI MedGen | **C4748176**, UID **1648384**. [12] |
| Orphanet | OMIM lists **ORPHA:508512** as a cross-reference. Orphanet calls the entry “intrauterine growth restriction–congenital multiple café-au-lait macules–increased sister chromatid exchange syndrome”; its broader phenotype-based description should **not** be treated as proof that every case has *TOP3A*-defined MGRISCE2. [41][221][256] |
| Alternative clinical name | *TOP3A*-related **Bloom syndrome-like disorder** or **Bloom-like microcephalic dwarfism**; these are descriptive names, not Bloom syndrome caused by *BLM*. [41][59] |
| ICD-10/ICD-11 and MeSH | No verified, disease-specific code or heading was established by the sources reviewed. Code the documented manifestations where required rather than inventing an MGRISCE2-specific code. |

## 2. Etiology, risk, protection, and environment

**Cause.** Disease-associated **biallelic germline *TOP3A* variants** impair topoisomerase IIIα. Its nuclear activity helps the BLM–TOP3A–RMI1–RMI2 (**BTRR**) complex dissolve DNA-recombination intermediates without crossover; its mitochondrial activity helps separate replicated mitochondrial DNA (mtDNA). The original families showed segregation consistent with recessive inheritance. *BLM*, *RMI1*, and *RMI2* cause overlapping disorders or are pathway partners; they are **not additional established causal genes for the specifically *TOP3A*-defined OMIM:618097 entry**. [41][50][41]

**Risk factors.** The established risk is inheriting pathogenic or likely pathogenic *TOP3A* alleles **on both homologous chromosomes**. A family history or parental consanguinity can increase the chance of such an inheritance pattern; neither establishes the diagnosis. The recurrent c.2271dup allele occurred in families from several Middle Eastern countries and later in two unrelated Egyptian children, but these observations do **not** establish a population-specific prevalence, carrier frequency, or proven founder effect. No validated susceptibility locus, modifier gene, protective variant, or sex-specific genetic risk has been demonstrated. [41][128][41]

**Environmental and infectious factors.** No toxin, infection, diet, smoking exposure, maternal age effect, or other environmental factor has been established as a **cause of this Mendelian disorder**; no protective diet, exposure, vaccine, or gene–environment interaction has been validated for it. Environmental causes of *microcephaly or growth restriction in general* must not be imported into this disease entry. Ordinary cardiac, nutritional, and infection care may still affect an individual’s complications. [41][41]

## 3. Phenotypes and their functional impact

The following frequencies use the **original 10 *TOP3A*-affected individuals** as the denominator unless specified. “Reported in *n*/10” is a count of positive reports, **not** an estimated penetrance: several features were not assessed or were marked unavailable. Ages at examination ranged from **5 months to 15 years**. HPO codes are suggested annotation terms; a term’s presence in an ontology is not independent confirmation of frequency. [41]

| Phenotype; type; suggested HPO | Onset, severity, course, and evidence in affected people | Likely day-to-day impact or qualification |
|---|---|---|
| Fetal growth restriction; prenatal clinical sign; **HP:0001511** | **10/10 reported** in the original series. Mean birth-weight Z score **−2.6 ± 0.9**; evident before birth. Later reports include two Egyptian children with strikingly different birth weights, illustrating variability. [41][128] | Signals an early, persistent growth disorder; individual feeding and growth needs require assessment. |
| Decreased body weight and short stature; growth signs; **HP:0004325**, **HP:0004322** | Poor postnatal growth **10/10**; mean weight **−4.8 ± 1.8 SD**, height **−3.9 ± 1.0 SD** in the original series. Chronic rather than episodic. [41] | May affect nutrition, physical stamina, equipment sizing, and psychosocial well-being; disease-specific quality-of-life scores are unavailable. |
| Microcephaly; physical sign; **HP:0000252** | **10/10** in the original series; mean occipital-frontal circumference **−4.0 ± 1.2 SD** at assessment. Generally apparent early, though measurements at birth were incomplete. [41] | Calls for developmental assessment; head size alone does not establish cognitive outcome. |
| Increased spontaneous SCE; **cytogenetic laboratory abnormality**; **HP:0010998** | Present in **all seven original patients tested**; cultured patient cells had approximately **3–6 times** control SCE rates. Not tested in the other three. The later Egyptian report did not provide individual SCE measurements. [41][128][130] | Useful diagnostic evidence of cellular genome instability; generally not itself a symptom. |
| Multiple café-au-lait macules; skin sign; **HP:0000957** | Reported in **8/10** original patients; severity and evolution were not systematically quantified. Both subsequently reported Egyptian children also had multiple macules. [41][128][168] | Visible skin finding; not diagnostic on its own. |
| Dilated cardiomyopathy; cardiac sign; **HP:0001644** | Reported in **three original patients**; one died at age **10 years** with severe disease and another had undergone heart transplantation. A fourth had mild, asymptomatic left-ventricular dilatation, which should not automatically be coded as dilated cardiomyopathy. [41][170] | Can dominate morbidity and survival; warrants individual cardiac assessment. |
| Hypertrophic cardiomyopathy; cardiac sign; **HP:0001639** | Reported in **one original patient**; it should not be merged with dilated cardiomyopathy. [41][134] | Potential cardiac functional risk; longitudinal severity is unknown. |
| Mild developmental or expressive-speech delay; developmental/behavioral sign; **HP:0001263** only when *global* delay is documented | **Four of 10** had mild delay; one was described as having **expressive-speech delay only**, for which a speech-specific HPO term is more accurate than global delay. No uniform progressive intellectual decline was established. [41][170] | May affect communication or learning; standardized functional or quality-of-life scores were not reported. |
| Reduced subcutaneous adipose tissue; physical sign; **HP:0003758** | **3/10** reported; distribution and progression were not established. [41][292] | May contribute to appearance or nutritional concern; metabolic lipodystrophy should not be assumed. |
| Recurrent infections; clinical history; **HP:0002719** | Reported in **three** original patients, with assessment unavailable for others. Examples included otitis/tonsillitis and upper-respiratory infections/oral thrush. A primary human immunodeficiency has **not** been established. [41][171] | Episodic illness and healthcare use where present. |
| Gastroesophageal reflux; symptom; **HP:0002020** | Reported in **two** original patients; others had missing or negative assessments. [41][290] | May aggravate feeding difficulty or discomfort. |
| Muscle mtDNA depletion; laboratory/pathology abnormality; **HP:0009141** | Measured in **one original MGRISCE2 patient**: **87% depletion**. It was not systematically tested across the cohort. [41][131] | Supports mitochondrial involvement; neither universal nor sufficient alone for this diagnosis. |
| Feeding difficulty, atrial septal defect, pectus excavatum; later clinical observations; **HP:0011968** for feeding difficulty | The two Egyptian children had feeding difficulties and pectus excavatum; one had an atrial septal defect. These observations expand the *reported* findings but are too few to establish characteristic frequencies. [128][304] | Feeding needs should be assessed; structural cardiac findings need their own clinical evaluation. |
| Hepatomegaly with hepatic lipid storage; later clinical/pathology observation | Described in **two additional siblings** with a Bloom-like *TOP3A* disorder, not quantified in the original ten. [175] | Possible hepatic involvement; not an established universal feature. |
| **Absence of classic malar rash**; useful differential feature | **0/10** original *TOP3A* patients had the classic Bloom-syndrome malar rash. This is a cohort observation, **not** a guarantee of lifelong absence. A database listing “malar rash” as a positive MGRISCE2 feature conflicts with the primary clinical report. [41][41][139] | Helps distinguish conditions clinically but cannot replace molecular testing. |

**Quality of life:** No MGRISCE2-specific EQ-5D, SF-36, PROMIS, or validated natural-history quality-of-life estimates were identified. The impacts above are clinical interpretations of the reported impairments, not measured scores. [41]

## 4. Genetic and molecular information

*TOP3A* (**HGNC:11992; NCBI Gene:7156; OMIM:601243**) lies at **17p11.2**. The principal disease-associated alleles are germline frameshifts or a missense variant paired with a frameshift. Transcript notation below follows **NM_004618.4** as reported in the original paper; clinical laboratories should normalize against their stated transcript, such as NM_004618.5. **Pathogenicity is variant-specific, and a variant of uncertain significance must not be promoted to pathogenic solely because it occurs in *TOP3A*.** [14][238][41][50]

| Reported disease-associated *TOP3A* variant or genotype | Class, evidence, and interpretation |
|---|---|
| **c.2271dup; p.Arg758GlnfsTer3**, homozygous | Recurrent frameshift in **six original patients from four families**; also homozygous in **two unrelated Egyptian children** reported online in December 2024. ClinVar Variation **560203** records a **germline pathogenic** aggregate classification. A ClinVar submitter reports gnomAD v2.1.1 overall frequency **0.005%** and Finnish-subpopulation frequency **0.02%**; these version-specific figures must not be treated as a current global carrier frequency. A **2024 correction** clarifies that the original paper’s “c.2771dup” for patients P9/P10 was a typo: it is **c.2271dup**. [41][128][225][126] |
| **c.2718del; p.Thr907LeufsTer101**, homozygous | C-terminal frameshift in one original patient. The original protein work found low abundance but retained activity when purified protein was supplied at equal concentration; later reanalysis detected a stable truncated protein, refining a simple “all protein absent” interpretation. [41][270] |
| **c.2428del; p.Ser810LeufsTer2**, homozygous | Frameshift in two original siblings; associated with loss of the C-terminal region. The 2023 study found that a purified C-terminal truncation could retain single-stranded-DNA decatenation in one assay despite impaired cellular mitochondrial rescue: different assays probe different functions. [41][50] |
| **c.[527C>T];[1072_1073dup]; p.[Ala176Val];[Tyr359GlyfsTer17]**, compound heterozygous | One original patient. In 2023 assays p.Ala176Val bound DNA but had strongly impaired decatenation; **2025** biochemical testing of a different complex/assay found near-wild-type behavior and questioned whether this substitution is independently pathogenic. Record the **genotype and conflicting functional evidence**, rather than asserting a settled standalone ACMG classification for p.Ala176Val. [41][50][270] |
| **p.Gln788Ter / p.Asp479Gly**, reported together in two siblings | Additional 2021 Bloom-like family. Patient-cell experiments separated partly preserved nuclear-genome readouts from defective mitochondrial respiration; detailed clinical ACMG classification should be checked against the individual variant records. [175] |

The 2023 study’s **11 people from nine families with predominantly adult-onset mitochondrial disease** are valuable genotype–function comparators, **not 11 additional MGRISCE2 patients**. The authors propose that more severe overall *TOP3A* defects tend toward childhood Bloom-like disease, whereas milder combinations can produce later mitochondrial disease. This is a model, not a validated severity predictor for a newly diagnosed child. [50]

**Other molecular annotations.** No disease-specific modifier allele, recurrent constitutional translocation/aneuploidy, diagnostic DNA-methylation signature, or established transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial, or multi-omics *patient* signature was identified. Mitotic missegregation and micronuclei are **cellular consequences**, not evidence of a defining constitutional karyotype. [41][41]

## 5. Environmental information

MGRISCE2 is **not an infectious disease** and has no demonstrated zoonotic, toxic-exposure, or lifestyle cause. The relevant non-genetic context is management of consequences—adequate nutrition, standard infection prevention and care, and monitoring of cardiac disease—rather than a demonstrated exposure that switches the *TOP3A* phenotype on or off. Specific chemicals should not be assigned a causal CHEBI disease annotation without such evidence. [41][41]

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic *TOP3A* lesions lead to reduced or altered topoisomerase IIIα activity** in the nucleus and, for some genotypes, mitochondria. Protein abundance, C-terminal DNA binding, and catalytic defects differ by allele; complete enzyme absence is **not** established for every patient. **Upstream lesion; demonstrated in patient material and biochemical studies.** [41][50][270]
2. **Nuclear TOP3A dysfunction leads to less effective BTRR-mediated dissolution** of double Holliday junctions and other linked DNA intermediates; alternative processing **results in more crossover products**, observed as elevated SCEs. **Pathway demonstrated biochemically; patient SCE increase demonstrated.** [41][59]
3. **Persistence of DNA links into mitosis leads to chromosome-segregation defects and DNA-damage markers:** patient fibroblasts showed chromatin/ultrafine bridges, lagging chromosomes, micronuclei, and 53BP1 nuclear bodies. **Demonstrated in cells from one intensively studied patient.** [41]
4. **Accumulated genome instability is inferred to reduce developmental cell survival or proliferative capacity, leading to fetal growth restriction and microcephaly.** The cellular abnormalities and clinical phenotype are observed; the precise causal cell-loss sequence in the developing **human brain** has **not** been directly demonstrated. [41]
5. **Mitochondrial branch:** impaired mitochondrial TOP3A **leads to defective decatenation/separation of replicated mtDNA**, which can **result in mtDNA depletion or instability** and reduced mitochondrial energy production; this is a plausible contributor to cardiomyopathy and other organ findings, **not a proven cause of every affected heart phenotype**. Human muscle depletion and patient-cell respiration defects support this branch. [60][41][175]
6. **Additional experimentally induced branch—not established as the MGRISCE2 lesion:** a self-trapping engineered TOP3A variant **leads to trapped TOP3A–DNA cleavage complexes**, fork-associated DNA damage, and repair through SPRTN–TDP2 or ATM–MRE11 pathways. These 2023 cell-model findings clarify TOP3A biology but **must not be annotated as demonstrated in MGRISCE2 patient cells**. [364]

**Cellular and biochemical detail.** BLM drives branch migration; TOP3A, assisted by RMI1/RMI2, performs the final DNA unlinking. SCE is an especially useful readout because normal dissolution favors **non-crossover** products. Mitochondrial TOP3A acts apart from the nuclear BTRR partners. In 2023, *TOP3A* knockdown in a cell-rescue experiment reduced mtDNA copy number by approximately **75%**, reversible with wild-type TOP3A; the authors’ assays showed genotype-dependent differences in DNA binding, relaxation, decatenation, and mtDNA rescue. These are **in-vitro findings**, not a patient treatment response. [41][50]

**Important 2025 refinement:** an engineered C-terminally truncated mouse protein and reexamined human fibroblasts showed that some truncations produce **detectable shortened protein**, rather than necessarily undergoing complete nonsense-mediated decay. The C-terminal domain contributed to DNA binding; homozygous mutant mouse embryos developed profound mtDNA depletion and died early. This strengthens the mitochondrial-developmental hypothesis while demonstrating a significant human–mouse phenotype difference. [270][336]

**Suggested mechanistic annotations:** GO **GO:0000724** (double-strand-break repair via homologous recombination), **GO:0007059** (chromosome segregation), and **GO:0006915** (apoptotic process; supported in the mutant-mouse model, not measured as a human-brain lesion). Candidate CL terms are **CL:0000057** (fibroblast; directly studied), **CL:0000746** (cardiac muscle cell; organ-level clinical involvement), and **CL:0000047** (neuronal stem cell; *inferred* developmental target, not directly proven in patients). These are process/cell-type **suggestions**, not claims that a particular signaling cascade such as Wnt, MAPK, or mTOR has been established. [41][270][146][152][319]

## 7. Anatomical structures affected

| Level | Established observation and suggested annotation |
|---|---|
| Organs and systems | **Whole-body fetal/postnatal growth**, head/central nervous system, **heart**, skin, and—in selected cases—skeletal muscle/mitochondrial function and gastrointestinal tract. Suggested UBERON: **UBERON:0000948** heart, **UBERON:0001134** skeletal muscle tissue. **UBERON:0000956** cerebral cortex is a *possible developmental site*, not a demonstrated site of MGRISCE2-specific pathology. [41][147] |
| Tissues and cells | Patient **dermal fibroblasts** and cultured blood cells provided direct evidence of genome instability; muscle biopsy provided one mtDNA result. Cardiomyocytes (**CL:0000746**), skeletal-muscle cells (**CL:0000188**), and neural stem cells (**CL:0000047**) are plausible tissues/cells for the corresponding manifestations, but were not all examined directly in affected humans. [41][325][152] |
| Subcellular | **Nucleus, GO:0005634** and **mitochondrion, GO:0005739** are the functionally relevant TOP3A locations; chromosomes/mitotic DNA bridges and mitochondrial nucleoids are relevant structures. [50][324] |
| Laterality | The growth and genome-instability findings are systemic; no characteristic unilateral or asymmetric brain lesion is established. The two Egyptian children were described as having asymmetry, without evidence that lateralization defines the disorder. [41][128] |

## 8. Temporal development

Onset is **prenatal and insidious**, followed by chronic poor growth through childhood. There is **no validated stage classification, typical remission, or measured rate of progression**. Microcephaly and short stature persisted across the original 5-month-to-15-year age range, while cardiac disease varied substantially and could become life-threatening in childhood. The fetal period is the most clearly documented period of vulnerability; the benefit of any disease-specific intervention during a proposed “critical window” has not been tested. Do not substitute the decades-later onset pattern of *TOP3A*-associated ophthalmoplegia for MGRISCE2 natural history. [41][50]

## 9. Inheritance, epidemiology, and population

Inheritance is **autosomal recessive**: homozygous and compound-heterozygous affected genotypes were reported, with parents identified as carriers in the original families. If both parents carry a disease-causing allele, the conventional recessive **risk per pregnancy is 25% affected, 50% carrier, and 25% neither familial allele**. Penetrance, variant-specific expressivity, germline-mosaicism rates, anticipation, and a population carrier frequency have **not** been quantified; clinical expressivity is visibly variable, especially cardiac involvement. [41][41]

**Prevalence and incidence per 100,000 are unknown.** Ten affected individuals from seven families were reported in 2018, two further siblings in 2021, and two unrelated Egyptian children in a study published online in December 2024; these are **published ascertainments, not a complete registry or an incidence numerator**. Original patients came from multiple countries and ancestries. The original **7 female:3 male** count is too small and selected to define a sex ratio. Recurrent c.2271dup is not proof of an exclusive ethnic distribution. [41][175][128][41]

## 10. Diagnostics

**Practical diagnostic approach:** document prenatal and postnatal growth parameters and head circumference; examine skin and development; assess cardiac symptoms and obtain **echocardiography** when clinically indicated or when establishing baseline involvement. If the phenotype suggests a chromosome-instability disorder, a laboratory experienced with **SCE cytogenetics** can test cultured blood cells or fibroblasts. Confirm the diagnosis with **two pathogenic/likely pathogenic *TOP3A* variants in trans**, interpreted with segregation, current variant standards, and the phenotype. Seven of seven original patients who had SCE testing showed elevation, but that small series does not establish test sensitivity. [41][41]

**Genetic test selection:** exome sequencing identified variants in the original families; genome sequencing found homozygous c.2271dup in the two Egyptian children after an initial work-up for an imprinting-disorder-like growth phenotype. A microcephaly/growth-failure or genome-instability **panel including *TOP3A* and the differential genes *BLM*, *RMI1*, and *RMI2***, or exome/genome sequencing, is reasonable according to the clinical breadth. Targeted familial-variant testing is appropriate once both familial alleles are known. Chromosomal microarray, karyotyping, and FISH can investigate *other* suspected chromosomal diagnoses but do not substitute for sequencing the typical small *TOP3A* variants; mtDNA analysis may characterize selected muscle/cardiac presentations but does not replace nuclear-*TOP3A* testing. No validated disease-specific RNA-seq, proteomic, metabolomic, epigenomic, or liquid-biopsy diagnostic is established. [41][128][7][41]

**Differential diagnosis:** *BLM*-related Bloom syndrome shares growth failure and high SCE but classically has a photosensitive malar rash; *RMI1*/*RMI2*-related BTRR disorders can overlap; and other primordial-dwarfism, imprinting, or mitochondrial conditions can resemble individual components. **High SCE is not *BLM*-specific.** Conversely, adult-onset *TOP3A* mitochondrial disease can have normal stature and no elevated SCE, so a *TOP3A* result must be interpreted against its allele combination and clinical presentation. No formal MGRISCE2 diagnostic scoring criteria or population newborn screen was identified. [41][50][128]

## 11. Outcomes and prognosis

**Prognosis is individually variable and not quantifiable as a survival rate.** One of the original ten genetically described patients died from severe dilated cardiomyopathy at **age 10**; another affected brother was reported to have died of cardiomyopathy at **age 13**, but was not among the ten fully characterized cases. Another patient had received a heart transplant. The cohort is too small and young to calculate 5-year survival, life expectancy, or disease-attributable mortality rates. [41]

No malignancy had occurred among the original ten at publication, **but they were all aged 15 or younger**. Bloom syndrome raises a biologically relevant concern, not a measured MGRISCE2 cancer penetrance. A cervical cancer in the early 30s was noted in a **2023 *TOP3A* mitochondrial-disease cohort**; it cannot establish a cancer rate for the childhood MGRISCE2 group. Long-term developmental disability rates, validated quality-of-life outcomes, recovery probabilities, and prognostic biomarkers are unavailable. Severe cardiomyopathy is an evident adverse clinical feature, but no validated risk model predicts it from genotype. [41][50]

## 12. Treatment and current clinical application

**There is no established *TOP3A*-restoring drug or proven disease-modifying treatment for MGRISCE2.** Management is coordinated, manifestation-directed care rather than a genotype-guided drug algorithm. The table separates observed interventions from reasonable clinical applications that have **not** been evaluated in MGRISCE2 trials. [41]

| Intervention; suggested NCIT term | Evidence and use |
|---|---|
| Cardiac evaluation and standard cardiomyopathy care; **Echocardiography Test, NCIT:C16525** | Cardiac involvement ranged from asymptomatic ventricular dilatation to fatal cardiomyopathy in the original cohort. The timing and choice of medicines or devices must follow the individual cardiac findings; no MGRISCE2-specific drug-response rate or pharmacogenomic rule exists. [41][360] |
| Heart transplantation; **Heart Transplantation, NCIT:C15246** | **Observed in one** original patient with dilated cardiomyopathy. This is treatment of severe organ disease, **not correction of the genetic defect**; no MGRISCE2 transplant response series is available. [41][360] |
| Growth and nutritional support; NCIT terminology to be selected for the actual nutrition intervention | Individualized feeding assessment is reasonable for marked growth failure or reflux. One child received **growth hormone from age 4 years 3 months to 5 years 11 months without response**; growth hormone is **not** an established MGRISCE2 treatment. [41][128] |
| Developmental, speech, physical, or occupational support; intervention-specific NCIT terms as applicable | Reasonable when delay or functional limitations are documented; the original cohort provides **no controlled efficacy or adverse-event estimates** for these interventions. [41] |
| Genetic counseling; **NCIT:C15240** | Explains biallelic inheritance, variant interpretation, cascade testing, and reproductive options. It is a clinical service, not a molecular cure. [41][350] |

No MGRISCE2-specific approved gene, cell, RNA, targeted, or immune therapy—or disease-specific NCT-numbered interventional result—was established in the reviewed evidence. Research-cell rescue by introducing wild-type TOP3A is **experimental functional evidence**, not a treatment administered to patients. Drug classes, combination regimens, adverse-event rates, and pharmacogenomic recommendations cannot responsibly be specified as disease-specific without clinical studies. [175][50][41]

## 13. Prevention and screening

**Primary prevention of a child’s inherited genotype** is not achieved by vaccination, diet, or toxin avoidance. For a family with established pathogenic variants, **genetic counseling (NCIT:C15240)**, carrier/cascade testing, and discussion of prenatal or preimplantation genetic testing offer reproductive risk assessment and options. These are *options*, not a claim that all families choose or have access to them. [41][350]

**Secondary prevention** means timely recognition of poor fetal/postnatal growth, diagnostic evaluation, developmental assessment, and attention to possible cardiac disease. **Tertiary prevention** is management of cardiomyopathy, feeding/reflux problems, and other individual complications. There is no established population newborn-screening program, MGRISCE2-specific vaccine, chemoprophylaxis, or validated cancer-surveillance schedule; extrapolation from Bloom syndrome should be discussed explicitly as extrapolation. [41][41]

## 14. Other species and naturally occurring disease

The **human** condition occurs in *Homo sapiens* (**NCBI Taxon:9606**). Orthologous *Top3a/top3a* genes have been studied in mouse (*Mus musculus*, **10090**; mouse NCBI Gene **21975**), zebrafish (*Danio rerio*, **7955**), and fruit fly (*Drosophila melanogaster*, **7227**). These are **experimental models**, not verified naturally occurring companion-animal or breed-associated MGRISCE2. No veterinary breed/VBO association or zoonotic transmission applies to the inherited human disorder. [381][247][384]

## 15. Model organisms and research uses

| Model and evidence type | Finding, degree of recapitulation, and limitation |
|---|---|
| Patient-derived fibroblasts and blood cells; **human ex vivo**, PMID **30057030** | Low full-length TOP3A in tested cells, **3–6-fold elevated SCE**, and, in one extensively examined fibroblast line, mitotic bridges/micronuclei. Directly models cellular features but not a developing human brain or full natural history. [41] |
| Patient-cell biochemical and engineered-cell rescue systems; **in vitro**, PMID **37013609** (2023) | Distinguished nuclear and mitochondrial isoforms and tested allele-dependent DNA binding, relaxation, decatenation, and mtDNA rescue. Supports a severity-dependent genotype–phenotype hypothesis; engineered-cell responses are not clinical response rates. [50] |
| *Top3a* knockout mouse; **induced mammalian model**, PMID **9448276** | Early embryonic lethality demonstrates essential developmental function. A complete knockout cannot reproduce the survival of affected humans with residual or altered TOP3A function. [204][387] |
| C-terminal-truncation *Top3a* mouse, created by CRISPR; **induced mammalian model**, PMID **40450688** (2025) | Designed to mimic the consequence of common patient truncations. Homozygotes were small, accumulated DNA damage and apoptosis, had approximately **90% mtDNA depletion by embryonic day 6.5**, and lost viability around day **7.5**. It models the molecular/developmental insult but **not** the postnatal human phenotype. [270][270][225] |
| Zebrafish *top3a* deleterious alleles; **induced vertebrate model**, PMID **20623552** | Revealed impaired developing thymocytes and a **p53-dependent checkpoint**, without an observed V(D)J-recombination defect. Useful for tissue sensitivity; it **does not establish primary immunodeficiency in human MGRISCE2** or reproduce the whole syndrome. [237] |
| Fruit-fly *top3α* mutants and isoform-rescue experiments; **induced invertebrate model**, PMID **20308575** | Null alleles caused delayed development and lethality; mitochondrial-function experiments demonstrated mtDNA maintenance and germ-line consequences. Conserves TOP3A biology but fly reproductive findings should not be assigned as human clinical phenotypes. [193][379] |

**Evidence interpretation and key abstract wording.** The foundational human study states, “**Here, we describe biallelic mutations in TOP3A in ten individuals with prenatal-onset growth restriction and microcephaly**” and reports that the mutations reduce cellular TopIIIα with elevated SCE (**Martin et al., published July 26, 2018; PMID:30057030**; https://pubmed.ncbi.nlm.nih.gov/30057030/). [59] The subsequent human/biochemical study describes “**11 individuals from 9 families with an adult-onset mitochondrial disease**” and proposes that the overall severity of catalytic impairment helps determine the distinct clinical outcomes (**published April 4, 2023; PMID:37013609**; https://pubmed.ncbi.nlm.nih.gov/37013609/). Those 11 are **comparators, not MGRISCE2 prevalence data**. [50][70] The corrected variant notation for original patients P9/P10 was published **May 2, 2024; PMID:38701747** (https://pmc.ncbi.nlm.nih.gov/articles/PMC11080603/). [115][51]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `Gene`, `Taxon`.

30 of 36 terms resolved to a current term; the rest could not be looked up either way.