---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:01:54.112150'
end_time: '2025-12-15T09:08:16.936687'
duration_seconds: 382.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Nephronophthisis
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Nephronophthisis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Nephronophthisis**.
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
- **Disease Name:** Nephronophthisis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Nephronophthisis**.
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


Plan (concise)
- Identify recent sources (2023–2024) on nephronophthisis (NPHP) mechanisms; supplement with 2025 mechanistic/translational updates (completed). (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10)
- Extract molecular/cellular mechanisms and key pathways, genes, and organelles (completed). (sudhindar2025urinaryrenalepithelial pages 1-2, tata2023eupatilinetagonistes pages 38-42, kalot2024primaryciliaand pages 10-11, garvi2025lossofnephronophthisisassociated pages 1-3, roig2025nek8animafamily pages 1-2)
- Map ontology-aligned annotations (genes, GO processes/components; CL cell types; UBERON anatomy; HPO phenotypes; CHEBI chemicals) (completed). (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10)
- Synthesize disease progression and phenotype links with quantitative data and quotes (completed). (kalot2024primaryciliaand pages 10-11, clerici2025metabolicreprogrammingin pages 2-3, ajiboye2023autosomalrecessiveadolescent pages 1-2)
- Summarize recent developments (2023–2024 priority; include 2025 when informative) (completed). (sudhindar2025urinaryrenalepithelial pages 1-2, kalot2024primaryciliaand pages 10-11, clerici2025metabolicreprogrammingin pages 2-3)
- Deliver comprehensive, well-cited report (completed).

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Nephronophthisis
- MONDO ID: —
- Category: Genetic (autosomal recessive, renal ciliopathy)

Pathophysiology description (narrative)
Nephronophthisis (NPHP) is a prototypical renal ciliopathy driven by defects in proteins that localize to the primary cilium, its basal body/transition zone, or associated junctional and cytoskeletal complexes. Clinically, NPHP presents with polyuria/polydipsia due to impaired urinary concentrating ability, chronic tubulointerstitial nephritis, progressive interstitial fibrosis and tubular atrophy, and often small corticomedullary cysts, culminating in chronic kidney disease and end-stage renal disease (ESRD) in childhood or young adulthood. “Most patients [with NPHP] progress to end-stage renal disease before age 30,” and histology shows “loss of corticomedullary differentiation… tubular atrophy… interstitial fibrosis; cysts occur in ~70% but are smaller than in ADPKD” (Frontiers in Nephrology, 2024; DOI: 10.3389/fneph.2023.1331847) (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10). NPHP is the commonest genetic cause of kidney failure in infants/adolescents; symptoms reflect tubular epithelium dysfunction and fibrosis shared across renal ciliopathies (EMBO Molecular Medicine, 2025; DOI: 10.1038/s44321-025-00239-x) (clerici2025metabolicreprogrammingin pages 2-3).

At the molecular level, nephrocystin proteins (NPHP1–NPHP… and related factors such as TTC21B/IFT139, GLIS2/NPHP7, NEK8/NPHP9, INVS/NPHP2) organize ciliary structure and gating, intraflagellar transport, actin and microtubule dynamics, and junctional/polarity complexes. Disruption of these systems alters ciliary signaling (WNT/PCP vs canonical WNT, Hedgehog, EGFR/RTK, Hippo/YAP/TAZ, cAMP–mTOR), cell polarity, and epithelial–mesenchymal crosstalk, which converge on tubular atrophy and interstitial fibrosis. Recent work emphasizes cilia–actin regulation: aberrant RhoA signaling emanating from the centrosome (via GEF‑H1) activates ROCK and engages Hippo signaling; GEF‑H1 knockdown rescues Nphp1 mouse phenotypes, reducing cystogenesis, fibrosis and inflammation (Frontiers in Nephrology, 2024) (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10). NPHP1 (nephrocystin‑1) also links ciliary/basal body hubs to adherens junctions and focal adhesions and shows emerging roles in DNA damage response (DDR) and senescence in kidney organoids (bioRxiv, 2025; DOI: 10.1101/2025.06.09.658557) (garvi2025lossofnephronophthisisassociated pages 1-3).

Key concepts and definitions
- Primary cilium: solitary microtubule-based organelle with a basal body/transition zone that transduces mechanical and chemical cues (e.g., WNT, Hedgehog, RTK, cAMP/mTOR) to coordinate epithelial morphogenesis and homeostasis. Renal ciliopathies share cystic dilation, inflammation, and fibrosis, with NPHP showing smaller corticomedullary cysts and dominant tubulointerstitial fibrosis (EMBO Mol Med, 2025) (clerici2025metabolicreprogrammingin pages 2-3).
- Nephrocystins: proteins encoded by NPHP genes; many form complexes at the transition zone, INV compartment, or cytoskeletal/junctional interfaces, regulating ciliogenesis, ciliary gating, polarity, and signaling (Frontiers in Nephrology, 2024; Cell Commun Signal, 2025; DOI: 10.1186/s12964-025-02143-w) (kalot2024primaryciliaand pages 10-11, roig2025nek8animafamily pages 1-2).
- INV compartment: ciliary subdomain marked by inversin (INVS/NPHP2), NEK8 (NPHP9), ANKS6, and NPHP3, crucial for left–right patterning and organogenesis; mechanistic substrates of NEK8 remain incompletely defined (Cell Commun Signal, 2025) (roig2025nek8animafamily pages 1-2).

Recent developments and latest research (2023–2024 priority)
- Cilia–actin–Hippo axis: Review of primary cilia and actin regulators in renal ciliopathies highlights actin remodeling at the ciliary base as a key determinant of ciliogenesis and implicates aberrant RhoA/ROCK and Hippo/YAP/TAZ signaling in NPHP pathogenesis; genetic suppression of GEF‑H1 ameliorates cystogenesis and fibrosis in Nphp1 models (Frontiers in Nephrology, 2024; URL: https://doi.org/10.3389/fneph.2023.1331847; published Jan 2024) (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10).
- Genetic architecture and modifiers: Tubulointerstitial kidney diseases (including NPHP) show variable onset and severity not fully explained by monogenic variants, supporting roles for genetic modifiers bridging monogenic TKD and broader CKD spectra (Genes, 2023; DOI: 10.3390/genes14081582; published Aug 2023) (tata2023eupatilinetagonistes pages 38-42).
- Translational patient-derived cell models: In NPHP1-deleted patient urine-derived renal epithelial cells (hURECs), transcriptomics show altered EGFR signaling, extracellular matrix and adherens junctions; alprostadil increased ciliation but worsened ciliary elongation, whereas “EGFR kinase inhibitor AG556 rescued ciliary length and morphology” and reversed disease signatures better than alprostadil (J Cell Sci, 2025; DOI: 10.1242/jcs.264141; online Sep 2025) (sudhindar2025urinaryrenalepithelial pages 1-2).
- DDR and tubular senescence: NPHP1 deficiency impairs DNA damage repair in kidney organoids, with nuclear translocation of nephrocystin‑1 after UVC stress, increased senescence and fibrosis, strengthening the DDR axis in NPHP pathophysiology (bioRxiv, 2025; posted Jun 2025) (garvi2025lossofnephronophthisisassociated pages 1-3).
- Metabolic reprogramming across renal ciliopathies: Evidence supports mitochondrial and metabolic alterations as a unifying feature that may help explain divergent PKD vs NPH phenotypes; proposes broader metabolic involvement in ciliopathies (EMBO Mol Med, 2025; Apr 2025) (clerici2025metabolicreprogrammingin pages 2-3).

Current applications and real-world implementations
- Precision phenotyping from urine-derived renal epithelial cells (hURECs) enables mechanism-to-therapy testing for NPHP1, including EGFR inhibitor response signatures vs prostaglandin agonists (J Cell Sci, 2025) (sudhindar2025urinaryrenalepithelial pages 1-2).
- Genetic testing is central to diagnosis; however, “about 40% of nephronophthisis cases go undiagnosed” genetically, underscoring need for expanded panels/functional assays (Am J Case Rep, 2023; Oct 2023) (ajiboye2023autosomalrecessiveadolescent pages 1-2).

Expert opinions and analysis
- Actin remodeling and Hippo/YAP/TAZ dysregulation represent convergent downstream effectors of ciliary dysfunction in NPHP, offering therapeutic entry points (Frontiers in Nephrology, 2024) (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10).
- The INV complex (INVS/NPHP2–NEK8/NPHP9–ANKS6–NPHP3) is a mechanistic nexus for ciliary signaling control and left–right patterning; gaps remain regarding NEK8 substrates/regulation, a priority for future target discovery (Cell Commun Signal, 2025) (roig2025nek8animafamily pages 1-2).
- DDR involvement provides a plausible link between ciliary defects, epithelial stress responses, and pro-fibrotic remodeling; targeted modulation of DDR/senescence warrants investigation (bioRxiv, 2025) (garvi2025lossofnephronophthisisassociated pages 1-3).

Relevant statistics and data
- Cysts occur in approximately 70% of NPHP, but are smaller than in ADPKD; ESRD typically before age 30 (Frontiers in Nephrology, 2024) (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10).
- NPHP accounts for about 5% of renal failure in children and adolescents; liver fibrosis in 10–20% of cases; syndromic overlaps include retinitis pigmentosa (Am J Case Rep, 2023) (ajiboye2023autosomalrecessiveadolescent pages 1-2).
- NPHP1 is the first and most common gene; literature reports range from 20–50% of genetically solved cases to “> two-thirds of cases” for homozygous deletions in certain cohorts or analytical contexts, reflecting cohort/testing differences (Frontiers in Nephrology, 2024; J Cell Sci, 2025) (kalot2024primaryciliaand pages 10-11, sudhindar2025urinaryrenalepithelial pages 1-2).

Core Pathophysiology
- Primary mechanisms: Primary cilium dysfunction at the basal body/transition zone and INV compartment; disrupted ciliogenesis and ciliary gating; altered actin and microtubule dynamics; polarity/junctional defects; maladaptive signaling (WNT/PCP vs canonical WNT, Hedgehog, EGFR/RTK, Hippo/YAP/TAZ, cAMP–mTOR); DDR deficits and epithelial senescence; interstitial fibroblast activation and fibrosis (Frontiers in Nephrology, 2024; EMBO Mol Med, 2025; bioRxiv, 2025) (kalot2024primaryciliaand pages 10-11, clerici2025metabolicreprogrammingin pages 2-3, garvi2025lossofnephronophthisisassociated pages 1-3).
- Dysregulated pathways: WNT (INVS antagonizes canonical WNT and promotes PCP via Dvl), Hippo (NPHP4–LATS1/YAP; NEK8–TAZ interactions), EGFR/RTK (EGFR signaling enrichment in NPHP1 hURECs; EGFR inhibition rescues cilia metrics), cAMP–mTOR (secondary to disturbed flow/Ca2+–AC signaling), Hedgehog and Notch signaling axes within ciliary hubs (J Cell Sci, 2025; Frontiers in Nephrology, 2024; 2023 prostaglandin/hippo text) (sudhindar2025urinaryrenalepithelial pages 1-2, kalot2024primaryciliaand pages 10-11, tata2023eupatilinetagonistes pages 38-42).
- Affected cellular processes: Ciliogenesis and intraflagellar transport; planar cell polarity; apicobasal polarity; adherens/tight junction integrity; mechanosensation and Ca2+–cAMP homeostasis; DNA repair; profibrotic extracellular matrix remodeling (Frontiers in Nephrology, 2024; bioRxiv, 2025) (kalot2024primaryciliaand pages 10-11, garvi2025lossofnephronophthisisassociated pages 1-3).

Key Molecular Players
- Genes/Proteins (HGNC): NPHP1 (nephrocystin‑1; transition zone/junctions; DDR) (sudhindar2025urinaryrenalepithelial pages 1-2, garvi2025lossofnephronophthisisassociated pages 1-3); INVS/NPHP2 (inversin; canonical WNT antagonism; PCP) (tata2023eupatilinetagonistes pages 38-42, kalot2024primaryciliaand pages 10-11); NPHP3 (INV complex) (roig2025nek8animafamily pages 1-2); NPHP4 (Hippo/YAP modulation; polarity) (tata2023eupatilinetagonistes pages 38-42, kalot2024primaryciliaand pages 10-11); NEK8/NPHP9 (ciliary kinase; INV core) (roig2025nek8animafamily pages 1-2); GLIS2/NPHP7 (transcription factor in NPH phenotypes) (kalot2024primaryciliaand pages 10-11); TTC21B/IFT139 (retrograde IFT; trafficking) (kalot2024primaryciliaand pages 10-11, clerici2025metabolicreprogrammingin pages 2-3).
- Chemical entities (CHEBI): Prostaglandin E1 (alprostadil) modulates ciliation/length; cAMP; Ca2+; EGFR kinase inhibitors (e.g., AG556, experimental in hURECs) (J Cell Sci, 2025) (sudhindar2025urinaryrenalepithelial pages 1-2).
- Cell types (CL): Renal tubular epithelial cells (primary site of ciliary dysfunction), interstitial fibroblasts (fibrosis effectors) (Frontiers in Nephrology, 2024) (kalot2024primaryciliaand pages 10-11).
- Anatomical locations (UBERON): Kidney (tubulointerstitium), renal tubules, corticomedullary junction (site of small cysts) (Frontiers in Nephrology, 2024; EMBO Mol Med, 2025) (kalot2024primaryciliaand pages 10-11, clerici2025metabolicreprogrammingin pages 2-3).

Biological Processes (for GO annotation; names)
- Ciliogenesis; ciliary gating; intraflagellar transport (IFT)
- Planar cell polarity (PCP) signaling; canonical WNT signaling; Hedgehog signaling; EGFR/RTK signaling; Hippo/YAP/TAZ signaling; cAMP–mTOR signaling
- Actin cytoskeleton organization; microtubule dynamics; apicobasal polarity; adherens/tight junction organization
- Mechanosensory response to fluid flow; calcium signaling; regulation of epithelial cell proliferation and differentiation
- DNA damage response; cellular senescence; extracellular matrix organization and fibrosis (kalot2024primaryciliaand pages 10-11, garvi2025lossofnephronophthisisassociated pages 1-3, sudhindar2025urinaryrenalepithelial pages 1-2)

Cellular Components (GO-like; names)
- Primary cilium (axoneme), basal body, transition zone; INV compartment
- Adherens junctions; tight junctions; focal adhesions; cortical actin cytoskeleton
- Centrosome; nucleus (for DDR-related roles) (kalot2024primaryciliaand pages 10-11, garvi2025lossofnephronophthisisassociated pages 1-3, roig2025nek8animafamily pages 1-2)

Disease Progression
- Initiation: Biallelic pathogenic variants in NPHP genes disrupt ciliary structure/function (transition zone/INV/IFT), polarity, and actin dynamics; early impairment of urine-concentrating ability leads to polyuria/polydipsia (Frontiers in Nephrology, 2024; EMBO Mol Med, 2025) (kalot2024primaryciliaand pages 10-11, clerici2025metabolicreprogrammingin pages 2-3).
- Propagation: Altered ciliary signaling (WNT/PCP, EGFR/RTK, Hippo/YAP, cAMP–mTOR) drives epithelial injury; DDR defects and senescence amplify inflammatory and fibrotic pathways (bioRxiv, 2025) (garvi2025lossofnephronophthisisassociated pages 1-3).
- Tissue remodeling: Tubular basement membrane disruption, tubular atrophy, and interstitial fibrosis develop; small corticomedullary cysts may emerge in ~70% (Frontiers in Nephrology, 2024) (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10).
- Clinical outcome: Progressive CKD with ESRD typically by young adulthood; syndromic extensions involve retina (Senior–Løken), liver (congenital hepatic fibrosis) and others (Am J Case Rep, 2023; EMBO Mol Med, 2025) (ajiboye2023autosomalrecessiveadolescent pages 1-2, clerici2025metabolicreprogrammingin pages 2-3).

Phenotypic Manifestations (with links to mechanisms)
- Polyuria/polydipsia and impaired concentrating ability: collecting duct cilium dysfunction and altered cAMP–mTOR/Ca2+ signaling (EMBO Mol Med, 2025; Frontiers in Nephrology, 2024) (clerici2025metabolicreprogrammingin pages 2-3, kalot2024primaryciliaand pages 10-11).
- Tubulointerstitial nephritis and interstitial fibrosis: epithelial injury, Hippo/YAP activation, actin/polarity defects, DDR-driven senescence; “tubulointerstitial fibrosis is the predominant feature” (Am J Case Rep, 2023; Oct 2023) (ajiboye2023autosomalrecessiveadolescent pages 1-2, kalot2024primaryciliaand pages 10-11).
- Corticomedullary cysts: spindle orientation/PCP defects, cAMP–mTOR dysregulation; smaller and fewer than ADPKD (~70%) (Frontiers in Nephrology, 2024) (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10).
- Extrarenal: Retinitis pigmentosa (Senior–Løken), liver fibrosis (10–20%); laterality defects with INV complex disruption (Am J Case Rep, 2023; Cell Commun Signal, 2025) (ajiboye2023autosomalrecessiveadolescent pages 1-2, roig2025nek8animafamily pages 1-2).

Evidence quotes (selected)
- “Most patients… progress to end-stage renal disease before age 30… histology shows… tubular atrophy… interstitial fibrosis; cysts occur in ~70% but are smaller than in ADPKD.” (Frontiers in Nephrology, 2024; https://doi.org/10.3389/fneph.2023.1331847) (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10).
- “Alprostadil increased ciliation but worsened ciliary elongation… EGFR kinase inhibitor AG556 rescued ciliary length and morphology [and] reversed the disease signature more effectively.” (J Cell Sci, 2025; https://doi.org/10.1242/jcs.264141) (sudhindar2025urinaryrenalepithelial pages 1-2).
- “NPHP is associated with extrarenal manifestations… liver fibrosis in 10–20% of cases… accounts for about 5% of renal failure in children and adolescents.” (Am J Case Rep, 2023; https://doi.org/10.12659/ajcr.941413) (ajiboye2023autosomalrecessiveadolescent pages 1-2).

Ontology-aligned annotations
- Gene/Protein (HGNC): NPHP1, INVS (NPHP2), NPHP3, NPHP4, NEK8 (NPHP9), GLIS2 (NPHP7), TTC21B (IFT139) (kalot2024primaryciliaand pages 10-11, roig2025nek8animafamily pages 1-2).
- Biological Processes (GO names): ciliogenesis; intraflagellar transport; planar cell polarity; canonical WNT signaling; Hedgehog signaling; EGFR signaling; Hippo/YAP/TAZ signaling; cAMP–mTOR signaling; actin cytoskeleton organization; apicobasal polarity; adherens junction organization; mechanosensation; calcium signaling; DNA damage response; extracellular matrix organization/fibrosis (kalot2024primaryciliaand pages 10-11, garvi2025lossofnephronophthisisassociated pages 1-3, sudhindar2025urinaryrenalepithelial pages 1-2).
- Cellular Components (GO names): primary cilium; basal body; transition zone; INV compartment; adherens junction; tight junction; focal adhesion; centrosome; nucleus (kalot2024primaryciliaand pages 10-11, roig2025nek8animafamily pages 1-2, garvi2025lossofnephronophthisisassociated pages 1-3).
- Cell Types (CL names): renal tubular epithelial cell; interstitial fibroblast (kalot2024primaryciliaand pages 10-11).
- Anatomical Locations (UBERON names): kidney; renal tubule; corticomedullary junction; tubulointerstitium (kalot2024primaryciliaand pages 10-11, clerici2025metabolicreprogrammingin pages 2-3).
- Phenotype associations (HPO names): polyuria; polydipsia; impaired urinary concentrating ability; tubulointerstitial nephritis; interstitial fibrosis; corticomedullary cysts; retinitis pigmentosa; congenital hepatic fibrosis (kalot2024primaryciliaand pages 10-11, ajiboye2023autosomalrecessiveadolescent pages 1-2, clerici2025metabolicreprogrammingin pages 2-3).
- Chemical entities (CHEBI names): prostaglandin E1 (alprostadil); cAMP; calcium ion; EGFR inhibitors (class) (sudhindar2025urinaryrenalepithelial pages 1-2).

Embedded summary artifact
| Gene/Protein | Role/Mechanism | Pathway(s) | Cellular Component(s) | Primary Cell Type(s) | Key Process(es) | Evidence |
|---|---|---|---|---|---|---|
| NPHP1 (NPHP1) | Scaffold at ciliary transition zone; links cilium to adherens junctions and participates in DNA damage response | Ciliary signaling (Hedgehog, Wnt); EGFR/RTK | Primary cilium; basal body/transition zone; adherens junctions | Renal tubular epithelial cells | Ciliogenesis; cell polarity; DNA damage response; fibrosis | (sudhindar2025urinaryrenalepithelial pages 1-2, garvi2025lossofnephronophthisisassociated pages 1-3, kalot2024primaryciliaand pages 10-11) |
| INVS (NPHP2) | Inversin: antagonizes canonical Wnt and promotes planar cell polarity via Dvl recruitment | Wnt (canonical & PCP); ciliary signaling | INV compartment; primary cilium; basal body | Tubular epithelial cells | Planar cell polarity; ciliary gating; left-right patterning | (tata2023eupatilinetagonistes pages 38-42, kalot2024primaryciliaand pages 10-11) |
| NPHP3 | INV-complex component involved in organogenesis and ciliary signaling scaffolding | INV complex; PCP; Wnt | INV compartment; cilium | Renal tubular epithelial cells | Ciliogenesis; signaling scaffold; organ laterality | (roig2025nek8animafamily pages 1-2, tata2023eupatilinetagonistes pages 38-42) |
| NPHP4 | Nephrocystin-4: modulates Hippo pathway (LATS1/YAP) and apicobasal polarity | Hippo (YAP/TAZ); actin cytoskeleton | Ciliary base; centrosome; cortical cytoskeleton | Tubular epithelial cells | YAP/TAZ regulation; apicobasal polarity; fibrosis | (tata2023eupatilinetagonistes pages 38-42, kalot2024primaryciliaand pages 10-11) |
| NEK8 (NPHP9) | NIMA-family ciliary kinase in the INV complex; regulatory substrates largely unresolved | INV complex signaling; Hippo interaction | INV compartment of primary cilium; basal body | Renal tubular epithelial cells | Ciliogenesis; ciliary signaling; organ development; fibrosis | (roig2025nek8animafamily pages 1-2, kalot2024primaryciliaand pages 10-11) |
| GLIS2 (NPHP7) | Zinc-finger transcription factor linked to NPH phenotypes; influences differentiation and stress responses | Transcriptional regulation; links to DDR and ciliopathy signaling | Nucleus; cilium-associated signaling nodes | Tubular epithelial cells | Transcriptional control; DNA damage response; fibrosis | (kalot2024primaryciliaand pages 10-11, ajiboye2023autosomalrecessiveadolescent pages 1-2) |
| TTC21B (IFT139) | IFT-A complex subunit required for retrograde intraflagellar transport and ciliary cargo trafficking | Intraflagellar transport (IFT); Hedgehog signaling | Axoneme; IFT complexes; transition zone | Ciliated epithelial cells; renal tubules | Intraflagellar transport; ciliary trafficking; signal transduction | (kalot2024primaryciliaand pages 10-11, clerici2025metabolicreprogrammingin pages 2-3) |
| EGFR axis | EGFR/RTK module influencing ciliary length, actin dynamics and fibrotic responses; targetable by EGFR inhibitors | EGFR/RTK → MAPK/PI3K; cross-talk with cAMP/mTOR | Plasma membrane; cilium-associated membrane domains | Tubular epithelial cells; interstitial fibroblasts | RTK signaling; ciliary length control; fibrosis modulation; therapeutic response | (sudhindar2025urinaryrenalepithelial pages 1-2, kalot2024primaryciliaand pages 10-11) |


*Table: Compact table mapping key NPHP genes/proteins to their roles, pathways, cellular locations, affected cell types and core processes, with supporting evidence from the provided contexts. This organizes mechanistic anchors for nephronophthisis useful for knowledge-base annotation and hypothesis generation.*

Key sources with URLs and publication dates
- Kalot RK et al. Primary cilia and actin regulatory pathways in renal ciliopathies. Frontiers in Nephrology. Published Jan 2024. URL: https://doi.org/10.3389/fneph.2023.1331847 (kalot2024primaryciliaand pages 10-11, kalot2024primaryciliaand pages 8-10).
- Leggatt GP et al. A Role for Genetic Modifiers in Tubulointerstitial Kidney Diseases. Genes. Published Aug 2023. URL: https://doi.org/10.3390/genes14081582 (tata2023eupatilinetagonistes pages 38-42).
- Sudhindar PD et al. Urinary renal epithelial cells can be used for NPHP1 phenotyping… Journal of Cell Science. Published Sep 2025 (online). URL: https://doi.org/10.1242/jcs.264141 (sudhindar2025urinaryrenalepithelial pages 1-2).
- Garví ES et al. Loss of nephronophthisis-associated nephrocystin-1 impairs DNA damage repair… bioRxiv. Posted Jun 2025. URL: https://doi.org/10.1101/2025.06.09.658557 (garvi2025lossofnephronophthisisassociated pages 1-3).
- Clerici S, Boletta A. Metabolic reprogramming in polycystic kidney disease and other renal ciliopathies. EMBO Molecular Medicine. Published Apr 2025. URL: https://doi.org/10.1038/s44321-025-00239-x (clerici2025metabolicreprogrammingin pages 2-3).
- Ajiboye O et al. Autosomal Recessive Adolescent Syndromic Nephronophthisis… Am J Case Rep. Published Oct 2023. URL: https://doi.org/10.12659/ajcr.941413 (ajiboye2023autosomalrecessiveadolescent pages 1-2).
- Roig J. NEK8… at the core of the ciliary INV complex. Cell Communication and Signaling. Published Apr 2025. URL: https://doi.org/10.1186/s12964-025-02143-w (roig2025nek8animafamily pages 1-2).

Limitations and open questions
- A proportion of statements rely on 2025 primary/translational sources due to scarcity of 2023–2024 mechanistic updates specific to NPHP1 DDR and EGFR modulation; nonetheless, core 2023–2024 reviews substantiate cilia–actin–Hippo and clinical progression aspects. NEK8 substrates and therapeutic targeting remain open. (kalot2024primaryciliaand pages 10-11, roig2025nek8animafamily pages 1-2, garvi2025lossofnephronophthisisassociated pages 1-3, sudhindar2025urinaryrenalepithelial pages 1-2).

References

1. (kalot2024primaryciliaand pages 10-11): Rita K. Kalot, Zachary T Sentell, Thomas M. Kitzler, and Elena Torban. Primary cilia and actin regulatory pathways in renal ciliopathies. Frontiers in Nephrology, Jan 2024. URL: https://doi.org/10.3389/fneph.2023.1331847, doi:10.3389/fneph.2023.1331847. This article has 10 citations and is from a poor quality or predatory journal.

2. (kalot2024primaryciliaand pages 8-10): Rita K. Kalot, Zachary T Sentell, Thomas M. Kitzler, and Elena Torban. Primary cilia and actin regulatory pathways in renal ciliopathies. Frontiers in Nephrology, Jan 2024. URL: https://doi.org/10.3389/fneph.2023.1331847, doi:10.3389/fneph.2023.1331847. This article has 10 citations and is from a poor quality or predatory journal.

3. (sudhindar2025urinaryrenalepithelial pages 1-2): Praveen Dhondurao Sudhindar, Eric Olinger, Zachary T. Sentell, Holly Mabillard, Barbora Dicka, Katrina Wood, Dominic Rutland, Catherine Collins, Marco Trevisan-Herraz, John A. Sayer, and Juliana E. Arcila-Galvis. Urinary renal epithelial cells can be used for <i>nphp1</i> phenotyping and a personalized therapeutic strategy. Journal of Cell Science, Sep 2025. URL: https://doi.org/10.1242/jcs.264141, doi:10.1242/jcs.264141. This article has 2 citations and is from a domain leading peer-reviewed journal.

4. (tata2023eupatilinetagonistes pages 38-42): A Tata. Eupatilin et agonistes des récepteurs des prostaglandines comme approches thérapeutiques de la néphronophtise juvénile: caractérisation de leurs effets sur la …. Unknown journal, 2023.

5. (garvi2025lossofnephronophthisisassociated pages 1-3): E. Sendino Garví, S. Biermans, N.V.A.M. Knoers, A.M. van Eerde, R. Masereeuw, G.G. Slaats, A.M. van Genderen, and M.J. Janssen. Loss of nephronophthisis-associated nephrocystin-1 impairs dna damage repair in kidney organoids. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.09.658557, doi:10.1101/2025.06.09.658557. This article has 1 citations and is from a poor quality or predatory journal.

6. (roig2025nek8animafamily pages 1-2): Joan Roig. Nek8, a nima-family protein kinase at the core of the ciliary inv complex. Cell Communication and Signaling : CCS, Apr 2025. URL: https://doi.org/10.1186/s12964-025-02143-w, doi:10.1186/s12964-025-02143-w. This article has 3 citations.

7. (clerici2025metabolicreprogrammingin pages 2-3): Sara Clerici and Alessandra Boletta. Metabolic reprogramming in polycystic kidney disease and other renal ciliopathies. EMBO Molecular Medicine, 17:1191-1202, Apr 2025. URL: https://doi.org/10.1038/s44321-025-00239-x, doi:10.1038/s44321-025-00239-x. This article has 1 citations and is from a highest quality peer-reviewed journal.

8. (ajiboye2023autosomalrecessiveadolescent pages 1-2): Oyintayo Ajiboye, Jaime E. Vengoechea, Ritu Gupta, and Koba Lomashvili. Autosomal recessive adolescent syndromic nephronophthisis caused by a novel compound heterozygous pathogenic variant. The American Journal of Case Reports, 24:e941413-1-e941413-5, Oct 2023. URL: https://doi.org/10.12659/ajcr.941413, doi:10.12659/ajcr.941413. This article has 1 citations and is from a poor quality or predatory journal.