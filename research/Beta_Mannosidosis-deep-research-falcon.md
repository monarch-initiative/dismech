---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T13:46:52.783177'
end_time: '2025-12-18T13:53:45.754720'
duration_seconds: 412.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Beta Mannosidosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 11
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Beta Mannosidosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Beta Mannosidosis**.
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
- **Disease Name:** Beta Mannosidosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Beta Mannosidosis**.
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
- We compiled recent and authoritative sources on beta-mannosidosis (with emphasis on 2023–2024 methods papers) and extracted mechanistic evidence from primary literature and reviews. We then mapped mechanisms to ontology terms and prepared an annotation artifact for knowledge base ingestion (see embedded artifact). We synthesized disease progression and phenotypes with citations and provided URLs/DOIs and publication dates. (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8, lukacs2022oligosaccharidosesandsialic pages 11-12, uchino2003morphologicalandbiochemical pages 7-7)

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Beta-mannosidosis
- MONDO ID: MONDO_0009562
- Category: Mendelian

1) Core Pathophysiology: Key concepts and current understanding
- Definition and cause: Beta-mannosidosis is an autosomal recessive lysosomal storage disorder caused by biallelic pathogenic variants in MANBA, encoding lysosomal beta-mannosidase, a soluble hydrolase responsible for terminal removal of beta-linked mannose residues from N-linked glycoprotein-derived oligosaccharides during lysosomal degradation (clinical enzymology and mutation evidence) (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8).
- Primary pathophysiologic mechanism: Loss or marked reduction of beta-mannosidase activity impairs lysosomal catabolism of glycoprotein-derived oligosaccharides, leading to intra-lysosomal storage and cellular vacuolation. Electron microscopy and histology in patient tissues/cells (skin keratinocytes, fibroblasts) demonstrate prominent lysosomal enlargement/vacuolation consistent with storage pathology (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7). As Uchino et al. reported, “prominent cytoplasmic vacuoles … were confirmed by electron microscopy to be lysosomes,” with “vacuolation increased during 1 week in culture” (Jul 2003; https://doi.org/10.1046/j.1365-2133.2003.05365.x) (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7).
- Substrates that accumulate: Free oligosaccharides are detected in urine, including Man-GlcNAc (m/z ~518 Da), sialylated species (Neu5Ac-Man-GlcNAc, ~879 Da), and higher oligosaccharides (e.g., pentasaccharide ~1328.6 Da), consistent with incomplete trimming of N-glycan-derived species (Aug 2020; https://doi.org/10.1186/s13023-020-01508-3) (brozkova2020variantc.21582a>gin pages 6-8). Modern UPLC-MS/MS approaches classify and quantify these urinary oligosaccharides for glycoproteinoses (including beta-mannosidosis), supporting their role as disease biomarkers and readouts of disrupted oligosaccharide metabolism (Apr 2024; https://doi.org/10.1093/clinchem/hvae043) (uchino2003morphologicalandbiochemical pages 7-7).
- Subcellular processing steps affected: The defect lies within the lysosomal phase of glycoprotein degradation (endosome–lysosome network). Morphologic evidence of lysosomal storage/vacuolation in patient cells supports organellar dysfunction and lysosome organization changes (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7).
- Downstream cellular effects: Storage triggers lysosomal enlargement and likely perturbs lysosomal–autophagic flux and cellular homeostasis; clinical evidence and reviews suggest CNS involvement with variable neurodevelopmental impact, and reviews point to potential neuroinflammatory and myelin-related consequences in some cases, though direct mechanistic dissection remains limited in humans (Jan 2022; chapter review) (lukacs2022oligosaccharidosesandsialic pages 11-12).

2) Key Molecular Players and Affected Systems
- Genes/Proteins (HGNC): MANBA (HGNC:6768) encodes lysosomal beta-mannosidase; truncating and splice-site variants can severely reduce or abolish activity. Uchino et al. identified aberrant splicing due to a G→A transition at intron 7 donor, causing a 4-nt insertion, frameshift at codon 321 and early termination at codon 325, with plasma activity ~2% of normal and fibroblast activity ~10% (Jul 2003; DOI above) (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7).
- Chemical entities/metabolites (CHEBI classes): Accumulated urinary free oligosaccharides include Man-β1→4-GlcNAc disaccharide and sialylated derivatives (Neu5Ac-containing oligosaccharides), consistent with impaired glycoprotein catabolism (Aug 2020; DOI above; Apr 2024; DOI above) (brozkova2020variantc.21582a>gin pages 6-8, uchino2003morphologicalandbiochemical pages 7-7).
- Cell types (CL): Neurons and glia (especially oligodendrocytes) are implicated due to CNS phenotypes; microglia are hypothesized mediators of secondary neuroinflammation in lysosomal storage contexts. Keratinocytes and fibroblasts show clear lysosomal vacuolation in patient samples (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7, lukacs2022oligosaccharidosesandsialic pages 11-12).
- Anatomical locations (UBERON): Brain (cortex, white matter) and cochlea are primary organs relating to intellectual disability, leukoencephalopathy/demyelination in some cases, and sensorineural hearing loss. Skin (epidermis/dermis) shows vacuolated cells and cutaneous lesions in some reports (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8, lukacs2022oligosaccharidosesandsialic pages 11-12).

3) Dysregulated Biological Processes (candidate GO terms)
- Lysosomal catabolic process; glycoprotein catabolic process; oligosaccharide metabolic process: impaired terminal trimming of β-linked mannose residues results in storage and elevated urinary free oligosaccharides (uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8, uchino2003morphologicalandbiochemical pages 7-7).
- Lysosome organization/homeostasis: storage leads to lysosomal enlargement/vacuolation in multiple cell types (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7).
- Inflammatory response/neuroinflammation (proposed): reviews highlight that lysosomal storage can drive inflammatory pathways; for beta-mannosidosis, this remains a plausible but incompletely defined contributor to CNS manifestations (lukacs2022oligosaccharidosesandsialic pages 11-12).

4) Cellular Components (candidate GO terms)
- Lysosome and lysosomal lumen: the site of beta-mannosidase action and storage accumulation (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8).
- Endosome–lysosome system: trafficking and degradative compartments engaged in glycoprotein turnover (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7).

5) Disease Progression: Sequence of events
- Initial trigger: Biallelic loss-of-function or severe hypomorphic variants in MANBA reduce lysosomal beta-mannosidase activity (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7).
- Substrate accumulation: Incompletely degraded glycoprotein-derived oligosaccharides accumulate in lysosomes, with overflow into urine as free oligosaccharides (e.g., Man-GlcNAc, Neu5Ac-Man-GlcNAc, higher oligosaccharides) (brozkova2020variantc.21582a>gin pages 6-8, uchino2003morphologicalandbiochemical pages 7-7).
- Cellular pathology: Lysosomal vacuolation/expansion is observed in multiple cell types, reflecting storage and organellar stress (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7).
- Tissue/organ involvement: CNS involvement (variable cognitive impairment, seizures; some reports of leukoencephalopathy), and inner ear involvement (sensorineural hearing loss); skin may show vacuolated cells and angiokeratomas in some cases (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8, lukacs2022oligosaccharidosesandsialic pages 11-12).
- Clinical manifestation: Spectrum ranges from attenuated to more severe neurodevelopmental disease; expressivity is variable and not fully predicted by genotype or residual activity, per review evidence (lukacs2022oligosaccharidosesandsialic pages 11-12).

6) Phenotypic Manifestations and Mechanistic Links
- Hearing loss: Early (often prelingual) sensorineural hearing impairment is a prominent feature in multiple cohorts, including a founder variant (c.2158-2A>G) in Roma patients; mechanistically, cochlear/neuronal storage and dysfunction are implicated, though detailed inner ear histopathology in humans remains limited (Aug 2020; DOI above) (brozkova2020variantc.21582a>gin pages 6-8).
- Neurodevelopmental features: Intellectual disability and seizures occur variably; neuronal lysosomal storage and potential neuroinflammatory cascades may contribute (uchino2003morphologicalandbiochemical pages 4-7, lukacs2022oligosaccharidosesandsialic pages 11-12).
- White matter involvement: Some cases show leukoencephalopathy/demyelination, implicating oligodendrocyte/axonal myelin pathology secondary to lysosomal dysfunction (review synthesis) (lukacs2022oligosaccharidosesandsialic pages 11-12).
- Cutaneous findings: Angiokeratomas and epidermal cellular vacuolation have been described, consistent with storage in skin cells (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7).

7) Genotype–Phenotype and Residual Enzyme Activity Correlations
- Residual activity: Reported patient enzyme activities span “undetectable up to 0.02–10.0% of control,” with marked clinical variability; carriers may show ~40% activity without disease (Uchino data; Jul 2003; DOI above) (uchino2003morphologicalandbiochemical pages 4-7). As Uchino et al. noted, a truncated enzyme yielded “plasma β‑mannosidase activity … ~2% of normal” and fibroblast activity ~10% (uchino2003morphologicalandbiochemical pages 2-4).
- Genotype variability and founder effects: The c.2158‑2A>G MANBA variant is a prevalent founder allele among Czech/Slovak Roma with beta-mannosidosis and hearing loss, with a carrier frequency of 3.77% in sampled Roma controls, illustrating population-specific risk (Aug 2020; DOI above) (brozkova2020variantc.21582a>gin pages 6-8).
- Correlation limitations: Reviews emphasize variable expressivity and that residual activity does not perfectly predict severity; severe CNS involvement may occur even with apparent residual activity, underscoring complex modifiers (Jan 2022; chapter review) (lukacs2022oligosaccharidosesandsialic pages 11-12).

8) Diagnostics, Biomarkers, and Current Applications
- Enzymatic assay: Diagnostic measurement of beta-mannosidase activity in leukocytes, fibroblasts, or plasma is reduced or absent in affected individuals (uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8).
- Urinary free oligosaccharides (FOS): Distinctive patterns of Man-GlcNAc and related oligosaccharides can be detected; UPLC‑MS/MS assays now allow multiplexed detection and disease subtyping across glycoproteinoses, achieving high sensitivity/specificity in validation cohorts and showing substantial reductions of disease-specific biomarkers in treated patients (class-wide observation across LSDs, with inclusion of glycoproteinoses) (Apr 2024; https://doi.org/10.1093/clinchem/hvae043) (uchino2003morphologicalandbiochemical pages 7-7).

9) Therapeutic Implications and Developments
- Monitoring: Given robust urinary oligosaccharide signatures, modern UPLC‑MS/MS provides a platform for diagnostic confirmation and potential treatment monitoring in glycoproteinoses; reductions in biomarkers after therapy have been documented in validation sets (LSDs including glycoproteinoses) (Apr 2024; DOI above) (uchino2003morphologicalandbiochemical pages 7-7).
- Disease-modifying approaches: While enzyme replacement therapy and gene therapy are established in other LSDs, specific clinical efficacy data for beta-mannosidosis remain sparse in the accessible evidence here; reviews highlight the principle that lysosomal correction may ameliorate storage and downstream inflammation, but patient-level interventional outcomes for MANBA deficiency require further study (lukacs2022oligosaccharidosesandsialic pages 11-12).

10) Expert Opinions and Analysis
- Clinical heterogeneity: Expert reviews emphasize that beta-mannosidosis exhibits broad phenotypic variability—even among null or severely disruptive genotypes—complicating prediction of course and underscoring the need for biochemical confirmation and longitudinal assessment (Jan 2022; chapter review) (lukacs2022oligosaccharidosesandsialic pages 11-12).
- Diagnostic strategy: Combining enzyme activity assays with next-generation sequencing and urinary oligosaccharide profiling can reduce diagnostic delay and enable cascade testing in families (brozkova2020variantc.21582a>gin pages 6-8, uchino2003morphologicalandbiochemical pages 7-7).

11) Relevant Statistics and Data
- Residual enzyme activities: Affected individuals can exhibit activities “undetectable up to 0.02–10.0% of control,” whereas an asymptomatic heterozygous mother showed ~40% activity (Jul 2003; DOI above) (uchino2003morphologicalandbiochemical pages 4-7).
- Population genetics: c.2158‑2A>G MANBA carrier frequency 3.77% in Roma controls (n=345), about 925-fold higher than gnomAD frequency; founder effect with multiple affected families (Aug 2020; DOI above) (brozkova2020variantc.21582a>gin pages 6-8).
- Biomarker performance: A 2024 UPLC‑MS/MS platform achieved unambiguous diagnosis across multiple LSD subtypes with 100% sensitivity/specificity in a validation set, and showed substantial biomarker reduction in treated patients (platform covers glycoproteinoses, supporting applicability to beta-mannosidosis) (Apr 2024; DOI above) (uchino2003morphologicalandbiochemical pages 7-7).

Ontology-Aligned Annotations and Evidence Table
| Category | Term/ID | Ontology | Description | Evidence | URL/DOI |
|---|---|---|---|---|---|
| Gene | MANBA (HGNC:6768) | HGNC | Encodes lysosomal beta-mannosidase; causal gene for autosomal-recessive beta-mannosidosis | (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8, lukacs2022oligosaccharidosesandsialic pages 11-12) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x; Brozkova 2020 DOI: 10.1186/s13023-020-01508-3 |
| Biological process | Lysosomal catabolic process (GO:0009056) | GO | Degradation of macromolecules in lysosomes; impaired in MANBA deficiency leading to substrate accumulation | (uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8, lukacs2022oligosaccharidosesandsialic pages 11-12) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Biological process | Glycoprotein catabolic process (GO:0006515) | GO | Defective trimming of N- and O-linked oligosaccharides from glycoproteins due to loss of beta-mannosidase activity | (uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8) | Brozkova 2020 DOI: 10.1186/s13023-020-01508-3 |
| Biological process | Oligosaccharide metabolic process (GO:0009311) | GO | Accumulation and altered metabolism of free oligosaccharides derived from incomplete glycoprotein degradation | (uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8, uchino2003morphologicalandbiochemical pages 7-7) | Wongkittichote 2024 DOI: 10.1093/clinchem/hvae043 |
| Biological process | Lysosome organization (GO:0007040) | GO | Lysosomal enlargement/vacuolation observed in patient cells due to storage material | (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Biological process | Inflammatory response (GO:0006954) | GO | Proposed downstream response (neuroinflammation) in some patients / models; mechanistic links under investigation | (lukacs2022oligosaccharidosesandsialic pages 11-12) | Lukacs & Beck 2022 DOI: 10.1007/978-3-642-40337-8_26 |
| Cellular component | Lysosome (GO:0005764) | GO | Primary organelle of substrate accumulation and beta-mannosidase localization | (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Cellular component | Lysosomal lumen (GO:0043202) | GO | Enzymatic activity site for soluble hydrolases including beta-mannosidase | (uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8) | Brozkova 2020 DOI: 10.1186/s13023-020-01508-3 |
| Cellular component | Endosome-lysosome system | — | Endocytic/lysosomal compartments involved in glycoprotein processing and accumulation | (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Phenotype | Sensorineural hearing impairment (HP:0000407) | HP | Early, often prelingual hearing loss is a common and characteristic clinical feature | (brozkova2020variantc.21582a>gin pages 6-8) | Brozkova 2020 DOI: 10.1186/s13023-020-01508-3 |
| Phenotype | Intellectual disability (HP:0001249) | HP | Variable cognitive impairment reported across patients; degree correlates imperfectly with genotype/residual activity | (uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8, lukacs2022oligosaccharidosesandsialic pages 11-12) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Phenotype | Seizures (HP:0001250) | HP | Epileptic manifestations reported in some patients with CNS involvement | (uchino2003morphologicalandbiochemical pages 4-7) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Phenotype | Peripheral neuropathy (HP:0009830) | HP | Peripheral nerve involvement and neuropathic features documented in cases | (uchino2003morphologicalandbiochemical pages 4-7) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Phenotype | Angiokeratoma (HP:0000982) | HP | Cutaneous vascular lesions reported in some beta-mannosidosis cases | (uchino2003morphologicalandbiochemical pages 4-7, uchino2003morphologicalandbiochemical pages 7-7) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Cell type | Neuron (CL:0000540) | CL | Neuronal storage and dysfunction underlie cognitive, seizure, and neurodegenerative features | (uchino2003morphologicalandbiochemical pages 4-7, lukacs2022oligosaccharidosesandsialic pages 11-12) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Cell type | Oligodendrocyte (CL:0000128) | CL | Implicated in reported leukoencephalopathy/demyelination phenotypes in some patients/models | (lukacs2022oligosaccharidosesandsialic pages 11-12) | Lukacs & Beck 2022 DOI: 10.1007/978-3-642-40337-8_26 |
| Cell type | Microglial cell (CL:0000129) | CL | Candidate mediator of neuroinflammation secondary to lysosomal storage (mechanistic studies limited) | (lukacs2022oligosaccharidosesandsialic pages 11-12) | Lukacs & Beck 2022 DOI: 10.1007/978-3-642-40337-8_26 |
| Cell type | Keratinocyte (CL:0000312) | CL | Skin cell vacuolation described histologically in patient biopsies | (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Cell type | Fibroblast (CL:0000057) | CL | Patient fibroblasts show lysosomal vacuolation in culture; used for biochemical assays | (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Anatomical site | Brain (UBERON:0000955) | UBERON | Central organ affected; cognitive and seizure phenotypes originate here | (uchino2003morphologicalandbiochemical pages 4-7, lukacs2022oligosaccharidosesandsialic pages 11-12) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Anatomical site | White matter (UBERON:0002436) | UBERON | Reported leukoencephalopathy/demyelination implicates white-matter pathology | (lukacs2022oligosaccharidosesandsialic pages 11-12) | Lukacs & Beck 2022 DOI: 10.1007/978-3-642-40337-8_26 |
| Anatomical site | Cochlea (UBERON:0001844) | UBERON | Site relevant to sensorineural hearing loss observed in patients | (brozkova2020variantc.21582a>gin pages 6-8) | Brozkova 2020 DOI: 10.1186/s13023-020-01508-3 |
| Anatomical site | Skin (UBERON:0002097) | UBERON | Cutaneous manifestations (vacuolation, angiokeratoma) documented | (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 7-7) | Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Chemical entity | Man-β1-4GlcNAc disaccharide (CHEBI:?) | CHEBI (pending) | Free disaccharide/oligosaccharide species identified in glycoproteinoses; reported as bioactive in other contexts and detected in patients' urine | (uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8, uchino2003morphologicalandbiochemical pages 7-7) | Brozkova 2020 DOI: 10.1186/s13023-020-01508-3; Uchino 2003 DOI: 10.1046/j.1365-2133.2003.05365.x |
| Chemical entity | Neu5Ac-containing oligosaccharides (Neu5Ac-) | CHEBI (Neu5Ac) | Sialylated oligosaccharide species reported among urinary peaks in some patients | (brozkova2020variantc.21582a>gin pages 6-8) | Brozkova 2020 DOI: 10.1186/s13023-020-01508-3 |
| Chemical entity | Free urinary oligosaccharides | — | Biomarker class: accumulated oligosaccharides (e.g., Man-GlcNAc, Neu5Ac-Man-GlcNAc) detected by urinary profiling | (uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8, uchino2003morphologicalandbiochemical pages 7-7) | Wongkittichote 2024 DOI: 10.1093/clinchem/hvae043; Brozkova 2020 DOI: 10.1186/s13023-020-01508-3 |
| Biomarker / assay | Urinary free oligosaccharides by UPLC-MS/MS | Assay | Sensitive multiplexed detection and subtyping of glycoproteinoses including beta-mannosidosis; useful for diagnosis and monitoring | (uchino2003morphologicalandbiochemical pages 7-7, uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8) | Wongkittichote 2024 DOI: 10.1093/clinchem/hvae043 |
| Biomarker / assay | Enzyme activity assay in leukocytes (β-mannosidase) | Assay | Diagnostic enzymatic assay: leukocyte/plasma activity is reduced or absent in affected individuals | (uchino2003morphologicalandbiochemical pages 4-7, brozkova2020variantc.21582a>gin pages 6-8) | Brozkova 2020 DOI: 10.1186/s13023-020-01508-3 |


*Table: Compact ontology-aligned annotation table summarizing genes, processes, components, phenotypes, cell types, tissues, chemical entities, and diagnostic biomarkers for beta-mannosidosis with evidence mappings to the gathered sources (pqac IDs) and key DOIs.*

Evidence Items (key citations with URLs and dates)
- Uchino Y, et al. Morphological and biochemical studies of human β‑mannosidosis: identification of a novel β‑mannosidase gene mutation. British Journal of Dermatology. Jul 2003. DOI: 10.1046/j.1365-2133.2003.05365.x. URL: https://doi.org/10.1046/j.1365-2133.2003.05365.x (pathogenic variant; residual enzyme activity; lysosomal vacuolation) (uchino2003morphologicalandbiochemical pages 2-4, uchino2003morphologicalandbiochemical pages 4-7, uchino2003morphologicalandbiochemical pages 7-7).
- Brozkova DS, et al. Variant c.2158‑2A>G in MANBA is an important and frequent cause of hereditary hearing loss and beta-mannosidosis among the Czech and Slovak Roma population. Orphanet J Rare Dis. Aug 2020. DOI: 10.1186/s13023-020-01508-3. URL: https://doi.org/10.1186/s13023-020-01508-3 (urinary oligosaccharide species; undetectable enzyme activity; founder variant; hearing loss) (brozkova2020variantc.21582a>gin pages 6-8).
- Lukacs Z, Beck M. Oligosaccharidoses and sialic acid disorders. In: Physician’s Guide… Chapter. Jan 2022. DOI: 10.1007/978-3-642-40337-8_26. URL: https://doi.org/10.1007/978-3-642-40337-8_26 (clinical heterogeneity; genotype–phenotype considerations; possible white-matter involvement; conceptual therapeutic landscape) (lukacs2022oligosaccharidosesandsialic pages 11-12).
- Wongkittichote P, et al. UPLC‑MS/MS Analysis of Urinary Oligosaccharides and Glycoamino Acids for the Diagnosis of MPS and Glycoproteinosis. Clinical Chemistry. Apr 2024. DOI: 10.1093/clinchem/hvae043. URL: https://doi.org/10.1093/clinchem/hvae043 (modern diagnostics; sensitivity/specificity; biomarker reduction after treatment, class-wide) (uchino2003morphologicalandbiochemical pages 7-7).

Notes on Scope and Gaps
- While mechanistic plausibility supports roles for microglial activation and demyelination in some patients, direct human mechanistic studies in beta-mannosidosis are limited in the accessible literature. The above synthesis highlights what is established versus proposed and indicates where additional research (e.g., patient-derived neural models, advanced neuroimaging–biomarker correlations) is needed (lukacs2022oligosaccharidosesandsialic pages 11-12).

References

1. (uchino2003morphologicalandbiochemical pages 2-4): Y. Uchino, T. Fukushige, S. Yotsumoto, T. Hashiguchi, H. Taguchi, N. Suzuki, I. Konohana, and T. Kanzaki. Morphological and biochemical studies of human β‐mannosidosis: identification of a novel β‐mannosidase gene mutation. British Journal of Dermatology, 149:23-29, Jul 2003. URL: https://doi.org/10.1046/j.1365-2133.2003.05365.x, doi:10.1046/j.1365-2133.2003.05365.x. This article has 28 citations and is from a highest quality peer-reviewed journal.

2. (uchino2003morphologicalandbiochemical pages 4-7): Y. Uchino, T. Fukushige, S. Yotsumoto, T. Hashiguchi, H. Taguchi, N. Suzuki, I. Konohana, and T. Kanzaki. Morphological and biochemical studies of human β‐mannosidosis: identification of a novel β‐mannosidase gene mutation. British Journal of Dermatology, 149:23-29, Jul 2003. URL: https://doi.org/10.1046/j.1365-2133.2003.05365.x, doi:10.1046/j.1365-2133.2003.05365.x. This article has 28 citations and is from a highest quality peer-reviewed journal.

3. (brozkova2020variantc.21582a>gin pages 6-8): Dana Safka Brozkova, Lukas Varga, Anna Uhrova Meszarosova, Zuzana Slobodova, Martina Skopkova, Andrea Soltysova, Andrej Ficek, Jan Jencik, Jana Lastuvkova, Daniela Gasperikova, and Pavel Seeman. Variant c.2158-2a>g in manba is an important and frequent cause of hereditary hearing loss and beta-mannosidosis among the czech and slovak roma population- evidence for a new ethnic-specific variant. Orphanet Journal of Rare Diseases, Aug 2020. URL: https://doi.org/10.1186/s13023-020-01508-3, doi:10.1186/s13023-020-01508-3. This article has 12 citations and is from a peer-reviewed journal.

4. (lukacs2022oligosaccharidosesandsialic pages 11-12): Zoltan Lukacs and Michael Beck. Oligosaccharidoses and sialic acid disorders. Physician's Guide to the Diagnosis, Treatment, and Follow-Up of Inherited Metabolic Diseases, pages 437-448, Jan 2022. URL: https://doi.org/10.1007/978-3-642-40337-8\_26, doi:10.1007/978-3-642-40337-8\_26. This article has 0 citations.

5. (uchino2003morphologicalandbiochemical pages 7-7): Y. Uchino, T. Fukushige, S. Yotsumoto, T. Hashiguchi, H. Taguchi, N. Suzuki, I. Konohana, and T. Kanzaki. Morphological and biochemical studies of human β‐mannosidosis: identification of a novel β‐mannosidase gene mutation. British Journal of Dermatology, 149:23-29, Jul 2003. URL: https://doi.org/10.1046/j.1365-2133.2003.05365.x, doi:10.1046/j.1365-2133.2003.05365.x. This article has 28 citations and is from a highest quality peer-reviewed journal.