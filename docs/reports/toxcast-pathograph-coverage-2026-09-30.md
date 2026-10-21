# ToxCast assay coverage of the dismech pathograph

How many ToxCast and Tox21 assay endpoints declare a gene target that a dismech pathophysiology node also names, counted from the side of the assays, the nodes, the genes and the diseases. Background: issue #12858; scope and interpretation: `projects/TOXCAST.md`.

A shared gene is a **candidate**, not a mapping. It says an endpoint and a node concern the same gene. It does not say they agree on direction, on the quantity measured, or on mechanism, so every figure below is an upper bound on what could be mapped.

Assay annotations retrieved from the EPA CTX API on **2026-09-30**; `kb/disorders/` as of commit `0aedd3ce8e`. Both move, so treat the numbers as a dated snapshot and regenerate with `just toxcast-coverage`.

## Pathograph node coverage

### From the assay side

| Assay endpoints | Count | Share of panel |
| --- | ---: | ---: |
| In the panel | 1570 | |
| Declare no usable gene target | 462 | 29.4% |
| Declare a gene target | 1108 | 70.6% |
| **Candidates: a target is named by at least one node** | **552** | **35.2%** |
| &nbsp;&nbsp;of which through the human gene | 481 | 30.6% |
| &nbsp;&nbsp;of which through another species' ortholog only | 71 | 4.5% |

Of the endpoints that declare a gene target, 49.8% are candidates. An endpoint with no gene target cannot be found by this join at all, which is not the same as having no node it could speak to: a cell-viability counter-screen declares no gene and may still bear on a cell-death node.

By intended target family, largest first:

| Intended target family | Endpoints | With a gene target | Candidates | Nodes reached | Entries reached |
| --- | ---: | ---: | ---: | ---: | ---: |
| nuclear receptor | 255 | 255 | 164 | 56 | 45 |
| cell cycle | 180 | 18 | 5 | 5 | 4 |
| gpcr | 158 | 158 | 47 | 39 | 33 |
| kinase | 112 | 112 | 55 | 92 | 79 |
| cyp | 78 | 78 | 11 | 6 | 6 |
| cytokine | 72 | 72 | 43 | 20 | 20 |
| dna binding | 71 | 71 | 42 | 104 | 84 |
| neurodevelopment | 64 | 0 | 0 | 0 | 0 |
| background measurement | 55 | 10 | 3 | 6 | 3 |
| zebrafish development | 46 | 0 | 0 | 0 | 0 |
| channel 1 | 45 | 0 | 0 | 0 | 0 |
| channel 2 | 45 | 0 | 0 | 0 | 0 |
| transporter | 45 | 45 | 26 | 18 | 15 |
| protease | 43 | 39 | 22 | 15 | 13 |
| cell adhesion molecules | 32 | 32 | 22 | 14 | 11 |
| ion channel | 32 | 32 | 22 | 28 | 21 |
| phosphatase | 27 | 27 | 8 | 23 | 17 |
| cell morphology | 26 | 3 | 3 | 1 | 1 |
| esterase | 26 | 26 | 5 | 7 | 4 |
| steroid hormone | 24 | 22 | 16 | 16 | 13 |
| oxidoreductase | 17 | 16 | 7 | 12 | 11 |
| neuroactivity | 15 | 0 | 0 | 0 | 0 |
| transcription factor | 15 | 15 | 10 | 7 | 6 |
| transferase | 14 | 14 | 8 | 6 | 5 |
| growth factor | 10 | 10 | 6 | 9 | 9 |
| lyase | 8 | 8 | 6 | 4 | 4 |
| hydrolase | 7 | 7 | 2 | 4 | 4 |
| deiodinase | 4 | 4 | 0 | 0 | 0 |
| misc protein | 4 | 4 | 3 | 7 | 6 |
| cardiomyocyte function | 3 | 0 | 0 | 0 | 0 |
| cytokine receptor | 3 | 3 | 3 | 7 | 7 |
| metabolite | 3 | 0 | 0 | 0 | 0 |
| mitochondria | 3 | 0 | 0 | 0 | 0 |
| protease inhibitor | 3 | 3 | 2 | 1 | 1 |
| stress response | 3 | 3 | 0 | 0 | 0 |
| apoptosis | 2 | 2 | 2 | 1 | 1 |
| dehalogenase | 2 | 2 | 1 | 1 | 1 |
| epigenetic enzyme | 2 | 2 | 1 | 1 | 1 |
| growth factor receptor | 2 | 2 | 0 | 0 | 0 |
| ligase | 2 | 2 | 2 | 2 | 1 |
| membrane protein | 2 | 2 | 0 | 0 | 0 |
| mutagenicity response | 2 | 2 | 0 | 0 | 0 |
| apolipoprotein | 1 | 1 | 1 | 2 | 2 |
| catalase | 1 | 1 | 1 | 1 | 1 |
| enzyme | 1 | 0 | 0 | 0 | 0 |
| filaments | 1 | 1 | 0 | 0 | 0 |
| immunoglobulin | 1 | 1 | 1 | 1 | 1 |
| methyltransferase | 1 | 1 | 1 | 2 | 2 |
| microrna | 1 | 1 | 0 | 0 | 0 |
| oxidase | 1 | 1 | 1 | 1 | 1 |

Nodes and entries are counted once per family, so those two columns do not sum to the totals below: one node can be reached from several families.

### From the node side

| Pathophysiology nodes in `kb/disorders/` | Count | Share of all nodes |
| --- | ---: | ---: |
| All nodes | 22403 | |
| Name at least one HGNC-bound gene | 4021 | 17.9% |
| **Candidates: name a gene some endpoint targets** | **452** | **2.0%** |

That is 11.2% of the nodes that name a gene. Pairing every candidate endpoint with every node it reaches gives **2080 endpoint-node pairs**, which is the size of the job if each candidate were reviewed.

Candidate nodes by `biological_scale`, against all nodes:

| `biological_scale` | Candidate nodes | All nodes | Share of that scale |
| --- | ---: | ---: | ---: |
| MOLECULAR | 186 | 4545 | 4.1% |
| CELLULAR | 37 | 3981 | 0.9% |
| TISSUE | 5 | 3271 | 0.2% |
| ORGANISM | 2 | 2306 | 0.1% |
| (untagged) | 222 | 8300 | 2.7% |

64 of the 452 candidate nodes (14.2%) carry a `genetic_context`, meaning the node records a variant. Those are the nodes most likely to name a lesion where an assay reads a state, which is the first mismatch #12858 describes. The remainder are not thereby cleared: a node can name a lesion in prose without the slot.

## Gene coverage

The panel names **496 distinct gene targets**. 433 are named through the human gene by at least one endpoint; 63 are named only through another species' gene, and join to dismech only where the upper-cased symbol happens to be a human gene's symbol.

| Where the target sits in `kb/disorders/` | Human targets | Ortholog-only targets | All | Endpoints naming one |
| --- | ---: | ---: | ---: | ---: |
| `ON_NODE`: named by a pathophysiology node in at least one entry | 180 | 14 | 194 | 552 |
| `GENETIC_ONLY`: bound in a `genetic:` record, on no node | 31 | 4 | 35 | 93 |
| `ELSEWHERE_ONLY`: bound elsewhere in an entry (a subtype, a treatment, a biomarker), in no `genetic:` record and on no node | 0 | 0 | 0 | 0 |
| `ABSENT`: bound nowhere in `kb/disorders/` | 222 | 45 | 267 | 486 |

Each target takes the first tier it satisfies. The endpoint column can count one endpoint in two rows, because 41 endpoints name more than one gene.

The 20 most-assayed targets, and how far each reaches:

| Target | Endpoints | Tier | Nodes | Entries |
| --- | ---: | --- | ---: | ---: |
| ESR1 | 40 | `ON_NODE` | 8 | 7 |
| AR | 34 | `ON_NODE` | 6 | 4 |
| PPARG | 22 | `ON_NODE` | 4 | 4 |
| NR3C1 | 16 | `ON_NODE` | 1 | 1 |
| PGR | 14 | `ABSENT` | 0 | 0 |
| ESR2 | 13 | `ON_NODE` | 2 | 2 |
| THRA | 13 | `ON_NODE` | 1 | 1 |
| THRB | 13 | `ON_NODE` | 1 | 1 |
| CXCL8 | 10 | `GENETIC_ONLY` | 0 | 0 |
| NR1H4 | 10 | `ON_NODE` | 4 | 3 |
| NR3C2 | 10 | `ABSENT` | 0 | 0 |
| TP53 | 10 | `ON_NODE` | 38 | 36 |
| CCL2 | 9 | `ON_NODE` | 1 | 1 |
| CYP2C19 | 8 | `GENETIC_ONLY` | 0 | 0 |
| NR1I2 | 8 | `ABSENT` | 0 | 0 |
| PPARA | 8 | `ABSENT` | 0 | 0 |
| SRC | 8 | `ABSENT` | 0 | 0 |
| VCAM1 | 8 | `ON_NODE` | 1 | 1 |
| CYP1A2 | 7 | `ABSENT` | 0 | 0 |
| CYP2C9 | 7 | `ABSENT` | 0 | 0 |

The panel is very uneven: 247 targets appear in exactly one endpoint and 12 appear in ten or more.

Symbols the join rewrote, because ToxCast writes them differently from HGNC's approved symbol:

- `FOS|JUN` is read as `FOS` and `JUN`
- `H2AFX` is read as `H2AX`
- `H3F3A` is read as `H3-3A`
- `PPP2R4` is read as `PTPA`

## Disease coverage

| Entries in `kb/disorders/` | Count | Share |
| --- | ---: | ---: |
| All entries | 3256 | |
| **Carry at least one candidate node** | **317** | **9.7%** |
| Bind a target somewhere, on no node | 189 | 5.8% |
| Bind no target | 2750 | 84.5% |

In the middle row the gene is already bound in the entry, typically in `genetic:`, and no pathophysiology node names it. Whether it belongs on a node is a curation question for each entry, not a backfill: a gene on a node asserts that the gene drives that mechanism in that disease.

| Candidate nodes in the entry | Entries |
| --- | ---: |
| 1 | 230 |
| 2-3 | 77 |
| 4 or more | 10 |

The 20 targets reaching the most entries:

| Target | Entries | Nodes | Nodes with a `genetic_context` | Endpoints |
| --- | ---: | ---: | ---: | ---: |
| TP53 | 36 | 38 | 9 | 10 |
| STAT3 | 20 | 21 | 0 | 2 |
| PIK3CA | 18 | 18 | 3 | 1 |
| PTEN | 10 | 15 | 0 | 3 |
| FGFR3 | 9 | 10 | 1 | 2 |
| FGFR1 | 8 | 10 | 0 | 2 |
| GNAS | 8 | 10 | 2 | 2 |
| MYC | 8 | 8 | 2 | 2 |
| ESR1 | 7 | 8 | 1 | 40 |
| JAK2 | 7 | 7 | 2 | 2 |
| TNF | 7 | 7 | 0 | 2 |
| CACNA1A | 5 | 8 | 1 | 4 |
| FAS | 5 | 5 | 0 | 1 |
| HNF4A | 5 | 5 | 0 | 1 |
| IL6 | 5 | 5 | 0 | 3 |
| NR5A1 | 5 | 6 | 0 | 1 |
| PAX6 | 5 | 6 | 0 | 1 |
| TGFB1 | 5 | 5 | 0 | 4 |
| ABL1 | 4 | 4 | 2 | 2 |
| AR | 4 | 6 | 0 | 34 |

## Mechanism modules

Counted apart, because a module is not a disease. 12 of the 898 pathophysiology nodes in `kb/modules/` name a gene some endpoint targets, across 9 of 180 modules.

## Regenerating

```bash
just toxcast-refresh                                 # cache the annotations; needs CTX_API_KEY
just toxcast-coverage                                # this report, to stdout
just toxcast-coverage --format tsv --table targets   # one row per gene target
just toxcast-coverage --format tsv --table nodes     # one row per candidate node
just toxcast-coverage --format tsv --table endpoints # one row per assay endpoint
just toxcast-coverage --format tsv --table diseases  # one row per entry with a candidate node
```

