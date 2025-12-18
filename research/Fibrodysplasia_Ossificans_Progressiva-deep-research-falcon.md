---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-16T19:12:23.956250'
end_time: '2025-12-16T19:18:28.929320'
duration_seconds: 364.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fibrodysplasia Ossificans Progressiva
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 16
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Fibrodysplasia Ossificans Progressiva
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Fibrodysplasia Ossificans Progressiva**.
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
- **Disease Name:** Fibrodysplasia Ossificans Progressiva
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Fibrodysplasia Ossificans Progressiva**.
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


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Fibrodysplasia Ossificans Progressiva (FOP)
- MONDO ID: (not confirmed here)
- Category: Genetic

Pathophysiology description
FOP is an ultra-rare genetic disorder in which gain-of-function mutations in ACVR1 (ALK2), most commonly p.R206H, dysregulate canonical BMP signaling and confer a pathogenic neofunction: Activin A becomes an agonist for mutant ACVR1, driving SMAD1/5/8 transcriptional programs that induce endochondral bone formation in soft tissues (heterotopic ossification, HO) (rivera2024cellularandmolecular pages 2-4, juan2024intersectionsoffibrodysplasia pages 4-5). The mutant receptor exhibits reduced FKBP12-mediated autoinhibition and heightened ligand responsiveness; competition between wild-type and mutant ACVR1 further modulates disease severity (gamberale2024…characterizationof pages 46-49, gamberale2024cellularandmolecular pages 46-49). Traumatic or inflammatory triggers initiate flare-ups in susceptible connective tissues (muscle, tendon, ligament) with a stereotyped lesion progression: a catabolic inflammatory phase (cell/tissue damage; infiltration by macrophages, mast cells, lymphocytes), followed by an anabolic fibroproliferative phase with angiogenesis, then chondrogenesis and endochondral ossification yielding mature ectopic bone (gamberale2024…characterizationof pages 39-42, gamberale2024…characterizationof pages 46-49, gamberale2024cellularandmolecular pages 46-49).

Multiple signaling axes amplify disease. Activin A produced by innate immune cells after soft-tissue injury aberrantly signals through ACVR1R206H to SMAD1/5/8, and type II receptors ACVR2A/ACVR2B influence oligomerization and activation of the mutant complex (gamberale2024…characterizationof pages 46-49, juan2024intersectionsoffibrodysplasia pages 4-5). Hypoxia/HIF-1α and mTOR signaling enhance early lesion chondrogenesis and BMP-pathway output; inhibition of these amplifiers reduces HO in preclinical models (rivera2024cellularandmolecular pages 2-4, gamberale2024cellularandmolecular pages 46-49). Tissue-resident mesenchymal progenitors—particularly fibro-adipogenic progenitors (FAPs)—are the dominant cellular origin of the chondro-osteogenic cascade, and the inflammatory microenvironment (macrophages, mast cells) is necessary for robust lesion expansion (rivera2024cellularandmolecular pages 2-4, diolintzi2024immunologicaspectsin pages 6-8, gamberale2024…characterizationof pages 39-42).

Direct quote (immune role): “Multiple lines of evidence indicate a key role for the immune system in driving FOP pathogenesis. Critical cell types include macrophages, mast cells, and adaptive immune cells” (Biomolecules, 2024-03; https://doi.org/10.3390/biom14030357) (diolintzi2024immunologicaspectsin pages 6-8).

1) Core pathophysiology
- Primary mechanisms: Mutant ACVR1/ALK2 hypersensitizes canonical BMP signaling and converts Activin A into a BMP-like agonist for SMAD1/5/8 activation, initiating endochondral ossification programs in soft tissues (rivera2024cellularandmolecular pages 2-4, juan2024intersectionsoffibrodysplasia pages 4-5). Hypoxia/HIF-1α and mTOR amplify signaling in early lesions (rivera2024cellularandmolecular pages 2-4, gamberale2024cellularandmolecular pages 46-49).
- Dysregulated pathways: BMP/SMAD1/5/8; Activin/TGF-β pathway re-routed via mutant ACVR1; hypoxia/HIF-1 and mTOR axes; noncanonical BMP signaling that augments osteo-chondrogenic transcription (rivera2024cellularandmolecular pages 2-4, gamberale2024…characterizationof pages 46-49).
- Affected cellular processes: inflammatory recruitment and cytokine signaling, fibroproliferation and matrix remodeling, chondrogenic differentiation, angiogenesis, endochondral ossification (gamberale2024…characterizationof pages 39-42, gamberale2024…characterizationof pages 46-49).

2) Key molecular players
- Genes/Proteins (HGNC): ACVR1/ALK2 (driver), ACVR2A/ACVR2B (type II partners), SMAD1/5/8, SMAD2/3, HIF1A, MTOR (gamberale2024…characterizationof pages 46-49, rivera2024cellularandmolecular pages 2-4, juan2024intersectionsoffibrodysplasia pages 4-5, gamberale2024cellularandmolecular pages 46-49).
- Ligands: Activin A/INHBA (obligate for HO in FOP models), selected BMPs; BMP9/GDF2 implicated in fibroproliferation/flare biology (gamberale2024…characterizationof pages 46-49, zhou2025advancementsinmechanisms pages 1-3).
- Cell types (CL): Fibro-adipogenic progenitors (FAPs; tissue-resident mesenchyme), macrophages, mast cells, endothelial cells (EndMT contributions), perivascular/adventitial fibroblasts (rivera2024cellularandmolecular pages 2-4, diolintzi2024immunologicaspectsin pages 6-8, gamberale2024…characterizationof pages 39-42, juan2024intersectionsoffibrodysplasia pages 4-5).
- Anatomical locations (UBERON): skeletal muscle, tendon, ligament as principal soft-tissue sites of HO initiation and progression (rivera2024cellularandmolecular pages 2-4, gamberale2024…characterizationof pages 39-42).

3) Biological processes (GO terms)
- Signaling pathways: BMP signaling via SMAD1/5/8; TGF-β/Activin signaling (re-wired via mutant ACVR1); response to hypoxia; mTOR signaling (rivera2024cellularandmolecular pages 2-4, gamberale2024cellularandmolecular pages 46-49, gamberale2024…characterizationof pages 46-49).
- Cellular programs: fibroproliferation, chondrogenesis, angiogenesis, endochondral ossification; immune cell activation and cytokine production (gamberale2024…characterizationof pages 39-42, diolintzi2024immunologicaspectsin pages 6-8).

4) Cellular components (GO-CC)
- Membrane and endosomes (mutant ACVR1 retention under hypoxia), extracellular matrix (ligand sequestration/availability and remodeling) (gamberale2024…characterizationof pages 46-49, gamberale2024…characterizationof pages 39-42).

5) Disease progression
- Sequence of events: trigger (minor trauma/inflammation) → catabolic phase (cell damage, macrophage/mast-cell/lymphocyte infiltration) → anabolic fibroproliferation with angiogenesis → chondrogenesis → endochondral ossification with mature, lamellar bone indistinguishable from the normal skeleton (gamberale2024…characterizationof pages 39-42, gamberale2024…characterizationof pages 46-49, gamberale2024cellularandmolecular pages 46-49). Hypoxia and mTOR activation peak early and amplify chondroprogenitor specification (rivera2024cellularandmolecular pages 2-4, gamberale2024cellularandmolecular pages 46-49).

6) Phenotypic manifestations
- Clinical phenotypes include congenital great-toe malformations; episodic painful flare-ups in soft tissues (muscle, tendon, ligaments) leading to progressive ankylosis, restricted mobility, and life-shortening thoracic insufficiency (gamberale2024…characterizationof pages 39-42, rivera2024cellularandmolecular pages 2-4). Inflammation can precipitate flares; immune cell depletion experiments indicate substantial reductions in HO when mast cells and macrophages are suppressed (approximately 50% with mast cell depletion; ~75% with combined depletion) (diolintzi2024immunologicaspectsin pages 6-8).

Recent developments and latest research (2023–2024 priority)
- Immunologic drivers and therapeutic targets: 2024 review synthesizes the central role of macrophages and mast cells, hypoxia, and inflammatory cytokines in FOP HO; emphasizes that “inflammation may be a common target” across FOP and non-genetic HO (Biomolecules, 2024-03; https://doi.org/10.3390/biom14030357) (diolintzi2024immunologicaspectsin pages 6-8).
- Cellular origins and signaling integration: 2024 review details aberrant ACVR1R206H signaling and identifies FAPs as dominant progenitors; discusses noncanonical pathway contributions (PI3K–AKT–mTOR, MAPKs) and clinical implications of targeting chondrogenesis (Biomedicines, 2024-04; https://doi.org/10.3390/biomedicines12040779) (rivera2024cellularandmolecular pages 2-4).
- Activin A neofunction and receptor complex dynamics: Evidence underscores ACVR2A/B roles in mutant ACVR1 activation and the obligate function of Activin A in mouse models; anti-Activin approaches remain compelling (gamberale2024…characterizationof pages 46-49, juan2024intersectionsoffibrodysplasia pages 4-5).
- Hypoxia and mTOR as amplifiers: Targeting HIF-1α/mTOR diminishes HO in genetic/acquired models, positioning these as disease amplifiers rather than sole initiators (Biomolecules, 2024-01; https://doi.org/10.3390/biom14020147) (rivera2024cellularandmolecular pages 2-4, gamberale2024cellularandmolecular pages 46-49).

Current applications and real-world implementations
- Retinoid pathway (RARγ agonism): Palovarotene is used to reduce new HO formation; trial and natural history learnings inform imaging endpoints and functional timelines (BMC Med Res Methodol, 2023-11; https://doi.org/10.1186/s12874-023-02080-7). Mechanistically, retinoids suppress chondrogenesis in lesions; preclinical data demonstrate reduction of local Activin A–expressing cell populations during HO (JBMR Plus, 2023-10; https://doi.org/10.1002/jbm4.10821) (rivera2024cellularandmolecular pages 2-4, gamberale2024…characterizationof pages 46-49).
- Activin A neutralization: Anti-Activin A strategies effectively prevent de novo HO in R206H mouse models; clinical interest persists given the obligate role of Activin A in FOP mouse HO (juan2024intersectionsoffibrodysplasia pages 4-5, gamberale2024…characterizationof pages 46-49).
- ALK2 kinase inhibition and pathway modulators: Saracatinib (AZD0530) and related ALK2-targeted strategies are under evaluation; mTOR inhibitors (e.g., rapamycin) and other pathway dampeners reduce HO in preclinical settings (Journal of Zhejiang University Sci B, 2025-03; https://doi.org/10.1631/jzus.b2300779) (zhou2025advancementsinmechanisms pages 1-3, gamberale2024cellularandmolecular pages 46-49).

Expert opinions and analysis
- “Multiple lines of evidence indicate a key role for the immune system in driving FOP pathogenesis” and suggest immune modulators as adjunctive therapeutic strategies (Biomolecules, 2024-03) (diolintzi2024immunologicaspectsin pages 6-8).
- Reviews emphasize FAPs as principal HO progenitors under mutant ACVR1 signaling and support targeting chondrogenesis and early inflammatory amplification to attenuate lesion formation (Biomedicines, 2024-04) (rivera2024cellularandmolecular pages 2-4).

Relevant statistics and data
- Epidemiology and natural history: FOP prevalence ≈ 1 in 2,000,000; onset early childhood; flare-ups often triggered by minor trauma or infection; the dorsal/axial-to-distal pattern and progressive ankylosis are characteristic (gamberale2024…characterizationof pages 39-42).
- Immune modulation effects (preclinical): Mast cell depletion reduces HO by ~50%; combined mast cell/macrophage depletion with clodronate reduces HO by ~75% (diolintzi2024immunologicaspectsin pages 6-8).

Gene/protein annotations with ontology terms
- HGNC: ACVR1 (ALK2); ACVR2A; ACVR2B; SMAD1; SMAD5; SMAD9 (SMAD8); SMAD2; SMAD3; HIF1A; MTOR; INHBA (Activin A); GDF2 (BMP9) (gamberale2024…characterizationof pages 46-49, rivera2024cellularandmolecular pages 2-4, zhou2025advancementsinmechanisms pages 1-3).
- GO Biological Process: BMP signaling via SMAD1/5/8; TGF-β/Activin signaling; response to hypoxia; mTOR signaling; chondrogenesis; angiogenesis; endochondral ossification; inflammatory response (rivera2024cellularandmolecular pages 2-4, gamberale2024…characterizationof pages 39-42, gamberale2024cellularandmolecular pages 46-49).
- GO Cellular Component: endosome; extracellular matrix (gamberale2024…characterizationof pages 46-49, gamberale2024…characterizationof pages 39-42).

Phenotype associations (HP terms)
- HP: congenital hallux valgus/malformed great toes; episodic painful soft-tissue swellings (flares); progressive ankylosis; thoracic insufficiency (gamberale2024…characterizationof pages 39-42, rivera2024cellularandmolecular pages 2-4).

Cell type involvement (CL terms)
- CL: fibro-adipogenic progenitor; macrophage; mast cell; endothelial cell (EndMT contribution); perivascular/adventitial fibroblast (rivera2024cellularandmolecular pages 2-4, diolintzi2024immunologicaspectsin pages 6-8, gamberale2024…characterizationof pages 39-42, juan2024intersectionsoffibrodysplasia pages 4-5).

Anatomical locations (UBERON terms)
- UBERON: skeletal muscle; tendon; ligament (rivera2024cellularandmolecular pages 2-4, gamberale2024…characterizationof pages 39-42).

Chemical entities (CHEBI terms)
- CHEBI: palovarotene (RARγ agonist); garetosmab (anti–Activin A monoclonal antibody); saracatinib (kinase inhibitor); sirolimus/rapamycin (mTOR inhibitor) (rivera2024cellularandmolecular pages 2-4, zhou2025advancementsinmechanisms pages 1-3, gamberale2024cellularandmolecular pages 46-49).

Evidence items with PMIDs/DOIs/URLs and dates
- Rivera LM, Shore EM, Mourkioti F. Biomedicines. 2024-04. DOI: 10.3390/biomedicines12040779; URL: https://doi.org/10.3390/biomedicines12040779 (rivera2024cellularandmolecular pages 2-4).
- Diolintzi A, Pervin MS, Hsiao EC. Biomolecules. 2024-03. DOI: 10.3390/biom14030357; URL: https://doi.org/10.3390/biom14030357 (diolintzi2024immunologicaspectsin pages 6-8).
- Juan C et al. Biomolecules. 2024-03. DOI: 10.3390/biom14030349; URL: https://doi.org/10.3390/biom14030349 (juan2024intersectionsoffibrodysplasia pages 4-5).
- Wang H, Kaplan FS, Pignolo RJ. Biomolecules. 2024-01. DOI: 10.3390/biom14020147; URL: https://doi.org/10.3390/biom14020147 (rivera2024cellularandmolecular pages 2-4, gamberale2024cellularandmolecular pages 46-49).
- Gamberale R. 2024. Cellular/molecular characterization of macrophages at HO onset in FOP model (source text excerpt). (gamberale2024…characterizationof pages 46-49, gamberale2024…characterizationofa pages 46-49, gamberale2024cellularandmolecular pages 46-49, gamberale2024…characterizationof pages 39-42).
- Zhou Y, Shi C, Sun H. J Zhejiang Univ Sci B. 2025-03. DOI: 10.1631/jzus.b2300779; URL: https://doi.org/10.1631/jzus.b2300779 (zhou2025advancementsinmechanisms pages 1-3).

Ontology summary table
| Category | Term (preferred ontology label) | Ontology | Role in FOP (1–2 lines) | Representative Evidence |
|---|---|---|---|---|
| Gene | ACVR1 (Activin A receptor type I / ALK2) | HGNC: ACVR1 | Gain-of-function mutations (eg. R206H) confer Activin A responsiveness and hyperactivate SMAD1/5/8, driving chondrogenesis and HO. | Gamberale 2024; Rivera 2024 (gamberale2024…characterizationof pages 46-49, rivera2024cellularandmolecular pages 2-4) |
| Gene | ACVR2A (Activin receptor type-2A) | HGNC: ACVR2A | Type II receptor partnering with ACVR1; ligand/receptor oligomerization influences mutant ALK2 activation. | Juan 2024; Gamberale 2024 (juan2024intersectionsoffibrodysplasia pages 4-5, gamberale2024…characterizationof pages 46-49) |
| Gene | ACVR2B (Activin receptor type-2B) | HGNC: ACVR2B | Forms homomers/heteromers that can promote ligand-independent clustering and activation of ALK2R206H. | Szilágyi 2024 summary (gamberale2024…characterizationof pages 46-49) |
| Protein / Ligand | Activin A / INHBA | HGNC: INHBA | Neofunctional agonist for mutant ACVR1; produced by innate immune cells after tissue damage and required for HO in models. | Gamberale 2024; Diolintzi 2024 (gamberale2024…characterizationof pages 46-49, diolintzi2024immunologicaspectsin pages 6-8) |
| Gene | BMP9 / GDF2 | HGNC: GDF2 | BMP family ligand implicated in fibroproliferation and flare initiation via TGF-β/SMAD cross-talk in FOP models. | Zhou 2025 summary (zhou2025advancementsinmechanisms pages 1-3) |
| Protein complex | SMAD1/5/8 (canonical BMP SMADs) | HGNC group | Primary transcriptional mediators of mutant ACVR1-driven osteo/chondrogenic gene programs (SOX9, RUNX2). | Gamberale 2024; Rivera 2024 (gamberale2024…characterizationof pages 46-49, rivera2024cellularandmolecular pages 2-4) |
| Protein complex | SMAD2/3 (TGF-β/Activin SMADs) | HGNC group | Normally downstream of Activin/TGF-β; Activin A engagement of mutant ACVR1 shifts signaling toward SMAD1/5/8 in FOP. | Gamberale 2024; Juan 2024 (gamberale2024…characterizationof pages 46-49, juan2024intersectionsoffibrodysplasia pages 4-5) |
| Transcription factor | HIF‑1α (HIF1A) | HGNC: HIF1A | Hypoxia amplifier in early lesions; promotes retention/amplification of ACVR1 signaling and chondrogenesis. | Gamberale 2024; Rivera 2024 (gamberale2024…characterizationof pages 39-42, rivera2024cellularandmolecular pages 2-4) |
| Kinase pathway | mTOR (mechanistic target of rapamycin) | HGNC: MTOR | mTOR pathway amplifies HO; mTOR inhibition (rapamycin) reduces lesion formation in models. | Gamberale 2024; Rivera 2024 (gamberale2024cellularandmolecular pages 46-49, rivera2024cellularandmolecular pages 2-4) |
| Protease | MMP‑9 (Matrix metalloproteinase‑9) | HGNC: MMP9 | Links inflammation to HO via ECM remodeling and Activin A bioavailability; inhibition confers resilience in models (therapeutic target). | (see model summaries) Gamberale 2024 (gamberale2024…characterizationof pages 46-49) |
| Drug | Palovarotene (RARγ agonist) | CHEBI: palovarotene | Reduces new HO formation (clinical program); modulates chondrogenic cell populations and retinoid-mediated suppression of cartilage differentiation. | Rivera 2024; Zhou 2025 (rivera2024cellularandmolecular pages 2-4, zhou2025advancementsinmechanisms pages 1-3) |
| Drug (biologic) | Garetosmab (anti‑Activin A mAb) | CHEBI: monoclonal antibody (Activin A) | Neutralizes Activin A to prevent new lesion formation in trials; blocked de novo HO in models and clinical phase 2 signals for prevention. | Juan 2024; Diolintzi 2024 (juan2024intersectionsoffibrodysplasia pages 4-5, diolintzi2024immunologicaspectsin pages 6-8) |
| Drug | Saracatinib (AZD0530; ALK2/SRC inhibitor) | CHEBI: saracatinib | Repurposed kinase inhibitor targeting ALK2 activity; under clinical evaluation (STOPFOP) to limit HO. | Zhou 2025; Smilde protocol cited (zhou2025advancementsinmechanisms pages 1-3) |
| Drug | Rapamycin / Sirolimus (mTOR inhibitor) | CHEBI: rapamycin | Inhibits mTOR/HIF amplification of HO and reduces chondrogenesis in models; candidate therapy in trials/preclinical work. | Gamberale 2024; Rivera 2024 (gamberale2024cellularandmolecular pages 46-49, rivera2024cellularandmolecular pages 2-4) |
| Cell type | Fibro‑adipogenic progenitor (FAP) | CL: fibro‑adipogenic progenitor | Tissue‑resident mesenchymal progenitor that aberrantly adopts chondro‑osteogenic fate under mutant ACVR1 signaling and forms HO. | Rivera 2024; Gamberale 2024 (rivera2024cellularandmolecular pages 2-4, gamberale2024…characterizationof pages 46-49) |
| Cell type | Macrophage (innate immune) | CL: macrophage | Key initiators of inflammation and source of Activin A; depletion reduces HO in models (major contributor to flare phase). | Gamberale 2024; Diolintzi 2024 (gamberale2024…characterizationof pages 39-42, diolintzi2024immunologicaspectsin pages 6-8) |
| Cell type | Mast cell | CL: mast cell | Contribute to inflammatory amplification during flares; mast cell depletion reduces HO in preclinical studies. | Diolintzi 2024 (diolintzi2024immunologicaspectsin pages 6-8) |
| Cell type / process | Endothelial cell (EndMT context) | CL: endothelial cell | Endothelial-to-mesenchymal transition contributes progenitors/mesenchymal cells that can adopt osteogenic programs in HO contexts. | Juan 2024; Gamberale 2024 (juan2024intersectionsoffibrodysplasia pages 4-5, gamberale2024…characterizationof pages 46-49) |
| Cell type | Perivascular cell / Adventitial fibroblast | CL: adventitial fibroblast / perivascular cell | Perivascular niche harbors osteo‑progenitors and immune cells that create a permissive microenvironment for HO. | Xu/overview cited in summaries; Gamberale 2024 (gamberale2024…characterizationof pages 39-42, gamberale2024…characterizationof pages 46-49) |
| Anatomy | Skeletal muscle | UBERON: skeletal muscle | Primary soft‑tissue site of flare‑triggered HO in FOP; damaged muscle undergoes fibroproliferation then endochondral ossification. | Gamberale 2024; Rivera 2024 (gamberale2024…characterizationof pages 39-42, rivera2024cellularandmolecular pages 2-4) |
| Anatomy | Tendon | UBERON: tendon | Common anatomical substrate for ectopic bone deposition in FOP (tendon involvement typical). | Rivera 2024 (rivera2024cellularandmolecular pages 2-4) |
| Anatomy | Ligament | UBERON: ligament | Frequently affected connective tissue in progressive HO and ankylosis. | Rivera 2024 (rivera2024cellularandmolecular pages 2-4) |
| Cellular component | Extracellular matrix (ECM) | GO: CC extracellular matrix | ECM remodeling concentrates ligands (eg. Activin A) and modulates progenitor differentiation during lesion progression. | Gamberale 2024 (gamberale2024…characterizationof pages 46-49) |
| Cellular component | Endosome | GO: CC endosome | Endosomal retention of ACVR1 under hypoxia/ligand conditions amplifies signaling driving chondrogenesis. | Gamberale 2024 (gamberale2024…characterizationof pages 46-49) |
| Biological process | SMAD‑dependent BMP signaling | GO: BP BMP signaling via SMAD1/5/8 | Central pathway driving osteo/chondrogenic transcriptional programs in mutant ACVR1-expressing cells. | Gamberale 2024; Rivera 2024 (gamberale2024…characterizationof pages 46-49, rivera2024cellularandmolecular pages 2-4) |
| Biological process | TGF‑β / Activin signaling | GO: BP TGF‑β signaling | Activin/TGF‑β axis intersects with mutant ACVR1, enabling Activin A to hijack BMP-like SMAD1/5/8 signaling in FOP. | Gamberale 2024; Diolintzi 2024 (gamberale2024…characterizationof pages 46-49, diolintzi2024immunologicaspectsin pages 6-8) |
| Biological process | Chondrogenesis | GO: BP chondrogenesis | Transitional program in HO: fibroproliferative tissue differentiates to cartilage prior to endochondral ossification. | Rivera 2024; Mundy 2023 summaries (rivera2024cellularandmolecular pages 2-4, gamberale2024…characterizationof pages 46-49) |
| Biological process | Endochondral ossification | GO: BP endochondral ossification | Final conserved bone‑forming program that produces mature ectopic bone via cartilage template. | Rivera 2024 (rivera2024cellularandmolecular pages 2-4) |
| Biological process | Angiogenesis | GO: BP angiogenesis | Required during anabolic lesion phase; supports progenitor survival and endochondral progression. | Gamberale 2024; Juan 2024 (gamberale2024…characterizationof pages 46-49, juan2024intersectionsoffibrodysplasia pages 4-5) |
| Biological process | Hypoxia response | GO: BP response to hypoxia | Hypoxia/HIF‑1α amplify BMP/ACVR1 signaling and foster chondrogenic differentiation in early lesions. | Gamberale 2024; Rivera 2024 (gamberale2024…characterizationof pages 39-42, rivera2024cellularandmolecular pages 2-4) |


*Table: Compact ontology-aligned map linking genes, proteins, cells, anatomical sites, cellular components, and biological processes in FOP with concise roles and representative evidence (selected recent reviews and studies). This table is useful for ontology annotation, knowledge‑base curation, or quick reference for mechanisms and therapeutic nodes.*

Notes on limitations and open questions
- While Activin A is obligate for HO in several FOP mouse models, serum Activin A may not reliably track human flare activity; locus-specific ligand/cytokine dynamics and microenvironmental availability likely dominate early lesion biology (consistent with immunologic and hypoxia amplification) (diolintzi2024immunologicaspectsin pages 6-8, rivera2024cellularandmolecular pages 2-4). Further human longitudinal biomarker studies are needed.

References are indicated inline with citations and include URLs and publication dates when available. All mechanistic assertions are supported by the cited sources.

References

1. (rivera2024cellularandmolecular pages 2-4): Loreilys Mejias Rivera, Eileen M. Shore, and Foteini Mourkioti. Cellular and molecular mechanisms of heterotopic ossification in fibrodysplasia ossificans progressiva. Biomedicines, 12:779, Apr 2024. URL: https://doi.org/10.3390/biomedicines12040779, doi:10.3390/biomedicines12040779. This article has 14 citations and is from a poor quality or predatory journal.

2. (juan2024intersectionsoffibrodysplasia pages 4-5): Conan Juan, Alec C. Bancroft, Ji Hae Choi, Johanna H. Nunez, Chase A. Pagani, Yen-Sheng Lin, Edward C. Hsiao, and Benjamin Levi. Intersections of fibrodysplasia ossificans progressiva and traumatic heterotopic ossification. Biomolecules, 14:349, Mar 2024. URL: https://doi.org/10.3390/biom14030349, doi:10.3390/biom14030349. This article has 11 citations and is from a poor quality or predatory journal.

3. (gamberale2024…characterizationof pages 46-49): R Gamberale. … characterization of the infiltrating polarized macrophages during the onset of heterotopic ossification in a mouse model of fibrodysplasia ossificans progressiva (fop …. Unknown journal, 2024.

4. (gamberale2024cellularandmolecular pages 46-49): R Gamberale. Cellular and molecular characterization of the infiltrating polarized macrophages during the onset of heterotopic ossification in a mouse model of fibrodysplasia …. Unknown journal, 2024.

5. (gamberale2024…characterizationof pages 39-42): R Gamberale. … characterization of the infiltrating polarized macrophages during the onset of heterotopic ossification in a mouse model of fibrodysplasia ossificans progressiva (fop …. Unknown journal, 2024.

6. (diolintzi2024immunologicaspectsin pages 6-8): Anastasia Diolintzi, Mst Shaela Pervin, and Edward C. Hsiao. Immunologic aspects in fibrodysplasia ossificans progressiva. Biomolecules, 14:357, Mar 2024. URL: https://doi.org/10.3390/biom14030357, doi:10.3390/biom14030357. This article has 11 citations and is from a poor quality or predatory journal.

7. (zhou2025advancementsinmechanisms pages 1-3): Yijun Zhou, Ce Shi, and Hongchen Sun. Advancements in mechanisms and drug treatments for fibrodysplasia ossificans progressiva. Journal of Zhejiang University. Science. B, 26 4:317-332, Mar 2025. URL: https://doi.org/10.1631/jzus.b2300779, doi:10.1631/jzus.b2300779. This article has 0 citations.

8. (gamberale2024…characterizationofa pages 46-49): R Gamberale. … characterization of the infiltrating polarized macrophages during the onset of heterotopic ossification in a mouse model of fibrodysplasia ossificans progressiva (fop …. Unknown journal, 2024.