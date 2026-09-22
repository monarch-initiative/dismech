# Binding validation gaps

### Terms Inside `qualifiers` Are Not Covered by `validate-terms`

**`linkml-term-validator` does not look inside `qualifiers`.** It validates slots
whose range is bound to an ontology-backed dynamic enum; `Qualifier.predicate`
and `Qualifier.value` are plain `Descriptor`s with no such binding, so their
`term:` blocks are invisible to it. A fabricated label there passes
`just validate-terms` outright — verified by putting
`label: Totally Bogus Fabricated Label` on one and watching it report
"✅ Validation passed" (#10197).

That blind spot had already admitted 32 wrong bindings across 10 entries — 31
CURIE corrections plus one where the code was right and only the label wrong — all
plausible-looking codes naming the wrong concept:

| Curated as | `NCIT` code actually means |
|---|---|
| vancomycin | Azacitidine (an antineoplastic) |
| Broad Spectrum Antibiotic | Arthritis |
| Tooth Extraction | Breast Extraskeletal Osteosarcoma |
| Tracheostomy | Ambulation Difficulty |
| Budesonide | Panobinostat |
| fidaxomicin | Cellular Changes Resembling Foveolar Epithelium Cells |

```bash
just check-qualifier-terms          # gate (offline, in `just qc`)
just list-qualifier-terms           # census, including what nothing can check
just check-qualifier-terms-online   # also resolve uncached CURIEs via OAK
```

The gate is offline and cache-first, so it only sees CURIEs already cached from
elsewhere in the KB. **Run `just check-qualifier-terms-online` after adding a
qualifier term** — a qualifier-only CURIE is never cached by anything else, so
the offline gate has no opinion on it. `RO` and `PR` (109 terms) have no adapter
in `conf/oak_config.yaml` and cannot be validated by any current tooling; the
census reports them separately.

Given all this, prefer a dedicated slot over `qualifiers` wherever one exists —
see the next section, and note that `therapeutic_agent` already covers most of
what these qualifier pairs were expressing.

### A Gene Binding Only Has To Be Self-Consistent (dismech#10948)

`just validate-terms` checks that a `term.label` is HGNC's canonical label for
that `term.id`. Nothing checks that the resolved gene is **the gene the entry
says the record is about**, so this validates clean under both
`linkml-validate` and `linkml-term-validator`:

```yaml
genetic:
- name: THAP11
  gene_term:
    preferred_term: THAP11
    term:
      id: hgnc:20856      # THAP1 — a different gene, causing DYT6 dystonia
      label: THAP1        # ...and the label does agree with the CURIE
```

Two fields directly above the binding say THAP11. The binding says THAP1.
Nothing compared them.

The perverse part is that the *inconsistent* version (`hgnc:20856` labelled
`THAP11`) **is** caught. So filling `label:` in from the ontology — the careful,
responsible-looking thing to do with a CURIE copied out of a deep-research
report — converts a caught error into a silent one.

The path is short, because the two lanes give different guarantees. The research
lane skips the prefix entirely (`--term-skip-prefix HGNC`, because the uppercase
form misresolves through both adapters), so a gene CURIE is **unchecked where it
is emitted**; the KB lane checks the CURIE against its label and nothing else, so
it is **half-checked where it lands**. #10948 reports an OpenScientist run
offering `HGNC:20856` as *THAP11* in four places; that report is not committed
here, but the same identifier is used correctly for THAP1 in
`research/Spasmodic_Dysphonia-deep-research-openscientist.md`, so the confusion
is live in the corpus.

```bash
just list-gene-term-mismatches                                # whole KB (offline)
just list-gene-term-mismatches kb/disorders/Gaucher_Disease.yaml
just list-gene-term-mismatches --format tsv --findings-only
just list-gene-term-mismatches-online                         # ask HGNC about the uncached + advisory rows
```

**Report-only, and deliberately not in `just qc`.** It exits 0 even with
findings. Across the whole KB — twelve-odd thousand gene descriptors, nearly all
HGNC-bound — it finds **no** wrong binding, so there is nothing to gate on yet;
`--strict` exists for whoever decides to gate the confident class later.

**Read the coverage line, not just the finding count.** Offline it compares only
the CURIEs that have a row in `cache/hgnc/terms.csv`, so a few dozen get no
opinion at all rather than a clean one, and a wrong binding among them would be
invisible. `--resolve` fetches those labels and closes that gap; at the time of
writing every one of them comes back clean. A handful of further descriptors bind
mouse `MGI:` orthologs under animal models, which this check structurally cannot
judge; they are reported as `not_hgnc` rather than folded into `uncached`, because
an uncached HGNC CURIE is one `just validate-terms` run from being checkable and
an MGI one never will be.

Exact totals are deliberately not quoted here. They moved by ~100 within a day of
this section being written, because every curation PR that adds an entry adds
bindings — so a number here is stale by construction, while the report's own count
line is current by construction. Run the recipe for figures.

Two finding classes, and the difference between them is what the check can
honestly claim:

| Class | What it means |
|---|---|
| `names_another_gene` | The text names a gene that resolves elsewhere in HGNC, and does not name the gene it binds. Two known genes; the entry disagrees with its own binding. |
| `symbol_unexplained` | The text names no symbol the check can resolve. **Usually benign** — a previous symbol, or a protein/product name. Advisory. |

Offline the confident class needs the *other* gene to be cached, which happens
only because some other entry has bound it — so a row lands in the advisory class
purely because nothing in `kb/` has ever bound the symbol the text names, and
moves to the confident class the day some unrelated curation PR does. Do not
record which side a given example falls on; run the recipe. `--resolve` removes
the dependency by asking HGNC directly: a symbol that is a **synonym of the bound
term** explains the row (`GBA1` → `hgnc:4177`/`GBA` is a *correct* binding the
OBO build lags on, #10102), while a symbol resolving to a **different id**
condemns it (`THAP11` → `hgnc:23194`). A symbol the build has never heard of
leaves the row alone — `WDR34` is absent from `hgnc:28296` (`DYNC2I2`)
altogether, and the build's silence is a fact about the build, not about the
binding.

**The tolerances are load-bearing, so do not tighten them casually.** Dozens of
bindings are model-organism ortholog symbols (`Adnp`, `Pkhd1`, `smchd1`,
including a zebrafish paralog's trailing letter in `inppl1a`) and a few are HLA
serotype detail (`HLA-B27` bound to `HLA-B` — allele-level detail in a gene field
is legitimate, #9017). Without those two classes the real findings would be
buried. Note the serotype rule is restricted to `HLA-*` on
purpose: generalizing it to "the label followed by digits" would excuse `THAP1`
under a `THAP11` entry, which is the exact defect this exists to find. For the
same reason the confident class is decided **before** any tolerance is applied.

Beyond genes, the same shape applies to any descriptor where `preferred_term`
names the entity and `term` binds it. Genes are the sharpest case because the
label is usually an exact symbol.
