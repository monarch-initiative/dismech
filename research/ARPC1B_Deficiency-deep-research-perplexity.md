---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-23T22:12:31.221413'
end_time: '2026-08-23T22:16:12.097346'
duration_seconds: 220.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ARPC1B Deficiency
  mondo_id: ''
  category: Immunological
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
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 8
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ARPC1B Deficiency
- **MONDO ID:**  (if available)
- **Category:** Immunological

## Research Objectives

Please provide a comprehensive research report on **ARPC1B Deficiency** covering all of the
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

# Comprehensive Characterization of ARPC1B Deficiency (Immunodeficiency-71 with Inflammatory Disease and Congenital Thrombocytopenia)

ARPC1B deficiency is a recently recognized, ultra‑rare inborn error of immunity caused by biallelic pathogenic variants in the *ARPC1B* gene, encoding actin‑related protein 2/3 complex subunit 1B, a hematopoietic‑restricted regulatory component of the Arp2/3 actin‑branching complex.[3][4][7][9][10][14] Clinically, it manifests as a syndromic combined immunodeficiency with a characteristic constellation of recurrent sinopulmonary and skin infections, severe eczema and atopic disease, autoimmunity and vasculitis, inflammatory bowel disease, platelet abnormalities with bleeding diathesis, eosinophilia, hypergammaglobulinemia (especially IgE and IgA elevation), short stature, and lymphadenopathy, often presenting in infancy or early childhood.[6][7][9][10][16][17] The disease entity was originally catalogued under the descriptive name “platelet abnormalities with eosinophilia and immune‑mediated inflammatory disease” and is now indexed in OMIM as Immunodeficiency‑71 with inflammatory disease and congenital thrombocytopenia (IMD71; OMIM #617718), with *ARPC1B* as the causal gene (OMIM *604223*).[1][7][9][11] Molecular and cellular studies demonstrate that ARPC1B deficiency disrupts Arp2/3‑dependent actin polymerization, leading to defective immune synapse formation, impaired T‑cell and neutrophil migration and proliferation, abnormal platelet morphogenesis and function, dysregulated class‑switched memory B‑cell development, and, more recently, increased radiosensitivity linked to defective DNA double‑strand break clustering and homologous recombination repair.[3][6][15][17][18] Only a few dozen patients have been reported worldwide, but a 2026 cohort from Nepal suggests that case ascertainment is expanding, with about 20 individuals diagnosed in a single center, underscoring both the severity and under‑recognition of this actinopathy‑associated immunodeficiency.[7][19] Therapeutically, hematopoietic stem cell transplantation (HSCT) currently represents the only curative approach, while immunoglobulin replacement, antimicrobial prophylaxis, and immunomodulation—most recently including sirolimus for thrombocytopenia—are used to manage infections and immune‑mediated complications.[5][6][7][8][13][17]  

## 1. Disease Information

### 1.1 Definition and Overview

ARPC1B deficiency is an autosomal recessive primary immunodeficiency and immune‑mediated inflammatory syndrome that arises from loss‑of‑function mutations in *ARPC1B*, a gene encoding a hematopoietic‑restricted regulatory subunit of the Arp2/3 actin‑nucleating complex.[3][4][7][9][10] The disorder is characterized by combined immunodeficiency, recurrent bacterial and viral infections, allergic and atopic manifestations, autoimmune phenomena, vasculitis, colitis, and congenital thrombocytopenia or other platelet abnormalities, often accompanied by eosinophilia and markedly elevated IgE and IgA.[6][7][9][10][14][16][17] OMIM summarizes the clinical entity under the phenotype “Immunodeficiency‑71 with inflammatory disease and congenital thrombocytopenia (IMD71)” and explicitly links it to homozygous or compound heterozygous mutations in *ARPC1B* on chromosome 7q22.1.[1][9] VisualDx and recent clinical series describe ARPC1B deficiency as a “rare condition characterized by combined immune deficiency, recurrent infections, allergies, asthma, and autoinflammation,” emphasizing its syndromic nature within the broader group of actin cytoskeleton‑related inborn errors of immunity.[7][10][14]  

The clinical concept of ARPC1B deficiency originally emerged from descriptions of patients with “platelet abnormalities with eosinophilia and immune‑mediated inflammatory disease (PLTEID),” in whom recurrent infections co‑occurred with severe eczema, vasculitis, colitis, and bleeding due to congenital platelet defects.[7][9][10][14] Subsequent genetic analyses identified biallelic *ARPC1B* variants as the unifying cause, prompting reclassification as an inborn error of immunity and assignment of an IMD number by the International Union of Immunological Societies (IUIS).[9][10][14] A landmark case series in J Allergy and Clinical Immunology in 2019 described “a combined immunodeficiency with severe infections, inflammation, and allergy caused by ARPC1B deficiency,” highlighting impaired T‑cell migration and proliferation, hyper‑IgE and hyper‑IgA, and thrombocytopenia as core biologic features.[16] More recent cohorts from Latin America and South Asia have broadened the phenotype, reporting additional manifestations such as keloid formation, Epstein–Barr virus (EBV) chronic hepatitis, recurrent gastrointestinal bleeding, and radiosensitivity.[7][17][18][19]  

Taken together, ARPC1B deficiency can be defined as an actinopathy‑associated, autosomal recessive, combined immunodeficiency syndrome characterized by immune dysregulation, platelet abnormalities, and a high burden of infection and inflammatory complications. This conceptualization situates the disease within the modern taxonomy of monogenic inborn errors of immunity with cytoskeletal defects, alongside Wiskott–Aldrich syndrome and other Arp2/3‑related disorders.[6][7][14][18]  

### 1.2 Key Identifiers and Classification

Several standardized identifiers and classifications have been assigned to ARPC1B deficiency in genomic, clinical, and ontology databases. At the phenotypic level, OMIM records the entity as “Immunodeficiency‑71 with inflammatory disease and congenital thrombocytopenia,” phenotype MIM number 617718, with autosomal recessive inheritance and mapping key 3, indicating a well‑established gene–phenotype relationship.[9] The causal gene *ARPC1B* itself is catalogued in OMIM under MIM number 604223, with locus 7q22.1.[1][7][9] ClinGen’s Gene Curation resource lists ARPC1B under the disease label “platelet abnormalities with eosinophilia and immune‑mediated inflammatory disease” and associates it with MONDO:0060583, thereby providing a MONDO ID for the disease concept.[11]  

VisualDx identifies “ARPC1B deficiency syndrome” and notes that it is also known as platelet abnormalities with eosinophilia and immune‑mediated inflammatory disease (PTLEID) and Immunodeficiency‑71 with inflammatory disease and congenital thrombocytopenia (IMD71).[10] For clinical coding, VisualDx reports ICD‑10‑CM code D84.9 (“Immunodeficiency, unspecified”) as the closest available designation, reflecting the absence of a more specific ICD code for this newly described entity.[10] SNOMED CT is referenced with the concept “Congenital immunodeficiency disease” (SNOMED CT 36138009), again emphasizing that ARPC1B deficiency is currently subsumed under broader primary immunodeficiency categories in large terminologies.[10]  

From a mechanistic perspective, ARPC1B is registered in HGNC as gene HGNC:704, “actin related protein 2/3 complex subunit 1B,” and ClinGen notes submissions linking this gene to OMIM:617718 under an autosomal recessive (AR) inheritance model.[11] The NCBI Gene entry for *ARPC1B* (Gene ID 10095) provides genomic localization, transcript variants, and links to functional studies, including work showing that inherited ARPC1B deficiency alters T‑cell cytoskeletal dynamics and contributes to combined immunodeficiency phenotypes.[4] Within the IUIS classification of inborn errors of immunity, ARPC1B deficiency is grouped among congenital defects of the actin cytoskeleton, frequently referred to as “actinopathies.”[6][7][14]  

For ontology mapping, suggested identifiers include MONDO:0060583 for the disease entity, HP:0001873 for thrombocytopenia, HP:0002725 for cutaneous vasculitis, HP:0002037 for colitis, HP:0003212 for elevated IgE level, HP:0003150 for elevated IgA level, HP:0001880 for eosinophilia, and HP:0000964 for eczema, among many other HPO terms that capture the rich phenotypic spectrum described in case series.[7][9][10][12][17] At the gene level, GO terms such as GO:0034314 (Arp2/3 complex), GO:0007010 (cytoskeleton organization), and GO:0030036 (actin cytoskeleton organization) are appropriate functional annotations, while CL terms such as CL:0000895 (T cell), CL:0000236 (platelet), and CL:0000788 (neutrophil) denote the major cell types impacted by ARPC1B deficiency.[3][4][6][7][15][17][18]  

### 1.3 Synonyms and Naming History

The naming history of ARPC1B deficiency reflects its evolution from a clinical descriptive syndrome to a molecularly defined inborn error of immunity. Early reports described patients with “platelet abnormalities with eosinophilia and immune‑mediated inflammatory disease,” emphasizing the triad of thrombocytopenia or platelet morphological defects, peripheral eosinophilia, and multi‑system inflammatory manifestations such as eczema, vasculitis, and colitis.[7][9][10][14] OMIM adopted a closely related phrase, “PLTEID” (Platelet abnormalities with eosinophilia and immune‑mediated inflammatory disease), as an initial descriptor of the phenotype before it was integrated into the IMD numbering system.[9][14]  

Following elucidation of the genetic cause, ClinGen and VisualDx began referring to the condition explicitly as “ARPC1B deficiency syndrome,” acknowledging that biallelic mutations in *ARPC1B* underlie the diverse clinical features.[10][11][14] The IUIS classification formalized the name “Immunodeficiency‑71 with inflammatory disease and congenital thrombocytopenia (IMD71)” to describe the immunologic and hematologic core of the disorder.[9][10][14] In clinical practice and recent literature, terms such as “ARPC1B deficiency,” “ARPC1B deficiency syndrome,” and “ARPC1B‑related actinopathy” are now commonly used, often accompanied by explanatory phrases such as “combined immunodeficiency with eczema, allergy, and inflammation” or “platelet abnormalities with eosinophilia and immune‑mediated inflammatory disease.”[6][7][16][17]  

A 2023 series of six patients from multiple families used the phrase “hereditary ARPC1B deficiency” and summarized the condition as “a combined immune defect with short stature, skin infection, allergic and bleeding diatheses, vasculitis, leukocytosis, eosinophilia, platelet abnormalities, hypergammaglobulinemia with elevated B cells, and risk of malignancy,” thereby reinforcing its status as a hereditary syndrome rather than an acquired disorder.[7] Similarly, a case report focusing on gastrointestinal bleeding described it as “mutations in the *ARPC1B* gene cause a syndrome of combined immunodeficiency, allergy, and autoimmunity,” underscoring the immune dysregulation aspects.[17]  

### 1.4 Source and Level of Evidence

The information summarized here is derived predominantly from aggregated disease‑level resources, including OMIM, ClinGen, NCBI Gene, and clinical synopsis tools such as VisualDx, as well as from a limited but growing number of case series and mechanistic studies reported in peer‑reviewed journals.[1][3][4][6][7][9][10][11][13][16][17][18][19] To date, only a few dozen individuals with confirmed ARPC1B deficiency have been described, often in highly detailed case reports or small cohorts, which constitute the primary source of clinical and immunologic characterization.[5][6][7][13][16][17][18][19]  

For example, Kahr and colleagues’ early work, referenced in OMIM and PanelApp summaries, contributed foundational observations about platelet morphology, eosinophilia, and immune dysregulation, while later reports from Afghanistan, Colombia, and Nepal have expanded the genetic and phenotypic spectrum.[5][7][15][19] A 2022 Frontiers in Immunology paper systematically investigated radiosensitivity in a small series of ARPC1B‑deficient patients, combining trio‑based next‑generation sequencing for molecular diagnosis with cytogenetic and cell‑cycle analyses to identify increased G2/M arrest and chromatid‑type aberrations after ionizing radiation and bleomycin exposure.[13][18] The 2019 J Allergy Clin Immunol report and subsequent case series provide detailed immunophenotyping, documenting T‑cell migration defects, B‑cell alterations, hypergammaglobulinemia, and clinical responses to HSCT.[6][7][16][17]  

Because no large registry or prospective natural history study yet exists for ARPC1B deficiency, estimates of incidence, prevalence, and phenotype frequencies are extrapolated from these small aggregated datasets rather than from population‑wide electronic health record analyses. This limitation should be explicitly recognized when interpreting the current evidence base, and many aspects of disease course, long‑term prognosis, and quality of life remain incompletely characterized.[7][9][19]  

## 2. Etiology

### 2.1 Genetic Causal Factors

The primary, and thus far only firmly established, causal factor in ARPC1B deficiency is biallelic germline mutation in the *ARPC1B* gene, which encodes the actin‑related protein 2/3 complex subunit 1B.[1][3][4][7][9][10][11][16][17] OMIM’s gene entry notes that *ARPC1B* maps to chromosome 7q22.1 and encodes one of two isoforms of the first regulatory subunit of the Arp2/3 complex, with ARPC1B being the sole isoform expressed in hematopoietic cells, whereas other tissues express both ARPC1A and ARPC1B.[1][4][7][10] This hematopoietic restriction explains why immunologic and hematologic manifestations predominate in the clinical phenotype, and why other organ systems are relatively spared from direct structural defects.[4][7][10]  

The phenotypic OMIM entry for IMD71 states unequivocally that “a number sign (#) is used with this entry because of evidence that immunodeficiency‑71 with inflammatory disease and congenital thrombocytopenia (IMD71) is caused by homozygous or compound heterozygous mutation in the *ARPC1B* gene (604223) on chromosome 7q22.”[9] Multiple independent families have been reported with distinct loss‑of‑function variants, including frameshift deletions, splice‑affecting synonymous mutations, and other truncating alleles that abolish or severely reduce ARPC1B protein expression.[3][5][6][7][13][15][16][17][18]  

One extensively characterized variant is c.899_944del (p.E300Gfs*7), a 46‑base‑pair deletion in exon 8 that introduces a frameshift, six aberrant amino acids, and a premature stop codon between the fifth and sixth WD40 domains of the ARPC1B protein.[3][7][15] A recent study described this variant as a “founder mutation of indigenous American ancestry that leads to loss of protein expression,” demonstrating by Western blot and flow cytometry that ARPC1B protein is undetectable in patient immune cells.[3][15] In that paper, the authors concluded:  

> “In conclusion, this study characterized the c.899_944del variant in *ARPC1B* as a founder mutation of indigenous American ancestry that leads to loss of protein expression.”[3][15]  

Another notable mutation is a synonymous change, c.783G>A (p.Ala261Ala), reported in three siblings from a consanguineous Afghan family, which affects pre‑mRNA splicing and results in markedly reduced levels of correctly spliced ARPC1B transcript, likely leading to premature termination of the aberrant mRNA.[5] The abstract of that case report states:  

> “In this case series, we report the wide spectrum of phenotype in 3 siblings…with a novel homozygous synonymous pathogenic variant c.783G>A, p.(Ala261Ala) of the *ARPC1B* gene that causes a similar syndrome but no thrombocytopenia. Targeted RNA studies demonstrated that the variant affects the splicing process of mRNA, resulting in a marked reduction of the levels of primary (normal) RNA transcript of the *ARPC1B* gene.”[5]  

Additional variants include c.212_226del, described in the radiosensitivity cohort, and others catalogued by recent clinical series and gene panel studies, all of which are biallelic and produce either complete or near‑complete loss of ARPC1B protein function.[6][7][13][18] The inheritance pattern is consistently autosomal recessive, with affected individuals typically homozygous for the pathogenic variant due to parental consanguinity or compound heterozygous for two different truncating alleles.[5][7][9][10][11][14][18]  

To date, no gain‑of‑function or dominant‑negative *ARPC1B* variants have been associated with disease, and there is no evidence of somatic ARPC1B mutations in hematologic malignancies or solid tumors from the limited literature surveyed. The etiologic model thus centers on germline loss‑of‑function of ARPC1B as the primary causal factor for the immunodeficiency and inflammatory phenotype.[3][4][7][9][10][13][17][18]  

### 2.2 Environmental and Lifestyle Risk Factors

Because ARPC1B deficiency is a monogenic, autosomal recessive inborn error of immunity, environmental and lifestyle factors do not act as primary causes of the disease, but they can modulate disease expression, trigger clinical episodes, and influence severity. The published case series emphasize that clinical manifestations often emerge in infancy or early childhood, frequently in the setting of common infectious exposures, including ear, skin, and lung infections, and invasive bacterial infections such as pneumonia and meningitis.[6][7][9][10][16][17] These infections typically reflect the underlying combined immunodeficiency rather than serving as etiologic risk factors, but high pathogen exposure environments, crowded living conditions, or limited access to healthcare may exacerbate morbidity.  

For example, the 2023 series of six patients described recurrent otitis, sinusitis, bronchitis, pneumonia, and skin infections as prominent features, noting that these infections often occurred early in life and required aggressive antimicrobial management.[7] A case report on gastrointestinal bleeding in ARPC1B deficiency highlighted recurrent infections and inflammation as triggers for disease flares.[17] In the radiosensitivity study, exposure to ionizing radiation and the radiomimetic drug bleomycin was used experimentally to reveal underlying DNA repair defects in patient cells, but there is no evidence that such exposures causally contribute to the development of ARPC1B deficiency; rather, they illustrate an additional vulnerability once the genetic defect is present.[13][18]  

Lifestyle factors such as diet, physical activity, smoking, or alcohol consumption have not been systematically studied in ARPC1B‑deficient cohorts, largely because most reported patients are children or adolescents. There is no current evidence for specific environmental toxins, occupational exposures, or lifestyle factors that increase the risk of developing ARPC1B deficiency in the absence of genetic mutations, although standard recommendations for infection prevention and reduction of environmental triggers of atopic disease are clinically relevant for affected individuals.[7][10][17]  

### 2.3 Genetic and Demographic Risk Factors

Within the genetic framework, several risk factors influence the likelihood of ARPC1B deficiency occurring in a given population. Most reported families demonstrate parental consanguinity, leading to homozygous pathogenic variants in affected children, and the disease therefore appears more frequently in settings where consanguineous marriage is common.[5][7][19] The Afghan siblings with the c.783G>A synonymous variant exemplify this pattern, as do several indigenous American and South Asian families with the c.899_944del frameshift mutation or other truncating variants.[3][5][7][15][19]  

The identification of a founder mutation c.899_944del in an indigenous American population suggests that carrier frequency for this specific allele may be elevated in certain geographic or ethnic groups, although precise estimates from gnomAD or population genetics databases have not yet been published.[3][7][15] The 2023 series reported that a novel deletion in exon 8 is shared by three unrelated families and “might be the result of a founder effect,” consistent with this notion.[7] The 2026 abstract from Nepal further indicates that a single center has diagnosed 20 cases, including 14 previously reported, implying that founder effects and local clustering may contribute to disease burden in specific regions.[19]  

Demographically, ARPC1B deficiency affects both males and females, consistent with autosomal inheritance, and reported patients include infants, children, and adolescents, with occasional young adults.[6][7][9][16][17][19] There is no clear sex predilection, and penetrance appears high among individuals with biallelic loss‑of‑function variants, although expressivity is markedly variable, ranging from severe congenital thrombocytopenia and early‑onset life‑threatening infections to milder vasculitis with relatively preserved platelet counts.[7][9][10][14][15][16][17][19]  

### 2.4 Protective Factors and Gene–Environment Interactions

Specific genetic protective factors, such as hypomorphic alleles that mitigate disease severity or polymorphisms in modifier genes, have not yet been formally identified in ARPC1B deficiency, though the heterogeneity of clinical phenotypes suggests that such modifiers may exist. Some individuals with ARPC1B loss‑of‑function variants exhibit relatively mild thrombocytopenia or even normal platelet counts, and one family with the c.783G>A synonymous mutation showed combined immunodeficiency and allergy without thrombocytopenia, pointing to variant‑specific and potentially modifier‑dependent differences in phenotypic expression.[5][7][9][10][14][15]  

The presence of ARPC1A, a paralogous isoform expressed in non‑hematopoietic tissues, likely functions as a partial protective factor at the systemic level, preventing widespread non‑immune organ dysfunction in ARPC1B‑deficient individuals.[4][7][10] In tissues where both ARPC1A and ARPC1B are expressed, functional redundancy may reduce the impact of ARPC1B loss, whereas in hematopoietic cells, where ARPC1B is the only isoform, no such redundancy exists.[4][7][10] This gene‑context interaction illustrates a form of genetic protection that is intrinsic to the tissue expression pattern of ARPC1 isoforms.  

Regarding gene–environment interactions, the radiosensitivity study suggests that ARPC1B deficiency interacts with environmental exposure to ionizing radiation and radiomimetic chemotherapeutic agents in a way that increases cellular damage and G2/M‑phase arrest compared to healthy controls.[13][18] The authors reported higher levels of chromatid‑type aberrations and γH2AX foci in patient cells after irradiation and bleomycin treatment, concluding that “our data suggest increased radiosensitivity as an additional trait in ARPC1B deficiency and support the necessity to investigate this feature in ARPC1B patients as well as in other IEI with cytoskeleton defects to address specific clinical follow‑up and optimize therapeutic interventions.”[18] This implies that ARPC1B‑deficient individuals may be at greater risk of adverse effects from radiotherapy or certain chemotherapies, and that environmental exposures to DNA‑damaging agents may have more pronounced consequences in this genetic background.  

Beyond these examples, gene–environment interaction research in ARPC1B deficiency remains limited, and no formal GxE studies have been performed. However, one can infer that typical environmental triggers of infection and inflammation may precipitate more severe clinical episodes in ARPC1B‑deficient individuals due to their impaired immune cell migration, altered immune synapse formation, and dysregulated cytokine responses, forming a causal chain in which environmental pathogens act downstream of a primary genetic vulnerability.[6][7][16][17][18]  

## 3. Phenotypes

### 3.1 Overall Phenotypic Spectrum and Age of Onset

ARPC1B deficiency presents with a broad and heterogeneous phenotypic spectrum, encompassing infectious susceptibility, allergic and atopic disease, autoimmunity, vasculitis, gastrointestinal inflammation and bleeding, platelet abnormalities, growth impairment, lymphadenopathy, and, more recently, radiosensitivity.[6][7][9][10][13][16][17][18][19] The age of onset is typically infancy or very early childhood, with many patients manifesting symptoms within the first months or years of life, aligning with the categorization of ARPC1B deficiency as a congenital combined immunodeficiency.[6][7][9][16][17]  

The phenotypic OMIM entry for IMD71 notes that the disorder is “characterized by the onset of recurrent infections and inflammatory features such as vasculitis and eczema in infancy or early childhood,” emphasizing early presentations with skin and systemic inflammation.[9] The 2023 patient series similarly highlights that actinopathies like ARPC1B deficiency “manifest early in life (usually the first two months) as combined or syndromic defects, with atopic and hemorrhagic diatheses, susceptibility to viral and bacterial infections, an increased risk of hematologic malignancy, and inflammatory manifestations.”[7] In the Afghan sibling case with the c.783G>A variant, clinical symptoms included infections, asthma, and allergy beginning in childhood, demonstrating that onset may span from early infancy to school age but is rarely adult‑onset.[5][16][17]  

Severity varies substantially among patients. Some individuals experience life‑threatening infections, severe thrombocytopenia with bleeding, refractory colitis, and multi‑organ vasculitis requiring HSCT at a young age, whereas others have milder immune dysregulation with manageable infections and relatively preserved platelet counts.[5][6][7][9][10][14][16][17][19] Disease progression can be episodic, with flares of vasculitis or colitis, or more chronically active, with ongoing eczema, atopic disease, and recurrent infections leading to progressive organ damage such as bronchiectasis or chronic hepatitis.[7][9][17][19]  

The quality of life impact is profound in severely affected patients, who may require frequent hospitalizations, long‑term immunosuppressive and antimicrobial therapies, and ultimately HSCT, whereas individuals with milder variants may function relatively well with supportive care but still face chronic eczema, asthma, and bleeding risks that interfere with daily activities.[5][6][7][16][17][19]  

### 3.2 Infectious Phenotypes

Recurrent infections involving the ears, sinuses, skin, and lungs are among the most consistent features of ARPC1B deficiency and form a major component of the combined immunodeficiency phenotype.[6][7][9][10][16][17][19] The 2023 series summarized that “hereditary ARPC1B deficiency is characterized clinically by ear, skin, and lung infections, bleeding, eczema, food allergy, asthma, skin vasculitis, colitis, arthritis, short stature, and lymphadenopathy,” highlighting frequent otitis, sinusitis, cellulitis, and pneumonia as core manifestations.[7] VisualDx similarly notes that the syndrome is “characterized by combined immune deficiency, recurrent infections, allergies, asthma, and autoinflammation.”[10]  

Bacterial pathogens reported include common respiratory organisms such as *Streptococcus pneumoniae* and *Haemophilus influenzae*, as well as skin flora causing abscesses and cellulitis; viral pathogens such as EBV have also been implicated, with one patient developing chronic EBV hepatitis.[7][17][19] The susceptibility profile resembles that of other combined immunodeficiencies, with increased risk for both bacterial and viral infections, likely due to impaired T‑cell migration and proliferation, altered neutrophil chemotaxis, and dysfunctional immune synapse formation.[6][7][16][17] OMIM notes that infectious agents in IMD71 include both bacteria and viruses, and that laboratory findings often show leukocytosis, reflecting chronic inflammatory stimulation by repeated infections.[9]  

Suggested HPO terms for these infectious phenotypes include HP:0002719 (Recurrent bacterial infections), HP:0002718 (Recurrent viral infections), HP:0000388 (Otitis media), HP:0002097 (Recurrent pneumonia), and HP:0002716 (Lymphadenopathy), all of which capture the recurrent and systemic nature of infection‑related manifestations.[7][9][12][17] Downstream impacts on quality of life include frequent school absences, impaired physical activity due to chronic respiratory symptoms, and psychosocial burdens related to long‑term antibiotic use and hospitalizations.[6][7][17][19]  

### 3.3 Allergic and Atopic Phenotypes

Marked allergic and atopic disease is a defining characteristic of ARPC1B deficiency. Patients commonly exhibit severe eczema, food allergies, asthma, and elevated serum immunoglobulin E (IgE) and immunoglobulin A (IgA), often in the context of eosinophilia.[6][7][9][10][14][16][17] The J Allergy Clin Immunol report and PanelApp summaries emphasize that homozygous mutations in *ARPC1B* “cause an autosomal recessive syndrome of combined immune deficiency, impaired T‑cell migration and proliferation, increased levels of immunoglobulin E (IgE) and immunoglobulin A (IgA), and thrombocytopenia.”[5][14][16] The 2023 series reiterates that “hypergammaglobulinemia (high IgE/IgA/IgG) and serum autoantibodies (ANA, ANCA)” are typical laboratory findings, associated with clinical eczema, food allergy, and asthma.[7]  

Cutaneous manifestations include severe, often treatment‑refractory eczema, sometimes accompanied by keloid scarring, as well as cutaneous vasculitis with purpuric or ulcerative lesions.[6][7][9][10][17][19] Respiratory atopy includes asthma with bronchial hyperreactivity and allergic rhinitis. Food allergies may present with gastrointestinal symptoms and occasionally contribute to GI bleeding in the context of colitis.[7][17] Suggested HPO terms include HP:0000964 (Eczema), HP:0001025 (Asthma), HP:0002715 (Food allergy), HP:0001880 (Eosinophilia), HP:0003212 (Elevated IgE level), and HP:0003150 (Elevated IgA level).[7][9][12][14][16][17]  

These allergic and atopic phenotypes significantly impair quality of life, leading to chronic pruritus, sleep disturbance, dietary restrictions, and anxiety about anaphylaxis or severe asthma exacerbations. Importantly, the coexistence of allergic disease and immunodeficiency in ARPC1B deficiency complicates management, as standard immunosuppressive therapies for eczema and asthma must be balanced against heightened infection risks.[6][7][10][16][17]  

### 3.4 Autoimmunity, Vasculitis, and Inflammation

Immune dysregulation in ARPC1B deficiency extends beyond atopy to include autoimmunity, vasculitis, and chronic inflammatory states affecting the skin, gastrointestinal tract, and joints.[6][7][9][10][14][16][17][18][19] OMIM describes IMD71 as characterized by “inflammatory features such as vasculitis and eczema,” and notes that laboratory studies often reveal autoantibodies including antinuclear antibodies (ANA) and anti‑neutrophil cytoplasmic antibodies (ANCA).[9] PanelApp further indicates that IUIS‑associated features include recurrent invasive infections, colitis, vasculitis, autoantibodies (ANA, ANCA), eosinophilia, and defective Arp2/3 filament branching.[14]  

Clinically, patients may develop cutaneous leukocytoclastic vasculitis with palpable purpura, ulcerations, and skin necrosis; systemic vasculitis affecting small or medium vessels; inflammatory arthritis; and chronic colitis or enterocolitis with abdominal pain, diarrhea, and sometimes hematochezia.[6][7][17][19] A case report focusing on recurrent hematemesis described immune‑mediated inflammatory disease with associated platelet defects, rashes, and bowel disease, emphasizing gastrointestinal autoimmunity and vasculitis as major disease components.[17] Inflammatory bowel disease can be severe and refractory to conventional therapies, occasionally necessitating HSCT for control.[7][17][19]  

Suggested HPO terms include HP:0002725 (Cutaneous vasculitis), HP:0002037 (Colitis), HP:0001824 (Arthritis), HP:0002090 (Gastrointestinal hemorrhage), and HP:0004319 (Abnormality of the skin). These manifestations substantially reduce quality of life through chronic pain, fatigue, functional limitation, and the need for long‑term corticosteroids or immunosuppressants, which further exacerbate infection risk.[6][7][17][19]  

### 3.5 Hematologic and Platelet Phenotypes

Platelet abnormalities are central to ARPC1B deficiency and were among the first features recognized in early descriptions of PLTEID. OMIM notes that laboratory findings in IMD71 “usually show thrombocytopenia, sometimes with abnormal platelet morphology,” and that platelets may have abnormal shape, decreased dense granules, and impaired spreading ability.[9] The 2023 series reports that ARPC1B deficiency is associated with “thrombocytopenia/thrombocytosis, small or large platelets,” and emphasizes bleeding diathesis as a prominent clinical issue.[7]  

Mechanistic studies indicate that loss of ARPC1B disrupts Arp2/3‑dependent actin branching in megakaryocytes and platelets, leading to defective proplatelet formation, impaired platelet spreading on fibrinogen, and reduced dense granule content, all of which contribute to bleeding tendency.[6][9][14][18] A 2022 Frontiers in Immunology paper summarized that “loss of the Arp2/3 complex component ARPC1B causes platelet abnormalities and predisposes to inflammatory disease,” encapsulating the dual hematologic and immunologic impact.[6][9][18]  

Notably, not all patients exhibit severe thrombocytopenia; some have mild thrombocytopenia or even normal platelet counts but abnormal platelet size or function, and one family with the c.783G>A synonymous mutation had no thrombocytopenia despite combined immunodeficiency and allergy, illustrating phenotypic variability and highlighting that platelet abnormalities, while typical, are not absolutely universal.[5][7][9][10][14][15] Suggested HPO terms include HP:0001873 (Thrombocytopenia), HP:0001907 (Abnormal platelet morphology), HP:0001928 (Abnormal platelet size), HP:0004423 (Abnormal platelet spreading), and HP:0001892 (Bleeding diathesis). These hematologic manifestations increase risk of epistaxis, mucosal bleeding, GI hemorrhage, and perioperative complications, further impairing quality of life and necessitating careful transfusion and procedural planning.[6][7][9][17][18]  

### 3.6 Immunologic Laboratory Phenotypes

Beyond clinical manifestations, ARPC1B deficiency is characterized by distinctive immunologic laboratory profiles. OMIM and PanelApp summarize that laboratory findings usually include leukocytosis, eosinophilia, hypergammaglobulinemia (elevated IgE, IgA, and sometimes IgG), serum autoantibodies (ANA, ANCA), low CD3+ T cells, increased B cells, and variable changes in T‑cell subsets.[7][9][14][16][17]  

Flow cytometric analysis of patient immune cells consistently shows severely reduced or undetectable ARPC1B protein levels compared to controls, confirming loss‑of‑function at the protein level.[1][3][6] One OMIM entry notes that “flow cytometric analysis of patient immune cells showed severely reduced ARPC1B levels compared to controls, consistent with a loss of function,” highlighting the utility of ARPC1B expression assays as a diagnostic biomarker.[1][3] A recent mechanistic study suggested that ARPC1B is critical for immunoglobulin class switching, as ARPC1B‑deficient patients had reduced frequencies of class‑switched memory B cells, consistent with impaired germinal center dynamics.[15]  

Suggested HPO terms for these laboratory abnormalities include HP:0002723 (Leukocytosis), HP:0001880 (Eosinophilia), HP:0003212 (Elevated IgE level), HP:0003150 (Elevated IgA level), HP:0002863 (Autoantibodies), HP:0002722 (Abnormal T‑cell morphology or number), and HP:0002833 (Abnormal B‑cell count). These immunologic phenotypes, while primarily laboratory features, have direct clinical correlates in susceptibility to infections, atopic disease, and autoimmunity.[6][7][9][14][16][17]  

### 3.7 Radiosensitivity Phenotype

Increased radiosensitivity has recently been recognized as an additional trait of ARPC1B deficiency. The 2022 Frontiers in Immunology study systematically evaluated chromatid‑type aberrations and γH2AX foci in ARPC1B‑deficient cells exposed to ionizing radiation and bleomycin, identifying higher levels of DNA damage markers and an increased number of cells arrested in the G2/M phase compared to healthy donors.[13][18] The authors concluded:  

> “Overall, our data suggest increased radiosensitivity as an additional trait in ARPC1B deficiency and support the necessity to investigate this feature in ARPC1B patients as well as in other IEI with cytoskeleton defects to address specific clinical follow‑up and optimize therapeutic interventions.”[18]  

Mechanistically, they proposed that defective Arp2/3‑ARPC1B complex function impairs DNA double‑strand break clustering required for homology‑directed repair during G2, and that ARPC1B also localizes to centrosomes and interacts with Aurora‑A kinase, influencing cell‑cycle progression and preventing mitotic entry, thereby linking actin cytoskeleton dynamics to DNA repair pathways.[18] Suggested HPO terms include HP:0005425 (Increased sensitivity to radiation) and HP:0002709 (Abnormal DNA repair), capturing the cellular phenotype. Clinically, this trait necessitates caution when considering radiotherapy or radiomimetic chemotherapies for ARPC1B‑deficient patients and may influence long‑term cancer risk, although epidemiologic data on malignancy incidence remain limited.[7][18][19]  

### 3.8 Growth and Development Phenotypes

Short stature and growth impairment have been reported in multiple ARPC1B‑deficient patients, suggesting that chronic inflammation, recurrent infections, and possibly intrinsic effects on hematopoietic and stromal cell function may impact growth.[7][9][19] The 2023 series explicitly noted short stature as part of the clinical spectrum, and OMIM includes growth impairment among variable features.[7][9] Suggested HPO terms include HP:0004322 (Short stature) and HP:0001510 (Growth delay).  

Neurodevelopmental outcomes have not been systematically studied, but most reports do not describe major neurocognitive deficits, implying that ARPC1B deficiency predominantly affects immune and hematologic systems rather than brain development, although chronic disease and repeated hospitalizations may secondarily impair educational attainment and psychosocial functioning.[7][17][19]  

### 3.9 Phenotypic Table and Ontology Mapping

The following table summarizes key phenotypes, their type, suggested HPO terms, and qualitative frequency based on reported cohorts. Frequencies are approximate and should be interpreted cautiously given the small number of patients studied.

| Phenotype                              | Phenotype Type           | Suggested HPO Term          | Approximate Frequency among reported patients |
|----------------------------------------|--------------------------|-----------------------------|-----------------------------------------------|
| Recurrent ear, skin, and lung infections | Symptom/clinical sign   | HP:0002719, HP:0002097      | Very common (majority)                        |
| Severe eczema                          | Symptom/clinical sign    | HP:0000964                  | Very common                                   |
| Asthma and allergic rhinitis           | Symptom/clinical sign    | HP:0001025                  | Common                                        |
| Food allergy                           | Symptom/clinical sign    | HP:0002715                  | Common                                        |
| Cutaneous vasculitis                   | Clinical sign            | HP:0002725                  | Common                                        |
| Colitis/enterocolitis                  | Clinical sign            | HP:0002037                  | Common                                        |
| Arthritis                              | Clinical sign            | HP:0001824                  | Reported in subset                            |
| Thrombocytopenia                       | Laboratory abnormality   | HP:0001873                  | Very common, but variable severity            |
| Abnormal platelet morphology           | Laboratory abnormality   | HP:0001907                  | Common                                        |
| Eosinophilia                           | Laboratory abnormality   | HP:0001880                  | Very common                                   |
| Elevated IgE and IgA                   | Laboratory abnormality   | HP:0003212, HP:0003150      | Very common                                   |
| Autoantibodies (ANA, ANCA)            | Laboratory abnormality   | HP:0002863                  | Common                                        |
| Leukocytosis                           | Laboratory abnormality   | HP:0002723                  | Common                                        |
| Short stature                          | Physical manifestation   | HP:0004322                  | Common                                        |
| Lymphadenopathy                        | Clinical sign            | HP:0002716                  | Common                                        |
| Radiosensitivity                       | Laboratory/cellular      | HP:0005425                  | Documented in small cohort                    |

These phenotypes, collectively, create a complex disease burden that substantially impacts daily functioning, educational participation, and psychosocial well‑being for affected individuals and their families.[6][7][9][10][17][19]  

## 4. Genetic and Molecular Information

### 4.1 The ARPC1B Gene and Protein

The *ARPC1B* gene encodes actin‑related protein 2/3 complex subunit 1B, one of two isoforms of the first regulatory subunit of the Arp2/3 complex.[1][4][7][10] NCBI Gene locates *ARPC1B* on chromosome 7 (NC_000007.14), with multiple transcript variants identified, and notes that inherited ARPC1B deficiency alters T‑cell cytoskeletal dynamics and functions, contributing to combined immunodeficiency.[4] OMIM gene entry #604223 summarizes that ARPC1B is “primarily expressed in hematopoietic cells, where it promotes the branching out (initiation and remodeling) of new actin filaments from the mother thread.”[1][7]  

Structurally, ARPC1B contains six WD40 domains that form a β‑propeller, a common protein architecture for scaffold and regulatory functions.[3] The c.899_944del frameshift mutation locates between the fifth and sixth WD40 domains, and is predicted to cause a shift in the reading frame, introducing a six‑amino‑acid aberrant sequence followed by a premature stop codon and complete loss of the last WD40 domain.[3][15] WD40 repeats are crucial for protein–protein interactions, and their disruption likely impairs the ability of ARPC1B to stabilize and regulate the Arp2/3 complex, thereby compromising actin branching.[3][4][7][15]  

At the protein complex level, ARPC1B is part of the seven‑subunit Arp2/3 complex, which includes two actin‑related proteins (Arp2 and Arp3) and five regulatory subunits (ARPC1–5).[3][4][6][7][18] The complex binds to the side of existing actin filaments and nucleates the formation of new branches, generating a dendritic actin network that drives membrane protrusions such as lamellipodia and filopodia in migrating cells.[3][4][6][7][18] In hematopoietic cells, ARPC1B is uniquely required for this process, as ARPC1A is not expressed, making ARPC1B loss particularly detrimental to immune cell motility and platelet biogenesis.[4][7][10]  

Suggested HGNC ID for ARPC1B is HGNC:704, and relevant GO molecular function and biological process terms include GO:0003779 (actin binding), GO:0034314 (Arp2/3 complex), GO:0007010 (cytoskeleton organization), GO:0030036 (actin cytoskeleton organization), and GO:0060326 (cell chemotaxis), reflecting the protein’s role in actin regulation and cell migration.[3][4][6][7][15][18]  

### 4.2 Pathogenic Variant Landscape

Pathogenic variants in *ARPC1B* reported to date are predominantly truncating, loss‑of‑function alleles, including frameshift deletions, nonsense mutations, and splice‑affecting substitutions, consistent with a disease mechanism of complete or near‑complete absence of functional protein.[3][5][6][7][13][15][16][17][18] The c.899_944del (p.E300Gfs*7) variant described in indigenous American families is a 46‑bp deletion in exon 8, causing frameshift and premature termination; immunoblot and flow cytometry analyses demonstrate complete absence of ARPC1B protein in patient cells.[3][15] This variant segregates as an autosomal recessive trait and has been found in multiple unrelated families, suggesting a founder effect.[3][7][15]  

The c.783G>A (p.Ala261Ala) synonymous variant in Afghan siblings affects mRNA splicing, reducing levels of correctly spliced transcript and likely resulting in truncated protein from aberrant splice products.[5] Targeted RNA sequencing confirmed these splicing defects, and the clinical phenotype mirrored that of other ARPC1B‑deficient patients, except for the absence of thrombocytopenia, underscoring variant‑specific phenotypic divergence.[5]  

The radiosensitivity cohort identified a homozygous deletion c.212_226del in one patient, also producing a frameshift and loss of protein function, with combined immunodeficiency, recurrent infections, thrombocytopenia, immune dysregulation, and increased radiosensitivity.[13][18] Other variants catalogued in case series include similar truncating mutations across different exons, all classified as pathogenic or likely pathogenic according to ACMG/AMP guidelines, based on their predicted loss‑of‑function nature, segregation in affected families, and functional evidence of absent protein.[3][6][7][13][15][16][17][18][19]  

Somatic ARPC1B mutations have not been described in association with hematologic malignancies in current literature, and cancer genome resources have not yet highlighted ARPC1B as a recurrently mutated oncogene or tumor suppressor. All reported variants are germline, inherited from carrier parents often in consanguineous unions.[5][7][9][11][14] Population allele frequencies for specific pathogenic variants such as c.899_944del are not yet well defined in gnomAD or ExAC, but their extreme rarity and absence in large control cohorts are consistent with severe Mendelian disease.[3][7][15][19]  

### 4.3 Founder Effects, Modifier Genes, and Population Genetics

Founder mutations appear to play a role in ARPC1B deficiency epidemiology. The c.899_944del variant was shown to originate from a founder effect in indigenous American populations, with shared haplotypes across different families supporting common ancestry.[3][7][15] The 2023 series noted that “a novel deletion in exon 8 is shared by three unrelated families and might be the result of a founder effect,” further corroborating this.[7] Similarly, the cluster of cases in Nepal suggests that one or more local founder variants contribute to a relatively high case load in that region, though the specific alleles have not yet been fully published.[19]  

Modifier genes that influence disease severity and expression have not been systematically identified, but the marked variability in thrombocytopenia, vasculitis, and infection severity among patients with similar *ARPC1B* mutations implies the existence of genetic modifiers or environmental influences. For example, variation in genes regulating cytokine production, immune synapse stability, or DNA repair may modify susceptibility to specific complications such as colitis or radiosensitivity.[6][7][18][19] However, until genome‑wide association or exome‑wide modifier analyses are performed in larger cohorts, such modifiers remain hypothetical.  

### 4.4 Epigenetic Information and Chromosomal Abnormalities

Direct epigenetic studies focusing on DNA methylation, histone modifications, or chromatin accessibility in ARPC1B‑deficient patients have not yet been reported. Nonetheless, the Arp2/3 complex, including ARPC1B, has been implicated in nuclear actin dynamics and chromatin remodeling in experimental systems, suggesting that ARPC1B loss may indirectly affect epigenetic regulation by altering nuclear actin structures.[18] The radiosensitivity study notes that ARPC1B localizes to centrosomes and interacts with Aurora‑A kinase, influencing cell‑cycle progression and DNA end‑resection in homologous recombination, processes intimately linked to chromatin status and DNA repair, though not strictly epigenetic in the classical sense.[18]  

No recurrent large‑scale chromosomal abnormalities, such as aneuploidy, translocations, or inversions, have been associated with ARPC1B deficiency itself; the disease is caused by point mutations and small indels within the *ARPC1B* locus.[3][5][7][13][15][16][17][18] However, standard cytogenetic analyses used in radiosensitivity testing revealed increased chromatid‑type aberrations after irradiation, reflecting functional defects in DNA repair rather than constitutional chromosomal abnormalities.[13][18]  

## 5. Environmental Information

### 5.1 Environmental Exposures and Triggers

As a monogenic inborn error of immunity, ARPC1B deficiency is not caused by environmental factors, but certain exposures serve as triggers that reveal or exacerbate the underlying defect. Common viral and bacterial pathogens precipitate recurrent infections due to impaired immune cell migration and synapse formation, and inflammatory triggers such as allergens, dietary antigens, and microbiota‑derived signals may aggravate eczema, asthma, and colitis in the context of immune dysregulation.[6][7][10][16][17]  

Ionizing radiation and radiomimetic chemotherapeutic agents like bleomycin are notable environmental stressors that interact with ARPC1B deficiency. The radiosensitivity study demonstrated that ARPC1B‑deficient cells show increased DNA damage markers and cell‑cycle arrest after exposure to these agents, suggesting that environmental or iatrogenic DNA‑damaging exposures have amplified effects in this genetic background.[13][18] Clinically, this raises concerns about radiotherapy and certain chemotherapies in ARPC1B‑deficient patients, prompting recommendations for minimizing such exposures where possible.[18]  

No specific environmental toxins, pollutants, or occupational exposures have been linked to the incidence of ARPC1B deficiency, and standard environmental risk factor databases do not catalog ARPC1B as a gene responsive to particular xenobiotics in ways that would cause disease in the absence of genetic mutation. Nonetheless, reducing infection risk through vaccination, hygiene, and public health measures remains crucial for managing disease burden in affected individuals.[7][10][17]  

### 5.2 Lifestyle Factors and Infectious Agents

Lifestyle factors such as smoking, diet, and exercise have not been systematically studied in ARPC1B‑deficient cohorts, but general principles of infection prevention and inflammatory disease management apply. Balanced nutrition supporting immune function, avoidance of smoking and indoor air pollution, and adherence to recommended vaccination schedules are likely beneficial for reducing infection burden and inflammatory flares, although these are not disease‑specific protective factors in the etiologic sense.[7][10][17]  

Infectious agents relevant to ARPC1B deficiency include common respiratory and skin pathogens, as well as EBV and possibly other herpesviruses. One patient in the 2023 series developed EBV chronic hepatitis, and other cohorts report viral respiratory infections and bacterial pneumonias as frequent events.[7][17][19] These pathogens do not cause ARPC1B deficiency but exploit the impaired immune system, leading to recurrent or severe infections that drive morbidity and can precipitate vasculitis or colitis flares through bystander inflammatory mechanisms.[6][7][16][17]  

## 6. Mechanism and Pathophysiology

### 6.1 Molecular Pathways: Arp2/3 Complex and Actin Cytoskeleton

The central pathogenic mechanism in ARPC1B deficiency involves disruption of the Arp2/3 complex and actin cytoskeleton dynamics in hematopoietic cells. ARPC1B is a regulatory subunit of the Arp2/3 complex, which nucleates branched actin filament networks essential for cell migration, immune synapse formation, phagocytosis, and platelet biogenesis.[3][4][6][7][18] In immune cells, Arp2/3‑dependent actin branching underpins the formation of lamellipodia and filopodia required for chemotaxis and for the assembly of immunologic synapses between T cells and antigen‑presenting cells.[3][4][6][7][16][18]  

When ARPC1B is absent or nonfunctional due to loss‑of‑function mutations, the Arp2/3 complex fails to properly initiate and remodel actin branches, leading to aberrant cytoskeletal architecture, impaired membrane protrusions, and defective cell migration.[3][4][6][7][16][18] Functional studies in ARPC1B‑deficient T cells demonstrate impaired chemotaxis toward chemokines, reduced formation of stable immune synapses, and diminished proliferative responses to antigenic stimulation, collectively contributing to combined immunodeficiency.[4][6][16] Neutrophils likewise show defective migration and chemotaxis, compromising innate immune responses to bacterial and fungal pathogens.[6][7][16][17]  

From a pathway perspective, key GO biological process terms include GO:0007010 (cytoskeleton organization), GO:0030036 (actin cytoskeleton organization), GO:0060326 (cell chemotaxis), GO:0007163 (establishment or maintenance of cell polarity), and GO:0006955 (immune response), all of which are disrupted in ARPC1B‑deficient cells.[3][4][6][7][16][18] Upstream triggers include chemokine receptor activation and T‑cell receptor engagement, which in healthy cells lead to Arp2/3 recruitment and actin polymerization; downstream consequences in ARPC1B deficiency are reduced immune cell migration, impaired antigen recognition, and defective effector functions such as cytotoxicity and cytokine production.[4][6][16][18]  

### 6.2 Cellular Processes: Immune Synapse, Migration, and Class Switching

At the cellular level, ARPC1B deficiency disrupts multiple processes critical for immune function. T‑cell and neutrophil migration is compromised, as demonstrated by defective chemotaxis assays and impaired formation of lamellipodia in ARPC1B‑deficient cells.[4][6][16][18] The immunologic synapse between T cells and antigen‑presenting cells relies on actin reorganization to stabilize contact and organize signaling molecules; ARPC1B loss leads to unstable synapses and reduced T‑cell activation and proliferation, contributing to combined immunodeficiency.[4][6][16]  

In B cells, recent evidence suggests that ARPC1B is critical for immunoglobulin class switching. A mechanistic study concluded that “ARPC1B is critical for class switching since our ARPC1B‑deficient patient had reduced frequencies of class‑switched memory B cells,” implying that actin dynamics are essential for germinal center B‑cell interactions and DNA recombination events in class switch recombination.[15] This defect explains the paradoxical observation of hypergammaglobulinemia with altered class‑switched memory B‑cell profiles and autoantibody production in ARPC1B‑deficient individuals.[7][9][14][15]  

Regulatory T cells (Tregs) also appear to be affected; PanelApp notes “defective regulatory T cell (Treg) function” among the consequences of ARPC1B mutations, which likely contributes to autoimmunity and allergic disease.[10][14] The combination of impaired effector T‑cell migration and activation, altered Treg function, and disordered B‑cell class switching creates a milieu of immune dysregulation where infections, allergy, and autoimmunity coexist and amplify one another.[6][7][14][16][17]  

Suggested CL terms include CL:0000895 (T cell), CL:0000788 (neutrophil), CL:0000236 (platelet), CL:0000945 (regulatory T cell), and CL:0000824 (B cell), representing the main cellular players affected. GO terms such as GO:0002283 (neutrophil activation involved in immune response), GO:0002460 (adaptive immune response), and GO:0031295 (T‑cell costimulation) are relevant downstream processes that are impaired.[4][6][7][15][16][18]  

### 6.3 Platelet Biogenesis and Hemostasis

ARPC1B plays a critical role in platelet biogenesis and function. Megakaryocytes rely on Arp2/3‑driven actin branching to form proplatelets, long cytoplasmic extensions that fragment into platelets in the bloodstream.[6][9][14][18] Loss of ARPC1B impairs proplatelet formation and platelet release, leading to thrombocytopenia in many patients.[6][9][14][18] Platelets themselves depend on dynamic actin cytoskeleton remodeling to spread on damaged endothelium and to form stable aggregates during hemostasis; ARPC1B‑deficient platelets show abnormal morphology, decreased dense granules, and impaired spreading ability.[9][14][18]  

These defects manifest clinically as bleeding diathesis, epistaxis, mucosal bleeding, and GI hemorrhage, particularly in the context of colitis or vasculitis. OMIM notes that “laboratory studies show platelets with abnormal shape, decreased dense granules, and impaired spreading ability, as well as immune dysregulation with increased eosinophils, B cells, IgA and IgE, and autoantibodies,” capturing the dual hematologic and immunologic impact.[9] In vitro platelet function tests demonstrate reduced spreading on fibrinogen and impaired aggregation, confirming the functional consequences of ARPC1B loss.[6][9][14][18]  

GO biological process terms relevant to these pathways include GO:0007596 (blood coagulation), GO:0002576 (platelet degranulation), GO:0030168 (platelet activation), and GO:0034332 (adherens junction assembly), all of which are influenced by actin cytoskeleton dynamics. CL:0000236 (platelet) and UBERON:0001982 (bone marrow) denote the cell type and organ where defects originate.[6][9][14][18]  

### 6.4 DNA Damage Response, Aurora‑A, and Radiosensitivity

The discovery of increased radiosensitivity in ARPC1B deficiency revealed a previously unappreciated role for the Arp2/3 complex in DNA damage response and cell‑cycle regulation. The 2022 study showed that ARPC1B‑deficient cells exposed to ionizing radiation or bleomycin exhibited higher levels of chromatid‑type aberrations and γH2AX foci, with an increased number of cells arrested in the G2/M phase of the cell cycle compared to healthy donors and to cells from patients with other immunodeficiencies such as Wiskott–Aldrich syndrome.[13][18]  

The authors integrated these observations with prior work on Arp2/3 in DNA double‑strand break clustering and homologous recombination. They noted that “the arrest of damaged cells in the G2/M‑phase is suggestive of a defective Arp2/3‑ARPC1B complex that is unable to drive DNA double‑strand breaks (DSBs) clustering for homology‑directed repair (HDR),” and that ARPC1B interacts with Aurora‑A kinase, a regulator of mitotic entry.[18] They further stated that ARPC1B localizes to centrosomes and influences Aurora‑A activity, such that ARPC1B depletion delays mitotic entry and alters DNA end‑resection during HDR, preventing proper cell‑cycle progression.[18]  

These findings situate ARPC1B within a broader network of DNA repair and cell‑cycle regulators, suggesting GO biological process terms such as GO:0006281 (DNA repair), GO:0006974 (response to DNA damage stimulus), GO:0007088 (regulation of mitotic nuclear division), and GO:0000086 (G2/M transition of mitotic cell cycle) as relevant annotations. The radiosensitivity trait emerges as a downstream consequence of ARP2/3‑dependent nuclear actin and chromatin dynamics, with ARPC1B deficiency impairing efficient clustering and repair of DSBs and altering checkpoint control.[18]  

Clinically, this mechanistic insight informs caution regarding radiotherapy and potentially suggests that ARPC1B‑deficient patients may fall into a category of DNA repair‑related immunodeficiencies, though their primary phenotype remains dominated by actin cytoskeleton defects in immune cells and platelets.[6][7][9][13][18]  

### 6.5 Immune System Involvement and Tissue Damage

The immune system involvement in ARPC1B deficiency spans innate and adaptive arms. Innate immunity is compromised by defective neutrophil chemotaxis, impaired phagocytosis, and dysregulated inflammatory responses, leading to recurrent bacterial and fungal infections and persistent inflammatory states.[6][7][16][17] Adaptive immunity is impaired by defective T‑cell migration and proliferation, altered Treg function, and disordered B‑cell class switching, producing combined immunodeficiency, autoimmunity, and atopy.[4][6][7][10][14][15][16][17]  

Tissue damage arises from a combination of uncontrolled infection and immune‑mediated inflammation. Chronic sinopulmonary infections can lead to bronchiectasis and lung parenchymal damage; cutaneous vasculitis produces ulcerations and scarring; colitis and GI vasculitis cause mucosal ulceration, bleeding, and potential strictures; and chronic hepatitis from EBV infection damages liver tissue.[7][9][17][19] Mechanisms include oxidative stress from neutrophil activation, cytokine‑driven inflammation, complement activation, and extravasation of immune cells into tissues in the absence of adequate regulatory control.[6][7][17][19]  

GO terms such as GO:0006954 (inflammatory response), GO:0006955 (immune response), GO:0006957 (complement activation), and GO:0006952 (defense response) are relevant to these processes. UBERON terms such as UBERON:0002048 (small intestine), UBERON:0002108 (colon), UBERON:0002049 (large intestine), UBERON:0002049 (skin), and UBERON:0002048 (lung) denote organs commonly affected. CL terms include CL:0000094 (neutrophil), CL:0000895 (T cell), and CL:0000824 (B cell), representing effector populations involved in tissue injury.[6][7][9][17][18][19]  

### 6.6 Metabolic and Biochemical Abnormalities

Specific metabolic changes—such as alterations in lipid, glucose, or amino acid metabolism—have not been extensively reported in ARPC1B deficiency, and the disease does not appear to involve primary enzymatic defects in classical metabolic pathways. However, at the biochemical level, abnormalities include hypergammaglobulinemia, elevated immunoglobulin subclasses, and autoantibody production, reflecting dysregulated B‑cell metabolism and differentiation.[7][9][14][15]  

Platelet dense granule deficiency implies altered storage and release of small molecules such as ADP, serotonin, and calcium, which are critical for coagulation, though these changes are secondary to cytoskeletal defects rather than primary metabolic enzyme deficiencies.[9][14][18]  

### 6.7 Molecular Profiling and Advanced Technologies

Comprehensive transcriptomic, proteomic, metabolomic, or single‑cell analyses of ARPC1B‑deficient patients have not yet been published, but targeted RNA studies in the c.783G>A variant case demonstrated splicing defects and reduced normal transcript levels, providing a first glimpse of disease‑specific gene expression changes.[5] Flow cytometry‑based immunophenotyping and Western blot analyses constitute the main proteomic tools used thus far, revealing loss of ARPC1B protein and alterations in immune cell subset distributions.[1][3][6][15][16][18]  

The radiosensitivity study employed γH2AX immunofluorescence and flow cytometry to quantify DNA damage, effectively serving as a phosphoproteomic marker of DSBs and supporting the concept of impaired HDR.[13][18] Future applications of single‑cell RNA‑seq, ATAC‑seq, and spatial transcriptomics in ARPC1B deficiency could elucidate cell‑type specific mechanisms and heterogeneity within immune and stromal compartments, but such data are currently lacking.  

## 7. Anatomical Structures Affected

### 7.1 Organ‑Level Involvement

ARPC1B deficiency primarily affects organs and systems that depend heavily on hematopoietic and immune cell function. The hematologic system is central, with bone marrow megakaryocytes and peripheral platelets showing structural and functional abnormalities that manifest as thrombocytopenia and bleeding.[6][7][9][14][18] UBERON:0001982 (bone marrow) and UBERON:0000178 (blood) are key anatomical terms for these effects.  

The immune system, including lymphoid organs such as lymph nodes, spleen, and thymus, is extensively involved. Lymphadenopathy, splenomegaly, and sometimes thymic abnormalities are reported, reflecting chronic immune activation and dysregulation.[7][9][19] UBERON:0002375 (spleen), UBERON:0000029 (lymph node), and UBERON:0002370 (thymus) capture these structures.  

Secondary organ involvement arises from infections and immune‑mediated inflammation. The respiratory system (UBERON:0002048, lung) is affected by recurrent pneumonia and bronchitis; the skin (UBERON:0002097) manifests eczema, vasculitis, and keloid scarring; the gastrointestinal tract (UBERON:0002108, colon; UBERON:0002048, small intestine) develops colitis and bleeding; and the liver (UBERON:0002107) may be involved in chronic hepatitis.[7][9][17][19]  

### 7.2 Tissue and Cell‑Level Involvement

At the tissue level, epithelial barriers of skin and mucosa are frequently compromised by inflammation and infection, while connective tissues in vessel walls are targeted by vasculitis.[7][9][17][19] Hematopoietic tissue in the bone marrow is directly impacted by ARPC1B deficiency in megakaryocytes and immune progenitors.  

Cell types most profoundly affected include T cells, B cells, neutrophils, and platelets. T cells (CL:0000895) show impaired migration, synapse formation, and proliferation; regulatory T cells (CL:0000945) exhibit functional defects contributing to autoimmunity; B cells (CL:0000824) display altered class switching and autoantibody production; neutrophils (CL:0000094) demonstrate defective chemotaxis; and platelets (CL:0000236) have abnormal morphology and spreading.[4][6][7][9][14][15][16][17][18]  

### 7.3 Subcellular Localization

Subcellular compartments involved in ARPC1B deficiency include the actin cytoskeleton (GO:0005884, actin cytoskeleton), centrosomes (GO:0005813), and the nucleus, particularly chromatin regions undergoing DNA repair.[3][4][18] ARPC1B localizes to the Arp2/3 complex at the leading edge of migrating cells, facilitating actin branch formation, and also to centrosomes where it interacts with Aurora‑A kinase.[18]  

In DNA damage response, ARP2/3‑dependent actin structures contribute to clustering of DSBs in the nucleus, and ARPC1B deficiency disrupts this process, leading to scattered breaks and inefficient HDR.[18] γH2AX foci mark DSBs, and increased foci in ARPC1B‑deficient cells indicate persistent damage in the nuclear compartment.[13][18]  

## 8. Temporal Development

### 8.1 Onset and Early Course

ARPC1B deficiency is congenital, with clinical manifestations typically emerging in infancy or early childhood. OMIM notes onset of recurrent infections and inflammatory features such as vasculitis and eczema in infancy or early childhood.[9] The 2023 series reports that actinopathies including ARPC1B deficiency “manifest early in life (usually the first two months) as combined or syndromic defects,” although some patients present later in childhood.[7]  

Early course often involves recurrent otitis, sinusitis, and skin infections, severe eczema, and signs of thrombocytopenia such as petechiae or easy bruising. Asthma and food allergies may emerge in toddlerhood, while colitis and vasculitis can appear around the same time or later.[6][7][9][16][17][19]  

### 8.2 Disease Progression and Patterns

Disease progression is variable. Some patients experience a relapsing‑remitting course of inflammatory flares (vasculitis, colitis, arthritis) on a background of chronic eczema and atopy, while others have a more progressive trajectory with cumulative organ damage from recurrent infections and chronic inflammation.[7][9][17][19]  

Colitis and vasculitis can become refractory, leading to chronic pain, GI bleeding, and risk of strictures or perforation. Chronic lung infections may result in bronchiectasis. Radiosensitivity and DNA repair defects may theoretically predispose to malignancy, although long‑term data are sparse.[7][18][19]  

HSCT alters the temporal course by providing a curative reset of hematopoietic and immune systems, often leading to resolution of infections and inflammatory manifestations and improved platelet counts, although transplant‑related complications introduce new risks and may affect long‑term outcomes.[5][6][7][13][17][19]  

### 8.3 Critical Periods and Intervention Windows

The first years of life represent a critical period for diagnosis and intervention. Early recognition of recurrent infections, severe eczema, thrombocytopenia, and vasculitis should prompt evaluation for inborn errors of immunity, including ARPC1B deficiency.[6][7][9][10][14][16][17] Timely HSCT before irreversible organ damage or severe infections occur may improve survival and quality of life, indicating that infancy and early childhood are windows of opportunity for curative treatment.[5][6][7][13][17][19]  

Later childhood and adolescence remain important periods for monitoring and managing complications such as colitis, vasculitis, radiosensitivity, and potential malignancy, requiring ongoing surveillance and adaptation of therapy.[7][18][19]  

## 9. Inheritance and Population

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

ARPC1B deficiency follows an autosomal recessive inheritance pattern, with affected individuals harboring homozygous or compound heterozygous pathogenic variants in *ARPC1B*.[1][5][7][9][10][11][14][16][17][18] OMIM explicitly states that IMD71 is caused by homozygous or compound heterozygous mutation in *ARPC1B* on chromosome 7q22.[9] ClinGen lists ARPC1B with autosomal recessive inheritance for platelet abnormalities with eosinophilia and immune‑mediated inflammatory disease.[11]  

Penetrance appears high among individuals with biallelic truncating variants, given that all reported carriers with such genotypes exhibit clinical manifestations, though expressivity is highly variable.[3][5][7][9][10][14][15][16][17][19] Some patients present with severe thrombocytopenia, life‑threatening infections, and refractory vasculitis, while others have milder disease with limited bleeding and manageable eczema and asthma. The c.783G>A variant family demonstrates that certain alleles may spare platelet counts, indicating variant‑specific expressivity.[5]  

There is no evidence of genetic anticipation, germline mosaicism, or dominant inheritance in the current literature. Carrier parents are clinically unaffected but can transmit the disease in autosomal recessive fashion, making carrier screening and genetic counseling important in populations with known founder variants.[3][5][7][9][11][19]  

### 9.2 Epidemiology and Population Demographics

Exact prevalence and incidence estimates for ARPC1B deficiency are not yet available, but it is considered an ultra‑rare disease, with only a few dozen cases reported worldwide.[6][7][9][10][19] The 2026 abstract from Nepal notes that “only a few dozen cases have been reported worldwide” and that “a single Nepalese center has diagnosed 20 cases (including 14 previously reported cases),” underscoring both the rarity and potential under‑diagnosis of the condition.[19]  

Affected populations include indigenous American groups with the c.899_944del founder variant, Afghan families with the c.783G>A synonymous variant, and South Asian cases from Nepal and possibly India, as well as patients from Europe and North America.[3][5][7][15][19] Consanguinity appears common among reported families, suggesting higher local prevalence in regions where consanguineous marriage is frequent.[5][7][19]  

Sex distribution appears roughly equal, with both males and females affected, consistent with autosomal recessive inheritance.[6][7][9][16][17][19] Age distribution includes infants, children, adolescents, and young adults, with most diagnoses made in childhood due to early onset of symptoms.[6][7][9][16][17][19]  

Carrier frequency for specific pathogenic variants is unknown, but founder alleles such as c.899_944del may have elevated carrier rates in certain populations. Global population databases like gnomAD have not yet provided detailed allele frequencies for these variants, but their absence in control cohorts and presence in multiple affected families support their pathogenicity.[3][7][15][19]  

## 10. Diagnostics

### 10.1 Clinical and Laboratory Evaluation

Diagnostic evaluation of suspected ARPC1B deficiency involves integration of clinical history, physical examination, laboratory tests, and genetic analyses. Clinically, suspicion should arise in patients with combined immunodeficiency features (recurrent infections, eczema, asthma, food allergy), platelet abnormalities (thrombocytopenia, bleeding diathesis), eosinophilia, hypergammaglobulinemia, autoantibodies, vasculitis, and colitis, particularly when onset occurs in infancy or early childhood and when there is parental consanguinity.[6][7][9][10][14][16][17][19]  

Laboratory tests include complete blood counts revealing leukocytosis, eosinophilia, and thrombocytopenia; peripheral blood smears showing abnormal platelet morphology; immunoglobulin quantification demonstrating elevated IgE and IgA; autoantibody panels detecting ANA and ANCA; and lymphocyte subset analysis showing low CD3+ T cells and increased B cells.[7][9][14][16][17] Coagulation studies and platelet function tests may reveal impaired spreading and aggregation.[9][14][18]  

Flow cytometry‑based assessment of ARPC1B protein expression in peripheral blood mononuclear cells can provide direct evidence of deficiency. OMIM reports that “flow cytometric analysis of patient immune cells showed severely reduced ARPC1B levels compared to controls, consistent with a loss of function,” emphasizing the diagnostic value of such assays.[1][3]  

### 10.2 Genetic Testing Strategies

Genetic confirmation is essential for definitive diagnosis. Whole‑exome sequencing (WES) and targeted gene panels for primary immunodeficiency and monogenic inflammatory bowel disease have successfully identified *ARPC1B* mutations in multiple patients.[5][7][13][14][16][18][19] PanelApp lists ARPC1B as part of a “Primary immunodeficiency or monogenic inflammatory bowel disease” gene panel, noting that “a novel syndrome of combined immune deficiency, infections, allergy, and inflammation has been attributed to mutations in the gene encoding actin‑related protein 2/3 complex subunit 1B (ARPC1B).”[14]  

Trio‑based next‑generation sequencing (affected child and both parents) enhances detection and interpretation of autosomal recessive variants and has been used in the radiosensitivity cohort to obtain molecular diagnosis.[13][18] Once a pathogenic variant is identified, segregation analysis in family members confirms inheritance pattern and allows carrier testing.[3][5][7][15][19]  

Single‑gene testing by Sanger sequencing of *ARPC1B* exons and splice sites may be appropriate in families with known variants or in settings where WES is unavailable. RNA sequencing can be used to evaluate splicing‑affecting synonymous variants, as demonstrated in the c.783G>A case.[5] Chromosomal microarray, karyotyping, and FISH are not primary diagnostic tools for ARPC1B deficiency, as the disease is caused by point mutations and small indels rather than copy number changes or chromosomal rearrangements.[3][5][7][13][15][16][17][18]  

### 10.3 Omics‑Based Diagnostic Tools and Biomarkers

Beyond DNA sequencing, omics‑based tools have limited but emerging roles. RNA studies are crucial for variants suspected to affect splicing, as in the c.783G>A case where targeted RNA analysis revealed splicing defects.[5] Proteomic assessments, such as Western blotting and flow cytometry for ARPC1B protein, provide functional confirmation of loss‑of‑function at the protein level.[1][3][6][18]  

γH2AX staining and analysis of chromatid‑type aberrations in irradiated cells serve as biomarkers of radiosensitivity and DNA repair defects, useful for characterizing disease traits and potentially informing clinical decisions regarding radiotherapy.[13][18] However, these assays are currently research tools and not standard diagnostic measures.  

Standardized diagnostic criteria for ARPC1B deficiency have not yet been published by professional societies, but the convergence of clinical features, immunologic laboratory abnormalities, and genetic confirmation constitutes the practical diagnostic framework used in reported cases.[6][7][9][10][14][16][17][19] Differential diagnoses include Wiskott–Aldrich syndrome, other actinopathies, common variable immunodeficiency, and primary inflammatory bowel disease, which can be distinguished by specific genetic findings, platelet morphology, and immunophenotypic patterns.[6][7][14][16][17][18]  

### 10.4 Screening and Early Detection

Population‑based newborn screening for ARPC1B deficiency does not currently exist, and the rarity of the disease makes such programs challenging to justify. However, carrier screening and cascade testing in families with known pathogenic variants can identify at‑risk individuals and inform reproductive decisions.[3][5][7][15][19]  

In clinical practice, early detection relies on heightened awareness among pediatricians, immunologists, and hematologists. Use of broad immunodeficiency gene panels in children with syndromic features (infections, eczema, thrombocytopenia, colitis, vasculitis) improves early diagnosis and can accelerate referral for HSCT evaluation.[7][13][14][16][17][19]  

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

Because ARPC1B deficiency has only recently been described and relatively few cases have long‑term follow‑up, precise survival and mortality statistics are unavailable. Nonetheless, reported outcomes indicate that, without curative therapy, severe infections, bleeding, and inflammatory complications can be life‑threatening, while HSCT can markedly improve survival in many patients.[5][6][7][13][16][17][19]  

The Afghan sibling case report describes HSCT from an HLA‑matched healthy sibling as a therapeutic decision facilitated by next‑generation sequencing diagnosis, with successful outcomes noted for at least some siblings.[5] The 2023 series and other reports state that “stem‑cell transplantation has been curative” in ARPC1B deficiency, with resolution of infections and inflammatory manifestations and normalization of platelet counts in transplanted patients.[7][13][17][19]  

Without HSCT, life expectancy is likely reduced, particularly in individuals with severe thrombocytopenia, refractory colitis, and vasculitis. Mortality may result from severe infections (sepsis, meningitis, pneumonia), massive GI bleeding, or complications of chronic inflammation such as organ failure, although specific case‑level details are not always reported.[6][7][9][16][17][19]  

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in ARPC1B deficiency is substantial, encompassing recurrent infections, chronic eczema and pruritus, asthma, colitis, vasculitis, arthritis, bleeding diathesis, and growth impairment.[6][7][9][10][17][19] These manifestations lead to frequent hospitalizations, long‑term medication use (antibiotics, immunosuppressants, corticosteroids), dietary restrictions, and psychosocial stress. Physical disability may arise from joint damage due to arthritis, scarring from vasculitis and keloids, and chronic fatigue from anemia and inflammation.[7][17][19]  

Quality‑of‑life measures such as EQ‑5D or SF‑36 have not been specifically applied to ARPC1B‑deficient cohorts, but qualitative descriptions indicate significant impairment in domains of physical health, emotional well‑being, and social functioning, particularly in severely affected patients prior to HSCT.[6][7][17][19] Post‑transplant, many patients experience improved quality of life, though transplantation introduces its own risks and long‑term sequelae.[5][7][13][17][19]  

### 11.3 Prognostic Factors and Biomarkers

Prognostic factors likely include age at diagnosis, severity of thrombocytopenia and bleeding, frequency and severity of infections, extent of vasculitis and colitis, presence of radiosensitivity, and availability of HSCT.[6][7][9][13][17][19] Early diagnosis and timely HSCT are associated with better outcomes, as they prevent cumulative organ damage and reduce risk of fatal complications.[5][6][7][13][17][19]  

Biomarkers such as ARPC1B protein expression, immunoglobulin levels, eosinophil counts, and γH2AX responses to DNA damage may provide prognostic information, though formal predictive models have not yet been developed.[1][3][6][7][13][15][18][19] For instance, severe radiosensitivity might indicate higher risk of treatment‑related complications from radiotherapy or certain chemotherapies, influencing prognostic assessment in patients who develop malignancies or require such therapies.[13][18]  

## 12. Treatment

### 12.1 Hematopoietic Stem Cell Transplantation (HSCT)

HSCT is currently the only established curative treatment for ARPC1B deficiency. By replacing the patient’s hematopoietic system with donor stem cells, HSCT can restore functional ARPC1B expression in immune cells and platelets, thereby correcting combined immunodeficiency, immune dysregulation, and thrombocytopenia.[5][6][7][13][16][17][19]  

The Afghan sibling case report explains that “next generation sequencing (NGS) studies facilitated the diagnosis of this rare combined immunodeficiency and led to the decision to treat the affected patients with hematopoietic cell transplant (HCT) from an human leukocyte antigen (HLA)‑matched healthy sibling.”[5] Post‑transplant, patients showed clinical improvement, including reduced infections and inflammation, though transplant‑related challenges such as graft‑versus‑host disease and immunosuppression risks must be managed.[5][7][13][17][19]  

The 2023 series notes that “stem‑cell transplantation has been curative” in ARPC1B deficiency, based on experiences from several families.[7] HSCT is therefore recommended for severe cases, ideally performed early in life before irreversible organ damage occurs, using standard conditioning regimens and donor selection practices for primary immunodeficiencies.[6][7][13][17][19] Suggested NCIT term is NCIT:C15206 (Hematopoietic Stem Cell Transplantation).  

### 12.2 Immunomodulatory and Supportive Pharmacotherapy

Supportive pharmacotherapy plays a crucial role in managing infections and immune‑mediated complications. Immunoglobulin replacement therapy (intravenous or subcutaneous) may be used to prevent recurrent infections in patients with hypogammaglobulinemia or dysfunctional antibody responses, although ARPC1B‑deficient patients often have hypergammaglobulinemia; nevertheless, functional antibody defects may still warrant supplementation in some cases.[6][7][16][17] NCIT:C15443 (Immunoglobulin Therapy) is an appropriate term.  

Antimicrobial prophylaxis with antibiotics and antifungals is commonly employed to reduce infection burden. Corticosteroids and other immunosuppressants (e.g., azathioprine, methotrexate) are used to control vasculitis, colitis, and arthritis, though they must be carefully balanced against infection risks, and their long‑term use is ideally minimized through early HSCT when feasible.[7][17][19]  

A notable recent development is the use of sirolimus (rapamycin), an mTOR inhibitor, as a management strategy for thrombocytopenia related to ARPC1B deficiency. A 2026 Frontiers in Immunology paper notes that “ARPC1B expression is restricted to hematopoietic cells, playing a key role in the development of adaptive immune cells and thrombocytes,” and explores sirolimus as a therapeutic agent to modulate megakaryocyte and platelet function.[8] While detailed results are not fully available in the abstract snippet, sirolimus may improve platelet counts and reduce inflammatory complications by targeting mTOR‑dependent pathways, representing a promising adjunct or alternative for patients not immediately eligible for HSCT.[8] NCIT:C1315 (Sirolimus) and NCIT:C20401 (mTOR Inhibitor) are relevant terms.  

Asthma and allergic disease are treated with standard therapies such as inhaled corticosteroids, leukotriene receptor antagonists, antihistamines, and biologic agents targeting IgE or eosinophils (e.g., omalizumab), though evidence specific to ARPC1B deficiency is limited.[7][10][16][17]  

### 12.3 Management of Radiosensitivity

Given increased radiosensitivity, careful management is required when ARPC1B‑deficient patients require radiologic procedures or radiotherapy. Diagnostic imaging involving low‑dose radiation (e.g., X‑rays) is generally safe with appropriate precautions, but therapeutic radiotherapy should be used cautiously, with consideration of alternative modalities when possible.[13][18]  

If chemotherapy with radiomimetic agents like bleomycin is necessary, close monitoring of hematologic and immunologic parameters and dose adjustments may be warranted. While formal guidelines have not yet been developed, the radiosensitivity study’s findings suggest that ARPC1B‑deficient patients might benefit from individualized radiation dosing and frequent assessment of toxicity.[13][18]  

### 12.4 Surgical and Interventional Care

Surgical interventions may be required for severe GI bleeding (e.g., endoscopic hemostasis, bowel resection) or complications of vasculitis and colitis, such as perforation or strictures.[17][19] Perioperative management must account for thrombocytopenia and platelet dysfunction, often necessitating platelet transfusions and careful hemostatic planning.  

Central venous catheter placement and other procedures common in HSCT and chronic disease care also require bleeding risk assessment. NCIT terms relevant to surgical interventions include NCIT:C15176 (Surgical Procedure) and NCIT:C48843 (Endoscopic Procedure).  

### 12.5 Experimental and Future Therapies

Gene therapy and gene editing for ARPC1B deficiency have not yet entered clinical trials, but the monogenic nature of the disease and hematopoietic restriction of ARPC1B expression make it an attractive target for hematopoietic stem cell gene therapy using viral vectors or CRISPR‑based editing. Proof‑of‑concept in related actinopathies and primary immunodeficiencies (e.g., Wiskott–Aldrich syndrome) suggests that ex vivo correction of hematopoietic stem cells followed by autologous transplantation could eventually be developed for ARPC1B deficiency.[6][7][18]  

RNA‑based therapies targeting specific splicing defects, like the c.783G>A variant, could theoretically restore correct splicing, but no such interventions have yet been reported.  

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of ARPC1B deficiency at the population level is currently impractical due to its ultra‑rare nature and the diversity of causal variants. However, in families with known pathogenic mutations, primary prevention can involve pre‑implantation genetic diagnosis or prenatal testing to avoid having affected offspring, guided by genetic counseling.[3][5][7][15][19]  

Secondary prevention focuses on early detection and intervention to prevent severe complications. Use of broad immunodeficiency gene panels in children with syndromic features (infections, eczema, thrombocytopenia, colitis, vasculitis) enables earlier diagnosis and timely HSCT, reducing morbidity and mortality.[7][13][14][16][17][19]  

Tertiary prevention involves preventing complications in those already diagnosed. This includes infection prophylaxis, vaccination, careful management of thrombocytopenia and bleeding, monitoring and treatment of colitis and vasculitis, and avoidance or minimization of DNA‑damaging therapies that could exploit radiosensitivity.[6][7][9][13][17][18][19]  

### 13.2 Genetic Counseling and Family Planning

Genetic counseling is essential for families affected by ARPC1B deficiency. Counselors should explain autosomal recessive inheritance, carrier risks, recurrence risks in future pregnancies, and options for carrier screening among extended family members.[3][5][7][9][11][15][19] In populations with founder variants, community‑level education and screening may be considered.  

NCIT: C18089 (Genetic Counseling) is an appropriate term.  

### 13.3 Infection Prevention and Public Health Measures

Standard public health measures such as vaccination, good hygiene, and prompt treatment of infections are critical for preventing severe disease episodes in ARPC1B‑deficient patients. While live vaccines may be contraindicated in some immunodeficiencies, decisions must be individualized based on immune function; influenza and pneumococcal vaccinations are generally recommended.[6][7][10][16][17]  

Avoidance of known allergens and triggers of eczema and asthma, as well as dietary management of food allergies, helps reduce inflammatory flares and contributes to tertiary prevention.[7][10][17][19]  

## 14. Other Species and Natural Disease

### 14.1 Orthologs and Comparative Biology

Orthologous genes for ARPC1B exist in multiple species, including mice, zebrafish, and other vertebrates, reflecting evolutionary conservation of the Arp2/3 complex. NCBI Gene lists ARPC1B orthologs across model organisms, although specific ARPC1B‑deficient natural diseases in animals have not been widely reported.[4][18]  

Comparative pathology of actin cytoskeleton defects is better characterized for other genes, such as WAS in Wiskott–Aldrich syndrome, but similar principles likely apply to ARPC1B, with immune and platelet defects in species lacking functional ARPC1B.[6][7][18]  

### 14.2 Zoonotic Potential and Cross‑Species Susceptibility

ARPC1B deficiency is a non‑infectious genetic disorder and does not have zoonotic potential. Cross‑species susceptibility pertains to conservation of the gene and potential to induce similar phenotypes in animal models rather than natural interspecies transmission.[4][18]  

## 15. Model Organisms

### 15.1 Existing and Potential Models

Specific ARPC1B knockout or knock‑in animal models have not yet been detailed in the provided literature, but studies of the Arp2/3 complex, including ARPC1B, have been conducted in cell lines and in murine systems for DNA repair and cell‑cycle investigations.[18] For example, Schrank et al., cited in the radiosensitivity study, explored the role of Arp2/3 in DSB clustering and HDR, likely using cell and animal models to demonstrate functional consequences.[18]  

The lack of published ARPC1B‑specific mouse models represents an opportunity for future research. Creating conditional ARPC1B knockouts in hematopoietic cells could recapitulate human phenotypes, including combined immunodeficiency, platelet abnormalities, and radiosensitivity, enabling detailed mechanistic and therapeutic studies.[4][6][7][18]  

### 15.2 Applications and Limitations

Model organisms for ARP2/3 complex research provide insight into fundamental actin cytoskeleton biology and DNA repair, but ARPC1B’s hematopoietic restriction in humans means that systemic knockout models may not fully mimic human tissue specificity unless carefully designed.[4][18] Cellular models (e.g., CRISPR‑edited human cell lines lacking ARPC1B) can elucidate immune synapse, migration, and HDR mechanisms, but they cannot capture organism‑level outcomes such as thrombocytopenia and colitis.  

The main limitation is that, without dedicated ARPC1B‑deficient animal models, translational application of mechanistic findings to clinical therapy is constrained. Nonetheless, existing actinopathy models and DNA repair studies provide a conceptual framework for understanding ARPC1B deficiency and for designing future interventions.[6][7][18]  

## Conclusion

ARPC1B deficiency, formally classified as Immunodeficiency‑71 with inflammatory disease and congenital thrombocytopenia and indexed in MONDO as platelet abnormalities with eosinophilia and immune‑mediated inflammatory disease (MONDO:0060583), represents a paradigmatic example of an actin cytoskeleton‑related inborn error of immunity.[1][7][9][10][11][14] Biallelic germline loss‑of‑function mutations in *ARPC1B*, a hematopoietic‑restricted regulatory subunit of the Arp2/3 complex, disrupt actin branching in immune cells and platelets, leading to combined immunodeficiency, immune dysregulation with allergy and autoimmunity, congenital platelet abnormalities with bleeding diathesis, eosinophilia, hypergammaglobulinemia, and, more recently, increased radiosensitivity linked to defective DNA double‑strand break clustering and homologous recombination.[3][4][6][7][9][10][13][15][16][17][18]  

Clinically, the disease manifests in infancy or early childhood with recurrent ear, skin, and lung infections; severe eczema, asthma, and food allergies; cutaneous and systemic vasculitis; colitis and gastrointestinal bleeding; thrombocytopenia and abnormal platelet morphology; short stature; lymphadenopathy; and a distinctive immunologic laboratory profile featuring leukocytosis, eosinophilia, elevated IgE and IgA, and autoantibodies.[6][7][9][10][14][16][17][19] The phenotypic spectrum is heterogeneous, with variant‑specific expressivity and possible modifier influences, but the core pathophysiology consistently reflects impaired immune cell migration and synapse formation, dysregulated regulatory T‑cell and B‑cell function, abnormal platelet biogenesis and spreading, and compromised DNA damage response.[4][6][7][9][14][15][16][17][18]  

Diagnostic strategies integrate clinical recognition of syndromic features with laboratory evaluation and genetic testing, including WES, targeted panels, single‑gene sequencing, and RNA studies for splicing defects, complemented by flow cytometry and Western blot assessments of ARPC1B protein expression.[1][3][5][6][7][13][14][16][17][18][19] Differential diagnosis includes other actinopathies and primary immunodeficiencies, but the specific combination of platelet abnormalities, eosinophilia, hyper‑IgE/IgA, and vasculitis strongly suggests ARPC1B deficiency when present.  

Treatment currently centers on HSCT as the only curative option, which can restore functional ARPC1B expression in hematopoietic cells and resolve immunologic and hematologic manifestations, particularly when performed early.[5][6][7][13][17][19] Supportive therapies include immunoglobulin replacement, antimicrobial prophylaxis, corticosteroids and immunosuppressants for vasculitis and colitis, standard asthma and eczema treatments, and emerging use of sirolimus for thrombocytopenia.[6][7][8][10][16][17][19] Radiosensitivity mandates cautious use of radiotherapy and radiomimetic chemotherapies, underscoring the need for personalized oncologic management in ARPC1B‑deficient patients.[13][18]  

Future directions involve expanding epidemiologic understanding, developing standardized diagnostic and management guidelines, exploring gene therapy or gene‑editing approaches, and generating dedicated ARPC1B‑deficient animal and cellular models to dissect mechanisms and test interventions. As more cases are reported, particularly from centers like the Nepalese cohort that have diagnosed multiple individuals, a more comprehensive natural history will emerge, enabling refined prognostic assessments and improved quality of life for patients with this complex, multi‑system actinopathy‑associated immunodeficiency.[7][18][19]

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.