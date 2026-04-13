---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-13T04:20:00Z'
end_time: '2026-04-13T05:35:00Z'
duration_seconds: 4500.0
citation_count: 7
notes: >
  Manual PubMed and ontology-browser review completed for Waldenstrom
  macroglobulinemia curation. Cancer curation guidance from issue #1198 /
  Wilms tumor was applied explicitly: the curation unit remains one coherent
  Waldenstrom mechanism graph anchored to MONDO:0100280, lymphoplasmacytic
  lymphoma is treated as the parent histopathologic backbone rather than a
  separate dismech page, and smoldering/familial/recurrent/refractory/
  transformed states were not split into standalone disease pages because they
  do not define separate core causal programs for this entry. Instead, the YAML
  uses flat `has_subtypes` facet axes for clinical course and molecular context
  within one page. NCIT was used where the current schema and validator support
  oncology-specific grounding directly (histopathology, drug, and procedure
  terms). The current schema still lacks disease-level or subtype-level
  `ncit_mappings`, and the current `RegimenTerm` expansion did not admit the
  candidate BR and zanubrutinib regimen codes, so those #1198 recommendations
  were applied conservatively rather than approximated with ad hoc slots.
---

## Question

Produce a disease-level mechanistic research summary for Waldenstrom
macroglobulinemia suitable for a dismech cancer curation, with explicit notes
on MONDO/NCIT modeling choices.

## Output

# Waldenstrom Macroglobulinemia: Mechanistic Summary

## Disease anchor and modeling choice

Waldenstrom macroglobulinemia (WM) is best modeled here as a single disease-level
mechanism graph rooted to **MONDO:0100280 Waldenstrom macroglobulinemia**, not as
a lattice of every oncology subclass. The key defining combination is:

- lymphoplasmacytic lymphoma involving the bone marrow
- secretion of a monoclonal IgM paraprotein
- recurrent MYD88-driven B-cell oncogenesis with CXCR4-mutant subclonal evolution

Following issue #1198, I treated **lymphoplasmacytic lymphoma** as the disease
parent / diagnostic histopathology concept rather than opening a separate dismech
page for every related ontology refinement. Likewise, I did **not** split
smoldering WM, familial WM, refractory WM, recurrent WM, or transformed WM into
separate disorder files, because those are disease-state, predisposition, or
transformation facets rather than distinct causal programs for the baseline WM
mechanism graph. In the YAML, this was reflected by keeping one disease page and
encoding subtype structure only as flat `has_subtypes` facets for clinical
course and molecular context.

Relevant ontology anchors:

- MONDO:0100280 Waldenstrom macroglobulinemia
- MONDO:0000432 lymphoplasmacytic lymphoma
- NCIT:C80307 Waldenstrom Macroglobulinemia
- NCIT:C3212 Lymphoplasmacytic Lymphoma

## Foundational disease definition

PMID:12720118 remains the key disease-definition paper for this curation. It
defines WM as an uncommon lymphoproliferative disorder characterized by bone
marrow lymphoplasmacytic infiltration and IgM monoclonal gammopathy, and it
explicitly argues that WM is a distinct clinicopathologic entity rather than
just an IgM secretion syndrome.

PMID:11718214 complements this by describing the underlying cell composition:
small mature B lymphocytes, plasmacytoid lymphocytes, and plasma cells. For the
dismech entry, that supports treating the bone-marrow lymphoplasmacytic clone as
the core disease unit and the IgM paraprotein as a downstream biochemical output
of that clone.

## Core mechanisms selected for the YAML graph

### 1. Bone marrow lymphoplasmacytic infiltration

This is the disease-defining tissue state. The mechanistic unit is the marrow
infiltrating clone composed of B-cell/plasma-cell lineage lymphoplasmacytic
cells. This node should sit near the top of the graph because it links the
founding genomic lesions to the clinical consequences of marrow occupation and
paraprotein secretion.

Key support:

- PMID:12720118
- PMID:11718214

### 2. Monoclonal IgM secretion

The IgM paraprotein is the key biochemical output of the malignant clone and is
best modeled as a separate downstream node rather than bundled into the marrow
infiltration node. This helps keep the graph atomic and allows direct edges to
paraprotein-driven complications.

Key support:

- PMID:12720118

### 3. Serum hyperviscosity

Hyperviscosity is a downstream biophysical consequence of heavy circulating IgM
burden. I modeled this as a separate pathophysiology node rather than collapsing
it into the phenotype list, because it is an intermediate pathogenic process
that explains neurologic and visual symptoms.

Key support:

- PMID:18813229

### 4. MYD88 L265P founder mutation

MYD88 L265P is the dominant recurrent somatic lesion in WM and should be treated
as an upstream genomic driver node. The cached abstract set supports two
important, conservative claims:

- MYD88 L265P is present in the majority of WM cases (PMID:24224040)
- CXCR4 WHIM-like mutations are usually acquired after MYD88 L265P in WM
  oncogenesis (PMID:26659815)

Because the cached abstract set was used conservatively, I did not overstate the
full MYD88 -> BTK -> IRAK -> NF-kB signaling chain in the YAML evidence block
without a validated PMID cache line for that exact claim. That mechanistic detail
is real and well-supported in the broader WM literature, but the YAML entry is
restricted to what could be quoted exactly and validated in this branch.

### 5. CXCR4 WHIM-like subclonal evolution

CXCR4 mutations are not the founding lesion; they are modeled as a later,
subclonal branch layered onto the MYD88-mutant clone. This is a good example of
an oncology refinement that belongs inside the same disease graph rather than in
a separate disease page.

Key support:

- PMID:26659815
- PMID:37099027 (clinical relevance for BTK-inhibitor sensitivity)

### 6. Mast-cell supportive signaling in the marrow microenvironment

PMID:18216294 shows that excess marrow mast cells are common in WM and provide
growth/survival signals to lymphoplasmacytic cells. This is worth a separate
node because it captures a bona fide microenvironmental mechanism rather than a
mere descriptive pathology feature.

Key support:

- PMID:18216294

## Clinical phenotype and complication summary

The best abstract-backed phenotype set from the cached reference slice is:

- IgM paraproteinemia / monoclonal gammopathy (PMID:12720118)
- lymphadenopathy (PMID:18813229)
- peripheral neuropathy, occurring in nearly half of patients (PMID:18813229)

Hyperviscosity-related neurologic disorders are common enough to matter
mechanistically but were better represented as a downstream pathophysiology node
than as an HP-grounded phenotype because the available ontology grounding in this
schema is much cleaner for the manifestations than for the syndrome label itself.

## Treatment conclusions for the entry

The current disease-level treatment section should emphasize:

- **watchful waiting** for asymptomatic patients, per the 2023 IWWM consensus
  (PMID:37099027)
- fixed-duration **chemoimmunotherapy** as an important first-line option,
  especially bendamustine-rituximab (PMID:37099027)
- **zanubrutinib** as a current covalent BTK inhibitor option with lower toxicity
  and deeper remissions than ibrutinib in the referenced randomized-trial update
  (PMID:37099027)
- **plasmapheresis** for rapid paraprotein reduction in hyperviscosity and related
  neurologic complications (PMID:18813229)

Following #1198, NCIT should be preferred where it gives materially better
oncology specificity. In the YAML this means:

- NCIT:C3212 for the histopathology finding
- NCIT:C1702 for rituximab
- NCIT:C141428 for zanubrutinib
- NCIT:C15304 for plasmapheresis

I initially attempted to ground BR and zanubrutinib with NCIT regimen terms as
well, but the current `RegimenTerm` validator expansion in this branch did not
accept those codes, so I retained the validated disease-level treatment
representation using treatment actions plus ontology-grounded agents/procedures.

## References

- PMID:11718214
- PMID:12720118
- PMID:18216294
- PMID:18813229
- PMID:24224040
- PMID:26659815
- PMID:37099027
