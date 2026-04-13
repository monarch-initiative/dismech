---
provider: openai
generated_at: "2026-04-13T05:29:21Z"
disease_name: Sezary Syndrome
mondo_id: MONDO:0017844
ncit_id: NCIT:C3366
---

# Sezary Syndrome Deep Research Notes

## Modeling decisions

- Per cancer curation guidance from dismech issue `#1198`, this curation treats Sezary syndrome as a single disease-level mechanism graph rather than trying to make every ontology child or staging bucket its own dismech page.
- `disease_term` is MONDO-first: `MONDO:0017844` Sezary syndrome.
- NCIT grounding was added wherever the current schema supports cancer-specific terms directly: disease-context term `NCIT:C3366` Sezary Syndrome, parent context `NCIT:C3467` Primary Cutaneous T-Cell Non-Hodgkin Lymphoma, histopathology findings such as `NCIT:C36722` Sezary Cell and `NCIT:C39621` Cerebriform Lymphocyte, biomarker `NCIT:C74625` Sezary Cell Count, biomarker `NCIT:C171048` KIR3DL2 Positive, and oncology-specific intervention terms such as `NCIT:C62729` Extracorporeal Photopheresis and `NCIT:C46089` Allogeneic Hematopoietic Stem Cell Transplantation.
- I did not create separate disorder files for nonerythrodermic Sezary syndrome, B-stage strata, or large-cell transformation. Those are presentation, staging, or progression facets, not separate disease-level causal programs.
- I therefore omitted `has_subtypes` in the YAML. For this disease slice, adding pseudo-subtypes would have created ontology noise without improving the mechanism graph.

## Disease identity and ontology grounding

- MONDO disease anchor: `MONDO:0017844` Sezary syndrome.
- NCIT disease grounding for cancer curation context: `NCIT:C3366` Sezary Syndrome.
- NCIT parent disease context: `NCIT:C3467` Primary Cutaneous T-Cell Non-Hodgkin Lymphoma.
- Core cell-type grounding used in the graph: `CL:0000904` central memory CD4-positive, alpha-beta T cell.
- Core biological-process grounding used in the graph:
  - `GO:0072678` T cell migration
  - `GO:0007259` cell surface receptor signaling pathway via JAK-STAT
  - `GO:0050852` T cell receptor signaling pathway
  - `GO:0008283` cell population proliferation
  - `GO:0002710` negative regulation of T cell mediated immunity

## Key literature takeaways used in the YAML

### Definition and diagnosis

- `PMID:34165432` gives the operational disease-defining triad and the classic circulating `CD4+/CD8-` phenotype with loss of `CD7` and/or `CD26`.
- `PMID:31487384` shows that `KIR3DL2` materially improves early diagnosis and blood staging, especially in lymphopenic patients.
- `PMID:28709694` argues that early Sezary syndrome can be missed when erythroderma is absent and supports blood PCR for monoclonal T-cell receptor rearrangement plus flow cytometry in suspicious refractory dermatitis.

### Cell of origin and trafficking biology

- `PMID:20484084` supports the central-memory T-cell model for Sezary syndrome and contrasts it with mycosis fungoides.
- `PMID:15727636` anchors the skin/blood/lymph-node recirculation program through `CCR4`, `CCR10`, and `CCR7`.

### Core oncogenic mechanisms

- `PMID:26415585` is the main disease-genomics anchor for this entry:
  - recurrent `ARID1A` loss and broader chromatin-remodeling defects
  - recurrent `PLCG1` gain-of-function mutations
  - recurrent `JAK1`, `JAK3`, `STAT3`, and `STAT5B` lesions
  - explicit therapeutic rationale for JAK/STAT pathway inhibition
- `PMID:29204699` supports downstream immune dysfunction through expanded suppressive T-cell populations in Sezary syndrome.

### Histopathology and phenotype

- `PMID:6651315` supports the classic skin-biopsy pattern of atypical lymphoid cells with cerebriform nuclei.
- `PMID:31489115` supports pruritic inflammatory disease burden and immune dysfunction in a modern human-sample transcriptomic study.
- `PMID:29026585` supports palmoplantar keratoderma as a clinically useful Sezary clue.

### Therapy

- `PMID:34478581` supports extracorporeal photopheresis as a blood- and skin-active treatment in real-world SS/MF practice.
- `PMID:11331325` supports oral bexarotene as effective systemic CTCL therapy.
- `PMID:25605368` supports mogamulizumab, with stronger response rates in Sezary syndrome than in mycosis fungoides and especially strong blood responses.
- `PMID:31532724` supports pembrolizumab activity in advanced relapsed/refractory MF/SS.
- `PMID:25068422` supports allogeneic hematopoietic cell transplantation as the main potentially curative option in advanced MF/SS.

## Important research not fully promoted into the YAML graph

- `PMID:38170178` shows that *Staphylococcus aureus* enterotoxins can induce drug resistance in primary malignant T cells from patients with Sezary syndrome through TCR, NF-kappaB, and JAK/STAT-associated programs. I kept this in research notes instead of making it a core disease node because it is a clinically important resistance modifier, but not the cleanest disease-defining upstream program for the base Sezary syndrome graph.
- `PMID:25802883` reports a `CTLA4:CD28` fusion in an advanced Sezary syndrome case with rapid clinical response to ipilimumab. This is mechanistically interesting but currently better treated as a rare precision-oncology exception than as a disease-level canonical node.
- `PMID:25981000` and `PMID:28709694` support nonerythrodermic/early Sezary presentations. Per `#1198`, these were not split into a separate disease file because they are presentation variants rather than a separate causal program.

## Expected validation-sensitive points

- The triad and blood-burden snippets use typography from PubMed abstracts, including the multiplication sign and micro symbol; these should be preserved exactly for reference validation.
- NCIT disease-level mappings were handled through schema-supported NCIT uses (findings, biomarkers, treatment terms, agents) plus this research note because the current `DiseaseMappings` container only exposes explicit `mondo_mappings`, not `ncit_mappings`.
