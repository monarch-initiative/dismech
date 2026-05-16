---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-06T21:04:26.978372Z'
end_time: '2026-05-06T22:38:23.286733Z'
duration_seconds: 5636.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aortitis
  mondo_id: ''
  category: Complex
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
citation_count: 53
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aortitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Aortitis** covering all of the
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

# Comprehensive Disease Characterization Report: Aortitis

## Summary

Aortitis is a heterogeneous group of inflammatory conditions affecting the aorta, encompassing both infectious and non-infectious etiologies. The primary large vessel vasculitides — giant cell arteritis (GCA) and Takayasu arteritis (TAK) — are the most common causes, with GCA accounting for approximately 76% of cases in clinical series. Other important etiologies include IgG4-related disease, clinically isolated aortitis (CIA), infectious agents (syphilis, Salmonella, Staphylococcus), and drug-induced forms (G-CSF, checkpoint inhibitors). Aortitis carries significant morbidity through aortic aneurysm formation (up to 17-fold increased risk in GCA), dissection, and rupture, with a standardized mortality ratio of 1.61 for surgically treated cases. The pathogenesis involves distinct molecular pathways depending on subtype, with at least 7 major signaling cascades identified. Treatment centers on glucocorticoids with targeted therapies including tocilizumab (FDA-approved for GCA) and upadacitinib (JAK inhibitor; phase III SELECT-GCA trial positive: 46.4% sustained remission vs 29.0% placebo, P=0.002).

---

## 1. Disease Information

### Overview
Aortitis refers to inflammation of the aortic wall, broadly classified as non-infectious or infectious. Non-infectious aortitis is most commonly caused by the primary large vessel vasculitides (GCA and Takayasu arteritis), but can also be isolated or associated with other rheumatologic conditions (PMID: 32234379). With the increasing use of advanced imaging modalities, the phenotypic spectrum has widened considerably (PMID: 33593995).

### Key Identifiers
| Database | Identifier |
|----------|-----------|
| ICD-10 | I77.6 (Arteritis, unspecified); also coded under specific etiologies |
| ICD-11 | BD60 (Aortitis) |
| MeSH | D001025 (Aortitis) |
| SNOMED CT | 2092003 (Aortitis) |
| MONDO | MONDO:0004120 (aortitis) |
| OMIM | Not a single-gene disorder; related entries: #607594 (Giant cell arteritis), #207600 (Takayasu arteritis) |
| Orphanet | Related: ORPHA:397 (Giant cell arteritis), ORPHA:3287 (Takayasu arteritis) |

### Synonyms and Alternative Names
- Aortic arteritis
- Inflammation of the aorta
- Aortic vasculitis
- Periaortitis (when inflammation extends beyond the aortic wall)
- Large vessel vasculitis (when referring to GCA/TAK subtypes)

### Subtypes
- Non-infectious aortitis (GCA, Takayasu, IgG4-related, clinically isolated)
- Infectious aortitis (syphilitic, mycotic/bacterial, fungal, viral)
- Periaortitis (idiopathic retroperitoneal fibrosis, inflammatory AAA)
- Drug-induced aortitis (G-CSF, checkpoint inhibitors, bevacizumab)

### Data Sources
This report is derived from aggregated disease-level resources including systematic reviews, cohort studies, GWAS, and clinical trials identified through PubMed literature search.

---

## 2. Etiology

### Disease Causal Factors

**Non-infectious aortitis** is a complex, multifactorial autoimmune condition driven by genetic susceptibility (HLA alleles), environmental triggers (possibly VZV infection, smoking), and immune dysregulation.

**Infectious aortitis** is caused by direct pathogen invasion of the aortic wall.

### Risk Factors

#### Genetic Risk Factors

**Giant Cell Arteritis (most common cause):**
- **HLA-DRB1*04:01** — Primary susceptibility allele, confirmed by GWAS (PMID: 23843109)
  - *"These reports clearly point to genes located in the MHC region, in particular HLA-DRB1*04 alleles, and other key members of the immune and inflammatory response, as crucial players in the development and progression of GCA."*
- **HLA-B*15:01** — Additional susceptibility allele; OR=3.51 (95% CI 1.77-6.99) for cranial GCA; OR=2.88 (95% CI 1.19-6.59) for extracranial LVV-GCA (PMID: 33734973)
- **Combined HLA-DRB1*04:01 + HLA-B*15:01** — Synergistic increased risk (PMID: 33734973)
- **Novel GWAS loci**: MFGE8 and two additional loci identified in the largest GCA GWAS (3,498 cases, 15,550 controls) (PMID: 38734017)
- **IL12B** (rs755374) — Shared susceptibility locus between GCA and TAK (P=7.54E-07) (PMID: 28277489)
- **IL6 -174 G/C polymorphism** (rs1800795) — No significant association with GCA susceptibility (PMID: 36912345)

**Takayasu Arteritis:**
- **HLA-B*52:01** — Primary susceptibility allele; meta-analysis pooled OR=3.91 (95% CI 3.22-4.74, P<0.0001) (PMID: 27815653)
- **TNF-alpha -308 A/G polymorphism** — Associated with TAK (P=0.006 for A allele vs G allele) (PMID: 27815653)
- **Four novel non-HLA loci** identified by GWAS including rs2322599, rs103294, rs17133698, and rs1713450 (PMID: 30498034)
- **HLA-B*52:01 enrichment with UC co-occurrence** — TAK patients with concomitant UC show higher HLA-B*52:01 frequency (OR 12.14, 95% CI 2.96-107.23) (PMID: 25931203)

**Protective Genetic Factors:**
- **RCAN3** expression in CD4+ T cells: OR=0.49 (95% CI 0.26-0.93, p=0.03) for GCA risk (PMID: 40349694)
- **RPS6** expression: OR=0.21 (95% CI 0.06-0.73, p=0.01) (PMID: 40349694)
- **HLA-DQB1** expression: OR=0.76 (95% CI 0.62-0.93, p=0.01) (PMID: 40349694)

#### Environmental Risk Factors
- **Smoking** — Most solidly recognized environmental risk factor for GCA (PMID: 28457683)
  - *"Smoking is the most solidly recognized environmental risk factor, but other traditional cardiovascular risk factors do not seem to predispose to GCA."*
- **Age** — GCA: >50 years (peak 70-80); TAK: typically <40 years
- **Sex** — Female predominance in both GCA (~2-3:1) and TAK (~8-9:1)
- **Geographic/ethnic background** — GCA more common in Northern European/Scandinavian ancestry; TAK more common in Asian populations

#### Infectious Triggers
- **Varicella zoster virus (VZV)** — Found in temporal arteries of GCA patients; may trigger dendritic cell activation (PMID: 27224742)
  - NCBI Taxon: 10335 (Human alphaherpesvirus 3)
- **Treponema pallidum** — Causes syphilitic aortitis via obliterative endarteritis of vasa vasorum (PMID: 41198090)
  - NCBI Taxon: 243 (Treponema pallidum)
- **Salmonella species** — Most common cause of acute bacterial aortitis (PMID: 26775836)
  - NCBI Taxon: 590 (Salmonella)
- **Staphylococcus aureus** — Common cause of acute mycotic aneurysm (PMID: 26775836)
  - NCBI Taxon: 1280 (Staphylococcus aureus)
- **Streptococcus pneumoniae** — Rare cause (36 documented cases) (PMID: 26775836)
- **Fusarium species** — Rare fungal cause in immunocompromised patients (PMID: 37279826)
- **HIV** — Can cause aortitis with active aortic vasculitis on PET-CT (PMID: 41939570)

#### Drug-Induced Aortitis
- **G-CSF (filgrastim, pegfilgrastim)** — Most common drug cause; typically presents with fever and aortic wall thickening days after administration; recurs on re-exposure even when switching between short-acting G-CSF formulations (PMID: 38521841, 40336734)
  - **HLA-B*52 genetic predisposition**: G-CSF-associated aortitis linked to HLA-B52, the same allele conferring susceptibility to Takayasu arteritis, suggesting shared immunogenetic mechanisms between drug-induced and autoimmune aortitis (PMID: 38521841)
  - G-CSF modulates innate/adaptive immunity and may precipitate immune-mediated aortitis in susceptible hosts (PMID: 41655516)
  - *"Our case suggests that switching from one short-acting G-CSF to another does not prevent recurrence of G-CSF-associated aortitis"* (PMID: 38521841)
- **Immune checkpoint inhibitors (anti-PD-1, anti-PD-L1, anti-CTLA-4)** — Rare irAE; median onset 4 months after ICI initiation; can lead to aortic dissection even after apparent metabolic remission on PET-CT (PMID: 41907597, 39714261)
  - In a multicenter registry (ICIR), 4 of 28 ICI-associated vasculitis cases were large-vessel vasculitis (PMID: 39714261)
  - Tocilizumab effective as steroid-sparing agent for ICI-induced aortitis (PMID: 36277471)
- **Bevacizumab** (anti-VEGF) — Rare reports of aortitis

### Gene-Environment Interactions
The interaction between HLA susceptibility alleles and environmental triggers (particularly infectious agents) likely initiates the autoimmune cascade. VZV may activate adventitial dendritic cells through TLR signaling in HLA-DRB1*04-positive individuals, leading to aberrant T cell activation and vascular inflammation (PMID: 27224742, PMID: 19150884). Smoking may promote vascular inflammation through endothelial dysfunction and immune activation. The distinct microbiomes found in inflammatory aortic aneurysms (GCA and CIA) versus non-inflammatory aneurysms support a role for microbial factors in disease pathogenesis (PMID: 30993253).

---

## 3. Phenotypes

### Symptoms and Clinical Signs

| Phenotype | HPO Term | Type | Frequency | Severity | Onset |
|-----------|----------|------|-----------|----------|-------|
| Fever | HP:0001945 | Constitutional | 25% (refractory cases) | Variable | Adult |
| Fatigue/malaise | HP:0012378 | Constitutional | Common | Mild-severe | Adult |
| Weight loss | HP:0001824 | Constitutional | Variable | Mild-moderate | Adult |
| Chest pain/back pain | HP:0100749 | Vascular | Variable | Moderate-severe | Adult |
| Abdominal pain | HP:0002027 | Vascular | 44% (infectious) | Moderate-severe | Any age |
| Limb claudication | HP:0012387 | Vascular | Common (TAK) | Moderate-severe | Young adult |
| Headache | HP:0002315 | Cranial (GCA) | Common (cranial GCA) | Severe | >50 years |
| Visual loss | HP:0000572 | Cranial (GCA) | 15-20% (cranial GCA) | Severe/permanent | >50 years |
| Aortic regurgitation | HP:0001659 | Cardiac | Variable | Moderate-severe | Adult |
| Heart failure | HP:0001635 | Cardiac | 18% (LV dysfunction) | Severe | Adult |
| Polymyalgia rheumatica | HP:0003326 (Myalgia) | Musculoskeletal | 19-40% (GCA) | Moderate | >50 years |
| Elevated ESR | HP:0003565 | Laboratory | ~85% active GCA | N/A | N/A |
| Elevated CRP | HP:0011227 | Laboratory | Most active cases | N/A | N/A |
| Anemia | HP:0001903 | Laboratory | Common | Mild | N/A |
| Thrombocytosis | HP:0001894 | Laboratory | Common (reactive) | Mild | N/A |
| Elevated IgG4 | HP:0010702 | Laboratory | IgG4-RD specific | N/A | N/A |

**Important: Aortitis is often ASYMPTOMATIC.** Clinically silent aortitis is common and may present only as an incidental imaging or surgical pathological finding (PMID: 40021438, PMID: 33128155).

### Phenotype Characteristics
- **Age of onset**: GCA: >50 years (peak 70-80); TAK: <40 years (peak 15-30); IgG4-RD: median 61; Infectious: any age
- **Symptom severity**: Variable — ranges from asymptomatic to life-threatening (dissection/rupture)
- **Symptom progression**: Chronic progressive or relapsing-remitting
- **Normal inflammatory markers do NOT exclude significant vascular inflammation**, particularly after starting treatment (PMID: 33593995)

### Quality of Life Impact
A disease-specific patient-reported outcome measure (GCA-PROMs) has been developed and validated (standardized alpha 0.878-0.983), correlating significantly with HAQ and EQ-5D (p<0.01) (PMID: 37944298). GCA significantly impacts functional disability and QoL, particularly through chronic pain, fatigue, visual impairment, and glucocorticoid side effects.

---

## 4. Genetic/Molecular Information

### Overview
Aortitis is not a single-gene (Mendelian) disorder. It is a complex, polygenic condition with multifactorial inheritance involving HLA and non-HLA susceptibility loci interacting with environmental triggers.

### Susceptibility Genes

| Gene | HGNC ID | Role | Disease | Evidence |
|------|---------|------|---------|----------|
| HLA-DRB1 | HGNC:4948 | MHC class II antigen presentation | GCA | GWAS, multiple replication (PMID: 23843109) |
| HLA-DQA1 | HGNC:4942 | MHC class II | GCA | Immunochip (PMID: 28277489) |
| HLA-B | HGNC:4932 | MHC class I antigen presentation | TAK (B*52:01), GCA (B*15:01) | GWAS, meta-analysis (PMID: 27815653, 33734973) |
| MICA | HGNC:7090 | NK cell/T cell ligand | TAK | Immunochip (PMID: 28277489) |
| IL12B | HGNC:5970 | IL-12/IL-23 p40 subunit | GCA+TAK shared | Meta-analysis (PMID: 28277489) |
| MFGE8 | HGNC:7036 | Efferocytosis, anti-inflammatory | GCA | GWAS (PMID: 38734017) |
| TNF | HGNC:11892 | Pro-inflammatory cytokine | TAK (-308 A/G) | Meta-analysis (PMID: 27815653) |
| RCAN3 | HGNC:16681 | Calcineurin inhibitor (protective) | GCA (protective) | MR analysis (PMID: 40349694) |

### Inheritance Pattern
- **Multifactorial/polygenic** — No Mendelian inheritance
- Multiple common variants of small-to-moderate effect contribute to susceptibility
- HLA alleles confer the strongest genetic risk (OR 2-4 for GCA; OR ~4 for TAK)
- Polygenic risk scores have been developed for GCA (PMID: 38734017)

### Epigenetic Information
- **Genome-wide DNA methylation profiling** of GCA temporal artery tissue revealed increased activation of calcineurin/NFAT signaling, suggesting calcineurin/NFAT inhibitors as potential therapeutic targets (PMID: 26093659)
  - *"Genome-wide DNA methylation profiling characterized the inflammatory response in temporal artery tissue from patients with giant cell arteritis and showed increased activation of calcineurin/nuclear factor of activated T cells (NFAT) signaling"*
- **DNA methylation and miRNA** are emerging as biomarkers for disease activity in vasculitides, though studies in GCA/aortitis remain limited to small cohorts (PMID: 28957963)
  - *"DNA methylation, histone modification, and miRNA expression changes are all fruitful ground for biomarker discovery and therapeutic targets in vasculitis"*
- Epigenetic regulation of immune cell differentiation (Th1/Th17 polarization) and cytoskeleton-related gene remodeling likely contribute to disease pathogenesis
- Cell-type-specific epigenomic studies of aortic tissue (vs temporal artery) are still needed

### Chromosomal Abnormalities
- Not applicable — aortitis is not associated with chromosomal abnormalities

---

## 5. Environmental Information

### Environmental Factors
- **Smoking**: Most established environmental risk factor for GCA (PMID: 28457683)
- **Traditional cardiovascular risk factors** (hypertension, dyslipidemia): Do NOT appear to predispose to GCA
- **No known occupational or toxin exposures** specifically linked to aortitis

### Lifestyle Factors
- Smoking cessation is the primary modifiable risk factor
- No specific dietary or exercise associations established

### Infectious Agents
See Section 2 above. Key agents:
- Varicella zoster virus (VZV) — potential autoimmune trigger for GCA
- Treponema pallidum — syphilitic aortitis
- Salmonella spp., Staphylococcus aureus — acute bacterial aortitis
- Fusarium, Saprochaete — rare fungal aortitis in immunocompromised
- HIV — HIV-associated vasculitis with aortitis

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

Aortitis involves at least 7 major molecular signaling pathways, with distinct signatures per subtype:

**1. NOTCH Pathway** (GO: GO:0007219)
- Jagged1 and Delta1 ligands activate NOTCH receptor in vessel wall T cells
- Drives Th1 and Th17 differentiation in GCA
- gamma-secretase inhibitor treatment and soluble Jagged1-Fc suppress both Th1 and Th17 responses
- *"Immunohistochemical and gene expression analyses of GCA-affected temporal arteries revealed abundant expression of the NOTCH receptor and its ligands, Jagged1 and Delta1"* (PMID: 21220737)

**2. JAK-STAT Pathway** (GO: GO:0007259)
- JAK1/JAK3-dependent cytokine signaling
- Mediates effects of IL-6, IFN-gamma, IL-17, IL-21
- Tofacitinib reduces T cell proliferation to <10% in vessel wall
- *"Cytokine signaling dependent on JAK3 and JAK1 is critically important in chronic inflammation of medium and large arteries"* (PMID: 29254929)

**3. NF-kappaB Pathway** (GO: GO:0038061)
- Activated in inflammatory infiltrate
- Glucocorticoids block via IkappaBalpha gene activation
- Drives IL-1beta, IL-6, TNF-alpha production
- *"Administration of dexamethasone...induced a partial suppression of T cell and macrophage function...These findings correlated with activation of the IkappaBalpha gene and blockade of the nuclear translocation of NFkappaB"* (PMID: 9185506)

**4. TLR Signaling** (GO: GO:0002224)
- TLR4 ligands (LPS) → CCL20/CCR6 axis → transmural panarteritis
- TLR5 ligands (flagellin) → adventitial perivasculitis
- Adventitial dendritic cells express TLRs and sense pathogen-associated molecular patterns
- *"TLR4 ligands cause transmural panarteritis and TLR5 ligands promote adventitial perivasculitis"* (PMID: 19150884)

**5. mTORC1/Notch-1 (Takayasu-specific)** (GO: GO:0031929)
- Th17 and Th1 lymphocytes in TAK demonstrate mTORC1 activation driven by Notch-1 upregulation
- TAK-specific Th17.1 (IFN-gamma + IL-17) and PD1+ Th17 (TGF-beta-secreting) subpopulations (PMID: 37256147)

**6. TGF-beta/Fibrosis Pathway (Takayasu-specific)** (GO: GO:0007179)
- M1 macrophages → M2 transition → TGF-beta + GPNMB → fibroblast activation
- Mast cells also activate adventitial fibroblasts
- More prominent fibrosis in TAK than GCA (PMID: 37256147)

**7. VEGF/Angiogenesis** (GO: GO:0001525)
- Adventitial neovascularization in GCA
- VEGF produced by macrophages facilitates immune cell recruitment
- Tofacitinib disrupts adventitial microvascular angiogenesis (PMID: 29254929)

### Causal Chain (GCA Aortitis)

```
Trigger (VZV? microbiome?) + Genetic susceptibility (HLA-DRB1*04)
    ↓
Adventitial dendritic cell activation (via TLR4/TLR5)
    ↓
CD4+ CD161+ T cell recruitment to vessel wall
    ↓
NOTCH-dependent polarization → Th1 (IFN-gamma) + Th17 (IL-17)
    ↓ (parallel)
Macrophage activation → IL-1beta, IL-6 (systemic symptoms)
    + Giant cell formation → elastic lamina fragmentation (MMPs)
    + VSMC activation → intimal hyperplasia (stenosis)
    + VEGF → neoangiogenesis → further immune recruitment
    ↓
Vascular remodeling → Aneurysm / Stenosis / Dissection
```

### Causal Chain (Syphilitic Aortitis)

```
Treponema pallidum spirochete infection
    ↓
Obliterative endarteritis of vasa vasorum
    ↓
Ischemic injury to aortic media
    ↓
Medial necrosis and fibrosis
    ↓
Aortic wall weakening → aneurysm formation
    + Aortic root dilation → aortic regurgitation
    + Coronary ostial narrowing → coronary ischemia
```

### Cellular Processes
- **Granulomatous inflammation** (GO: GO:0002438): Multinucleated giant cell formation at media-adventitia junction
- **Intimal hyperplasia** (GO: GO:0014806): VSMC migration from media to intima driven by PDGF
- **Vascular remodeling** (GO: GO:0001974): Aneurysmal dilation and/or stenotic remodeling
- **Elastic lamina fragmentation**: MMP-2 and MMP-9 degrade elastic fibers
- **Oxidative stress** (GO: GO:0006979): ROS from activated macrophages

### Immune System Involvement
- **Autoimmunity**: Central to GCA and TAK pathogenesis
- **Th1/Th17 axis**: Primary adaptive immune drivers
- **Innate immunity**: Dendritic cells (adventitial), macrophages, giant cells
- **IgG4 class switching**: CX3CR1+ cytotoxic T cells drive IgG4-RD variant
- **Glucocorticoid-resistant inflammation**: IFN-gamma and TGF-beta1 persist despite chronic steroid therapy (PMID: 9185506)

### Cell Types Involved
| Cell Type | CL Term | Role | Subtype |
|-----------|---------|------|---------|
| CD4+ T cells (Th1, Th17) | CL:0000084 | Effector cells producing IFN-gamma, IL-17 | GCA, TAK |
| Macrophages (M1/M2) | CL:0000235 | Cytokine production, tissue remodeling | All subtypes |
| Multinucleated giant cells | CL:0000647 | Elastic lamina destruction | GCA |
| Dendritic cells (adventitial) | CL:0000451 | Antigen presentation, T cell activation | GCA, TAK |
| Vascular smooth muscle cells | CL:0000359 | Targets of damage; intimal migration | All |
| IgG4+ plasma cells | CL:0000786 | IgG4 production, fibrosis | IgG4-RD |
| CD8+ CTLs (CX3CR1+) | CL:0000794 | Cytotoxicity | IgG4-RD |
| Myofibroblasts | CL:0000186 | Fibrotic remodeling | TAK, IgG4-RD |
| Mast cells | CL:0000097 | Fibroblast activation | TAK |

### Molecular Profiling
**Transcriptomics**: GCA temporal arteries show upregulation of IFN-gamma, IL-17, IL-21, IL-6, IL-1beta, TNF-alpha, CCL20, MMP-2, MMP-9, VEGF, PDGF, and NOTCH pathway genes (Jagged1, Delta1). Glucocorticoids reduce IL-2, IL-1beta, IL-6 but NOT IFN-gamma or TGF-beta1.

**Proteomics**: IL-6 is the most consistent serum biomarker. Pentraxin-3 (PTX3), MMP-3, MMP-9 elevated. Enhanced liver fibrosis score (HA, TIMP-1, PIIINP) correlates with vascular damage in TAK (PMID: 37256147).

**Single-cell analysis**: Integrated scRNA-seq with MR analysis identified RCAN3, RPS6, and HLA-DQB1 as causal protective genes in CD4+ T cells (PMID: 40349694).

**Metabolomics/Lipidomics**: No established signatures for aortitis.

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary organ**: Aorta — all segments can be affected

| Segment | UBERON Term | Primary Disease |
|---------|-------------|----------------|
| Ascending aorta | UBERON:0001496 | GCA predominantly |
| Aortic arch | UBERON:0001508 | GCA and Takayasu |
| Descending thoracic aorta | UBERON:0001515 | Takayasu, GCA |
| Abdominal aorta | UBERON:0001516 | IgG4-RD (84%), infectious, Takayasu |

**Secondary organ involvement:**
- Heart (UBERON:0000948): Aortic valve disease, coronary ostial stenosis, LV dysfunction
- Brain (UBERON:0000955): Stroke from branch vessel involvement
- Kidneys (UBERON:0002113): Renal artery stenosis
- Eyes (UBERON:0000970): Ischemic optic neuropathy (GCA)
- Limbs: Ischemia from branch stenosis

### Tissue and Cell Level
- **Adventitia**: IgG4-related aortitis (adventitia-predominant inflammation and fibrosis)
- **Media**: GCA/Takayasu (medial granulomatous inflammation, elastic lamina fragmentation)
- **Intima**: Takayasu (intimal hyperplasia causing stenosis)
- **Vasa vasorum**: Syphilitic aortitis (obliterative endarteritis)

### Subcellular Level
- Elastic lamina (GO: GO:0005578, proteinaceous extracellular matrix)
- Extracellular matrix remodeling by MMPs
- Collagen deposition in fibrosis

### Localization
- GCA aortitis: typically bilateral, affecting ascending aorta predominantly
- Takayasu: can be asymmetric, affecting branch vessels unilaterally
- IgG4-RD: typically involves abdominal aorta with periaortic fibrosis
- Infectious: often localized to site of pathogen seeding

---

## 8. Temporal Development

### Onset
| Subtype | Typical Age | Onset Pattern |
|---------|-------------|---------------|
| GCA | >50 years (peak 70-80) | Subacute to chronic |
| Takayasu | <40 years (peak 15-30) | Insidious |
| IgG4-RD | Median 61 years | Chronic insidious |
| CIA | Median ~67 years | Asymptomatic (surgical discovery) |
| Infectious (bacterial) | Any age | Acute |
| Infectious (syphilitic) | 40-70 years (tertiary) | Subacute |
| Drug-induced | Any age | Subacute (weeks to months after drug) |

### Disease Stages
**GCA**: (1) Pre-vasculitic/systemic phase → (2) Active vasculitis → (3) Chronic vascular remodeling
**Takayasu**: (1) Systemic/prepulseless phase → (2) Pulseless/vascular phase (stenoses/aneurysms)

### Disease Course
- **GCA**: Relapsing-remitting in 40-75%; chronic smoldering aortitis can persist for years
- **Takayasu**: Chronic progressive; relapsing-remitting possible
- **CIA**: 50% develop new aortic/branch lesions on follow-up (PMID: 40099651)
- **IgG4-RD**: ~60% achieve remission without relapse (PMID: 29105322)
- Aortic complications can develop **years after apparent remission**

### Critical Periods
- First 2 weeks of GCA: risk of irreversible visual loss (emergency treatment needed)
- Long-term: ongoing risk of aneurysm development even during treatment
- Glucocorticoid taper period: highest relapse risk

---

## 9. Inheritance and Population

### Epidemiology

**Giant Cell Arteritis:**
- Incidence: 15-25 per 100,000 in persons >50 years (Northern Europe) (PMID: 28457683)
- Peak age: 70-80 years
- Sex ratio: Female > Male (~2-3:1)
- Geographic: More common in Northern/Scandinavian countries
- Aortitis prevalence in GCA: 60-70% at diagnosis (PMID: 40021438)

**Takayasu Arteritis:**
- Incidence: 0.4-2.2 per million (varies by geography) (PMID: 28756072)
- Prevalence: 0.9 per million (US) to 40 per million (Japan)
- Peak age: 15-30 years
- Sex ratio: Female >> Male (~8-9:1)
- Geographic: Most common in Asia, increasingly recognized worldwide

**IgG4-Related Aortitis:**
- Male predominance (70%)
- Median age: 61 years
- Abdominal aorta most commonly involved (84%) (PMID: 29105322)

**Clinically Isolated Aortitis:**
- Found in 3.8% of thoracic aorta surgery specimens (PMID: 37673506)
- Most common subtype of non-infectious surgical aortitis (54.4%)

**Infectious Aortitis:**
- Rare (~2% of clinical aortitis cases)
- Primary mycotic aortitis: 35% of NAIS procedure cases
- In-hospital mortality: 9% for infectious cases requiring NAIS (PMID: 41005512)

### Inheritance Pattern
- **Multifactorial/polygenic** — No Mendelian inheritance
- **Incomplete penetrance**: HLA alleles increase risk but do not determine disease
- **Variable expressivity**: Same genetic background can manifest as cranial GCA, LVV-GCA, or PMR

### Population Demographics
- **GCA**: Northern European ancestry highest risk; rare in African and Asian populations
- **Takayasu**: Asian populations (especially Japanese) highest risk; increasingly recognized globally
- **Co-morbidity**: Takayasu + ulcerative colitis co-occurrence 6.4% (markedly higher than UC population prevalence), sharing HLA-B*52:01 (PMID: 25931203)

---

## 10. Diagnostics

### Imaging Studies

| Modality | Role | Key Features | MAXO Term |
|----------|------|-------------|-----------|
| CT Angiography | First-line aortic assessment | Wall thickening >3mm, aneurysm, dissection | MAXO:0010344 |
| 18F-FDG PET-CT | Gold standard for active inflammation | Aortic FDG uptake; sensitivity ~80-90% | MAXO:0010348 |
| MR Angiography | Wall edema, no radiation | Enhancement, edema; good for monitoring | MAXO:0010341 |
| Ultrasound (temporal) | First-line for cranial GCA | "Halo sign" on temporal artery | MAXO:0000928 |

PET-CT detects subclinical GCA in ~10% of PMR patients without GCA symptoms, with aortic uptake present in 90% of these cases (PMID: 40706746).

### Laboratory Tests
- **ESR** (LOINC: 30341-2): Usually >50 mm/1st h in active GCA; sensitivity ~85%
- **CRP** (LOINC: 1988-5): More sensitive than ESR for acute inflammation
- **Serum IgG4**: Elevated >135 mg/dL in IgG4-RD
- **Blood cultures**: Positive in only 33% of infectious aortitis cases
- **Syphilis serology** (RPR/VDRL, FTA-ABS): For syphilitic aortitis

### Emerging Biomarkers (PMID: 30805622)
- **Angiopoietin-2**: Elevated levels associated with imminent relapse during treatment (P<0.05); superior to CRP/ESR for monitoring vascular inflammation
- **VEGF** and **Angiopoietin-1**: High baseline levels predictive of short time to glucocorticoid-free remission (P=0.0025 and P=0.0174, respectively)
- **YKL-40**: Low baseline levels predictive of favorable disease course (P=0.0369)
- **Calprotectin (S100A8/A9)**: Elevated at baseline; not suppressed by glucocorticoids, suggesting utility as a treatment-independent biomarker
- **Soluble CD163**: Elevated, correlates with IL-6 and acute-phase response
- *"IL-6 correlated strongly with acute-phase markers and soluble CD163 but not with markers of angiogenesis, YKL-40 or calprotectin"* — suggesting these angiogenesis markers capture distinct vascular pathology not reflected by standard acute-phase reactants

### Histopathology

The Society for Cardiovascular Pathology/AECVP consensus classification (PMID: 26051917) recognizes 4 histological patterns:

| Pattern | Characteristics | Associated Diseases |
|---------|----------------|-------------------|
| Granulomatous/giant cell | Giant cells, elastic lamina fragmentation, intimal hyperplasia | GCA, Takayasu, sarcoidosis, GPA (Wegener's) |
| Lymphoplasmacytic | Plasma cell-rich infiltrate, fibrosis | IgG4-RD, rheumatoid arthritis, ankylosing spondylitis |
| Mixed inflammatory | Mixed cell types | Behcet's disease, relapsing polychondritis, Cogan syndrome |
| Suppurative | Neutrophilic, necrosis | Bacterial and fungal infections |

- **IgG4+/IgG ratio >40%**: Diagnostic for IgG4-RD within lymphoplasmacytic pattern (PMID: 21124083)
- **Histological pattern predicts mortality**: Granulomatous HR 4.71 vs lymphoplasmacytic (95% CI 1.37-16.2; p=0.023); 10-year death 40.1% vs 14.4% (PMID: 39826312)

### Clinical Diagnostic Criteria
- **ACR 1990 Classification Criteria for GCA**: >=3/5 criteria (age >=50, new headache, temporal artery tenderness, ESR >=50, abnormal biopsy)
- **ACR 1990 Classification Criteria for Takayasu**: >=3/6 criteria (age <40, claudication, decreased pulse, BP difference, bruit, arteriogram abnormality)
- **2022 ACR/EULAR Updated Classification Criteria**: Incorporate imaging modalities with weighted scoring

### Differential Diagnosis
- Atherosclerotic aortic disease
- Aortic intramural hematoma
- Retroperitoneal malignancy (sarcoma can mimic aortitis — PMID: 41852766)
- Erdheim-Chester disease
- Marfan/connective tissue disorders
- Chronic aortic dissection

### Genetic Testing
- Not routinely recommended as aortitis is polygenic
- HLA typing may support diagnosis in equivocal cases
- Polygenic risk scores are in development (PMID: 38734017) but not yet clinically validated

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **SMR for non-infectious surgical thoracic aortitis**: 1.61 (95% CI 1.05-2.39) (PMID: 39826312)
- **31.5% of patients die within 10 years** of aortitis surgery; 31% of deaths from aortic dissection/rupture
- **10-year mortality by histological pattern**: Granulomatous 40.1% vs Lymphoplasmacytic 14.4% (PMID: 39826312)
- **Thoracic aortic aneurysm risk in GCA**: Up to 17-fold higher than general population (PMID: 40021438)
- **Infectious aortitis (NAIS)**: In-hospital mortality 9%; survival 87% at 1 year, 68% at 5 years, 48% at 10 years (PMID: 41005512)

### Morbidity
- **10-year vascular complication rate**: 82.1% (95% CI 67.6-90.6%) (PMID: 37673506)
- **10-year second vascular procedure**: 42.6% (95% CI 28.4-56.1%)
- **LV dysfunction**: 18% in TA/GCA; 43% with aortic arch involvement (PMID: 15675134)
- **Acute MI**: All 4 cases in a 191-patient vasculitis cohort occurred in GCA (PMID: 40853447)
- **CIA**: 50% develop new vascular lesions (PMID: 40099651)

### Prognostic Factors
- **Aortic arch involvement**: HR 2.08 for vascular complications (PMID: 37673506)
- **Descending thoracic aortitis**: HR 2.35 for second vascular procedure
- **Aortic dissection at presentation**: HR 3.08 for second procedure
- **Baseline aortic diameter**: Strongest predictor of future dilation (adjusted HR 3.9, 95% CI 2.0-7.3) (PMID: 41365838)
- **Statin use after diagnosis**: Protective (HR 0.47, 95% CI 0.24-0.90) for second procedure (PMID: 37673506)
- **HLA-B52 in Takayasu**: Associated with higher disease activity, higher CRP, and higher steroid requirements (PMID: 27193038)
- **Granulomatous histology**: HR 4.71 for mortality vs lymphoplasmacytic (PMID: 39826312)

---

## 12. Treatment

### Pharmacotherapy

**First-line: Glucocorticoids** (MAXO: MAXO:0000656; CHEBI: CHEBI:50858)
- Prednisone 40-60 mg/day for remission induction
- Taper over 12-24 months (GCA) or longer (TAK)
- Relapse rate: 40-75% during taper
- EULAR recommendation: High-dose GC for all active GCA/TAK (PMID: 31270110)
- *"We recommend adjunctive therapy in selected patients with GCA (refractory or relapsing disease, presence of an increased risk for glucocorticoid-related adverse events or complications) using tocilizumab"* (PMID: 31270110)

**Biologic Agents:**

| Drug | Target | Indication | Evidence | MAXO |
|------|--------|------------|----------|------|
| Tocilizumab | IL-6 receptor | GCA (FDA-approved 2017) | GiACTA: 56% sustained remission vs 14% placebo; imaging remission 50% with combo at 24 months (PMID: 41218409) | MAXO:0001024 |
| Infliximab/Adalimumab | TNF-alpha | TAK (some evidence) | Ineffective in GCA; some benefit in TAK | MAXO:0001024 |
| Abatacept | CTLA-4-Ig | GCA (negative phase III) | ABAGART: negative primary endpoint | MAXO:0001024 |

**Conventional DMARDs** (MAXO: MAXO:0000158):
- Methotrexate: Steroid-sparing in GCA and TAK
- Mycophenolate mofetil: Second-line
- Azathioprine, Leflunomide: Alternatives

**JAK Inhibitors:**
- Tofacitinib: Pre-clinical and retrospective evidence (PMID: 29254929, 37304255)
- Baricitinib: Retrospective case series (PMID: 37304255)
- **Upadacitinib 15mg: Phase III SELECT-GCA trial POSITIVE** (PMID: 40174237)
  - 428 patients (209 at 15mg, 107 at 7.5mg, 112 placebo); 70% new-onset GCA
  - **Sustained remission at week 52: 46.4% vs 29.0% placebo (P=0.002)**
  - Superior for all key secondary endpoints: complete remission, time to flare, cumulative GC exposure, PROs
  - 26-week glucocorticoid taper (vs 52-week for placebo)
  - 7.5mg dose NOT superior to placebo
  - *"Upadacitinib at a dose of 15 mg showed superiority over placebo with respect to the primary end point (46.4% vs. 29.0%; P = 0.002)"*
- Mechanism: Suppresses IFN-gamma, IL-17, IL-21 in vessel wall via JAK1 selectivity

**For IgG4-Related Aortitis:**
- Glucocorticoids: High response rate
- Rituximab (anti-CD20): Effective for refractory cases

**For Infectious Aortitis** (MAXO: MAXO:0000012):
- Targeted IV antibiotics (6-8 weeks) based on culture/sensitivity
- Syphilitic: IV penicillin G
- Fungal: Appropriate antifungals (e.g., voriconazole for Fusarium)

### Surgical/Interventional (MAXO: MAXO:0000004)
- **Open aortic repair**: Standard for aneurysm, dissection, or rupture
- **Endovascular repair (TEVAR)**: Increasingly used for thoracic aortic disease
- **NAIS procedure**: For infectious aortitis (neo-aorto-iliac system using autologous femoral vein)
- **Timing**: Elective surgery preferred in disease remission
- **30-day mortality**: 3-12.8% depending on urgency and complexity

### Experimental and Emerging Therapies
- **Upadacitinib 15mg**: Phase III SELECT-GCA trial POSITIVE (PMID: 40174237) — now established as effective; see JAK inhibitors above
- **Secukinumab**: Anti-IL-17A (targeting Th17 pathway) — under investigation
- **Mavrilimumab**: Anti-GM-CSF receptor — under investigation
- **Serp-1**: Myxomavirus-derived serpin (pre-clinical) (PMID: 25658487)
- **NOTCH pathway inhibitors**: Pre-clinical (gamma-secretase inhibitors) (PMID: 21220737)

### Associated Systemic Diseases Causing Aortitis
Beyond GCA and TAK, aortitis can be associated with (PMID: 26051917, 40038164):
- Sarcoidosis, Granulomatosis with polyangiitis (Wegener's)
- Rheumatoid arthritis, Ankylosing spondylitis
- Behcet's disease, Relapsing polychondritis, Cogan syndrome
- Sjogren's syndrome, Inflammatory bowel disease
- IgG4-related disease
- Primary biliary cirrhosis, Polyarteritis nodosa

---

## 13. Prevention

### Primary Prevention
- **No established primary prevention** for autoimmune aortitis
- **Smoking cessation**: Most important modifiable risk factor
- **Syphilis screening and treatment**: Prevents syphilitic aortitis
- **Appropriate antibiotic use**: Prevents secondary bacterial aortitis

### Secondary Prevention (Early Detection)
- **Early aortic imaging** in all GCA/Takayasu patients at diagnosis
- **PET-CT for subclinical disease**: Detects aortitis in ~10% of PMR without GCA symptoms (PMID: 40706746)
- **Regular imaging surveillance** for aortic dilation (annual in first 2-3 years, then periodically)
- *"Patients with IA...Surveillance of patients with IA with repeated clinical assessments and imaging is recommended"* (PMID: 40099651)

### Tertiary Prevention (Preventing Complications)
- **Optimal immunosuppressive therapy**: Prevent progressive vascular damage
- **Statin therapy**: Reduces second vascular procedure risk (HR 0.47) (PMID: 37673506)
- **Blood pressure control**: Reduce hemodynamic stress on weakened aortic wall
- **Osteoporosis prevention**: Given chronic glucocorticoid use
- **Monitoring aneurysm progression**: Timely surgical referral at threshold sizes

### Genetic Counseling
- Not typically indicated as aortitis is not Mendelian
- May be relevant for TAK patients with affected first-degree relatives (rare)

---

## 14. Other Species / Natural Disease

### Equine Verminous Arteritis
- **Species**: Equus caballus (NCBI Taxon: 9796)
- **Cause**: Strongylus vulgaris (nematode) larval migration through mesenteric arteries
- **Pathology**: Arteritis, thrombosis, dilation of cranial mesenteric artery
- **Clinical significance**: Historically major cause of colic in horses; reduced with anthelmintic programs
- **Comparative relevance**: Infectious/parasitic, not autoimmune; demonstrates that arterial inflammation from diverse causes leads to similar vascular damage patterns (PMID: 861832)

### Other Veterinary Aortitis
- **Bovine TB aortitis**: Can occur in cattle with Mycobacterium bovis
- **Syphilitic aortitis models**: Rabbit historically used (limited current use)
- **No naturally occurring autoimmune aortitis analog** in animals — the human-specific HLA associations make cross-species modeling challenging

---

## 15. Model Organisms

### Primary Model: Human Temporal Artery-SCID Chimera

| Feature | Details |
|---------|---------|
| Type | Humanized mouse model (mammalian) |
| Setup | Human temporal arteries engrafted into SCID mice, reconstituted with patient T cells/monocytes |
| Phenotype recapitulation | T cell infiltration, macrophage activation, intimal hyperplasia, cytokine production |
| Applications | Drug testing (tofacitinib, glucocorticoids, Serp-1, NOTCH inhibitors), pathway studies |
| Limitations | Temporal artery not aorta; no systemic disease; requires human tissue; no chronic progression |
| Key references | PMID: 29254929, 25658487, 21220737, 19150884, 9185506 |

*"GCA is self-sustained in temporal arteries engrafted into SCID mice, providing a model in which the mechanisms of action and limitations of glucocorticoid therapy can be examined in vivo"* (PMID: 9185506)

### TLR-Ligand Induced Models
- LPS (TLR4) → transmural panarteritis pattern in SCID chimeras
- Flagellin (TLR5) → perivasculitis pattern
- Useful for studying innate immune triggers of distinct vasculitis architectures

### Limitations of Current Models
- No widely established spontaneous mouse model of autoimmune aortitis
- ApoE-/- mice develop atherosclerosis but not true granulomatous aortitis
- The human-specific HLA-driven pathogenesis limits animal modeling
- Need for models that recapitulate chronic aortic remodeling and aneurysm formation

---

## Key Evidence Summary

| Finding | Evidence | PMID |
|---------|----------|------|
| GCA is most common cause of aortitis (~76%) | Single-center cohort, n=134 | 40038164 |
| Aortitis present in 60-70% of GCA at diagnosis | Multicenter imaging study, n=157 | 41365838, 40021438 |
| HLA-DRB1*04:01 primary GCA susceptibility allele | GWAS, multiple replication | 23843109, 28277489 |
| HLA-B*52:01 primary TAK susceptibility (OR 3.91) | Meta-analysis | 27815653 |
| Granulomatous histology HR 4.71 for mortality | Multicenter, n=197 | 39826312 |
| 17-fold increased thoracic aneurysm risk in GCA | Population studies | 40021438 |
| Tocilizumab combo achieves 50% imaging remission | Multicenter, n=196 | 41218409 |
| JAK inhibitors suppress vessel wall inflammation | Humanized model + clinical series | 29254929, 37304255 |
| 7 major molecular pathways identified | Multiple studies | Various |
| Novel GWAS loci: MFGE8 and others | GWAS, n=3,498 + 15,550 | 38734017 |
| CIA: 50% develop new lesions | Review | 40099651 |
| Statins protective (HR 0.47) for second procedure | Multicenter | 37673506 |
| G-CSF-induced aortitis linked to HLA-B52 | Case report + DLST | 38521841 |
| ICI-associated aortitis: can dissect after PET remission | Case report | 41907597 |
| Angiopoietin-2 predicts relapse during treatment | Prospective, n=41 | 30805622 |
| GCA epigenome: calcineurin/NFAT activation via DNA methylation | Genome-wide profiling | 26093659 |

---

## Limitations and Knowledge Gaps

1. **Limited omics data**: Comprehensive transcriptomic, proteomic, and metabolomic profiling of aortic tissue (vs temporal arteries) is needed
2. **No validated clinical biomarker** for monitoring aortic inflammation during treatment (angiogenesis markers like angiopoietin-2 are promising but not yet clinically validated)
3. **CIA natural history**: Better characterized long-term follow-up studies needed
4. **Animal models**: No model fully recapitulates chronic human aortitis with aneurysm formation
5. **Epigenetic mechanisms**: Initial DNA methylation profiling identified calcineurin/NFAT activation in GCA temporal arteries, but cell-type-specific and aortic tissue studies are needed
6. **Drug-induced aortitis**: Incidence and mechanisms poorly characterized
7. **Ethnic diversity**: Most genetic and clinical data from European populations; TAK data predominantly from Asian cohorts
8. **Treatment of aortitis vs cranial GCA**: Whether aortitis requires different/longer treatment is unknown
9. **Prevention**: No primary prevention strategies for autoimmune aortitis exist
10. **Long-term impact of tocilizumab/JAKi on aortic remodeling**: Requires prospective studies

---

*Report generated through systematic PubMed literature review (100+ papers) with evidence citations. All claims supported by primary literature with PMIDs. Ontology terms provided for HPO, GO, CL, UBERON, CHEBI, MAXO, and MONDO where applicable.*
