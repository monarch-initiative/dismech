# Gene-to-process jumps in the pathograph: how many, how findable, how fillable

**Date:** 2026-08-26
**Scan:** `just gene-activity-gaps` (`scripts/gene_activity_gap_scan.py`)
**Corpus:** `kb/disorders` + `kb/modules`, 2,424 entries

## The question

GO names three levels between a gene and what a cell can no longer do:
**gene → molecular function → biological process.** Where a dismech pathograph
draws an edge from a `genetic:` node to a `pathophysiology` node annotated only
with `biological_processes:`, the middle level is missing — the graph goes from
the lesion to the process, skipping what the *protein* can no longer do. This
report asks how often that happens, whether the cases can be found mechanically,
and whether the missing step can actually be supplied.

## How the edge is drawn

`build_causal_graph` links a `genetic:` entry to every `pathophysiology` node
that shares one of its gene identifiers (`pathophysiology_by_gene_key` in
`src/dismech/graph.py`). Nothing about that edge is curated per-edge: it exists
because both ends carry the same HGNC CURIE. So the question "what does the gene
point at?" is answered entirely by the annotations on the landing node.

## Are they easy to find? Yes — it is a slot-presence query

The whole census is a `molecular_functions` / `biological_processes` presence
test on the landing node of a gene-sourced edge. No ontology traversal, no
network, no LLM: the scan runs offline over the whole KB in about 40 seconds.

```
Gene -> mechanism edges by grounding of the landing node:
     607  ACTIVITY_BOUND   20.6%    molecular_functions: present -- no jump
    1626  PROCESS_JUMP     55.2%    biological_processes: only  -- the jump
      15  PROTEIN_ONLY      0.5%    gene_products/protein_complexes only
     696  UNGROUNDED       23.6%    no molecular grounding at all
    2944  total
```

The 1,626 jump edges collapse to **972 distinct landing nodes across 578
entries** (several gene nodes commonly point at the same mechanism node).

Two related counts, for scale: 645 of 2,267 disorder files use
`molecular_functions:` anywhere, and 594 pathophysiology nodes in `kb/disorders` have an
activity-shaped *name* (`… molecular function deficiency`, `… Loss of Function`,
`… Channel Dysfunction`) — **355 of those, 60%, carry no MF term.**

## How far do the jumps land?

Reading each landing node's GO BP term through the existing seed table
(`docs/superpowers/pathograph_node_class_go_seed.tsv`) gives the tier the edge
lands on, which is the jump distance:

| landing tier | distinct nodes | reading |
|---|---:|---|
| CELLULAR | 250 | gene → what the cell does. Two tiers skipped. |
| *(BP term not in the 640-term seed table)* | 204 | unclassified, mostly specialist vocabulary |
| GENOMIC | 120 | transcription/repair processes; arguably the right level already |
| PATHWAY | 107 | a whole signalling cascade drawn as one node |
| TISSUE | 53 | gene → tissue-level process. Three tiers skipped. |
| ACTIVITY | 49 | barely a jump — the BP term is already activity-adjacent |
| SUBSTANCE | 47 | gene → metabolite pool |
| SYSTEMIC | 21 | gene → organ/systemic derangement |

## Sampling: the jumps come in four shapes

The scan assigns an advisory verdict from three signals — how many genes the
landing node carries, whether its own prose already asserts an activity, and
where the BP term lands.

```
     372  ANNOTATE_MF            add the term to the node that exists
     274  DEBUNDLE_FIRST         several genes on one node; no single MF is correct
     266  INSERT_ACTIVITY_NODE   a genuine missing node
      60  INSERT_CHAIN           a cascade drawn as one node
```

**1. The activity is already claimed, just not bound (372).**
`Carnitine-Acylcarnitine_Translocase_Deficiency` has a node *named* `SLC25A20
transporter molecular function deficiency`, whose description says the variants
"reduce mitochondrial inner membrane carnitine-acylcarnitine translocase
activity" — annotated with `GO:0015879 carnitine transport` and nothing else.
Same shape in `Lysosomal_Acid_Phosphatase_Deficiency` ("Lysosomal Acid
Phosphatase 2 Deficiency" → `GO:0016311 dephosphorylation`),
`NAGA_Deficiency_Type_3`, `MGAT2-congenital_disorder_of_glycosylation`,
`Spinocerebellar_Ataxia_Type_2` ("Loss of Ataxin-2 RNA-Binding and Translational
Regulation" → `GO:0006417 regulation of translation`). Nothing new has to be
established for these: the claim is curated, the term is missing.

Of the 698 single-gene landing nodes, **262 already assert the activity in prose**
and 56 assert it in the node name itself.

**2. Several genes on one node — a debundle target, not an annotation gap (274).**
`Primary_Ciliary_Dyskinesia` / "Ciliary Dysfunction" carries **21 genes**:
DNAH5 and DNAH11 are dynein motors, RSPH1/4A/9 are radial-spoke structural
constituents, CCDC39/40 are axonemal rulers, FOXJ1 and MCIDAS are transcription
factors. No single MF term is true of that set, and picking one would fabricate.
Same for `Dilated_Cardiomyopathy` / "Sarcomeric and Cytoskeletal Dysfunction" (31
genes) and `Autosomal_Recessive_Primary_Microcephaly` / "Heterogeneous Biallelic
MCPH Gene Dysfunction" (28 genes). These are the DEBUNDLE TARGETS the
node-classification design already identified: a node needing several classes is
making several claims.

**3. A genuine missing node (266).** Single gene, landing on a cellular or
tissue process, with no activity claim anywhere in the entry — e.g.
`Familial_Hypercholesterolemia` / "PCSK9 Gain-of-Function" → `GO:0006898
receptor-mediated endocytosis`.
Supplying the activity here adds a node and an edge, and needs its own evidence.

**4. A cascade drawn as one node (60; 107 nodes land on a PATHWAY term alone,
149 counting nodes that mix it with another tier).**
`Growth_Hormone_Insensitivity_Syndrome` / "GH-IGF1 Axis Disruption" is the clean
example. Its description already spells the chain out — "GH binds the homodimeric
GH receptor (GHR), activating the receptor-associated kinase JAK2, which
phosphorylates STAT5B; phosphorylated STAT5B dimerizes, translocates to the
nucleus, and drives hepatic transcription of IGF1, IGFBP3, and IGFALS" — while
the graph holds one node with two BP terms. 49 of the 149 PATHWAY-landing nodes
carry descriptions over 400 characters; the chain is frequently written already,
in prose, one field away from being nodes.

## Can the middle level actually be supplied?

For the single-gene cases, yes, and mostly without new literature work: the
molecular function is a property of the gene product, so it comes from GO
directly rather than from the disease. Ten fills drawn from the sample above,
each verified against OLS as a live `molecular_function` term:

| entry | landing node (BP-only today) | proposed `molecular_functions:` |
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

Two of these ten (`GO:0005041`, `GO:0001227`) are already in
`cache/enums/molecularfunctionterm_305077eac108.csv`, so they validate offline;
the rest need one network validation each. The MF enum cache holds 523 terms
against the BP cache's 2,346 — the activity vocabulary in use is about a fifth
the size of the process vocabulary, which is itself a measure of the gap.

The pattern to copy already exists: 404 disorder entries carry at least one
gene-landing node that is MF-bound. `ornithine_aminotransferase_deficiency`,
`Primary_Carnitine_Deficiency`, `Trimethylaminuria` and the other inborn-errors
entries all carry MF and BP on the same node.

## Where filling it in would be wrong

- **Multi-gene nodes.** Covered above: split first, or leave alone.
- **Classes with no shared molecular function.**
  `Autosomal_Recessive_Non-Syndromic_Intellectual_Disability` has a node called
  "Loss of a Gene-Specific Molecular Function Required by Developing Neurons"
  whose description states outright that there are no prevalent genes, pathways
  or complexes and that the affected protein functions are very diverse. The
  absence of an MF term there is the finding.
- **Nodes that are genuinely genomic.** 120 landing nodes take a GENOMIC-class BP
  term (transcriptional regulation, DNA repair). Dosage and silencing claims do
  not have an activity step to insert.
- **Structural proteins.** MF has `GO:0005200 structural constituent of
  cytoskeleton` and relatives, which is right for SPTB but thin for a
  radial-spoke component; `protein_complexes:` may carry the claim better.

Also worth stating plainly: the earlier depth analysis found gene-grounded nodes
at mean depth 0.94 and MF-grounded nodes at 0.81 — statistically the same place.
GENOMIC and ACTIVITY read as **alternative entry points** in the current corpus,
not sequential steps. Inserting activity nodes wholesale would be a change to how
entries open, not just an annotation pass. That is an argument for doing the 372
ANNOTATE_MF cases first (they add a term without touching topology) and treating
the 266 INSERT cases as a separate, evidence-bearing decision.

## Suggested next steps

1. **A term-only tranche.** Work `--verdict ANNOTATE_MF --single-gene-only`,
   starting with the 262 nodes whose prose already asserts the activity. No new
   nodes, no new edges, no new claims — a term for a claim already curated.
2. **Fold the check into the compliance signal.** A single-gene pathophysiology
   node carrying a gene and a BP but no MF is a recommended-field gap of the same
   kind `dismech-compliance` already reports.
3. **Treat the 274 multi-gene nodes as a debundle worklist**, feeding the
   existing node-classification design rather than this one.
4. **Pick two or three PATHWAY nodes as chain pilots** — GH-IGF1 is the obvious
   first, since the chain is already written in its description — and see whether
   the resulting graph reads better before generalizing.

## Reproducing

```bash
just gene-activity-gaps                                        # the census above
just gene-activity-gaps --format tsv --out /tmp/gaps.tsv        # per-node worklist
just gene-activity-gaps --verdict ANNOTATE_MF --single-gene-only --format list
just gene-activity-gaps kb/disorders/Asthma.yaml --format tsv   # one entry
```
