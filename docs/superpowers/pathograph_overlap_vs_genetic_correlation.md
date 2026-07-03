# Pathograph overlap as a qualitative mirror of shared heritability

Prototype motivated by Zhao et al., *Nature Genetics* (2026),
"Pleiotropic shared heritability quantifies the shared genetic variance of
common diseases" (doi:10.1038/s41588-026-02607-w).

## Idea

That paper's method (PHBC) quantifies *how much* genetic variance a target
disease shares with a set of auxiliary diseases (a scalar, `h2_pleio/h2`), but
has no representation of *what* is shared. dismech is the complementary layer:
every disorder is a **pathograph** (pathophysiology nodes annotated with cell
types, biological processes, genes, phenotypes, and causal edges). The
primitive operation is therefore a pairwise **overlap(A, B)** — intersect two
pathographs into a pair-specific subgraph of shared mechanism. Pre-curated
mechanism modules (`kb/modules/`) are just the overlaps recurrent enough to be
worth naming; the overlap function needs no module to run on an arbitrary pair.

## Method (`scripts/pathograph_overlap.py`)

- Extract mechanistic terms (CL, GO, gene symbols, HP) from every disorder
  pathograph (1,214 disorders, ~7,300 unique terms).
- **Specificity inference:** IDF-weight terms over the corpus so ubiquitous
  mechanisms (inflammation, apoptosis, seizure) self-decay and specific shared
  mechanisms dominate.
- **Near-parent inference:** optionally expand each term to its 2-hop `is_a`
  ancestors (OAK), then recompute IDF on the expanded corpus, so over-generic
  ancestors self-cancel while a shared *moderately specific* ancestor connects
  diseases that used different child terms.
- Score = symmetric weighted Jaccard (>= 2 shared terms required).

Run:
```bash
python3 scripts/pathograph_overlap.py            # corpus stats + top pairs
python3 scripts/pathograph_overlap.py validate   # vs genetic rg (exact match)
python3 scripts/pathograph_overlap.py validate-expand  # + near-parent inference
```

## Result

Against 22 disease pairs with published LDSC genetic correlations (illustrative
literature consensus; see `RG_PAIRS` in the script), spanning strong to
near-zero:

| metric | exact match | + near-parent |
|---|---|---|
| Spearman rho(\|rg\|, overlap) | 0.40 | 0.50 |
| mean overlap, strong pairs (\|rg\| >= 0.30) | 0.109 | 0.134 |
| mean overlap, near-zero controls (\|rg\| < 0.15) | 0.020 | 0.044 |
| Schizophrenia <-> Bipolar (rg 0.68) | 0.000 | 0.046 (recovered) |

Overlap tracks genetic correlation; near-parent inference improves the rank
correlation and recovers pairs exact matching missed. Near-zero-rg negative
controls correctly sit near-zero overlap.

## Most actionable output: high-rg / zero-overlap pairs = curation gaps

**Type 2 Diabetes <-> Coronary Artery Disease: rg ~ 0.35, overlap = 0.000**
even after ancestor expansion. The two pathographs share no annotated mechanism
because CAD is curated around atherosclerotic-plaque/foam-cell biology and T2D
around insulin/beta-cell biology; the connecting insulin-resistance ->
endothelial-inflammation layer is not yet curated. Established genetics asserts
shared mechanism the KB has not captured — a ranked, evidence-backed curation
to-do list.

## Caveats / next steps

- The rg table is hand-curated literature consensus, not a harmonized pull;
  swap for a real genetic-correlation source (e.g., LDSC atlas / LD Hub) for a
  systematic test.
- Gene matching is by symbol from the `genetic` section; could be tightened to
  HGNC ids.
- Ancestor expansion is is_a only and 2 hops; a Resnik-style information-content
  measure over most-specific common ancestors is the principled successor.
- Generate the full ranked high-rg / low-overlap gap list across all pairs to
  drive curation priorities.
