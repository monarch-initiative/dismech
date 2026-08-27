# Mitochondrial Disease Genetics and Pathograph Integration Review (2026-08-27)

Review of how dismech assigns genes to mitochondrial disease entries, whether that
strategy is complete for mitochondrially encoded genes, and whether the genetics and
the core GO biology actually reach the pathographs.

Motivating question: HGNC and OMIM were both suspected of having incomplete
classification for mitochondrial genes. **HGNC's coverage turns out to be complete;
its *classification* is not usable, and the real gaps are elsewhere.**

## Scope

102 entries qualify as mitochondrial disease: every entry with a curated causal gene
that is mtDNA-encoded or belongs to the nuclear OXPHOS / mtDNA-maintenance / mitochondrial
translation / CoQ / mitochondrial dynamics gene set, plus every entry carrying
`parents: mitochondrial disease`. Together they hold 579 pathophysiology nodes and 276
curated genes.

15 of the 102 are mtDNA-encoded (`MT-*`) disorders; the remaining 87 are nuclear-encoded.

## The gene-assignment strategy, stated

Genes are bound as HGNC CURIEs on `GeneDescriptor.gene_term`, validated by
`linkml-term-validator` against the `GeneTerm` dynamic enum. `GeneTerm` carries **no
`reachable_from` constraint** — unlike `CellTypeTerm` (rooted at `CL:0000000`) or the
NCIT treatment enums, it validates only that the CURIE exists and that `term.label`
matches the canonical HGNC symbol exactly. CURIEs use the repository's lowercase
`hgnc:` form.

OMIM is **not** part of gene assignment. Its 1,165 occurrences in `kb/` are
cross-references (`external_assertions`, `mappings`) and prose. So the suspicion about
OMIM's mtDNA gene-phenotype map does not affect how genes are assigned — but it does
mean OMIM cannot be used to *audit* completeness, since OMIM lumps most mtDNA
phenotypes under allelic variants of a single MIM number rather than distinct
phenotype entries.

## Finding 1 — HGNC covers all 37 mtDNA genes

Checked directly against the OAK `sqlite:obo:hgnc` build: all 37 mitochondrially
encoded genes resolve with correct labels and SO type assignments.

| Class | Count | Example | SO type |
|---|---:|---|---|
| Protein-coding | 13 | `hgnc:7414` MT-ATP6 | `SO:0001217` protein_coding_gene |
| rRNA | 2 | `hgnc:7470` MT-RNR1 | `SO:0001637` rRNA_gene |
| tRNA | 22 | `hgnc:7490` MT-TL1 | `SO:0001272` tRNA_gene |

None missing. HGNC additionally carries 16 non-gene mtDNA control-region features
(`MT-HSP1`, `MT-LSP`, `MT-OHR`, `MT-TER`, `MT-CSB1..3`, `MT-TAS`, `MT-7SDNA`, `MT-ATT`),
which is more than the KB currently needs but is available for D-loop variants.

**There is no identifier-level gap.** The 14 MT genes in `cache/hgnc/terms.csv` are
simply the ones curated so far, not the limit of what validates.

## Finding 2 — HGNC's *classification* of mtDNA genes is unusable here

The gene groups exist but do not form a coherent axis:

- `hgnc.genegroup:1974` covers only the **13 protein-coding** genes.
- tRNA genes sit in `843`, rRNA genes in `1378`. **No superclass unites all 37.**
- In the OAK sqlite build every `hgnc.genegroup:*` node is a label-less stub carrying
  only `rdf:type` — no `rdfs:label`, no group hierarchy.

So a `reachable_from: hgnc.genegroup:1974` dynamic enum would yield an unlabeled,
incomplete set. HGNC cannot answer "is this gene mtDNA-encoded" for dismech.

Nor can SO: `MT-ND1` and `NDUFS4` are both `SO:0001217`. **Genome of origin is not
derivable from any authority dismech currently binds to.** Today the only signal is the
`MT-` symbol prefix, which is a naming convention, not an assertion.

## Finding 3 — heteroplasmy is unmodeled

For an mtDNA disease, heteroplasmy fraction and the tissue-specific threshold are the
genetic parameters that determine penetrance and severity. dismech has no slot for
either:

- `ZygosityEnum` is `HETEROZYGOUS | SIMPLE_HETEROZYGOUS | COMPOUND_HETEROZYGOUS |
  HOMOZYGOUS | HEMIZYGOUS` — no homoplasmic/heteroplasmic values, and zygosity is
  orthogonal to heteroplasmy in any case.
- The word "heteroplasmy" appears in 20 files, always as free text in `description`
  or `notes` — 41 times in `MT-ATP6_MT-ATP8-Related_Infantile_Hypertrophic_Cardiomyopathy`
  alone.

This is a real representational gap, not a curation lapse: curators wrote the biology
into prose because there was nowhere else to put it. See "Recommendation" below; it is
a structural schema decision and is proposed, not enacted, here.

## Finding 4 — 42% of curated genes never reached the pathograph

`graph.py` links a `genetic[]` entry to a mechanism only by matching gene keys against
`pathophysiology[].genes` / `.gene` (`_gene_lookup_keys`, lines 176–191, 371–390). A
pathophysiology node with no `genes:` is therefore invisible to the genetic block, and
the gene renders as a disconnected node.

Before this review:

| Measure | Value |
|---|---:|
| Pathophysiology nodes carrying no `genes:` | 492 / 579 (85%) |
| Curated genes not reachable from any node | 116 / 276 (42%) |
| Entries with ≥1 orphaned gene | 54 |
| Entries whose **entire** genetic block was disconnected | 40 |

Among the 40 were entries *named for their gene* — `COX10-Related_COX_Deficiency`,
`SURF1-Related_Leigh_Syndrome`, `TACO1-Related_COX_Deficiency` — whose proximal node
("COX10 Loss and Defective Heme A Biosynthesis") named the gene in prose while
linking nothing.

## Finding 5 — GO coverage is solid on OXPHOS, thin elsewhere

273 distinct GO terms are used across the 102 entries; **none is obsolete**. Coverage
concentrates on the respiratory chain and falls away outside it:

| GO term | Entries |
|---|---:|
| `GO:0006119` oxidative phosphorylation | 46 |
| `GO:0033617` complex IV assembly | 22 |
| `GO:0032543` mitochondrial translation | 13 |
| `GO:0007005` mitochondrion organization | 11 |
| `GO:0006264` mitochondrial DNA replication | 9 |
| `GO:0008053` mitochondrial fusion | 3 |
| `GO:0000266` mitochondrial fission | 2 |
| `GO:0034551` complex III assembly | 1 |
| `GO:0000423` mitophagy | **0** |
| `GO:0070585` protein localization to mitochondrion | **0** |
| `GO:0008637` apoptotic mitochondrial changes | **0** |
| `GO:0001836` release of cytochrome c from mitochondria | **0** |
| `GO:0006851` mitochondrial calcium ion transmembrane transport | **0** |
| `GO:0051881` regulation of mitochondrial membrane potential | **0** |

Zero mitophagy annotation is the most surprising: `PRKN-Related_Juvenile_Parkinson_Disease`
and `Parkinson_Disease_Mitochondrial` are both in scope. Complex III assembly at 1 entry
against complex IV at 22 is a lopsidedness worth a targeted pass.

Also: 152 / 579 nodes (26%) carry no bound biological process, molecular function, or
cellular component at all. Most are tissue- or organism-scale "energy failure" nodes
(`Kearns-Sayre_Syndrome` has seven), which could carry `GO:0006119` plus an UBERON site
rather than being pure free text.

**One correction to a plausible-looking gap:** `GO:0000002` "mitochondrial genome
maintenance" is **obsolete** with no replacement — GO deliberately split it because it
conflated transport, lipid metabolism, DNA metabolism, fission, and fusion. The KB's
existing use of `GO:0006264` (mtDNA replication) and `GO:0032042` (mtDNA metabolic
process) for the depletion syndromes is correct. `GO:0006626` is likewise obsolete,
replaced by `GO:0070585`.

## Finding 6 — missing inheritance on mtDNA-caused entries

Five entries with a curated mtDNA cause carried no `inheritance:` block at all, so
nothing recorded maternal transmission. `Leigh_Syndrome` was the most consequential:
six curated genes spanning three inheritance modes (mitochondrial `MT-ATP6`, autosomal
recessive `NDUFS4`/`NDUFV1`/`SURF1`/`LRPPRC`, X-linked `PDHA1`) and no inheritance
block to distinguish them.

## What this review changed

37 KB entries changed, all validated (schema, terms, snippets, duplicate keys, entity refs).

**Gene → pathograph links (35 gene links across 34 entries).** Attached the curated causal
gene to the proximal molecular node that was already named for it. Two passes: the node
name contains the HGNC symbol, then the node names the gene *product* instead
(`Twinkle` → TWNK, `DNA Polymerase Gamma` → POLG, `mt-tRNA(Glu)` → MT-TE,
`COX4-1` → COX4I1). This adds 37 `genetic` → mechanism edges (16 → 53 across the changed
entries). No new biological claims — each gene was already curated with evidence in the
same file, and each node was already named for its lesion.

`Pathophysiology` carries **both** a singular `gene:` and a multivalued `genes:` slot,
and `_gene_lookup_keys` reads either, so a node using `gene:` was already linked. An
initial pass that indexed only `genes:` proposed 12 edits to nodes that were already
correctly bound; those were withdrawn before merge and are not in this change. The
duplicate slot is a curation-consistency wart worth a separate look — nothing in the
schema or the checks says which to use, and the KB uses both.

| Measure | Before | After |
|---|---:|---:|
| Genes not reachable from any node | 116 (42%) | 78 (28%) |
| Entries with ≥1 orphaned gene | 54 | 23 |
| Entries fully disconnected | 40 | 6 |

**Inheritance blocks (4 entries).** `Leigh_Syndrome` (three modes: `HP:0001427`,
`HP:0000007`, `HP:0001417`), `NARP_syndrome`, `Adult-Onset_Ataxia_and_Polyneuropathy`,
`Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency` (all `HP:0001427`). Every block
carries its own PMID and verified snippet.

The Reversible Infantile COX Deficiency block records the biologically unusual part
explicitly: m.14674T>C/T>G are **homoplasmic**, so there is no heteroplasmy threshold
and the reversible course reflects developmental compensation rather than a shifting
mutant load.

## Recommendation — a structural slot for heteroplasmy and genome of origin

Proposed, not enacted; it is a schema decision for the register rather than a curation
fix. Shape:

```yaml
genetic:
- name: MT-TL1 m.3243A>G
  gene_term: {preferred_term: MT-TL1, term: {id: hgnc:7490, label: MT-TL1}}
  genome: MITOCHONDRIAL          # GenomeEnum: NUCLEAR | MITOCHONDRIAL
  heteroplasmy:
    state: HETEROPLASMIC         # HOMOPLASMIC | HETEROPLASMIC | BOTH
    threshold_percent: 60
    threshold_tissue: skeletal muscle
    evidence: [...]              # standard EvidenceItem
```

`genome` is the cheaper half and is mechanically derivable for existing entries (the
`MT-` prefix over a closed 37-gene set), which makes it a safe backfill. `heteroplasmy`
is the half that carries biology no other slot can hold, and it needs per-entry
curation from the 20 files that currently state it in prose.

## Follow-ups not taken

- **`Kearns-Sayre_Syndrome` and `Pearson_Syndrome` have no `genetic:` block.** Both are
  single large-scale mtDNA deletion syndromes with no single causal gene, so the
  omission is defensible — but the deletion span is enumerable, and now that all 37
  mtDNA genes validate, the genes removed by the common 4,977 bp deletion could be
  curated explicitly. Needs a reference stating the span; the cached GeneReviews
  (`PMID:20301382`) is abstract-only.
- **`relationship_type` is unset** on causal genes in several entries
  (`Leigh_Syndrome` all six, `MELAS_Syndrome` both, `NARP_syndrome`).
- **6 entries remain fully disconnected** — `Charcot-Marie-Tooth_Disease`,
  `Complex_Hereditary_Spastic_Paraplegia`, `Pheochromocytoma_Paraganglioma`,
  `Multiple_System_Atrophy`, `Chronic_Intestinal_Pseudoobstruction`, `STAT2_Deficiency`.
  All are multi-gene entries where assigning each gene to the right node needs curation
  judgment, not a mechanical rule.
- **`MTO1_Deficiency` lists `MT-TF` as a `MODIFIER`.** MTO1 is a nuclear tRNA-modifying
  enzyme acting on mt-tRNAs; MT-TF is its substrate, not a modifier locus of MTO1
  disease. Worth re-checking against the cited evidence.
- **GO gaps** above — mitophagy, mitochondrial protein import, calcium transport,
  cytochrome c release, complex III assembly.
