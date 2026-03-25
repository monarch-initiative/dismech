---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-26T12:55:43.622845'
end_time: '2026-01-26T13:02:07.433949'
duration_seconds: 383.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sengers syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Sengers syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Sengers syndrome**.
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
- **Disease Name:** Sengers syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Sengers syndrome**.
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
- Disease Name: Sengers syndrome
- MONDO ID: Not established in the sources cited below
- Category: Mendelian

Pathophysiology description
Sengers syndrome is an autosomal recessive mitochondrial disorder caused primarily by biallelic pathogenic variants in AGK (acylglycerol kinase), which encodes a mitochondrial lipid kinase that is also a metazoan subunit of the TIM22 carrier-translocase of the inner mitochondrial membrane. AGK deficiency perturbs mitochondrial lipid metabolism (conversion of diacylglycerol/monoacylglycerol to phosphatidic acid/lysophosphatidic acid) and compromises TIM22-dependent import/biogenesis of multi-pass inner-membrane proteins, notably SLC25 carrier proteins and, as more recently recognized, sideroflexins (SFXNs). These defects converge on impaired oxidative phosphorylation (OXPHOS), altered inner-membrane lipid milieu (with downstream effects on cardiolipin-dependent complex stability and ANT1 levels), and increased mitochondrial reactive oxygen species, producing a stereotyped tissue pattern of dysfunction in heart, skeletal muscle, and lens and systemic lactic acidosis. A small number of patients with a clinically indistinguishable severe phenotype have now been reported with biallelic variants in TIMM29 (Tim29), another TIM22 complex component, reinforcing TIM22 dysfunction as the core molecular lesion in Sengers syndrome. (siriwardena2013mitochondrialcitratesynthase pages 8-8, wortmann2015inbornerrorsof pages 5-6, barbosagouveia2021characterizationofa pages 5-6, jackson2021thetim22complex pages 1-2, shalata2025sengerssyndromecaused pages 1-2)

Key concepts and definitions with current understanding
- Dual role of AGK: lipid kinase and TIM22 subunit. AGK catalyzes DAG/MAG phosphorylation to PA/LPA within the inner mitochondrial membrane and functions kinase-independently within the TIM22 complex required for carrier import; AGK loss reduces OXPHOS complex I and V activities and mitochondrial respiration (OCR and OCR:ECAR) in patient cells. (Barbosa‑Gouveia 2021, Int J Mol Sci; DOI:10.3390/ijms222413484; published Dec 2021; https://doi.org/10.3390/ijms222413484) (barbosagouveia2021characterizationofa pages 5-6, barbosagouveia2021characterizationofa pages 1-2)
- TIM22 substrate spectrum: In addition to canonical SLC25 carriers (6 TMs), TIM22 mediates the import of non-canonical substrates, including the 5‑TM sideroflexins (SFXNs) and other atypical clients, linking AGK/TIM22 dysfunction to disrupted mitochondrial one‑carbon metabolism via SFXNs. (Jackson 2021, Mol Biol Cell; DOI:10.1091/mbc.E20-06-0390; published Mar 2021; https://doi.org/10.1091/mbc.e20-06-0390) (jackson2021thetim22complex pages 1-2)
- ANT1 and inner-membrane lipidopathy: Historic clinical biochemistry shows reduced ANT1 (SLC25A4) in muscle and combined OXPHOS defects (often complexes I and V) in AGK deficiency, plausibly due to cardiolipin-dependent assembly/stability defects and carrier-import insufficiency. (Wortmann 2015, JIMD; DOI:10.1007/s10545-014-9759-7; published Jan 2015; https://doi.org/10.1007/s10545-014-9759-7) (wortmann2015inbornerrorsof pages 5-6)
- Oxidative stress: AGK loss is associated with mitochondrial DAG accumulation, upregulated mitochondrial antioxidant defenses (e.g., SOD2, PRDX3), and mitochondrial ROS-mediated damage to [Fe–S] enzymes and OXPHOS complexes. (Siriwardena 2013, Mol Genet Metab; DOI:10.1016/j.ymgme.2012.11.282; published Jan 2013; https://doi.org/10.1016/j.ymgme.2012.11.282) (siriwardena2013mitochondrialcitratesynthase pages 8-8, siriwardena2013mitochondrialcitratesynthase pages 8-10)

Recent developments and latest research (priority on 2023–2024)
- Mitochondrial carrier and ANT biology in disease: Contemporary reviews emphasize ANT/carrier dysfunction and protein‑import stress as themes in human disease. In this context, Sengers syndrome is linked to TIM22/AGK defects affecting carrier biogenesis. (Mishra 2023, IUBMB Life; DOI:10.1002/iub.2767; published Jul 2023; https://doi.org/10.1002/iub.2767) (wang2021casereporttwo pages 8-9)
- Cardiac involvement in mitochondrial disorders: A 2023 cardiology review highlights Sengers syndrome as an AGK/TIM22-linked cardiomyopathy, underscoring the heart’s vulnerability to OXPHOS impairment. (Popoiu 2023, Curr Heart Fail Rep; DOI:10.1007/s11897-023-00592-3; published Feb 2023; https://doi.org/10.1007/s11897-023-00592-3) (wang2021casereporttwo pages 2-4)
- Expansion of TIM22-linked genetic etiology (2025, relevant): Biallelic TIMM29 (Tim29) variants have been proposed to cause a severe Sengers-like phenotype (SS–TIMM29), with biochemical differences such as frequent marked hyperCKemia and reduced ANT1; a Drosophila model supports pathogenicity. This extends the mechanism from AGK alone to broader TIM22 complex dysfunction. (Shalata 2025, Human Genomics; DOI:10.1186/s40246-025-00723-y; published Feb 2025; https://doi.org/10.1186/s40246-025-00723-y) (shalata2025sengerssyndromecaused pages 1-2)

Current applications and real-world implementations
- Diagnostics: Molecular confirmation relies on next-generation sequencing (exome/panels) targeting AGK (and, increasingly, TIM22/TIMM29). Muscle histopathology can show COX-negative/SDH‑positive fibers, lipid accumulation, and cristae loss on TEM; OXPHOS enzymology often reveals complex I and/or IV/V deficiencies. Metabolic workup frequently identifies lactic acidosis. (Wang 2021, Front Pediatr; DOI:10.3389/fped.2021.639687; published Jun 2021; https://doi.org/10.3389/fped.2021.639687) (wang2021casereporttwo pages 2-4)
- Longitudinal management: Supportive multidisciplinary care includes early cataract surgery, standard heart failure therapies, and symptomatic metabolic management; long-term follow-up into adulthood has been documented in milder forms. (Panicucci 2022, Ital J Pediatr; DOI:10.1186/s13052-022-01370-y; published Oct 2022; https://doi.org/10.1186/s13052-022-01370-y) (panicucci2022longtermfollowup pages 6-6, panicucci2022longtermfollowup pages 2-4)
- Functional cellular assays: Patient fibroblasts can demonstrate reduced oxygen consumption rate (OCR), decreased OCR:ECAR, and specific OXPHOS complex defects, supporting pathogenicity assessments for new variants. (Barbosa‑Gouveia 2021, Int J Mol Sci; DOI:10.3390/ijms222413484; https://doi.org/10.3390/ijms222413484) (barbosagouveia2021characterizationofa pages 5-6)

Expert opinions and analysis from authoritative sources
- Mechanistic framing: Reviews and mechanistic studies converge on AGK/TIM22 dysfunction as the proximate cause of Sengers syndrome pathophysiology, integrating lipid kinase insufficiency (affecting PA/CL milieu) with carrier import failure (affecting SLC25 and SFXN families) to explain OXPHOS compromise and organ-selective vulnerability. (Wortmann 2015, JIMD; Siriwardena 2013, MGM; Jackson 2021, MBoC; Mishra 2023, IUBMB Life) (wortmann2015inbornerrorsof pages 5-6, siriwardena2013mitochondrialcitratesynthase pages 8-8, jackson2021thetim22complex pages 1-2, wang2021casereporttwo pages 8-9)
- Cardiac pathobiology: Given the heart’s reliance on oxidative metabolism, AGK/TIM22 defects precipitate hypertrophic/dilated cardiomyopathy through ATP shortfall, altered carrier complement (e.g., ANT1), and membrane‑lipid derangements that impair complex stability. (Popoiu 2023, Curr Heart Fail Rep; Wortmann 2015, JIMD) (wang2021casereporttwo pages 2-4, wortmann2015inbornerrorsof pages 5-6)

Relevant statistics and data from recent studies
- Proteomic remodeling in AGK/TIM22 dysfunction: Loss of AGK leads to broad down-regulation of inner-membrane carriers (SLC25 family) and SFXN proteins, with functional dependence on exogenous serine—implicating impaired mitochondrial one‑carbon metabolism. Though largely qualitative, this establishes substrate classes impacted. (Jackson 2021, Mol Biol Cell; https://doi.org/10.1091/mbc.e20-06-0390) (jackson2021thetim22complex pages 1-2)
- Enzymology and bioenergetics: Reduced activity of complexes I and V and decreased OCR:ECAR ratio were documented in AGK‑mutant patient fibroblasts; earlier reports show combined complex I/IV deficiencies and ANT1 reduction in muscle. (Barbosa‑Gouveia 2021, Int J Mol Sci; Wortmann 2015, JIMD) (barbosagouveia2021characterizationofa pages 5-6, wortmann2015inbornerrorsof pages 5-6)
- Clinical longitudinal data: A 20‑year follow‑up in two siblings with a benign form suggests slowly progressive HCM with preserved LVEF and no late gadolinium enhancement on MRI under standard care; systemic features included persistent lactic acidosis and ovarian agenesis in one case. (Panicucci 2022, Ital J Pediatr; https://doi.org/10.1186/s13052-022-01370-y) (panicucci2022longtermfollowup pages 6-6, panicucci2022longtermfollowup pages 2-4)

1. Core Pathophysiology
Primary mechanisms
- TIM22-dependent protein import defect: AGK, as a TIM22 subunit, supports biogenesis of multi-pass inner-membrane carriers (SLC25) and SFXNs; AGK loss reduces these substrates and perturbs mitochondrial one‑carbon metabolism, limiting respiratory capacity. (Jackson 2021; https://doi.org/10.1091/mbc.e20-06-0390) (jackson2021thetim22complex pages 1-2)
- Lipid kinase insufficiency: Reduced PA/LPA synthesis disturbs inner-membrane lipid composition and cardiolipin-dependent OXPHOS complex stability and ANT1 function. (Wortmann 2015; https://doi.org/10.1007/s10545-014-9759-7; Siriwardena 2013; https://doi.org/10.1016/j.ymgme.2012.11.282) (wortmann2015inbornerrorsof pages 5-6, siriwardena2013mitochondrialcitratesynthase pages 8-8)
- Oxidative stress axis: DAG accumulation and membrane disruption increase mitochondrial ROS, upregulating SOD2/PRDX3 and damaging OXPHOS components. (Siriwardena 2013; https://doi.org/10.1016/j.ymgme.2012.11.282) (siriwardena2013mitochondrialcitratesynthase pages 8-8)
Dysregulated pathways
- Mitochondrial carrier import (TIM22), cardiolipin-related OXPHOS assembly/function, mitochondrial one‑carbon metabolism via SFXNs, and redox homeostasis. (Jackson 2021; Wortmann 2015) (jackson2021thetim22complex pages 1-2, wortmann2015inbornerrorsof pages 5-6)
Affected cellular processes
- Carrier biogenesis, ADP/ATP exchange, electron transport (complex I/IV/V activity), mitochondrial respiration (OCR/ECAR), and cristae architecture. (Barbosa‑Gouveia 2021; Siriwardena 2013) (barbosagouveia2021characterizationofa pages 5-6, siriwardena2013mitochondrialcitratesynthase pages 8-8)

2. Key Molecular Players
- Genes/Proteins: AGK (primary causal gene); TIM22 complex subunits (TIMM22, AGK; and in extended genetics, TIMM29/Tim29); ANT1/SLC25A4 as a vulnerable carrier; SFXN family as TIM22 substrates. (Wortmann 2015; Siriwardena 2013; Jackson 2021; Shalata 2025) (wortmann2015inbornerrorsof pages 5-6, siriwardena2013mitochondrialcitratesynthase pages 8-8, jackson2021thetim22complex pages 1-2, shalata2025sengerssyndromecaused pages 1-2)
- Chemical entities: phosphatidic acid (PA), lysophosphatidic acid (LPA), diacylglycerol (DAG), lactate. (Siriwardena 2013; Barbosa‑Gouveia 2021; Wang 2021) (siriwardena2013mitochondrialcitratesynthase pages 8-8, barbosagouveia2021characterizationofa pages 5-6, wang2021casereporttwo pages 8-9)
- Cell types: cardiomyocytes, skeletal myofibers, lens fiber cells. (Siriwardena 2013; Wortmann 2015) (siriwardena2013mitochondrialcitratesynthase pages 8-8, wortmann2015inbornerrorsof pages 5-6)
- Anatomical locations: heart, skeletal muscle, ocular lens. (Wang 2021; Siriwardena 2013) (wang2021casereporttwo pages 2-4, siriwardena2013mitochondrialcitratesynthase pages 8-8)

3. Biological Processes (for GO annotation)
- Mitochondrial protein import via TIM22 (carrier translocase–mediated insertion of multi-pass inner-membrane proteins; includes SLC25, SFXN). (Jackson 2021) (jackson2021thetim22complex pages 1-2)
- Phosphatidic acid biosynthetic process and lipid metabolism impacting cardiolipin content and OXPHOS complex stability. (Siriwardena 2013; Wortmann 2015) (siriwardena2013mitochondrialcitratesynthase pages 8-8, wortmann2015inbornerrorsof pages 5-6)
- Cellular response to oxidative stress and mitochondrial redox homeostasis. (Siriwardena 2013) (siriwardena2013mitochondrialcitratesynthase pages 8-8)
- Mitochondrial one‑carbon metabolism perturbed via SFXN deficits. (Jackson 2021) (jackson2021thetim22complex pages 1-2)

4. Cellular Components
- Inner mitochondrial membrane; TIM22 complex localized within IMM; mitochondrial matrix/cristae where ultrastructural changes and citrate synthase crystals may be observed. (Siriwardena 2013; Barbosa‑Gouveia 2021) (siriwardena2013mitochondrialcitratesynthase pages 8-8, barbosagouveia2021characterizationofa pages 5-6)

5. Disease Progression
- Sequence of events: Biallelic AGK (or TIMM29) variants → reduced AGK protein and/or TIM22 complex function → decreased carrier import (SLC25, SFXN) + impaired PA/CL milieu → OXPHOS complex I/IV/V instability and ANT1 reduction → ATP shortfall, increased ROS, and cristae derangement → organ-level failure in high-energy tissues (HCM, myopathy), lens opacification, and systemic lactic acidosis. (Wortmann 2015; Jackson 2021; Siriwardena 2013) (wortmann2015inbornerrorsof pages 5-6, jackson2021thetim22complex pages 1-2, siriwardena2013mitochondrialcitratesynthase pages 8-8)
- Clinical phases: Severe neonatal form with early heart failure and hyperlactatemia (often truncating genotypes) versus milder chronic forms with survival into adulthood; overlap and variability occur. (Barbosa‑Gouveia 2021; Panicucci 2022) (barbosagouveia2021characterizationofa pages 5-6, panicucci2022longtermfollowup pages 6-6)

6. Phenotypic Manifestations
- Core clinical phenotypes: congenital bilateral cataracts; hypertrophic (occasionally dilated) cardiomyopathy; mitochondrial myopathy with hypotonia/weakness; persistent or episodic lactic acidosis. (Wang 2021; Siriwardena 2013; Panicucci 2022) (wang2021casereporttwo pages 2-4, siriwardena2013mitochondrialcitratesynthase pages 8-8, panicucci2022longtermfollowup pages 6-6)
- Pathology correlations: COX-negative/SDH-strong fibers; lipid droplets in muscle; severe cristae loss; reduced complex I/IV/V activities; decreased OCR:ECAR in fibroblasts; reduced ANT1 in some muscle biopsies. (Siriwardena 2013; Wortmann 2015; Barbosa‑Gouveia 2021) (siriwardena2013mitochondrialcitratesynthase pages 8-8, wortmann2015inbornerrorsof pages 5-6, barbosagouveia2021characterizationofa pages 5-6)

Gene/protein annotations with ontology terms
- AGK (HGNC; protein: acylglycerol kinase): mitochondrial lipid kinase and TIM22 subunit; loss causes Sengers syndrome. Processes: phosphatidic acid biosynthesis; mitochondrial carrier import via TIM22; OXPHOS assembly/function; response to oxidative stress. Components: inner mitochondrial membrane; TIM22 complex. (siriwardena2013mitochondrialcitratesynthase pages 8-8, barbosagouveia2021characterizationofa pages 5-6, wortmann2015inbornerrorsof pages 5-6, jackson2021thetim22complex pages 1-2)
- TIM22 complex (includes TIMM22, AGK, Tim9/10/10b, TIMM29/Tim29): mediates insertion of multi-pass carriers (SLC25) and SFXNs; dysfunction underlies Sengers spectrum. (jackson2021thetim22complex pages 1-2, shalata2025sengerssyndromecaused pages 1-2)
- ANT1/SLC25A4: mitochondrial ADP/ATP carrier impacted secondarily in AGK/TIM22 dysfunction. (wortmann2015inbornerrorsof pages 5-6)

Phenotype associations (HP terms)
- Congenital cataract (HP:0000538) (siriwardena2013mitochondrialcitratesynthase pages 8-8, wang2021casereporttwo pages 2-4)
- Hypertrophic cardiomyopathy (HP:0001639) (wang2021casereporttwo pages 2-4, panicucci2022longtermfollowup pages 6-6)
- Lactic acidosis (HP:0002151) (barbosagouveia2021characterizationofa pages 5-6, panicucci2022longtermfollowup pages 6-6)
- Mitochondrial myopathy (HP:0003016) (siriwardena2013mitochondrialcitratesynthase pages 8-8, wang2021casereporttwo pages 2-4)

Cell type involvement (CL terms)
- Cardiomyocytes (CL:0000746) (wang2021casereporttwo pages 2-4)
- Skeletal muscle fibers (CL:0000186) (siriwardena2013mitochondrialcitratesynthase pages 8-8)
- Lens fiber cells (CL:0000653) (siriwardena2013mitochondrialcitratesynthase pages 8-8)

Anatomical locations (UBERON terms)
- Heart (UBERON:0000948) (wang2021casereporttwo pages 2-4)
- Skeletal muscle (UBERON:0001134) (siriwardena2013mitochondrialcitratesynthase pages 8-8)
- Ocular lens (UBERON:0001105) (siriwardena2013mitochondrialcitratesynthase pages 8-8)

Chemical entities (CHEBI terms)
- Phosphatidic acid (CHEBI:PA) (siriwardena2013mitochondrialcitratesynthase pages 8-8)
- Lysophosphatidic acid (CHEBI:LPA) (siriwardena2013mitochondrialcitratesynthase pages 8-8)
- Diacylglycerol (CHEBI:DAG) (siriwardena2013mitochondrialcitratesynthase pages 8-8)
- Lactate (CHEBI:16526) (wang2021casereporttwo pages 2-4)

Evidence items and selected sources (URLs, publication dates)
- Siriwardena et al., Mol Genet Metab 2013; DOI:10.1016/j.ymgme.2012.11.282; published Jan 2013; https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8, siriwardena2013mitochondrialcitratesynthase pages 8-10)
- Wortmann et al., J Inherit Metab Dis 2015; DOI:10.1007/s10545-014-9759-7; published Jan 2015; https://doi.org/10.1007/s10545-014-9759-7 (wortmann2015inbornerrorsof pages 5-6)
- Jackson et al., Mol Biol Cell 2021; DOI:10.1091/mbc.E20-06-0390; published Mar 2021; https://doi.org/10.1091/mbc.e20-06-0390 (jackson2021thetim22complex pages 1-2)
- Barbosa‑Gouveia et al., Int J Mol Sci 2021; DOI:10.3390/ijms222413484; published Dec 2021; https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6, barbosagouveia2021characterizationofa pages 1-2)
- Wang et al., Front Pediatr 2021; DOI:10.3389/fped.2021.639687; published Jun 2021; https://doi.org/10.3389/fped.2021.639687 (wang2021casereporttwo pages 8-9, wang2021casereporttwo pages 2-4)
- Panicucci et al., Ital J Pediatr 2022; DOI:10.1186/s13052-022-01370-y; published Oct 2022; https://doi.org/10.1186/s13052-022-01370-y (panicucci2022longtermfollowup pages 6-6, panicucci2022longtermfollowup pages 2-4)
- Mishra et al., IUBMB Life 2023; DOI:10.1002/iub.2767; published Jul 2023; https://doi.org/10.1002/iub.2767 (wang2021casereporttwo pages 8-9)
- Popoiu et al., Curr Heart Fail Rep 2023; DOI:10.1007/s11897-023-00592-3; published Feb 2023; https://doi.org/10.1007/s11897-023-00592-3 (wang2021casereporttwo pages 2-4)
- Shalata et al., Hum Genomics 2025; DOI:10.1186/s40246-025-00723-y; published Feb 2025; https://doi.org/10.1186/s40246-025-00723-y (shalata2025sengerssyndromecaused pages 1-2)

Embedded core annotations table
| Category | Entity Name | Ontology/ID | Role/Description | Evidence (DOI/URL), Year |
|---|---|---|---|---|
| Genes / Proteins | AGK (acylglycerol kinase) | HGNC:AGK | Mitochondrial lipid kinase; structural subunit of TIM22 complex — required for PA/LPA production and TIM22-dependent carrier import | https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6), https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), https://doi.org/10.1007/s10545-014-9759-7 (wortmann2015inbornerrorsof pages 5-6), 2021/2013/2015 |
| Genes / Proteins | TIM22 complex (TIMM22 + subunits; AGK as TIM22 subunit) | Complex:TIM22 (includes TIMM22, TIMM29, AGK) | Inner-membrane carrier translocase that inserts multispanning carrier proteins (SLC25 family, SFXNs); loss impairs carrier biogenesis and downstream metabolism | Functional/TIM22 role noted in AGK studies: https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6), mechanistic TIM22 literature summarized in reviews (wortmann2015inbornerrorsof pages 5-6), 2021/2015 |
| Genes / Proteins | SLC25A4 (ANT1, adenine nucleotide translocator 1) | HGNC:SLC25A4 | Mitochondrial ADP/ATP carrier; reported decreased/absent in some AGK-deficient patient muscle — links to impaired ADP/ATP exchange and OXPHOS dysfunction | https://doi.org/10.1007/s10545-014-9759-7 (wortmann2015inbornerrorsof pages 5-6), https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2015/2013 |
| Biological Process | Mitochondrial protein import via TIM22 | GO: mitochondrial carrier import (TIM22-related) | Insertion/biogenesis of multispanning inner-membrane carrier proteins (SLC25 family, SFXNs); AGK deficiency reduces TIM22 substrates and impairs metabolism (e.g., one-carbon) | Functional proteomics and TIM22 substrate loss in AGK deficiency: https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6), 2021 |
| Biological Process | Phosphatidic acid (PA) biosynthesis / DAG -> PA conversion | GO: phosphatidic acid biosynthetic process | AGK phosphorylates DAG/MAG to produce PA/LPA in mitochondria; loss perturbs inner-membrane lipid composition and signaling | Lipid-kinase role described: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6), 2013/2021 |
| Biological Process | Cardiolipin-related OXPHOS assembly/function | GO: cardiolipin metabolic process / OXPHOS assembly | Altered PA/CL metabolism destabilizes respiratory-chain complexes (esp. complexes I and V) and ANT function, reducing ATP synthesis | Reviews and mechanistic reports: https://doi.org/10.1007/s10545-014-9759-7 (wortmann2015inbornerrorsof pages 5-6), https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6), 2015/2021 |
| Biological Process | Reactive oxygen species (ROS) response / oxidative stress | GO: cellular response to oxidative stress | AGK loss → DAG accumulation, increased mitochondrial ROS, upregulation of SOD2/antioxidant responses and oxidative damage to OXPHOS components | Mitochondrial ROS and antioxidant changes: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2013 |
| Cellular Component | Inner mitochondrial membrane (IMM) | GO:0005743 (inner mitochondrial membrane) | Location of AGK, TIM22 complex, carrier proteins and critical lipid milieu (PA/CL) required for OXPHOS and carrier import | AGK/TIM22 localizations and IMM dysfunction: https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6), https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2021/2013 |
| Cellular Component | TIM22 complex | Complex:TIM22 (IMM translocase) | Multisubunit carrier translocase that inserts multispanning proteins into IMM; AGK functions as an accessory/subunit for stability/function | TIM22–AGK relationship and substrate loss: https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6), 2021 |
| Cellular Component | Mitochondrial matrix / cristae | UBERON:mitochondrial matrix / mitochondrial cristae | Cristae structure and matrix enzymes (e.g., citrate synthase) show ultrastructural/biochemical abnormalities (including citrate synthase crystals) in Sengers patients | Ultrastructure and citrate synthase crystals: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2013 |
| Phenotype | Congenital cataract | HPO: Congenital cataract (HP:0000538) | Early bilateral lens opacities are a defining clinical feature (very high penetrance in AGK cases) linked to mitochondrial/lipid dysfunction in lens fibers | Multiple case series/reviews reporting high cataract frequency: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-10), 2013 |
| Phenotype | Hypertrophic cardiomyopathy (HCM) / cardiomyopathy | HPO: Hypertrophic cardiomyopathy (HP:0001639) | Severe neonatal-onset HCM or dilated cardiomyopathy occurs commonly and is a major cause of early mortality; reflects high cardiac energy demand and OXPHOS failure | Clinical cohorts and case reports: https://doi.org/10.3389/fped.2021.639687 (wang2021casereporttwo pages 8-9), https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2021/2013 |
| Phenotype | Lactic acidosis / elevated lactate | HPO: Lactic acidosis (HP:0002151) | Impaired oxidative phosphorylation leads to increased anaerobic glycolysis and elevated blood/tissue lactate; variable severity from intermittent to marked neonatal lactic acidosis | Metabolic findings in patient fibroblasts / clinical reports: https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6), https://doi.org/10.3389/fped.2021.639687 (wang2021casereporttwo pages 8-9), 2021 |
| Phenotype | Skeletal myopathy / mitochondrial myopathy | HPO: Mitochondrial myopathy (HP:0003016) | Hypotonia, weakness, exercise intolerance and muscle pathology (RRF-like changes, lipid droplets, abnormal mitochondria) reflect impaired muscle OXPHOS | Case reports and muscle pathology studies: https://doi.org/10.3389/fped.2021.639687 (wang2021casereporttwo pages 8-9), https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2021/2013 |
| Cell Type | Cardiomyocytes | CL: cardiomyocyte (CL:0000746) | High-energy cardiac myocytes show pronounced vulnerability to AGK/TIM22 dysfunction, resulting in cardiomyopathy and heart failure | Cardiac involvement reviews and cases: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), https://doi.org/10.1016/j.10.1007/s10545-014-9759-7 (wortmann2015inbornerrorsof pages 5-6), 2013/2015 |
| Cell Type | Skeletal myofibers | CL: skeletal muscle fiber (CL:0000186) | Skeletal muscle fibers display mitochondrial structural defects, OXPHOS deficiency and clinical myopathy | Muscle biopsy and ultrastructure reports: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), https://doi.org/10.3389/fped.2021.639687 (wang2021casereporttwo pages 8-9), 2013/2021 |
| Cell Type | Lens fiber cells | CL: lens fiber cell (CL:0000653) | Lens fibers rely on mitochondrial/lipid homeostasis during development; AGK-related lipid/protein import defects associated with congenital cataract | Cataract genetics and AGK frequency: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2013 |
| Anatomical Location | Heart | UBERON:0000948 (heart) | Primary organ affected with early hypertrophic/dilated cardiomyopathy and heart failure in severe forms | Clinical case series and reviews: https://doi.org/10.3389/fped.2021.639687 (wang2021casereporttwo pages 8-9), https://doi.org/10.1007/s10545-014-9759-7 (wortmann2015inbornerrorsof pages 5-6), 2021/2015 |
| Anatomical Location | Skeletal muscle | UBERON:0001134 (skeletal muscle) | Affected tissue with mitochondrial myopathy, exercise intolerance and histopathologic mitochondrial changes | Muscle pathology reports: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2013 |
| Anatomical Location | Ocular lens | UBERON:0001105 (lens) | Early bilateral congenital cataracts are a hallmark, reflecting mitochondrial/lipid dysregulation in lens cells | Cataract-focused reviews and case reports: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2013 |
| Chemical / Metabolite | Phosphatidic acid (PA) | CHEBI:PA (phosphatidic acid) | Product of AGK-mediated phosphorylation (DAG -> PA); PA is precursor for cardiolipin and critical for IMM lipid homeostasis | Lipid-kinase function and PA role: https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6), https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2021/2013 |
| Chemical / Metabolite | Lysophosphatidic acid (LPA) | CHEBI:LPA (lysophosphatidic acid) | AGK product (from MAG) and signaling lipid; perturbation implicated in IMM lipid imbalance | AGK substrate/product descriptions: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2013 |
| Chemical / Metabolite | Diacylglycerol (DAG) | CHEBI:DAG (diacylglycerol) | AGK substrate; DAG accumulation in AGK deficiency may drive ROS signaling and PKD1 activation | DAG accumulation and ROS links: https://doi.org/10.1016/j.ymgme.2012.11.282 (siriwardena2013mitochondrialcitratesynthase pages 8-8), 2013 |
| Chemical / Metabolite | Lactate | CHEBI:16526 (lactate) | Elevated systemic/tissue lactate due to impaired oxidative phosphorylation; used clinically as a metabolic marker | Clinical metabolic findings and lactic acidosis in reports: https://doi.org/10.3389/fped.2021.639687 (wang2021casereporttwo pages 8-9), https://doi.org/10.3390/ijms222413484 (barbosagouveia2021characterizationofa pages 5-6), 2021 |


*Table: Concise ontology-aligned annotations for Sengers syndrome covering genes, processes, components, phenotypes, cells, organs and metabolites with primary evidence links to the collected literature (context IDs).*

Notes on limitations
- Cohort-level statistics remain sparse in the available 2023–2024 literature cited here; most data are mechanistic, case-based, or review-level. A 2023 mini‑review of AGK‑confirmed cases (Wu et al., Mol Genet Metab) was unobtainable in this search, limiting the ability to provide pooled phenotypic frequencies from 2023–2024. (jackson2021thetim22complex pages 1-2)


References

1. (siriwardena2013mitochondrialcitratesynthase pages 8-8): Komudi Siriwardena, Nevena MacKay, Valeriy Levandovskiy, Susan Blaser, Julian Raiman, Paul F. Kantor, Cameron Ackerley, Brian H. Robinson, Andreas Schulze, and Jessie M. Cameron. Mitochondrial citrate synthase crystals: novel finding in sengers syndrome caused by acylglycerol kinase (agk) mutations. Molecular genetics and metabolism, 108 1:40-50, Jan 2013. URL: https://doi.org/10.1016/j.ymgme.2012.11.282, doi:10.1016/j.ymgme.2012.11.282. This article has 46 citations and is from a peer-reviewed journal.

2. (wortmann2015inbornerrorsof pages 5-6): Saskia B. Wortmann, Marc Espeel, Ligia Almeida, Annette Reimer, Dennis Bosboom, Frank Roels, Arjan P.M. de Brouwer, and Ron A. Wevers. Inborn errors of metabolism in the biosynthesis and remodelling of phospholipids. Journal of Inherited Metabolic Disease, 38:99-110, Jan 2015. URL: https://doi.org/10.1007/s10545-014-9759-7, doi:10.1007/s10545-014-9759-7. This article has 64 citations and is from a peer-reviewed journal.

3. (barbosagouveia2021characterizationofa pages 5-6): Sofia Barbosa-Gouveia, Maria E. Vázquez-Mosquera, Emiliano Gonzalez-Vioque, Álvaro Hermida-Ameijeiras, Laura L. Valverde, Judith Armstrong-Moron, Maria del Carmen Fons-Estupiña, Liesbeth T. Wintjes, Antonia Kappen, Richard J. Rodenburg, and Maria L. Couce. Characterization of a novel splicing variant in acylglycerol kinase (agk) associated with fatal sengers syndrome. International Journal of Molecular Sciences, 22:13484, Dec 2021. URL: https://doi.org/10.3390/ijms222413484, doi:10.3390/ijms222413484. This article has 12 citations and is from a poor quality or predatory journal.

4. (jackson2021thetim22complex pages 1-2): Thomas D. Jackson, Daniella H. Hock, Kenji M. Fujihara, Catherine S. Palmer, Ann E. Frazier, Yau C. Low, Yilin Kang, Ching-Seng Ang, Nicholas J. Clemons, David R. Thorburn, David A. Stroud, and Diana Stojanovski. The tim22 complex mediates the import of sideroflexins and is required for efficient mitochondrial one-carbon metabolism. Molecular Biology of the Cell, 32:475-491, Mar 2021. URL: https://doi.org/10.1091/mbc.e20-06-0390, doi:10.1091/mbc.e20-06-0390. This article has 37 citations and is from a domain leading peer-reviewed journal.

5. (shalata2025sengerssyndromecaused pages 1-2): Adel Shalata, Ann Saada, Mohammed Mahroum, Yarin Hadid, Chaya Furman, Zaher Eldin Shalata, Robert J. Desnick, Avraham Lorber, Asaad Khoury, Adnan Higazi, Avraham Shaag, Varda Barash, Ronen Spiegel, Euvgeni Vlodavsky, Pierre Rustin, Shmuel Pietrokovski, Irena Manov, Dan Gieger, Galit Tal, Adi Salzberg, and Hanna Mandel. Sengers syndrome caused by biallelic timm29 variants and rnai silencing in drosophila orthologue recapitulates the human phenotype. Human Genomics, Feb 2025. URL: https://doi.org/10.1186/s40246-025-00723-y, doi:10.1186/s40246-025-00723-y. This article has 2 citations and is from a peer-reviewed journal.

6. (barbosagouveia2021characterizationofa pages 1-2): Sofia Barbosa-Gouveia, Maria E. Vázquez-Mosquera, Emiliano Gonzalez-Vioque, Álvaro Hermida-Ameijeiras, Laura L. Valverde, Judith Armstrong-Moron, Maria del Carmen Fons-Estupiña, Liesbeth T. Wintjes, Antonia Kappen, Richard J. Rodenburg, and Maria L. Couce. Characterization of a novel splicing variant in acylglycerol kinase (agk) associated with fatal sengers syndrome. International Journal of Molecular Sciences, 22:13484, Dec 2021. URL: https://doi.org/10.3390/ijms222413484, doi:10.3390/ijms222413484. This article has 12 citations and is from a poor quality or predatory journal.

7. (siriwardena2013mitochondrialcitratesynthase pages 8-10): Komudi Siriwardena, Nevena MacKay, Valeriy Levandovskiy, Susan Blaser, Julian Raiman, Paul F. Kantor, Cameron Ackerley, Brian H. Robinson, Andreas Schulze, and Jessie M. Cameron. Mitochondrial citrate synthase crystals: novel finding in sengers syndrome caused by acylglycerol kinase (agk) mutations. Molecular genetics and metabolism, 108 1:40-50, Jan 2013. URL: https://doi.org/10.1016/j.ymgme.2012.11.282, doi:10.1016/j.ymgme.2012.11.282. This article has 46 citations and is from a peer-reviewed journal.

8. (wang2021casereporttwo pages 8-9): Benzhen Wang, Zhanhui Du, Guangsong Shan, Chuanzhu Yan, Victor Wei Zhang, and Zipu Li. Case report: two chinese infants of sengers syndrome caused by mutations in agk gene. Frontiers in Pediatrics, Jun 2021. URL: https://doi.org/10.3389/fped.2021.639687, doi:10.3389/fped.2021.639687. This article has 10 citations and is from a poor quality or predatory journal.

9. (wang2021casereporttwo pages 2-4): Benzhen Wang, Zhanhui Du, Guangsong Shan, Chuanzhu Yan, Victor Wei Zhang, and Zipu Li. Case report: two chinese infants of sengers syndrome caused by mutations in agk gene. Frontiers in Pediatrics, Jun 2021. URL: https://doi.org/10.3389/fped.2021.639687, doi:10.3389/fped.2021.639687. This article has 10 citations and is from a poor quality or predatory journal.

10. (panicucci2022longtermfollowup pages 6-6): Chiara Panicucci, Maria Cristina Schiaffino, Claudia Nesti, Maria Derchi, Gianluca Trocchio, Mariasavina Severino, Nicola Stagnaro, Enrico Priolo, Federico Zara, Filippo M. Santorelli, and Claudio Bruno. Long term follow-up in two siblings with sengers syndrome: case report. Italian Journal of Pediatrics, Oct 2022. URL: https://doi.org/10.1186/s13052-022-01370-y, doi:10.1186/s13052-022-01370-y. This article has 3 citations and is from a peer-reviewed journal.

11. (panicucci2022longtermfollowup pages 2-4): Chiara Panicucci, Maria Cristina Schiaffino, Claudia Nesti, Maria Derchi, Gianluca Trocchio, Mariasavina Severino, Nicola Stagnaro, Enrico Priolo, Federico Zara, Filippo M. Santorelli, and Claudio Bruno. Long term follow-up in two siblings with sengers syndrome: case report. Italian Journal of Pediatrics, Oct 2022. URL: https://doi.org/10.1186/s13052-022-01370-y, doi:10.1186/s13052-022-01370-y. This article has 3 citations and is from a peer-reviewed journal.