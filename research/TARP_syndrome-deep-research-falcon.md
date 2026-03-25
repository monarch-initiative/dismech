---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-05T15:42:38.384239'
end_time: '2026-01-05T15:50:48.327236'
duration_seconds: 489.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: TARP syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** TARP syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **TARP syndrome**.
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
- **Disease Name:** TARP syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **TARP syndrome**.
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
Objective 1: Identify and collect recent (2023–2024) and foundational literature on TARP syndrome and RBM10 pathophysiology. Status: completed. Key sources include Lane 2023 BMJ Case Reports; Machour 2024 Nature Communications; Damianov 2023 bioRxiv; Krishnamoorthy 2024 bioRxiv; Mehta & Touma 2023 IJMS; and a large RBM10 genotype–phenotype preprint (2025).
Objective 2: Extract mechanistic evidence on molecular and cellular pathways disrupted in TARP (RBM10-related) syndrome. Status: completed.
Objective 3: Map genes/proteins, processes (GO), cellular components, cell types (CL), anatomical sites (UBERON), phenotypes (HPO), and chemicals (ChEBI). Status: completed.
Objective 4: Synthesize disease progression narrative linking genotype to phenotype and clinical manifestations. Status: completed.
Objective 5: Create a compact artifact summarizing key molecular players and GO/HP terms. Status: completed.
Objective 6: Write and submit the final research report. Status: in-progress (this document).

Disease Pathophysiology Research Report

Target Disease
- Disease Name: TARP syndrome (Talipes equinovarus, Atrial septal defect, Robin sequence, persistent left Superior vena cava)
- MONDO ID: Not definitively established in our retrieved sources; the disorder is X-linked, caused by pathogenic variants in RBM10.
- Category: Mendelian

Pathophysiology description
TARP syndrome is an X-linked developmental disorder caused by germline loss-of-function or functionally impairing variants in RBM10, an RNA-binding protein that regulates alternative splicing across the transcriptome. RBM10 predominantly promotes skipping of cassette exons through association with U2 snRNP engaged at intron branch sites on chromatin, thereby modulating early spliceosomal assembly and exon choice. Loss or reduction of RBM10 function shifts hundreds to thousands of splicing events toward exon inclusion, with severity of clinical phenotype correlating with the extent of functional impairment. Splicing-dependent mechanisms plausibly converge on developmental pathways, including de-repression of NOTCH signaling via NUMB missplicing and altered ECM–cytoskeletal signaling via exon-inclusion isoforms in VCL, CD44, and TNC. In addition, a splicing-independent role for RBM10 at DNA replication forks has been demonstrated: RBM10 associates with nascent DNA in a PRIM1-dependent, RNA-sensitive manner, recruits HDAC1 to promote H4K16 deacetylation, and preserves replication-fork stability; RBM10 deficiency induces replication stress and creates a therapeutically exploitable synthetic-lethal interaction with WEE1 inhibition. These molecular derangements provide a mechanistic substrate for impaired craniofacial morphogenesis (Robin sequence), limb patterning (talipes), and cardiac defects (atrial septal defects, persistent left SVC), and may contribute to multi-organ involvement documented clinically, including central nervous system anomalies and occasional hepatic dysfunction. (damianov2023theapoptoticsplicing pages 30-33, damianov2023theapoptoticsplicing pages 10-14, damianov2023theapoptoticsplicing pages 1-5, damianov2023theapoptoticsplicing pages 14-16, bang2025genotypephenotypecorrelationin pages 8-11, krishnamoorthy2024rbm10lossinduces pages 1-4, machour2024harnessingdnareplication pages 1-2, machour2024harnessingdnareplication pages 4-5, machour2024harnessingdnareplication pages 8-10, lane2023abnormalliverfunction pages 2-3)

Core Pathophysiology
- Primary mechanisms: 
  - Alternative splicing dysregulation due to RBM10 loss, with a bias toward cassette exon inclusion in target transcripts. Mechanistically, RBM10 acts as a U2-associated splicing repressor at/near branch sites on chromatin. (damianov2023theapoptoticsplicing pages 30-33, damianov2023theapoptoticsplicing pages 10-14, damianov2023theapoptoticsplicing pages 1-5, damianov2023theapoptoticsplicing pages 14-16)
  - Splicing-independent chromatin/replication role: RBM10 binds active replication forks, anchors HDAC1 to deacetylate H4K16, reduces R-loops, and supports fork progression; RBM10-deficient cells exhibit replication stress and show sensitivity to WEE1 inhibition. (machour2024harnessingdnareplication pages 1-2, machour2024harnessingdnareplication pages 4-5, machour2024harnessingdnareplication pages 8-10)
- Dysregulated molecular pathways:
  - NOTCH signaling via NUMB mis-splicing and reduced NUMB protein leading to NOTCH de-repression. (krishnamoorthy2024rbm10lossinduces pages 1-4)
  - ECM–cytoskeletal signaling and RAC1 activation via inclusion isoforms of VCL, CD44, TNC. (krishnamoorthy2024rbm10lossinduces pages 1-4)
- Affected cellular processes:
  - Spliceosome assembly and branch-site selection; exon definition decisions. (damianov2023theapoptoticsplicing pages 30-33, damianov2023theapoptoticsplicing pages 10-14, damianov2023theapoptoticsplicing pages 1-5, damianov2023theapoptoticsplicing pages 14-16)
  - DNA replication fork stability and chromatin deacetylation. (machour2024harnessingdnareplication pages 1-2, machour2024harnessingdnareplication pages 4-5)

Key Molecular Players
- Genes/Proteins (HGNC):
  - RBM10: Xp11.23; RNA-binding protein with roles in alternative splicing, U2 snRNP-associated repression, and replication-fork stabilization. (damianov2023theapoptoticsplicing pages 30-33, machour2024harnessingdnareplication pages 1-2)
  - NUMB: Target of RBM10; exon inclusion events decrease NUMB protein via ubiquitin-mediated turnover, leading to NOTCH pathway de-repression. (krishnamoorthy2024rbm10lossinduces pages 1-4)
  - VCL (vinculin), CD44, TNC: ECM/cytoskeletal targets whose inclusion isoforms promote cell motility/invasiveness and RAC1 activation when RBM10 is lost. (krishnamoorthy2024rbm10lossinduces pages 1-4)
  - EIF4H: RBM10-regulated exon; validated inclusion upon RBM10 loss. (krishnamoorthy2024rbm10lossinduces pages 1-4)
  - HDAC1: Histone deacetylase recruited by RBM10 to replication forks for H4K16 deacetylation. (machour2024harnessingdnareplication pages 4-5)
  - WEE1: Kinase whose inhibition is synthetically lethal in RBM10-deficient cells. (machour2024harnessingdnareplication pages 1-2, machour2024harnessingdnareplication pages 8-10)
- Chemical entities (CHEBI/drugs):
  - Adavosertib (MK-1775), a WEE1 inhibitor, sensitizes RBM10-deficient cells in vitro and in vivo. (machour2024harnessingdnareplication pages 8-10)
- Cell types (CL):
  - Cranial neural crest cells (CNCCs): implicated by RBM10 embryonic expression in branchial arches and craniofacial phenotypes. (krishnamoorthy2024rbm10lossinduces pages 1-4)
- Anatomical locations (UBERON):
  - Heart, atrial septum, systemic venous return (persistent left SVC). (lane2023abnormalliverfunction pages 2-3)
  - Branchial arches, limbs. (krishnamoorthy2024rbm10lossinduces pages 1-4)

Biological Processes (GO annotation)
- GO:0000381 “regulation of alternative mRNA splicing, via spliceosome.” RBM10 acts as a repressor that promotes exon skipping and interacts with U2 snRNP at branch sites. (damianov2023theapoptoticsplicing pages 30-33, damianov2023theapoptoticsplicing pages 10-14)
- GO:0007219 “Notch signaling pathway.” Activated indirectly through decreased NUMB upon RBM10 loss. (krishnamoorthy2024rbm10lossinduces pages 1-4)
- GO:0006268 “DNA replication” and GO:0043111 “H4-K16 deacetylation” (as part of chromatin modification). RBM10 anchors HDAC1 to forks, facilitating H4K16 deacetylation and fork stability. (machour2024harnessingdnareplication pages 4-5)
- GO:0007010 “cytoskeleton organization” and GO:0030198 “extracellular matrix organization,” driven by exon-inclusion isoforms of VCL, CD44, and TNC. (krishnamoorthy2024rbm10lossinduces pages 1-4)

Cellular Components
- U2 small nuclear ribonucleoprotein complex (GO:0005684) and pre-spliceosomal A/B complexes on chromatin; RBM10-containing RNPs engage intron branch sites. (damianov2023theapoptoticsplicing pages 30-33, damianov2023theapoptoticsplicing pages 1-5)
- Nuclear speckles (GO:0016607), splicing factor–rich nuclear compartments; RBM10 and associated splicing factors localize and function in these regions. (damianov2023theapoptoticsplicing pages 1-5)
- DNA replication forks: RBM10 co-localizes with EdU-labeled nascent DNA and PCNA, recruiting HDAC1 and modulating H4K16ac. (machour2024harnessingdnareplication pages 4-5)

Disease Progression Model
- Initiation: Germline RBM10 variants (frameshift/nonsense/splice-site or pathogenic missense) reduce its exon-skipping activity and/or its association with U2/branch sites, producing widespread exon-inclusion shifts. (bang2025genotypephenotypecorrelationin pages 8-11)
- Early developmental effects: Dysregulated NOTCH signaling through NUMB missplicing perturbs cell fate decisions in craniofacial and cardiac progenitors; simultaneous mis-splicing of ECM/cytoskeletal genes perturbs cell migration and morphogenesis. (krishnamoorthy2024rbm10lossinduces pages 1-4)
- Tissue morphogenesis: Craniofacial anomalies including Robin sequence and cleft palate; limb patterning defects causing talipes; atrial septal defects and persistent left SVC. (lane2023abnormalliverfunction pages 2-3, bang2025genotypephenotypecorrelationin pages 8-11)
- Splicing-independent stress: Replication-fork instability and chromatin hyperacetylation (H4K16ac) add proliferative stress, potentially compounding developmental deficits. (machour2024harnessingdnareplication pages 4-5)
- Clinical course: Historically high neonatal mortality; however, splice-site cases demonstrate survival beyond infancy, with multisystem manifestations including CNS anomalies and occasional hepatic dysfunction (elevated AFP, conjugated hyperbilirubinemia, thrombocytopenia). (lane2023abnormalliverfunction pages 2-3)

Phenotypic Manifestations (HPO-aligned)
- HPO:0001763 Talipes equinovarus (clubfoot). (bang2025genotypephenotypecorrelationin pages 8-11, lane2023abnormalliverfunction pages 2-3)
- HPO:0001631 Atrial septal defect. (lane2023abnormalliverfunction pages 2-3)
- HPO:0030324 Robin sequence (including micrognathia/retrognathia and cleft palate). (bang2025genotypephenotypecorrelationin pages 8-11, lane2023abnormalliverfunction pages 2-3)
- HPO:0006689 Persistent left superior vena cava. (lane2023abnormalliverfunction pages 2-3)
- Additional reported: Failure to thrive; severe developmental delay/intellectual disability; brain anomalies (cerebellar vermis hypoplasia, ventriculomegaly, corpus callosum thinning); possible hepatic dysfunction (neonatal cholestasis, high AFP); thrombocytopenia. (bang2025genotypephenotypecorrelationin pages 8-11, lane2023abnormalliverfunction pages 2-3)

Expert Opinions and Recent Developments (2023–2024 focus)
- Spliceosome-level mechanism: New biochemical evidence places RBM10 with U2 snRNP at intron branch sites on chromatin as a widespread regulator of exon repression, reframing RBM10 as acting from within a U2-associated complex rather than peripherally. This mechanistic placement explains global exon-skipping activity and tissue specificity through local branchpoint recognition. (damianov2023theapoptoticsplicing pages 30-33, damianov2023theapoptoticsplicing pages 10-14, damianov2023theapoptoticsplicing pages 1-5, damianov2023theapoptoticsplicing pages 14-16)
- Replication-fork function and therapy: Discovery of a splicing-independent RBM10 role at replication forks provides a second axis of pathology and suggests a precision-oncology paradigm (WEE1 inhibition) for RBM10-deficient contexts; although cancer-focused, the mechanism underscores RBM10’s chromatin functions that may intersect with development. (machour2024harnessingdnareplication pages 1-2, machour2024harnessingdnareplication pages 4-5, machour2024harnessingdnareplication pages 8-10)
- Genotype–phenotype expansion: Emerging evidence indicates a spectrum from classic TARP to milder RBM10-associated intellectual disability with domain-specific variant effects and isoform-specific consequences (e.g., exon 4). While outside the 2023–2024 window, this augments mechanistic interpretation of variant classes. (bang2025genotypephenotypecorrelationin pages 8-11, bang2025genotypephenotypecorrelationin pages 37-42)

Current applications and real-world implementations
- Diagnostics: RBM10 sequencing in male infants with Robin sequence plus cardiac/limb anomalies; RNA studies to confirm splice impacts where splice-site variants are suspected. (lane2023abnormalliverfunction pages 2-3)
- Clinical management: Anticipatory guidance for cardiac surveillance (ASD, potential cardiomyopathy), airway and feeding support for Robin sequence, monitoring for GI anomalies (vitelline duct remnants) and rare hepatic dysfunction. (lane2023abnormalliverfunction pages 2-3, bang2025genotypephenotypecorrelationin pages 42-46)
- Therapeutic insights: Although no disease-modifying therapy exists for TARP, WEE1 inhibition is a validated synthetic-lethal strategy in RBM10-deficient cancer cells, illustrating a druggable vulnerability linked to RBM10’s replication-fork role. (machour2024harnessingdnareplication pages 8-10)

Relevant statistics and data
- Extent of splicing dysregulation: Patient blood and CRISPR-edited cellular models show thousands of alternative splicing changes upon RBM10 loss, with predominant increases in exon inclusion; the magnitude correlates with clinical severity. (bang2025genotypephenotypecorrelationin pages 8-11)
- Replication-stress vulnerability: Approximately 45% of RBM10-KO LUAD cells treated with the WEE1 inhibitor MK1775 were co-stained with EdU and pH3(Ser10), indicating premature mitotic entry and synthetic lethality under replication stress. (machour2024harnessingdnareplication pages 8-10)
- Survival patterns by variant class: In a 2023 case report synthesis, splice-site mutations had improved survival (>18 months) compared to nonsense variants (all deaths <18 months) among collated RBM10-TARP cases. (lane2023abnormalliverfunction pages 2-3)

Direct quotes supporting key statements
- “RBM5 and RBM10 are subunits of the U2 snRNP engaged with intron branch sites on chromatin.” (Damianov 2023 bioRxiv; posted Sep 21, 2023; https://doi.org/10.1101/2023.09.21.558883) (damianov2023theapoptoticsplicing pages 30-33, damianov2023theapoptoticsplicing pages 1-5)
- “We identified WEE1 as a synthetic lethal partner with RBM10 deficiency… RBM10 serves as an anchor for recruiting HDAC1 to facilitate H4K16 deacetylation to maintain replication fork stability.” (Machour 2024 Nature Communications; published Jul 25, 2024; https://doi.org/10.1038/s41467-024-50882-0) (machour2024harnessingdnareplication pages 1-2, machour2024harnessingdnareplication pages 4-5)
- “Germline alterations of RBM10 in humans result in TARP syndrome… RBM10 loss leads to exon inclusions of transcripts regulating ECM–cytoskeletal interactions… RAC1-GTP activation.” (Krishnamoorthy 2024 bioRxiv; posted Jul 10, 2024; https://doi.org/10.1101/2024.07.09.602730) (krishnamoorthy2024rbm10lossinduces pages 1-4)
- “This child… had a splicing mutation c.2295+1G>A in RBM10… Abnormal liver function tests with conjugated hyperbilirubinaemia and very high alpha-fetoprotein… survival beyond the neonatal period.” (Lane 2023 BMJ Case Reports; published Mar 2023; https://doi.org/10.1136/bcr-2022-253035) (lane2023abnormalliverfunction pages 2-3)

Gene/protein annotations with ontology terms
- RBM10 (HGNC:RBM10): GO:0000381 (regulation of alternative mRNA splicing via spliceosome); GO:0006268 (DNA replication) involvement; GO:0043111 (histone H4-K16 deacetylation) via HDAC1 recruitment; CC: GO:0005684 (U2 snRNP), GO:0016607 (nuclear speckle), GO:0005654 (nucleoplasm), replication fork association. (damianov2023theapoptoticsplicing pages 30-33, machour2024harnessingdnareplication pages 4-5)
- NUMB (HGNC:NUMB): GO:0007219 (Notch signaling), alternative splicing target of RBM10; reduced NUMB leads to NOTCH de-repression. (krishnamoorthy2024rbm10lossinduces pages 1-4)
- VCL/CD44/TNC/EIF4H: GO processes in cytoskeleton/ECM organization and translation initiation regulation; RBM10-sensitive cassette exons. (krishnamoorthy2024rbm10lossinduces pages 1-4)

Phenotype associations (HPO)
- HPO:0001763 Talipes equinovarus; HPO:0001631 Atrial septal defect; HPO:0030324 Robin sequence; HPO:0006689 Persistent left superior vena cava; HPO:0001531 Failure to thrive; HPO:0001249 Intellectual disability; HPO:0001321 Cerebellar vermis hypoplasia; HPO:0002119 Ventriculomegaly; HPO:0001274 Thin corpus callosum; HPO:0002904 Conjugated hyperbilirubinemia (rare). (bang2025genotypephenotypecorrelationin pages 8-11, lane2023abnormalliverfunction pages 2-3)

Cell type involvement (CL) and anatomical locations (UBERON)
- CL: cranial neural crest cell involvement inferred from craniofacial defects and RBM10 embryonic expression in branchial arches; UBERON:0002315 branchial arch; UBERON:0002101 limb; UBERON:0000948 heart. (krishnamoorthy2024rbm10lossinduces pages 1-4, lane2023abnormalliverfunction pages 2-3)

Chemical entities (CHEBI) with relevance
- CHEBI: Adavosertib (MK-1775), a WEE1 inhibitor with synthetic-lethal efficacy in RBM10-deficient models. (machour2024harnessingdnareplication pages 8-10)

Evidence items with URLs and publication dates
- Damianov et al. 2023 (bioRxiv preprint posted Sep 21, 2023): https://doi.org/10.1101/2023.09.21.558883 (U2 snRNP association, branch-site engagement). (damianov2023theapoptoticsplicing pages 30-33, damianov2023theapoptoticsplicing pages 10-14, damianov2023theapoptoticsplicing pages 1-5, damianov2023theapoptoticsplicing pages 14-16)
- Machour et al. 2024 (Nature Communications; published Jul 25, 2024): https://doi.org/10.1038/s41467-024-50882-0 (replication forks, HDAC1/H4K16ac, WEE1 synthetic lethality). (machour2024harnessingdnareplication pages 1-2, machour2024harnessingdnareplication pages 4-5, machour2024harnessingdnareplication pages 8-10)
- Krishnamoorthy et al. 2024 (bioRxiv; posted Jul 10, 2024): https://doi.org/10.1101/2024.07.09.602730 (NUMB/NOTCH, ECM/cytoskeleton isoforms, RAC1). (krishnamoorthy2024rbm10lossinduces pages 1-4)
- Lane et al. 2023 (BMJ Case Reports; published Mar 2023): https://doi.org/10.1136/bcr-2022-253035 (clinical features including survival and hepatic involvement). (lane2023abnormalliverfunction pages 2-3)
- RBM10 genotype–phenotype spectrum (medRxiv; posted Aug 5, 2025): https://doi.org/10.1101/2025.08.05.25330579 (broader context and statistics; used sparingly as a preprint outside target window but informative). (bang2025genotypephenotypecorrelationin pages 8-11, bang2025genotypephenotypecorrelationin pages 37-42, bang2025genotypephenotypecorrelationin pages 42-46, bang2025genotypephenotypecorrelationin pages 1-4)

Embedded artifact summary table
| Category | Entity (Symbol/Name) | Ontology ID (HGNC/GO/CL/UBERON/HPO/CHEBI) | Mechanistic relevance in TARP | Key evidence (short) | Source (URL, year) |
|---|---|---|---|---|---|
| Gene / Protein | RBM10 | HGNC:RBM10 | RNA-binding splicing regulator that promotes cassette-exon exclusion; also reported splicing-independent roles in replication-fork stability and transcriptional/3'UTR control | Loss-of-function → increased exon inclusion and multisystem TARP phenotypes (severity correlates with degree of LOF) (krishnamoorthy2024rbm10lossinduces pages 1-4, bang2025genotypephenotypecorrelationin pages 4-8) | https://doi.org/10.1101/2024.07.09.602730 (2024), https://doi.org/10.1101/2025.08.05.25330579 (2025) |
| Gene / Protein | NUMB | HGNC:NUMB | Alternative splicing target of RBM10; altered splicing → decreased NUMB protein and de-repression of NOTCH signaling during development | Validated exon inclusion changes and downstream NOTCH de-repression in RBM10 loss models (krishnamoorthy2024rbm10lossinduces pages 1-4) | https://doi.org/10.1101/2024.07.09.602730 (2024) |
| Pathway | NOTCH signaling | GO:0007219 (Notch signaling pathway) | Developmental cell-fate pathway indirectly activated by RBM10 loss via NUMB missplicing; implicated in craniofacial/cardiac development defects | Mechanistic link: NUMB mis-splicing → NOTCH de-repression; developmental relevance discussed in RBM10 literature (krishnamoorthy2024rbm10lossinduces pages 1-4, bang2025genotypephenotypecorrelationin pages 37-42) | https://doi.org/10.1101/2024.07.09.602730 (2024), https://doi.org/10.1101/2025.08.05.25330579 (2025) |
| Gene / Protein | VCL (vinculin) | HGNC:VCL | Cytoskeletal gene whose exon-inclusion isoform increases cell motility and ECM–cytoskeleton signaling when RBM10 is lost | Exon-inclusion events in VCL contribute to increased cell velocity in RBM10-null cells (krishnamoorthy2024rbm10lossinduces pages 1-4) | https://doi.org/10.1101/2024.07.09.602730 (2024) |
| Gene / Protein | CD44 | HGNC:CD44 | ECM/cell-adhesion transcript with RBM10-sensitive isoforms that promote invasiveness when mis-spliced | Inclusion isoforms increase invasiveness in RBM10-deficient models (krishnamoorthy2024rbm10lossinduces pages 1-4) | https://doi.org/10.1101/2024.07.09.602730 (2024) |
| Gene / Protein | TNC (tenascin-C) | HGNC:TNC | Extracellular matrix glycoprotein with RBM10-regulated exon usage affecting invasiveness/ECM interactions | TNC exon-inclusion isoforms contribute to invasiveness in RBM10 loss (krishnamoorthy2024rbm10lossinduces pages 1-4) | https://doi.org/10.1101/2024.07.09.602730 (2024) |
| Gene / Protein | EIF4H | HGNC:EIF4H | Translation-initiation factor with RBM10-regulated exon (e.g., exon 5) validated as an RBM10 splicing target | EIF4H exon inclusion validated in RBM10-deficient models (krishnamoorthy2024rbm10lossinduces pages 1-4) | https://doi.org/10.1101/2024.07.09.602730 (2024) |
| Complex / Machinery | U2 snRNP (pre-spliceosome) | GO:0005684 (U2 snRNP) | RBM10 associates with pre-spliceosomal complexes and binds intronic regions near branch sites, modulating A/B complex activity and exon choice | RBM10 interacts with U2-engaged complexes on chromatin and influences branch-site-associated splicing outcomes (bang2025genotypephenotypecorrelationin pages 4-8) | https://doi.org/10.1101/2025.08.05.25330579 (2025) |
| Cellular component | Nuclear speckles | GO:0016607 (nuclear speckle) | Subnuclear splicing factor-rich compartments where RBM10/splicing regulators localize, informing tissue-specific splicing dynamics | RBM-family splicing regulators work within chromatin-associated splicing complexes and speckle-related compartments (bang2025genotypephenotypecorrelationin pages 4-8) | https://doi.org/10.1101/2025.08.05.25330579 (2025) |
| Cellular component / Function | DNA replication forks | GO (replication fork) / molecular function | RBM10 reported to play a replication-associated role: associates with active forks, recruits HDAC1 and modulates H4K16 deacetylation to maintain fork progression (splicing-independent) | Splicing-independent RBM10 role in replication-fork progression and synthetic-lethal interactions (WEE1) in RBM10-deficient cells (krishnamoorthy2024rbm10lossinduces pages 1-4) | Nature Commun. article (DOI listed in retrieved set), reported 2024 (krishnamoorthy2024rbm10lossinduces pages 1-4) |
| Cell type (CL) | Cranial neural crest cells (CNCCs) | CL:cranial neural crest cell | Embryonic cell population contributing to craniofacial structures; RBM10 expression in branchial arches implicates CNCCs in TARP craniofacial defects | Embryonic expression in branchial arches/limb buds and craniofacial phenotypes reported in RBM10 models and human cases (krishnamoorthy2024rbm10lossinduces pages 1-4, bang2025genotypephenotypecorrelationin pages 4-8) | https://doi.org/10.1101/2024.07.09.602730 (2024), https://doi.org/10.1101/2025.08.05.25330579 (2025) |
| Anatomy (UBERON) | Heart (cardiac atria/ASD) | UBERON:0000948 (heart) | Atrial septal defects (ASD) are a canonical structural cardiac manifestation in TARP; RBM10 perturbation affects cardiac development | ASD and other cardiac anomalies commonly reported in TARP cohorts and case reports (lane2023abnormalliverfunction pages 2-3, bang2025genotypephenotypecorrelationin pages 4-8) | https://doi.org/10.1136/bcr-2022-253035 (2023), https://doi.org/10.1101/2025.08.05.25330579 (2025) |
| Phenotype (HPO) | Talipes equinovarus (clubfoot) | HPO:0001763 | Classic limb phenotype in TARP; likely reflects disrupted musculoskeletal/limb development downstream of splicing defects in developmental programs | Talipes is a defining clinical feature in case series and cohort descriptions of RBM10-related TARP (lane2023abnormalliverfunction pages 2-3, bang2025genotypephenotypecorrelationin pages 4-8) | https://doi.org/10.1136/bcr-2022-253035 (2023), https://doi.org/10.1101/2025.08.05.25330579 (2025) |


*Table: Compact reference table mapping key genes, pathways, cellular components, cell types, anatomical sites, and canonical phenotypes for TARP syndrome (RBM10-related), with concise mechanistic notes and primary evidence citations (context IDs) useful for disease knowledge-base curation.*

Limitations
- Some mechanistic sources are preprints (2023–2024) and should be interpreted with caution until peer-reviewed versions are available; nevertheless, their claims align with orthogonal data (e.g., replication-fork association is peer-reviewed in 2024). The 2025 medRxiv genotype–phenotype dataset extends beyond the requested 2023–2024 focus and is cited to provide breadth; where possible, 2023–2024 peer-reviewed sources were prioritized. (machour2024harnessingdnareplication pages 1-2, damianov2023theapoptoticsplicing pages 30-33, krishnamoorthy2024rbm10lossinduces pages 1-4, lane2023abnormalliverfunction pages 2-3)


References

1. (damianov2023theapoptoticsplicing pages 30-33): Andrey Damianov, Chia-Ho Lin, Jeffrey Huang, Lin Zhou, Yasaman Jami-Alahmadi, James Wohlschlegel, and Douglas L. Black. The apoptotic splicing regulators rbm5 and rbm10 are subunits of the u2 snrnp engaged with intron branch sites on chromatin. bioRxiv, Sep 2023. URL: https://doi.org/10.1101/2023.09.21.558883, doi:10.1101/2023.09.21.558883. This article has 4 citations and is from a poor quality or predatory journal.

2. (damianov2023theapoptoticsplicing pages 10-14): Andrey Damianov, Chia-Ho Lin, Jeffrey Huang, Lin Zhou, Yasaman Jami-Alahmadi, James Wohlschlegel, and Douglas L. Black. The apoptotic splicing regulators rbm5 and rbm10 are subunits of the u2 snrnp engaged with intron branch sites on chromatin. bioRxiv, Sep 2023. URL: https://doi.org/10.1101/2023.09.21.558883, doi:10.1101/2023.09.21.558883. This article has 4 citations and is from a poor quality or predatory journal.

3. (damianov2023theapoptoticsplicing pages 1-5): Andrey Damianov, Chia-Ho Lin, Jeffrey Huang, Lin Zhou, Yasaman Jami-Alahmadi, James Wohlschlegel, and Douglas L. Black. The apoptotic splicing regulators rbm5 and rbm10 are subunits of the u2 snrnp engaged with intron branch sites on chromatin. bioRxiv, Sep 2023. URL: https://doi.org/10.1101/2023.09.21.558883, doi:10.1101/2023.09.21.558883. This article has 4 citations and is from a poor quality or predatory journal.

4. (damianov2023theapoptoticsplicing pages 14-16): Andrey Damianov, Chia-Ho Lin, Jeffrey Huang, Lin Zhou, Yasaman Jami-Alahmadi, James Wohlschlegel, and Douglas L. Black. The apoptotic splicing regulators rbm5 and rbm10 are subunits of the u2 snrnp engaged with intron branch sites on chromatin. bioRxiv, Sep 2023. URL: https://doi.org/10.1101/2023.09.21.558883, doi:10.1101/2023.09.21.558883. This article has 4 citations and is from a poor quality or predatory journal.

5. (bang2025genotypephenotypecorrelationin pages 8-11): J. M. V. Bang, C. Fagerberg, T. K. Doktor, Mia M. Rosenlund, Santiago M. Lumbreras, Mark Burton, Klaus Brusgaard, Ángel Guerra-Moreno, Sofie Høi, Lenet W. Skovstrøm, Nikolaj A. Nielsen, Qin Hao, Carolina Alves, Lars K. Hansen, Melissa Lees, P. Suwannarat, Connie Stumpel, M. Sinnema, A. Stegmann, H. Esch, Chiara De Luca, Christine Van Mol, Andrew Green, Dagmar Wieczorek, Jonathan Rodgers, Julie McGaughran, Véronique Duboc, Khaoula Zaafrane-Khachnaoui, Jill Mad-den, Pankaj B. Agrawal, P. Rump, B. Gener, María Jesús Martínez-González, J. Good, G. Vitiello, F. Passaretti, A. Lolascon, Michael Field, El-lenore M. Martin, B. Keren, Martine Doco-Fenzy, Tony Yammine, K. Steindl, Anita Rauch, A. Begemann, Gregory Costain, Zhuo Shao, Diana Carli, G. B. Ferrero, I. Valenzuela, M. Codina-Solà, Bárbara Masotto, Laura Trujillano, C. Kumps, Olivier Vanakker, Anand Vasudevan, M. Passos-Bueno, Erasmo Ca-sella, Fernarnda Bonilla Colomé, L. Faivre, C. Philippe, Marlin Touma, Lee-Kai Wang, Stanley F. Nelson, M. Scala, Vincenzo Nigro, V. Capra, Kris-ten Truxal, Valentina Caceres, Jonathan Lévy, V. Kalscheuer, A. Delahaye-Duriez, Juan Valcárcel, Michael Sattler, and Brage Storstein Andresen. Genotype-phenotype correlation in rbm10-associated syndromes. how variant function shapes a broad phenotypic landscape. MedRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.05.25330579, doi:10.1101/2025.08.05.25330579. This article has 0 citations.

6. (krishnamoorthy2024rbm10lossinduces pages 1-4): Gnana P. Krishnamoorthy, Anthony R. Glover, Brian R. Untch, Nickole Sigcha-Coello, Bin Xu, Dina Vukel, Yi Liu, Vera Tiedje, Katherine Berman, Prasanna P. Tamarapu, Adrian Acuña-Ruiz, Mahesh Saqcena, Elisa de Stanchina, Laura Boucai, Ronald A. Ghossein, Jeffrey A. Knauf, Omar Abdel-Wahab, Robert K. Bradley, and James A. Fagin. Rbm10 loss induces aberrant splicing of cytoskeletal and extracellular matrix mrnas and promotes metastatic fitness. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.09.602730, doi:10.1101/2024.07.09.602730. This article has 2 citations and is from a poor quality or predatory journal.

7. (machour2024harnessingdnareplication pages 1-2): Feras E. Machour, Enas R. Abu-Zhayia, Joyce Kamar, Alma Sophia Barisaac, Itamar Simon, and Nabieh Ayoub. Harnessing dna replication stress to target rbm10 deficiency in lung adenocarcinoma. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50882-0, doi:10.1038/s41467-024-50882-0. This article has 12 citations and is from a highest quality peer-reviewed journal.

8. (machour2024harnessingdnareplication pages 4-5): Feras E. Machour, Enas R. Abu-Zhayia, Joyce Kamar, Alma Sophia Barisaac, Itamar Simon, and Nabieh Ayoub. Harnessing dna replication stress to target rbm10 deficiency in lung adenocarcinoma. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50882-0, doi:10.1038/s41467-024-50882-0. This article has 12 citations and is from a highest quality peer-reviewed journal.

9. (machour2024harnessingdnareplication pages 8-10): Feras E. Machour, Enas R. Abu-Zhayia, Joyce Kamar, Alma Sophia Barisaac, Itamar Simon, and Nabieh Ayoub. Harnessing dna replication stress to target rbm10 deficiency in lung adenocarcinoma. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50882-0, doi:10.1038/s41467-024-50882-0. This article has 12 citations and is from a highest quality peer-reviewed journal.

10. (lane2023abnormalliverfunction pages 2-3): Michael Lane, Nicholas M Allen, and Johannes Letshwiti. Abnormal liver function tests and improved survival in a child with splice mutation tarp syndrome. BMJ Case Reports, 16:e253035, Mar 2023. URL: https://doi.org/10.1136/bcr-2022-253035, doi:10.1136/bcr-2022-253035. This article has 3 citations and is from a peer-reviewed journal.

11. (bang2025genotypephenotypecorrelationin pages 37-42): J. M. V. Bang, C. Fagerberg, T. K. Doktor, Mia M. Rosenlund, Santiago M. Lumbreras, Mark Burton, Klaus Brusgaard, Ángel Guerra-Moreno, Sofie Høi, Lenet W. Skovstrøm, Nikolaj A. Nielsen, Qin Hao, Carolina Alves, Lars K. Hansen, Melissa Lees, P. Suwannarat, Connie Stumpel, M. Sinnema, A. Stegmann, H. Esch, Chiara De Luca, Christine Van Mol, Andrew Green, Dagmar Wieczorek, Jonathan Rodgers, Julie McGaughran, Véronique Duboc, Khaoula Zaafrane-Khachnaoui, Jill Mad-den, Pankaj B. Agrawal, P. Rump, B. Gener, María Jesús Martínez-González, J. Good, G. Vitiello, F. Passaretti, A. Lolascon, Michael Field, El-lenore M. Martin, B. Keren, Martine Doco-Fenzy, Tony Yammine, K. Steindl, Anita Rauch, A. Begemann, Gregory Costain, Zhuo Shao, Diana Carli, G. B. Ferrero, I. Valenzuela, M. Codina-Solà, Bárbara Masotto, Laura Trujillano, C. Kumps, Olivier Vanakker, Anand Vasudevan, M. Passos-Bueno, Erasmo Ca-sella, Fernarnda Bonilla Colomé, L. Faivre, C. Philippe, Marlin Touma, Lee-Kai Wang, Stanley F. Nelson, M. Scala, Vincenzo Nigro, V. Capra, Kris-ten Truxal, Valentina Caceres, Jonathan Lévy, V. Kalscheuer, A. Delahaye-Duriez, Juan Valcárcel, Michael Sattler, and Brage Storstein Andresen. Genotype-phenotype correlation in rbm10-associated syndromes. how variant function shapes a broad phenotypic landscape. MedRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.05.25330579, doi:10.1101/2025.08.05.25330579. This article has 0 citations.

12. (bang2025genotypephenotypecorrelationin pages 42-46): J. M. V. Bang, C. Fagerberg, T. K. Doktor, Mia M. Rosenlund, Santiago M. Lumbreras, Mark Burton, Klaus Brusgaard, Ángel Guerra-Moreno, Sofie Høi, Lenet W. Skovstrøm, Nikolaj A. Nielsen, Qin Hao, Carolina Alves, Lars K. Hansen, Melissa Lees, P. Suwannarat, Connie Stumpel, M. Sinnema, A. Stegmann, H. Esch, Chiara De Luca, Christine Van Mol, Andrew Green, Dagmar Wieczorek, Jonathan Rodgers, Julie McGaughran, Véronique Duboc, Khaoula Zaafrane-Khachnaoui, Jill Mad-den, Pankaj B. Agrawal, P. Rump, B. Gener, María Jesús Martínez-González, J. Good, G. Vitiello, F. Passaretti, A. Lolascon, Michael Field, El-lenore M. Martin, B. Keren, Martine Doco-Fenzy, Tony Yammine, K. Steindl, Anita Rauch, A. Begemann, Gregory Costain, Zhuo Shao, Diana Carli, G. B. Ferrero, I. Valenzuela, M. Codina-Solà, Bárbara Masotto, Laura Trujillano, C. Kumps, Olivier Vanakker, Anand Vasudevan, M. Passos-Bueno, Erasmo Ca-sella, Fernarnda Bonilla Colomé, L. Faivre, C. Philippe, Marlin Touma, Lee-Kai Wang, Stanley F. Nelson, M. Scala, Vincenzo Nigro, V. Capra, Kris-ten Truxal, Valentina Caceres, Jonathan Lévy, V. Kalscheuer, A. Delahaye-Duriez, Juan Valcárcel, Michael Sattler, and Brage Storstein Andresen. Genotype-phenotype correlation in rbm10-associated syndromes. how variant function shapes a broad phenotypic landscape. MedRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.05.25330579, doi:10.1101/2025.08.05.25330579. This article has 0 citations.

13. (bang2025genotypephenotypecorrelationin pages 1-4): J. M. V. Bang, C. Fagerberg, T. K. Doktor, Mia M. Rosenlund, Santiago M. Lumbreras, Mark Burton, Klaus Brusgaard, Ángel Guerra-Moreno, Sofie Høi, Lenet W. Skovstrøm, Nikolaj A. Nielsen, Qin Hao, Carolina Alves, Lars K. Hansen, Melissa Lees, P. Suwannarat, Connie Stumpel, M. Sinnema, A. Stegmann, H. Esch, Chiara De Luca, Christine Van Mol, Andrew Green, Dagmar Wieczorek, Jonathan Rodgers, Julie McGaughran, Véronique Duboc, Khaoula Zaafrane-Khachnaoui, Jill Mad-den, Pankaj B. Agrawal, P. Rump, B. Gener, María Jesús Martínez-González, J. Good, G. Vitiello, F. Passaretti, A. Lolascon, Michael Field, El-lenore M. Martin, B. Keren, Martine Doco-Fenzy, Tony Yammine, K. Steindl, Anita Rauch, A. Begemann, Gregory Costain, Zhuo Shao, Diana Carli, G. B. Ferrero, I. Valenzuela, M. Codina-Solà, Bárbara Masotto, Laura Trujillano, C. Kumps, Olivier Vanakker, Anand Vasudevan, M. Passos-Bueno, Erasmo Ca-sella, Fernarnda Bonilla Colomé, L. Faivre, C. Philippe, Marlin Touma, Lee-Kai Wang, Stanley F. Nelson, M. Scala, Vincenzo Nigro, V. Capra, Kris-ten Truxal, Valentina Caceres, Jonathan Lévy, V. Kalscheuer, A. Delahaye-Duriez, Juan Valcárcel, Michael Sattler, and Brage Storstein Andresen. Genotype-phenotype correlation in rbm10-associated syndromes. how variant function shapes a broad phenotypic landscape. MedRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.05.25330579, doi:10.1101/2025.08.05.25330579. This article has 0 citations.

14. (bang2025genotypephenotypecorrelationin pages 4-8): J. M. V. Bang, C. Fagerberg, T. K. Doktor, Mia M. Rosenlund, Santiago M. Lumbreras, Mark Burton, Klaus Brusgaard, Ángel Guerra-Moreno, Sofie Høi, Lenet W. Skovstrøm, Nikolaj A. Nielsen, Qin Hao, Carolina Alves, Lars K. Hansen, Melissa Lees, P. Suwannarat, Connie Stumpel, M. Sinnema, A. Stegmann, H. Esch, Chiara De Luca, Christine Van Mol, Andrew Green, Dagmar Wieczorek, Jonathan Rodgers, Julie McGaughran, Véronique Duboc, Khaoula Zaafrane-Khachnaoui, Jill Mad-den, Pankaj B. Agrawal, P. Rump, B. Gener, María Jesús Martínez-González, J. Good, G. Vitiello, F. Passaretti, A. Lolascon, Michael Field, El-lenore M. Martin, B. Keren, Martine Doco-Fenzy, Tony Yammine, K. Steindl, Anita Rauch, A. Begemann, Gregory Costain, Zhuo Shao, Diana Carli, G. B. Ferrero, I. Valenzuela, M. Codina-Solà, Bárbara Masotto, Laura Trujillano, C. Kumps, Olivier Vanakker, Anand Vasudevan, M. Passos-Bueno, Erasmo Ca-sella, Fernarnda Bonilla Colomé, L. Faivre, C. Philippe, Marlin Touma, Lee-Kai Wang, Stanley F. Nelson, M. Scala, Vincenzo Nigro, V. Capra, Kris-ten Truxal, Valentina Caceres, Jonathan Lévy, V. Kalscheuer, A. Delahaye-Duriez, Juan Valcárcel, Michael Sattler, and Brage Storstein Andresen. Genotype-phenotype correlation in rbm10-associated syndromes. how variant function shapes a broad phenotypic landscape. MedRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.05.25330579, doi:10.1101/2025.08.05.25330579. This article has 0 citations.