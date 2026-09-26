---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-18T15:06:19.583799'
end_time: '2026-08-18T15:11:17.233395'
duration_seconds: 297.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities
  mondo_id: ''
  category: Mendelian
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 25
  total_cost_usd: 2.0803689
  session_id: 16d918bb-574c-58cf-90c1-b24e51379c94
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 14
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities** covering all of the
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

I'll research this disease using web search tools, which I need to load first.

Now let me get the full-text details from PMC (Kurolap et al. 2022, AJHG) for granular clinical/phenotype/mechanism data.

I now have sufficient primary-literature detail to compile the comprehensive report. Let me do a couple final targeted searches for prevalence/diagnosis/treatment-guideline gaps.

# Research Report: Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities (NEDNMS)

## 1. Disease Information

**Overview:** Neurodevelopmental Disorder with Neuromuscular and Skeletal Abnormalities (NEDNMS) is a rare, autosomal recessive Mendelian disorder caused by bi-allelic (homozygous or compound heterozygous) loss-of-function or damaging missense variants in *NRCAM* (Neuronal Cell Adhesion Molecule). It presents from infancy or early childhood with global developmental delay/intellectual disability, hypotonia and/or spasticity, peripheral neuropathy, skeletal anomalies, and dysmorphic facial features, with a highly variable severity spectrum ranging from early mortality to isolated adult-onset peripheral neuropathy without cognitive impairment. The disorder was first delineated in 2022 by Kurolap et al. in *The American Journal of Human Genetics*, describing 10 affected individuals from 8 families ([PMID:35108495](https://pubmed.ncbi.nlm.nih.gov/35108495/); PMC8948158).

**Key identifiers:**
- **OMIM:** #619833 (NEDNMS); gene locus OMIM #601581 (*NRCAM*)
- **Gene:** *NRCAM* (HGNC:7994), chromosome 7q31.1
- **Suggested MONDO:** disease should map to a MONDO term for OMIM 619833 (specific 7-digit MONDO CURIE not confirmed via direct lookup in this search session — verify via `oak` against `sqlite:obo:mondo` before curation, per dismech SOP)
- **Inheritance:** Autosomal recessive
- **Synonyms:** NEDNMS; NRCAM-related neurodevelopmental disorder; NRCAM deficiency

**Evidence basis:** Aggregated, disease-level cohort data derived from clinical genetics case series (exome sequencing cohorts) rather than large-scale EHR/registry data — this is a nano-rare disorder with fewer than 15 published cases to date across three case series.

---

## 2. Etiology

**Primary cause:** Bi-allelic pathogenic variants in *NRCAM*, encoding neuronal cell adhesion molecule (NrCAM), a member of the L1/neurofascin/NgCAM immunoglobulin-superfamily of cell adhesion molecules. Loss of functional NrCAM protein disrupts neuron-neuron adhesion, axon growth/guidance, node-of-Ranvier formation, and synaptogenesis (Kurolap et al., PMID:35108495).

**Genetic risk factors:**
- Founder/recurrent variants have been reported in specific communities: the Amish population and Libyan Jewish population each contributed families with homozygous variants (Kurolap et al. 2022), consistent with founder-effect or consanguinity-driven homozygosity.
- Reported variants cluster disproportionately in the **third fibronectin type III (Fn-III) domain** of NrCAM, which contains a putative RGD-equivalent integrin-binding motif (KGE, residues 934–936) and a furin protease recognition site (RNRR, residues 894–897) — suggesting this domain is functionally critical (PMC8948158).
- A second, independent report (Elahi et al. 2023, *Molecular Genetics & Genomic Medicine*) identified a homozygous nonsense variant, c.73C>T (p.Gln25*), causing an isolated motor-predominant axonal polyneuropathy phenotype, expanding genetic and allelic heterogeneity.

**Environmental risk factors:** None established; this is a purely monogenic Mendelian disorder with no known environmental trigger or modifier reported in the literature reviewed.

**Protective factors:** None reported.

**Gene-environment interactions:** Not established for the Mendelian NEDNMS phenotype. (Note: common *NRCAM* SNPs, distinct from the rare bi-allelic disease-causing variants, have been separately associated with autism spectrum traits and substance-use/addiction vulnerability in population genetic-association studies — International Journal of Neuropsychopharmacology reports — but these are polygenic-susceptibility associations, not causal for NEDNMS, and should not be conflated with it.)

---

## 3. Phenotypes

Cohort of 10 patients (Kurolap et al. 2022) plus additional isolated-neuropathy cases (Elahi et al. 2023; Cortese/motor-neuronopathy cohort, PMC10808011) define the phenotypic spectrum:

| Phenotype | Frequency in cohort | Suggested HPO term |
|---|---|---|
| Global developmental delay / intellectual disability | 80% (8/10); one individual unaffected cognitively | HP:0001263 / HP:0001249 |
| Hypotonia (axial and/or peripheral) | 70% (7/10) | HP:0001252 |
| Spasticity / hypertonia (incl. spastic quadriplegia/paraplegia) | 50% (5/10) | HP:0001257 / HP:0002510 |
| Peripheral (demyelinating) neuropathy | 60–70% (6-7/10); sole finding in mildest cases | HP:0000762 / HP:0003701 |
| Ataxia | present in subset | HP:0001251 |
| Microcephaly | 30% (3/10) | HP:0000252 |
| Seizures | 1 individual | HP:0001250 |
| Scoliosis | multiple individuals | HP:0002650 |
| Hip dysplasia/dislocation | multiple individuals | HP:0001385 |
| Pes cavus / pes planus | present | HP:0001761 / HP:0001763 |
| Distal arthrogryposis / contractures | present | HP:0005684 |
| Dysmorphic facial features (bitemporal narrowing, bushy/medially flared eyebrows, long eyelashes, depressed nasal bridge, cupid-bow lips, micrognathia, plagiocephaly) | ~70% | HP:0000316 / HP:0000426 / HP:0000348 |
| Optic atrophy | subset | HP:0000648 |
| Strabismus / exotropia | subset | HP:0000577 |
| Cataract, retinal detachment, abnormal VEP | subset | HP:0000518 / HP:0000541 |
| Sensorineural/abnormal auditory evoked responses | 3/10 | HP:0008619 |
| Hydrocephalus / ventriculomegaly | variable | HP:0000238 / HP:0002119 |
| Thin/agenetic corpus callosum, delayed myelination, periventricular leukomalacia, gray matter heterotopia | variable, some with normal imaging | HP:0002079 / HP:0002188 |
| Self-injurious/behavioral abnormalities (irritability, anxiety, aggression) | 3 individuals | HP:0100716 |
| Failure to thrive / growth restriction | present | HP:0001508 |
| Cryptorchidism | present | HP:0000028 |

**Onset/course:** Symptoms are apparent from infancy or early childhood in most cases; onset in the isolated-neuropathy phenocopies can be delayed to the second/third decade (Elahi et al. 2023; PMC10808011 motor-neuronopathy cohort reported onset "second decade of life" in some). Severity spans a continuum: most severe individuals died in infancy/early childhood (e.g., death at 21 months in one individual, with hydrocephalus, failure to thrive, and neuropathy); moderate cases show persistent intellectual disability, motor dysfunction and neuropathy/spasticity; a neonatally severe individual improved with age and had no intellectual disability by age 5; the mildest reported adults (ages 27–31) had isolated late-onset peripheral neuropathy with normal cognition.

**Quality of life impact:** Not formally measured with standardized instruments (EQ-5D/SF-36) in the literature identified; qualitatively, severely affected individuals require gastrostomy feeding, tracheostomy/oxygen support, and have marked functional impairment; mildly affected adults function independently with isolated neuropathy.

---

## 4. Genetic/Molecular Information

**Causal gene:** *NRCAM* (HGNC:7994; OMIM *601581*), chromosome 7q31.1, encoding a 1,275-amino-acid transmembrane protein with 6 Ig-like (V-set) domains and 5 fibronectin type III (Fn-III) repeats (UniProt Q92823).

**Reported pathogenic variants (Kurolap et al. 2022, 8 families):**

| Individual | cDNA | Protein | Zygosity | Domain |
|---|---|---|---|---|
| 1 | c.2785C>T | p.Arg929* | Homozygous | Fn-III domain 3 |
| 2 | c.331G>T | p.Glu111* | Homozygous | Ig-like domain 1 |
| 3 | c.164A>G; c.230+824G>C | p.Asp55Gly; splice | Compound het | Ig-like 1; intron 6 |
| 4 | c.2557C>T; c.2705A>C | p.Arg853Cys; p.Lys902Thr | Compound het | Fn-III 3 (both) |
| 5 | c.1406A>G; c.2738G>A | p.Asn469Ser; p.Gly913Asp | Compound het | Ig-like 5; Fn-III 3 |
| 6a/6b | c.590G>A | p.Gly197Asp | Homozygous | Ig-like 2 |
| 7 | c.2297_2302delinsTC; c.2647-2A>G | p.Thr766Ilefs*4; splice | Compound het | Fn-III 2; intron 24 |
| 8a/8b | c.400T>C | p.Ser134Pro | Homozygous | Ig-like 1 |

Plus: c.73C>T (p.Gln25*), homozygous, in an Iranian patient with isolated motor-predominant axonal polyneuropathy (Elahi et al. 2023).

**Variant classification:** Predominantly nonsense, frameshift, splice-site, and missense variants classified pathogenic/likely pathogenic per ACMG/AMP criteria in the original reports; formal aggregate ClinVar counts were not retrievable in this search session and should be queried directly at clinvar.ncbi.nlm.nih.gov before curation.

**Genotype-phenotype correlation:** Loss-of-function (nonsense/frameshift/splice) variants are associated with more severe phenotypes; missense variant effects are variant- and location-dependent. Variants cluster in the third Fn-III domain, implicated in protein-protein interaction interfaces (RGD-like integrin-binding motif, furin cleavage site).

**Population allele frequency:** *NRCAM* loss-of-function constraint metrics (pLI, o/e ratios) from gnomAD were not directly retrieved in this session; recommend querying gnomAD directly (gnomad.broadinstitute.org, gene NRCAM) prior to KB entry to populate `case_fractions`/constraint context.

**Functional consequence:** Loss of function (nonsense, frameshift, splice-disrupting) and hypomorphic/damaging missense — consistent with `LOSS_OF_FUNCTION` / `PARTIAL_LOSS_OF_FUNCTION` `functional_impact_category` values per dismech's `GeneticContext` slot guidance.

**Epigenetic information:** None reported specific to this disorder in the literature surveyed.

**Chromosomal abnormalities:** Not applicable — disease is caused by intragenic sequence variants, not large-scale chromosomal rearrangements.

**Notable tangential molecular finding (not disease-causing for NEDNMS):** A 2025 study (Cell Reports / bioRxiv, medRxiv preprint on TCGA analysis) describes an oncogenic NRCAM microexon-skipping splice isoform as a targetable cell-surface proteoform in high-grade gliomas — a distinct, non-Mendelian somatic phenomenon unrelated to the germline bi-allelic NEDNMS mechanism, included here only to flag it as an irrelevant hit if encountered during NEC preflight checks.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious triggers have been implicated in NEDNMS in the literature surveyed — consistent with its status as a purely monogenic, bi-allelic Mendelian disorder.

---

## 6. Mechanism / Pathophysiology

**Molecular function of NrCAM:** NrCAM is an L1-family immunoglobulin-superfamily cell adhesion molecule mediating homophilic trans-binding via its extracellular Ig-like and Fn-III domains, coupled intracellularly to the actin cytoskeleton via ankyrin and ERM (ezrin-radixin-moesin) proteins, and to PDZ-domain scaffolds (PSD-95, SAP102) at synapses.

**Causal chain (proposed):**
1. Bi-allelic *NRCAM* variant → loss/reduction of functional NrCAM protein or disruption of its Fn-III domain 3 interaction surface
2. → Impaired neuron-neuron and neuron-glia adhesion; disrupted axon growth/guidance signaling
3. → Abnormal synaptogenesis and defective neurite outgrowth (shown in *Nrcam*-deficient murine cerebellar granule cells)
4. → Impaired node-of-Ranvier formation/maintenance at the Schwann cell-axon interface (NrCAM + gliomedin establish the heminode that matures into the node), producing peripheral demyelinating neuropathy
5. → Thalamic axon mistargeting → abnormal visual-evoked potentials / optic atrophy
6. → Downstream: global developmental delay, hypotonia/spasticity, ataxia, and CNS structural anomalies (thin corpus callosum, delayed myelination, heterotopia)
7. Skeletal/musculoskeletal findings (scoliosis, hip dysplasia, contractures/arthrogryposis, pes cavus/planus) are likely secondary consequences of chronic hypotonia/neuropathy-driven altered biomechanical loading rather than a direct skeletal-lineage NRCAM defect (no primary bone/cartilage cell-autonomous mechanism reported).

**Cellular processes involved:** Axon guidance and outgrowth, cell adhesion, synaptogenesis, myelination/node-of-Ranvier assembly, actin cytoskeletal coupling.

**Protein dysfunction:** Predicted disruption of protein folding/surface electrostatics and protein-protein interaction interfaces by missense substitutions (SWISS-MODEL, ProSA-web, APBS electrostatics, ODA docking-area analyses in Kurolap et al. 2022); truncating variants predicted to produce loss of the Fn-III domain 3 region entirely.

**Model-organism corroboration:** CRISPR-generated zebrafish *nrcama* mutants (302-bp deletion of the third Fn-III domain) showed significantly increased swimming activity in darkness (p=0.03) versus wild-type, and trends toward increased α-tubulin-positive axonal fibers in the dorsal telencephalon and a thickened anterior telencephalic commissure — interpreted as altered axonal projections and abnormal activity-driven behavior, mechanistically consistent with the human phenotype (Kurolap et al. 2022).

**Suggested GO terms:** GO:0007155 (cell adhesion), GO:0007411 (axon guidance), GO:0031175 (neuron projection development), GO:0007416 (synapse assembly), GO:0031290 (retinal ganglion cell axon guidance), GO:1990138 (neuron projection extension involved in neuron projection guidance).

**Suggested CL terms:** CL:0000540 (neuron), CL:0000125 (glial cell), CL:0002573 (Schwann cell), CL:0000121 (cerebellar Purkinje cell) / cerebellar granule cell, CL:0000679 (glutamatergic neuron) as relevant to cortical circuits.

**Cell types/tissues involved:** Central and peripheral neurons, Schwann cells (myelinating peripheral glia), oligodendrocytes (CNS myelination), retinal ganglion cells/optic pathway neurons.

---

## 7. Anatomical Structures Affected

**Organ/system level:** Central nervous system (brain — cortex, corpus callosum, cerebellum, thalamus), peripheral nervous system (peripheral nerves), visual system (optic nerve, retina), auditory system, musculoskeletal system (spine, hips, feet), and secondarily the gastrointestinal system (failure to thrive/feeding difficulty).

**Tissue/cell level:** Peripheral nerve myelin and nodes of Ranvier; cerebellar granule neurons; corpus callosum white matter; optic nerve axons.

**Subcellular level:** Plasma membrane (NrCAM is a type-I transmembrane cell-surface glycoprotein), sites of axo-glial contact at nodes of Ranvier, synaptic membrane/postsynaptic density (PSD-95/SAP102 scaffold interactions). Suggested GO Cellular Component terms: GO:0033268 (node of Ranvier), GO:0043198 (dendritic shaft), GO:0045202 (synapse), GO:0005886 (plasma membrane).

**Localization / UBERON suggestions:** UBERON:0000955 (brain), UBERON:0001017 (central nervous system), UBERON:0000010 (peripheral nervous system), UBERON:0001851 (cortex), UBERON:0002336 (corpus callosum), UBERON:0002037 (cerebellum), UBERON:0000940 (optic nerve), UBERON:0001021 (nerve).

**Lateralization:** Findings are generally bilateral/symmetric (e.g., bilateral peripheral neuropathy, bilateral optic atrophy); not typically lateralized.

---

## 8. Temporal Development

**Onset:** Most cases present from infancy or early childhood (congenital-to-early-childhood onset); a subset of loss-of-function homozygotes present later, in the second-to-third decade, with an isolated motor-predominant polyneuropathy phenotype only.

**Onset pattern:** Insidious/developmental for the classic multisystem phenotype; can be subacute in the milder isolated-neuropathy phenocopy.

**Progression:** Highly variable — ranges from a static/non-progressive developmental delay pattern in some, to a progressive/severe course leading to early mortality in others (death at 21 months reported in the most severe case), to an improving trajectory in at least one neonatally severe individual who lost the intellectual disability component by age 5. The isolated-neuropathy phenotype in older, mildly affected adults (ages 27–31) appears slowly progressive or stable.

**Disease course pattern:** Chronic; not episodic or relapsing-remitting based on available reports.

**Critical periods:** Neurodevelopmental window (infancy-early childhood) appears to be the period of greatest phenotypic expressivity for the CNS component; no established treatment window identified.

---

## 9. Inheritance and Population

**Epidemiology:** NEDNMS is an ultra-rare disorder; only ~13 patients have been reported in the peer-reviewed literature across three publications (Kurolap et al. 2022, n=10; Elahi et al. 2023, n=1; motor-neuronopathy cohort n≥2 with isolated neuropathy phenotype). No formal prevalence or incidence estimate exists; classify as prevalence_class `NOT_YET_DOCUMENTED` or `ULTRA_RARE` pending Orphanet assignment.

**Inheritance pattern:** Autosomal recessive (bi-allelic — homozygous or compound heterozygous).

**Penetrance:** Appears complete for at least some phenotypic manifestation, though expressivity is markedly variable (from lethal multisystem disease to isolated late-onset neuropathy).

**Expressivity:** Highly variable, both between and within genotype classes; genotype-phenotype correlation trends toward LOF variants = more severe, but is not absolute.

**Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for NEDNMS.

**Founder effects:** Suggested by recurrent homozygous variants in the Amish and Libyan Jewish communities in the original cohort (Kurolap et al. 2022), consistent with population-specific founder alleles, though formal founder-haplotype analysis was not confirmed in the sources reviewed.

**Consanguinity:** Implied as a contributing factor given the preponderance of homozygous (rather than compound heterozygous) genotypes in several families.

**Population demographics:** Reported affected families span diverse ancestries — Muslim Arab, European, Chinese, Amish, Libyan Jewish, Turkish, and Iranian — indicating a pan-ethnic distribution rather than restriction to a single population.

**Sex ratio:** Not clearly skewed in the reported cohort (mixed male/female cases, including sibling pairs 6a/6b and 8a/8b).

---

## 10. Diagnostics

**Genetic testing (primary diagnostic modality):** Whole exome sequencing (WES) is the modality used in all reported cases, with Sanger confirmation and segregation analysis; WES-based CNV detection and runs-of-homozygosity assessment were used to detect the homozygous nonsense variant in the Elahi et al. 2023 case. Gene panel testing for hereditary spastic paraplegia / peripheral neuropathy / intellectual disability may include *NRCAM* (it is listed on the Genomics England PanelApp "Childhood onset hereditary spastic paraplegia" panel).

**Clinical/laboratory tests:** No specific biomarker or lab test exists; diagnosis relies on WES/WGS plus supportive clinical, neuroimaging, and electrophysiologic findings:
- Nerve conduction studies — demonstrating demyelinating peripheral neuropathy
- Brain MRI — variable findings (thin/agenetic corpus callosum, delayed myelination, periventricular leukomalacia, ventriculomegaly/hydrocephalus, gray matter heterotopia; can also be normal)
- Visual evoked potentials — abnormal, consistent with optic pathway involvement
- Brainstem auditory evoked responses — abnormal in a subset (3/10)
- Skeletal radiographs — for scoliosis, hip dysplasia, contractures

**Differential diagnosis:** Other genetic causes of the combined developmental delay + hypotonia/spasticity + peripheral neuropathy phenotype — e.g., other L1CAM-family disorders (L1CAM syndrome/X-linked hydrocephalus), Charcot-Marie-Tooth disease subtypes, other hereditary spastic paraplegias, and other syndromic intellectual disability disorders with skeletal involvement should be excluded by targeted or exome-wide testing given phenotypic overlap.

**Screening:** No newborn screening or population carrier-screening program exists given the disorder's recent delineation (2022) and extreme rarity.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Highly variable; the most severely affected reported individual died at 21 months of age with hydrocephalus, failure to thrive, and neuropathy. No formal survival statistics exist given the small case count.

**Morbidity/function:** Severely affected individuals require gastrostomy feeding and, in some cases, tracheostomy/supplemental oxygen; the mildest reported adults (ages 27–31) have normal cognition with isolated peripheral neuropathy and are functionally independent.

**Complications:** Hydrocephalus, failure to thrive, self-injurious behavior, seizures (rare), scoliosis/hip dysplasia requiring orthopedic management.

**Recovery potential:** At least one neonatally severely affected individual showed improvement with age, losing the intellectual disability component by age 5 — suggesting some plasticity/reversibility is possible in a subset of cases, though this is based on a single reported observation and should not be generalized.

**Prognostic factors:** Variant type (LOF vs. missense) and domain location appear to correlate loosely with severity; the mildest phenotype (isolated adult-onset neuropathy) has so far only been associated with specific homozygous LOF or missense genotypes in outlier families, so genotype alone is an imperfect predictor.

---

## 12. Treatment

There is **no disease-specific or targeted therapy** for NEDNMS; management reported in the literature is entirely supportive/symptomatic:

- **Supportive care:** Gastrostomy tube feeding for failure to thrive; supplemental oxygen; tracheostomy (reported as reversible in some cases) — NCIT:C15747 (Supportive Care)
- **Orthopedic/surgical management:** For scoliosis and hip dysplasia/dislocation — NCIT:C15329 (Surgical Procedure) / NCIT:C16186 (Orthopedic Surgical Procedure)
- **Physical/rehabilitative therapy:** For hypotonia/spasticity and motor delay (inferred standard-of-care management, not explicitly detailed in source abstracts) — NCIT:C15302 (Physical Therapy) / NCIT:C15315 (Rehabilitation)
- **Genetic counseling:** Recommended given autosomal recessive inheritance and reported consanguinity/founder patterns — NCIT:C15240 (Genetic Counseling)
- **Incidental/unrelated treatment note:** One individual (Individual 1 in Kurolap et al. 2022) received eculizumab for seizures secondary to thrombosis attributed to an unrelated co-occurring CD55 deficiency — this is not an NRCAM-targeted therapy and should not be curated as a NEDNMS treatment.
- **Experimental/investigational:** No registered clinical trials (ClinicalTrials.gov / WHO ICTRP) for NRCAM-related NEDNMS were identified in this search.

No pharmacogenomic, gene-therapy, RNA-based, or targeted-molecular therapy has been reported or is in development specifically for NEDNMS as of this search.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies are established beyond standard **genetic counseling** for carrier parents (especially in consanguineous unions or founder populations such as the Amish and Libyan Jewish communities identified in the literature) regarding the 25% recurrence risk in future pregnancies under autosomal recessive inheritance, and the theoretical availability of carrier screening / prenatal diagnosis / preimplantation genetic testing once a familial variant is known. No population-level screening program, vaccine, or prophylactic medication applies.

---

## 14. Other Species / Natural Disease

No spontaneously occurring NRCAM-deficient disease has been reported in companion animals or wildlife (no OMIA entry identified in this search). All non-human data derive from engineered laboratory models (see Section 15).

**Orthologous gene:** *Nrcam* is conserved in mouse (MGI), zebrafish (*nrcama*/*nrcamb* paralogs, ZFIN), and other vertebrates as a core L1-family cell adhesion molecule.

---

## 15. Model Organisms

**Mouse (*Nrcam⁻/⁻* knockout):**
- No overt gross neuromuscular phenotype or obvious motor-behavior deficits at baseline.
- Delayed node-of-Ranvier formation and occasional "split nodes" in adult peripheral nerve, consistent with NrCAM's role (with gliomedin) in heminode-to-node maturation at the Schwann cell-axon interface.
- Behaviorally: impaired context-dependent fear conditioning; male *Nrcam* knockout mice display autism-related behaviors — impaired sociability, cognitive rigidity, and repetitive behavior.
- *Nrcam*-deficient cerebellar granule cells show abnormal neurite outgrowth and defective synaptogenesis (cited in Kurolap et al. 2022).
- Thalamic axon mistargeting has been linked to abnormal visual-evoked potentials in *Nrcam*-deficient mice, mechanistically mirroring the human optic-pathway findings.

**Zebrafish (CRISPR *nrcama* third-Fn-III-domain deletion mutant, generated in Kurolap et al. 2022):**
- 302-bp deletion removing the third Fn-III domain (the same domain where most human disease variants cluster).
- Significantly increased swimming activity in darkness versus wild-type (p=0.03).
- Trend toward increased α-tubulin-positive axonal fiber density in the dorsal telencephalon and a thickened anterior telencephalic commissure.
- Interpreted as recapitulating altered axonal projection patterning and abnormal activity-driven behavior, providing in vivo functional support for pathogenicity of Fn-III domain 3 variants.

**Model limitations:** The mouse knockout does not reproduce the severe multisystem human phenotype (developmental delay, spasticity, skeletal anomalies) despite recapitulating the peripheral nodal and some behavioral/synaptic phenotypes — a translational gap worth flagging as a `HUMAN_MODEL_MISMATCH` in any dismech curation of this entry, since basal mouse motor function is preserved despite null Nrcam, unlike the human hypotonia/spasticity phenotype.

**Applications:** Both models support the causal role of NRCAM loss-of-function in axon guidance/adhesion defects, nodal architecture, and behavioral abnormalities, and specifically implicate the Fn-III domain 3 region as functionally critical, consistent with human variant clustering.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested terms |
|---|---|
| Disease | OMIM:619833; gene OMIM:601581; MONDO ID to be confirmed via `runoak -i sqlite:obo:mondo` |
| Gene | hgnc:7994 (NRCAM) |
| Phenotypes (HP) | HP:0001263, HP:0001249, HP:0001252, HP:0001257, HP:0000762, HP:0001251, HP:0000252, HP:0001250, HP:0002650, HP:0001385, HP:0001761, HP:0005684, HP:0000648, HP:0000577, HP:0000238, HP:0002079, HP:0100716, HP:0001508 |
| GO (biological process) | GO:0007155, GO:0007411, GO:0031175, GO:0007416 |
| GO (cellular component) | GO:0033268, GO:0045202, GO:0005886 |
| CL | CL:0000540 (neuron), CL:0002573 (Schwann cell) |
| UBERON | UBERON:0000955, UBERON:0000010, UBERON:0002336, UBERON:0000940 |
| NCIT (treatment) | NCIT:C15747, NCIT:C15329, NCIT:C16186, NCIT:C15302, NCIT:C15315, NCIT:C15240 |

---

## Citation Note and Limitations

All primary clinical/molecular detail above derives from three peer-reviewed sources: **Kurolap A, et al. (2022)**, *Am J Hum Genet*, PMID:[35108495](https://pubmed.ncbi.nlm.nih.gov/35108495/) (PMCID: PMC8948158) — the founding case series; **Elahi Z, et al. (2023)**, *Mol Genet Genomic Med*, "Bi-allelic loss of function variant in the NRCAM gene is associated with motor-predominant axonal polyneuropathy; the second report"; and the pediatric-onset motor neuronopathy cohort paper (PMCID: PMC10808011) referencing additional isolated-neuropathy NRCAM cases. Direct PubMed/OMIM full-text fetches were blocked (HTTP 403) during this session; all figures and quotes above were relayed through search-engine-summarized excerpts of the cited PMC full texts rather than a first-hand read of the primary HTML — **before committing any of these snippets as dismech evidence items, curators must independently fetch and cache each PMID via `just fetch-reference`, and run `just count-verified-snippets` / `just validate-terms` to confirm exact-quote and ontology-term accuracy**, per the project's anti-hallucination SOP. Prevalence, gnomAD constraint metrics, and a confirmed MONDO CURIE were not resolved in this session and require direct database queries prior to KB entry.

**Sources:**
- [Entry - #619833 - NEURODEVELOPMENTAL DISORDER WITH NEUROMUSCULAR AND SKELETAL ABNORMALITIES; NEDNMS - OMIM](https://omim.org/entry/619833)
- [Clinical Synopsis - #619833 - OMIM](https://omim.org/clinicalSynopsis/619833)
- [NEURONAL CELL ADHESION MOLECULE; NRCAM - OMIM #601581](https://omim.org/entry/601581)
- [Bi-allelic variants in neuronal cell adhesion molecule cause a neurodevelopmental disorder characterized by developmental delay, hypotonia, neuropathy/spasticity - PubMed (PMID:35108495)](https://pubmed.ncbi.nlm.nih.gov/35108495/)
- [PMC8948158 - full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8948158/)
- [Bi-allelic loss of function variant in the NRCAM gene is associated with motor-predominant axonal polyneuropathy; the second report - Elahi et al. 2023, Molecular Genetics & Genomic Medicine](https://onlinelibrary.wiley.com/doi/full/10.1002/mgg3.2131)
- [Novel and nano-rare genetic causes of paediatric-onset motor neuronopathies - PMC10808011](https://pmc.ncbi.nlm.nih.gov/articles/PMC10808011/)
- [NRCAM Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=NRCAM)
- [Neuronal cell adhesion molecule - UniProt Q92823](https://www.uniprot.org/uniprotkb/Q92823/entry)
- [The role of NrCAM in neural development and disorders—Beyond a simple glue in the brain - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1044743111002739)
- [Gene: NRCAM (Childhood onset hereditary spastic paraplegia) - Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/568/gene/NRCAM/)
- [Association of the neuronal cell adhesion molecule (NRCAM) gene variants with autism - IJNP](https://academic.oup.com/ijnp/article/12/1/1/626999)
- [NRCAM variant defined by microexon skipping is a targetable cell surface proteoform in high-grade gliomas - Cell Reports](https://www.cell.com/cell-reports/fulltext/S2211-1247(25)00870-8)
- [Mondo Disease Ontology - Monarch Initiative](https://mondo.monarchinitiative.org/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.