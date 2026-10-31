# Searching drugs and environmental factors in DisMech

Written while looking for the chemical exposures associated with Parkinson's disease and
the drugs used to treat it — two questions that sound symmetrical and are not. Either one
depends on knowing where drugs and environmental factors actually sit in the schema, which
is less obvious than it looks. Parkinson's shows why: `Parkinsons_Disease.yaml` binds its
exposure side as `ECTO:0000530 exposure to pesticide`, a class-level exposure event that
names no chemical and that only three entries share, while levodopa is bound as a specific
substance (`CHEBI:15765`) on 34 entries as a therapy. No single query returns both. This
note covers the schema and the search, not one disease.

dismech at commit [`c31a6b6`](https://github.com/monarch-initiative/dismech/commit/c31a6b6edd5ce59b55b0f4ded9d36320f724d433)
(2026-10-20). The tree moves with every curation PR, so re-run rather than quoting these
figures.

Measurements:
- 3,915 files parsed from `kb/disorders/`, `kb/modules/`, `kb/groupings/`.
- 29,611 bindings & 3,573 distinct terms, across CHEBI, NCIT, ECTO, XCO, ENVO and FOODON.

## Drugs and exposures have no cross-entry *record*, but the bound CURIEs are indexed

`kb/` has a directory per cross-cutting entity for some kinds and not others:

| Entity | Cross-entry home |
|---|---|
| Genes | `kb/genes/curated/`, `kb/genes/ingest/`, `kb/gene_classifications/` |
| Pathograph node classes | `kb/node_classes/` |
| Comorbidities | `kb/comorbidities/` |
| Surrogate endpoints | `kb/surrogate_endpoints/` |
| Modules, groupings, module collections | `kb/modules/`, `kb/groupings/`, `kb/module_collections/` |
| **Drugs, chemicals, exposures** | **no record directory** |

So no drug or exposure has a record of its own: every one exists as a nested object inside a
Disease entry, and there is no page to open to ask "what does dismech say about levodopa?"
The schema tree below shows where they sit; for a full worked entry, see *The load-bearing
distinction: disease vs agent* in
[`occupational-environmental-classifications.md`](occupational-environmental-classifications.md).

### Where a drug or exposure can be expected to be found

Every place in the `Disease` class that binds a chemical, drug or exposure term, with the
vocabulary each accepts and how heavily it is used. Counts are bindings · distinct terms ·
files, from the inventory run described below.

```text
Disease
│
├── treatments: [Treatment]                      THE DRUG LIVES HERE
│   ├── name                                     string; a clinical concept, NOT the drug
│   └── treatment_term: TreatmentDescriptor
│       ├── term                                 NCIT    14,784 ·  460 · 3,477
│       │                                        the ACTION (Pharmacotherapy, …), not the drug
│       ├── therapeutic_agent: [ChemicalEntityDescriptor]   ◄── search HERE for a drug
│       │   └── term                             CHEBI    4,674 ·            2,182 files
│       │                                        NCIT     1,891   drug classes, biologics
│       ├── regimen_term                         NCIT        23 ·   15 ·    19
│       ├── dietary_modifications[].food         FOODON       7 ·    7 ·     3
│       └── qualifiers[].value                   CHEBI/NCIT 206 ·   50 ·   125
│
├── environmental: [Environmental]               THE EXPOSURE LIVES HERE
│   ├── name                                     string
│   ├── exposure_term                            ECTO/XCO   679 ·  192 ·   397
│   │                                            an exposure EVENT, not a substance
│   │   └── qualifiers[].value                   CHEBI       19 ·   12 ·     9
│   ├── environment_context                      ENVO        27 ·   16 ·    19
│   ├── food_source                              FOODON      14 ·   13 ·     8
│   ├── exposure_classifications                 six ENUM axes, no CURIE
│   │                                            44 blocks in 24 files
│   └── influences_mechanisms[]                  → pathophysiology[].name
│
├── pathophysiology: [Pathophysiology]           THE CHEMICAL AS MECHANISM PARTICIPANT
│   ├── name                                     the pathograph node
│   ├── chemical_entities[].term                 CHEBI    1,088 ·  458 ·   382
│   └── triggers[].term                          CHEBI/ECTO  12 ·   12 ·    10
│
├── biochemical: [Biochemical]                   THE CHEMICAL AS MEASURED ANALYTE
│   ├── biomarker_term                           CHEBI/NCIT 900 ·  485 ·   390
│   └── mappings_list[].term                     CHEBI       10 ·    8 ·     5
│
├── datasets: [Dataset]
│   └── exposures[].term                         ECTO         5 ·    4 ·     3
│
├── computational_models: [ComputationalModel]
│   └── variables[].mappings_list[].term         CHEBI/NCIT   6 ·    6 ·     3
│
├── infectious_agent: [InfectiousAgent]
│   └── food_source                              FOODON       1 ·    1 ·     1
│
└── discussions: [Discussion]                    PROPOSED, not asserted
    └── proposed_experiments[].perturbations[]
        ├── chemical_entities[].term             CHEBI        6 ·    6 ·     1
        ├── exposure_term                        ECTO         4 ·    4 ·     2
        └── treatment_term                       NCIT         4 ·    4 ·     4
```

Three things follow for a search:

- **The two main homes take different vocabularies.** `therapeutic_agent` is CHEBI or NCIT;
  `exposure_term` is ECTO or XCO. A drug and the exposure to it are different CURIEs.
- **The heaviest-bound path is not the drug.** `treatment_term.term` outnumbers
  `therapeutic_agent` more than two to one and holds the action, not the substance.
- **`exposure_classifications` holds no CURIE at all**, so a term search never returns it;
  see [*Environmental Factors*](#environmental-factors) below.

### The bound-term index

**A bound-term index does exist, and it is easy to overlook.** `cache/<prefix>/terms.csv` is
committed, one row per CURIE bound anywhere in the KB, with columns `curie,label,retrieved_at`:

| Cache | Rows |
|---|---|
| `cache/ncit/terms.csv` | 2,140 |
| `cache/chebi/terms.csv` | 1,431 |
| `cache/ecto/terms.csv` | 185 |
| `cache/foodon/terms.csv` | 22 |
| `cache/xco/terms.csv` | 23 |

That is the fast first pass for "is this chemical bound at all", and it is far cheaper than
parsing 3,915 YAML files.

Two caveats carry over from `CLAUDE.md`, and both are load-bearing:

- **An absent row is silence, not a negative answer.** The cache holds what the KB has already
  bound, so a chemical nobody has curated yet is missing from it for that reason alone.
- The cache tells you a CURIE is bound *somewhere*, not where or in what role. For that you
  still need the per-entry scan the scripts below do.
- A row being present is not proof it is current either. The label is what the KB accepted when
  the row was written, which `retrieved_at` dates; `migrate-cache` is what moves it.

### Environmental Factors

`ExposureClassifications` has six slot options, which follow. Usage is thin: across 1,391
`environmental[]` entries in `kb/disorders/` and `kb/modules/`, only **44 carry an
`exposure_classifications` block at all**, in 24 files:

| Axis | Values recorded |
|---|---|
| `exposure_duration` | 45 |
| `hazard_agent_type` | 44 |
| `exposure_route` | 44 |
| `exposome_domain` | 21 |
| `ghs_health_hazard_class` | 9 |
| `iarc_carcinogen_group` | 4 |

For exposure work these are the most directly usable fields in the schema — route, duration
and hazard class are what separate an occupational pesticide exposure from a dietary residue,
which `exposure to pesticide` alone cannot — but at 44 of 1,391 entries they are not yet a
search surface.

## Recipe: how to search for a drug or environmental factor

### The query sequence, against the schema it touches

Four stages. The left column is what the query does; the right is the part of the schema tree
above that each stage reads. `drug_exposure_query.py` performs all four in one pass.

```text
  QUERY SEQUENCE                       SCHEMA IT READS
  ──────────────                       ───────────────

  input   a drug, an environmental factor, or either as a CURIE
          "levodopa" · CHEBI:15765 · ECTO:0000530
            │
            ▼
  1. RESOLVE ──────────────────────►   cache/chebi/terms.csv   ┐ substance
     name ─► CURIE(s)                  cache/ncit/terms.csv    ┘
     one name can be several           cache/ecto/terms.csv    ┐ exposure
     CURIEs in two vocabularies        cache/xco/terms.csv     ┘ EVENT
     that do not join                  cache/foodon/terms.csv
            │
            │  matched by: exact CURIE · term label · holder name
            ▼
  2. LOCATE ───────────────────────►   treatments[]
     every slot that can hold it         └ treatment_term
     role = the block it sits in              ├ .therapeutic_agent[].term  ◄ THE DRUG
                                              └ .term                        the action
       therapy                           environmental[]
       exposure                            ├ exposure_term.term           ◄ THE EXPOSURE
       mechanism_node                      ├ environment_context.term
       analyte                             └ food_source.term
       dataset                           pathophysiology[]
       model_variable                      ├ chemical_entities[].term
       proposed  (never asserted)          └ triggers[].term
                                         biochemical[].biomarker_term.term
            │
            ▼
  3. FOLLOW ───────────────────────►   treatments[].target_mechanisms[]
     holder ─► pathograph node             ├ target          ─────────┐
     with direction and link type          └ treatment_effect         │
                                         environmental[].influences_mechanisms[]
       INHIBITS · TRIGGERS                   ├ target        ─────────┤
       EXACERBATES · PREDISPOSES             ├ environmental_effect   │
       DIRECT · INDIRECT_*                   └ causal_link_type       │
            │                                                        ▼
            │                              pathophysiology[].name  ◄ the FK must
            │                              phenotypes[].name         resolve here
            ▼
  4. REPORT
     disease × role × mechanism
     + does it act as BOTH drug and exposure?
       · across the KB      (different CURIEs, different entries)
       · in the same entry  (rare; the two claims are never reconciled)
```

Stage 3 is the one that makes this a mechanism query rather than a term lookup: without it you
learn which diseases mention a chemical, not what it is claimed to do. Stage 4's dual-role
check is asked at two scopes because a drug and the exposure to it are different CURIEs, so
"both roles" is usually true of the *term* and false of any single entry.

### Step by step

Run everything from the repository root. `uv run` builds the project venv on first use, so no
interpreter path is needed, and every script defaults `--repo` to its own checkout — which
matters in a worktree, where a hard-coded path would silently query a different one.

**The short version.** One command does all four stages of the sequence above:

```sh
uv run python scripts/drug_exposure_query.py --term levodopa
```

The longer path. Steps 1 and 2 get a good name and CURIE into step 3, which is the short
version above. Steps 4 to 6 are not continuations of it — each answers a question
`drug_exposure_query.py` does not:

1. **Grep the term caches first.** `grep -i <name> cache/{chebi,ncit,ecto,xco,foodon}/terms.csv`
    answers "is this bound anywhere" in one command. Remember an absent row is silence, not a
    negative answer — see [*The bound-term index*](#the-bound-term-index).

    ```sh
    # The clinical name alone misses the CHEBI label:
    grep -i levodopa cache/{chebi,ncit,ecto,xco,foodon}/terms.csv
    # cache/chebi/terms.csv:CHEBI:3396,Carbidopa-levodopa,2026-08-04T20:05:32.515244
    # cache/ncit/terms.csv:NCIT:C611,Levodopa,2026-10-03T04:58:28.962202

    # Both spellings find the substance itself:
    grep -iE "l-dopa|levodopa" cache/{chebi,ncit,ecto,xco,foodon}/terms.csv
    # cache/chebi/terms.csv:CHEBI:15765,L-dopa,2026-03-08T15:53:02.773504
    # ...and three more, including CHEBI:16852 L-dopaquinone

    # A herbicide nobody has bound — no output at all, exit status 1:
    grep -i trifluralin cache/{chebi,ncit,ecto,xco,foodon}/terms.csv
    ```

    The first two cases are the label trap in miniature: `CHEBI:15765` is the substance the
    treatments actually point at, and grepping the clinical spelling alone does not return it.

2. **Resolve the name to a CURIE before searching the KB**, and do not assume the bound label
    matches clinical usage — CHEBI's canonical label may be a systematic name. Search the
    pinned local build, not OLS: `uv run runoak -i sqlite:obo:chebi search "levodopa"`. For
    ECTO, vary the spelling (`l~anaesthetic` and `l~anesthetic` return different sets) and
    re-run your searches before asserting a term does not exist — both traps are recorded in
    `CLAUDE.md`.

3. **Query the term for diseases and mechanisms.** Pass the name, the CURIE, or both:

    ```sh
    uv run python scripts/drug_exposure_query.py --term levodopa --term "L-dopa" \
      --curie CHEBI:15765 --curie NCIT:C611
    ```

    `--term` is a case-insensitive substring on the bound term's label, the descriptor's
    `preferred_term` and the holder's name; `--curie` is exact. Both are repeatable. The
    `preferred_term` is what catches a substance bound under a systematic label — `levodopa`
    finds `CHEBI:15765 L-dopa` because the agent descriptor prefers the clinical name — but
    passing the CURIE too is still the safer habit. About 2.5 s — a raw-text prefilter means
    only the handful of files that could match are parsed.

4. **Inventory the bindings across the whole KB** when the question is coverage rather than one
    term. Cover **all** the vocabularies: CHEBI *and* NCIT for therapy, mechanism and
    biochemical; ECTO, XCO, ENVO and FOODON for exposure. A chemical absent from one is not
    absent from the KB.

    ```sh
    uv run python scripts/chemical_binding_inventory.py \
      --prefix CHEBI --prefix NCIT --prefix ECTO --prefix XCO --prefix ENVO --prefix FOODON \
      --curie CHEBI:15765 --curie ECTO:0000530
    ```

5. **Locate the string matches by schema path** when grep finds a name but step 3 returns
    nothing, or a hit looks doubtful. It matches strings rather than CURIEs, reports the schema
    path of each one, and lists the CURIEs bound under the holding object, so you can tell a
    curated identity from a mention that is only prose.

    ```sh
    uv run python scripts/entity_path_locator.py --term levodopa --term trifluralin
    ```

6. **Read the enum axes separately** if route, duration or hazard class matter. They hold no
    CURIE, so no stage of the sequence reaches them — this is a gap in the query's coverage
    rather than a step in it. The axes and how thinly they are used are in
    [*Environmental Factors*](#environmental-factors).

## Scripts

All three live in `scripts/` in this repository. Each takes its targets as arguments, defaults
`--repo` to the checkout it sits in, and records that checkout's commit in its output, so a
report says which tree and which commit produced it. Each also has a `just` recipe in the `QC`
group, which is the shorter way in; both forms take the same arguments, and either runs from
the repository root:

```sh
just drug-exposure-query --term levodopa
uv run python scripts/drug_exposure_query.py --term levodopa
```

- `drug_exposure_query.py` — `just drug-exposure-query`
- `chemical_binding_inventory.py` — `just chemical-binding-inventory`
- `entity_path_locator.py` — `just entity-path-locator`

| Script | Answers | Scope and cost |
|---|---|---|
| `drug_exposure_query.py` | For one drug or environmental factor: which diseases carry it, in which role, and which pathograph nodes it acts on, with direction and link type. Plus whether it acts as both a drug and an exposure, asked across the KB and within a single entry. | One term. ~2.5 s, prefiltered. |
| `chemical_binding_inventory.py` | Every nested ontology binding by schema path, role and prefix; which terms are multi-role; reverse lookup from CURIE to entries. The reverse lookup is the part no `just` recipe offers. Does not read the enum axes. | Whole KB, ~1.5 min. |
| `entity_path_locator.py` | For a named entity, the schema path of every string match, and which CURIEs are bound under the holding object's term-bearing slots, so a curated identity can be told from a prose mention. | Whole KB, ~1.5 min. |

Every script writes markdown by default and takes `--out`. `drug_exposure_query.py` also takes
`--format tsv` for a row per disease × role × mechanism, and `--format json`;
the other two take `--json` alongside `--out`.

```sh
# One term: diseases, roles, and the mechanisms it acts on.
uv run python scripts/drug_exposure_query.py --term levodopa --term "L-dopa" \
  --curie CHEBI:15765 --curie NCIT:C611

# The same, as rows, for downstream filtering.
uv run python scripts/drug_exposure_query.py --term levodopa \
  --format tsv --out /tmp/levodopa.tsv

# A chemical with no binding anywhere: 0 files parsed, nothing matched.
uv run python scripts/drug_exposure_query.py --term trifluralin

# Whole-KB binding inventory, with a reverse lookup on a drug and an exposure.
uv run python scripts/chemical_binding_inventory.py \
  --prefix CHEBI --prefix NCIT --prefix ECTO --prefix XCO --prefix ENVO --prefix FOODON \
  --curie CHEBI:15765 --curie ECTO:0000530 \
  --out /tmp/bindings.md --json /tmp/bindings.json

# Triage a grep hit list by schema path.
uv run python scripts/entity_path_locator.py --term levodopa --term trifluralin
```

## Prior art

Four dismech documents already cover parts of the data model and the queries described here.
Read them before extending anything in this note.

- [`occupational-environmental-classifications.md`](occupational-environmental-classifications.md)
  — *The load-bearing distinction: disease vs agent* separates what the disease is classified
  as from what the hazardous agent is — "agent" in that document meaning the causal substance
  or physical factor, not an AI agent.
- [`explanation/design-decisions.md`](explanation/design-decisions.md) — *4. Ontology
  constraints* holds the per-domain prefix table, mirroring `conf/oak_config.yaml`: ChEBI
  for chemicals, NCIT for treatments, ECTO/ExO/XCO for exposures, ENVO for environment,
  FOODON for food. The therapy-versus-exposure vocabulary split this note works around is
  a recorded decision, not an accident of curation.
- [`explanation/ontology-caches.md`](explanation/ontology-caches.md) — *Why we commit cache
  files* and *Cache structure* document the `cache/<prefix>/terms.csv` layout that step 1
  greps. *Anti-patterns* is the one to read before touching them: never hand-edit a cache
  CSV, and never `git add -A` from a worktree.
- [`reports/diet-representation-audit-2026-09-01.md`](reports/diet-representation-audit-2026-09-01.md)
  — the closest prior example of a census of this kind. *Ontology binding — the secondary
  axis* reports bound-versus-free-text rates per track. *Treatment-side inconsistency*
  records the NCIT action-term scatter, `NCIT:C15986` pharmacotherapy among them, which is
  why a holder name can match a query that the bound substance does not. *Method and its
  limits* explains why an `environmental[]` description is signal where a `treatments[]`
  one is not.

Three `just` recipes cover adjacent censuses: `just environmental-term-audit` for ECTO/XCO
coverage, `just diet-audit` for the two-track diet census, and `just tk-node-census` for where
exposures land on toxicokinetic nodes. None takes a drug name and returns the entries using
it, which is the gap the scripts above fill.
