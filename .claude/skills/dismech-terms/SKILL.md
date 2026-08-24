---
name: dismech-terms
description: >
  Skill for adding and validating ontology term references in the dismech knowledge base.
  This skill should be used when working with disorder YAML files that need ontology term
  annotations (HPO for phenotypes, CL for cell types, GO for biological processes, MONDO
  for diseases, UBERON for anatomical entities). Use this skill when adding phenotype_term,
  cell_types term, biological_processes term, or other ontology-bound fields to disorder files.
---

# DisMech Ontology Terms Skill

## Overview

Add and validate ontology term references in the dismech disorder knowledge base. This ensures
phenotypes, cell types, biological processes, and other entities are properly linked to
authoritative ontology terms with correct IDs and labels.

## When to Use

- Adding `phenotype_term` to phenotype entries (uses HP - Human Phenotype Ontology)
- Adding `term` to `cell_types` entries (uses CL - Cell Ontology)
- Adding `term` to `biological_processes` entries (uses GO - Gene Ontology)
- Adding `disease_term` to disease entries (uses MONDO)
- Validating existing ontology term references
- Fixing label mismatches between preferred_term and ontology labels

## Term Object Structure

All term references follow this YAML structure:

```yaml
# For phenotypes:
phenotype_term:
  preferred_term: <Human readable name>
  term:
    id: HP:XXXXXXX
    label: <Exact HP label from ontology>

# For cell types:
cell_types:
- preferred_term: <Human readable name>
  term:
    id: CL:XXXXXXX
    label: <Exact CL label from ontology>

# For biological processes:
biological_processes:
- preferred_term: <Human readable name>
  term:
    id: GO:XXXXXXX
    label: <Exact GO label from ontology>
```

## Ontology Lookup with OAK

Use the Ontology Access Kit (OAK) to look up terms:

### Exact Match
```bash
uv run runoak -i sqlite:obo:hp info "seizure"
# Returns: HP:0001250 ! Seizure
```

### Fuzzy Search
```bash
uv run runoak -i sqlite:obo:hp info "l~cognitive impairment"
# Returns multiple matches - select the most appropriate
```

### Get Full Term Details
```bash
uv run runoak -i sqlite:obo:cl info CL:0000540 -O obo
# Returns complete term information including definition
```

### Common Ontology Prefixes
| Ontology | Prefix | CLI adapter | Use For |
|----------|--------|-------------|---------|
| Human Phenotype | HP | sqlite:obo:hp | phenotype_term |
| Cell Ontology | CL | sqlite:obo:cl | cell_types |
| Gene Ontology | GO | sqlite:obo:go | biological_processes |
| MONDO Disease | MONDO | sqlite:obo:mondo | disease_term |
| Uberon Anatomy | UBERON | sqlite:obo:uberon | anatomical locations |

**These are CLI conveniences, not a mirror of `conf/oak_config.yaml`.** That file
configures *automated term validation*, where these prefixes are all served over
`ols:` to avoid large local downloads. The `sqlite:obo:*` adapters above are for
your own ad-hoc `runoak` lookups, and are deliberate:

- `-O obo` output is **not implemented** for `ols:` adapters (it raises
  `NotImplementedError`), so any example using it needs a local build.
- Plain `info` and `search` do work over `ols:` — e.g.
  `uv run runoak -i ols:hp info HP:0002014`. Prefer that for a one-off lookup if
  you would rather not download the build (`hp` is ~1.1 GB, `chebi` ~3.7 GB).

Either way, what a lookup tells you is the same **for these five prefixes** —
`just validate-terms` remains the authority on whether a binding is valid.

### ECTO and XCO are the exception: search the LOCAL build, not OLS

For the prefixes above, `conf/oak_config.yaml` serves validation over `ols:`, so
an OLS lookup and the validator see the same ontology. **ECTO and XCO are
configured as `sqlite:obo:ecto` / `sqlite:obo:xco` — pinned local builds.** OLS
serves a *newer* ECTO, so an OLS search will happily hand you terms the validator
cannot see.

This is not a hypothetical. In #8430 the OLS ECTO offered a whole
`ECTO:30000xx` organism-exposure branch — `exposure to Campylobacter jejuni`,
`... Staphylococcus aureus`, `... Pseudomonas aeruginosa`, `... Zika virus` and
more. Every one of them:

- returned HTTP 200 from the OLS API, non-obsolete, `is_defining_ontology: true`
- resolved under `runoak -i ols:ecto info`
- was correctly reachable from `ExO:0000002`, the `ExposureTerm` enum root

…and every one failed `just validate-terms`, because the local build stops at
`ECTO:3000009`. Same for `ECTO:9002228` (allopurinol) and `ECTO:9002593`
(sertraline). Fourteen bindings had to be reverted.

So for an exposure term, check the build the validator actually reads:

```bash
uv run runoak -i sqlite:obo:ecto info ECTO:0000006 -O obo   # not ols:ecto
uv run runoak -i sqlite:obo:ecto search 'l~exposure to dust'
```

To see what a branch actually contains locally before planning a tranche:

```bash
uv run runoak -i sqlite:obo:ecto descendants ECTO:3000000 -p i
```

**General rule:** before trusting any lookup, check which adapter
`conf/oak_config.yaml` maps that prefix to, and search *that*. A term that
"exists" in an ontology the validator does not read is not a term you can bind.
`just environmental-term-audit` sizes the exposure-binding gap.

### XCO terms flagged `Not4Curation`

RGD keeps XCO terms for hierarchy that it does **not** want annotated with, and
marks them with a related synonym reading `Not4Curation` — a synonym, not an
obsoletion axiom. Such a term exists, has a matching label, and is reachable
from `XCO:0000000` (the XCO root among the `ExposureTerm` enum's `source_nodes`;
`ExO:0000002` is the ECTO one), so `just validate-terms` passes it. Twenty-four XCO terms
carry the marker, and three of them (`XCO:0000294` estrogen/estrogen analog,
`XCO:0000950` anticonvulsant, `XCO:0000561` antidepressant) got into the #8430
tranches before a reviewer noticed (#8472).

`just check-not4curation` gates this in `just qc` and CI, so you do not have to
remember — but if you are choosing an XCO term by hand, check it first, because
the flagged ones are exactly the broad drug-class terms an exposure binding
reaches for:

```bash
just check-not4curation --list-flagged --prefix XCO   # the whole deny-list
uv run runoak -i sqlite:obo:xco info XCO:0000294      # synonyms include Not4Curation
```

All three found so far had proper ECTO equivalents (`XCO:0000294` →
`ECTO:9000010` exposure to estrogens), so a flag is a prompt to look in ECTO
rather than a dead end.

## Specificity Guidelines

**Critical**: Always use the most specific term that accurately describes the entity:

| Incorrect (too general) | Correct (specific) |
|------------------------|-------------------|
| CL:0000066 epithelial cell | CL:0002202 epithelial cell of tracheobronchial tree |
| HP:0000001 All | HP:0001250 Seizure |
| CL:0000000 cell | CL:0000540 neuron |

When a fuzzy search returns multiple results:
1. Review all candidates
2. Check term definitions with `-O obo` flag
3. Select the term that most precisely matches the biological context
4. If no specific term exists, use the closest parent but note the limitation

## Validation

After adding terms, validate the file you edited with:

```bash
just validate-terms kb/disorders/YourDisease.yaml
```

This checks:
- Term IDs exist in the ontology
- Labels match the canonical ontology labels exactly
- Required fields are present

### Fixing Label Mismatches

If validation reports a label mismatch:
```
LABEL MISMATCH: Cholera.yaml
  Term: HP:0003394
  Expected: Muscle cramps
  Actual: Muscle spasm
```

Update the `label` field to match the ontology's canonical label exactly.

## Batch Processing

To find entries missing term annotations:

```python
import yaml
import glob

for f in glob.glob("kb/disorders/*.yaml"):
    with open(f) as file:
        data = yaml.safe_load(file)
    for pheno in data.get('phenotypes', []):
        if 'phenotype_term' not in pheno:
            print(f"{f}: {pheno.get('name')} - missing phenotype_term")
```

## Common Patterns

### Adding HPO to a Phenotype
1. Look up term: `uv run runoak -i sqlite:obo:hp info "l~<phenotype name>"`
2. Verify specificity: `uv run runoak -i sqlite:obo:hp info <HP:ID> -O obo`
3. Add to YAML:
   ```yaml
   phenotype_term:
     preferred_term: <Original Name>
     term:
       id: <HP:ID>
       label: <Exact label from OAK>
   ```
4. Validate: `just validate-terms kb/disorders/YourDisease.yaml`

### Descriptor Qualifiers for Common Clinical Modifiers

When a base ontology term needs common clinical qualification, prefer the explicit
descriptor slots instead of the deprecated generic `qualifiers` list:

```yaml
phenotype_term:
  preferred_term: Diarrhea
  term:
    id: HP:0002014
    label: Diarrhea
  temporality: CHRONIC

phenotype_term:
  preferred_term: Muscle weakness
  term:
    id: HP:0001324
    label: Muscle weakness
  clinical_course: PROGRESSIVE

phenotype_term:
  preferred_term: Meningitis
  term:
    id: HP:0001287
    label: Meningitis
  severity: SEVERE
  onset:
    onset_category: NEONATAL
```

Enum values with ontology `meaning` mappings:
- `temporality`: `ACUTE` = `HP:0011009`, `TRANSIENT` = `HP:0025153`,
  `SUBACUTE` = `HP:0011011`, `CHRONIC` = `HP:0011010`, `RECURRENT` = `HP:0031796`,
  `DIURNAL` = `HP:0025302`, `NOCTURNAL` = `HP:0025301`, `PROLONGED` = `HP:0025297`
- `clinical_course`: `PROGRESSIVE` = `HP:0003676`, `STABLE` = `HP:0031915`
- `severity`: `MILD` = `HP:0012825`, `MODERATE` = `HP:0012826`, `SEVERE` = `HP:0012828`

Prefer a precoordinated ontology term when one already exists; otherwise add the
qualifier in these dedicated slots.

### Adding CL to Cell Types
1. Look up term: `uv run runoak -i sqlite:obo:cl info "l~<cell type>"`
2. Verify specificity
3. Add `term:` block under the cell_type entry
4. Validate

## ECTO Exposure Terms: Disconnected Branches, Not Specificity Ladders

Smoking and alcohol each have **two** ECTO terms in use in the KB. It is tempting to
read each pair as a specificity ladder — a general term and a narrower one — but that
is not what the ontology says. In each pair the two terms sit in **disconnected
branches**, so neither is a refinement of the other, and "promoting" or "demoting"
between them is not a meaningful operation.

Look up a term two ways before reasoning about it, because they answer different
questions. `ancestors -p i` gives the branch it lives in; `info -O obo` gives its
`RO:0002309` ("involving") anchor, which is what the term is actually *about*:

```bash
uv run runoak -i sqlite:obo:ecto ancestors ECTO:9000027 -p i   # branch
uv run runoak -i sqlite:obo:ecto info      ECTO:9000027 -O obo # direct is_a + anchor
```

Unlike the prefixes in the table above, ECTO and XCO are served from the local build
for automated validation too (`conf/oak_config.yaml`: `ECTO: sqlite:obo:ecto`),
because the builds are small — so there is no `ols:` alternative to fall back on here.

| CURIE | Label | Direct `is_a` | "Involving" anchor | Anchor kind |
|---|---|---|---|---|
| `ECTO:6000029` | exposure to tobacco smoking | `ECTO:6000013` exposure to smoking | `NCIT:C17934` Tobacco Smoking | behaviour |
| `ECTO:0001082` | exposure to alcohol consumption | `ECTO:6000016` exposure to personal behavior | `NCIT:C16273` Alcohol Consumption | behaviour |
| `ECTO:0100003` | exposure to cigarette smoking | `ECTO:0100002` exposure to smoking nicotine | *anonymous class* | behaviour (product-specific) |
| `ECTO:9000027` | exposure to ethanol | `ECTO:9001334` exposure to primary alcohol; `ECTO:9001621` exposure to volatile organic compound | `CHEBI:16236` ethanol | chemical |

**The two pairs are not disconnected for the same reason, and it matters.**

- **Alcohol** genuinely splits behaviour vs. substance: `ECTO:0001082` involves an
  NCIT *behaviour* class, `ECTO:9000027` involves a *CHEBI chemical*.
- **Smoking does not.** Both members are behaviours — `ECTO:0100003`'s own definition
  reads *"An exposure event involving nicotine cigarette smoking **behavior**"*. It is
  a **product-specific** behaviour term stranded in an isolated branch: its parent
  `ECTO:0100002` hangs directly off `ExO:0000002` (exposure event) rather than under
  `ECTO:6000016` (exposure to personal behavior) where the other behaviour terms live,
  and its "involving" anchor is an anonymous class rather than a named NCIT or CHEBI
  entity. So the two smoking terms share no ECTO ancestor below `ExO:0000002`, and
  `ECTO:0100003` is **not** a narrower `ECTO:6000029`.

Do not describe `ECTO:0100003` as "substance-anchored" or as the chemical member of
its pair — it is neither. Nothing in the binding rule below depends on this, but the
structure is worth stating correctly, since misreading it as a ladder is what
produced the original mis-binding.

### The binding rule (one rule, both pairs)

**Bind the term the entry's own `name` states.** The name is the curated signal;
the description and evidence are not, because they routinely mention a product or
substance in passing while making a behavioural claim (a study of *smokers* will
still say "cigarette").

| Entry `name` states… | Bind |
|---|---|
| smoking as a habit — "Smoking", "Tobacco Smoking", "Tobacco Use" | `ECTO:6000029` |
| cigarettes specifically — "Cigarette Smoking" | `ECTO:0100003` |
| drinking as a habit — "Alcohol Consumption", "Chronic Heavy Alcohol Consumption" | `ECTO:0001082` |
| the chemical — "Ethanol Exposure", "Alcohol (Ethanol) Exposure" | `ECTO:9000027` |

**If the name and the mechanism disagree, fix the name, not just the CURIE.** An
entry whose mechanism is genuinely about ethanol chemistry (acetaldehyde, ALDH2,
DNA adducts) but is named "Alcohol Consumption" should be *renamed* to state the
chemical, then bound to `ECTO:9000027`. Keeping the chemical CURIE under a
behaviour-shaped name is what produced the duplicate-name conflicts in #8469: the
binding stops being derivable from the curated text, and no audit can tell a
deliberate distinction from a mistake.

Conversely, an entry that only says the exposure "contributes to risk", with no
chemical mechanism, is a behavioural claim — bind the behaviour term even if
sibling entries in nearby disorders bind the chemical.

Record *why* a binding was chosen in the entry's `notes:`, not in `description:`.
The description says what the exposure is; the reasoning behind the CURIE choice is
curation provenance and belongs in the slot meant for it.

**When that reason is "nothing more specific exists", write the query, not the
conclusion.** A note asserting that a search was run and found nothing is unverifiable
prose that passes every check in the stack while telling the next reviewer not to
re-run the search — the failure mode in CLAUDE.md §2c (dismech#7835), which produced
three wrong bindings in one batch of ten entries. Paste the exact re-runnable command
and what it returned, or write no note at all: an unexplained over-broad binding is a
smaller defect than one carrying a false justification.

Do not migrate an entry between the terms in a pair without checking that its name
and its mechanistic claim agree with the destination.
