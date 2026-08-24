---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-08T23:05:55.108161'
end_time: '2026-08-08T23:08:39.488618'
duration_seconds: 164.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Toxoplasmosis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  num_turns: 1
  total_cost_usd: 0.929703
  session_id: de2e0829-eea8-5ecc-aeb4-31051b057600
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Toxoplasmosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Toxoplasmosis** covering all of the
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

Toxoplasmosis Comprehensive Research Report

## 1. Disease Information

**Overview:** Toxoplasmosis is a zoonotic parasitic infection caused by the obligate intracellular protozoan *Toxoplasma gondii*, an Apicomplexan parasite. Felids (cats) are the definitive host where the parasite undergoes sexual reproduction in the intestinal epithelium, producing oocysts shed in feces; virtually all warm-blooded animals, including humans, can serve as intermediate hosts. Infection is typically asymptomatic or mild in immunocompetent hosts but causes severe disease in immunocompromised individuals (encephalitis, particularly in AIDS patients) and in congenital transmission (fetal infection following primary maternal infection during pregnancy), producing the classic triad of chorioretinitis, hydrocephalus, and intracranial calcifications.

**Key Identifiers:**
- **MONDO:** MONDO:0005108 (toxoplasmosis); congenital toxoplasmosis: MONDO:0018848
- **OMIM:** 314350 (Toxoplasmosis, Congenital)
- **Orphanet:** ORPHA:857 (Congenital toxoplasmosis)
- **ICD-10:** B58 (Toxoplasmosis); B58.0 (Toxoplasma oculopathy); B58.2 (Toxoplasma meningoencephalitis); P37.1 (Congenital toxoplasmosis)
- **ICD-11:** 1F57 (Toxoplasmosis)
- **MeSH:** D014123 (Toxoplasmosis); D014124 (Toxoplasmosis, Congenital); D014125 (Toxoplasmosis, Cerebral); D014126 (Toxoplasmosis, Ocular); D014128 (Toxoplasmosis, Animal)
- **NCBI Taxon (organism):** NCBITaxon:5811 (*Toxoplasma gondii*)

**Synonyms:** Toxoplasma infection; congenital toxoplasmosis (TORCH infection); cerebral toxoplasmosis; ocular toxoplasmosis; toxoplasmic encephalitis (in AIDS context); "cat scratch fever" is a common lay misnomer/confusion (that is actually *Bartonella henselae*—distinct disease).

**Data source type:** Predominantly aggregated disease-level information from clinical case series, national/international birth cohorts (e.g., the European Multicentre Study on Congenital Toxoplasmosis - EMSCOT), CDC/WHO surveillance, and large epidemiological cohorts, supplemented by individual case reports for rare manifestations (e.g., PMID:15668997, PMID:11224510 for congenital case series).

---

## 2. Etiology

**Disease Causal Factor:** Infection with *Toxoplasma gondii*, an obligate intracellular apicomplexan protozoan parasite with three main infectious stages: tachyzoites (rapidly dividing, acute infection), bradyzoites (encysted in tissue cysts, chronic/latent infection, especially muscle and CNS), and sporozoites (within oocysts shed by cats).

**Risk Factors:**

*Environmental/Behavioral:*
- Consumption of raw or undercooked meat (particularly pork, lamb, venison) containing tissue cysts (PMID:22218351 — Robert-Gangneux & Dardé review notes meat-borne transmission as a major route in industrialized countries)
- Exposure to cat feces / handling litter boxes; soil contact (gardening) containing oocysts
- Contaminated water supplies (waterborne oocyst outbreaks documented, e.g., Brazil, Canada)
- Consumption of unwashed raw fruits/vegetables
- Occupational exposure (farmers, abattoir workers, veterinarians)
- Organ transplantation from seropositive donor to seronegative recipient
- Blood transfusion (rare)
- Geography: higher seroprevalence in regions with warm/humid climates (France, Brazil) vs. cold/dry (Scandinavia)

*Genetic (host susceptibility):*
- HLA associations with severity of congenital and ocular toxoplasmosis — HLA-DQ3 and HLA-B associated with retinochoroiditis risk (PMID:16826765, Peyron et al., identified associations between HLA class II and mental retardation/hydrocephalus severity in congenital toxoplasmosis)
- Polymorphisms in ABCA4, COL2A1 have been implicated in modifying ocular disease severity in some cohorts
- Immunodeficiency (genetic or acquired) — CD4+ T-cell deficiency (AIDS, HIV) is the dominant host risk factor for reactivation of latent infection into toxoplasmic encephalitis

*Parasite strain genotype:*
- Atypical/recombinant strains (particularly in South America) associated with more severe disease, including severe ocular disease in immunocompetent hosts (PMID:16880330 — Type I and atypical genotypes linked to more severe congenital and ocular disease compared to the milder Type II strains dominant in Europe/North America)

**Protective Factors:**
- Pre-conceptional immunity (IgG seropositivity prior to pregnancy) is strongly protective against congenital transmission — established immunity essentially eliminates transmission risk except in profound immunosuppression or reinfection with a different/more virulent strain
- Cooking meat to safe internal temperatures (destroys tissue cysts)
- Freezing meat below -12°C for several days
- Handwashing after soil/litter box contact
- Antiretroviral therapy restoring CD4+ counts >200 cells/µL in HIV-infected individuals dramatically reduces reactivation risk (PMID:11815817 — HAART reduces incidence of toxoplasmic encephalitis)

**Gene-Environment Interactions:** Host genetic background (HLA, immune gene polymorphisms) interacts with environmental parasite exposure and infecting strain genotype to determine clinical outcome. For example, HLA-B*4901 and NALP1/COL2A1 have been implicated (in French and Brazilian cohorts respectively) in modulating risk for severe ocular disease following identical exposure (PMID:21966149 — Jamieson et al. review of host genetics in toxoplasmosis).

---

## 3. Phenotypes

Toxoplasmosis presentation differs markedly by host immune status and timing of infection (congenital vs. acquired). HPO terms suggested below.

### A. Congenital Toxoplasmosis (classic triad + broader spectrum)
| Phenotype | HPO Term | Frequency | Notes |
|---|---|---|---|
| Chorioretinitis | HP:0000585 | ~20-80% (varies by study/screening) | Most common manifestation, may be delayed onset (years after birth) |
| Hydrocephalus | HP:0000238 | ~10-30% of symptomatic cases | Due to aqueductal obstruction from ependymitis |
| Intracranial calcifications | HP:0002514 | Common in symptomatic congenital cases | Periventricular distribution characteristic |
| Microcephaly | HP:0000252 | Variable | |
| Seizures | HP:0001250 | Subset of symptomatic infants | |
| Intellectual disability | HP:0001249 | Long-term sequela in untreated/severe cases | |
| Hepatosplenomegaly | HP:0001433 | Neonatal presentation | |
| Jaundice | HP:0000952 | Neonatal presentation | |
| Thrombocytopenia | HP:0001873 | Neonatal presentation | |
| Sensorineural hearing loss | HP:0000407 | Reported subset | |
| Most infected newborns are asymptomatic at birth | — | ~70-90% asymptomatic at birth (SYROCOT study, PMID:17825405) | Sequelae, especially chorioretinitis, may develop later in childhood |

### B. Acquired Toxoplasmosis in Immunocompetent Hosts
| Phenotype | HPO Term | Frequency |
|---|---|---|
| Asymptomatic infection | — | ~80-90% of immunocompetent adults |
| Lymphadenopathy (cervical) | HP:0002716 | Most common symptomatic presentation |
| Fatigue | HP:0012378 | Common |
| Low-grade fever | HP:0001954 | Common |
| Myalgia | HP:0003326 | Common |
| Mononucleosis-like syndrome | — | Self-limited, resolves in weeks-months |

### C. Ocular Toxoplasmosis
| Phenotype | HPO Term |
|---|---|
| Retinochoroiditis | HP:0100653 (chorioretinal abnormality) / HP:0000585 |
| Vitritis / vitreous inflammation | HP:0025406 (related) |
| Blurred vision | HP:0000622 |
| Scotoma | HP:0000575 (visual impairment, general) |
| Ocular pain | HP:0100543 (eye pain) |

### D. Reactivation/Immunocompromised (Toxoplasmic Encephalitis)
| Phenotype | HPO Term | Notes |
|---|---|---|
| Focal neurologic deficit | HP:0002322 (resistant) — better: HP:0034332 or general focal neurological signs | Hemiparesis, aphasia |
| Altered mental status/confusion | HP:0031466 | |
| Headache | HP:0002315 | |
| Seizures | HP:0001250 | |
| Fever | HP:0001945 | |
| Ring-enhancing brain lesions (imaging) | — | Radiologic, not strictly HPO |

**Onset:** Congenital infection manifests in utero, at birth, or is delayed (asymptomatic at birth with sequelae — especially retinochoroiditis — emerging months to years later, sometimes into the third/fourth decade of life) (PMID:17825405, SYROCOT Study Group — pooled European cohort meta-analysis).

**Severity/Progression:** Highly variable — from entirely asymptomatic lifelong infection to fulminant, fatal disseminated disease in the severely immunocompromised. Ocular disease is characteristically **recurrent/relapsing** (episodic reactivation of quiescent retinal cysts), a hallmark distinguishing feature.

**Quality of life impact:** Ocular disease causes progressive visual impairment/blindness with recurrent flares impacting daily function; congenital neurological sequelae (intellectual disability, seizures) impose lifelong disability burden; toxoplasmic encephalitis in AIDS carries high mortality without treatment.

---

## 4. Genetic/Molecular Information

Toxoplasmosis is an infectious disease, not a classic monogenic disorder, so "causal genes" apply to the **parasite** genome and to **host susceptibility modifier genes**, not to a single Mendelian human locus.

**Parasite Genetics:**
- *T. gondii* has three canonical clonal lineages: Type I, Type II, Type III, plus numerous atypical/recombinant strains especially in South America
- Genotype correlates with virulence: Type I strains are highly virulent in mouse models (LD100 = 1 organism); Type II/III are less virulent
- Key virulence factor genes: **ROP18** (rhoptry kinase, polymorphic virulence determinant, PMID:16709124 — Taylor et al. showed ROP18 as a major virulence determinant via QTL mapping), **ROP5** (pseudokinase, cooperates with ROP18 to inactivate host immunity-related GTPases/IRGs), **GRA15**, **NLRP1/NLRP3 inflammasome interactions**

**Host Susceptibility/Modifier Genes:**
- **HLA-DQ3, HLA-B*4901, HLA-Bw16** — associated with risk of retinochoroiditis and severity of neurological sequelae in congenital toxoplasmosis (PMID:16826765; Mack et al. earlier HLA studies)
- **NALP1 (NLRP1)** — inflammasome gene, polymorphisms associated with congenital toxoplasmosis susceptibility in human cohorts, replicating findings from mouse Nalp1 studies (PMID:19468306 — Witola et al., NALP1 polymorphisms and human congenital toxoplasmosis)
- **P2X7** purinergic receptor gene polymorphisms — implicated in susceptibility to ocular toxoplasmosis in Brazilian cohorts
- **ABCA4, COL2A1** — implicated in modifying severity of retinal involvement in some studies

**Pathogenic Variants:** Not applicable in the classic ClinVar/ACMG sense (this is not a Mendelian disease); host susceptibility variants are typically common polymorphisms (SNPs) studied via candidate-gene and GWAS-style association studies rather than rare pathogenic variants.

**Epigenetic Information:** *T. gondii* infection has been shown to alter host cell epigenetics — the parasite secretes effectors (e.g., TgIST) that modulate host STAT1-dependent transcription and can affect histone modifications in infected cells to suppress interferon-gamma responses (PMID:27300474 — Gay et al., *Toxoplasma gondii* TgIST co-opts host chromatin repressors to block STAT1-dependent gene expression).

**Chromosomal Abnormalities:** Not applicable (infectious, not a chromosomal disorder).

---

## 5. Environmental Information

**Environmental Factors:**
- Soil contaminated with oocysts (can remain infectious for over a year in moist soil)
- Water supply contamination — waterborne outbreaks documented in Canada (Victoria, BC, 1995 — PMID:9366006, Bowie et al.) and Brazil
- Environmental persistence of oocysts is a major reservoir independent of direct cat contact

**Lifestyle Factors:**
- Dietary practices: consumption of raw/undercooked meat, unwashed produce, unpasteurized goat's milk
- Cat ownership and litter box hygiene (though studies show meat consumption is often a larger risk factor than cat ownership in seroprevalence studies)
- Gardening without gloves
- Geographic/cultural dietary practices (e.g., high raw meat consumption in France correlates with higher seroprevalence)

**Infectious Agent:**
- ***Toxoplasma gondii*** (NCBITaxon:5811), Phylum Apicomplexa, family Sarcocystidae
- Definitive host: Felidae (domestic cats and wild felids) — sexual reproduction occurs in intestinal epithelium
- Intermediate hosts: virtually all warm-blooded vertebrates (asexual reproduction; tissue cyst formation)
- Transmission routes: (1) ingestion of oocysts from contaminated soil/water/produce, (2) ingestion of tissue cysts in undercooked meat, (3) congenital (transplacental) transmission, (4) organ transplantation, (5) blood transfusion (rare), (6) laboratory accident

---

## 6. Mechanism / Pathophysiology

**Causal chain overview:** Ingestion of oocysts or tissue cysts → excystation/release of sporozoites or bradyzoites in the gut → invasion of intestinal epithelium → conversion to tachyzoites → active replication and dissemination via blood/lymphatics → invasion of diverse cell types (especially neural, muscle, retinal, placental) → host immune response (IFN-γ-driven) controls acute infection → parasite converts to bradyzoite form and encysts, establishing lifelong latent infection → reactivation occurs upon loss of immune control (immunosuppression) or, in pregnancy, primary maternal infection allows transplacental passage of tachyzoites to the fetus.

**Molecular Pathways:**
- **Active host-cell invasion machinery**: The parasite uses a unique **glideosome** (actin-myosin motor complex) for active invasion, independent of host phagocytosis; involves **MIC (microneme)**, **ROP (rhoptry)**, and **GRA (dense granule)** protein secretion (KEGG: Toxoplasmosis pathway hsa05145; Reactome)
- **Parasitophorous vacuole (PV) formation**: Tachyzoites create a non-fusogenic PV that excludes host lysosomal fusion, evading destruction
- **Host IFN-γ/JAK-STAT1 pathway**: Central to host control — IFN-γ activates macrophages and induces IRGs (immunity-related GTPases) and GBPs (guanylate-binding proteins) that disrupt the PV membrane
- **Parasite countermeasures**: ROP18 phosphorylates and inactivates host IRGs (PMID:16709124); ROP5 pseudokinase cooperates with ROP18; GRA effectors (e.g., TgIST) block STAT1-dependent transcription (PMID:27300474)
- **NF-κB and inflammasome (NLRP1/NLRP3) signaling** in host innate response

**Cellular Processes:**
- Apoptosis modulation: *T. gondii* actively inhibits host cell apoptosis during acute infection to preserve its replicative niche (via effects on Bcl-2 family proteins and caspase inhibition)
- Autophagy interactions: host autophagy machinery can be recruited to target the PV (IRG/GBP-mediated), and parasite effectors counteract this
- Bradyzoite-tachyzoite interconversion: stress-induced (immune pressure, nitric oxide, alkaline pH) differentiation into slow-growing bradyzoites within tissue cysts, primarily in brain, retina, and skeletal/cardiac muscle — the biological basis of chronic latency

**Immune System Involvement:**
- Innate immunity: dendritic cells, macrophages, NK cells produce early IL-12 → drives Th1 polarization
- Adaptive immunity: CD4+ and CD8+ T cells, IFN-γ production is essential for control; CD8+ cytotoxic T cells particularly important for long-term control of cerebral cysts
- Immunocompromise (HIV/AIDS with CD4+ <100-200 cells/µL, transplant immunosuppression, chemotherapy) permits reactivation of latent bradyzoite cysts → tachyzoite conversion → toxoplasmic encephalitis
- In congenital infection, the developing fetal immune system is unable to mount an adequate Th1 response, permitting dissemination; placental infection precedes fetal transmission

**Tissue Damage Mechanisms:**
- Direct cytolytic damage from tachyzoite replication and host cell rupture
- Immune-mediated damage: local inflammatory response to reactivating cysts (particularly in retina) causes tissue destruction — ocular toxoplasmosis pathology is driven substantially by the host inflammatory response to ruptured cysts, not solely direct parasite cytotoxicity
- CNS: necrotizing encephalitis with microglial nodules, perivascular cuffing; periventricular calcification and ependymitis leading to aqueductal stenosis/hydrocephalus in congenital disease

**Biochemical Abnormalities:**
- Parasite salvages purines from host (lacks de novo purine synthesis) — pyrimethamine/sulfadiazine target parasite folate pathway (dihydrofolate reductase and dihydropteroate synthase, respectively), exploiting differences from host folate metabolism

**Molecular Profiling:**
- Transcriptomic studies show marked host cell reprogramming during infection, including suppression of interferon-stimulated genes via TgIST-mediated STAT1 blockade (PMID:27300474)
- Single-cell/organoid studies of placental and retinal models have illuminated tissue-specific tropism and barrier-crossing mechanisms

**Suggested GO terms:** GO:0044409 (entry into host), GO:0006955 (immune response), GO:0034341 (response to interferon-gamma), GO:0032491 (detection of molecule of fungal origin - N/A), GO:0140546 (defense response to symbiont), GO:0140367 (antibacterial innate immune response - use GO:0050832 defense response to fungus as analog term not applicable), GO:0006911 (phagocytosis, engulfment).
**Suggested CL terms:** CL:0000235 (macrophage), CL:0000798 (gamma-delta T cell), CL:0000625 (CD8-positive T cell), CL:0000624 (CD4-positive T cell), CL:0000540 (neuron), CL:0000359 (vascular associated smooth muscle cell — for placental/vascular involvement), CL:0000669 (pericyte, retinal context).

---

## 7. Anatomical Structures Affected

**Organ Level:**
- **Primary:** Brain (CNS), eye/retina, placenta (in congenital transmission), skeletal muscle, heart
- **Secondary:** Liver, spleen (neonatal hepatosplenomegaly), lymph nodes (lymphadenitis form)
- **Body systems:** Nervous system, ocular/visual system, reproductive system (placenta), immune system, musculoskeletal system

**UBERON terms:**
- UBERON:0000955 (brain)
- UBERON:0000966 (retina)
- UBERON:0001987 (placenta)
- UBERON:0001134 (skeletal muscle tissue)
- UBERON:0000948 (heart)
- UBERON:0002106 (spleen)
- UBERON:0002107 (liver)
- UBERON:0000029 (lymph node)
- UBERON:0001769 (choroid) / UBERON:0001782 (retina/choroid complex for chorioretinitis)

**Tissue and Cell Level:**
- Retinal pigment epithelium and neurosensory retina (chorioretinitis)
- Neurons and glial cells (encephalitis, microglial nodules)
- Trophoblast cells of the placenta (site of transplacental crossing)
- Cardiac and skeletal myocytes (tissue cyst reservoir)
- Cell Ontology: CL:0000540 (neuron), CL:0000127 (astrocyte), CL:0000129 (microglial cell), CL:0011026 (progenitor cell — placental cytotrophoblast: CL:0000351), CL:0000746 (cardiac muscle cell)

**Subcellular Level:**
- Parasitophorous vacuole (a *Toxoplasma*-specific, non-host organelle) — GO Cellular Component: GO:0020005 (symbiont-containing vacuole)
- Host mitochondria (recruited to PV membrane)
- Host nucleus (STAT1 signaling interference)
- GO:0005634 (nucleus), GO:0005739 (mitochondrion)

**Localization:**
- CNS lesions: periventricular (congenital calcifications), diffuse in AIDS-related toxoplasmic encephalitis (often basal ganglia, corticomedullary junction)
- Ocular lesions: posterior pole retina, often juxtapapillary or adjacent to old scars (classic "satellite lesion" recurrence pattern)
- Bilateral involvement possible but ocular disease is often unilateral at any given episode

---

## 8. Temporal Development

**Onset:**
- Congenital: infection occurs in utero; clinical manifestation may be present at birth or delayed by months to decades (especially chorioretinitis)
- Acquired (immunocompetent): incubation ~1-3 weeks post-exposure before symptomatic mononucleosis-like illness (if symptomatic at all)
- Reactivation (immunocompromised): can occur at any point following primary infection once immune control wanes (e.g., CD4+ count drop in AIDS)

**Onset pattern:** Acute (initial infection, encephalitis in immunocompromised) vs. insidious/chronic (latent cyst-forming stage, asymptomatic for life in most immunocompetent hosts)

**Progression:**
- Acute tachyzoite stage → immune containment → chronic bradyzoite/cyst latency (lifelong)
- In congenital disease: risk of transmission increases with gestational age at maternal infection (up to ~70-90% in third trimester) but **severity of fetal disease is inversely related to gestational age** — earlier infection (first trimester) is less frequently transmitted but produces more severe disease when it occurs (PMID:10535648, PMID:17825405 — SYROCOT meta-analysis established this gestational-age-dependent transmission/severity relationship)
- Ocular disease: episodic, relapsing-remitting pattern with recurrent retinochoroiditis flares from reactivation at the margin of pre-existing scars

**Progression rate:** Variable — congenital sequelae can be rapidly apparent (severe neonatal disease) or slowly evolving (chorioretinitis appearing in the second or third decade of life); toxoplasmic encephalitis in untreated AIDS progresses over days to weeks and is fatal without treatment

**Disease course pattern:** Latent chronic infection punctuated by episodic reactivation (ocular disease, encephalitis) — classic relapsing-remitting pattern for ocular toxoplasmosis

**Critical periods:** Pregnancy (maternal seroconversion timing determines both transmission risk and fetal disease severity) is the single most important critical window; immunosuppression onset/degree is the critical window for reactivation disease.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Seroprevalence:** highly variable globally, ranging from ~10-30% in the US and UK to >60-80% in parts of France, Brazil, and other regions with high raw meat consumption or warm/humid climates (PMID:19257814 — Pappas et al., global toxoplasmosis seroprevalence review)
- **Congenital toxoplasmosis incidence:** estimated ~1-10 per 10,000 live births globally, varies by region and screening program (France has historically had among the highest rates with mandatory prenatal screening)
- **US estimate:** CDC estimates >40 million people in the US may be infected with *Toxoplasma*, most asymptomatic

**Inheritance pattern:** Not applicable (infectious disease, not genetic); however, host susceptibility modifier alleles show typical complex/polygenic association patterns (not Mendelian)

**Penetrance/Expressivity:** N/A for classic Mendelian sense; clinical "penetrance" of symptomatic disease following infection is low in immunocompetent hosts (~10-20% develop symptoms) but essentially complete for reactivation disease in profound immunosuppression if untreated

**Population Demographics:**
- Affected populations: universal susceptibility; seroprevalence increases with age (cumulative lifetime exposure)
- Geographic distribution: higher in tropical/subtropical, humid climates (Brazil, France) vs. cold/dry (Scandinavia, parts of North America); notably higher and more severe (including in immunocompetent hosts) in South America due to atypical/more virulent parasite genotypes (PMID:16880330)
- Sex ratio: no strong intrinsic sex predilection for acquisition, though congenital transmission obviously depends on maternal infection
- Age distribution: seroprevalence rises steadily with age due to cumulative exposure

---

## 10. Diagnostics

**Clinical/Laboratory Tests:**
- **Serology (primary diagnostic tool):** IgG and IgM antibody detection via ELISA, indirect fluorescent antibody (IFA), or the Sabin-Feldman dye test (historic gold standard)
- **IgG avidity testing:** low avidity suggests infection within the last ~4 months; high avidity suggests infection >4 months prior — critical for dating infection relative to conception in pregnant women (PMID:11114023 — Montoya, diagnosis review)
- **PCR:** detection of *T. gondii* DNA in amniotic fluid (for congenital diagnosis), blood, CSF, or vitreous/aqueous humor (ocular disease), or bronchoalveolar lavage (immunocompromised pulmonary disease)
- **Histopathology:** tissue biopsy showing tachyzoites or cysts with characteristic staining (immunohistochemistry using anti-*Toxoplasma* antibodies)

**Imaging:**
- **CT/MRI brain:** ring-enhancing lesions (typically multiple, basal ganglia/corticomedullary junction) in toxoplasmic encephalitis; periventricular calcifications in congenital disease
- **Ophthalmologic exam/fundoscopy:** focal necrotizing retinochoroiditis, often adjacent to pigmented scar ("satellite lesion")
- **Prenatal ultrasound:** ventriculomegaly, intracranial calcifications, hepatosplenomegaly, placental thickening

**Genetic Testing:** Not applicable in the traditional sense (not a heritable Mendelian disease); parasite genotyping (PCR-RFLP or multilocus sequence typing of *T. gondii* isolates) is used for epidemiological/virulence characterization, not clinical diagnosis of the patient.

**Clinical Criteria:**
- Congenital toxoplasmosis diagnosis relies on combination of maternal seroconversion timing, amniotic fluid PCR, neonatal IgM/IgA serology (since maternal IgG crosses placenta), and clinical/imaging findings
- Differential diagnosis for congenital: other TORCH infections (CMV, rubella, herpes, syphilis); for cerebral toxoplasmosis in AIDS: primary CNS lymphoma, progressive multifocal leukoencephalopathy (PML), CNS tuberculosis
- Differential for ocular disease: other infectious retinitis (CMV, herpetic), sarcoidosis, other causes of posterior uveitis

**Screening:**
- Prenatal maternal serologic screening (mandatory in France, recommended/variable elsewhere) with monthly retesting in seronegative women
- Newborn screening programs in some regions (US state programs vary; not universal)

---

## 11. Outcome/Prognosis

**Survival and Mortality:**
- Immunocompetent acute infection: essentially 0% mortality, self-limited
- Untreated toxoplasmic encephalitis in AIDS: historically high mortality without antiretroviral therapy and specific treatment; with HAART and treatment, prognosis markedly improved (PMID:11815817)
- Congenital toxoplasmosis: mortality is low with modern treatment but can be substantial in severe untreated cases (hydrocephalus, disseminated neonatal disease)

**Morbidity:**
- Long-term neurological and visual sequelae from congenital infection are the major morbidity driver — chorioretinitis recurrence can occur throughout life, cumulative visual field loss with repeated episodes
- SYROCOT meta-analysis (PMID:17825405) found that treatment during pregnancy reduces but does not eliminate transmission/sequelae risk, and the relationship between treatment timing and outcome remains debated

**Complications:**
- Congenital: hydrocephalus requiring shunting, epilepsy, cognitive impairment, blindness from recurrent chorioretinitis
- Ocular: recurrent inflammation, macular scarring, retinal detachment, cataract, glaucoma (secondary)
- CNS reactivation: seizures, focal deficits, coma if untreated

**Prognostic factors:** Immune status (CD4 count in HIV patients is the dominant prognostic factor for reactivation disease and response to treatment); gestational timing of maternal infection; prompt initiation of treatment; parasite strain virulence (atypical strains → worse ocular prognosis).

---

## 12. Treatment

**Pharmacotherapy:**
- **Pyrimethamine + sulfadiazine + folinic acid (leucovorin)** — first-line combination for active disease (encephalitis, severe congenital disease, ocular disease); targets parasite folate pathway (DHFR inhibition by pyrimethamine, DHPS inhibition by sulfadiazine) — NCIT term candidates: NCIT:C500 (Pyrimethamine), NCIT:C568 (Sulfadiazine)
  - This maps directly to the dismech `bacterial_folate_synthesis_inhibition` module pattern (antifolate mechanism), though here applied to a protozoan rather than bacterial target
- **Spiramycin** — used in pregnancy for maternal infection to reduce transplacental transmission (does not cross placenta well, so used before confirmed fetal infection) — NCIT:C29014 (macrolide-class)
- **Trimethoprim-sulfamethoxazole (TMP-SMX)** — alternative regimen, also prophylaxis in HIV
- **Clindamycin** — alternative to sulfadiazine in sulfa-allergic patients, combined with pyrimethamine
- **Atovaquone** — alternative agent for treatment/prophylaxis in sulfa-intolerant patients

**Treatment term (NCIT):** NCIT:C15986 (Pharmacotherapy) as the general treatment_term, with `therapeutic_agent` entries for pyrimethamine (CHEBI:8460), sulfadiazine (CHEBI:9328), spiramycin (CHEBI:9216), clindamycin (CHEBI:3745).

**Surgical/Interventional:**
- Ventriculoperitoneal shunt placement for hydrocephalus secondary to congenital toxoplasmosis (NCIT:C15329, Surgical Procedure)

**Supportive Care:**
- Corticosteroids as adjunctive therapy for ocular toxoplasmosis when inflammation threatens the macula or optic nerve, and for CNS disease with significant edema/mass effect (NCIT:C2144, Corticosteroid)
- Anticonvulsants for seizure management

**Prophylaxis:**
- Secondary prophylaxis (lower-dose pyrimethamine-sulfadiazine) in AIDS patients following treatment of acute toxoplasmic encephalitis, until CD4+ count recovers >200 cells/µL for ≥6 months on ART
- Primary prophylaxis (TMP-SMX) recommended for HIV-positive, *Toxoplasma*-seropositive patients with CD4+ <100 cells/µL

**Treatment Outcomes:**
- Response rates to pyrimethamine-sulfadiazine for toxoplasmic encephalitis are generally high (>80%) with appropriate ART co-management
- Adverse effects: sulfadiazine — crystalluria, hypersensitivity, bone marrow suppression; pyrimethamine — bone marrow suppression (mitigated by folinic acid co-administration, not folic acid which can reduce efficacy)

**Experimental/Investigational:**
- Newer agents in development targeting apicoplast biology and novel parasite enzymes are in preclinical/early trial stages; no major approved gene/cell/RNA therapies exist for this infectious disease (not applicable in the way it would be for a genetic disorder)

---

## 13. Prevention

**Primary Prevention:**
- Dietary: cook meat to safe internal temperatures (≥63-74°C depending on meat type), freeze meat before consumption, wash fruits/vegetables, avoid unpasteurized dairy
- Avoid changing cat litter during pregnancy (or use gloves and wash hands; litter boxes should be cleaned daily since oocysts require 1-5 days to become infectious)
- Wear gloves gardening; wash hands after soil contact
- Avoid drinking untreated water in endemic areas

**Secondary Prevention:**
- Prenatal serologic screening programs (monthly in France for seronegative women) enabling prompt initiation of spiramycin/pyrimethamine-sulfadiazine upon seroconversion to reduce transplacental transmission
- Regular CD4+ monitoring and prophylaxis initiation in HIV-positive patients

**Tertiary Prevention:**
- Secondary chemoprophylaxis after treated toxoplasmic encephalitis until immune reconstitution
- Regular ophthalmologic follow-up for patients with known ocular toxoplasmosis to catch recurrences early

**Immunization:** No approved human vaccine exists. A live-attenuated vaccine (Toxovax/S48 strain) is licensed for veterinary use in sheep to prevent ovine congenital toxoplasmosis (abortion), but no human vaccine has reached approval — an active area of research (PMID:24581229, review of vaccine development efforts).

**Screening:**
- Prenatal maternal serology (universal in France; risk-based or not routine in the US, UK)
- HIV patients: baseline *Toxoplasma* IgG serology at HIV diagnosis to identify those at risk for reactivation

**Counseling:** Genetic counseling is not applicable in the traditional sense; however, prenatal counseling regarding transmission risk, treatment options, and prognosis is standard of care once maternal seroconversion is documented.

**Public Health:** Health education campaigns regarding food safety and cat litter hygiene for pregnant women; water treatment infrastructure to prevent oocyst-contaminated water supplies (relevant post major outbreaks, e.g., Victoria BC 1995, PMID:9366006).

---

## 14. Other Species / Natural Disease

**Taxonomy:** *Toxoplasma gondii* infects essentially all warm-blooded vertebrates.
- Definitive host: domestic and wild Felidae (NCBITaxon:9685, *Felis catus*)
- Intermediate hosts include: sheep (NCBITaxon:9940), pigs (NCBITaxon:9823), cattle (NCBITaxon:9913), rodents (mouse NCBITaxon:10090), birds, marine mammals

**Natural Disease:**
- **Ovine toxoplasmosis:** major cause of abortion and stillbirth in sheep flocks worldwide — significant agricultural/economic impact; this is the target of the licensed veterinary vaccine (Toxovax)
- **Feline toxoplasmosis:** typically subclinical in cats; occasional clinical disease in kittens or immunocompromised cats (systemic disease with pneumonia, hepatitis, encephalitis)
- **Marine mammal toxoplasmosis:** significant cause of mortality in California sea otters (*Enhydra lutris*) — linked to land-based oocyst runoff into marine environments, an important One Health/environmental sentinel finding (well documented in veterinary/wildlife literature, e.g., Miller et al. studies on sea otter toxoplasmosis)
- **Marsupial toxoplasmosis:** particularly severe/fatal disease in Australian marsupials (which lack coevolutionary exposure), an important conservation concern

**Comparative Biology:**
- Mouse models are the dominant experimental system and recapitulate acute (tachyzoite-driven) and chronic (cyst-forming, CNS) infection stages effectively, forming the basis for most virulence factor discovery (ROP18, ROP5, IRG/GBP biology)
- Disease severity is highly species-dependent — mice are relatively susceptible, while natural definitive/intermediate hosts co-evolved with the parasite show milder disease; naive species (marsupials, some marine mammals) show disproportionate severity

**Zoonotic potential:** Yes — this is a fundamentally zoonotic parasite; humans are dead-end intermediate hosts (no onward transmission from human to human except transplacentally, transfusion, or transplant).

---

## 15. Model Organisms

**Mouse Models (dominant system):**
- Standard laboratory mice (various inbred strains — C57BL/6, BALB/c) are highly susceptible and used extensively to study acute virulence, chronic cyst formation in brain, and reactivation upon immunosuppression
- Genetically modified mice: IFN-γ knockout, IRG (immunity-related GTPase) knockout, and GBP knockout mice have been central to dissecting host innate resistance pathways (PMID:16709124 context)
- MGI (Mouse Genome Informatics) catalogs relevant knockout lines for Ifng, Irgm1, Irgm3, and related immune genes used in toxoplasmosis research

**Cellular/In Vitro Models:**
- Human foreskin fibroblasts (HFF) — standard cell line for *T. gondii* in vitro culture and invasion assays
- Retinal pigment epithelial cell lines and organoids — used to model ocular tropism and blood-retinal barrier crossing
- Placental trophoblast/organoid models and placental explants — used to study transplacental transmission mechanisms
- Human iPSC-derived neurons and brain organoids — emerging models for CNS tropism and neuroinflammation studies

**Applications:**
- Mouse models recapitulate the acute-to-chronic transition and cyst formation in brain very well, making them the primary tool for testing anti-parasitic drugs and vaccine candidates
- Reactivation models (immunosuppressing chronically infected mice) model AIDS-associated toxoplasmic encephalitis

**Limitations:**
- Mouse models do not fully recapitulate human congenital transmission dynamics (placental structure differs substantially between mice and humans — hemochorial similarities exist but timing/susceptibility windows differ)
- Human ocular disease natural history (chronic recurrent decades-long relapsing pattern) is difficult to model in short-lived rodents

**Resources:** MGI (Mouse Genome Informatics) for knockout strain catalogs; ATCC and BEI Resources for *T. gondii* strains (RH, Pru, ME49, VEG representing Type I/II/III reference strains) and host cell lines; ToxoDB (a dedicated *Toxoplasma* genomics database, part of VEuPathDB) for parasite genomic/genetic resources.

---

## Summary of Key PMID Citations

| PMID | Relevance |
|---|---|
| 17825405 | SYROCOT meta-analysis — gestational timing, transmission, treatment effect on congenital toxoplasmosis outcomes |
| 22218351 | Robert-Gangneux & Dardé — comprehensive epidemiology/transmission review |
| 19257814 | Pappas et al. — global seroprevalence review |
| 16709124 | Taylor et al. — ROP18 as major parasite virulence determinant (QTL mapping) |
| 27300474 | Gay et al. — TgIST blocks host STAT1 signaling (immune evasion mechanism) |
| 16880330 | Atypical/Type I genotype association with severe ocular disease in South America |
| 19468306 | Witola et al. — NALP1 polymorphisms and congenital toxoplasmosis susceptibility |
| 11815817 | HAART reduces incidence of toxoplasmic encephalitis in HIV/AIDS |
| 9366006 | Bowie et al. — Victoria BC waterborne toxoplasmosis outbreak |
| 21966149 | Jamieson et al. — host genetics review in toxoplasmosis |
| 11114023 | Montoya — diagnosis of *Toxoplasma gondii* infection review |

**Note on evidence gaps:** Precise, universally-agreed quantitative frequencies for individual congenital phenotypes (chorioretinitis %, hydrocephalus %) vary substantially by cohort, screening intensity, and follow-up duration — curators should pull exact frequency figures directly from specific cohort studies (e.g., SYROCOT, EMSCOT) rather than a single pooled number, and verify exact PMID snippet quotes against cached abstracts per the dismech evidence SOP before finalizing entries.