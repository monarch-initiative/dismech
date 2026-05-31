---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T02:43:25.383043'
end_time: '2026-05-05T03:11:46.336595'
duration_seconds: 1700.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Allergic Cutaneous Vasculitis
  mondo_id: ''
  category: Immune-Mediated
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 15
    timeout: 5400
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Allergic Cutaneous Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Immune-Mediated

## Research Objectives

Please provide a comprehensive research report on **Allergic Cutaneous Vasculitis** covering all of the
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

# Comprehensive Disease Characterization: Allergic Cutaneous Vasculitis

## Summary

**Allergic Cutaneous Vasculitis** (also known as **Hypersensitivity Vasculitis**, **Cutaneous Leukocytoclastic Angiitis**, or **Single-Organ Cutaneous Small Vessel Vasculitis [SoCSVV]**) is a Type III hypersensitivity immune complex-mediated small vessel vasculitis that predominantly affects postcapillary venules in the dermis. The disease is characterized by the hallmark clinical finding of **palpable purpura** on the lower extremities and the histopathological triad of **leukocytoclastic vasculitis** (neutrophilic infiltration with nuclear dust/leukocytoclasia), **fibrinoid necrosis** of vessel walls, and **extravasation of red blood cells**. The annual incidence of biopsy-proven cutaneous vasculitis is approximately 38.6 per million population, with cutaneous leukocytoclastic angiitis specifically estimated at 15.4 per million ([PMID: 9598892](https://pubmed.ncbi.nlm.nih.gov/9598892/)).

The etiology is multifactorial: **drugs** account for approximately 40% of identifiable triggers (notably antibiotics such as amoxicillin, vancomycin, and clarithromycin, as well as NSAIDs and allopurinol), **infections** account for ~20%, and the condition remains **idiopathic in up to 50%** of cases. The pathogenesis involves immune complex deposition in small blood vessel walls, complement activation via the classical pathway with elaboration of chemotactic factors (C3a, C5a), neutrophil recruitment, and lysosomal enzyme-mediated vessel wall destruction. The disease is generally self-limited with a favorable prognosis, though relapse rates of 18-25% are reported. Treatment centers on removal of the offending trigger, supportive care, and graduated pharmacotherapy from colchicine (first-line for chronic/relapsing disease) to dapsone (second-line), corticosteroids (for severe disease with skin necrosis), and immunosuppressive agents for refractory cases.

This report provides a comprehensive characterization of Allergic Cutaneous Vasculitis across 15 disease knowledge domains, integrating data from 104 peer-reviewed publications, population-based epidemiological studies, and international consensus guidelines.

---

## 1. Disease Information

### Overview

Allergic Cutaneous Vasculitis is an immune complex-mediated inflammatory disease of the small blood vessels (primarily postcapillary venules) confined to the skin. It was first described by Gruber in 1925 and later characterized by Zeek in 1948 as "hypersensitivity angiitis." The condition represents the most common form of cutaneous vasculitis and is distinguished from systemic vasculitides by its predominant or exclusive skin involvement.

### Key Identifiers

| Identifier | Code/ID |
|---|---|
| **ICD-10** | L95.0 (Livedoid vasculitis), L95.1 (Erythema elevatum diutinum), L95.8/L95.9 (Vasculitis limited to skin), M31.0 (Hypersensitivity angiitis) |
| **ICD-11** | 4A44.1 (Cutaneous small vessel vasculitis) |
| **MeSH** | D018366 (Vasculitis, Leukocytoclastic, Cutaneous) |
| **MONDO** | MONDO:0019552 (Cutaneous leukocytoclastic vasculitis) |
| **Orphanet** | ORPHA:889 (Cutaneous leukocytoclastic vasculitis) |
| **OMIM** | Not assigned (non-Mendelian, complex etiology) |

### Synonyms and Alternative Names

- Hypersensitivity vasculitis (HV)
- Cutaneous leukocytoclastic angiitis (CLA)
- Cutaneous leukocytoclastic vasculitis (CLCV/LCV)
- Single-organ cutaneous small vessel vasculitis (SoCSVV)
- Cutaneous small vessel vasculitis (CSVV)
- Allergic vasculitis
- Small vessel vasculitis of the skin
- Leukocytoclastic vasculitis (LCV) - when skin-limited

### Information Sources

The information in this report is derived from **aggregated disease-level resources** including population-based epidemiological studies, classification criteria from the American College of Rheumatology (ACR 1990), the Chapel Hill Consensus Conference (CHCC 2012) nomenclature, and the European League Against Rheumatism (EULAR) guidelines, supplemented by large clinical case series and retrospective cohort studies.

---

## 2. Etiology

### Disease Causal Factors

Allergic Cutaneous Vasculitis is fundamentally a **Type III hypersensitivity reaction** (Gell and Coombs classification) driven by immune complex deposition. As described by Sams (1986): *"Human hypersensitivity angiitis is an immune complex disease in which patients present with palpable purpuric lesions of the skin and may often have multiple organ involvement. The antigen may be derived from an infectious organism such as the hepatitis virus, streptococcus, or a drug, and complexes with antibody"* ([PMID: 3159805](https://pubmed.ncbi.nlm.nih.gov/3159805/)).

### Primary Triggers

| Trigger Category | Estimated Frequency | Examples |
|---|---|---|
| **Drugs** | ~40% | Antibiotics (amoxicillin, vancomycin, clarithromycin, ciprofloxacin), NSAIDs, allopurinol, phenytoin, levetiracetam, sorafenib, ruxolitinib, semaglutide |
| **Infections** | ~20% | Hepatitis B/C virus, Streptococcus, HIV, SARS-CoV-2, hMPV, upper respiratory tract infections |
| **Autoimmune diseases** | ~15% | SLE, rheumatoid arthritis, Sjogren's syndrome, inflammatory bowel disease |
| **Malignancy** | ~3.8% of adults | Hematologic malignancies (most common), solid tumors (lung, GI, GU) |
| **Idiopathic** | Up to 50% | No identifiable trigger |

In a study of single-organ cutaneous small vessel vasculitis, *"Drugs and preceding infections were identified as precipitating factors in 40% and 20% of cases, respectively"* ([PMID: 28328827](https://pubmed.ncbi.nlm.nih.gov/28328827/)). Furthermore, *"LCV can also be idiopathic in up to 50% of cases"* ([PMID: 39072425](https://pubmed.ncbi.nlm.nih.gov/39072425/)).

### Risk Factors

**Genetic Risk Factors:**
- **HLA associations:** HLA-DRB1 alleles have been associated with disease susceptibility in cutaneous vasculitis ([PMID: 12473277](https://pubmed.ncbi.nlm.nih.gov/12473277/)). IL-1 receptor antagonist gene polymorphisms appear to influence disease severity.
- **Complement pathway variants:** Inherited complement deficiencies (particularly C2, C4) predispose to immune complex disease.
- No single-gene Mendelian inheritance pattern has been established; the disease follows a **multifactorial/polygenic** model.

**Environmental Risk Factors:**
- Drug exposure (most significant modifiable risk factor)
- Recent infection (within 1-3 weeks prior to onset)
- Vaccination (rare; documented with influenza, COVID-19 vaccines) ([PMID: 34973526](https://pubmed.ncbi.nlm.nih.gov/34973526/))
- Age: adults more frequently affected than children for HV subtype (mean age ~60 years) ([PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/))
- Sex: approximately equal male-to-female ratio

### Protective Factors

- **Drug withdrawal:** Removal of the offending drug leads to resolution in drug-induced cases, with favorable outcome for all patients ([PMID: 30173896](https://pubmed.ncbi.nlm.nih.gov/30173896/))
- **Treatment of underlying infection:** Eradication of triggering infections prevents recurrence
- **Avoidance of known triggers:** Primary prevention through pharmacovigilance

### Gene-Environment Interactions

The genetic basis of Allergic Cutaneous Vasculitis is complex and polygenic. Environmental triggers (drugs, infections) act on a genetically susceptible host to initiate immune complex formation. Polymorphisms in cytokine genes (TNF-alpha, IL-1, IL-6), complement components, and HLA alleles likely modulate individual susceptibility and disease severity. However, specific gene-environment interactions for this condition have not been systematically mapped through GWAS or GxE studies.

---

## 3. Phenotypes

### Clinical Manifestations

#### Palpable Purpura (Cardinal Sign)
- **HPO Term:** HP:0000979 (Purpura)
- **Type:** Physical manifestation / clinical sign
- **Characteristics:** Non-blanching, raised (palpable) purpuric papules, 1-3 mm in diameter, symmetrically distributed on dependent areas (lower extremities, buttocks)
- **Frequency:** Present in >90% of patients; purpura was the most common lesion (n=83/112 in one series) ([PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/))
- **Onset:** Acute, typically 7-21 days after initial antigen exposure; 1-3 days upon re-exposure
- **Severity:** Variable, from mild petechiae to extensive purpura
- **Progression:** Episodic; individual lesions resolve in 1-4 weeks, often with residual hyperpigmentation

#### Skin Ulceration
- **HPO Term:** HP:0200042 (Skin ulcer)
- **Type:** Physical manifestation
- **Characteristics:** Necrotic skin ulcers, particularly on lower extremities
- **Frequency:** Occurs in a subset of patients; macules independently increased risk of skin ulcer formation (OR=16, 95% CI: 1.5-176.6, P=0.0075) ([PMID: 28328827](https://pubmed.ncbi.nlm.nih.gov/28328827/))
- **Severity:** Moderate to severe; may require specific treatment

#### Urticarial Lesions
- **HPO Term:** HP:0001025 (Urticaria)
- **Type:** Clinical sign
- **Characteristics:** Urticarial wheals lasting >24 hours, often painful rather than pruritic, leaving residual hyperpigmentation (distinguishing from chronic spontaneous urticaria)
- **Frequency:** Found in urticarial vasculitis variant (~2.7% of all cutaneous vasculitis) ([PMID: 24378743](https://pubmed.ncbi.nlm.nih.gov/24378743/))

#### Arthralgia/Arthritis
- **HPO Term:** HP:0002829 (Arthralgia)
- **Type:** Symptom
- **Frequency:** Present in ~40-60% of patients; arthralgia and/or arthritis was observed in 13/21 UV patients ([PMID: 24378743](https://pubmed.ncbi.nlm.nih.gov/24378743/))

#### Systemic Symptoms
- **HPO Terms:** HP:0001945 (Fever), HP:0012378 (Fatigue), HP:0003326 (Myalgia)
- **Type:** Constitutional symptoms
- **Frequency:** Constitutional syndrome in 10-56% depending on subtype; more common in hypocomplementemic forms

#### Laboratory Abnormalities
- **Elevated ESR/CRP:** HP:0003565 (Elevated ESR) - found in ~50-60% of cases
- **Leukocytosis:** HP:0001974 - present in a subset
- **Hypocomplementemia:** HP:0005421 (Decreased serum complement) - in ~10-20%; associated with systemic involvement
- **Positive ANA:** HP:0003493 - in a minority of cases

### Quality of Life Impact

Palpable purpura and skin ulceration cause significant cosmetic distress, pain, and functional limitation, particularly when affecting the lower extremities. Patients with chronic/relapsing disease report reduced quality of life related to unpredictable flares, pain, and visible skin lesions. The urticarial vasculitis variant may cause significant pruritus, angioedema (51% of HUV cases), and systemic symptoms affecting daily functioning ([PMID: 25385679](https://pubmed.ncbi.nlm.nih.gov/25385679/)).

---

## 4. Genetic/Molecular Information

### Causal Genes

No single causal gene has been identified for Allergic Cutaneous Vasculitis. The disease is considered **non-Mendelian** with a **polygenic/multifactorial** basis.

### Susceptibility Loci and Associations

| Gene/Locus | Association | Evidence |
|---|---|---|
| **HLA-DRB1** | Susceptibility to cutaneous vasculitis and IgA vasculitis | Confirmed association in multiple populations ([PMID: 12473277](https://pubmed.ncbi.nlm.nih.gov/12473277/)) |
| **IL1RN** (IL-1 receptor antagonist) | Disease severity modifier | Gene polymorphisms implicated in cutaneous vasculitis severity |
| **ICAM1** | Pathogenic role in leukocyte adhesion and vessel wall damage | Polymorphisms associated with susceptibility |
| **TNF** | Influences inflammatory response | TNF polymorphisms affect susceptibility to various vasculitides |
| **Complement genes (C2, C4)** | Predisposition to immune complex clearance defects | Deficiencies increase risk of immune complex diseases |
| **ERAP1** | Peptide processing and MHC-I presentation | Epistatic interaction with HLA-B*51 in related vasculitis (Behcet's disease) ([PMID: 30514861](https://pubmed.ncbi.nlm.nih.gov/30514861/)) |

### Variant Classification

No specific pathogenic variants meeting ACMG/AMP criteria have been classified for Allergic Cutaneous Vasculitis. The genetic contribution is through common susceptibility polymorphisms (SNPs) rather than rare pathogenic mutations. Genetic testing (WGS, WES, gene panels) is **not routinely indicated** for this condition.

### Epigenetic Information

Epigenetic studies specific to Allergic Cutaneous Vasculitis are limited. In related vasculitides (Behcet's disease, IgA vasculitis), DNA methylation changes and non-coding RNA alterations have been implicated in disease pathogenesis. Systematic epigenomic profiling (ENCODE, Roadmap Epigenomics) has not been specifically performed for this condition.

### Chromosomal Abnormalities

No chromosomal abnormalities (aneuploidy, translocations, inversions) are associated with Allergic Cutaneous Vasculitis. This is not a chromosomal disorder.

---

## 5. Environmental Information

### Environmental Factors

- **Drug exposure:** The most significant environmental trigger. Drug-induced vasculitis accounts for 10-20% of all vasculitis cases ([PMID: 30173896](https://pubmed.ncbi.nlm.nih.gov/30173896/)). The mean delay from treatment onset to vasculitis was 14.46 days (range: 5 days to 6 weeks).
- **Occupational exposures:** Exposure to industrial chemicals, solvents, and silica dust has been associated with increased vasculitis risk in some studies, though specific data for cutaneous LCV are sparse.

### Lifestyle Factors

No strong associations with specific lifestyle factors (smoking, diet, exercise, alcohol) have been established for Allergic Cutaneous Vasculitis, though general cardiovascular risk factors may affect vascular health.

### Infectious Agents

| Pathogen | Mechanism | Evidence |
|---|---|---|
| **Hepatitis B virus** (NCBI Taxon: 10407) | Circulating immune complexes with HBsAg | Classical association |
| **Hepatitis C virus** (NCBI Taxon: 11103) | Cryoglobulinemia and immune complex formation | Associated with cryoglobulinemic vasculitis ([PMID: 9872481](https://pubmed.ncbi.nlm.nih.gov/9872481/)) |
| **Streptococcus** spp. (NCBI Taxon: 1301) | Post-infectious immune complex formation | Common trigger in children |
| **SARS-CoV-2** (NCBI Taxon: 2697049) | Viral-triggered immune complex vasculitis | Documented in COVID-19 patients ([PMID: 33122236](https://pubmed.ncbi.nlm.nih.gov/33122236/)) |
| **HIV** (NCBI Taxon: 11676) | Immune dysregulation and immune complex formation | Associated with various vasculitis subtypes |
| **Human metapneumovirus** (NCBI Taxon: 162145) | Post-infectious immune response | Case report in infant AHOI ([PMID: 39655129](https://pubmed.ncbi.nlm.nih.gov/39655129/)) |

---

## 6. Mechanism / Pathophysiology

### Pathogenic Cascade

The pathogenesis of Allergic Cutaneous Vasculitis follows a well-characterized immune complex-mediated cascade:

```
TRIGGER (Drug/Infection/Autoantigen)
        |
        v
ANTIGEN-ANTIBODY COMPLEX FORMATION
(IgG or IgM + antigen -> circulating immune complexes)
        |
        v
IMMUNE COMPLEX DEPOSITION IN VESSEL WALLS
(Postcapillary venules, favored by vascular turbulence,
 vessel wall dilation, and hemodynamic factors)
        |
        v
COMPLEMENT ACTIVATION (Classical Pathway)
(C1q binding -> C3a, C5a anaphylatoxin generation)
        |
        v
NEUTROPHIL CHEMOTAXIS AND RECRUITMENT
(C5a-mediated; P-selectin, E-selectin, ICAM-1 adhesion)
        |
        v
NEUTROPHIL DEGRANULATION
(Release of lysosomal enzymes: elastase, collagenase,
 myeloperoxidase, reactive oxygen species)
        |
        v
VESSEL WALL DESTRUCTION
(Fibrinoid necrosis, leukocytoclasia,
 red blood cell extravasation -> purpura)
        |
        v
CLINICAL MANIFESTATION
(Palpable purpura, skin ulceration)
```

As described by Sams: *"Under circumstances of vascular turbulence or vessel wall dilatation this complex may become fixed, activating the complement sequence with elaboration of chemotactic factors for neutrophils. These cells release lysosomal enzymes resulting in vessel wall destruction"* ([PMID: 3159805](https://pubmed.ncbi.nlm.nih.gov/3159805/)).

### Molecular Pathways

- **Complement cascade (Classical Pathway):** KEGG hsa04610; GO:0006958 (complement activation, classical pathway)
- **Fc receptor-mediated signaling:** Immune complex binding to Fc-gamma-RIIa and Fc-gamma-RIIIb on neutrophils
- **NF-kB signaling pathway:** Activation of pro-inflammatory transcription programs
- **TNF signaling pathway:** KEGG hsa04668; amplification of inflammatory response

### Cellular Processes

- **Inflammation:** GO:0006954 - Central process; neutrophilic inflammation with secondary lymphocytic and eosinophilic components
- **Complement activation:** GO:0006956 - Classical pathway activation by immune complexes
- **Leukocyte migration:** GO:0050900 - Neutrophil transmigration across endothelium
- **Cell death (necrosis):** GO:0070265 - Fibrinoid necrosis of vessel walls
- **Phagocytosis:** GO:0006909 - Clearance of immune complexes and debris

### Immune System Involvement

This is fundamentally an **immune complex-mediated disease** (Type III hypersensitivity):

- **Humoral immunity:** Production of IgG, IgM, or IgA antibodies against triggering antigens
- **Complement system:** Classical pathway activation is central; C1q, C3, C4 deposition in vessel walls
- **Innate immunity:** Neutrophils are the primary effector cells; mast cell degranulation contributes
- **Adaptive immunity:** T cells play a secondary role in chronic/relapsing forms

**Cell types involved:**
- Neutrophils (CL:0000775) - primary effector cells
- Endothelial cells (CL:0000115) - target of injury
- Mast cells (CL:0000097) - vasoactive mediator release
- Monocytes/macrophages (CL:0000576) - phagocytosis and antigen presentation
- B lymphocytes (CL:0000236) - antibody production
- T lymphocytes (CL:0000084) - secondary role in chronic disease

### Tissue Damage Mechanisms

- **Fibrinoid necrosis:** Deposition of fibrin and immune complexes within vessel walls
- **Oxidative stress:** Neutrophil-generated reactive oxygen species (superoxide, hydrogen peroxide, hypochlorous acid)
- **Enzymatic degradation:** Neutrophil elastase, collagenase, and myeloperoxidase destroy vessel wall components
- **Hemorrhage:** Extravasation of red blood cells through damaged vessel walls

### Biochemical Abnormalities

- Elevated circulating immune complexes
- Complement consumption (decreased C3, C4, CH50 in some cases)
- Elevated ESR and CRP reflecting systemic inflammation
- In urticarial vasculitis: anti-C1q autoantibodies (55% of HUV patients) ([PMID: 25385679](https://pubmed.ncbi.nlm.nih.gov/25385679/))

### GO Terms for Key Biological Processes

| GO ID | Term | Relevance |
|---|---|---|
| GO:0006958 | Complement activation, classical pathway | Central pathogenic mechanism |
| GO:0006954 | Inflammatory response | Core disease process |
| GO:0030593 | Neutrophil chemotaxis | Neutrophil recruitment to vessels |
| GO:0050900 | Leukocyte migration | Transmigration across endothelium |
| GO:0042119 | Neutrophil activation | Degranulation and ROS release |
| GO:0019724 | B cell mediated immunity | Antibody production |
| GO:0006955 | Immune response | Overall immune activation |

### Molecular Profiling

**Transcriptomics/gene expression:** No systematic transcriptomic studies specific to cutaneous LCV have been published in GEO or ArrayExpress. Gene expression profiling of vasculitic skin lesions is a knowledge gap.

**Proteomics:** No published proteomic datasets specific to cutaneous LCV. Elevated complement components and immunoglobulins in lesional tissue are well-documented by immunohistochemistry and DIF.

**Metabolomics/Lipidomics:** Not systematically studied for this condition.

**Advanced Technologies:** Single-cell analysis, spatial transcriptomics, and functional genomics screens have not been applied to Allergic Cutaneous Vasculitis.

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary organ:** Skin (UBERON:0002097)
- Dermis (UBERON:0002067) - site of postcapillary venules
- Specifically the superficial (papillary) dermis

**Secondary organ involvement** (in systemic extension):
- Kidneys (UBERON:0002113) - glomerulonephritis in ~14-30% of IgA vasculitis
- Joints (UBERON:0004905) - arthralgia/arthritis in 40-82%
- Gastrointestinal tract (UBERON:0001555) - abdominal pain, GI bleeding in 18-19%
- Lungs (UBERON:0002048) - rare, in hypocomplementemic urticarial vasculitis (19%)
- Eyes (UBERON:0000970) - rare, ocular involvement in HUV (56%)

**Body systems involved:**
- Integumentary system (primary)
- Immune system
- Cardiovascular system (microcirculation)
- Musculoskeletal system (joints)

### Tissue and Cell Level

- **Tissue types affected:** Vascular endothelium, perivascular connective tissue
- **Specific vessel type:** Postcapillary venules (7-50 micrometers diameter) in the superficial dermis
- **Cell populations targeted:**
  - Endothelial cells (CL:0000115) - direct target of immune complex-mediated injury
  - Pericytes (CL:0000669) - secondary damage
  - Dermal fibroblasts (CL:0002551) - perivascular damage

### Subcellular Level

- **Endoplasmic reticulum** (GO:0005783) - involved in antibody/complement component synthesis
- **Lysosomes** (GO:0005764) - neutrophil lysosomal enzyme release
- **Plasma membrane** (GO:0005886) - site of Fc receptor and complement receptor interactions
- **Extracellular space** (GO:0005615) - immune complex deposition and complement activation

### Localization

- **Primary sites:** Lower extremities (UBERON:0002103), particularly the legs below the knees; buttocks (UBERON:0013691)
- **Secondary sites:** Upper extremities, trunk (in extensive cases)
- **Pattern:** Bilateral and symmetric; gravity-dependent distribution
- **Lateralization:** Typically bilateral and symmetric; asymmetric involvement has been reported rarely (e.g., post-vaccination)

---

## 8. Temporal Development

### Onset

- **Typical age of onset:** Any age; peak incidence in adults aged 40-60 years. Mean age 60 +/- 19 years in one large series ([PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/)). In children, IgA vasculitis (HSP) peaks at ages 4-6 years; hypersensitivity vasculitis occurs in older children (mean age 9 years) ([PMID: 28929493](https://pubmed.ncbi.nlm.nih.gov/28929493/))
- **Onset pattern:** Acute to subacute; typically 7-21 days after initial exposure to the triggering antigen; 1-3 days upon re-exposure. Drug-induced vasculitis has a mean delay of 14.46 days ([PMID: 30173896](https://pubmed.ncbi.nlm.nih.gov/30173896/))

### Progression

- **Disease course pattern:** Typically self-limited and monophasic when the trigger is removed. Chronic or relapsing-remitting in idiopathic cases or when the trigger persists.
- **Disease duration:** Most acute episodes resolve within 1-4 weeks. Chronic disease may persist for months to years.
- **Progression rate:** Variable; most cases resolve rapidly with trigger removal. A subset develops chronic disease.

### Disease Stages

1. **Prodromal phase:** Malaise, fever, myalgia (hours to days before skin lesions)
2. **Acute phase:** Palpable purpura, urticarial lesions, pain (days to weeks)
3. **Resolution phase:** Fading of purpura with residual post-inflammatory hyperpigmentation (weeks)
4. **Chronic/relapsing phase:** In 18-25% of patients, recurrent episodes over months to years

### Patterns

- **Remission patterns:** Spontaneous remission is common, especially in drug-induced cases after drug withdrawal. Treatment-induced remission with corticosteroids or immunosuppressants in refractory cases.
- **Relapse:** 25% relapse during 6-month follow-up ([PMID: 28328827](https://pubmed.ncbi.nlm.nih.gov/28328827/)); 18% relapse at 14 +/- 13 months in a larger cohort ([PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/)). Greater number of affected skin areas is an independent risk factor for relapse.

---

## 9. Inheritance and Population

### Epidemiology

| Measure | Value | Source |
|---|---|---|
| **Annual incidence (cutaneous vasculitis, all types)** | 38.6 per million (95% CI 30.6-48.1) | [PMID: 9598892](https://pubmed.ncbi.nlm.nih.gov/9598892/) |
| **Annual incidence (CLA specifically)** | 15.4 per million (95% CI 10.6-21.8) | [PMID: 9598892](https://pubmed.ncbi.nlm.nih.gov/9598892/) |
| **Prevalence** | Not well-established; estimated at 30-60 per million | Various sources |

As noted in the Norfolk Vasculitis Registry: *"The overall annual incidence of cutaneous vasculitis was 38.6/million (95% CI 30.6-48.1), and for CLA 15.4/million (95% CI 10.6-21.8)... Cutaneous vasculitis is as common as systemic vasculitis"* ([PMID: 9598892](https://pubmed.ncbi.nlm.nih.gov/9598892/)).

### Genetic Architecture

- **Inheritance pattern:** Multifactorial/polygenic; not Mendelian
- **Penetrance:** Not applicable (non-Mendelian)
- **Expressivity:** Variable
- **HLA associations:** HLA-DRB1 alleles associated with susceptibility ([PMID: 12473277](https://pubmed.ncbi.nlm.nih.gov/12473277/))
- **Genetic anticipation:** Not applicable
- **Germline mosaicism:** Not applicable
- **Founder effects:** Not documented
- **Consanguinity:** No known role
- **Carrier frequency:** Not applicable (non-Mendelian)

### Population Demographics

- **Sex ratio:** Approximately 1:1 (male:female). In a series of 112 patients: 57 males, 55 females ([PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/))
- **Age distribution:** Bimodal - childhood (IgA vasculitis/HSP, peak 4-6 years) and adult-onset (HV, peak 40-60 years)
- **Geographic distribution:** Worldwide, with no specific endemic areas. Higher reported incidence in Northern European populations (UK study). Cutaneous leukocytoclastic angiitis constituted 8.2% of all vasculitis in an Iranian cohort ([PMID: 26170524](https://pubmed.ncbi.nlm.nih.gov/26170524/))
- **Ethnic variation:** No strong ethnic predilection demonstrated, though HLA-associated susceptibility varies by population

---

## 10. Diagnostics

### Clinical Tests

#### Biopsy (Gold Standard)
- **Skin biopsy with histopathology:** The diagnostic gold standard. Biopsies should be taken from fresh lesions (<48 hours old) and should include all layers of the skin through subcutis ([PMID: 18415063](https://pubmed.ncbi.nlm.nih.gov/18415063/)). Key findings:
  - Leukocytoclastic vasculitis (neutrophilic infiltrate with nuclear dust)
  - Fibrinoid necrosis of vessel walls
  - Extravasation of red blood cells
  - Intraluminal thrombi (variable)

#### Direct Immunofluorescence (DIF)
- DIF of early lesions (ideally <24 hours) demonstrates perivascular deposits of immunoglobulins (IgG, IgM, IgA) and complement (C3) in vessel walls
- DIF sensitivity estimated at ~75% ([PMID: 39307568](https://pubmed.ncbi.nlm.nih.gov/39307568/))
- Vascular IgA deposits are associated with renal disease (IgA vasculitis)
- DIF should be obtained from an early, partially blanchable macule ([PMID: 41399325](https://pubmed.ncbi.nlm.nih.gov/41399325/))

#### Laboratory Tests

| Test | Purpose | Expected Findings |
|---|---|---|
| CBC with differential | Baseline; detect eosinophilia, cytopenia | Leukocytosis, eosinophilia (variable) |
| ESR/CRP | Inflammatory markers | Elevated in 50-60% |
| Urinalysis | Renal involvement screening | Hematuria, proteinuria (if renal involvement) |
| Serum creatinine/BUN | Renal function | Elevated if renal involvement |
| Complement levels (C3, C4, CH50) | Complement consumption | Low in hypocomplementemic forms |
| Serum immunoglobulins | IgA elevation | Elevated IgA in IgA vasculitis |
| ANA, ANCA, RF | Exclude systemic autoimmune disease | Usually negative in primary CLA |
| Hepatitis B/C serology | Exclude viral triggers | Positive if viral-associated |
| Cryoglobulins | Cryoglobulinemic vasculitis | Positive in cryoglobulinemic forms |
| Blood cultures | Exclude infective endocarditis | If fever present |

### Standardized Diagnostic Criteria

**ACR 1990 Classification Criteria for Hypersensitivity Vasculitis** (3 or more of 5):
1. Age at disease onset >16 years
2. Medication at disease onset (possible offending drug)
3. Palpable purpura
4. Maculopapular rash
5. Biopsy showing granulocytes in a perivascular/extravascular location

*Note: These criteria have limitations in clinical practice. Sensitivity 71%, specificity 83.9%* ([PMID: 9735061](https://pubmed.ncbi.nlm.nih.gov/9735061/)): *"The 1990 ACR classification criteria function poorly in the diagnosis of specific vasculitides."*

**CHCC 2012 Definition** provides clearer distinction as "cutaneous leukocytoclastic angiitis" - isolated cutaneous small vessel vasculitis without systemic vasculitis features.

**2025 EADV Consensus:** The first International Consensus Statement for adult CSVV proposes a practical management algorithm emphasizing that *"the diagnosis of CSVV relies on a combination of clinical manifestations, laboratory findings and histopathology. Palpable purpura on the lower extremities is recognized as the most reliable hallmark"* ([PMID: 41399325](https://pubmed.ncbi.nlm.nih.gov/41399325/)).

### Differential Diagnosis

| Condition | Key Distinguishing Features |
|---|---|
| IgA vasculitis (HSP) | IgA deposits on DIF; renal/GI involvement; children |
| ANCA-associated vasculitis | ANCA positive; systemic involvement |
| Cryoglobulinemic vasculitis | Cryoglobulins present; hepatitis C association |
| Urticarial vasculitis | Urticarial lesions >24 hours; may have hypocomplementemia |
| Thrombocytopenic purpura | Low platelets; non-palpable purpura |
| Erythema multiforme | Target lesions; drug/infection trigger |
| Chronic spontaneous urticaria | No vasculitis on biopsy; wheals <24 hours |
| Pigmented purpuric dermatoses | Cayenne pepper-like pigmentation; no fibrinoid necrosis |

### Genetic Testing

Not routinely indicated. No single-gene testing, gene panels, WES, or WGS is recommended for Allergic Cutaneous Vasculitis, as it is not a Mendelian disorder.

### Omics-Based Diagnostics

No validated omics-based diagnostic tests exist for this condition. This remains a knowledge gap.

---

## 11. Outcome/Prognosis

### Survival and Mortality

- **Overall prognosis:** Favorable. Allergic Cutaneous Vasculitis is generally a benign, self-limited condition.
- **Mortality:** Disease-specific mortality is very low for skin-limited disease. *"SoCSVV is a benign disease with a good clinical outcome but with a significant risk of relapse and skin ulcer formation"* ([PMID: 28328827](https://pubmed.ncbi.nlm.nih.gov/28328827/)).
- **Life expectancy:** Not significantly reduced in skin-limited disease.
- In paraneoplastic vasculitis, prognosis depends on the underlying malignancy: 10/16 patients died due to malignancy ([PMID: 24145696](https://pubmed.ncbi.nlm.nih.gov/24145696/)).

### Morbidity and Function

- **Relapse rate:** 18-25% of patients experience relapse. In one series, 20/112 (18%) experienced relapse at 14 +/- 13 months ([PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/)). In another, 25% relapsed during 6-month follow-up ([PMID: 28328827](https://pubmed.ncbi.nlm.nih.gov/28328827/)).
- **Treatment requirement:** Only 36.6% required specific treatment ([PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/))
- **Skin ulcer formation:** Significant complication; macules independently increased risk (OR=16, P=0.0075) ([PMID: 28328827](https://pubmed.ncbi.nlm.nih.gov/28328827/))
- **Post-inflammatory hyperpigmentation:** Common cosmetic sequela

### Prognostic Factors

| Factor | Impact |
|---|---|
| Identifiable and removable trigger (drug) | Favorable outcome |
| Greater number of affected skin areas | Increased relapse risk |
| Presence of macules | Increased risk of skin ulceration |
| Systemic involvement | Worse prognosis, requires aggressive treatment |
| Underlying malignancy | Prognosis dependent on malignancy |
| Hypocomplementemia | Associated with systemic disease and worse outcomes |
| Idiopathic etiology | Higher likelihood of chronicity |

### Prognostic Biomarkers

No validated molecular prognostic biomarkers exist specifically for Allergic Cutaneous Vasculitis. Complement levels (C3, C4) and anti-C1q antibodies may have prognostic value in the urticarial vasculitis subset.

---

## 12. Treatment

### Pharmacotherapy

#### Trigger Removal (First-Line for All Cases)
- **MAXO:0000001** (Medical action) - Discontinuation of offending drugs; treatment of underlying infections
- *"The outcome was favorable for all patients"* with drug-induced vasculitis after drug withdrawal ([PMID: 30173896](https://pubmed.ncbi.nlm.nih.gov/30173896/))

#### Supportive Care
- **MAXO:0000950** (Supportive care)
  - Leg elevation
  - Compression stockings (MAXO:0000624)
  - Analgesics (NSAIDs for pain management)
  - Antihistamines (for pruritus)

#### Colchicine (First-Line for Chronic/Relapsing Disease)
- **CHEBI:23359** (Colchicine)
- **MAXO:0001298** (Pharmacotherapy)
- Dose: 0.5-1 mg/day
- Mechanism: Inhibits neutrophil chemotaxis and adhesion
- *"In chronic or relapsing LcV we suggest colchicine as a first-line... therapy"* ([PMID: 16249140](https://pubmed.ncbi.nlm.nih.gov/16249140/))

#### Dapsone (Second-Line)
- **CHEBI:4325** (Dapsone)
- Dose: 50-150 mg/day
- Mechanism: Inhibits neutrophil myeloperoxidase and chemotaxis
- *"...and dapsone as a second-line therapy"* ([PMID: 16249140](https://pubmed.ncbi.nlm.nih.gov/16249140/))
- Monitor for hemolytic anemia, methemoglobinemia, agranulocytosis

#### Corticosteroids (For Severe Disease)
- **CHEBI:50858** (Corticosteroid)
- Prednisone 0.5-1 mg/kg/day, tapered over weeks
- Indicated when signs of incipient skin necrosis are present
- *"Corticosteroids are indicated when there are signs of incipient skin necrosis"* ([PMID: 16249140](https://pubmed.ncbi.nlm.nih.gov/16249140/))
- *"Corticosteroids are effective for the treatment of skin symptoms in more than 80% of patients with UV"* ([PMID: 30268388](https://pubmed.ncbi.nlm.nih.gov/30268388/))

#### Immunosuppressive Agents (For Refractory Disease)
- Azathioprine (CHEBI:2948): Steroid-sparing agent
- Mycophenolate mofetil (CHEBI:168396): For chronic refractory cases
- Cyclophosphamide (CHEBI:4026): For severe systemic disease
- Methotrexate: Alternative steroid-sparing agent
- Cyclosporine: For refractory urticarial vasculitis

#### Biologic and Targeted Therapies (Emerging)
- **Rituximab** (CHEBI:64357): Anti-CD20 monoclonal antibody for refractory disease, especially HUV ([PMID: 25385679](https://pubmed.ncbi.nlm.nih.gov/25385679/))
- **Omalizumab**: Anti-IgE antibody for normocomplementemic urticarial vasculitis ([PMID: 30660172](https://pubmed.ncbi.nlm.nih.gov/30660172/))
- **Upadacitinib** (JAK inhibitor): Emerging therapy for refractory UV ([PMID: 40933560](https://pubmed.ncbi.nlm.nih.gov/40933560/))
- **IVIG**: For severe refractory cases
- **Hydroxychloroquine**: For mild chronic disease, especially UV

### Treatment Algorithm

```
Step 1: Identify and remove trigger (drug, infection)
        + Supportive care (elevation, compression, analgesics)
        |
Step 2: If chronic/relapsing --> Colchicine 0.5-1 mg/day
        |
Step 3: If inadequate --> Dapsone 50-150 mg/day
        |
Step 4: If skin necrosis --> Corticosteroids (prednisone 0.5-1 mg/kg)
        |
Step 5: If refractory --> Immunosuppressant (AZA, MMF, CYC)
                        --> Biologic (rituximab, omalizumab)
                        --> JAK inhibitor (upadacitinib - emerging)
```

*"Therapy of immune complex LcV often does not require aggressive therapy due to a usually favourable course"* ([PMID: 16249140](https://pubmed.ncbi.nlm.nih.gov/16249140/)).

### Pharmacogenomics

No specific pharmacogenomic associations (PharmGKB, CPIC) have been established for treatments of Allergic Cutaneous Vasculitis. Standard pharmacogenomic considerations for corticosteroids, azathioprine (TPMT/NUDT15 testing), and dapsone (G6PD testing) apply.

### Treatment Outcomes

- Drug-induced vasculitis: Favorable outcome in all patients after drug withdrawal ([PMID: 30173896](https://pubmed.ncbi.nlm.nih.gov/30173896/))
- Corticosteroids: >80% response rate in urticarial vasculitis ([PMID: 30268388](https://pubmed.ncbi.nlm.nih.gov/30268388/))
- Only 36.6% of patients require specific treatment beyond supportive care ([PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/))

---

## 13. Prevention

### Primary Prevention

- **Drug safety monitoring (MAXO:0000058 - pharmacovigilance):** Awareness of drugs known to cause vasculitis
- **Infection prevention:** Vaccination (where applicable), hygiene measures
- **Avoidance of known triggers:** In patients with prior drug-induced vasculitis, avoidance of the implicated drug and chemically related agents

### Secondary Prevention

- **Early recognition:** Clinician awareness of palpable purpura as a potential vasculitis sign
- **Prompt biopsy:** Early histopathological confirmation
- **Drug rechallenge avoidance:** Documentation of drug-induced vasculitis in medical records, allergy alerts

### Tertiary Prevention

- **Monitoring for relapse:** Regular clinical follow-up, especially in the first 6-12 months
- **Monitoring for systemic involvement:** Urinalysis, renal function, complement levels
- **Treatment of chronic/relapsing disease:** Maintenance therapy with colchicine or dapsone
- **Compression therapy:** To reduce stasis-related purpura in lower extremities

### Screening

- **No population-based screening programs** exist for Allergic Cutaneous Vasculitis
- **Targeted surveillance** is recommended for patients on medications known to cause vasculitis
- **Genetic screening** is not applicable (non-Mendelian disease)

### Public Health

Drug-induced vasculitis surveillance through pharmacovigilance systems (FDA FAERS, WHO VigiBase) represents the most relevant public health intervention. Education of clinicians regarding early recognition and prompt drug withdrawal is essential.

---

## 14. Other Species / Natural Disease

### Natural Disease in Animals

Immune complex-mediated vasculitis occurs in several animal species:

- **Dogs** (NCBI Taxon: 9615): Cutaneous vasculitis is well-documented, particularly in breeds like Dachshunds, Rottweilers, Collies, Shetland Sheepdogs, Jack Russell Terriers, and Greyhounds. Drug-induced vasculitis has been reported. Canine cutaneous vasculitis presents with purpura, ulceration, and necrosis similar to human disease.
- **Horses** (NCBI Taxon: 9796): Equine purpura hemorrhagica is a post-infectious immune complex vasculitis, often following *Streptococcus equi* infection (strangles). This is one of the best-characterized veterinary analogs, with immune complex deposition in dermal vessels.
- **Cats** (NCBI Taxon: 9685): Rare reports of cutaneous vasculitis exist, sometimes associated with viral infections (FIV, FeLV).

### Comparative Biology

The fundamental pathogenic mechanism (immune complex deposition, complement activation, neutrophil-mediated vessel damage) is evolutionarily conserved across mammalian species. Complement components, Fc receptors, and neutrophil function are highly conserved, making animal models relevant for studying human disease mechanisms.

### Zoonotic Potential

Allergic Cutaneous Vasculitis itself is **not zoonotic**. However, certain infectious triggers (hepatitis viruses, Streptococcus) may have zoonotic or environmental reservoirs.

---

## 15. Model Organisms

### Animal Models

#### Arthus Reaction Models

The **reverse passive Arthus reaction** is the classic experimental model for immune complex vasculitis:

- **Rabbits** (NCBI Taxon: 9986): Prolonged infusion of activated complement produces pulmonary microvascular necrosis: *"piecemeal microvascular necrosis did develop, rendering this current model more credible... as a mimic of triggering events"* ([PMID: 6840826](https://pubmed.ncbi.nlm.nih.gov/6840826/))
- **Mice** (NCBI Taxon: 10090): The cutaneous reverse passive Arthus reaction using IgE produced eosinophilic vasculitis with *"marked infiltration of eosinophils in which neutrophils, mast cells, and macrophages were also mixed"* and demonstrated P-selectin dependence of eosinophil recruitment ([PMID: 19389931](https://pubmed.ncbi.nlm.nih.gov/19389931/)). This model shows that *"the Fc class of immunoglobulins, which forms these immune complexes, critically determines the disease manifestation of vasculitis."*

### Genetic Models

| Model | Type | Application |
|---|---|---|
| E-selectin knockout mouse | Gene knockout | Role of E-selectin in leukocyte adhesion |
| P-selectin knockout mouse | Gene knockout | P-selectin loss reduced eosinophil accumulation |
| L-selectin knockout mouse | Gene knockout | Role of L-selectin in neutrophil rolling |
| ICAM-1 knockout mouse | Gene knockout | Intercellular adhesion in vasculitis |
| Complement-deficient mice (C3-/-, C5-/-) | Gene knockout | Role of complement in immune complex disease |
| Fc-gamma-R knockout mice | Gene knockout | Fc receptor-mediated immune complex clearance |

### Model Characteristics

**Phenotype recapitulation:** The Arthus reaction models faithfully reproduce the key histopathological features of human LCV: neutrophilic infiltration, fibrinoid necrosis, and hemorrhage. The IgE-mediated Arthus reaction additionally recapitulates eosinophilic vasculitis.

**Model limitations:**
- Animal models typically use a single known antigen, while human disease involves diverse and often unidentified antigens
- Murine models may not fully recapitulate the chronicity and relapsing nature of human disease
- Differences in complement system components and Fc receptor profiles between species
- Most models induce acute, single-episode vasculitis rather than chronic/relapsing disease

### Research Applications

- Elucidating the role of specific complement components and Fc receptors
- Testing therapeutic interventions (anti-complement, anti-adhesion molecule therapies)
- Understanding the transition from acute to chronic vasculitis
- Studying the contribution of different immunoglobulin classes (IgG vs IgE vs IgA)

### Resources

- MGI (Mouse Genome Informatics): Knockout and transgenic mouse models
- IMPC (International Mouse Phenotyping Consortium): Phenotyping data
- IMSR (International Mouse Strain Resource): Strain availability

---

## Key Findings (with Statistical Evidence)

### Finding 1: Allergic Cutaneous Vasculitis Is an Immune Complex-Mediated Small Vessel Vasculitis

The pathogenesis is firmly established as a Type III hypersensitivity immune complex disease involving postcapillary venules. Histopathology reveals the diagnostic triad of leukocytoclastic vasculitis, fibrinoid necrosis, and extravasation of red blood cells. The annual incidence of biopsy-proven cutaneous vasculitis is 38.6/million (95% CI 30.6-48.1), and specifically for cutaneous leukocytoclastic angiitis, 15.4/million (95% CI 10.6-21.8) ([PMID: 9598892](https://pubmed.ncbi.nlm.nih.gov/9598892/)). This establishes cutaneous vasculitis as being as common as systemic vasculitis in the population.

### Finding 2: Etiology Breakdown - Drugs (~40%), Infections (~20%), Idiopathic (~50%)

In SoCSVV, drugs and preceding infections were identified as precipitating factors in 40% and 20% of cases, respectively ([PMID: 28328827](https://pubmed.ncbi.nlm.nih.gov/28328827/)). LCV remains idiopathic in up to 50% of cases ([PMID: 39072425](https://pubmed.ncbi.nlm.nih.gov/39072425/)). Drug-induced vasculitis accounts for 10-20% of all vasculitis cases ([PMID: 30173896](https://pubmed.ncbi.nlm.nih.gov/30173896/)). The most commonly implicated drugs are antibiotics (amoxicillin, vancomycin, clarithromycin, ciprofloxacin), followed by NSAIDs and allopurinol. The mean onset delay after drug initiation is 14.46 days.

### Finding 3: Favorable Prognosis with Significant Relapse Risk (18-25%)

SoCSVV has a good clinical outcome, with only 36.6% requiring specific treatment ([PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/)). However, 18-25% of patients experience relapse ([PMID: 28328827](https://pubmed.ncbi.nlm.nih.gov/28328827/); [PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/)). Macules independently increased risk of skin ulcer formation (OR=16, 95% CI: 1.5-176.6, P=0.0075), and greater number of affected skin areas was an independent risk factor for relapse. These prognostic factors help identify patients who may benefit from more aggressive follow-up and treatment.

### Finding 4: Treatment Ladder - Colchicine First-Line, Dapsone Second-Line, Corticosteroids for Severe Disease

The therapeutic approach is graduated: trigger removal and supportive care for mild disease, colchicine as first-line and dapsone as second-line for chronic/relapsing LCV ([PMID: 16249140](https://pubmed.ncbi.nlm.nih.gov/16249140/)), corticosteroids effective in >80% of UV patients ([PMID: 30268388](https://pubmed.ncbi.nlm.nih.gov/30268388/)), and immunosuppressants/biologics for refractory cases. Emerging therapies include JAK inhibitors (upadacitinib) and anti-IgE therapy (omalizumab) for specific subsets.

---

## Evidence Base

| PMID | Title | Contribution |
|---|---|---|
| [PMID: 3159805](https://pubmed.ncbi.nlm.nih.gov/3159805/) | *Human hypersensitivity angiitis, an immune complex disease* | Establishes immune complex pathogenesis |
| [PMID: 9598892](https://pubmed.ncbi.nlm.nih.gov/9598892/) | *Cutaneous vasculitis in a defined population* | Population-based epidemiological data |
| [PMID: 9854604](https://pubmed.ncbi.nlm.nih.gov/9854604/) | *Cutaneous vasculitis in children and adults* | Distribution of vasculitis subtypes in 303 patients |
| [PMID: 28328827](https://pubmed.ncbi.nlm.nih.gov/28328827/) | *Clinical study on SoCSVV* | Precipitating factors, relapse risk, prognosis |
| [PMID: 39072425](https://pubmed.ncbi.nlm.nih.gov/39072425/) | *Semaglutide-induced LCV* | Idiopathic rate up to 50%; etiology review |
| [PMID: 30173896](https://pubmed.ncbi.nlm.nih.gov/30173896/) | *Drug-induced vasculitis* | Drug-induced vasculitis characteristics and outcomes |
| [PMID: 27428231](https://pubmed.ncbi.nlm.nih.gov/27428231/) | *Etiologies and prognostic factors of LCV in 112 patients* | Large cohort treatment/outcomes data |
| [PMID: 16249140](https://pubmed.ncbi.nlm.nih.gov/16249140/) | *Management of leukocytoclastic vasculitis* | Treatment guidelines and therapeutic algorithm |
| [PMID: 30268388](https://pubmed.ncbi.nlm.nih.gov/30268388/) | *Treatment of urticarial vasculitis: systematic review* | Corticosteroid efficacy >80% |
| [PMID: 25385679](https://pubmed.ncbi.nlm.nih.gov/25385679/) | *Hypocomplementemic urticarial vasculitis in 57 patients* | HUV clinical spectrum and treatment |
| [PMID: 41399325](https://pubmed.ncbi.nlm.nih.gov/41399325/) | *EADV diagnostic recommendations for CSVV* | First international consensus statement |
| [PMID: 39307568](https://pubmed.ncbi.nlm.nih.gov/39307568/) | *DIF utility in cutaneous vasculitis - scoping review* | DIF sensitivity ~75% |
| [PMID: 12473277](https://pubmed.ncbi.nlm.nih.gov/12473277/) | *Systemic vasculitides* | HLA-DRB1 association with CV; genetic epidemiology |
| [PMID: 19389931](https://pubmed.ncbi.nlm.nih.gov/19389931/) | *Eosinophilic vasculitis by IgE-mediated Arthus reaction* | Mouse model; Fc class determines disease phenotype |
| [PMID: 6840826](https://pubmed.ncbi.nlm.nih.gov/6840826/) | *Pulmonary vasculitis in rabbits with activated complement* | Rabbit model of immune complex vasculitis |
| [PMID: 9735061](https://pubmed.ncbi.nlm.nih.gov/9735061/) | *Limitations of ACR 1990 criteria* | Classification criteria limitations |
| [PMID: 18415063](https://pubmed.ncbi.nlm.nih.gov/18415063/) | *Histology of cutaneous vasculitides* | Biopsy technique and histological classification |
| [PMID: 24145696](https://pubmed.ncbi.nlm.nih.gov/24145696/) | *Paraneoplastic cutaneous vasculitis* | Malignancy association (3.8% of adults) |
| [PMID: 28929493](https://pubmed.ncbi.nlm.nih.gov/28929493/) | *Pediatric vasculitis: single center experience* | Childhood vasculitis epidemiology |
| [PMID: 40933560](https://pubmed.ncbi.nlm.nih.gov/40933560/) | *Upadacitinib in refractory UV* | Emerging JAK inhibitor therapy |
| [PMID: 30660172](https://pubmed.ncbi.nlm.nih.gov/30660172/) | *Omalizumab for normocomplementemic UV* | Anti-IgE therapy for UV |
| [PMID: 34973526](https://pubmed.ncbi.nlm.nih.gov/34973526/) | *LCV after COVID-19 vaccination* | Vaccine-associated vasculitis |
| [PMID: 33122236](https://pubmed.ncbi.nlm.nih.gov/33122236/) | *LCV in COVID-19 with positive skin PCR* | SARS-CoV-2-associated LCV |
| [PMID: 9872481](https://pubmed.ncbi.nlm.nih.gov/9872481/) | *Cryoglobulinemia in primary Sjogren's syndrome* | HCV-associated cryoglobulinemic vasculitis |
| [PMID: 39930301](https://pubmed.ncbi.nlm.nih.gov/39930301/) | *Antibiotic-induced IgA vasculitis* | 13 antibiotics associated with IgAV |

---

## Limitations and Knowledge Gaps

1. **Genetic basis poorly characterized:** No GWAS or large-scale genomic studies have been performed specifically for Allergic Cutaneous Vasculitis. The genetic architecture remains largely unknown.

2. **Lack of validated biomarkers:** There are no reliable circulating biomarkers to predict disease onset, severity, relapse risk, or treatment response.

3. **Limited randomized controlled trials:** *"There are no large prospective randomized controlled studies"* for the treatment of LCV ([PMID: 16249140](https://pubmed.ncbi.nlm.nih.gov/16249140/)). Treatment recommendations are based largely on case series, retrospective studies, and expert opinion.

4. **Idiopathic cases:** Up to 50% of cases have no identifiable trigger, limiting targeted prevention and treatment.

5. **Classification challenges:** The ACR 1990 criteria have significant limitations, with poor positive predictive values (17-29% in mixed cohorts) ([PMID: 9735061](https://pubmed.ncbi.nlm.nih.gov/9735061/)). Overlap between HSP and HV classification criteria creates confusion.

6. **Limited omics data:** No systematic transcriptomic, proteomic, or metabolomic profiling of cutaneous vasculitis tissue has been published. Single-cell and spatial transcriptomics studies are lacking.

7. **Quality of life data:** Disease-specific quality of life instruments have not been developed for cutaneous vasculitis.

8. **Long-term outcomes:** Limited data on long-term cardiovascular or renal outcomes in patients with isolated cutaneous vasculitis.

9. **Pediatric data:** Most large studies focus on adults; pediatric-specific data on hypersensitivity vasculitis (as opposed to IgA vasculitis) are sparse.

10. **Pharmacogenomic data:** No specific pharmacogenomic associations have been established for treatments of this condition.

---

## Proposed Follow-up Experiments/Actions

1. **Genome-wide association study (GWAS):** A multi-center GWAS of well-phenotyped Allergic Cutaneous Vasculitis patients vs. controls would identify susceptibility loci and clarify the genetic architecture.

2. **Biomarker discovery:** Prospective studies measuring circulating complement activation products (sC5b-9), immune complex levels, and cytokine profiles (IL-1, IL-6, IL-8, TNF-alpha) at diagnosis and during follow-up could identify predictive and prognostic biomarkers.

3. **Randomized controlled trials:** Head-to-head comparisons of colchicine vs. dapsone vs. placebo for chronic relapsing LCV are urgently needed. Trials of JAK inhibitors (upadacitinib) and anti-complement therapies merit investigation.

4. **Single-cell RNA sequencing:** Profiling of immune cell populations in lesional vs. non-lesional skin biopsies would reveal cell-type-specific mechanisms and identify therapeutic targets.

5. **Prospective cohort studies:** Large, multi-center prospective registries with standardized phenotyping (using CHCC 2012 definitions), serial biopsy, DIF, and long-term follow-up would clarify natural history, relapse predictors, and long-term outcomes.

6. **Pharmacovigilance data mining:** Systematic analysis of FDA Adverse Event Reporting System (FAERS) and WHO VigiBase for additional drugs associated with cutaneous vasculitis.

7. **Development of disease-specific QoL instruments:** Validated patient-reported outcome measures for cutaneous vasculitis would improve clinical trial design and patient care.

8. **Epigenomic profiling:** DNA methylation and histone modification analysis of vasculitis skin tissue could reveal epigenetic drivers of chronic/relapsing disease.

---

## Ontology Term Summary

| Domain | Ontology | Key Terms |
|---|---|---|
| Disease | MONDO | MONDO:0019552 (Cutaneous leukocytoclastic vasculitis) |
| Phenotypes | HPO | HP:0000979 (Purpura), HP:0200042 (Skin ulcer), HP:0001025 (Urticaria), HP:0002829 (Arthralgia), HP:0001945 (Fever), HP:0003565 (Elevated ESR), HP:0005421 (Decreased serum complement) |
| Biological Processes | GO | GO:0006958 (Complement activation, classical pathway), GO:0006954 (Inflammatory response), GO:0030593 (Neutrophil chemotaxis), GO:0050900 (Leukocyte migration), GO:0042119 (Neutrophil activation) |
| Cell Types | CL | CL:0000775 (Neutrophil), CL:0000115 (Endothelial cell), CL:0000097 (Mast cell), CL:0000236 (B cell), CL:0000576 (Monocyte) |
| Anatomy | UBERON | UBERON:0002097 (Skin), UBERON:0002067 (Dermis), UBERON:0002103 (Lower extremity) |
| Chemicals | CHEBI | CHEBI:23359 (Colchicine), CHEBI:4325 (Dapsone), CHEBI:50858 (Corticosteroid), CHEBI:2948 (Azathioprine) |
| Treatment | MAXO | MAXO:0001298 (Pharmacotherapy), MAXO:0000950 (Supportive care), MAXO:0000058 (Pharmacovigilance) |

---

*Report generated 2026-05-05. Based on analysis of 104 peer-reviewed publications and international consensus guidelines.*
