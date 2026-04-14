---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-13T04:10:00Z'
end_time: '2026-04-13T05:40:00Z'
duration_seconds: 5400.0
citation_count: 9
notes: >-
  Manual cancer-focused curation for issue #1206. Modeling was adjusted to
  follow the cancer curation guidance from issue #1198 / Wilms tumor: MONDO-first
  disease anchor, routine disease-level NCIT mapping, flat subtype axes, and no
  separate dismech pages for ontology-grounded histologic facets.
---

## Question

Provide a disease-level mechanistic and clinical review of thymoma suitable for
high-quality dismech cancer curation, including ontology grounding strategy,
subtype axes, core pathophysiology, hallmark phenotypes, and treatment
implications.

## Output

# Thymoma: curation-oriented mechanistic summary

## Modeling decisions applied from issue #1198

- The dismech curation unit is the **disease-level mechanism graph**, not every oncology ontology subclass. Thymoma therefore remains one disease entry rather than separate pages for WHO types A, AB, B1, B2, B3, or invasion-status variants.
- `disease_term` stays **MONDO-first** as `MONDO:0006456` (thymoma).
- The entry should also carry a **disease-level NCIT mapping** to `NCIT:C3411` (Thymoma), because NCIT is the more oncology-native coding system for downstream cancer interoperability.
- Subtypes are best represented as **flat facet axes**. For thymoma, the highest-yield axes are:
  - `histological_pattern`: Type A (`NCIT:C6454`), Type AB (`NCIT:C6885`), Type B1 (`NCIT:C6887`), Type B2 (`NCIT:C6888`), Type B3 (`NCIT:C7997`)
  - `invasion_status`: Encapsulated thymoma (`NCIT:C7386`), invasive thymoma (`NCIT:C7904`)
- The NCIT-grounded subtype terms are **ontology grounding only**. They should not imply separate dismech pages or a “Not Yet Curated” renderer state.

## Disease overview

Thymoma is a thymic epithelial tumor of the anterior mediastinum whose biology is unusual among solid tumors because the neoplasm also distorts thymic T-cell selection. The two dominant disease-level themes are therefore:

1. **Tumor-cell intrinsic oncogenesis**, especially the GTF2I-enriched, low-mutation-burden program of indolent type A/AB thymoma.
2. **Tumor-microenvironment immune dysfunction**, in which abnormal thymic epithelial architecture impairs central tolerance and promotes paraneoplastic autoimmunity.

## Subtype biology

- **Type A / Type AB thymoma**: indolent histotypes with the strongest GTF2I enrichment. PMID:24974848 reports that GTF2I mutation is detected in 82% of type A and 74% of type AB thymomas.
- **Type B1 / Type B2 thymoma**: more cortical, lymphocyte-rich histotypes with increasing invasiveness and myasthenia gravis association.
- **Type B3 thymoma**: epithelial-predominant thymoma with substantially greater local invasion and worse disease-free survival. PMID:15063231 reports a monotonic increase in neighboring-organ invasion across A → AB → B1 → B2 → B3.
- **Encapsulated vs invasive thymoma**: a separate invasion-status axis is useful because clinical behavior spans indolent, organ-confined disease to locally invasive or metastatic disease even within the same broad disease entry (PMID:20207296).

## Core mechanisms

### 1. GTF2I-driven thymic epithelial transformation

- PMID:24974848: “We analyzed 28 thymic epithelial tumors (TETs) using next-generation sequencing and identified a missense mutation ... in GTF2I at high frequency in type A thymomas, a relatively indolent subtype.”
- PMID:32034314: “Our findings identify GTF2I mutation as a new oncogenic driver that is responsible for transformation of thymic epithelial cells.”

Interpretation for YAML: this supports a disease node centered on thymic epithelial transformation, with subtype restriction to type A/AB thymoma and downstream linkage to proliferative and metabolic programs.

### 2. Metabolic stress adaptation downstream of mutant GTF2I

- PMID:32034314: “Gtf2i L424H knockin cells exhibited cell transformation, aneuploidy, and increase tumor growth and survival under glucose deprivation or DNA damage.”
- PMID:32034314: “Gtf2i mutation also increased the expression of several glycolytic enzymes, cyclooxygenase-2, and caused modifications of lipid metabolism.”

Interpretation for YAML: metabolic rewiring is worth its own atomic node rather than being bundled into the transformation node.

### 3. Reduced MHC class II antigen presentation

- PMID:18567864: “expression levels of class II major histocompatibility complex (MHCII) genes are variably decreased in thymomas, most prominently in histological WHO types A and AB”

Interpretation for YAML: this directly supports an atomic node for reduced antigen presentation via MHC class II, especially in type A/AB thymoma.

### 4. AIRE loss in thymic epithelial cells

- PMID:18567864: “expression of the autoimmune regulator (AIRE) gene is absent from approximately 95% of thymomas.”

Interpretation for YAML: AIRE loss should remain separate from reduced MHC II expression because both are central-tolerance defects but represent distinct molecular lesions.

### 5. Central tolerance failure with autoreactive T-cell escape

- PMID:41098393: “Since thymomas are mainly composed of the cortex, with few medullae, MG may be caused by immature thymoma-derived T cells that fail to undergo negative selection and have not yet acquired sufficient self-tolerance.”
- PMID:18567864: “Generation of autoreactive CD4(+) effector T cells and defective production of regulatory CD4(+) T cells inside thymomas contribute to the development of myasthenia gravis (MG) in >90% of MG(+) thymomas.”

Interpretation for YAML: negative-selection failure, autoreactive effector-T-cell generation, and defective Treg production belong in a linked but still atomic disease mechanism chain.

### 6. Neuromuscular autoantigen niche in MG-associated thymoma

- PMID:41098393: “we identified neuromuscular medullary thymic epithelial cells (nmTECs) as neuromuscular antigen-expressing cell populations.”
- PMID:41098393: “We observed spatial nmTEC colocalization and an immune niche, inferring an interaction and suggesting a pathological role of nmTECs in MG.”

Interpretation for YAML: this is a more specific downstream mechanism that helps explain why myasthenia gravis is the dominant autoimmune phenotype.

## Hallmark phenotype profile

- **Anterior mediastinal mass**: characteristic anatomic presentation (PMID:37761349).
- **Myasthenia gravis**: dominant autoimmune phenotype (PMID:20207296).
- **Pure red cell aplasia**: recurrent hematologic autoimmune complication (PMID:40983285).
- **Good syndrome** and **recurrent infections**: thymoma-associated immunodeficiency phenotype with hypogammaglobulinemia and infection susceptibility (PMID:39180607).

## Treatment implications

- **Complete resection / thymectomy** remains the central intervention for localized disease (PMID:20207296; PMID:40983285).
- **Postoperative radiotherapy** is mainly relevant for invasive disease or aggressive histology (PMID:20207296).
- **Platinum-anthracycline chemotherapy** is the standard systemic approach for inoperable or metastatic thymoma (PMID:20207296).
- **Systemic immunosuppression** remains necessary when autoimmune complications persist or newly arise after thymectomy (PMID:40983285).

## Ontology grounding used in the YAML

- Disease anchor: `MONDO:0006456` thymoma
- Disease-level NCIT mapping: `NCIT:C3411` Thymoma
- Histologic subtype grounding:
  - `NCIT:C6454` Thymoma Type A
  - `NCIT:C6885` Thymoma Type AB
  - `NCIT:C6887` Thymoma Type B1
  - `NCIT:C6888` Thymoma Type B2
  - `NCIT:C7997` Thymoma Type B3
- Invasion-status subtype grounding:
  - `NCIT:C7386` Encapsulated Thymoma
  - `NCIT:C7904` Invasive Malignant Thymoma

NCIT subtype identifiers were checked against the EVS neoplasm hierarchy page for thymoma subclasses while keeping the disease anchor MONDO-first in the dismech entry.

## References

- PMID:24974848
- PMID:32034314
- PMID:18567864
- PMID:41098393
- PMID:15063231
- PMID:20207296
- PMID:37761349
- PMID:39180607
- PMID:40983285
