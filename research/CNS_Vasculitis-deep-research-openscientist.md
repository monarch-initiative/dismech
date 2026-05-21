---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-16T03:23:53.547033'
end_time: '2026-05-16T04:06:00.037920'
duration_seconds: 2526.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CNS Vasculitis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 56
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CNS Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **CNS Vasculitis** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Comprehensive Disease Characterization Report: CNS Vasculitis

## Summary

**Central Nervous System (CNS) Vasculitis** is a rare and heterogeneous group of inflammatory vasculopathies characterized by transmural inflammation of blood vessels within the brain, spinal cord, and leptomeninges. The primary form — **Primary Angiitis of the Central Nervous System (PACNS)** — has an estimated prevalence of approximately 2.4 cases per million person-years in North America, making it one of the rarest vasculitides. PACNS presents with a triad of headache (51%), focal neurological deficits (63%), and cognitive impairment (41%), and encompasses four histopathological subtypes: lymphocytic (65%), amyloid-beta-related angiitis/ABRA (16%), granulomatous (14%), and necrotizing (5%). Secondary CNS vasculitis occurs in the context of systemic vasculitides (ANCA-associated vasculitis, Behcet's disease) or connective tissue disorders (neuropsychiatric lupus).

Diagnosis remains challenging due to the absence of specific biomarkers, requiring a multimodal approach integrating clinical assessment, cerebrospinal fluid (CSF) analysis, advanced neuroimaging (particularly vessel wall MRI, which improves diagnostic accuracy from 36% to 89%), and brain biopsy as the gold standard for small-vessel disease. Critical differential diagnoses include reversible cerebral vasoconstriction syndrome (RCVS), cerebral amyloid angiopathy-related inflammation (CAA-RI), monogenic vasculitides such as DADA2 (Deficiency of Adenosine Deaminase 2), Tregopathies, and tumefactive PACNS mimicking glioblastoma. Treatment is empiric, relying on glucocorticoids plus cyclophosphamide for induction (which reduces relapse incidence with HR 0.47, 95% CI 0.24–0.92) followed by maintenance immunosuppression with mycophenolate mofetil, azathioprine, methotrexate, or rituximab.

Emerging pathophysiological insights reveal a complex immune-mediated mechanism involving IL-17/Th17 pathway activation, NK cells, M1 macrophages, memory B cells, follicular helper T cells, mitochondrial dysfunction, and upregulation of TBC1D3C/TBC1D3L genes. Neurofilament light chain (NfL) has emerged as a promising biomarker for disease activity, particularly in younger patients. IL-17 inhibition represents a rational translational therapeutic candidate based on convergent evidence from CSF cytokine profiling and successful anti-IL-17 trials in related large-vessel vasculitides. Despite progress, approximately one-third of patients have poor neurological outcomes, with the granulomatous subtype carrying the worst prognosis (25% mortality, only 29% induction response rate).

---

## 1. Disease Information

### Overview

CNS Vasculitis encompasses inflammatory disorders affecting blood vessels of the central nervous system. **PACNS** is the primary (idiopathic) form, restricted exclusively to the brain, spinal cord, and leptomeninges without systemic involvement. Secondary CNS vasculitis occurs as a manifestation of systemic diseases including ANCA-associated vasculitides, Behcet's disease, systemic lupus erythematosus, sarcoidosis, and infections.

PACNS was first described by Cravioto and Feigin in 1959 and later defined by Calabrese and Mallek in 1988 with three criteria: (1) an acquired neurological deficit unexplained by other diagnoses, (2) angiographic or histopathologic evidence of CNS vasculitis, and (3) no evidence of systemic vasculitis or infection. It remains "a rare autoimmune condition characterized by exclusive involvement of the brain, spinal cord, and leptomeninges" with "an estimated prevalence of 2.4 cases per million person-years in North America" representing "one of the rarest vasculitides" ([PMID: 41947889](https://pubmed.ncbi.nlm.nih.gov/41947889/)).

### Key Identifiers

| Identifier | Code/Term |
|---|---|
| **ICD-10** | I67.7 (Cerebral arteritis, not elsewhere classified) |
| **ICD-11** | 8B22.0 (Primary angiitis of the central nervous system) |
| **MeSH** | D020293 (Vasculitis, Central Nervous System) |
| **MONDO** | MONDO:0007141 (cerebral vasculitis) |
| **Orphanet** | ORPHA:140989 (Primary angiitis of the central nervous system) |
| **DOID** | DOID:13550 (central nervous system vasculitis) |
| **SNOMED CT** | 195185003 (Cerebral arteritis) |
| **OMIM** | Not assigned for PACNS (DADA2: 615688) |

### Synonyms and Alternative Names

- Primary angiitis of the central nervous system (PACNS)
- Primary central nervous system vasculitis (PCNSV)
- Isolated angiitis of the CNS
- Granulomatous angiitis of the CNS (historical)
- Cerebral vasculitis (primary)

### Information Sources

This report is derived from aggregated disease-level resources including systematic reviews, multicenter cohort studies, meta-analyses, and case series. Key data sources include the largest systematic review and meta-analysis of 46 cohort studies encompassing 911 PACNS patients ([PMID: 34663675](https://pubmed.ncbi.nlm.nih.gov/34663675/)), a multicenter German cohort of 163 patients ([PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/)), and multiple single-center biopsy-proven cohorts. Information is synthesized from 113 scientific publications with 40+ unique PMID citations.

---

## 2. Etiology

### Disease Causal Factors

PACNS is of **unknown etiology**. It is classified as an autoimmune/autoinflammatory condition, but the precise triggers remain elusive. The disease likely involves a combination of:

- **Immune dysregulation**: Aberrant activation of innate and adaptive immune responses targeting cerebral vessel walls, with dendritic cell maturation, NK cell activation, M1 macrophage polarization, and elevated IL-17 in CSF ([PMID: 41947889](https://pubmed.ncbi.nlm.nih.gov/41947889/); [PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/))
- **Infectious triggers**: Varicella zoster virus (VZV) has been identified as a potential trigger — anti-VZV IgG antibodies were detected in CSF of 32% of primary cerebral vasculitis patients, suggesting VZV activation in the trigeminal ganglion with transaxonal spread to cerebral arteries ([PMID: 41782529](https://pubmed.ncbi.nlm.nih.gov/41782529/)). VZV reactivation was found in 37% of HIV-infected and 9% of HIV-uninfected young adults presenting with stroke ([PMID: 35133008](https://pubmed.ncbi.nlm.nih.gov/35133008/))
- **Amyloid-related mechanisms**: In the ABRA subtype, inflammatory response directed against vascular amyloid-beta accumulation ([PMID: 37151140](https://pubmed.ncbi.nlm.nih.gov/37151140/))
- **Genetic susceptibility**: While no GWAS has been performed for PACNS specifically due to its rarity, cross-vasculitis genetics implicate HLA region polymorphisms as major susceptibility factors

### Risk Factors

#### Genetic Risk Factors

No PACNS-specific causal genes have been identified through GWAS. However, cross-phenotype Immunochip meta-analysis of 2,465 vasculitis patients identified shared susceptibility loci across vasculitides, with the HLA region showing the strongest signals ([PMID: 29374629](https://pubmed.ncbi.nlm.nih.gov/29374629/)). Related vasculitis genetics include:

- **HLA-B*52**: Associated with Takayasu arteritis (OR=3.29, p=5.57×10⁻¹⁶) ([PMID: 23830517](https://pubmed.ncbi.nlm.nih.gov/23830517/))
- **HLA-B*51**: Strongest genetic association with Behcet's disease (which causes secondary CNS vasculitis)
- **ApoE ε4/ε4 genotype**: Found in up to 70% of ABRA patients, strongly linking this PACNS subtype to cerebral amyloid angiopathy ([PMID: 24636849](https://pubmed.ncbi.nlm.nih.gov/24636849/))
- **ERAP1, CCR1-CCR3, STAT4, KLRC4, GIMAP4, TNFAIP3**: Associated with Behcet's disease; **SERPINA1 and SEMA6A**: Associated with ANCA-associated vasculitides ([PMID: 25405820](https://pubmed.ncbi.nlm.nih.gov/25405820/))
- **ADA2 gene mutations**: Biallelic mutations cause DADA2, a monogenic CNS vasculitis mimic (OMIM: 615688)
- **TBC1D3C and TBC1D3L gene upregulation**: Identified in PACNS brain tissue, suggesting altered vesicular trafficking ([PMID: 41947889](https://pubmed.ncbi.nlm.nih.gov/41947889/))

#### Environmental Risk Factors

- **Infections**: VZV, HIV, CMV, tuberculosis, syphilis, and other neurotropic pathogens can trigger secondary or post-infectious CNS vasculitis ([PMID: 39663273](https://pubmed.ncbi.nlm.nih.gov/39663273/))
- **Age**: PACNS median age of onset 46–48 years; older age associated with poorer survival (HR 1.96 per 10 years) ([PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/)); pediatric forms have mean onset of ~7.89 years
- **Sex**: Slight male predominance in most adult cohorts (55–58% male), though some series report near-equal distribution (45% female in the German cohort)
- **Cardiovascular risk factors**: Body weight has been specifically associated with PACNS vessel-size phenotype ([PMID: 41041677](https://pubmed.ncbi.nlm.nih.gov/41041677/))
- **Adverse childhood experiences (ACEs)**: Associated with neuropsychiatric SLE (adjusted OR=3.40, 95% CI 1.55–7.78), suggesting psychosocial stress may contribute to secondary CNS vasculitis ([PMID: 42009372](https://pubmed.ncbi.nlm.nih.gov/42009372/))

### Protective Factors

- **HLA-C*03**: Identified as a putative protective factor in Takayasu arteritis, present exclusively in patients with clinically mild disease ([PMID: 34931621](https://pubmed.ncbi.nlm.nih.gov/34931621/))
- **HLA-B*44**: Under-transmitted in Kawasaki disease families, suggesting a protective role ([PMID: 25809546](https://pubmed.ncbi.nlm.nih.gov/25809546/))
- **Early diagnosis and treatment**: Strongest modifiable factor; longer time from onset to treatment is an independent predictor of worse outcomes ([PMID: 41479923](https://pubmed.ncbi.nlm.nih.gov/41479923/))
- No PACNS-specific protective factors have been identified

### Gene-Environment Interactions

The intersection of VZV neurotropism and host immune susceptibility is the best-characterized gene-environment interaction. Genetically immunocompromised individuals (e.g., HIV-positive patients) show substantially higher rates of VZV-associated cerebral vasculopathy. In mouse models, T-cell-deficient (nude and SCID) mice are susceptible to CMV-induced CNS vasculitis while immunocompetent controls are resistant, demonstrating the critical role of adaptive immunity in controlling viral entry and dissemination in the brain ([PMID: 14722303](https://pubmed.ncbi.nlm.nih.gov/14722303/)). Genetic defects in innate antiviral immunity, inflammation, and autophagy have been identified in children with VZV CNS infections via whole exome sequencing ([PMID: 40848267](https://pubmed.ncbi.nlm.nih.gov/40848267/)). In ABRA, the ApoE ε4 genotype predisposes to cerebral amyloid angiopathy, upon which an inflammatory autoimmune response to beta-amyloid develops ([PMID: 24636849](https://pubmed.ncbi.nlm.nih.gov/24636849/)).

---

## 3. Phenotypes

### Core Clinical Phenotypes

The largest systematic review and meta-analysis (n=911 PACNS patients from 46 cohort studies) established the following symptom frequencies ([PMID: 34663675](https://pubmed.ncbi.nlm.nih.gov/34663675/)):

| Phenotype | Frequency | HPO Term | Type |
|---|---|---|---|
| Focal neurological signs | 63% | HP:0001269 (Hemiparesis) / HP:0007272 | Clinical sign |
| Headache | 51% | HP:0002315 (Headache) | Symptom |
| Cognitive impairment | 41% | HP:0100543 (Cognitive impairment) | Behavioral |
| Seizures | 16–36% | HP:0001250 (Seizures) | Clinical sign |
| Visual disturbances | ~20% | HP:0000504 (Abnormality of vision) | Symptom |
| Aphasia | ~15% | HP:0002381 (Aphasia) | Clinical sign |
| Ataxia | ~10% | HP:0001251 (Ataxia) | Clinical sign |
| Altered consciousness | Variable | HP:0007185 (Loss of consciousness) | Clinical sign |
| Psychiatric symptoms | Variable | HP:0000708 (Behavioral abnormality) | Behavioral |
| CSF elevated protein | 65–75% | HP:0002922 (Elevated CSF protein) | Laboratory |
| CSF pleocytosis | 65–75% | HP:0012229 (CSF pleocytosis) | Laboratory |

> "The most frequent onset symptoms were focal neurologic signs (63%), headache (51%), and cognitive impairment (41%). Biopsy- compared with angiogram-confirmed cases had higher occurrences of cognitive impairment (55% vs 39%) and seizures (36% vs 16%), whereas focal neurologic signs occurred less often (56% vs 95%)" ([PMID: 34663675](https://pubmed.ncbi.nlm.nih.gov/34663675/))

### Vessel-Size-Dependent Phenotypic Differences

PACNS phenotype varies critically by vessel caliber involved:

| Feature | Large-Vessel PACNS | Small-Vessel PACNS | p-value |
|---|---|---|---|
| Cerebrovascular events | 88.9% | 58.2% | 0.027 |
| Ischemic infarction | 66.7% | 20.7% | 0.002 |
| Tumor-like lesions | 5.6% | 41.4% | 0.008 |
| Limb weakness/sensory | 83.3% | 34.5% | 0.001 |
| Baseline mRS score | 2 | 3 | 0.043 |
| Time to treatment (days) | 58.5 | 154 | 0.013 |

Data from [PMID: 41479923](https://pubmed.ncbi.nlm.nih.gov/41479923/): "Compared with LV-PACNS, SV-PACNS had more severe initial neurological impairment (baseline modified Rankin Scale mRS score: 3 vs. 2, p=0.043) and a longer median time from onset to treatment initiation (154 days vs. 58.5 days, p=0.013)"

### Phenotype Characteristics

- **Age of onset**: Median 46–48 years in adults; mean 7.89 years in pediatric cases
- **Severity**: Variable — 52% had poor outcomes (mRS 3–6) in the German multicenter cohort; 18% died ([PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/))
- **Progression**: Relapsing-remitting in ~50% of patients; rapidly progressive variants carry highest mortality
- **Onset pattern**: Typically subacute (weeks to months); occasionally acute with stroke presentation

### Quality of Life Impact

Long-term follow-up (mean 5.5 years, n=27) using validated instruments demonstrated significant residual morbidity ([PMID: 30789149](https://pubmed.ncbi.nlm.nih.gov/30789149/)):

| Domain (EuroQol) | No Problems | Some/Severe Problems |
|---|---|---|
| Mobility | 51.9% | 48.1% |
| Self-care | 66.7% | 33.3% |
| Usual activities | 55.6% | 44.4% |
| Pain/discomfort | 51.9% | 48.1% |
| Anxiety/depression | 29.6% | **70.4%** |

> "Nineteen of 27 patients (70.4%) had mild disability; meanwhile, 5 (18.5%) had severe disability. [...] Approximately 70% of patients had minimal or no depression" ([PMID: 30789149](https://pubmed.ncbi.nlm.nih.gov/30789149/))

Intellectual functioning in pediatric CNS vasculitis: children with small-vessel disease had significantly lower FSIQ scores (81.90 vs. 94.82, p=0.04), with 24% showing intellectual disability (FSIQ <70) ([PMID: 30762375](https://pubmed.ncbi.nlm.nih.gov/30762375/)).

### Spinal Cord Involvement (HP:0002196)

Spinal cord PACNS is a rare but severe subset with 29% mortality at follow-up. Mainly thoracic and cervical cord involved. Granulomatous pattern most common histologically in spinal cases ([PMID: 39979764](https://pubmed.ncbi.nlm.nih.gov/39979764/)).

---

## 4. Genetic/Molecular Information

### Causal Genes

PACNS itself has no identified causal gene. However, several monogenic conditions cause CNS vasculitis:

| Gene | Condition | OMIM | Inheritance | Key Features |
|---|---|---|---|---|
| **ADA2** (HGNC:1839) | DADA2 | 615688 | AR | Childhood-onset PAN-like vasculitis, lacunar strokes, livedo reticularis |
| **LRBA** | Tregopathy | 614700 | AR | Regulatory T-cell deficiency with autoimmune complications including CNS vasculitis |
| **CTLA4** | CHAI disease | 616100 | AD | Immune dysregulation with CNS vasculitis |
| **FOXP3** | IPEX syndrome | 304790 | X-linked | Multi-organ autoimmunity including CNS vasculitis |
| **CD25/IL2RA** | Tregopathy | 606367 | AR | Immune dysregulation |
| **STAT3** (GOF) | STAT3 GOF syndrome | 615952 | AD | Multi-organ autoimmunity |

**DADA2** is the best-characterized monogenic cause. Autopsy findings revealed "numerous small, old infarcts throughout the brain that had not been demonstrated on prior MRI/MRA imaging" ([PMID: 29963054](https://pubmed.ncbi.nlm.nih.gov/29963054/)). Patients carry compound heterozygous or homozygous mutations (e.g., c.973-2A>G splice site, p.Val458Asp missense). Anti-TNF therapy is the treatment of choice — distinct from standard PACNS treatment.

**Tregopathies** (LRBA, CTLA4, FOXP3/IPEX, CD25, STAT3 GOF): median onset 4.25 years, CNS vasculitis among autoimmune complications, requiring mTOR inhibitors or abatacept rather than standard immunosuppression ([PMID: 41142805](https://pubmed.ncbi.nlm.nih.gov/41142805/)).

### Gene Expression Profiles

Gene expression profiling of PACNS brain tissue (RNA-seq: 4 granulomatous, 5 lymphocytic, 4 ABRA vs. 4 controls) revealed significant molecular alterations ([PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/)):

- **Upregulated pathways**: Dendritic cell maturation, antigen processing, neuroinflammation
- **Downregulated pathways**: Oxidative phosphorylation (indicating mitochondrial dysfunction)
- **Specific genes**: TBC1D3C and TBC1D3L upregulation (vesicular trafficking) ([PMID: 41947889](https://pubmed.ncbi.nlm.nih.gov/41947889/))

> "Pathway analysis revealed the activation of dendritic cell maturation and antigen processing as well as neuroinflammation in PCNSV versus normal brain, whereas oxidative phosphorylation was inhibited. CIBERSORT estimation of immune cell subsets suggested that activated NK cells, M1 macrophages, memory B cells, and follicular helper T cells were likely to be more prevalent in PCNSV samples" ([PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/))

### Cross-Vasculitis Genetic Susceptibility

| Vasculitis | Key Genetic Associations | Source |
|---|---|---|
| Behcet's disease | ERAP1, CCR1-CCR3, STAT4, KLRC4, GIMAP4, TNFAIP3 | [PMID: 25405820](https://pubmed.ncbi.nlm.nih.gov/25405820/) |
| Takayasu arteritis | HLA-B*52 (OR=3.29), FCGR2A/FCGR3A, IL12B | [PMID: 23830517](https://pubmed.ncbi.nlm.nih.gov/23830517/) |
| ANCA-AAV | SERPINA1, SEMA6A | [PMID: 25405820](https://pubmed.ncbi.nlm.nih.gov/25405820/) |
| Kawasaki disease | BLK, CD40 | [PMID: 25405820](https://pubmed.ncbi.nlm.nih.gov/25405820/) |
| Cross-vasculitis | HLA region (shared) | [PMID: 29374629](https://pubmed.ncbi.nlm.nih.gov/29374629/) |
| ABRA subtype | ApoE ε4/ε4 (70% of patients) | [PMID: 24636849](https://pubmed.ncbi.nlm.nih.gov/24636849/) |

### Epigenetic Information

No specific epigenetic studies have been performed on PACNS tissue. Dysregulated noncoding RNAs were identified in gene expression profiling ([PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/)). In giant cell arteritis, spatial profiling revealed ECM remodeling and T-cell activation pathways in glucocorticoid-refractory cases, providing a template for future PACNS studies ([PMID: 41109780](https://pubmed.ncbi.nlm.nih.gov/41109780/)).

---

## 5. Environmental Information

### Infectious Agents

Post-infectious CNS vasculitis represents a significant proportion of secondary cases ([PMID: 39663273](https://pubmed.ncbi.nlm.nih.gov/39663273/)):

| Pathogen | Mechanism | Key Evidence |
|---|---|---|
| **Varicella Zoster Virus (VZV)** | Transaxonal spread via trigeminal nerve to cerebral arteries | Anti-VZV IgG in 32% of PACNS CSF; can cause vasculopathy without rash ([PMID: 41782529](https://pubmed.ncbi.nlm.nih.gov/41782529/)) |
| **HIV** | Immune compromise enables opportunistic vasculopathy | VZV reactivation in 37% of HIV+ stroke patients ([PMID: 35133008](https://pubmed.ncbi.nlm.nih.gov/35133008/)) |
| **Cytomegalovirus (CMV)** | Monocyte-mediated CNS entry in immunodeficient hosts | Meningitis, choroiditis, encephalitis, vasculitis, necrosis ([PMID: 14722303](https://pubmed.ncbi.nlm.nih.gov/14722303/)) |
| **Mycobacterium tuberculosis** | Granulomatous vasculitis of basal arteries | Tuberculous meningitis with BBB disruption ([PMID: 38675201](https://pubmed.ncbi.nlm.nih.gov/38675201/)) |
| **Treponema pallidum** | Meningovascular syphilis | Endarteritis obliterans of cerebral vessels ([PMID: 37951699](https://pubmed.ncbi.nlm.nih.gov/37951699/)) |

### COVID-19 Association

SARS-CoV-2 can cause immune dysregulation leading to vasculitis, with "ischemic injury due to vasculitis" identified as a mechanism of organ dysfunction ([PMID: 39692912](https://pubmed.ncbi.nlm.nih.gov/39692912/)). Post-vaccination cerebral venous sinus thrombosis has also been reported.

### Environmental and Lifestyle Factors

No specific toxins, occupational exposures, or lifestyle factors (smoking, diet, exercise) have been definitively linked to PACNS development. Cardiovascular risk factors, particularly body weight, have been associated with PACNS vessel-size phenotype ([PMID: 41041677](https://pubmed.ncbi.nlm.nih.gov/41041677/)).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

The pathophysiology of PACNS involves multiple interconnected immune and inflammatory cascades:

```
Unknown trigger (? viral, ? autoimmune, ? amyloid-related)
         │
         ▼
┌─────────────────────────────┐
│  IMMUNE ACTIVATION          │
│  • Dendritic cell maturation│
│  • Antigen processing ↑     │
│  • IL-17 ↑ in CSF           │
│  • TBC1D3C/TBC1D3L ↑       │
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────────────────────────┐
│  CELLULAR INFILTRATION              │
│  • NK cells (activated) ↑           │
│  • M1 macrophages ↑                 │
│  • Memory B cells ↑                 │
│  • Follicular helper T cells ↑      │
│  • CD3/CD4/CD8/CD20 lymphocytes     │
└─────────┬───────────────────────────┘
          │
          ▼
┌─────────────────────────────────────┐
│  VASCULAR WALL DAMAGE               │
│  • Transmural inflammation           │
│  • Granulomatous reaction            │
│  • Fibrinoid necrosis                │
│  • Blood-brain barrier disruption    │
└─────────┬───────────────────────────┘
          │
          ▼
┌─────────────────────────────────────┐
│  TISSUE INJURY                       │
│  • Ischemic stroke (arterial)        │
│  • Hemorrhage (vessel rupture)       │
│  • Demyelination                     │
│  • Neuronal death (↑ NfL)            │
│  • Oxidative phosphorylation ↓       │
└─────────────────────────────────────┘
```

### Key Molecular Findings

1. **IL-17/Th17 axis**: "Recent advances in understanding pathophysiology have identified elevated interleukin-17 in cerebrospinal fluid, distinct gene expression profiles including upregulation of TBC1D3C and TBC1D3L genes, and immune cell profiling showing increased intrathecal NK-cell and B-cell frequencies" ([PMID: 41947889](https://pubmed.ncbi.nlm.nih.gov/41947889/)). This is significant because anti-IL-17 therapy (secukinumab) has shown efficacy in giant cell arteritis (70% sustained remission vs. 20% placebo at week 28) ([PMID: 38251601](https://pubmed.ncbi.nlm.nih.gov/38251601/)), suggesting potential translational relevance.

2. **Mitochondrial dysfunction**: Oxidative phosphorylation was inhibited in PACNS tissue compared to normal brain ([PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/)). GO terms: GO:0006119 (oxidative phosphorylation), GO:0005739 (mitochondrion).

3. **Dendritic cell and antigen processing activation**: Consistent with autoimmune pathogenesis. GO terms: GO:0019882 (antigen processing and presentation).

4. **Tryptophan-kynurenine pathway** (animal model): In MRL/lpr lupus-prone mice, cortical metabolomics revealed tryptophan metabolism diverted from serotonin toward the kynurenine pathway, with increased quinolinic acid/kynurenic acid ratio and IDO1 upregulation. "Inflammation was dominated by a Th1 cytokine program, with interferon-gamma emerging as a prominent component of the inflammatory profile. Composite cytokine scores correlated strongly with plasma NfL, establishing an immune-neuronal injury axis" ([PMID: 41869319](https://pubmed.ncbi.nlm.nih.gov/41869319/)). CHEBI: CHEBI:16828 (tryptophan), CHEBI:16675 (quinolinic acid).

### Immune System Involvement

| Immune Component | Role in PACNS | Cell Ontology | Evidence Source |
|---|---|---|---|
| Activated NK cells | Innate immune effectors | CL:0000623 | [PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/) |
| M1 macrophages | Pro-inflammatory tissue damage | CL:0000863 | [PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/) |
| Memory B cells | Antibody-mediated pathology | CL:0000787 | [PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/) |
| Follicular helper T cells | B-cell help, germinal center reactions | CL:0002038 | [PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/) |
| Th1 cells (IFN-gamma) | Dominant in lupus CNS model | CL:0000545 | [PMID: 41869319](https://pubmed.ncbi.nlm.nih.gov/41869319/) |
| IL-17/Th17 cells | Vascular wall inflammation | CL:0000899 | [PMID: 41947889](https://pubmed.ncbi.nlm.nih.gov/41947889/) |
| CD4+ T cells | Transmural infiltration | CL:0000624 | [PMID: 39732702](https://pubmed.ncbi.nlm.nih.gov/39732702/) |
| CD8+ T cells | Cytotoxic effectors | CL:0000625 | [PMID: 39732702](https://pubmed.ncbi.nlm.nih.gov/39732702/) |

### Tissue Damage Mechanisms

- **Ischemia**: Stenotic/occlusive vasculitis causing ischemic infarcts (most common mechanism)
- **Hemorrhage**: Vessel wall destruction causing parenchymal hemorrhage (55%), convexity subarachnoid hemorrhage (26%) ([PMID: 28330942](https://pubmed.ncbi.nlm.nih.gov/28330942/))
- **Fibrinoid necrosis**: Vessel wall necrosis with fibrin deposition (necrotizing subtype)
- **Granulomatous inflammation**: Epithelioid cell/giant cell reaction (granulomatous subtype)
- **Blood-brain barrier disruption**: Enabling immune cell infiltration and edema
- **Neuroaxonal damage**: Reflected by elevated NfL ([PMID: 40643487](https://pubmed.ncbi.nlm.nih.gov/40643487/))

### Molecular Profiling

**Transcriptomics** ([PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/)): RNA-seq of brain tissue revealed subtype-specific immune cell profiles via CIBERSORT: granulomatous/ABRA enriched for naive CD4 T cells and monocytes; lymphocytic for plasma cells and gamma-delta T cells.

**Biomarker candidates**: NfL elevated in active PACNS (serum and CSF) and may precede radiological abnormalities ([PMID: 40643487](https://pubmed.ncbi.nlm.nih.gov/40643487/); [PMID: 31211179](https://pubmed.ncbi.nlm.nih.gov/31211179/)). Circulating endothelial cells proposed as differential diagnostic biomarker ([PMID: 32296382](https://pubmed.ncbi.nlm.nih.gov/32296382/)).

### GO Terms for Key Biological Processes

| Process | GO ID |
|---|---|
| Inflammatory response | GO:0006954 |
| Antigen processing and presentation | GO:0019882 |
| Oxidative phosphorylation | GO:0006119 |
| T cell activation | GO:0042110 |
| B cell activation | GO:0042113 |
| Natural killer cell activation | GO:0030101 |
| Interleukin-17 production | GO:0032620 |
| Leukocyte migration | GO:0050900 |
| Endothelial cell activation | GO:0042118 |

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary**: Brain (UBERON:0000955) — principal target
- **Primary**: Spinal cord (UBERON:0002240) — rare but severe subset; 29% mortality ([PMID: 39979764](https://pubmed.ncbi.nlm.nih.gov/39979764/))
- **Leptomeninges** (UBERON:0000400): Enhancement in 42% of PACNS ([PMID: 28330942](https://pubmed.ncbi.nlm.nih.gov/28330942/))
- **Body systems**: Nervous system (primarily), cardiovascular system (vascular component)
- By definition, PACNS does NOT involve other organ systems

### Tissue and Cell Level

- **Blood vessel walls** (UBERON:0001981): Arterial wall — transmural inflammation of intima, media, adventitia
- **Cell populations**:
  - Vascular endothelial cells (CL:0000071) — reactive endothelium strongly associated with sv-cPACNS (OR 8.93, p=0.001) ([PMID: 39732702](https://pubmed.ncbi.nlm.nih.gov/39732702/))
  - Vascular smooth muscle cells (CL:0000359) — vessel wall remodeling
  - Neurons (CL:0000540) — secondary ischemic/hemorrhagic damage
  - Oligodendrocytes (CL:0000128) — demyelination in some cases

### Localization

- **Cerebral arteries**: Most commonly multiterritorial bilateral distal involvement (42% in COVAC cohort)
- **Internal carotid artery system**: 94% of cases in VZV-associated series
- **Lateralization**: Usually bilateral; unilateral PACNS (U-PACNS) rare (~49 cases) — "often misdiagnosed as glioma, demyelination, or chronic encephalitis" ([PMID: 40835417](https://pubmed.ncbi.nlm.nih.gov/40835417/))

---

## 8. Temporal Development

### Onset

- **Adult PACNS**: Median age 46–48 years (range: adolescence to elderly)
- **Pediatric cPACNS**: Mean onset 7.89 years (SD 4.17) ([PMID: 30762375](https://pubmed.ncbi.nlm.nih.gov/30762375/))
- **ABRA**: Typically elderly (mean age 73 years) ([PMID: 38900992](https://pubmed.ncbi.nlm.nih.gov/38900992/))
- **Onset pattern**: Usually subacute (weeks to months); median diagnostic delay 23 months ([PMID: 35931755](https://pubmed.ncbi.nlm.nih.gov/35931755/))

### Progression

- **Disease course**: Relapsing-remitting in ~50%; monophasic in some; rapidly progressive in a minority
- **Relapse rate**: 35–50% depending on cohort and treatment
- **Course by subtype**: Lymphocytic monophasic (65%); ABRA monophasic (75%); granulomatous relapsing-remitting (63%) ([PMID: 40494617](https://pubmed.ncbi.nlm.nih.gov/40494617/))

### Pediatric Course

Childhood cPACNS classified by vessel size and course ([PMID: 23622312](https://pubmed.ncbi.nlm.nih.gov/23622312/)):
- **Large-vessel non-progressive (APNP)**: n=49; monophasic
- **Large-vessel progressive (APP)**: n=10; chronic relapsing
- **Small-vessel (AN)**: n=21; requires biopsy; worst cognitive outcomes

### Critical Periods

Diagnostic delay is a modifiable prognostic factor (HR 1.01 per month) ([PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/)). "Early recognition and diagnosis of inflammatory brain diseases is critical, as the reversibility of the neurological deficits is closely related to early initiation of treatment" ([PMID: 25877722](https://pubmed.ncbi.nlm.nih.gov/25877722/)).

---

## 9. Inheritance and Population

### Epidemiology

| Metric | Value | Source |
|---|---|---|
| **Prevalence (PACNS)** | ~2.4 per million person-years (North America) | [PMID: 41947889](https://pubmed.ncbi.nlm.nih.gov/41947889/) |
| **Sex ratio** | ~45–55% female; slight male predominance in most cohorts | [PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/) |
| **Median age at onset** | 46–48 years (adults); 7.89 years (pediatric) | Multiple sources |
| **Diagnostic delay** | Median 23 months | [PMID: 35931755](https://pubmed.ncbi.nlm.nih.gov/35931755/) |

### Inheritance

PACNS is **not a Mendelian disorder** — multifactorial/polygenic susceptibility. Monogenic mimics follow specific patterns:
- **DADA2**: Autosomal recessive (ADA2, chromosome 22q11.1)
- **CTLA4 haploinsufficiency**: Autosomal dominant
- **IPEX/FOXP3**: X-linked recessive
- **LRBA deficiency**: Autosomal recessive

### Population Demographics

- No specific ethnic predilection for PACNS; most data from North American and European populations
- For Behcet's disease (secondary CNS vasculitis): Silk Road distribution
- For Takayasu arteritis: More common in East Asian populations
- No known geographic clustering for PACNS

---

## 10. Diagnostics

### Clinical Criteria

**Calabrese and Mallek Criteria (1988)** — the standard diagnostic framework:
1. Acquired neurological deficit unexplained by other diagnoses
2. Angiographic or histopathologic evidence of vasculitis within the CNS
3. No evidence of systemic vasculitis or any condition that could mimic angiographic or pathological features

### Laboratory Tests

- **CSF analysis**: Abnormalities in 65–75% (elevated protein, lymphocytic pleocytosis); normal CSF + normal MRI has high negative predictive value
- **NfL (Neurofilament light chain)**: "NfL holds potential as a biomarker for PACNS, in particular in younger patients" ([PMID: 40643487](https://pubmed.ncbi.nlm.nih.gov/40643487/)). "A marked increase in NFL levels preceding the onset of neuro-axonal damage and arterial-vessel abnormalities" ([PMID: 31211179](https://pubmed.ncbi.nlm.nih.gov/31211179/))
- **ESR/CRP**: Usually normal in PACNS (helps distinguish from systemic vasculitis)
- **ANCA, ANA, anti-dsDNA**: Should be negative in PACNS; if positive, consider secondary causes

### Imaging Studies

| Modality | Findings | Diagnostic Value |
|---|---|---|
| **Brain MRI** | Multiterritorial infarcts, WM hyperintensities, hemorrhage (55%), mass lesions | Sensitivity 97–98%, low specificity |
| **Vessel Wall MRI (VW-MRI)** | Concentric wall enhancement, wall thickening | Improves accuracy from 36.1% to 88.8% per-lesion ([PMID: 29030476](https://pubmed.ncbi.nlm.nih.gov/29030476/)) |
| **HR-VWI** | LMVV: 90% strong/concentric enhancement vs. 7.1% in SVV (p<0.001) | Distinguishes vessel-size subtypes ([PMID: 37073640](https://pubmed.ncbi.nlm.nih.gov/37073640/)) |
| **DSA** | "String of beads" pattern; alternating stenoses/dilatations | Gold standard for large/medium vessel disease |
| **SWI sequences** | Cerebral microbleeds, hemorrhage | Sensitive marker |

> "IVWI can significantly improve the differentiation of nonocclusive intracranial vasculopathies when combined with traditional luminal imaging modalities" ([PMID: 29030476](https://pubmed.ncbi.nlm.nih.gov/29030476/))

### Brain Biopsy

Brain and leptomeningeal biopsy remains the **gold standard** for small-vessel PACNS:
- Biopsy diagnosed SVV in 78.3% vs. 30.8% for LMVV (p=0.022) ([PMID: 37073640](https://pubmed.ncbi.nlm.nih.gov/37073640/))
- Biopsy accuracy: 100% for SVV, 57.1% for LMVV (p=0.015)
- **Pediatric distinction**: No granulomas, necrosis, or fibrin deposits found in any pediatric sv-PACNS case. "Reactive endothelium was strongly associated with sv-cPACNS, with an OR of 8.93 (p = 0.001)" ([PMID: 39732702](https://pubmed.ncbi.nlm.nih.gov/39732702/))

### Screening Algorithm

A published screening algorithm proposes ([PMID: 32776287](https://pubmed.ncbi.nlm.nih.gov/32776287/)):
- **Major clinical features**: Headache, stroke, cognitive impairment, focal neurological deficits
- **Minor clinical features**: Seizures, altered consciousness, psychiatric disorders
- **Major radiological features**: Multiple parenchymal lesions, parenchymal/meningeal contrast enhancement, MRA vessel abnormalities, vessel wall enhancement

### MRI Hemorrhagic Spectrum

French COVAC cohort (n=60) ([PMID: 28330942](https://pubmed.ncbi.nlm.nih.gov/28330942/)): "Hemorrhagic infarctions and parenchymal hemorrhages were also frequently found in the cohort (55%). Acute convexity subarachnoid hemorrhage was found in 26% of patients and 42% demonstrated pre-eminent leptomeningeal enhancement, which is found to be significantly more prevalent in biopsy-proven patients (60% versus 28%)"

### CAA-RI vs BP-PACNS Differentiation

Comparison of 104 CAA-RI vs. 52 BP-PACNS patients ([PMID: 38900992](https://pubmed.ncbi.nlm.nih.gov/38900992/)): CAA-RI patients older (73 vs. 45 years), more hemorrhagic signs, past ICH, ≥21 centrum semiovale perivascular spaces. BP-PACNS had more leptomeningeal enhancement and ischemic lesions.

### Differential Diagnosis

| Condition | Distinguishing Features |
|---|---|
| **RCVS** | Thunderclap headache, no focal deficit, convexal SAH, normal parenchyma, resolves in 3 months ([PMID: 22467936](https://pubmed.ncbi.nlm.nih.gov/22467936/)) |
| **CAA-RI** | Older age (73 vs. 45 years), hemorrhagic signs, ≥21 perivascular spaces |
| **DADA2** | Childhood onset, livedo reticularis, systemic inflammation, ADA2 mutations |
| **Tumefactive PACNS** | Mass-like lesion mimicking glioblastoma; 34 cases, mean age 35.9 years ([PMID: 41112399](https://pubmed.ncbi.nlm.nih.gov/41112399/)) |
| **Neuro-Behcet** | HLA-B51+, oral/genital ulcers, CSF IL-6 elevation |
| **NPSLE** | ANA/anti-dsDNA positive, multi-organ involvement |
| **SLIPPERS** | Overlapping features; some cases may be PACNS variants ([PMID: 41718297](https://pubmed.ncbi.nlm.nih.gov/41718297/)) |
| **Tregopathies** | Pediatric multi-organ autoimmunity with CNS vasculitis ([PMID: 41142805](https://pubmed.ncbi.nlm.nih.gov/41142805/)) |

> "Thunderclap headaches, the absence of a focal neurological deficit, a convexal subarachnoid hemorrhage and/or normal brain parenchyma on magnetic resonance imaging, and 'string of beads' appearance on conventional angiography had high diagnostic value" ([PMID: 22467936](https://pubmed.ncbi.nlm.nih.gov/22467936/))

### Genetic Testing

Not routinely recommended for adult PACNS. Indicated in:
- **ADA2 sequencing**: For childhood-onset PAN-like vasculitis with strokes
- **LRBA, CTLA4, FOXP3 panels**: For patients with multi-organ autoimmunity + CNS vasculitis
- **ApoE genotyping**: For suspected ABRA subtype
- **WES**: For VZV CNS infections to identify inborn errors of immunity ([PMID: 40848267](https://pubmed.ncbi.nlm.nih.gov/40848267/))

---

## 11. Outcome/Prognosis

### Survival and Mortality

| Metric | Value | Cohort | Source |
|---|---|---|---|
| Overall mortality | 18% | n=163, German multicenter | [PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/) |
| Poor outcome (mRS 3–6) | 52% | n=163, German multicenter | [PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/) |
| Good functional outcome | 65.2% | n=82, Indian cohort | [PMID: 35931755](https://pubmed.ncbi.nlm.nih.gov/35931755/) |
| Remission achieved | 61.3% | n=80, real-world | [PMID: 41995257](https://pubmed.ncbi.nlm.nih.gov/41995257/) |
| G-PACNS mortality | 25% | Biopsy-proven | [PMID: 40494617](https://pubmed.ncbi.nlm.nih.gov/40494617/) |
| Spinal cord PACNS mortality | 29% | n=38, systematic review | [PMID: 39979764](https://pubmed.ncbi.nlm.nih.gov/39979764/) |

> "Of 163 patients with PACNS (median [interquartile range (IQR)] age 48 [39-59.5] years; 73 [45%] women), 29 (18%) died, 84 (52%) had a poor outcome (modified Rankin scale [mRS] 3-6 at last follow-up), and 82 (50%) patients relapsed" ([PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/))

### Prognostic Factors

**Poorer survival** associated with ([PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/)):
- Older age (HR 1.96 per 10-year increase)
- Diagnostic delay (HR 1.01 per month)
- Necrotizing subtype (HR 10.2, 95% CI 2.18–48.2)

### Subtype-Specific Outcomes

| Subtype | Induction Response | Median mRS | Mortality |
|---|---|---|---|
| Lymphocytic | Good | 1–2 | Low |
| ABRA | Good | Variable | Moderate |
| Granulomatous | **29%** | **4 (worst)** | **25%** |
| Necrotizing | Variable | Variable | Highest (HR 10.2) |

> "Worst outcome (median mRS 4) and highest mortality (25%) were seen in G-PACNS. Good induction treatment response was achieved in 77% of all BP-PACNS patients but was low in those with G-PACNS (29%)" ([PMID: 40494617](https://pubmed.ncbi.nlm.nih.gov/40494617/))

---

## 12. Treatment

### Pharmacotherapy

**No randomized controlled trials exist for PACNS treatment.** All recommendations are based on observational studies and expert consensus.

#### Induction Therapy

| Agent | Class | Evidence | MAXO Term |
|---|---|---|---|
| **Glucocorticoids** | Corticosteroid | Standard of care; pulse then taper | MAXO:0000609 |
| **Cyclophosphamide** | Alkylating agent | HR 0.44 (95% CI 0.22–0.86) for relapse reduction ([PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/)) | MAXO:0001298 |
| **Rituximab** (refractory) | Anti-CD20 mAb | Combined CYC+RTX effective in rapidly progressive PACNS ([PMID: 39954605](https://pubmed.ncbi.nlm.nih.gov/39954605/)) | MAXO:0001380 |

> "Patients treated with cyclophosphamide alone or in combination with steroids had a lower incidence of relapse than untreated patients (HR, 0.44 [95% CI, 0.22-0.86]; HR, 0.47 [95% CI, 0.24-0.92])" ([PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/))

#### Maintenance Therapy

| Agent | Evidence | MAXO Term |
|---|---|---|
| **Mycophenolate mofetil** | No relapses over mean 29 months in pediatric cases ([PMID: 28034820](https://pubmed.ncbi.nlm.nih.gov/28034820/)) | MAXO:0001077 |
| **Azathioprine** | Commonly used maintenance | MAXO:0001069 |
| **Methotrexate** | Long-term immunosuppression | MAXO:0001084 |
| **Rituximab** | Relapsed/refractory cases | MAXO:0001380 |

> "In all children, no relapse of cerebral vasculitis occurred during the whole follow-up period and all of them improved while in MMF treatment" ([PMID: 28034820](https://pubmed.ncbi.nlm.nih.gov/28034820/))

#### Treatment Response

- Overall remission: 61.3%; favorable functional outcomes: 87.5% ([PMID: 41995257](https://pubmed.ncbi.nlm.nih.gov/41995257/))
- Good induction response: 77% overall, but only 29% in granulomatous subtype ([PMID: 40494617](https://pubmed.ncbi.nlm.nih.gov/40494617/))
- Relapse rate: 35% overall

#### Treatment Complications

- Glucocorticoid use before ICH may worsen bleeding severity in AAV patients (p<0.001) ([PMID: 40643697](https://pubmed.ncbi.nlm.nih.gov/40643697/))
- Standard immunosuppression risks: infections, bone marrow suppression, infertility (cyclophosphamide), PML (rituximab, rare)

### Treatment Algorithm

```
Suspected PACNS
      │
      ▼
Glucocorticoid pulse (methylprednisolone 1g/day × 3-5 days)
      │
      ▼
Induction: GC + Cyclophosphamide (3-6 months)
      │
      ├── Response → Maintenance: MMF or AZA or MTX (2-3 years)
      │
      ├── Refractory → Rituximab ± CYC combination
      │
      └── Rapidly progressive → CYC + RTX + GC (triple therapy)
```

### Advanced and Experimental Therapeutics

- **Anti-IL-17 (secukinumab)**: 70% sustained remission in GCA vs. 20% placebo ([PMID: 38251601](https://pubmed.ncbi.nlm.nih.gov/38251601/)) — rational candidate for PACNS given elevated CSF IL-17
- **Anti-TNF**: First-line for DADA2; efficacious in Neuro-Behcet
- **Anti-IL-6 (tocilizumab)**: Established in GCA; potential in CNS vasculitis
- **Abatacept/mTOR inhibitors**: Required for Tregopathies causing CNS vasculitis ([PMID: 41142805](https://pubmed.ncbi.nlm.nih.gov/41142805/))
- **Mepolizumab (anti-IL-5)**: For EGPA-related CNS vasculitis ([PMID: 38109745](https://pubmed.ncbi.nlm.nih.gov/38109745/))
- **Anifrolumab (anti-IFNAR)**: Glucocorticoid-sparing in NPSLE ([PMID: 41211782](https://pubmed.ncbi.nlm.nih.gov/41211782/))

### Pharmacogenomics

- **TPMT/NUDT15 genotyping**: For azathioprine dosing (CPIC guidelines)
- **CYP2B6**: Affects cyclophosphamide metabolism
- **ApoE genotype**: Influences ABRA treatment response and prognosis

---

## 13. Prevention

### Primary Prevention

No primary prevention strategies exist for PACNS. For secondary CNS vasculitis:
- **VZV vaccination**: May reduce VZV vasculopathy risk
- **HIV treatment**: Antiretroviral therapy reduces opportunistic CNS vasculitis
- **Treatment of underlying systemic vasculitis**: Prevents secondary CNS involvement

### Secondary Prevention (Early Detection)

- High clinical suspicion in young stroke patients with multiterritorial infarcts
- VW-MRI as screening tool when clinical/radiological "major features" are present
- NfL monitoring: Can precede radiological abnormalities ([PMID: 31211179](https://pubmed.ncbi.nlm.nih.gov/31211179/))
- Genetic screening for ADA2 mutations in childhood-onset vasculitis/stroke

### Tertiary Prevention

- Long-term maintenance immunosuppression to prevent relapse
- Regular neuroimaging surveillance
- NfL monitoring for early relapse detection
- Rehabilitation: physical, occupational, cognitive, and speech therapy
- Psychological support for anxiety/depression (affecting >70% long-term)

---

## 14. Other Species / Natural Disease

### Naturally Occurring CNS Vasculitis in Animals

| Species | Condition | Mechanism | Source |
|---|---|---|---|
| **Dog** (*Canis lupus familiaris*, NCBI Taxon: 9615) | Encephalitozoonosis | *Encephalitozoon cuniculi* parasitizes endothelial cells, causing granulomatous vasculitis | [PMID: 750958](https://pubmed.ncbi.nlm.nih.gov/750958/) |
| **Dog** | Trypanosomiasis | *Trypanosoma brucei* causes necrotizing vasculitis with CNS involvement | [PMID: 6110340](https://pubmed.ncbi.nlm.nih.gov/6110340/) |

> "Vasculitis is demonstrated as the underlying lesion of canine encephalitozoonosis affecting the brain and is suggested to be the basic factor in the pathogenesis of this disease" ([PMID: 750958](https://pubmed.ncbi.nlm.nih.gov/750958/))

No well-documented natural disease equivalent to human primary/idiopathic PACNS exists in other species.

---

## 15. Model Organisms

### Available Models

| Model | Type | Key Findings | Limitations |
|---|---|---|---|
| **MRL/lpr mouse** | Spontaneous lupus | IFN-gamma-dominated Th1; NfL-cytokine correlation; kynurenine pathway diversion ([PMID: 41869319](https://pubmed.ncbi.nlm.nih.gov/41869319/)) | Systemic disease, not isolated CNS |
| **Nude/SCID + CMV** | Induced viral | CNS vasculitis, meningitis, necrosis; requires immunodeficiency ([PMID: 14722303](https://pubmed.ncbi.nlm.nih.gov/14722303/)) | Not autoimmune |
| **ACE inhibitor MRL/lpr** | Pharmacological | Centrally-acting ACE inhibitors suppress IFN responses ([PMID: 33042154](https://pubmed.ncbi.nlm.nih.gov/33042154/)) | Limited to lupus model |

### Key Model Findings

The MRL/lpr mouse reveals critical mechanistic insights:
1. **Immune-neuronal injury axis**: Composite cytokine scores correlated with plasma NfL ([PMID: 41869319](https://pubmed.ncbi.nlm.nih.gov/41869319/))
2. **Region-specific cytokine signatures**: Hippocampal IL-10 loss, frontal cortex IFN-gamma dominance
3. **Metabolic remodeling**: Tryptophan diverted to neurotoxic kynurenine pathway
4. **Important negative result**: Anti-IFNAR treatment "did NOT improve neuropsychiatric disease despite decreasing IFN-stimulated genes" — "no significant differences were seen between the anti-IFNAR- and control-treated mice when assessing for depression-like behavior or cognitive dysfunction" ([PMID: 31474191](https://pubmed.ncbi.nlm.nih.gov/31474191/))

### Model Limitations

- No spontaneous model exactly recapitulates human PACNS
- MRL/lpr models systemic lupus with secondary CNS involvement
- Viral models require immunodeficiency
- Species differences in cerebrovascular anatomy and immune surveillance

---

## Mechanistic Model: Integrated Pathophysiology

Synthesizing all evidence, the following mechanistic model emerges for PACNS:

```
UPSTREAM TRIGGERS
├── Viral reactivation (VZV, CMV) ──────────────┐
├── Autoimmune predisposition (HLA, ERAP1) ─────┤
├── Amyloid deposition (ApoE ε4 → ABRA) ────────┤
└── Monogenic defects (ADA2, LRBA, CTLA4) ──────┘
                                                  │
                                                  ▼
              IMMUNE ACTIVATION IN CNS VESSELS
              ├── IL-17/Th17 activation (CSF IL-17 ↑)
              ├── Dendritic cell maturation
              ├── NK cell activation
              ├── M1 macrophage polarization
              ├── Memory B cell/plasma cell expansion
              └── TBC1D3C/TBC1D3L upregulation
                                                  │
                                                  ▼
              VASCULAR WALL INFLAMMATION
              ├── Lymphocytic infiltration (65%)
              ├── Granulomatous reaction (14%)
              ├── Fibrinoid necrosis (5%)
              └── ABRA (amyloid + inflammation) (16%)
                                                  │
                                                  ▼
              DOWNSTREAM CONSEQUENCES
              ├── Ischemic stroke (stenosis/occlusion)
              ├── Hemorrhage (55%) (vessel destruction)
              ├── Mitochondrial dysfunction (OXPHOS ↓)
              ├── BBB disruption → edema
              ├── Kynurenine pathway diversion (quinolinic acid ↑)
              └── Neuroaxonal injury (NfL ↑)
                                                  │
                                                  ▼
              CLINICAL MANIFESTATIONS
              ├── Focal deficits (63%)
              ├── Headache (51%)
              ├── Cognitive impairment (41%)
              ├── Seizures (16-36%)
              └── Long-term: anxiety/depression (70.4%)
```

**Translational implications**: The convergence of elevated CSF IL-17 in PACNS ([PMID: 41947889](https://pubmed.ncbi.nlm.nih.gov/41947889/)) with the success of anti-IL-17A therapy (secukinumab) in giant cell arteritis (70% sustained remission, [PMID: 38251601](https://pubmed.ncbi.nlm.nih.gov/38251601/)) identifies IL-17 inhibition as the most rational translational therapeutic candidate for PACNS. The negative anti-IFNAR result in MRL/lpr mice ([PMID: 31474191](https://pubmed.ncbi.nlm.nih.gov/31474191/)) cautions against targeting type I interferons alone.

---

## Evidence Base

This report synthesizes evidence from 113 papers, including:

| Paper Type | Key Examples | Count |
|---|---|---|
| Systematic reviews/meta-analyses | [PMID: 34663675](https://pubmed.ncbi.nlm.nih.gov/34663675/) (n=911 PACNS) | 8+ |
| Multicenter cohort studies | [PMID: 40546217](https://pubmed.ncbi.nlm.nih.gov/40546217/) (n=163) | 5+ |
| Single-center cohorts | [PMID: 40494617](https://pubmed.ncbi.nlm.nih.gov/40494617/) (n=57 biopsy-proven) | 10+ |
| Gene expression/molecular | [PMID: 36264136](https://pubmed.ncbi.nlm.nih.gov/36264136/) | 3+ |
| Genetics studies | [PMID: 29374629](https://pubmed.ncbi.nlm.nih.gov/29374629/), [PMID: 25405820](https://pubmed.ncbi.nlm.nih.gov/25405820/) | 5+ |
| Animal model studies | [PMID: 41869319](https://pubmed.ncbi.nlm.nih.gov/41869319/), [PMID: 31474191](https://pubmed.ncbi.nlm.nih.gov/31474191/) | 5+ |
| Comprehensive reviews | [PMID: 41947889](https://pubmed.ncbi.nlm.nih.gov/41947889/) | 15+ |
| Case reports/series | [PMID: 29963054](https://pubmed.ncbi.nlm.nih.gov/29963054/) | 20+ |

---

## Limitations and Knowledge Gaps

1. **No GWAS for PACNS**: Disease too rare; genetic susceptibility inferred from cross-vasculitis analyses
2. **No randomized controlled trials**: All treatment evidence observational; multicenter RCTs urgently needed
3. **Diagnostic uncertainty**: Up to 40–50% initially misdiagnosed; biopsy sensitivity only 57% for large-vessel disease
4. **Limited molecular profiling**: Only one gene expression study; no proteomics, metabolomics, or single-cell studies in human PACNS tissue
5. **Animal model limitations**: No model recapitulates primary PACNS; available models reflect secondary CNS vasculitis
6. **Pediatric data scarcity**: Smaller cohorts; distinct pathology from adults but treatment extrapolated
7. **Biomarker validation**: NfL promising but not validated in large prospective PACNS cohorts
8. **Long-term outcome data**: Limited follow-up beyond 5 years; late complications poorly characterized
9. **Subtype classification heterogeneity**: Different classification systems across studies limit comparison
10. **Quality of life data**: Limited to single study with small sample (n=27) and 34.6% response rate

---

## Proposed Follow-up Experiments/Actions

### Immediate Priorities

1. **Multicenter PACNS registry**: Establish a prospective international registry with standardized phenotyping, biobanking, and outcome measures to enable future GWAS and clinical trials
2. **NfL validation study**: Prospective longitudinal cohort measuring serum/CSF NfL at diagnosis, during treatment, and at relapse to establish clinical utility thresholds
3. **Single-cell RNA-seq of brain biopsies**: Profile cell-type-specific transcriptomic signatures in PACNS subtypes to identify therapeutic targets

### Medium-term Goals

4. **IL-17 inhibitor pilot trial**: Based on elevated CSF IL-17 in PACNS and secukinumab efficacy in GCA (70% sustained remission), a pilot study in refractory PACNS is warranted
5. **PACNS genetic study**: Whole-exome sequencing of well-phenotyped PACNS patients vs. controls to identify disease-specific susceptibility variants
6. **CSF proteomics/metabolomics**: Unbiased profiling across subtypes for diagnostic biomarkers and therapeutic targets
7. **VZV investigation**: Systematic CSF VZV antibody testing in all PACNS patients to determine proportion with occult viral triggers

### Long-term Vision

8. **Precision medicine framework**: Develop subtype-specific treatment algorithms based on histopathology, gene expression, and biomarker profiles
9. **Machine learning diagnostic tool**: Integrate clinical, imaging, laboratory, and molecular data for automated PACNS probability scoring
10. **Kynurenine pathway modulation**: Evaluate IDO1 inhibitors as adjunctive neuroprotective therapy based on animal model evidence

---

## Ontology Term Summary

| Category | Terms |
|---|---|
| **MONDO** | MONDO:0007141 (cerebral vasculitis) |
| **HPO** | HP:0002315 (Headache), HP:0001269 (Hemiparesis), HP:0100543 (Cognitive impairment), HP:0001250 (Seizures), HP:0000504 (Abnormality of vision), HP:0002381 (Aphasia), HP:0001251 (Ataxia), HP:0002922 (Elevated CSF protein), HP:0012229 (CSF pleocytosis) |
| **GO (BP)** | GO:0006954 (inflammatory response), GO:0019882 (antigen processing and presentation), GO:0006119 (oxidative phosphorylation), GO:0042110 (T cell activation), GO:0042113 (B cell activation), GO:0030101 (NK cell activation), GO:0032620 (IL-17 production), GO:0050900 (leukocyte migration), GO:0042118 (endothelial cell activation) |
| **GO (CC)** | GO:0005739 (mitochondrion), GO:0005768 (endosome), GO:0005840 (ribosome) |
| **CL** | CL:0000623 (NK cell), CL:0000863 (M1 macrophage), CL:0000787 (memory B cell), CL:0002038 (T follicular helper cell), CL:0000071 (endothelial cell), CL:0000540 (neuron), CL:0000624 (CD4+ T cell), CL:0000625 (CD8+ T cell) |
| **UBERON** | UBERON:0000955 (brain), UBERON:0002240 (spinal cord), UBERON:0000400 (leptomeninx), UBERON:0001981 (blood vessel) |
| **CHEBI** | CHEBI:16828 (tryptophan), CHEBI:16675 (quinolinic acid), CHEBI:28790 (serotonin), CHEBI:57959 (kynurenine) |
| **MAXO** | MAXO:0000609 (corticosteroid therapy), MAXO:0001298 (cyclophosphamide therapy), MAXO:0001380 (rituximab therapy), MAXO:0001077 (MMF therapy), MAXO:0001069 (azathioprine therapy), MAXO:0001084 (methotrexate therapy), MAXO:0000127 (brain biopsy) |

---

*Report generated through systematic PubMed literature review covering 113 publications across 5 research iterations. 13 confirmed findings recorded with statistical evidence and 40+ unique PMID citations with verbatim abstract quotes. Ontology annotations include HPO, GO, CL, UBERON, CHEBI, MAXO, and MONDO terms. Information current as of May 2026.*
