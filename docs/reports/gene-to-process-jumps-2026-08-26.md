# Gene-to-process jumps in the pathograph

**Date:** 2026-08-26
**Metrics:** `just compliance-connectivity` (`src/dismech/qc_plugins.py`)
**Corpus:** `kb/disorders`, 2,267 entries

## The question

GO names three levels between a gene and what a cell can no longer do:
**gene → molecular function → biological process.** A pathograph edge running
from a `genetic:` node to a `pathophysiology` node annotated only with
`biological_processes:` skips the middle one — the graph says what the *cell*
can no longer do without ever saying what the *protein* can no longer do.

That turns into two compliance questions, one after the other:

1. **Is the gene in the pathograph at all?** (`genetic[].mechanism_outlink`)
2. **Does the node it lands on name a molecular function?**
   (`genetic[].mechanism_activity_grounding`)

Both are graded coverage metrics in `dismech.qc_plugins`, alongside the existing
`phenotypes[].causal_inlink`. They compose with weighted compliance and the
`conf/qc_config.yaml` weights like any other field, and both carry
`min_compliance: null` — advisory, not gating, while the baseline is this low.

## Where the KB stands

```
Phenotype connectivity:  12945/26576 nodes causally connected      (48.7%)
Gene-to-mechanism wiring: 2400/5128  causal genes wired            (46.8%)
Gene activity grounding:   570/2400  wired genes land on an MF     (23.8%)
```

**More than half of causal genes never reach the pathograph.** A `genetic[]`
entry connects only when some `pathophysiology` node carries the same gene in
its `gene:`/`genes:` descriptor — that shared CURIE is the whole edge — so a
gene with no such node sits in the `genetic` block and is invisible in the
graph. 936 files have at least one. This is the larger of the two gaps by a wide
margin, and it is the prior question: an unwired gene has no landing node to
ground.

Of the genes that do reach the graph, **three quarters land on a node with no
molecular function**, across 763 files. The grounding denominator is the wired
genes deliberately, so an unwired gene is charged once, against wiring, rather
than twice.

Two related counts, for scale: 645 of 2,267 disorder files use
`molecular_functions:` anywhere, and 594 pathophysiology nodes have an
activity-shaped *name* (`… molecular function deficiency`, `… Loss of Function`,
`… Channel Dysfunction`) — **355 of those, 60%, carry no MF term.** The MF enum
cache holds 523 terms against the BP cache's 2,346.

## What the failures look like

**Most often, the activity is already claimed in prose and only the term is
missing.** `Carnitine-Acylcarnitine_Translocase_Deficiency` has a node *named*
`SLC25A20 transporter molecular function deficiency`, whose description says the
variants "reduce mitochondrial inner membrane carnitine-acylcarnitine
translocase activity" — annotated `GO:0015879 carnitine transport` and nothing
else. Same shape in `Lysosomal_Acid_Phosphatase_Deficiency` (→ `GO:0016311
dephosphorylation`), `NAGA_Deficiency_Type_3`,
`MGAT2-congenital_disorder_of_glycosylation`, `Spinocerebellar_Ataxia_Type_2`.
Of the 698 single-gene landing nodes that fail the check, **262 assert the
activity in their own prose** and 56 assert it in the node name. Nothing new has
to be established for those.

**Sometimes the whole cascade is one node.**
`Growth_Hormone_Insensitivity_Syndrome` / "GH-IGF1 Axis Disruption" spells the
chain out in its description — GH → GHR → JAK2 → STAT5B phosphorylation →
dimerization → nuclear translocation → IGF1 transcription — while the graph
holds a single node with two BP terms. 49 of the 149 pathway-landing nodes carry
descriptions over 400 characters; the chain is often already written, one field
away from being nodes.

## Where a term is not the fix

- **Many genes on one node.** `Primary_Ciliary_Dyskinesia` / "Ciliary
  Dysfunction" carries **21 genes**: DNAH5 and DNAH11 are dynein motors,
  RSPH1/4A/9 are radial-spoke structural constituents, CCDC39/40 are axonemal
  rulers, FOXJ1 and MCIDAS are transcription factors. No single MF term is true
  of that set. Also `Dilated_Cardiomyopathy` / "Sarcomeric and Cytoskeletal
  Dysfunction" (31 genes) and `Autosomal_Recessive_Primary_Microcephaly` /
  "Heterogeneous Biallelic MCPH Gene Dysfunction" (28). The check flags these,
  correctly, but the repair is to split the node.
- **Classes with no shared molecular function.**
  `Autosomal_Recessive_Non-Syndromic_Intellectual_Disability` has a node called
  "Loss of a Gene-Specific Molecular Function Required by Developing Neurons"
  whose description states outright that there are no prevalent genes, pathways
  or complexes and that the affected protein functions are very diverse. The
  absence of the term there is the finding.
- **Genuinely genomic nodes.** Dosage, imprinting and silencing claims have no
  activity step to name.

## The fix is usually cheap

The molecular function is a property of the gene product, so it comes from GO
directly rather than from disease literature. Ten fills drawn from the failing
set, each verified against OLS as a live `molecular_function`:

| entry | landing node (process-only today) | `molecular_functions:` |
|---|---|---|
| Carnitine-Acylcarnitine_Translocase_Deficiency | SLC25A20 transporter molecular function deficiency | `GO:0015227` O-acyl-L-carnitine transmembrane transporter activity |
| Lysosomal_Acid_Phosphatase_Deficiency | Lysosomal Acid Phosphatase 2 Deficiency | `GO:0003993` acid phosphatase activity |
| NAGA_Deficiency_Type_3 | Alpha-N-Acetylgalactosaminidase Deficiency | `GO:0008456` alpha-N-acetylgalactosaminidase activity |
| Aspartylglucosaminuria | AGA lysosomal enzyme deficiency | `GO:0003948` N4-(beta-N-acetylglucosaminyl)-L-asparaginase activity |
| MGAT2-congenital_disorder_of_glycosylation | MGAT2 deficiency | `GO:0008455` alpha-1,6-mannosylglycoprotein 2-beta-N-acetylglucosaminyltransferase activity |
| Familial_Hypercholesterolemia | LDLR Functional Defect | `GO:0005041` low-density lipoprotein particle receptor activity |
| Brachyolmia | Deficient PAPS biosynthesis | `GO:0004781` sulfate adenylyltransferase (ATP) activity |
| Ulnar-Mammary_Syndrome | TBX3 Haploinsufficiency | `GO:0001227` DNA-binding transcription repressor activity, RNA polymerase II-specific |
| Spinocerebellar_Ataxia_Type_2 | Loss of Ataxin-2 RNA-Binding and Translational Regulation | `GO:0003729` mRNA binding |
| Growth_Hormone_Insensitivity_Syndrome | GH-IGF1 Axis Disruption | `GO:0004903` growth hormone receptor activity (first link of a chain) |

Two (`GO:0005041`, `GO:0001227`) are already in the MF enum cache and validate
offline. The pattern to copy exists in 404 disorder entries — the inborn-errors
files (`ornithine_aminotransferase_deficiency`, `Primary_Carnitine_Deficiency`,
`Trimethylaminuria`) already carry MF and BP on the same node.

## One caveat about inserting nodes

The node-classification work measured gene-grounded nodes at mean topological
depth 0.94 and MF-grounded nodes at 0.81 — statistically the same place. GENOMIC
and ACTIVITY read as **alternative entry points** in the current corpus, not
sequential steps. So the metric should be read as "does the gene's landing name
an activity", which is usually satisfied by adding a term to the node that
already exists, rather than as a mandate to insert a node between every gene and
its mechanism. See
[`the node-classification brainstorm`](../superpowers/specs/2026-08-16-pathograph-node-classification-brainstorm.md).

## Running it

```bash
just compliance-connectivity                              # all three metrics, KB-wide
just compliance-connectivity --list-unconnected           # name the failing genes
uv run python -m dismech.qc_plugins kb/disorders/Asthma.yaml   # one entry
just compliance-connectivity --activity-fail-under 20     # gate on a threshold
```

`compliance-connectivity` is a curator tool, not a CI gate: both gene metrics
carry `min_compliance: null` in `conf/qc_config.yaml`, and neither runs in
`just qc`. Raising either to a real threshold is a decision to make once the
baseline moves — 46.8% and 23.8% are too low to gate on today.
