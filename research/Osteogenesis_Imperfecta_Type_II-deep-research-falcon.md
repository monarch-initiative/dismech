---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-04T19:33:43.713969'
end_time: '2026-02-04T19:40:00.093580'
duration_seconds: 376.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteogenesis Imperfecta Type II
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 16
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Osteogenesis Imperfecta Type II
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteogenesis Imperfecta Type II**.
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
- **Disease Name:** Osteogenesis Imperfecta Type II
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteogenesis Imperfecta Type II**.
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
Objective 1 (completed): Identified recent, authoritative sources (2023–2024 priority) and primary mechanistic literature on OI Type II, including Calcified Tissue International 2024 genetics update; ACS Pharmacology & Translational Science 2024 review; JCI Insight 2023 mechanistic mouse study; and foundational work on the CRTAP–P3H1–PPIB complex (as cited within our evidence). (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zieba2023alteredsox9and pages 18-19, zhang2020identificationofmoleculargenetic pages 40-42)
Objective 2 (completed): Extracted mechanistic evidence for collagen type I biosynthesis, 3-hydroxylation, folding, trafficking, ECM assembly, and downstream pathway perturbations (ER stress/UPR, TGF-β/BMP/WNT), as well as mineralization and growth-plate consequences. (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zieba2023alteredsox9and pages 18-19, zhang2020identificationofmoleculargenetic pages 40-42)
Objective 3 (completed): Mapped genes/proteins, processes, cell types, anatomy, and chemicals to standard ontologies.
Objective 4 (completed): Synthesized disease progression, phenotypes, recent developments, and expert perspectives with statistics and data where available.
Objective 5 (completed): Created a structured artifact summarizing key genes/complexes and mechanisms for embedding.
Objective 6 (completed): Wrote and submitted the comprehensive, cited research report.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Osteogenesis Imperfecta (OI) Type II (perinatal lethal OI)
- MONDO ID: MONDO_0008147
- Category: Mendelian

Pathophysiology description (narrative synthesis)
Osteogenesis Imperfecta Type II is the most severe, typically perinatal lethal, form of OI characterized by extreme skeletal fragility, multiple in utero fractures, crumpled long bones, severely undermineralized calvarium, and respiratory failure secondary to pulmonary hypoplasia. The disorder arises primarily from qualitative defects in type I collagen due to de novo dominant COL1A1 or COL1A2 missense variants (often glycine substitutions within the Gly–X–Y helical repeat) that impose dominant-negative effects on the heterotrimer, delaying triple-helix folding, causing prolonged post-translational modification (“overmodification”), and leading to failure of proper fibrillogenesis and matrix assembly (DOI:10.1007/s00223-024-01266-5; DOI:10.1021/acsptsci.3c00324). In other cases with perinatal lethality, recessive disruption of the ER prolyl 3-hydroxylation/folding complex—CRTAP, P3H1/LEPRE1, and PPIB—abolishes site-specific 3-hydroxylation (Pro986 in α1(I) and Pro707 in α2(I)), delays helix nucleation and folding, and results in overmodified collagen, ER processing/trafficking defects, and catastrophic bone matrix insufficiency (DOI:10.1021/acsptsci.3c00324). Together, these upstream molecular lesions trigger downstream cellular stress responses, dysregulated osteoblast/chondrocyte biology including altered growth plate dynamics, and defective mineralization that culminate in perinatal lethality. (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42)

Key concepts and definitions
- Type I collagen biosynthesis: Heterotrimer of two pro-α1(I) (COL1A1) and one pro-α2(I) (COL1A2) chains synthesized in the ER; extensive PTMs (prolyl 4-hydroxylation, lysyl hydroxylation/glycosylation), site-specific prolyl 3-hydroxylation at Pro986/Pro707 by the CRTAP–P3H1–PPIB complex; triple-helix formation proceeds C→N direction; chaperoned trafficking to Golgi and secretion; extracellular N- and C-propeptide cleavage (ADAMTS2/3/14; BMP1) precedes fibrillogenesis (DOI:10.1007/s00223-024-01266-5). (jovanovic2024updateonthe pages 4-5)
- Prolyl 3-hydroxylation complex: “CRTAP–P3H1 (LEPRE1)–PPIB” mediates 3-hydroxylation of a critical proline (α1(I) Pro986; α2(I) Pro707) and coordinates rapid helix folding; loss abolishes 3-hydroxylation, delays folding, and yields overmodified collagen with impaired trafficking and ECM assembly (DOI:10.1021/acsptsci.3c00324). (sun2024emerginglandscapeof pages 4-5)
- Dominant-negative collagen: Glycine substitutions in the Gly–X–Y repeat introduce steric hindrance, slow helix propagation, and cause helical overmodification; α1(I) substitutions are particularly enriched for severe/lethal outcomes (Calcified Tissue Int. 2024). (jovanovic2024updateonthe pages 4-5)

Recent developments and latest research (2023–2024 priority)
- Genetics and mechanisms update: Jovanovic & Marini 2024 provides current genetic architecture of OI including dominant COL1A1/COL1A2 and recessive mechanisms (CRTAP/P3H1/PPIB; chaperones; trafficking) and clarifies how delayed folding causes overmodification and severe phenotypes; it also integrates newer contributors to trafficking/signaling that intersect with WNT/LRP5/6 and MAPK/ERK (Calcified Tissue Int., Aug 2024; https://doi.org/10.1007/s00223-024-01266-5). (jovanovic2024updateonthe pages 4-5)
- Pathogenesis and therapeutic landscape: Sun et al. 2024 emphasizes the centrality of the CRTAP–P3H1–PPIB complex, explicitly noting that “the complex’s primary target is the 3-hydroxylation of a specific proline (Pro986)” and that loss causes delayed helix folding and severe bone dysplasia; it synthesizes progress on gene/stem-cell/editing concepts (ACS Pharmacol. & Transl. Sci., Jan 2024; https://doi.org/10.1021/acsptsci.3c00324). (sun2024emerginglandscapeof pages 4-5)
- Growth plate biology in collagen-mutant OI: Zieba et al. 2023 (Aga2+/- mouse) reports ER stress/UPR signatures and altered FGF/MAPK and Sox9 programs in growth-plate chondrocytes, linking mutant type I collagen to shortened proliferative zones and disordered endochondral ossification, consistent with growth failure across OI (JCI Insight, Nov 2023; https://doi.org/10.1172/jci.insight.171984). While not specific to Type II, the mechanistic axis is relevant to lethal forms with profound growth-plate disruption. (zieba2023alteredsox9and pages 18-19)

Current applications and real-world implementations
- Molecular diagnosis and prenatal counseling: Contemporary nosology/genetics reviews support using targeted or exome sequencing to detect glycine substitutions in COL1A1/2 or biallelic CRTAP/P3H1/PPIB variants in severe prenatal skeletal dysplasia; genotype informs prognosis and counseling for perinatal lethality. (Calcified Tissue Int. 2024; https://doi.org/10.1007/s00223-024-01266-5). (jovanovic2024updateonthe pages 4-5)
- Therapeutic implications of mechanisms: While no curative therapy exists for Type II, mechanistic insights underpin emerging strategies (chemical chaperones, pathway modulation, anti-sclerostin, and gene/cell therapy) under investigation across OI; however, perinatal lethality limits interventional windows. Sun 2024 summarizes translational approaches and their mechanistic rationale (https://doi.org/10.1021/acsptsci.3c00324). (sun2024emerginglandscapeof pages 4-5)

Expert opinions and analysis from authoritative sources
- “The most common pathogenic lesions are glycine substitutions within the Gly–X–Y helical repeat; these slow triple-helix folding, prolong exposure to modifying enzymes, cause helical overmodification, and can produce severe/lethal phenotypes.” (Calcified Tissue Int. 2024; DOI:10.1007/s00223-024-01266-5). (jovanovic2024updateonthe pages 4-5)
- “Deletion or biallelic mutations in any component [of CRTAP–P3H1–PPIB] abolish complex activity, causing failure of Pro986 hydroxylation, delayed triple-helix folding, and compensatory/excessive modification…[leading to] severe bone dysplasia phenotypes.” (ACS Pharmacol. & Transl. Sci. 2024; DOI:10.1021/acsptsci.3c00324). (sun2024emerginglandscapeof pages 4-5)

Relevant statistics and data from recent studies
- Genotype–phenotype patterns: Jovanovic & Marini 2024 highlight that α1(I) glycine substitutions are disproportionately associated with severe/lethal outcomes compared with α2(I), reflecting chain-specific structural consequences; the review collates historic series and registry data supporting this distribution (Calcified Tissue Int. 2024; DOI:10.1007/s00223-024-01266-5). (jovanovic2024updateonthe pages 4-5)
- Growth plate effects: Zieba 2023 reports single-cell and pathway analyses demonstrating increased FGF/MAPK signaling and ER stress markers in growth plate chondrocytes with mutant collagen, providing quantitative transcriptomic support for disordered endochondral ossification that correlates with short stature and severe skeletal dysplasia (JCI Insight 2023; DOI:10.1172/jci.insight.171984). (zieba2023alteredsox9and pages 18-19)

1) Core Pathophysiology
- Primary mechanisms: Qualitative defects in type I collagen triple helix (dominant glycine substitutions) or failure of ER 3-hydroxylation/folding (CRTAP–P3H1–PPIB) lead to delayed folding, overmodification (hyper-hydroxylation and glycosylation), impaired ER→Golgi trafficking, reduced collagen secretion, defective extracellular processing (C-terminal cleavage by BMP1) and fibrillogenesis, culminating in fragile, poorly mineralized bone. (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42)
- Dysregulated pathways: Evidence from OI models shows ER stress/UPR signatures in osteoblasts and growth-plate chondrocytes, and altered FGF/MAPK and Sox9 programs with effects on proliferative/hypertrophic zones; TGF-β signaling activation has been reported in severe OI models, linking matrix abnormalities to pro-catabolic signaling and bone turnover imbalance. (zieba2023alteredsox9and pages 18-19, zhang2020identificationofmoleculargenetic pages 40-42)
- Affected cellular processes: Collagen PTM/quality control; protein folding/isomerization; cargo trafficking; ECM assembly; mineral deposition; endochondral ossification. (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5)

2) Key Molecular Players
- Genes/Proteins (HGNC): COL1A1, COL1A2; CRTAP; LEPRE1 (P3H1); PPIB; SERPINH1 (HSP47); FKBP10; BMP1. Roles and evidence summarized below. (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42)
- Chemical entities (CHEBI): proline (CHEBI:26271); hydroxyproline (CHEBI:18050); lysine (CHEBI:25094); ascorbate (CHEBI:22652) as cofactor for hydroxylases; 4‑phenylbutyrate as a chemical chaperone in OI models (CHEBI:46195). (zieba2023alteredsox9and pages 18-19, zhang2020identificationofmoleculargenetic pages 40-42)
- Cell types (CL): osteoblast (CL:0000062); osteocyte (CL:0000100); chondrocyte (CL:0000138); fibroblast (CL:0000057). (zieba2023alteredsox9and pages 18-19, jovanovic2024updateonthe pages 4-5)
- Anatomical locations (UBERON): bone tissue (UBERON:0001474); growth plate (UBERON:0000981); calvaria (UBERON:0008222); rib (UBERON:0002228); lung/pulmonary system (UBERON:0002048) given hypoplasia. (jovanovic2024updateonthe pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42)

3) Biological Processes (GO) disrupted
- Collagen biosynthetic process (GO:0032964); protein folding (GO:0006457); peptidyl-proline 3-hydroxylation (GO:0018401); peptidyl-prolyl cis-trans isomerization (GO:0000413); ER to Golgi vesicle-mediated transport (GO:0006888); extracellular matrix organization (GO:0030198); collagen fibril organization (GO:0030199); ossification (GO:0001503); endochondral ossification (GO:0001958); response to endoplasmic reticulum stress (GO:0034976); regulation of TGF-β signaling pathway (GO:0017015); Wnt signaling pathway (GO:0016055); MAPK cascade (GO:0000165). (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zieba2023alteredsox9and pages 18-19, zhang2020identificationofmoleculargenetic pages 40-42)

4) Cellular Components
- Endoplasmic reticulum lumen (GO:0005788): site of procollagen folding and CRTAP–P3H1–PPIB action. (sun2024emerginglandscapeof pages 4-5)
- Golgi apparatus (GO:0005794): post-ER processing/trafficking checkpoint. (jovanovic2024updateonthe pages 4-5)
- Collagen-containing extracellular matrix (GO:0062023) and extracellular region (GO:0005576): site of propeptide cleavage, fibrillogenesis, mineral deposition. (jovanovic2024updateonthe pages 4-5)

5) Disease Progression (sequence of events)
- Initiation: De novo dominant COL1A1/2 glycine substitution or recessive loss of CRTAP/P3H1/PPIB activity. (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5)
- Intracellular pathogenesis: Delayed helix folding → overmodification; ER quality-control engagement, trafficking delay; reduced secretion and aberrant procollagen processing. (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5)
- Extracellular matrix failure: Impaired C-propeptide cleavage (BMP1 axis), altered cross-linking, disordered fibrillogenesis → defective mineralization and bone material quality. (jovanovic2024updateonthe pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42)
- Tissue-level consequences: Disorganized growth plate, shortened proliferative zone; altered FGF/MAPK/Sox9 programs; osteoblast dysfunction; high fragility and deformity. (zieba2023alteredsox9and pages 18-19)
- Clinical trajectory: Severe skeletal deformity and multiple fractures in utero, thin beaded ribs, crumpled femurs, undermineralized skull, pulmonary hypoplasia; perinatal demise from respiratory failure. (zhang2020identificationofmoleculargenetic pages 40-42)

6) Phenotypic Manifestations (HP terms)
- Perinatal death (HP:0003811); Multiple fractures (HP:0002757); Intrauterine fractures (HP:0005839); Beaded ribs (HP:0000883); Bowed/crumpled long bones (HP:0002816/HP related); Undermineralized skull (HP:0004281); Pulmonary hypoplasia (HP:0002089); Growth deficiency (HP:0001510); Blue sclerae (HP:0000592). (zhang2020identificationofmoleculargenetic pages 40-42, jovanovic2024updateonthe pages 4-5)

Gene/protein annotations with ontology terms and evidence
- COL1A1 (HGNC:2197): GO-BP: collagen biosynthetic process; GO-CC: ER lumen; collagen-containing ECM. Mechanism: dominant glycine substitutions delay folding and cause overmodification → severe/lethal phenotypes. Evidence: Calcified Tissue Int. 2024 (DOI:10.1007/s00223-024-01266-5; URL above). (jovanovic2024updateonthe pages 4-5)
- COL1A2 (HGNC:2198): As above; chain-specific severity differs from α1(I), but lethal variants are common in α2(I) as well. (jovanovic2024updateonthe pages 4-5)
- CRTAP (HGNC:2438), LEPRE1/P3H1 (HGNC:16721), PPIB (HGNC:9233): GO-BP: peptidyl-proline 3-hydroxylation; protein folding; GO-CC: ER lumen. Mechanism: loss abolishes 3-hydroxylation at Pro986/Pro707, delays folding; overmodified collagen; trafficking defects; severe/recessive OI with lethal spectrum. Evidence: ACS Pharmacol. & Transl. Sci. 2024 (DOI:10.1021/acsptsci.3c00324). (sun2024emerginglandscapeof pages 4-5)
- SERPINH1/HSP47 (HGNC:1222); FKBP10 (HGNC:3711): GO-BP: protein folding; ECM organization; GO-CC: ER lumen. Mechanism: chaperone/isomerase defects reduce secretion, crosslinking, and fibrillogenesis; severe OI. Evidence collated in 2024 reviews. (jovanovic2024updateonthe pages 4-5)
- BMP1 (HGNC:1050): GO-BP: procollagen C-propeptide processing; fibrillogenesis; ossification; GO-CC: extracellular region/ECM. Mechanism: impaired C-propeptide cleavage → defective fibrils and mineralization. (jovanovic2024updateonthe pages 4-5)

Embedded summary artifact
| Gene/Protein (HGNC symbol) | Protein/Complex role | Pathogenic mechanism in OI type II | Representative residue/site (if applicable) | Cellular compartment (GO-CC) | Key processes impacted (GO-BP) | Evidence (PMID/DOI; Year; URL) | Notes |
|---|---|---|---|---|---|---|---|
| COL1A1 | Type I procollagen α1 chain (major fibrillar collagen) | Dominant glycine substitutions in Gly-X-Y repeat → dominant-negative defective triple helix; delayed folding, helical overmodification, abnormal fibrillogenesis and ECM assembly → severe/perinatal phenotypes | — | ER lumen; Golgi; collagen-containing extracellular matrix | Collagen biosynthetic process; protein folding; ER → Golgi transport; extracellular matrix organization; ossification | Jovanovic & Marini 2024 DOI:10.1007/s00223-024-01266-5; Sun et al. 2024 DOI:10.1021/acsptsci.3c00324; Zhang thesis 2020 DOI:10.53846/goediss-7825 (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42) | Glycine substitutions in α1(I) often produce the most severe/lethal outcomes (Type II) |
| COL1A2 | Type I procollagen α2 chain (part of heterotrimer) | Dominant glycine substitutions → abnormal heterotrimer formation, delayed folding and overmodification; defective ECM incorporation and bone fragility | — | ER lumen; Golgi; collagen-containing extracellular matrix | Collagen biosynthetic process; protein folding; ER → Golgi transport; extracellular matrix organization; ossification | Jovanovic & Marini 2024 DOI:10.1007/s00223-024-01266-5; Sun et al. 2024 DOI:10.1021/acsptsci.3c00324; Zhang thesis 2020 DOI:10.53846/goediss-7825 (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42) | Glycine substitutions in α2(I) cause severe OI but genotype–phenotype severity distribution differs from α1(I) |
| CRTAP | Cartilage-associated protein; non-catalytic subunit of prolyl 3-hydroxylation complex | Biallelic loss → abolishes 3-hydroxylation of critical proline(s), delays triple-helix folding, causes collagen overmodification, impaired secretion/trafficking and defective matrix assembly → severe/recessive lethal OI | Pro986 α1(I); Pro707 α2(I) | ER lumen | Proline 3-hydroxylation; protein folding; ER quality control; ER → Golgi transport; extracellular matrix organization; ossification | Jovanovic & Marini 2024 DOI:10.1007/s00223-024-01266-5; Sun et al. 2024 DOI:10.1021/acsptsci.3c00324; Zhang thesis 2020 DOI:10.53846/goediss-7825 (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42) | Part of CRTAP–P3H1–PPIB complex required for site-specific 3-hydroxylation linked to severe perinatal phenotypes |
| P3H1 / LEPRE1 | Prolyl 3-hydroxylase 1 (catalytic enzyme in complex) | Biallelic loss or damaging variants → loss of Pro986/Pro707 3-hydroxylation, delayed helix formation, overmodification and ER retention → severe/recessive lethal OI | Pro986 α1(I); Pro707 α2(I) | ER lumen | Proline 3-hydroxylation; collagen biosynthetic process; protein folding; ER quality control; extracellular matrix organization; ossification | Jovanovic & Marini 2024 DOI:10.1007/s00223-024-01266-5; Sun et al. 2024 DOI:10.1021/acsptsci.3c00324; Zhang thesis 2020 DOI:10.53846/goediss-7825 (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42) | Known cause of severe autosomal recessive OI (type VIII and related severe forms) |
| PPIB | Cyclophilin B (peptidyl-prolyl cis–trans isomerase), member of the prolyl 3-hydroxylation complex | Loss/dysfunction → impaired isomerase activity in complex, delayed procollagen folding and defective 3-hydroxylation → abnormal collagen modification/trafficking and severe OI | Pro986 α1(I); Pro707 α2(I) (complex target) | ER lumen | Protein folding; proline isomerization; collagen biosynthetic process; ER → Golgi transport; extracellular matrix organization; ossification | Jovanovic & Marini 2024 DOI:10.1007/s00223-024-01266-5; Sun et al. 2024 DOI:10.1021/acsptsci.3c00324; Zhang thesis 2020 DOI:10.53846/goediss-7825 (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42) | PPIB variants produce recessive OI phenotypes overlapping perinatal/severe presentations |
| HSP47 / SERPINH1 | ER-resident collagen-specific chaperone (heat shock protein 47) | Dysfunctional chaperone → misfolded procollagen, ER retention, reduced secretion, abnormal fibrillogenesis and bone fragility; can trigger ER stress/UPR depending on context | — | ER lumen | Protein folding; ER quality control; collagen biosynthetic process; extracellular matrix organization; ossification | Jovanovic & Marini 2024 DOI:10.1007/s00223-024-01266-5; Sun et al. 2024 DOI:10.1021/acsptsci.3c00324; Zhang thesis 2020 DOI:10.53846/goediss-7825 (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42) | SERPINH1 pathogenic variants associated with severe OI phenotypes in humans and models |
| FKBP10 | ER-resident peptidyl-prolyl isomerase / foldase (FKBP65) involved in collagen folding and crosslinking | Loss → impaired collagen folding/trafficking and defective cross-linking (via LOX pathway perturbation), reduced ECM deposition and bone fragility; can produce severe OI | — | ER lumen; ER membrane | Protein folding; peptidyl-prolyl isomerization; extracellular matrix organization; collagen cross-linking; ossification | Jovanovic & Marini 2024 DOI:10.1007/s00223-024-01266-5; Sun et al. 2024 DOI:10.1021/acsptsci.3c00324; Zhang thesis 2020 DOI:10.53846/goediss-7825 (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42) | FKBP10 defects are a recognized recessive cause of severe OI with abnormal cross-links |
| BMP1 | Secreted metalloproteinase (C-propeptide cleavage; procollagen C-proteinase) | Impaired C-propeptide cleavage → defective procollagen to collagen conversion, abnormal fibril formation, altered mineralization and bone matrix quality → fragility and severe phenotypes | — | Extracellular region; extracellular matrix | Procollagen processing; extracellular matrix organization; collagen fibrillogenesis; ossification; bone mineralization | Jovanovic & Marini 2024 DOI:10.1007/s00223-024-01266-5; Zhang thesis 2020 DOI:10.53846/goediss-7825 (jovanovic2024updateonthe pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42) | BMP1 and related processing enzymes influence collagen maturation and mineralization; mutations can phenocopy severe OI features |


*Table: Table summarizing principal genes/protein complexes implicated in perinatal-lethal osteogenesis imperfecta (Type II), their molecular roles, pathogenic mechanisms, subcellular locations and the key biological processes they perturb, with primary evidence citations. Useful as a concise reference for ontology mapping and mechanistic annotation. (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42)*

Evidence items with PMIDs/DOIs, URLs, and dates (direct support of mechanistic claims)
- Jovanovic M, Marini JC. Update on the Genetics of Osteogenesis Imperfecta. Calcified Tissue International. Aug 2024. DOI:10.1007/s00223-024-01266-5. URL: https://doi.org/10.1007/s00223-024-01266-5. Key content: chain-specific glycine substitution severity; delayed folding/overmodification; roles of ADAMTS/BMP1 and trafficking/chaperones; signaling intersections. (jovanovic2024updateonthe pages 4-5)
- Sun Y et al. Emerging Landscape of Osteogenesis Imperfecta Pathogenesis and Therapeutic Approaches. ACS Pharmacology & Translational Science. Jan 2024. DOI:10.1021/acsptsci.3c00324. URL: https://doi.org/10.1021/acsptsci.3c00324. Key content: CRTAP–P3H1–PPIB complex target (Pro986), consequences of complex loss (delayed folding, overmodification), severe bone dysplasia. (sun2024emerginglandscapeof pages 4-5)
- Zieba J et al. Altered Sox9 and FGF signaling gene expression in Aga2 OI mice negatively affects linear growth. JCI Insight. Nov 2023. DOI:10.1172/jci.insight.171984. URL: https://doi.org/10.1172/jci.insight.171984. Key content: ER stress/UPR in growth plate chondrocytes, increased FGF/MAPK signaling, growth-plate dysfunction relevant to severe OI biology. (zieba2023alteredsox9and pages 18-19)
- Zhang X. Identification of molecular-genetic causes for osteogenesis imperfecta… PhD Thesis. 2020. DOI:10.53846/goediss-7825. URL: https://doi.org/10.53846/goediss-7825. Key content (with primary citations): discovery of CRTAP–P3H1–PPIB complex (Cell 2006; Am J Hum Genet 2009), ER stress/UPR and matrix/mineralization alterations; links to BMP1 processing and crosslinking. (zhang2020identificationofmoleculargenetic pages 40-42)

Limitations and open questions
- Quantitative thresholds linking degree/location of helical overmodification to lethality remain incompletely defined at the individual variant level; multi-omic correlates in perinatal cases remain sparse due to lethality. Growth-plate pathway dysregulation (FGF/MAPK, TGF-β, WNT) is well-supported in models but requires further human perinatal tissue data to resolve causal hierarchies. (zieba2023alteredsox9and pages 18-19, jovanovic2024updateonthe pages 4-5)

Appendix: Ontology-aligned annotations (concise)
- Genes/Proteins (HGNC): COL1A1 (HGNC:2197); COL1A2 (HGNC:2198); CRTAP (HGNC:2438); LEPRE1/P3H1 (HGNC:16721); PPIB (HGNC:9233); SERPINH1 (HGNC:1222); FKBP10 (HGNC:3711); BMP1 (HGNC:1050). (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5)
- GO Biological Process: GO:0032964; GO:0018401; GO:0000413; GO:0006888; GO:0030198; GO:0030199; GO:0001503; GO:0001958; GO:0034976; GO:0017015; GO:0016055; GO:0000165. (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5, zieba2023alteredsox9and pages 18-19)
- GO Cellular Component: GO:0005788; GO:0005794; GO:0062023; GO:0005576. (jovanovic2024updateonthe pages 4-5, sun2024emerginglandscapeof pages 4-5)
- HP Phenotypes: HP:0003811; HP:0002757; HP:0005839; HP:0000883; HP:0002816; HP:0004281; HP:0002089; HP:0001510; HP:0000592. (zhang2020identificationofmoleculargenetic pages 40-42, jovanovic2024updateonthe pages 4-5)
- CL Cell Types: CL:0000062; CL:0000100; CL:0000138; CL:0000057. (zieba2023alteredsox9and pages 18-19, jovanovic2024updateonthe pages 4-5)
- UBERON Anatomy: UBERON:0001474; UBERON:0000981; UBERON:0008222; UBERON:0002228; UBERON:0002048. (jovanovic2024updateonthe pages 4-5, zhang2020identificationofmoleculargenetic pages 40-42)
- CHEBI Chemicals: CHEBI:26271; CHEBI:18050; CHEBI:25094; CHEBI:22652; CHEBI:46195. (zieba2023alteredsox9and pages 18-19, zhang2020identificationofmoleculargenetic pages 40-42)

References

1. (jovanovic2024updateonthe pages 4-5): Milena Jovanovic and Joan C. Marini. Update on the genetics of osteogenesis imperfecta. Calcified Tissue International, 115:891-914, Aug 2024. URL: https://doi.org/10.1007/s00223-024-01266-5, doi:10.1007/s00223-024-01266-5. This article has 48 citations and is from a peer-reviewed journal.

2. (sun2024emerginglandscapeof pages 4-5): Yu Sun, Lin Li, Jiajun Wang, Huiting Liu, and Hu Wang. Emerging landscape of osteogenesis imperfecta pathogenesis and therapeutic approaches. ACS pharmacology & translational science, 7 1:72-96, Jan 2024. URL: https://doi.org/10.1021/acsptsci.3c00324, doi:10.1021/acsptsci.3c00324. This article has 17 citations and is from a peer-reviewed journal.

3. (zieba2023alteredsox9and pages 18-19): Jennifer Zieba, Lisette Nevarez, Davis Wachtell, Jorge H. Martin, Alexander Kot, Sereen Wong, Daniel H. Cohn, and Deborah Krakow. Altered sox9 and fgf signaling gene expression in aga2 oi mice negatively affects linear growth. JCI Insight, Nov 2023. URL: https://doi.org/10.1172/jci.insight.171984, doi:10.1172/jci.insight.171984. This article has 6 citations and is from a domain leading peer-reviewed journal.

4. (zhang2020identificationofmoleculargenetic pages 40-42): Xuying Zhang. Identification of molecular-genetic causes for osteogenesis imperfecta, interdigital hyperplasia and ribosomopathies in cattle. PhD thesis, University Goettingen Repository, 2020. URL: https://doi.org/10.53846/goediss-7825, doi:10.53846/goediss-7825.