# `has_subtypes` Usage and Subtype-Gene Pathograph Wiring Audit

**Date:** 2026-09-04
**Tooling:** `just subtype-usage-audit` (`scripts/subtype_usage_audit.py`)

## Why

Two related concerns about the `has_subtypes` field:

1. Even where the decision to lump subtypes into one entry is correct
   (per the granularity rules in design decisions §3/§3a), the entry may be
   throwing away information — particularly gene-specific phenotypic
   effects. A subtype only *carries* information beyond its own description
   when other sections stratify by it via the `subtype:` foreign key
   (phenotypes, genetic, biochemical, prevalence, progression,
   histopathology, imaging, and phenotype context).
2. Some entries declare a **gene-specific subtype** whose gene is not wired
   into the pathograph at all — the entry asserts "this subtype is caused by
   gene G" while the causal graph has never heard of G. This is
   deterministically detectable, and the audit script now detects it.

All numbers below regenerate with `just subtype-usage-audit` (summary),
`--format tsv` (per-gene rows), or `--format list --status ABSENT`
(worst-case findings). The audit is advisory — the backlog predates it, so
there is no gate and no baseline; `--strict` exists for focused sweeps.

## Census: how actively is `has_subtypes` used?

| Measure | Count |
|---|---|
| Disorder entries with `has_subtypes` | 912 (of 2,742 KB entries) |
| Subtypes declared (incl. nested `children`) | 3,571 |
| Subtypes ever referenced by a `subtype:` FK | 1,284 (36%) |
| Entries with a subtype list but **zero** `subtype:` FK refs anywhere | 475 |
| Total `subtype:` FK references | 2,996 |

FK references by section: phenotypes 1,679 · genetic 966 · progression 139
· prevalence 90 · histopathology 78 · biochemical 44.

So roughly **two-thirds of declared subtypes are inert**: they exist as a
nosology index card (name + description + evidence, usually well-sourced —
description fill is 98%, evidence fill 70%) but nothing in the entry is
stratified by them. That is not automatically a defect — many subtype lists
legitimately record a classification without subtype-divergent phenotypes —
but for genetically heterogeneous diseases it is exactly where gene-specific
phenotypic effects go missing.

The sharper version of that concern: **58 entries declare gene-specific
subtypes (a `genes:` list on the subtype) and have zero subtype-stratified
content of any kind** — e.g. Aicardi_Goutieres_Syndrome,
Cerebral_Cavernous_Malformation, Frontotemporal_Dementia,
Dystroglycanopathy. Each names per-gene subtypes whose phenotypic
consequences are documented in the literature but recorded here only as
prose, if at all.

## Detector: subtype genes not wired into the pathograph

`has_subtypes[].genes` names 924 gene references across 839 subtypes in 193
entries. A gene reaches the pathograph in exactly two machine-readable ways
(`dismech.graph`): a pathophysiology node carrying the gene as a structured
descriptor (`gene:` / `genes:`), or a `genetic:` node whose gene keys
auto-link it to such a node. Checking each subtype gene against both:

| Verdict | Count | Meaning |
|---|---|---|
| `WIRED_DIRECT` | 594 | A pathophysiology node carries the gene descriptor |
| `GENETIC_NONCAUSAL` | 3 | `genetic:` entry exists but is deliberately non-contributing (modifier etc.) |
| `GENETIC_UNWIRED` | 253 | A causal `genetic:` entry exists but floats — no pathophysiology node carries the gene |
| `ABSENT` | 74 | The gene appears nowhere in `genetic:` or pathophysiology descriptors |

**327 subtype genes (35%) across 81 entries are not wired into the
pathograph.** Of these, 41 have the gene symbol appearing in a
pathophysiology node *name* — meaning the mechanism chain was curated but
the gene→mechanism link is prose-only and invisible to the graph, KGX
export, and any downstream query.

### The two failure shapes, with worked examples

**Shape 1 — chain exists, descriptor missing** (the 41 `name_mention`
cases; cheap to fix). `Androgen_Insensitivity_Syndrome` has a complete
mechanism chain starting at a pathophysiology node literally named *"AR
Germline Pathogenic Variant"* — but the node carries no `genes:` descriptor,
so the `genetic:` AR node (and the CAIS/PAIS subtypes' AR reference) never
connects to it. Adding the structured descriptor to the node is the whole
fix.

**Shape 2 — gene attached to nothing** (the `ABSENT` rows; ranges from a
descriptor backfill to real curation work). `Galloway-Mowat_Syndrome`
declares eleven per-gene subtypes (GAMOS1–GAMOS10 plus PRDM15-related) and
*does* curate the mechanism families — "KEOPS and t6A Biogenesis
Deficiency", "Nuclear Pore Dysfunction" — but ten of the eleven genes
(everything except WDR4) appear nowhere outside `has_subtypes`: no
`genetic:` section exists and no mechanism node carries them, so which
GAMOS gene feeds which mechanism node lives only in prose. This case also
shows the limit of the `name_mention` heuristic: "OSGEP" is not a word in
"KEOPS and t6A Biogenesis Deficiency", so complex-level node naming
escapes the flag. At the far end, `Split_Hand_Foot_Malformation` has 12
per-locus subtypes against just two generic signaling nodes with no gene
anywhere — the per-locus etiology (TP63, DLX5/6, …) is not curated at all.
Other heavy `ABSENT` entries: Primary_Coenzyme_Q10_Deficiency (9),
Orofaciodigital_Syndrome (8), Inborn_Disorder_of_Bile_Acid_Synthesis (6),
Loeys-Dietz_Syndrome (5).

Entries with the most unwired subtype genes overall (ABSENT +
GENETIC_UNWIRED): Orofaciodigital_Syndrome (17),
Split_Hand_Foot_Malformation (13), Complex_Hereditary_Spastic_Paraplegia
(10), Galloway-Mowat_Syndrome (10), Primary_Coenzyme_Q10_Deficiency (9),
Autosomal_Recessive_Limb-Girdle_Muscular_Dystrophy (8),
Non-Syndromic_X-Linked_Intellectual_Disability (8).

### What the detector deliberately does not decide

- **A `GENETIC_UNWIRED` row is not always a curation gap.** Some entries
  correctly model a shared final common pathway where per-gene wiring adds
  nothing (all subtype genes converge on one node the entry describes in
  prose). The audit reports the machine-readability gap; whether to close it
  with a descriptor, a per-gene pathophysiology node, or a `notes:` line is
  the curator's call.
- **It only sees structured `genes:` lists.** A subtype named "FA-A" that
  implies FANCA without a `genes:` list is invisible; so the true unwired
  count is a floor. (Subtype `genes` fill is 839/3,571 = 23%.)
- **`GENETIC_NONCAUSAL` is usually correct as-is** — a modifier or
  susceptibility gene deliberately draws no causal edge.

## Suggested follow-ups

1. **Descriptor backfill tranche** — the 41 `name_mention` cases
   (`--format tsv`, filter `name_mention == yes`) need only a `genes:`
   descriptor added to an existing pathophysiology node; validation is
   offline since the hgnc CURIEs are already cached from the subtype block.
2. **Per-entry curation issues** for the top `ABSENT` entries
   (Galloway-Mowat, Split_Hand_Foot_Malformation, OFD, CoQ10 deficiency) —
   some need only gene descriptors on existing mechanism-family nodes,
   others need the per-gene etiology curated.
3. **Consider the census when lumping** — a lump/split decision that keeps
   subtypes inside one entry should be paired with `subtype:`-stratified
   phenotypes/genetic rows where the literature supports them; the 58
   gene-subtyped entries with zero stratified content are the natural
   worklist.

## Status update (2026-09-17, same branch)

The descriptor-backfill follow-ups were worked to exhaustion on this branch,
in three passes of decreasing mechanicalness. **The unwired backlog went from
327 genes across 81 entries to 66 across 33**, and `WIRED_DIRECT` from 594 to
855.

**Pass 1 - symbol in the node name (41 genes, 19 entries).** Every
`name_mention` case received a `genes:` descriptor on the node whose name and
description already assert that gene's mechanism, plus two adjacent cases
found in review: IRAK1 in `Chromosome_Xq_Duplication` and the complex-level
attachments in `Galloway-Mowat_Syndrome` (six KEOPS/t6A genes, NUP107/NUP133,
WDR73). That pass also showed the heuristic's limit: "OSGEP" is not a word in
"KEOPS and t6A Biogenesis Deficiency", so complex-level node naming escapes a
symbol match entirely.

**Pass 2 - symbol in the node *description* (185 genes, 53 entries).** The
much larger seam. A node description that says "Biallelic loss-of-function
variants in CHST14 (dermatan 4-O-sulfotransferase-1) or DSE..." is curated
prose making exactly the claim a `genes:` descriptor makes machine-readable.
Each placement was read against the full description before it was applied,
which is what caught the cases that should *not* be wired (below).

**Pass 2a - the node names the protein, not the gene (11 genes).** These were
invisible to any symbol search: `SERPINC1` against a node called "Antithrombin
Deficiency", `SGCA-D` against "Alpha-, beta-, gamma-, and delta-sarcoglycan
co-assemble...", `TUBA1A`/`TUBG1` against "mutations in microtubule subunits
(tubulins)", `CP`/`FTL` against an "iron homeostasis" arm. Worth knowing for
any future sweep: a gene-symbol grep systematically misses the nodes named
after what the gene makes.

**Pass 2b - the gene is named in the node's evidence snippet (4 genes).** The
last mechanical seam: TNFAIP3/NFKBIA in `Hodgkin_Lymphoma` (the snippet reads
"destructive mutations in negative regulators of NF-kB signaling (e.g.
TNFAIP3, NFKBIA)"), DNM2 in `Lethal_Congenital_Contracture_Syndrome`, C2CD3 in
`Orofaciodigital_Syndrome`.

**Real curation - `Split_Hand_Foot_Malformation`.** The report's worst case (13
subtype genes, 12 `ABSENT`, no gene anywhere in the pathograph) is now down to
2, both deliberate. Ten genes were wired to the AER node and HOXD13 to the
central-ray node, each backed by an evidence item on the same node - the
convergent-gene list already present (PMID:30101460) plus four added here for
DYNC1I1 as the DLX5/DLX6 enhancer host, the SHFM3 10q24 ectopic-AER mechanism
covering BTRC/FBXW4, PRDM1, and HOXD-cluster haploinsufficiency. Every new
snippet verifies against `references_cache`.

### What the audit cannot decide, with worked cases

Three flagged genes were left unwired **on purpose**, and each is a case where
wiring would have asserted something the entry's own evidence denies:

- **DLX1/DLX2 in `Split_Hand_Foot_Malformation`.** They sit in the deleted
  2q31.1 interval, but the entry's own SHFM5 evidence says "the absence of
  hand/foot anomalies in any of the individuals with deletions of DLX1/DLX2 but
  not the HOXD cluster supports the hypothesis that haploinsufficiency of the
  HOXD cluster, rather than DLX1/DLX2, accounts for the skeletal
  abnormalities". A `review_notes` on that subtype now records the decision so
  the next sweep does not undo it.
- **BTK in `Isolated_Growth_Hormone_Deficiency`.** The node is *named*
  "BTK-Region Xq21.3-q22 Genetic Lesion" - a perfect `name_mention` hit - and
  its description exists precisely to say BTK names the locus "not because BTK
  itself has been shown to cause the GH deficiency". The gene already sits in
  `genetic_context.gene`, which is the honest placement.

That last case is also a small finding about the tooling:
`dismech.graph._gene_lookup_keys` reads `gene:` and `genes:` but not
`genetic_context.gene`, so a gene placed there reads as unwired. Only one
flagged gene KB-wide is in that position, so it is a known false positive
rather than a systematic blind spot - but a future change to the graph's gene
indexing should decide that slot deliberately.

### What is left

66 genes across 33 entries, and **none of them is mechanical**. The
`name_mention` backlog is zero, the description and snippet seams are worked
out, and what remains needs either a curated per-gene mechanism node with
fetched literature (B2M/CIITA in `Hodgkin_Lymphoma` need an MHC-loss immune
evasion node distinct from the PD-L1 one; `Primary_Pigmented_Nodular_
Adrenocortical_Disease` needs PDE11A/PDE8B/PRKACA nodes; `Lissencephaly_
Spectrum_Disorders` needs the dystroglycanopathy and ARX arms) or a curator's
judgment that a shared final-common-pathway node suffices. Those are per-entry
literature jobs, best tracked as issues rather than as one sweep.
