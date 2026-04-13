---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-13T04:10:00Z'
end_time: '2026-04-13T05:35:00Z'
duration_seconds: 5100.0
citation_count: 11
notes: >
  Manual deep research was performed from primary PubMed sources for disease-level
  cancer curation of juvenile myelomonocytic leukemia (JMML). Modeling choices
  were updated to follow the cancer-curation guidance referenced from dismech
  issue #1198 before drafting the disorder YAML.
---

## Question

Produce a disease-level dismech cancer curation for juvenile myelomonocytic leukemia
with ontology-grounded disease, subtype, phenotype, histopathology, mechanism,
and treatment annotations; exact PMID-backed evidence; and explicit subtype-axis
reasoning consistent with the Wilms/#1198 modeling guidance.

## Output

# Juvenile Myelomonocytic Leukemia: Manual Deep Research Summary

## Disease-level modeling decision

JMML should be modeled as **one disease-level mechanism graph**, not split into
multiple pages for every ontology subclass or driver-defined variant. The strongest
support for this comes from the 2019 review that states that about 90% of patients
have lesions in one of five canonical Ras-pathway genes and that these define
**genetically and clinically distinct subtypes** rather than wholly separate diseases
(PMID:30670449). Following the #1198 cancer-curation guidance, the disease file
therefore uses:

- a single MONDO-first disease anchor for canonical JMML
- flat `has_subtypes` facets for the **molecular-driver axis** (`PTPN11-mutated`,
  `NRAS-mutated`, `KRAS-mutated`, `NF1-associated`, `CBL-associated`)
- no separate dismech page for those subtype facets

Noonan syndrome-associated myeloproliferative disorder (NS-MPD) was **not** folded
into `has_subtypes` for the JMML entry. The real-world series in PMID:39123476
explicitly separated NS-MPD from JMML treatment analysis because none of the NS-MPD
patients required chemotherapy, and spontaneous clinical remission was observed in
that group. That supports treating NS-MPD as a related but distinct disease context
or differential, not as an ordinary JMML subtype facet.

## Ontology grounding choices

- **Primary disease term:** MONDO:0011908 `juvenile myelomonocytic leukemia`
- **Disease-adjacent NCIT grounding:** NCIT:C9233 `Juvenile Myelomonocytic Leukemia`
- **Key phenotype terms:** monocytosis, splenomegaly, hepatomegaly, leukocytosis,
  anemia, thrombocytopenia
- **Key histopathology terms:** bone marrow hypercellularity, myelodysplasia
- **Key mechanism terms:** Ras protein signal transduction, MAPK cascade,
  cytokine-mediated signaling pathway, DNA methylation
- **Key treatment terms:** hematopoietic stem cell transplantation, pharmacotherapy
  with azacitidine and trametinib as therapeutic agents

Because the current schema exposes MONDO-specific disease mappings but not dedicated
NCIT disease mappings, NCIT grounding was carried in the disease-adjacent cancer
representation rather than inventing a new schema pattern locally.

## Core disease biology

### Canonical defining lesion space

JMML is a pediatric myelodysplastic/myeloproliferative neoplasm overlap syndrome
with sustained peripheral blood monocytosis and dominant Ras-pathway biology.

- PMID:32460983 describes JMML as a pediatric MDS/MPN overlap syndrome with sustained
  peripheral blood monocytosis and poor outcomes.
- PMID:30670449 states that JMML pathobiology is characterized by constitutive
  activation of Ras signal transduction and that about 90% of patients harbor lesions
  in `PTPN11`, `NRAS`, `KRAS`, `NF1`, or `CBL`.
- PMID:26457647 found canonical lesions in `NF1`, `NRAS`, `KRAS`, `PTPN11`, or
  `CBL` in 85% of cases and showed that additional somatic alterations at diagnosis
  are strongly associated with outcome.

### Atomic mechanism chain supported by the literature

1. **Ras-pathway driver lesion**
   - Canonical driver lesions involve `PTPN11`, `NRAS`, `KRAS`, `NF1`, or `CBL`
     (PMID:30670449, PMID:26457647).
2. **RAS/MAPK pathway hyperactivation**
   - Ras signaling is constitutively active in JMML (PMID:30670449).
   - Patient-derived iPSC models confirm constitutive Ras/MAPK signaling in
     PTPN11- and CBL-mutant JMML cells (PMID:29884903).
3. **GM-CSF hypersensitive signaling**
   - GM-CSF hypersensitivity is a disease hallmark in marrow progenitors
     (PMID:22195407).
   - iPSC-derived JMML cells show constitutive GM-CSF activation with enhanced
     STAT5/ERK phosphorylation (PMID:23620576).
4. **Myelomonocytic progenitor expansion**
   - This manifests as leukocytosis, absolute monocytosis, cytopenias, and marrow
     hypercellularity with myelomonocytic proliferation (PMID:22195407).
5. **Epigenetically aggressive subset**
   - High DNA methylation identifies an aggressive biologic JMML variant with worse
     survival and higher post-transplant relapse risk (PMID:21406719).

## Phenotype and pathology summary

The most reusable phenotype/pathology extraction came from the pathology review
PMID:22195407:

- marked splenomegaly and hepatomegaly
- leukocytosis
- absolute monocytosis
- anemia
- thrombocytopenia
- marrow hypercellularity due to myelomonocytic proliferation
- mild dysplasia

PMID:29884903 additionally highlights elevated fetal hemoglobin and GM-CSF
hypersensitivity as classic diagnostic/risk features.

## Treatment evidence summary

### Allogeneic hematopoietic stem cell transplantation

Transplant remains the only curative treatment for most canonical JMML cases.

- PMID:25435114: allogeneic hematopoietic stem cell transplant is the only curative
  option, but relapse and toxicity remain substantial.
- PMID:30670449: most children require allogeneic hematopoietic stem cell
  transplantation for long-term leukemia-free survival.

### Azacitidine

Azacitidine has meaningful pre-transplant cytoreductive and clinical activity.

- PMID:34297046: phase 2 AZA-JMML-001 showed 61% clinical partial remission after
  three cycles, with 82% leukemia-free survival after subsequent HSCT at median
  follow-up.
- Response was strongest in intermediate- or low-methylation groups in that trial.

### Trametinib

MEK inhibition has become credible salvage/bridging therapy for relapsed or
refractory disease.

- PMID:38867349: phase II Children's Oncology Group study reported an objective
  response rate of 50%.
- Four refractory patients were bridged to HSCT after trametinib, and three
  additional patients remained on off-protocol trametinib without HSCT at report
  time.

## Subtype-axis reasoning carried into the YAML

The curated subtype axis was limited to the canonical driver-defined JMML groups:

- `PTPN11-mutated`
- `NRAS-mutated`
- `KRAS-mutated`
- `NF1-associated`
- `CBL-associated`

These were chosen because PMID:30670449 explicitly describes them as the five
genetically and clinically distinct JMML subtypes. A separate methylation-risk
axis was **not** added to `has_subtypes`; methylation state was instead modeled as
an orthogonal pathobiologic/risk mechanism because it alters prognosis without
necessarily defining a separate clinical disease page or distinct primary causal
program.

## Key references used

- PMID:25435114
- PMID:22195407
- PMID:26457647
- PMID:21406719
- PMID:23620576
- PMID:29884903
- PMID:30670449
- PMID:32460983
- PMID:34297046
- PMID:38867349
- PMID:39123476
