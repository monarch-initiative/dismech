---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:00:53.642701'
end_time: '2025-12-15T09:08:14.659411'
duration_seconds: 441.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bardet-Biedl Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Bardet-Biedl Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Bardet-Biedl Syndrome**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Bardet-Biedl Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Bardet-Biedl Syndrome**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Bardet–Biedl Syndrome (BBS)
- MONDO ID: MONDO:0012746
- Category: Genetic (autosomal recessive ciliopathy)

## Pathophysiology Description
Bardet–Biedl syndrome is a prototypical non-motile ciliopathy caused by defects in proteins that localize predominantly to the primary cilium and its basal body/transition zone, leading to impaired ciliary compartmentalization and trafficking of membrane and signaling proteins across tissues including retina, kidney, and hypothalamus (energy balance) (melluso2023bardetbiedlsyndromecurrent pages 1-3). Mechanistically, BBS proteins assemble into the octameric BBSome with support from a dedicated chaperonin-like complex (BBS6/MKKS, BBS10, BBS12) and interface with intraflagellar transport (IFT) to regulate ciliary entry/retention and retrieval of G-protein–coupled receptors (GPCRs) and other membrane cargos (melluso2023bardetbiedlsyndromecurrent pages 1-3, melluso2023bardetbiedlsyndromecurrent pages 17-18). In photoreceptors, disruption of BBSome/IFT-mediated trafficking across the connecting cilium (“ciliary gate”) causes mislocalization of outer-segment proteins and triggers cell death and retinal degeneration (delvallee2023retinaldegenerationanimal pages 2-4). The multisystem phenotype reflects shared dependence on ciliary signaling and compartmentalization across organs (melluso2023bardetbiedlsyndromecurrent pages 1-3).

Direct quotes highlighting core mechanisms:
- “The BBSome is defined as an octameric complex (BBS1/2/4/5/7/8/9/BBIP1) whose assembly requires chaperonin-like proteins (BBS6, BBS10, BBS12)… A functional link to the BBS3 GTPase enables intraflagellar transport (IFT)” (DOI: 10.2147/TCRM.S338653) (melluso2023bardetbiedlsyndromecurrent pages 1-3).
- In photoreceptors “more than 1000 rhodopsin molecules [are] transiting per second… Defective IFT or BBSome-mediated trafficking causes abnormal protein trafficking across the [connecting cilium], provoking proapoptotic reactions and photoreceptor degeneration” (DOI: 10.1101/cshperspect.a041303) (delvallee2023retinaldegenerationanimal pages 2-4).

## 1. Core Pathophysiology
- Primary mechanisms: impaired ciliary trafficking and gatekeeping due to BBSome/chaperonin dysfunction; defective cooperation with IFT-A/IFT-B disrupts anterograde/retrograde transport of ciliary cargos (melluso2023bardetbiedlsyndromecurrent pages 1-3, delvallee2023retinaldegenerationanimal pages 2-4).
- Dysregulated pathways: ciliary GPCR signaling (e.g., leptin, serotonin 5-HT2C) and related neuronal energy-balance pathways; broad perturbation of ciliary signal transduction and proteostasis within the ciliary compartment (melluso2023bardetbiedlsyndromecurrent pages 14-15, melluso2023bardetbiedlsyndromecurrent pages 1-3).
- Affected cellular processes: ciliary cargo sorting, membrane protein localization, GPCR trafficking, transition-zone gating, and IFT-driven transport; secondary degeneration from protein mislocalization in highly polarized cells (photoreceptors) (delvallee2023retinaldegenerationanimal pages 2-4, melluso2023bardetbiedlsyndromecurrent pages 1-3, melluso2023bardetbiedlsyndromecurrent pages 14-15).

## 2. Key Molecular Players
- Genes/Proteins (HGNC): BBS1, BBS2, BBS4, BBS5, BBS7, BBS8, BBS9, BBIP1 (BBS18), BBS6/MKKS, BBS10, BBS12 (BBS chaperonins); ARL6/BBS3 (small GTPase recruiting BBSome); IFT-B (e.g., IFT25/IFT27, IFT74/IFT81), IFT-A subunits (melluso2023bardetbiedlsyndromecurrent pages 1-3, delvallee2023retinaldegenerationanimal pages 2-4, lazareva2023anevaluationof pages 16-18).
  - Evidence: “Multiple BBSome components… and chaperonin-complex members… are explicitly annotated, indicating roles in BBSome assembly and… ciliary trafficking… [and] intraflagellar transport proteins (IFT27, IFT172, IFT74)” (DOI: 10.1080/14656566.2023.2199152) (lazareva2023anevaluationof pages 16-18).
- Chemical entities (CHEBI)/drugs: Setmelanotide, an MC4R agonist, reduces hyperphagia and weight in BBS; additional small-molecule strategies include read-through agents (e.g., ataluren/amlexanox) for nonsense alleles (melluso2023bardetbiedlsyndromecurrent pages 12-14, lazareva2023anevaluationof pages 8-11, lazareva2023anevaluationof pages 16-18).
- Cell types (CL): Photoreceptors (rods/cones), hypothalamic POMC neurons, renal tubular epithelial cells (delvallee2023retinaldegenerationanimal pages 2-4, melluso2023bardetbiedlsyndromecurrent pages 14-15).
- Anatomical locations (UBERON): Retina (photoreceptor outer/inner segments, connecting cilium), kidney (renal tubules), hypothalamus (arcuate nucleus/POMC neurons) (delvallee2023retinaldegenerationanimal pages 2-4, melluso2023bardetbiedlsyndromecurrent pages 14-15).

## 3. Biological Processes (GO terms; disrupted)
- Ciliary transport and organization: cilium assembly (GO:0060271), ciliary transport (GO:0042073), protein localization to cilium (GO:0061512), ciliary GPCR signaling (e.g., response to peptide hormone) (melluso2023bardetbiedlsyndromecurrent pages 1-3, delvallee2023retinaldegenerationanimal pages 2-4, melluso2023bardetbiedlsyndromecurrent pages 14-15).
- Intraflagellar transport: anterograde IFT (GO:0035721), retrograde IFT (GO:0035720) (delvallee2023retinaldegenerationanimal pages 2-4).
- Membrane protein trafficking and proteostasis: protein targeting to membrane (GO:0006612); regulation of receptor localization and signaling (melluso2023bardetbiedlsyndromecurrent pages 14-15).
- Photoreceptor maintenance and visual perception: phototransduction (GO:0007602); outer segment organization (delvallee2023retinaldegenerationanimal pages 2-4).

## 4. Cellular Components (GO/CL/UBERON)
- Primary cilium (GO:0005929), basal body (GO:0005932), transition zone/connecting cilium (GO:0035869), periciliary membrane compartment (GO:0031526) (delvallee2023retinaldegenerationanimal pages 2-4, melluso2023bardetbiedlsyndromecurrent pages 1-3).
- Photoreceptor outer segment (GO:0001750) and inner segment (GO:0001917) (delvallee2023retinaldegenerationanimal pages 2-4).
- BBSome complex (GO:0034464), IFT-A/B complexes (GO:0030990/GO:0030991) (melluso2023bardetbiedlsyndromecurrent pages 1-3, delvallee2023retinaldegenerationanimal pages 2-4).

## 5. Disease Progression
- Initiation: biallelic variants in BBSome/chaperonin/IFT-associated genes impair BBSome assembly and BBSome–IFT coupling, compromising ciliary entry/retention/retrieval of key receptors and channels (melluso2023bardetbiedlsyndromecurrent pages 1-3, lazareva2023anevaluationof pages 16-18).
- Cellular dysfunction: disrupted trafficking across the transition zone/connecting cilium causes mislocalization of ciliary GPCRs and photoreceptor outer-segment proteins; in photoreceptors, continuous high-throughput trafficking demand makes them particularly vulnerable, leading to degeneration (delvallee2023retinaldegenerationanimal pages 2-4).
- Organ-level manifestations: progressive rod–cone dystrophy with early nyctalopia and vision loss; renal concentrating/diluting defects and progressive CKD; severe hyperphagia/obesity from hypothalamic ciliary signaling disruption (e.g., leptin/5-HT2C/MC4R axis) (melluso2023bardetbiedlsyndromecurrent pages 14-15, lazareva2023anevaluationof pages 8-11).

## 6. Phenotypic Manifestations (HP terms)
- Retinal dystrophy/rod–cone dystrophy (HP:0000510), nyctalopia (HP:0000662), progressive vision loss (HP:0000572) (delvallee2023retinaldegenerationanimal pages 2-4, lazareva2023anevaluationof pages 16-18).
- Polydactyly (HP:0010442), postaxial (HP:0100259) (lazareva2023anevaluationof pages 16-18).
- Obesity (HP:0001513), hyperphagia (HP:0002591) (lazareva2023anevaluationof pages 8-11, lazareva2023anevaluationof pages 16-18).
- Renal anomalies/CKD (HP:0000077) and urine concentration defects (HP:0004743) (melluso2023bardetbiedlsyndromecurrent pages 14-15).
- Learning difficulties (HP:0001328), hypogonadism (HP:0000135) (lazareva2023anevaluationof pages 16-18).

## Tissue-Specific Mechanisms
- Retina: Photoreceptor outer segments are modified cilia. The connecting cilium is a stringent gate; failure of BBSome/IFT trafficking causes mislocalization (e.g., rhodopsin) and photoreceptor death. Quote: “Defective IFT or BBSome-mediated trafficking… provoking proapoptotic reactions and photoreceptor degeneration” (DOI: 10.1101/cshperspect.a041303) (delvallee2023retinaldegenerationanimal pages 2-4).
- Kidney: Renal tubular epithelial cilia regulate solute handling and signaling; BBS-related ciliary dysfunction correlates with concentrating/diluting defects and progressive renal disease (AQP2/UMOD changes), consistent with a ciliopathy framework (melluso2023bardetbiedlsyndromecurrent pages 14-15).
- Hypothalamus/metabolism: Ciliary localization and trafficking of GPCRs (e.g., serotonin 5‑HT2C, leptin receptor) in POMC neurons are BBSome-dependent; mistrafficking impairs melanocortin signaling and contributes to hyperphagia and obesity (melluso2023bardetbiedlsyndromecurrent pages 14-15). Setmelanotide (MC4R agonist) pharmacologically restores downstream signaling, improving weight and hunger measures (lazareva2023anevaluationof pages 8-11, lazareva2023anevaluationof pages 16-18).

## Recent Developments and Latest Research (prioritized 2023–2024)
- 2023 review and updates: Comprehensive overviews emphasize BBSome–IFT cooperation, tissue mechanisms, and emerging therapies, with curated references to newer mechanistic work on IFT–BBS interfaces and ciliary trafficking (DOI: 10.2147/TCRM.S338653; Jan 2023) (melluso2023bardetbiedlsyndromecurrent pages 17-18, melluso2023bardetbiedlsyndromecurrent pages 1-3).
- Retinal ciliopathy mechanisms: Authoritative 2023 perspective details modular ciliary organization (BBSome, IFT-A/B, transition zone), high flux of photoreceptor cargo, and how trafficking failure leads to degeneration (DOI: 10.1101/cshperspect.a041303; Jan 2023) (delvallee2023retinaldegenerationanimal pages 2-4).
- Therapeutics for BBS obesity: 2023 expert evaluation consolidates clinical data for setmelanotide in BBS, with mechanistic rationale via MC4R pathway rescue and details of diagnostic criteria—supporting translation of ciliary signaling knowledge to treatment (DOI: 10.1080/14656566.2023.2199152; Apr 2023) (lazareva2023anevaluationof pages 8-11, lazareva2023anevaluationof pages 16-18).

Note: Although additional 2023–2024 mechanistic advances (e.g., BBSome ubiquitylation, TOM1L2-mediated ubiquitin recognition, refined IFT-B interfaces, EV/ectocytosis, and cAMP microdomains in cilia) are widely reported in the field, they were not present in the retrieved evidence excerpts and thus are not detailed here.

## Current Applications and Real-World Implementations
- Setmelanotide (MC4R agonist) for BBS-associated hyperphagia/obesity: clinical use with evidence of weight loss and reduced hunger burden in BBS, aligning with hypothalamic ciliary signaling pathophysiology (DOI: 10.1080/14656566.2023.2199152; Apr 2023) (lazareva2023anevaluationof pages 8-11, lazareva2023anevaluationof pages 16-18).
- Gene- and RNA-targeted strategies under investigation: readthrough therapy (ataluren/amlexanox) for nonsense alleles restored BBS2 and ciliogenesis in preclinical models; splicing correction tactics (snRNA/ASO) proposed; ocular gene therapy paradigms inform BBS pipelines (DOI: 10.2147/TCRM.S338653; Jan 2023) (melluso2023bardetbiedlsyndromecurrent pages 12-14).

## Expert Opinions and Authoritative Analyses
- Therapeutics and Clinical Risk Management review (Melluso et al., 2023) provides a consensus-style synthesis across molecular mechanisms, clinical spectrum, and translational avenues, underscoring the centrality of ciliary dysfunction and BBSome–IFT defects to pathogenesis (DOI: 10.2147/TCRM.S338653) (melluso2023bardetbiedlsyndromecurrent pages 1-3, melluso2023bardetbiedlsyndromecurrent pages 12-14, melluso2023bardetbiedlsyndromecurrent pages 17-18).
- Cold Spring Harbor Perspectives in Medicine (Delvallée & Dollfus, 2023) offers an organ-specific, mechanistic retina focus, highlighting the connecting cilium gate and extreme trafficking demands as the proximate cause of photoreceptor vulnerability (DOI: 10.1101/cshperspect.a041303) (delvallee2023retinaldegenerationanimal pages 2-4).

## Relevant Statistics and Data from Recent Studies
- Diagnostic criteria and frequency of features (summarized): primary features—retinal degeneration (~93%), polydactyly (63–81%), obesity (72–92%), genital anomalies, learning difficulties, renal anomalies—used in standard diagnostic rules (four primary or three primary plus two secondary features) (DOI: 10.1080/14656566.2023.2199152) (lazareva2023anevaluationof pages 16-18).
- Therapeutic outcomes: clinical analyses of setmelanotide in BBS report reductions in hyperphagia and body weight, positioning MC4R activation as a targeted approach for BBS-associated obesity (DOI: 10.1080/14656566.2023.2199152) (lazareva2023anevaluationof pages 8-11, lazareva2023anevaluationof pages 16-18).

## Gene/Protein Annotations (selected)
- BBSome core: BBS1; BBS2; BBS4; BBS5; BBS7; BBS8; BBS9; BBIP1/BBS18 (GO:0034464) (melluso2023bardetbiedlsyndromecurrent pages 1-3).
- Chaperonin-like assembly factors: BBS6/MKKS; BBS10; BBS12 (GO:0005813 basal body localization; BBSome assembly) (melluso2023bardetbiedlsyndromecurrent pages 1-3).
- ARL6/BBS3: GTPase recruiting BBSome to membranes (GO:0035091) (melluso2023bardetbiedlsyndromecurrent pages 1-3, delvallee2023retinaldegenerationanimal pages 2-4).
- IFT components: IFT25/IFT27 (interface with BBSome); IFT74/IFT81 (IFT-B) (delvallee2023retinaldegenerationanimal pages 2-4, lazareva2023anevaluationof pages 16-18).

## Ontology Mappings
- GO Biological Process: cilium assembly (GO:0060271); protein localization to cilium (GO:0061512); intraflagellar transport (GO:0042073); photoreceptor cell maintenance (GO:0045494).
- GO Cellular Component: primary cilium (GO:0005929); ciliary transition zone (GO:0035869); photoreceptor outer segment (GO:0001750); BBSome (GO:0034464); IFT-A/B complexes (GO:0030990/GO:0030991).
- HPO Phenotypes: HP:0000510 (Rod–cone dystrophy); HP:0000662 (Nyctalopia); HP:0001513 (Obesity); HP:0002591 (Hyperphagia); HP:0000077 (Renal anomaly); HP:0010442 (Postaxial polydactyly).
- CL Cell Types: CL:0000746 (photoreceptor cell); CL:0002607 (hypothalamic neuron); CL:0002306 (renal epithelial cell).
- UBERON Anatomy: UBERON:0000966 (retina); UBERON:0002048 (kidney); UBERON:0001898 (hypothalamus).
- CHEBI Chemicals: CHEBI:61093 (setmelanotide; MC4R agonist) [drug class mapping; used clinically in BBS obesity].

## Evidence Items
1) Melluso A, et al. Bardet–Biedl Syndrome: Current Perspectives and Clinical Outlook. Therapeutics and Clinical Risk Management. Jan 2023. DOI: 10.2147/TCRM.S338653; URL: https://doi.org/10.2147/TCRM.S338653 (melluso2023bardetbiedlsyndromecurrent pages 1-3, melluso2023bardetbiedlsyndromecurrent pages 12-14, melluso2023bardetbiedlsyndromecurrent pages 17-18, melluso2023bardetbiedlsyndromecurrent pages 14-15).
2) Delvallée C, Dollfus H. Retinal Degeneration Animal Models in Bardet–Biedl Syndrome and Related Ciliopathies. Cold Spring Harb Perspect Med. Jan 2023. DOI: 10.1101/cshperspect.a041303; URL: https://doi.org/10.1101/cshperspect.a041303 (delvallee2023retinaldegenerationanimal pages 2-4).
3) Lazareva J, Brady SM, Yanovski JA. An evaluation of setmelanotide injection for chronic weight management in adult and pediatric patients with obesity due to Bardet–Biedl syndrome. Expert Opin Pharmacother. Apr 2023. DOI: 10.1080/14656566.2023.2199152; URL: https://doi.org/10.1080/14656566.2023.2199152 (lazareva2023anevaluationof pages 8-11, lazareva2023anevaluationof pages 16-18).

Limitations: Additional 2024 advances (e.g., revised European consensus diagnostic criteria; detailed molecular updates on ubiquitylation and ciliary ubiquitin readers; EV/ectocytosis and cAMP microdomains) are recognized in the field but were not included in the retrieved excerpts; thus, mechanistic claims here are limited to the cited 2023 sources and their referenced evidence (melluso2023bardetbiedlsyndromecurrent pages 17-18).

References

1. (melluso2023bardetbiedlsyndromecurrent pages 1-3): Andrea Melluso, Floriana Secondulfo, Giovanna Capolongo, Giovambattista Capasso, and Miriam Zacchia. Bardet-biedl syndrome: current perspectives and clinical outlook. Therapeutics and Clinical Risk Management, 19:115-132, Jan 2023. URL: https://doi.org/10.2147/tcrm.s338653, doi:10.2147/tcrm.s338653. This article has 91 citations and is from a peer-reviewed journal.

2. (melluso2023bardetbiedlsyndromecurrent pages 17-18): Andrea Melluso, Floriana Secondulfo, Giovanna Capolongo, Giovambattista Capasso, and Miriam Zacchia. Bardet-biedl syndrome: current perspectives and clinical outlook. Therapeutics and Clinical Risk Management, 19:115-132, Jan 2023. URL: https://doi.org/10.2147/tcrm.s338653, doi:10.2147/tcrm.s338653. This article has 91 citations and is from a peer-reviewed journal.

3. (delvallee2023retinaldegenerationanimal pages 2-4): Clarisse Delvallée and Hélène Dollfus. Retinal degeneration animal models in bardet-biedl syndrome and related ciliopathies. Cold Spring Harbor perspectives in medicine, 13 1:a041303, Jan 2023. URL: https://doi.org/10.1101/cshperspect.a041303, doi:10.1101/cshperspect.a041303. This article has 12 citations and is from a peer-reviewed journal.

4. (melluso2023bardetbiedlsyndromecurrent pages 14-15): Andrea Melluso, Floriana Secondulfo, Giovanna Capolongo, Giovambattista Capasso, and Miriam Zacchia. Bardet-biedl syndrome: current perspectives and clinical outlook. Therapeutics and Clinical Risk Management, 19:115-132, Jan 2023. URL: https://doi.org/10.2147/tcrm.s338653, doi:10.2147/tcrm.s338653. This article has 91 citations and is from a peer-reviewed journal.

5. (lazareva2023anevaluationof pages 16-18): Julia Lazareva, Sheila M. Brady, and Jack A. Yanovski. An evaluation of setmelanotide injection for chronic weight management in adult and pediatric patients with obesity due to bardet–biedl syndrome. Expert Opinion on Pharmacotherapy, 24:667-674, Apr 2023. URL: https://doi.org/10.1080/14656566.2023.2199152, doi:10.1080/14656566.2023.2199152. This article has 13 citations and is from a peer-reviewed journal.

6. (melluso2023bardetbiedlsyndromecurrent pages 12-14): Andrea Melluso, Floriana Secondulfo, Giovanna Capolongo, Giovambattista Capasso, and Miriam Zacchia. Bardet-biedl syndrome: current perspectives and clinical outlook. Therapeutics and Clinical Risk Management, 19:115-132, Jan 2023. URL: https://doi.org/10.2147/tcrm.s338653, doi:10.2147/tcrm.s338653. This article has 91 citations and is from a peer-reviewed journal.

7. (lazareva2023anevaluationof pages 8-11): Julia Lazareva, Sheila M. Brady, and Jack A. Yanovski. An evaluation of setmelanotide injection for chronic weight management in adult and pediatric patients with obesity due to bardet–biedl syndrome. Expert Opinion on Pharmacotherapy, 24:667-674, Apr 2023. URL: https://doi.org/10.1080/14656566.2023.2199152, doi:10.1080/14656566.2023.2199152. This article has 13 citations and is from a peer-reviewed journal.