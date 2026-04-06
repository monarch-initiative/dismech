---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-09T23:27:20.038199'
end_time: '2026-02-09T23:35:13.503765'
duration_seconds: 473.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ellis-van Creveld Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Ellis-van Creveld Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ellis-van Creveld Syndrome**.
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
- **Disease Name:** Ellis-van Creveld Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ellis-van Creveld Syndrome**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Ellis-van Creveld Syndrome (EvC)
- MONDO ID: (not confirmed in this report)
- Category: Mendelian

Pathophysiology description
Ellis-van Creveld syndrome is a skeletal ciliopathy driven by defective Hedgehog (Hh) signal transduction at the primary cilium due to loss of function in the EVC–EVC2 transmembrane complex or disruption of its ciliary recruitment by intraflagellar transport components. The EVC–EVC2 heterodimer localizes to a specialized ciliary subdomain termed the EvC zone, where it forms a signaling complex with Smoothened (SMO) to promote dissociation of SUFU from GLI proteins and enable GLI trafficking and activation. Chondrocytes in the growth plate depend on these events for Indian hedgehog (IHH)-dependent proliferation and endochondral ossification; when impaired, proliferative and hypertrophic zones are reduced, explaining disproportionate short stature, short ribs, and polydactyly. Cardiac malformations, especially atrioventricular canal (AVC) defects and common atrium, arise from disrupted Sonic hedgehog (SHH) signaling during endocardial cushion and septal development; some evidence links this axis to laterality/heterotaxy pathways. Mechanistic variants in IFT-A (e.g., WDR35/IFT121) phenocopy EvC by preventing ciliary recruitment of EVC/EVC2 and SMO, collapsing downstream Hh readouts. Together, these data define EvC as a cilia-localized failure of Hh transduction with tissue-specific consequences in cartilage, heart, and ectodermal derivatives (teeth, nails) (caparrosmartin2013theciliaryevcevc2 pages 1-2, caparrosmartin2013theciliaryevcevc2 pages 7-9, caparrosmartin2015specificvariantsin pages 1-2, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

1) Core Pathophysiology
- Primary mechanism: loss of EVC–EVC2 complex function at the EvC zone of the primary cilium attenuates Hh signaling downstream of SMO by impairing SUFU–GLI dissociation and GLI trafficking/activation. In chondrocytes, this reduces IHH target expression and endochondral ossification. EvC is therefore a cilia-localized signal transduction defect impacting skeletal and cardiac morphogenesis (caparrosmartin2013theciliaryevcevc2 pages 1-2, caparrosmartin2013theciliaryevcevc2 pages 7-9).
- Molecular pathways dysregulated: canonical Hedgehog signaling (SHH/IHH→PTCH1→SMO→GLI). EVC/EVC2 physically associate with SMO in cilia; EVC/EVC2 loss reduces Hh output even when SUFU is absent, indicating roles at GLI activation/trafficking in the cilium (caparrosmartin2013theciliaryevcevc2 pages 7-9).
- Cellular processes affected: ciliary trafficking of SMO/GLI, SUFU–GLI complex dynamics, growth plate chondrocyte proliferation and hypertrophic differentiation, endochondral ossification; cardiac septation via SHH signaling in endocardial cushions (caparrosmartin2013theciliaryevcevc2 pages 1-2, caparrosmartin2013theciliaryevcevc2 pages 7-9, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

Key mechanistic quotes
- “A Smoothened‑Evc2 complex transduces the Hedgehog signal at primary cilia.” (Dorn et al. 2012) (caparrosmartin2013theciliaryevcevc2 pages 7-9).
- “The ciliary Evc/Evc2 complex… controls Hedgehog pathway activity in chondrocytes by regulating Sufu/Gli3 dissociation and Gli3 trafficking in primary cilia.” (Caparrós‑Martín et al. 2013) (caparrosmartin2013theciliaryevcevc2 pages 1-2).
- “Monoubiquitination of EVC‑EVC2 cytosolic tails greatly reduces their protein levels… modification with the small ubiquitin‑related modifier SUMO3… enhances complex accumulation at the EvC zone.” (Barbeito et al. 2023) (barbeito2023evcevc2complexstability pages 2-4).
- “Specific variants in WDR35 cause a distinctive form of Ellis‑van Creveld syndrome by disrupting the recruitment of the EvC complex and SMO into the cilium.” (Caparrós‑Martín et al. 2015) (caparrosmartin2015specificvariantsin pages 1-2).

2) Key Molecular Players
- Genes/Proteins (HGNC):
  - EVC (HGNC:3500) and EVC2 (HGNC:23301): transmembrane heterodimer at the EvC zone; required for Hh transduction downstream of SMO; EVC2 C‑terminal W‑peptide (including FV motif) mediates EvC‑zone targeting and stabilizes the complex (caparrosmartin2013theciliaryevcevc2 pages 1-2, barbeito2023evcevc2complexstability pages 2-4, louie2020molecularandcellular pages 3-5).
  - SMO (HGNC:11119): ciliary effector that binds EVC/EVC2 at EvC zone to propagate Hh signaling to GLI; SMO ciliary entry can occur without EVC/EVC2, but productive signaling is reduced (caparrosmartin2013theciliaryevcevc2 pages 7-9).
  - GLI3 (HGNC:4311) and SUFU (HGNC:20469): EVC/EVC2 promote SUFU–GLI dissociation and GLI trafficking to the ciliary tip to generate activator forms; loss redistributes GLI3 and enriches GLI3 repressor (caparrosmartin2013theciliaryevcevc2 pages 1-2).
  - EFCAB7 (HGNC:26058) and IQCE (HGNC:29063): tether the EVC/EVC2 complex to EvC zone; SUMO3 enhances tethering, ubiquitination reduces protein levels (barbeito2023evcevc2complexstability pages 2-4).
  - WDR35/IFT121 (HGNC:15866): IFT-A component required for entry/recruitment of EVC/EVC2 and SMO into cilia; disease variants prevent ciliary localization and collapse Hh readouts (caparrosmartin2015specificvariantsin pages 1-2, caparrosmartin2015specificvariantsin pages 4-5).

- Chemical entities: SAG (SMO agonist) used in functional studies to probe Hh responsiveness; proteasome inhibitor MG132 stabilizes hypomorphic WDR35Δ3 in vitro (experimental tools) (caparrosmartin2015specificvariantsin pages 4-5).

- Cell types (CL): growth plate chondrocytes (CL:0000138) are primary effectors of IHH signaling in bone; endocardial cushion mesenchyme (CL:0002519) in cardiac septation (caparrosmartin2013theciliaryevcevc2 pages 1-2, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

- Anatomical locations (UBERON): primary cilium/EvC zone near the transition zone (GO/UBERON mapping); growth plate of bone (UBERON:0003860); atrioventricular canal (UBERON:0002084); cardiac septum (UBERON:0002080); tooth (UBERON:0001091) (caparrosmartin2013theciliaryevcevc2 pages 1-2, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

3) Biological Processes (GO terms; disrupted in EvC)
- Hedgehog signaling pathway (GO:0007224): attenuated due to defective EVC–EVC2-SMO complex function and impaired SUFU–GLI dynamics (caparrosmartin2013theciliaryevcevc2 pages 1-2, caparrosmartin2013theciliaryevcevc2 pages 7-9).
- Chondrocyte differentiation (GO:0030154) and endochondral ossification (GO:0001958): reduced proliferative/hypertrophic zones and target gene expression in Evc/Evc2‑deficient growth plates (caparrosmartin2013theciliaryevcevc2 pages 1-2).
- Intraflagellar transport (GO:0035725): impaired recruitment of EVC/EVC2 and SMO to cilia in WDR35/IFT121 mutants (caparrosmartin2015specificvariantsin pages 1-2, caparrosmartin2015specificvariantsin pages 4-5).
- Protein ubiquitination (GO:0016567) and protein SUMOylation (GO:0016925): post-translational modifications modulate EVC–EVC2 stability and EvC‑zone targeting (barbeito2023evcevc2complexstability pages 2-4).

4) Cellular Components (GO terms)
- Primary cilium (GO:0005929), EvC zone at the ciliary base immediately distal to the transition zone (ciliary transition zone, GO:0035869): site of EVC–EVC2–SMO complex assembly and GLI regulation (caparrosmartin2013theciliaryevcevc2 pages 7-9, barbeito2023evcevc2complexstability pages 2-4).
- Ciliary tip: site of GLI accumulation and processing; ciliary base: site of SUFU–GLI dissociation (caparrosmartin2013theciliaryevcevc2 pages 1-2).

5) Disease Progression (sequence of events)
- Genetic trigger: biallelic pathogenic variants in EVC or EVC2 (or hypomorphic alleles), or select IFT-A components (e.g., WDR35) (caparrosmartin2015specificvariantsin pages 1-2, caparrosmartin2015specificvariantsin pages 4-5, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).
- Ciliary defect: failure of EVC–EVC2 complex to accumulate at EvC zone, or inability of EVC/EVC2 and SMO to enter/recruit to cilia; altered tethering (EFCAB7–IQCE) and post-translational regulation (ubiquitin/SUMO) further reduce complex abundance (caparrosmartin2013theciliaryevcevc2 pages 7-9, barbeito2023evcevc2complexstability pages 2-4, caparrosmartin2015specificvariantsin pages 1-2).
- Signaling failure: diminished SUFU–GLI dissociation and GLI trafficking; reduced GLI activator formation and Hh target gene transcription (caparrosmartin2013theciliaryevcevc2 pages 1-2, caparrosmartin2013theciliaryevcevc2 pages 7-9).
- Tissue outcomes: in growth plates, decreased IHH signaling reduces proliferative and hypertrophic chondrocyte zones and delays endochondral ossification; in heart, disturbed SHH contributes to AV canal/common atrium defects via impaired endocardial cushion morphogenesis; ectodermal derivatives (teeth/nails) show dysplasia (caparrosmartin2013theciliaryevcevc2 pages 1-2, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

6) Phenotypic Manifestations (HP terms; mechanistic links)
- Postaxial polydactyly (HP:0001162), short long bones (HP:0003026), short ribs (HP:0000773): arise from impaired IHH‑dependent growth plate proliferation/differentiation (caparrosmartin2013theciliaryevcevc2 pages 1-2).
- Common atrium (HP:0006697), atrioventricular canal defect (HP:0001671): linked to perturbed SHH signaling in cardiac septation; EVC/EVC2/SMO ciliary entry and SHH are emphasized as unifying mechanisms across syndromic AV canal defects (piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).
- Dental/nail anomalies (HP:0000692): reflect ectodermal consequences of ciliary Hh signaling defects (louie2020molecularandcellular pages 3-5, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

Recent developments and latest research (2023–2024 priority)
- Post-translational control of the EVC–EVC2 complex (2023): endogenous interactome revealed USP7 and confirmed EFCAB7–IQCE; “monoubiquitination… greatly reduces [EVC–EVC2] protein levels,” whereas “modification… with… SUMO3… enhances complex accumulation at the EvC zone,” mapping second EFCAB7-binding motif in EVC2’s W‑peptide (Frontiers in Cell and Developmental Biology, Jul 2023; doi:10.3389/fcell.2023.1190258) (barbeito2023evcevc2complexstability pages 2-4, barbeito2023evcevc2complexstability pages 1-2).
- Genotype–phenotype refinement (2020 but clinically impactful): hypomorphic EVC alleles can yield a mild EvC subtype dominated by common atrium/AV canal defect with postaxial polydactyly; patient fibroblasts show reduced EVC/EVC2 levels and fewer EVC2‑positive cilia (Human Mutation, Oct 2020; doi:10.1002/humu.24112) (piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

Current applications and real-world implementations
- Molecular diagnosis: sequencing of EVC/EVC2 plus IFT genes (e.g., WDR35) in EvC phenotypes with ciliary Hh defects; recognition that WDR35 variants can “disrupt the recruitment of the EvC complex and SMO into the cilium,” phenocopying EvC (Human Molecular Genetics, Apr 2015; doi:10.1093/hmg/ddv152) (caparrosmartin2015specificvariantsin pages 1-2, caparrosmartin2015specificvariantsin pages 4-5).
- Functional readouts: ciliary localization assays for EVC/EVC2/SMO; Hh pathway induction with SMO agonists (e.g., SAG) and GLI1/GLI‑reporters in patient-derived cells; proteasome inhibition (MG132) can stabilize hypomorphic WDR35Δ3 in vitro for mechanistic confirmation (caparrosmartin2015specificvariantsin pages 4-5).
- Cardiac risk stratification: expert reviews emphasize SHH’s “unifying role” in AV canal defects across syndromes and the importance of ciliary entry of EVC, EVC2 and SMO (2019–2021), supporting early echocardiographic surveillance in EvC (piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

Expert opinions and analysis from authoritative sources
- Developmental cell biology and human genetics papers converge that the EvC zone functions as a signal relay platform for SMO–EVC/EVC2 to license GLI activation in the cilium; loss produces partial Hh blunting rather than absolute null signaling in many contexts, consistent with viable but severely dysplastic phenotypes (caparrosmartin2013theciliaryevcevc2 pages 7-9, caparrosmartin2013theciliaryevcevc2 pages 1-2, louie2020molecularandcellular pages 3-5).
- Cardiac genetics reviews highlight SHH as a shared pathway for AV canal/common atrium in EvC, and suggest that defects in ciliary entry/retention of EVC/EVC2/SMO are pathogenic in the heart as in cartilage (piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

Relevant statistics and recent data
- Estimated EvC incidence ~1 in 60,000 (review synthesis) (Oct 2020; Journal of Developmental Biology; doi:10.3390/jdb8040025) (louie2020molecularandcellular pages 3-5).
- Growth plate pathology in Evc/Evc2 mouse models: reduced proliferative and hypertrophic zones with decreased IHH target expression, correlating with limb and rib shortening (Human Molecular Genetics, Oct 2013; doi:10.1093/hmg/dds409) (caparrosmartin2013theciliaryevcevc2 pages 1-2).

Evidence items with PMIDs/DOIs, URLs, and dates
- Caparrós‑Martín et al., Human Molecular Genetics, “The ciliary Evc/Evc2 complex…,” Oct 2013. doi:10.1093/hmg/dds409; URL: https://doi.org/10.1093/hmg/dds409 (caparrosmartin2013theciliaryevcevc2 pages 1-2).
- Dorn et al., Developmental Cell, “A Smoothened‑Evc2 complex…,” Oct 2012. doi:10.1016/j.devcel.2012.07.004; URL: https://doi.org/10.1016/j.devcel.2012.07.004 (caparrosmartin2013theciliaryevcevc2 pages 7-9).
- Barbeito et al., Frontiers in Cell and Developmental Biology, “EVC‑EVC2 complex stability… ubiquitin and SUMO,” Jul 2023. doi:10.3389/fcell.2023.1190258; URL: https://doi.org/10.3389/fcell.2023.1190258 (barbeito2023evcevc2complexstability pages 2-4, barbeito2023evcevc2complexstability pages 1-2).
- Caparrós‑Martín et al., Human Molecular Genetics, “Specific variants in WDR35…,” Apr 2015. doi:10.1093/hmg/ddv152; URL: https://doi.org/10.1093/hmg/ddv152 (caparrosmartin2015specificvariantsin pages 1-2, caparrosmartin2015specificvariantsin pages 4-5).
- Piceci‑Sparascio et al., Human Mutation, “Common atrium/AV canal defect… mild EvC,” Oct 2020. doi:10.1002/humu.24112; URL: https://doi.org/10.1002/humu.24112 (piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).
- Calcagni et al., Genes, “Cardiac Defects and Genetic Syndromes…,” Jul 2021. doi:10.3390/genes12071047; URL: https://doi.org/10.3390/genes12071047 (piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).
- Digilio et al., Clinical Genetics, “Atrioventricular canal defect… unifying role of SHH,” Feb 2019. doi:10.1111/cge.13375; URL: https://doi.org/10.1111/cge.13375 (piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).
- Louie et al., Journal of Developmental Biology, “Molecular and Cellular Pathogenesis of EvC…,” Oct 2020. doi:10.3390/jdb8040025; URL: https://doi.org/10.3390/jdb8040025 (louie2020molecularandcellular pages 3-5).

Gene/protein annotations with ontology terms
- EVC (HGNC:3500): GO processes—Hedgehog signaling (GO:0007224); Cellular component—primary cilium/EvC zone (GO:0005929/GO:0035869); Phenotypes—HP:0001162, HP:0000773, HP:0001671 (caparrosmartin2013theciliaryevcevc2 pages 1-2, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).
- EVC2 (HGNC:23301): GO processes—Hedgehog signaling; protein ubiquitination (GO:0016567); protein SUMOylation (GO:0016925); Cellular component—EvC zone; Phenotypes—polydactyly, dental anomalies (barbeito2023evcevc2complexstability pages 2-4, louie2020molecularandcellular pages 3-5).
- SMO (HGNC:11119): GO—Hedgehog signaling; Cellular component—ciliary membrane/EvC zone; Phenotypes—cardiac septation defects (caparrosmartin2013theciliaryevcevc2 pages 7-9, caparrosmartin2015specificvariantsin pages 1-2).
- GLI3 (HGNC:4311)/SUFU (HGNC:20469): GO—GLI-mediated transcription; proteolytic processing; Cellular component—ciliary tip/base; Phenotypes—skeletal anomalies (caparrosmartin2013theciliaryevcevc2 pages 1-2).
- EFCAB7 (HGNC:26058)/IQCE (HGNC:29063): GO—ciliary targeting; protein SUMOylation/ubiquitination; Cellular component—EvC zone tether; Phenotypes—EvC spectrum when disrupted (barbeito2023evcevc2complexstability pages 2-4).
- WDR35/IFT121 (HGNC:15866): GO—intraciliary transport (IFT‑A); Cellular component—ciliary shaft/base; Phenotypes—EvC‑like skeletal/cardiac features (caparrosmartin2015specificvariantsin pages 1-2, caparrosmartin2015specificvariantsin pages 4-5).

Phenotype associations (HP terms)
- HP:0001162 Postaxial polydactyly; HP:0000773 Short ribs; HP:0003026 Short long bones; HP:0006697 Common atrium; HP:0001671 Atrioventricular canal defect; HP:0000692 Abnormal dentition (caparrosmartin2013theciliaryevcevc2 pages 1-2, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20, louie2020molecularandcellular pages 3-5).

Cell type involvement (CL terms)
- CL:0000138 Growth plate chondrocyte; CL:0002519 Endocardial cushion mesenchyme (caparrosmartin2013theciliaryevcevc2 pages 1-2, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

Anatomical locations (UBERON terms)
- UBERON:0003860 Growth plate of bone; UBERON:0002084 Atrioventricular canal; UBERON:0002080 Cardiac septum; UBERON:0001091 Tooth (caparrosmartin2013theciliaryevcevc2 pages 1-2, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

Chemical entities (CHEBI terms)
- SAG (SMO agonist; CHEBI reference compound) used in ciliary Hh assays; MG132 (proteasome inhibitor) stabilizes hypomorphic WDR35Δ3 in vitro (experimental confirmation) (caparrosmartin2015specificvariantsin pages 4-5).

EvC Pathophysiology Summary (artifact)
| Genes/Proteins | Role in EvC/Hh signaling (one sentence) | Pathway/Process (GO term names) | Cellular component | Phenotypes linked (HP term names) | Key evidence | Source URL |
|---|---|---|---|---|---|---|
| EVC | Membrane protein that localizes to the EvC zone and supports Hedgehog signal transduction required for GLI activation in chondrocytes. | Hedgehog signaling; chondrocyte proliferation and differentiation; protein stability | Primary cilium — EvC zone / ciliary base | Postaxial polydactyly; Short stature; Short ribs; Tooth anomalies; AV canal defect | (caparrosmartin2013theciliaryevcevc2 pages 1-2, barbeito2023evcevc2complexstability pages 2-4) | https://doi.org/10.1093/hmg/dds409, https://doi.org/10.3389/fcell.2023.1190258 |
| EVC2 | Partner of EVC; its C‑terminal W‑peptide (FV motif and additional motifs) mediates EvC‑zone targeting and stabilizes the heterodimer to enable Hh transduction. | Hedgehog signaling; chondrocyte differentiation; protein ubiquitination; protein SUMOylation | Primary cilium — EvC zone; EVC2 cytosolic tail | Postaxial polydactyly; Short limbs; Dental/nail anomalies; Cardiac septation defects | (caparrosmartin2013theciliaryevcevc2 pages 1-2, barbeito2023evcevc2complexstability pages 2-4, louie2020molecularandcellular pages 3-5) | https://doi.org/10.1093/hmg/dds409, https://doi.org/10.3389/fcell.2023.1190258, https://doi.org/10.3390/jdb8040025 |
| EVC–EVC2 complex | Heterodimer that binds Smoothened (SMO) at the ciliary base to promote SUFU/GLI dissociation and GLI trafficking to the ciliary tip, enabling GLI activator formation. | Hedgehog signaling; SUFU–GLI processing; intraflagellar transport | EvC zone (immediately distal to transition zone); ciliary base and proximal axoneme | Impaired endochondral ossification; Polydactyly; AV canal/common atrium | (caparrosmartin2013theciliaryevcevc2 pages 1-2, caparrosmartin2013theciliaryevcevc2 pages 7-9, barbeito2023evcevc2complexstability pages 2-4) | https://doi.org/10.1093/hmg/dds409, https://doi.org/10.3389/fcell.2023.1190258 |
| SMO (Smoothened) | Ciliary GPCR‑like effector that translocates into cilia and forms a functional complex with EVC/EVC2 to propagate Hh signals to GLI effectors. | Hedgehog signaling; intraflagellar transport | Ciliary membrane and EvC zone (ciliary base) | Cardiac septation defects (AVCD/VSD); Skeletal dysplasia | (caparrosmartin2013theciliaryevcevc2 pages 1-2, caparrosmartin2015specificvariantsin pages 1-2) | https://doi.org/10.1093/hmg/dds409, https://doi.org/10.1093/hmg/ddv152 |
| GLI3 / SUFU | GLI transcription factors are processed into repressors/activators; EVC–EVC2 promotes SUFU–GLI dissociation and GLI trafficking/activation at cilia, controlling Hh target gene expression. | Hedgehog signaling; GLI-mediated transcription; proteolytic processing | Ciliary tip (GLI accumulation), ciliary base (SUFU complex), nucleus | Reduced growth‑plate proliferation/hypertrophy; VSD/AV canal defects; skeletal anomalies | (caparrosmartin2013theciliaryevcevc2 pages 1-2, caparrosmartin2013theciliaryevcevc2 pages 7-9) | https://doi.org/10.1093/hmg/dds409 |
| EFCAB7–IQCE tether | Tethers EVC–EVC2 to the EvC zone; required for proper EvC‑zone targeting and Hh signaling (SUMO3 enhances tethering; monoubiquitination reduces EVC–EVC2 levels). | Ciliary targeting; Hedgehog signaling; protein SUMOylation; protein ubiquitination | EvC zone / basal body interface (tether at ciliary base) | EvC skeletal/cardiac/dental phenotypes when disrupted | (barbeito2023evcevc2complexstability pages 2-4, barbeito2023evcevc2complexstability pages 1-2) | https://doi.org/10.3389/fcell.2023.1190258 |
| WDR35 (IFT121) | IFT‑A component necessary for recruitment/entry of the EVC–EVC2 complex and SMO into the cilium; pathogenic variants prevent ciliary localization and phenocopy EvC Hh defects. | Intraciliary transport (IFT‑A); Hedgehog signaling | Intraflagellar transport complex A; ciliary shaft/base | Ellis‑van Creveld–like skeletal dysplasia; Polydactyly; Cardiac malformations | (caparrosmartin2015specificvariantsin pages 1-2, caparrosmartin2015specificvariantsin pages 4-5) | https://doi.org/10.1093/hmg/ddv152 |


*Table: Compact summary table linking key genes/proteins to their mechanistic roles in Ellis‑van Creveld syndrome, relevant GO-like processes, subcellular localization, clinical phenotypes, and primary evidence (context IDs and DOI URLs) for rapid reference and knowledge‑base curation.*

Limitations
- While the 2023 study provides new regulatory insight (ubiquitin/SUMO), many foundational mechanistic data remain from 2012–2015, with fewer 2024 primary mechanistic updates specific to EvC identified here. Where possible, conclusions are triangulated across multiple sources (barbeito2023evcevc2complexstability pages 2-4, caparrosmartin2013theciliaryevcevc2 pages 7-9, caparrosmartin2013theciliaryevcevc2 pages 1-2).

Overall synthesis
EvC pathogenesis centers on a ciliary signaling module—EVC/EVC2 at the EvC zone—that licenses SMO‑dependent GLI activation. Failures in complex assembly, targeting (EFCAB7–IQCE), or ciliary entry (WDR35/IFT‑A) attenuate Hh outputs in cartilage and heart, yielding the characteristic skeletal dysplasia and AV canal/common atrium. Post‑translational control by ubiquitination/SUMOylation further tunes complex stability and localization, presenting emerging mechanistic points that may inform future diagnostic assays or therapeutic hypotheses (caparrosmartin2013theciliaryevcevc2 pages 1-2, barbeito2023evcevc2complexstability pages 2-4, caparrosmartin2013theciliaryevcevc2 pages 7-9, caparrosmartin2015specificvariantsin pages 1-2, piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20).

References

1. (caparrosmartin2013theciliaryevcevc2 pages 1-2): Jose A. Caparrós-Martín, María Valencia, Edel Reytor, María Pacheco, Margarita Fernandez, Antonio Perez-Aytes, Esther Gean, Pablo Lapunzina, Heiko Peters, Judith A. Goodship, and Victor L. Ruiz-Perez. The ciliary evc/evc2 complex interacts with smo and controls hedgehog pathway activity in chondrocytes by regulating sufu/gli3 dissociation and gli3 trafficking in primary cilia. Human Molecular Genetics, 22:124-139, Oct 2013. URL: https://doi.org/10.1093/hmg/dds409, doi:10.1093/hmg/dds409. This article has 134 citations and is from a domain leading peer-reviewed journal.

2. (caparrosmartin2013theciliaryevcevc2 pages 7-9): Jose A. Caparrós-Martín, María Valencia, Edel Reytor, María Pacheco, Margarita Fernandez, Antonio Perez-Aytes, Esther Gean, Pablo Lapunzina, Heiko Peters, Judith A. Goodship, and Victor L. Ruiz-Perez. The ciliary evc/evc2 complex interacts with smo and controls hedgehog pathway activity in chondrocytes by regulating sufu/gli3 dissociation and gli3 trafficking in primary cilia. Human Molecular Genetics, 22:124-139, Oct 2013. URL: https://doi.org/10.1093/hmg/dds409, doi:10.1093/hmg/dds409. This article has 134 citations and is from a domain leading peer-reviewed journal.

3. (caparrosmartin2015specificvariantsin pages 1-2): José A. Caparrós-Martín, Alessandro De Luca, François Cartault, Mona Aglan, Samia Temtamy, Ghada A. Otaify, Mennat Mehrez, María Valencia, Laura Vázquez, Jean-Luc Alessandri, Julián Nevado, Inmaculada Rueda-Arenas, Karen E. Heath, Maria Cristina Digilio, Bruno Dallapiccola, Judith A. Goodship, Pleasantine Mill, Pablo Lapunzina, and Victor L. Ruiz-Perez. Specific variants in wdr35 cause a distinctive form of ellis-van creveld syndrome by disrupting the recruitment of the evc complex and smo into the cilium. Human molecular genetics, 24 14:4126-37, Apr 2015. URL: https://doi.org/10.1093/hmg/ddv152, doi:10.1093/hmg/ddv152. This article has 70 citations and is from a domain leading peer-reviewed journal.

4. (piceci‐sparascio2020commonatriumatrioventricularcanal pages 16-20): Francesca Piceci‐Sparascio, Adrian Palencia‐Campos, Patricia Soto‐Bielicka, Angela D'Anzi, Valentina Guida, Jessica Rosati, Jose A. Caparros‐Martin, Isabella Torrente, M. Cecilia D'Asdia, Paolo Versacci, Silvana Briuglia, Pablo Lapunzina, Marco Tartaglia, Bruno Marino, M. Cristina Digilio, Victor L. Ruiz‐Perez, and Alessandro De Luca. Common atrium/atrioventricular canal defect and postaxial polydactyly: a mild clinical subtype of ellis‐van creveld syndrome caused by hypomorphic mutations in the <i>evc</i> gene. Human Mutation, 41:2087-2093, Oct 2020. URL: https://doi.org/10.1002/humu.24112, doi:10.1002/humu.24112. This article has 11 citations and is from a domain leading peer-reviewed journal.

5. (barbeito2023evcevc2complexstability pages 2-4): Pablo Barbeito, Raquel Martin-Morales, Adrian Palencia-Campos, Juan Cerrolaza, Celia Rivas-Santos, Leticia Gallego-Colastra, Jose Antonio Caparros-Martin, Carolina Martin-Bravo, Ana Martin-Hurtado, Laura Sánchez-Bellver, Gemma Marfany, Victor L. Ruiz-Perez, and Francesc R. Garcia-Gonzalo. Evc-evc2 complex stability and ciliary targeting are regulated by modification with ubiquitin and sumo. Frontiers in Cell and Developmental Biology, Jul 2023. URL: https://doi.org/10.3389/fcell.2023.1190258, doi:10.3389/fcell.2023.1190258. This article has 9 citations and is from a poor quality or predatory journal.

6. (louie2020molecularandcellular pages 3-5): Ke’ale W. Louie, Yuji Mishina, and Honghao Zhang. Molecular and cellular pathogenesis of ellis-van creveld syndrome: lessons from targeted and natural mutations in animal models. Journal of Developmental Biology, 8:25, Oct 2020. URL: https://doi.org/10.3390/jdb8040025, doi:10.3390/jdb8040025. This article has 29 citations and is from a poor quality or predatory journal.

7. (caparrosmartin2015specificvariantsin pages 4-5): José A. Caparrós-Martín, Alessandro De Luca, François Cartault, Mona Aglan, Samia Temtamy, Ghada A. Otaify, Mennat Mehrez, María Valencia, Laura Vázquez, Jean-Luc Alessandri, Julián Nevado, Inmaculada Rueda-Arenas, Karen E. Heath, Maria Cristina Digilio, Bruno Dallapiccola, Judith A. Goodship, Pleasantine Mill, Pablo Lapunzina, and Victor L. Ruiz-Perez. Specific variants in wdr35 cause a distinctive form of ellis-van creveld syndrome by disrupting the recruitment of the evc complex and smo into the cilium. Human molecular genetics, 24 14:4126-37, Apr 2015. URL: https://doi.org/10.1093/hmg/ddv152, doi:10.1093/hmg/ddv152. This article has 70 citations and is from a domain leading peer-reviewed journal.

8. (barbeito2023evcevc2complexstability pages 1-2): Pablo Barbeito, Raquel Martin-Morales, Adrian Palencia-Campos, Juan Cerrolaza, Celia Rivas-Santos, Leticia Gallego-Colastra, Jose Antonio Caparros-Martin, Carolina Martin-Bravo, Ana Martin-Hurtado, Laura Sánchez-Bellver, Gemma Marfany, Victor L. Ruiz-Perez, and Francesc R. Garcia-Gonzalo. Evc-evc2 complex stability and ciliary targeting are regulated by modification with ubiquitin and sumo. Frontiers in Cell and Developmental Biology, Jul 2023. URL: https://doi.org/10.3389/fcell.2023.1190258, doi:10.3389/fcell.2023.1190258. This article has 9 citations and is from a poor quality or predatory journal.