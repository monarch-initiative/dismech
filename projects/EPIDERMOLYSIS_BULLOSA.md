# Epidermolysis Bullosa Curation Project

## Overview

Comprehensive curation of Epidermolysis Bullosa (EB) for the dismech knowledge base. EB is a group of inherited mechanobullous disorders characterized by skin and mucosal fragility due to mutations in structural proteins of the dermal-epidermal junction. The four major types are defined by the ultrastructural level of skin cleavage:

1. **EB Simplex (EBS)** — intraepidermal (within basal keratinocytes)
2. **Junctional EB (JEB)** — lamina lucida of the basement membrane zone
3. **Dystrophic EB (DEB)** — sub-lamina densa (anchoring fibrils)
4. **Kindler EB** — mixed cleavage levels (actin-ECM interface)

Each type involves distinct genes, distinct ultrastructural defects, distinct inheritance patterns, and increasingly distinct therapeutic approaches (gene therapy, protein replacement, cell therapy targets differ by type). This mirrors the pattern used for thalassemia (Alpha vs Beta as separate files) and breast cancer molecular subtypes.

## Decision: One Entity or Multiple?

### Recommendation: **Multiple files (4 major types) + umbrella file**

| Structure | Pattern | Rationale |
|-----------|---------|-----------|
| `Epidermolysis_Bullosa.yaml` | Umbrella (like `Diabetes_Mellitus.yaml`) | Shared concepts: wound care, BMZ biology, diagnostic workup, classification system |
| `Epidermolysis_Bullosa_Simplex.yaml` | Major type | KRT5/KRT14/PLEC — keratin cytoskeleton |
| `Junctional_Epidermolysis_Bullosa.yaml` | Major type | LAMB3/LAMA3/LAMC2/COL17A1 — laminin-332 & hemidesmosomes |
| `Dystrophic_Epidermolysis_Bullosa.yaml` | Major type | COL7A1 — type VII collagen / anchoring fibrils |
| `Kindler_Epidermolysis_Bullosa.yaml` | Major type | FERMT1 — kindlin-1 / focal adhesions |

### Why split rather than one file?

- **Different genes at different structural layers**: EBS = keratins, JEB = laminins/integrins, DEB = collagen VII, Kindler = kindlin-1. These are not allelic variants of one gene — they're defects in entirely different protein complexes.
- **Different inheritance**: EBS is mostly autosomal dominant, JEB is autosomal recessive, DEB can be either (DDEB vs RDEB with very different outcomes), Kindler is autosomal recessive.
- **Different complications**: RDEB carries a uniquely high risk of aggressive squamous cell carcinoma; JEB-severe (Herlitz) is often lethal in infancy; EBS is generally non-scarring. These demand separate pathophysiology sections.
- **Different therapeutic pipelines**: Gene therapy approaches are type-specific (COL7A1 for DEB, LAMB3 for JEB). Beremagene geperpavec (Vyjuvek) is approved specifically for DEB.
- **Precedent in KB**: Alpha/Beta Thalassemia, ER+/HER2+/TNBC breast cancer, Type 1/Type 2 Diabetes all use separate files for mechanistically distinct subtypes.

### Why an umbrella file?

- Shared diagnostic approach (skin biopsy → IF mapping → genetic testing)
- Shared supportive care principles (wound management, infection prevention, nutrition, pain)
- Common classification framework (2020 international EB consensus reclassification)
- Historical context and epidemiology across all types
- MONDO:0019209 (Epidermolysis bullosa) as the grouping term

### Within-file `has_subtypes` usage

Each major type file will use `has_subtypes` for severity/phenotypic variants:

- **EBS**: Localized (Weber-Cockayne), Intermediate (Köbner), Severe (Dowling-Meara), with muscular dystrophy (PLEC), autosomal recessive EBS
- **JEB**: Severe (Herlitz, LAMB3 null) vs Intermediate (non-Herlitz, COL17A1 hypomorphic) vs with pyloric atresia (ITGA6/ITGB4)
- **DEB**: Dominant DEB (DDEB, mild) vs Recessive DEB severe generalized (RDEB-sev gen) vs RDEB intermediate vs RDEB inversa
- **Kindler**: Generally one main phenotype with variable severity; poikiloderma + photosensitivity distinguish it

## Key Genes and Proteins

| Gene | Protein | EB Type | Structural Role |
|------|---------|---------|-----------------|
| KRT5 | Keratin 5 | EBS | Basal keratinocyte intermediate filament |
| KRT14 | Keratin 14 | EBS | Basal keratinocyte intermediate filament |
| PLEC | Plectin | EBS-MD | Hemidesmosome-cytoskeleton linker |
| DST | Dystonin/BPAG1 | EBS | Hemidesmosome inner plaque |
| LAMB3 | Laminin β3 | JEB | Laminin-332 subunit (anchoring filaments) |
| LAMA3 | Laminin α3 | JEB | Laminin-332 subunit |
| LAMC2 | Laminin γ2 | JEB | Laminin-332 subunit |
| COL17A1 | Type XVII collagen (BP180) | JEB | Hemidesmosome transmembrane component |
| ITGA6 | Integrin α6 | JEB-PA | Hemidesmosome (with pyloric atresia) |
| ITGB4 | Integrin β4 | JEB-PA | Hemidesmosome (with pyloric atresia) |
| COL7A1 | Type VII collagen | DEB | Anchoring fibrils (sub-lamina densa) |
| FERMT1 | Kindlin-1 | Kindler | Focal adhesion-actin linkage |

## Therapeutics Landscape (Major Motivation for Curation)

EB is a frontier for genetic medicine — gene therapy, cell therapy, and protein replacement are all in active development:

| Therapy | Type | Target | Status |
|---------|------|--------|--------|
| Beremagene geperpavec (Vyjuvek) | HSV-1 gene therapy (topical) | COL7A1 / DEB | **FDA approved 2023** |
| EB-101 (autologous gene-corrected skin grafts) | Ex vivo gene therapy | LAMB3 / JEB | Phase III |
| PTR-01 (recombinant COL7) | Protein replacement | DEB | Phase II/III |
| KB103 (COL7A1 lentiviral) | Ex vivo gene therapy | DEB | Phase I/II |
| Rigosertib (topical) | SCC prevention (PLK/PI3K) | RDEB-SCC | Phase II |
| Gentamicin (topical/IV) | Readthrough of nonsense mutations | DEB/JEB (PTC) | Clinical trials |
| BMT/HSCT | Bone marrow transplant | RDEB | Investigational |
| Losartan | Anti-fibrotic (TGF-β) | DEB | Phase II |

## Curation Plan

### Phase 1: Umbrella + DEB (Highest Priority)

DEB is the most therapeutically active (Vyjuvek approval) and mechanistically rich (fibrosis → SCC pathway).

- [ ] Create `Epidermolysis_Bullosa.yaml` — umbrella with shared concepts, BMZ biology, classification
- [ ] Create `Dystrophic_Epidermolysis_Bullosa.yaml` — COL7A1, anchoring fibrils, DDEB/RDEB subtypes, SCC risk, Vyjuvek

### Phase 2: JEB (High Priority)

JEB-Herlitz is paradigmatic for understanding laminin-332 biology and lethal skin disease.

- [ ] Create `Junctional_Epidermolysis_Bullosa.yaml` — LAMB3/LAMA3/LAMC2, Herlitz vs non-Herlitz, pyloric atresia variant

### Phase 3: EBS (Moderate Priority)

Most common but generally mildest. Interesting keratin biology and PLEC-muscular dystrophy link.

- [ ] Create `Epidermolysis_Bullosa_Simplex.yaml` — KRT5/KRT14, dominant negative keratins, PLEC-MD variant

### Phase 4: Kindler EB (Lower Priority)

Rarest type. Interesting actin biology and photosensitivity mechanism.

- [ ] Create `Kindler_Epidermolysis_Bullosa.yaml` — FERMT1, focal adhesions, poikiloderma, photosensitivity

## Cross-Cutting Themes to Capture

- **Basement membrane zone ultrastructure**: The BMZ has defined layers (hemidesmosomes → lamina lucida → lamina densa → sub-lamina densa), and each EB type maps to a specific layer
- **Genotype-phenotype correlation**: Null mutations → severe, missense → milder across all types
- **Dominant negative vs haploinsufficiency**: EBS keratins and DEB collagen VII illustrate both mechanisms in the same gene
- **Cancer predisposition in RDEB**: Chronic wounds → fibrosis → aggressive SCC is a distinctive complication pathway
- **Wound healing biology**: EB is a natural model for understanding skin repair
- **Gene therapy paradigm**: EB represents one of the most successful applications of topical gene therapy (Vyjuvek)

## Relevant MONDO Terms

| Term | ID | Use |
|------|----|----|
| Epidermolysis bullosa | MONDO:0019209 | Umbrella |
| Epidermolysis bullosa simplex | MONDO:0017255 | EBS file |
| Junctional epidermolysis bullosa | MONDO:0015562 | JEB file |
| Dystrophic epidermolysis bullosa | MONDO:0015563 | DEB file |
| Kindler epidermolysis bullosa | MONDO:0017263 | Kindler file |

## Key References (Starting Points)

- Has C, et al. (2020) "Consensus reclassification of inherited epidermolysis bullosa" — PMID:32017015
- Bardhan A, et al. (2020) "Epidermolysis bullosa" — Nature Reviews Disease Primers — PMID:32943623
- Guide SV, et al. (2022) "Beremagene geperpavec for dystrophic EB" — PMID:36417996 (Vyjuvek phase III)
- Mavilio F, et al. (2006) "Correction of junctional EB by transplantation of genetically modified epidermal stem cells" — PMID:16971830
- Hirsch T, et al. (2017) "Regeneration of the entire human epidermis using transgenic stem cells" — PMID:29115066
- Fine JD, et al. (2009) "Inherited EB and risk of death from SCC" — PMID:19439728
