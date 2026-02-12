---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-30T19:25:27.385902'
end_time: '2026-01-30T19:29:54.230906'
duration_seconds: 266.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SADDAN
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 15
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** SADDAN
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **SADDAN**.
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
- **Disease Name:** SADDAN
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **SADDAN**.
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


Plan
Objective 1 (completed): Define SADDAN and establish nomenclature, causative gene, and canonical variant.
Objective 2: Identify recent authoritative sources on FGFR3 signaling and SADDAN mechanisms.
Objective 3: Extract core molecular and cellular mechanisms for SADDAN.
Objective 4: Map key molecular players to ontology terms (HGNC, GO, CL, UBERON, CHEBI) and compile disrupted processes/components.
Objective 5: Outline disease progression and phenotype associations (HPO).
Objective 6: Summarize applications, expert perspectives, and relevant statistics with URLs and dates.
Objective 7: Synthesize into a comprehensive, citation-rich research report.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Severe achondroplasia with developmental delay and acanthosis nigricans (SADDAN)
- MONDO ID: MONDO_0014658
- Category: Mendelian (autosomal dominant; monoallelic)
- Primary target-gene association: FGFR3 (ENSG00000068078; HGNC:3689) (OpenTargets Search: SADDAN,severe achondroplasia with developmental delay and acanthosis nigricans)

Pathophysiology description
SADDAN is an FGFR3-driven skeletal dysplasia distinguished by a triad of severe achondroplasia, neurodevelopmental delay, and acanthosis nigricans. OpenTargets maps the disease to MONDO_0014658 and Orphanet_85165, with a single, high-confidence associated target, FGFR3, supported by multiple genetic evidence sources (including Genomics England, UniProt variants, EVA, and Orphanet). The allelic requirement is monoallelic autosomal, consistent with gain-of-function pathogenesis (OpenTargets query; Nucleic Acids Research platform description; accessed 2025; see context) (OpenTargets Search: SADDAN,severe achondroplasia with developmental delay and acanthosis nigricans).

Causative variant and activation class
- Canonical variant: FGFR3 p.Lys650Met (K650M) in the activation loop of the tyrosine kinase domain; repeatedly described as the defining SADDAN allele and a highly activating, ligand-independent gain-of-function mutation. The skeletal dysplasia spectrum caused by FGFR3 shows “graded activation” correlating mutation and clinical severity, with activation-loop Lys650 substitutions among the strongest activators (urls/years in cited works) (reintjes2013activatingsomaticfgfr2 pages 8-8, legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2).
- Quote (contextualized): Publications cited in the retrieved evidence summarize that activation-loop Lys650 mutations produce “profound ligand-independent kinase activation” and that “distinct missense mutations of the FGFR3 lys650 codon modulate receptor kinase activation and the severity of the skeletal dysplasia phenotype” (citations aggregated within the PLoS ONE 2013 article’s reference trail; Mar 2013; https://doi.org/10.1371/journal.pone.0060264) (reintjes2013activatingsomaticfgfr2 pages 8-8).

Core signaling mechanisms
- Upstream: FGFR3 dimerization/auto-phosphorylation with activation-loop stabilization in K650M drives constitutive signaling (general FGFR3 mechanism summarized) (Feb 2001; https://doi.org/10.1182/blood.v97.3.729) (chesi2001activatedfibroblastgrowth pages 1-2).
- Downstream pathways engaged by mutant FGFR3 in growth plate chondrocytes include MAPK/ERK, STAT (notably STAT1), PI3K–AKT, and PLCγ. Experimental inhibition with the FGFR inhibitor NVP-BGJ398 (infigratinib) in mouse models reduced FGFR3 phosphorylation and suppressed multiple downstream axes, including MAPK and STAT1, in ex vivo growth plate systems and chondrocyte cultures (May 2016; https://doi.org/10.1172/JCI83926) (komlaebri2016tyrosinekinaseinhibitor pages 1-3, komlaebri2016tyrosinekinaseinhibitor pages 13-14).
- FGFR3 hyperactivation in growth plate cartilage is a negative regulator of endochondral bone growth, altering chondrocyte proliferation and differentiation. Reviews cited in the Bone 2020 article summarize that achondroplasia-spectrum FGFR3 mutations disrupt growth plate signaling and chondrogenesis; graded receptor activation correlates with severity (Dec 2020; https://doi.org/10.1016/j.bone.2020.115579) (legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2).

Growth plate cellular effects
- Proliferation and hypertrophic differentiation: FGFR3 activation shifts the balance toward growth arrest and impaired hypertrophic maturation, with SOX9 misregulation implicated in defective chondrocyte differentiation. STAT1 has been linked to increased apoptosis/reduced proliferation in mutant contexts; constitutive MEK1 activation recapitulates an achondroplasia-like phenotype independently of STAT1, underscoring a major role for MAPK signaling (May 2016; https://doi.org/10.1172/JCI83926) (komlaebri2016tyrosinekinaseinhibitor pages 13-14). These mechanisms align with the severe endochondral ossification defects in SADDAN.

Skin and nervous system involvement
- Acanthosis nigricans: Although direct SADDAN-specific skin-pathway studies were not retrieved in the current evidence set, FGFR-family signaling is known to influence keratinocyte and epidermal biology. The high-level, ligand-independent activity of K650M plausibly contributes cell-autonomously to epidermal hyperplasia and melanocytic/keratinocytic crosstalk typical of acanthosis nigricans; this is consistent with the general principle that FGFR activation can drive proliferative signaling in different tissues (Feb 2001; https://doi.org/10.1182/blood.v97.3.729; conceptual extension from high-activation K650M class) (chesi2001activatedfibroblastgrowth pages 1-2, reintjes2013activatingsomaticfgfr2 pages 8-8).
- Neurodevelopmental delay: FGFR3 is highly expressed in the developing central nervous system (CNS), and activating mutations alter developmental signaling programs. The Blood 2001 study highlights FGFR3 expression in developing CNS and skeletal precursors, supporting biological plausibility that highly activating K650M perturbs neurodevelopmental pathways and leads to developmental delay (Feb 2001; https://doi.org/10.1182/blood.v97.3.729) (chesi2001activatedfibroblastgrowth pages 1-2). Detailed, SADDAN-specific neural mechanistic papers were not captured by the current retrieval and represent a gap requiring targeted literature access.

Disease progression: from trigger to phenotype
- Molecular trigger: monoallelic FGFR3 K650M causes high, ligand-independent kinase activation (reintjes2013activatingsomaticfgfr2 pages 8-8, legeaimallet2020noveltherapeuticapproaches pages 1-2).
- Signaling cascade: constitutive autophosphorylation → MAPK/ERK, STAT (STAT1), PI3K–AKT, PLCγ activation in chondrocytes (komlaebri2016tyrosinekinaseinhibitor pages 1-3, komlaebri2016tyrosinekinaseinhibitor pages 13-14).
- Cellular effects in growth plate: reduced proliferation, increased apoptosis (STAT1-associated), impaired transition to hypertrophy with persistent SOX9; net inhibition of endochondral bone elongation (komlaebri2016tyrosinekinaseinhibitor pages 13-14).
- Tissue/organ outcomes: severe rhizomelic limb shortening, craniofacial dysmorphology consistent with FGFR3 GOF, narrow foramen magnum/spinal canal in severe forms; epidermal hyperplasia with acanthosis nigricans; neurodevelopmental delay tied to FGFR3 roles in CNS development (legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2, chesi2001activatedfibroblastgrowth pages 1-2).

Key molecular players
- Gene/protein: FGFR3 (HGNC:3689; ENSG00000068078) (OpenTargets Search: SADDAN,severe achondroplasia with developmental delay and acanthosis nigricans).
- Variant: FGFR3 p.Lys650Met (K650M), activation loop, tyrosine kinase domain (reintjes2013activatingsomaticfgfr2 pages 8-8, legeaimallet2020noveltherapeuticapproaches pages 1-2).
- Downstream signaling nodes: MAPK/ERK cascade; STAT1; PI3K–AKT; PLCγ; SOX9 regulation during chondrocyte maturation (komlaebri2016tyrosinekinaseinhibitor pages 1-3, komlaebri2016tyrosinekinaseinhibitor pages 13-14).
- Chemical entities with mechanistic relevance: Infigratinib (NVP-BGJ398), a pan-FGFR inhibitor that reduced FGFR3 phosphorylation and downstream signaling in preclinical models (May 2016; https://doi.org/10.1172/JCI83926) (komlaebri2016tyrosinekinaseinhibitor pages 1-3).
- Primary cell types: growth plate chondrocytes (resting, proliferative, hypertrophic); keratinocytes and melanocytes in epidermis (for acanthosis nigricans); neural progenitors/neurons for neurodevelopment (chesi2001activatedfibroblastgrowth pages 1-2, komlaebri2016tyrosinekinaseinhibitor pages 13-14).
- Anatomical locations: growth plate cartilage of long bones; craniofacial skeleton; epidermis; central nervous system (chesi2001activatedfibroblastgrowth pages 1-2, legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2).

Dysregulated biological processes (candidate GO annotations)
- Fibroblast growth factor receptor signaling pathway; transmembrane receptor protein tyrosine kinase signaling.
- MAPK cascade; ERK1/2 signaling; JAK/STAT signaling; PI3K–AKT signaling; phospholipase C-activating signaling.
- Endochondral ossification; chondrocyte proliferation; chondrocyte differentiation (hypertrophic transition); regulation of apoptosis.
- Epidermal cell proliferation and keratinization (by inference from FGFR signaling biology; SADDAN-specific confirmation required) (komlaebri2016tyrosinekinaseinhibitor pages 1-3, chesi2001activatedfibroblastgrowth pages 1-2, legeaimallet2020noveltherapeuticapproaches pages 5-5, komlaebri2016tyrosinekinaseinhibitor pages 13-14, legeaimallet2020noveltherapeuticapproaches pages 1-2).

Cellular components (candidate GO CC annotations)
- FGFR3 localized at plasma membrane; signaling complexes in the cytosol; nuclear effectors (e.g., STAT1) after activation. Growth plate extracellular matrix is affected indirectly through altered chondrocyte maturation (komlaebri2016tyrosinekinaseinhibitor pages 1-3, chesi2001activatedfibroblastgrowth pages 1-2, komlaebri2016tyrosinekinaseinhibitor pages 13-14).

Disease progression and stages
- Prenatal/early postnatal: constitutive FGFR3 signaling impairs endochondral ossification; severe limb shortening and craniofacial features evident early (legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2).
- Early childhood: progressive skeletal complications, foramen magnum/spinal canal narrowing risk (extrapolated from FGFR3-spectrum data), onset of acanthosis nigricans, neurodevelopmental delay manifests (legeaimallet2020noveltherapeuticapproaches pages 5-5, chesi2001activatedfibroblastgrowth pages 1-2).
- Later outcomes: persistent short stature with significant functional and orthopedic burden; skin findings and neurological sequelae vary (legeaimallet2020noveltherapeuticapproaches pages 5-5, chesi2001activatedfibroblastgrowth pages 1-2).

Phenotype associations (HPO terms; mechanistic links)
- Disproportionate short stature (HP:0004322), Rhizomelia (HP:0000912) due to impaired chondrocyte proliferation/hypertrophy and curtailed endochondral ossification (komlaebri2016tyrosinekinaseinhibitor pages 13-14, legeaimallet2020noveltherapeuticapproaches pages 5-5).
- Macrocephaly/craniofacial dysmorphology (HP:0000256, multiple craniofacial HPOs) consistent with FGFR3 GOF effects (legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2).
- Developmental delay (HP:0001263) aligned with FGFR3 expression in developing CNS and potential signaling dysregulation (chesi2001activatedfibroblastgrowth pages 1-2).
- Acanthosis nigricans (HP:0000956) plausibly arising from epidermal hyperproliferation driven by aberrant RTK signaling (chesi2001activatedfibroblastgrowth pages 1-2, reintjes2013activatingsomaticfgfr2 pages 8-8).

Current applications and implementations
- FGFR pathway inhibition: Infigratinib (NVP-BGJ398) reduced FGFR3 phosphorylation and corrected signaling in preclinical models of FGFR3-related dwarfism, supporting target validity for pharmacologic modulation of the FGFR3 axis (May 2016; https://doi.org/10.1172/JCI83926) (komlaebri2016tyrosinekinaseinhibitor pages 1-3). This aligns with the broader therapeutic exploration of FGFR pathway modulators across diseases.
- FGFR3-targeted skeletal dysplasia strategies: Reviews highlight multiple approaches to normalize growth plate signaling in FGFR3 GOF disorders, including ligand traps, FGFR inhibitors, and downstream pathway modulation (Dec 2020; https://doi.org/10.1016/j.bone.2020.115579) (legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2).

Expert opinions and analysis
- Bone 2020 review synthesizes FGFR3 pathobiology as a negative regulator of bone growth, emphasizing graded mutation activation and growth plate signaling derangements as central to disease; this conceptual framework supports SADDAN’s severe end of the spectrum (Dec 2020; https://doi.org/10.1016/j.bone.2020.115579) (legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2).
- Mechanistic breadth: Evidence across systems (developmental bone, CNS, and oncology) converges on FGFR3 as a potent RTK whose constitutive activation can drive proliferation, differentiation shifts, and survival changes depending on cellular context, explaining SADDAN’s skeletal and extra-skeletal features (Feb 2001; https://doi.org/10.1182/blood.v97.3.729) (chesi2001activatedfibroblastgrowth pages 1-2).

Relevant statistics and data
- OpenTargets association scores between SADDAN and FGFR3 are high (approximately 0.72–0.82 across disease entries), with multiple genetic evidence items and PMIDs listed in the platform’s evidence set (platform updated through 2025) (OpenTargets Search: SADDAN,severe achondroplasia with developmental delay and acanthosis nigricans).
- Preclinical pharmacology: FGFR inhibitor exposure in ex vivo/murine models reduces FGFR3 phosphorylation and downstream markers (MAPK, STAT1) and functionally improves bone growth phenotypes (May 2016; https://doi.org/10.1172/JCI83926) (komlaebri2016tyrosinekinaseinhibitor pages 1-3).

Ontology-ready annotations
- Gene/protein: FGFR3 (HGNC:3689; ENSG00000068078) (OpenTargets Search: SADDAN,severe achondroplasia with developmental delay and acanthosis nigricans).
- Variants: FGFR3 p.Lys650Met (K650M), canonical for SADDAN (reintjes2013activatingsomaticfgfr2 pages 8-8, legeaimallet2020noveltherapeuticapproaches pages 1-2).
- Biological processes (GO BP; examples): fibroblast growth factor receptor signaling pathway; MAPK cascade; regulation of chondrocyte proliferation; chondrocyte differentiation; endochondral ossification; JAK/STAT signaling; PI3K–AKT signaling; PLC-activating signaling (komlaebri2016tyrosinekinaseinhibitor pages 1-3, legeaimallet2020noveltherapeuticapproaches pages 5-5, komlaebri2016tyrosinekinaseinhibitor pages 13-14, legeaimallet2020noveltherapeuticapproaches pages 1-2, chesi2001activatedfibroblastgrowth pages 1-2).
- Cellular components (GO CC; examples): plasma membrane; cytosol; nucleus; extracellular matrix of cartilage (affected via chondrocytes) (komlaebri2016tyrosinekinaseinhibitor pages 1-3, komlaebri2016tyrosinekinaseinhibitor pages 13-14, chesi2001activatedfibroblastgrowth pages 1-2).
- Cell types (CL; examples): chondrocyte (growth plate), hypertrophic chondrocyte, keratinocyte, melanocyte, neural progenitor (komlaebri2016tyrosinekinaseinhibitor pages 13-14, chesi2001activatedfibroblastgrowth pages 1-2).
- Anatomical locations (UBERON; examples): growth plate cartilage of long bone; craniofacial skeleton; epidermis; brain (legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2, chesi2001activatedfibroblastgrowth pages 1-2).
- Chemical entities (examples): infigratinib/NVP-BGJ398 (FGFR inhibitor) (komlaebri2016tyrosinekinaseinhibitor pages 1-3).
- Phenotype associations (HPO; examples): disproportionate short stature (HP:0004322); rhizomelia (HP:0000912); macrocephaly (HP:0000256); developmental delay (HP:0001263); acanthosis nigricans (HP:0000956) (mechanism-linked in text) (legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2, chesi2001activatedfibroblastgrowth pages 1-2, reintjes2013activatingsomaticfgfr2 pages 8-8, komlaebri2016tyrosinekinaseinhibitor pages 13-14).

Direct quotes (from retrieved sources)
- “Tyrosine kinase inhibitor NVP-BGJ398 functionally improves FGFR3-related dwarfism in mouse model.” (Title; The Journal of Clinical Investigation; May 2016; https://doi.org/10.1172/JCI83926) (komlaebri2016tyrosinekinaseinhibitor pages 1-3).
- The review highlights FGFR3 as a “negative regulator of bone growth,” and that “graded activation of fibroblast growth factor receptor 3 by mutations” correlates with clinical severity across the achondroplasia spectrum (paraphrased from cited works within Bone 2020 review; Dec 2020; https://doi.org/10.1016/j.bone.2020.115579) (legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2).
- FGFR3 is “highly expressed in developing central nervous system and precursor bone/cartilage rudiments,” underscoring relevance to skeletal and neurodevelopmental phenotypes (Blood; Feb 2001; https://doi.org/10.1182/blood.v97.3.729) (chesi2001activatedfibroblastgrowth pages 1-2).

Limitations and evidence gaps
- The current tool-based retrieval did not surface the seminal primary descriptions of SADDAN with PMID-linked full text (e.g., earliest clinical-genetic reports) nor SADDAN-specific mechanistic skin/CNS studies. Where mechanistic inferences were drawn (e.g., acanthosis nigricans and neurodevelopment), they are grounded in FGFR3 expression biology and activation-class logic but would benefit from targeted retrieval of the primary SADDAN case series and molecular dermatology/neurology studies. These should be added in subsequent updates to strengthen direct-evidence quotes and statistics (OpenTargets Search: SADDAN,severe achondroplasia with developmental delay and acanthosis nigricans, reintjes2013activatingsomaticfgfr2 pages 8-8, chesi2001activatedfibroblastgrowth pages 1-2, legeaimallet2020noveltherapeuticapproaches pages 5-5, komlaebri2016tyrosinekinaseinhibitor pages 13-14, legeaimallet2020noveltherapeuticapproaches pages 1-2).

Citations with URLs and dates
- OpenTargets Platform mapping and evidence for SADDAN→FGFR3; accessed 2025; platform methods in Nucleic Acids Research: https://www.opentargets.org/ (OpenTargets Search: SADDAN,severe achondroplasia with developmental delay and acanthosis nigricans).
- Komla-Ebri D, et al. Tyrosine kinase inhibitor NVP-BGJ398 functionally improves FGFR3-related dwarfism in mouse model. The Journal of Clinical Investigation. May 2016. https://doi.org/10.1172/JCI83926 (komlaebri2016tyrosinekinaseinhibitor pages 1-3, komlaebri2016tyrosinekinaseinhibitor pages 13-14).
- Reintjes N, et al. Activating Somatic FGFR2 Mutations in Breast Cancer. PLoS ONE. Mar 2013. https://doi.org/10.1371/journal.pone.0060264 (contextual references to FGFR3 K650M activation class within article’s discussion). (reintjes2013activatingsomaticfgfr2 pages 8-8).
- Chesi M, et al. Activated fibroblast growth factor receptor 3 is an oncogene that contributes to tumor progression in multiple myeloma. Blood. Feb 2001. https://doi.org/10.1182/blood.v97.3.729 (chesi2001activatedfibroblastgrowth pages 1-2).
- Legeai‑Mallet L, Savarirayan R. Novel therapeutic approaches for the treatment of achondroplasia. Bone. Dec 2020. https://doi.org/10.1016/j.bone.2020.115579 (legeaimallet2020noveltherapeuticapproaches pages 5-5, legeaimallet2020noveltherapeuticapproaches pages 1-2).

Overall assessment
SADDAN pathophysiology is driven by a highly activating FGFR3 K650M mutation that constitutively engages MAPK/ERK, STAT1, PI3K–AKT, and PLCγ signaling in growth plate chondrocytes, disrupting proliferation and hypertrophic differentiation and promoting apoptosis, thereby severely restricting endochondral ossification. The combination of skeletal, skin, and neurodevelopmental phenotypes aligns with the breadth of FGFR3 expression and signaling roles in cartilage, epidermis, and CNS development. Preclinical FGFR inhibition restores signaling balance and bone growth in models, reinforcing the causal pathway. Further SADDAN-specific clinical-genetic series and dermatologic/neuroscience studies are recommended for more granular phenotype statistics and direct mechanistic quotations.

Support for each major claim is provided in the citations above, with URLs and publication months/years where available (OpenTargets Search: SADDAN,severe achondroplasia with developmental delay and acanthosis nigricans, komlaebri2016tyrosinekinaseinhibitor pages 1-3, reintjes2013activatingsomaticfgfr2 pages 8-8, chesi2001activatedfibroblastgrowth pages 1-2, legeaimallet2020noveltherapeuticapproaches pages 5-5, komlaebri2016tyrosinekinaseinhibitor pages 13-14, legeaimallet2020noveltherapeuticapproaches pages 1-2).

References

1. (OpenTargets Search: SADDAN,severe achondroplasia with developmental delay and acanthosis nigricans): Open Targets Query (SADDAN,severe achondroplasia with developmental delay and acanthosis nigricans, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (reintjes2013activatingsomaticfgfr2 pages 8-8): Nadine Reintjes, Yun Li, Alexandra Becker, Edyta Rohmann, Rita Schmutzler, and Bernd Wollnik. Activating somatic fgfr2 mutations in breast cancer. PLoS ONE, 8:e60264, Mar 2013. URL: https://doi.org/10.1371/journal.pone.0060264, doi:10.1371/journal.pone.0060264. This article has 53 citations and is from a peer-reviewed journal.

3. (legeaimallet2020noveltherapeuticapproaches pages 5-5): Laurence Legeai-Mallet and Ravi Savarirayan. Novel therapeutic approaches for the treatment of achondroplasia. Bone, 141:115579, Dec 2020. URL: https://doi.org/10.1016/j.bone.2020.115579, doi:10.1016/j.bone.2020.115579. This article has 68 citations and is from a domain leading peer-reviewed journal.

4. (legeaimallet2020noveltherapeuticapproaches pages 1-2): Laurence Legeai-Mallet and Ravi Savarirayan. Novel therapeutic approaches for the treatment of achondroplasia. Bone, 141:115579, Dec 2020. URL: https://doi.org/10.1016/j.bone.2020.115579, doi:10.1016/j.bone.2020.115579. This article has 68 citations and is from a domain leading peer-reviewed journal.

5. (chesi2001activatedfibroblastgrowth pages 1-2): Marta Chesi, Leslie A. Brents, Sarah A. Ely, Carlos Bais, Davide F. Robbiani, Enrique A. Mesri, W. Michael Kuehl, and P. Leif Bergsagel. Activated fibroblast growth factor receptor 3 is an oncogene that contributes to tumor progression in multiple myeloma. Blood, 97 3:729-36, Feb 2001. URL: https://doi.org/10.1182/blood.v97.3.729, doi:10.1182/blood.v97.3.729. This article has 393 citations and is from a highest quality peer-reviewed journal.

6. (komlaebri2016tyrosinekinaseinhibitor pages 1-3): Davide Komla-Ebri, Emilie Dambroise, Ina Kramer, Catherine Benoist-Lasselin, Nabil Kaci, Cindy Le Gall, Ludovic Martin, Patricia Busca, Florent Barbault, Diana Graus-Porta, Arnold Munnich, Michaela Kneissel, Federico Di Rocco, Martin Biosse-Duplan, and Laurence Legeai-Mallet. Tyrosine kinase inhibitor nvp-bgj398 functionally improves fgfr3-related dwarfism in mouse model. The Journal of clinical investigation, 126 5:1871-84, May 2016. URL: https://doi.org/10.1172/jci83926, doi:10.1172/jci83926. This article has 118 citations.

7. (komlaebri2016tyrosinekinaseinhibitor pages 13-14): Davide Komla-Ebri, Emilie Dambroise, Ina Kramer, Catherine Benoist-Lasselin, Nabil Kaci, Cindy Le Gall, Ludovic Martin, Patricia Busca, Florent Barbault, Diana Graus-Porta, Arnold Munnich, Michaela Kneissel, Federico Di Rocco, Martin Biosse-Duplan, and Laurence Legeai-Mallet. Tyrosine kinase inhibitor nvp-bgj398 functionally improves fgfr3-related dwarfism in mouse model. The Journal of clinical investigation, 126 5:1871-84, May 2016. URL: https://doi.org/10.1172/jci83926, doi:10.1172/jci83926. This article has 118 citations.