# Gene-to-process jumps in the pathograph

**Date:** 2026-08-26 (figures re-measured 2026-09-25 against current `main`)
**Metrics:** `just compliance-connectivity` (`src/dismech/qc_plugins.py`)
**Gate:** `just check-gene-activity-grounding` (`scripts/check_gene_activity_grounding.py`)
**Corpus:** `kb/disorders`, 3,149 entries

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
`conf/qc_config.yaml` weights like any other field. Both gene metrics carry
`min_compliance: null`: coverage is far too low for an absolute floor, so the
second question is enforced as a **ratchet** instead — see *Gating it* below.

## Where the KB stands

```
Phenotype connectivity:  21892/38839 nodes causally connected      (56.4%)
Gene-to-mechanism wiring: 3924/6444  causal genes wired            (60.9%)
Gene activity grounding:  1108/3924  wired genes land on an MF     (28.2%)
```

The grounding figure is what this branch leaves behind; on `main` it is
963/3924 (24.5%), so the tranches below move it 24.5% → 28.2% and cut the files
carrying a gap from 1,330 to 1,201. The corpus moves several times a day, so
read these as a dated snapshot — the recipes below print the current figures.

**More than half of causal genes never reach the pathograph.** A `genetic[]`
entry connects only when some `pathophysiology` node carries the same gene in
its `gene:`/`genes:` descriptor — that shared CURIE is the whole edge — so a
gene with no such node sits in the `genetic` block and is invisible in the
graph. 969 files have at least one. This is the larger of the two gaps, and it
is the prior question: an unwired gene has no landing node to ground.

Of the genes that do reach the graph, **more than seven in ten land on a node
with no molecular function**, across 1,201 files. The grounding denominator is
the wired genes deliberately, so an unwired gene is charged once, against
wiring, rather than twice.

Two related counts, for scale: 1,335 of 3,149 disorder files use
`molecular_functions:` anywhere, and 1,068 pathophysiology nodes have an
activity-shaped *name* (`… molecular function deficiency`, `… Loss of Function`,
`… Channel Dysfunction`) — **567 of those, 53%, carry no MF term.** The MF enum
cache holds 870 terms against the BP cache's 2,777.

## What the failures look like

**Most often, the activity is already claimed in prose and only the term is
missing.** `Carnitine-Acylcarnitine_Translocase_Deficiency` has a node *named*
`SLC25A20 transporter molecular function deficiency`, whose description says the
variants "reduce mitochondrial inner membrane carnitine-acylcarnitine
translocase activity" — annotated `GO:0015879 carnitine transport` and nothing
else. Same shape in `Lysosomal_Acid_Phosphatase_Deficiency` (→ `GO:0016311
dephosphorylation`), `NAGA_Deficiency_Type_3`,
`MGAT2-congenital_disorder_of_glycosylation`, `Spinocerebellar_Ataxia_Type_2`.
Of the 1,492 single-gene landing nodes that still fail the check, **388 assert
the activity in their own prose**. Nothing new has to be established for those.

**Sometimes the whole cascade is one node.**
`Growth_Hormone_Insensitivity_Syndrome` / "GH-IGF1 Axis Disruption" spells the
chain out in its description — GH → GHR → JAK2 → STAT5B phosphorylation →
dimerization → nuclear translocation → IGF1 transcription — while the graph
holds a single node with two BP terms. 70 of the 181 pathway-landing nodes carry
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
offline. The pattern to copy exists in 852 disorder entries — the inborn-errors
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

## Gating it

An absolute threshold cannot enforce this: at 28.2% coverage, a floor high
enough to matter fails every PR and one low enough to pass gates nothing. So
the second question is enforced as a **ratchet**, following
`check_environmental_evidence.py`:

```bash
just check-gene-activity-grounding                 # runs in `just qc`
just check-gene-activity-grounding --count
just update-gene-activity-baseline                 # only ever to SHRINK
```

CI derives the grandfather set live from the base branch via
`GENE_ACTIVITY_BASELINE_REF`, so a PR fails only on genes it *adds* whose
landing node names no molecular function. There is no snapshot to keep in sync
and nothing for parallel curation PRs to race on.
`tests/gene_activity_grounding_baseline.txt` (2,816 findings) is the local and
shallow-checkout fallback, and is allowed to drift stale-high: a line for a gene
since grounded grandfathers nothing.

Grandfathering a *new* line stays legitimate for the two shapes above — a
many-gene bundle, and a class whose members share no molecular function.
Neither is a reason to bind a term that overstates the node.

The `phenotypes[].causal_inlink` metric is separately gated by a corpus-level
`min_compliance` floor (50.0, against a measured 56.4%); the two gene metrics
stay advisory in the weighted score, with `--genes-fail-under` and
`--activity-fail-under` for ad-hoc checks.
