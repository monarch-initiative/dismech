# Proposal A — ModifierEnum PATO Bindings + GOF/LOF Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ground `ModifierEnum` in verified PATO ontology terms and add structured `GAIN_OF_FUNCTION` / `LOSS_OF_FUNCTION` enum values, demonstrated with a one-line exemplar in Noonan_Syndrome.yaml.

**Architecture:** Three files change — the LinkML schema (enum definitions), the OAK config (PATO adapter registration), and one KB disorder file (Noonan exemplar). All changes are additive; no existing KB files require migration.

**Tech Stack:** LinkML schema (YAML), OAK (`runoak`), `just` task runner, `linkml-validate`, `linkml-term-validator`

## Global Constraints

- Working branch: `feat/proposal-a-modifier-enum-pato` (worktree at `../dismech-proposal-a`)
- All commands run from the worktree root (`/Users/vibhor/Documents/dismech-proposal-a/`)
- Never create or hand-edit `references_cache/*.md` files
- Use `git add` with specific paths only — never `git add -A` or `git add .`
- PATO term IDs verified 2026-06-26: PATO:0002300 (increased quality), PATO:0002301 (decreased quality), PATO:0000460 (abnormal), PATO:0000462 (absent) — use exactly these IDs
- `DYSREGULATED`, `GAIN_OF_FUNCTION`, `LOSS_OF_FUNCTION` ship without `meaning:` bindings (no suitable terms found across PATO/GENO/GO/SO)

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `docs/superpowers/specs/2026-06-26-modifier-enum-pato-gof-lof-design.md` | Already exists | Design doc — commit as-is |
| `src/dismech/schema/dismech.yaml` | Modify lines 19–48 (prefixes) and 491–508 (ModifierEnum) | Add PATO prefix + update enum |
| `conf/oak_config.yaml` | Modify | Register PATO OAK adapter |
| `kb/disorders/Noonan_Syndrome.yaml` | Modify line ~137 | Add `modifier: GAIN_OF_FUNCTION` to SHP2 node |

---

## Task 1: Commit the Design Doc

**Files:**
- Commit: `docs/superpowers/specs/2026-06-26-modifier-enum-pato-gof-lof-design.md`

- [ ] **Step 1: Verify the design doc exists**

```bash
ls docs/superpowers/specs/2026-06-26-modifier-enum-pato-gof-lof-design.md
```

Expected: file listed with no error.

- [ ] **Step 2: Stage and commit**

```bash
git add docs/superpowers/specs/2026-06-26-modifier-enum-pato-gof-lof-design.md
git commit -m "docs: add Proposal A design spec (ModifierEnum PATO bindings + GOF/LOF)"
```

---

## Task 2: Schema + OAK Config

**Files:**
- Modify: `src/dismech/schema/dismech.yaml` (prefixes block ~line 33, ModifierEnum ~lines 491–508)
- Modify: `conf/oak_config.yaml`

**Interfaces:**
- Produces: `ModifierEnum` with `meaning:` on 4 values + 2 new unbound values; `PATO:` prefix resolvable by OAK

- [ ] **Step 1: Establish baseline — confirm schema currently validates cleanly**

```bash
just validate-all 2>&1 | tail -5
```

Expected: no errors. If errors exist, stop and investigate before proceeding.

- [ ] **Step 2: Add PATO prefix to schema**

In `src/dismech/schema/dismech.yaml`, find the prefixes block (around line 33). After the `GENO:` line, add:

```yaml
  PATO: http://purl.obolibrary.org/obo/PATO_
```

The prefixes block should look like:
```yaml
  GENO: http://purl.obolibrary.org/obo/GENO_
  PATO: http://purl.obolibrary.org/obo/PATO_
  ECTO: http://purl.obolibrary.org/obo/ECTO_
```

- [ ] **Step 3: Update ModifierEnum**

Replace the entire `ModifierEnum` block (lines 491–508) with:

```yaml
  ModifierEnum:
    description: Qualifiers for direction, intensity, or pathological state of a descriptor
    permissible_values:
      INCREASED:
        title: Increased
        meaning: PATO:0002300  # increased quality
        description: Upregulated, hyperactive, elevated, or excessive
      DECREASED:
        title: Decreased
        meaning: PATO:0002301  # decreased quality
        description: Downregulated, hypoactive, reduced, or deficient
      ABNORMAL:
        title: Abnormal
        meaning: PATO:0000460  # abnormal
        description: Qualitatively abnormal (e.g., misfolding, mislocalization, malformed)
      DYSREGULATED:
        title: Dysregulated
        # No PATO term exists — verified via OAK 2026-06-26
        description: Regulation is impaired (may be increased or decreased)
      ABSENT:
        title: Absent
        meaning: PATO:0000462  # absent
        description: Not occurring or not present
      GAIN_OF_FUNCTION:
        title: Gain of Function
        # No suitable ontology term found across PATO/GENO/GO/SO (verified 2026-06-26)
        # SO:0002053 exists but is a variant-consequence term, not an activity modifier
        description: Variant or activity that confers an abnormal or enhanced function
      LOSS_OF_FUNCTION:
        title: Loss of Function
        # No suitable ontology term found across PATO/GENO/GO/SO (verified 2026-06-26)
        # SO:0002054 exists but is a variant-consequence term, not an activity modifier
        description: Variant or activity that reduces or abolishes normal function
```

- [ ] **Step 4: Add PATO to OAK config**

In `conf/oak_config.yaml`, after the `GENO:` entry, add a new section:

```yaml
  # Quality/modifier ontology
  PATO: sqlite:obo:pato
```

- [ ] **Step 5: Verify schema still validates**

```bash
just validate-all 2>&1 | tail -5
```

Expected: no errors. The new enum values are additive — no existing KB file uses them yet.

- [ ] **Step 6: Verify PATO adapter resolves in OAK**

```bash
uv run runoak -i sqlite:obo:pato info PATO:0002300 PATO:0002301 PATO:0000460 PATO:0000462
```

Expected output (labels must match exactly):
```
PATO:0002300 ! increased quality
PATO:0002301 ! decreased quality
PATO:0000460 ! abnormal
PATO:0000462 ! absent
```

If any label differs from above, stop — do not commit until resolved.

- [ ] **Step 7: Commit**

```bash
git add src/dismech/schema/dismech.yaml conf/oak_config.yaml
git commit -m "feat: ground ModifierEnum in PATO and add GAIN_OF_FUNCTION/LOSS_OF_FUNCTION enum values"
```

---

## Task 3: Noonan Exemplar + Full QC

**Files:**
- Modify: `kb/disorders/Noonan_Syndrome.yaml` (~line 137)

**Interfaces:**
- Consumes: `GAIN_OF_FUNCTION` enum value from Task 2's schema change

- [ ] **Step 1: Locate the target node**

```bash
grep -n "protein tyrosine phosphatase activity" kb/disorders/Noonan_Syndrome.yaml
```

Expected: a line around 135–138 inside the "SHP2 Gain-of-Function Activation" node.

- [ ] **Step 2: Confirm the node has no modifier yet**

```bash
grep -n "modifier" kb/disorders/Noonan_Syndrome.yaml
```

Expected: no output (no `modifier:` currently used in this file).

- [ ] **Step 3: Add modifier: GAIN_OF_FUNCTION to the SHP2 molecular function descriptor**

In `kb/disorders/Noonan_Syndrome.yaml`, find this block (around line 134):

```yaml
  molecular_functions:
  - preferred_term: protein tyrosine phosphatase activity
    term:
      id: GO:0004725
      label: protein tyrosine phosphatase activity
```

Add `modifier: GAIN_OF_FUNCTION` after the `term:` block:

```yaml
  molecular_functions:
  - preferred_term: protein tyrosine phosphatase activity
    term:
      id: GO:0004725
      label: protein tyrosine phosphatase activity
    modifier: GAIN_OF_FUNCTION
```

- [ ] **Step 4: Validate Noonan schema conformance**

```bash
just validate kb/disorders/Noonan_Syndrome.yaml
```

Expected: no errors.

- [ ] **Step 5: Validate Noonan term references**

```bash
just validate-terms-file kb/disorders/Noonan_Syndrome.yaml
```

Expected: no errors. (`modifier:` enum values are not ontology term references — this checks GO/HP/etc. terms only.)

- [ ] **Step 6: Validate Noonan evidence snippets**

```bash
just validate-references kb/disorders/Noonan_Syndrome.yaml
```

Expected: no errors (we changed no evidence fields).

- [ ] **Step 7: Run full QC suite**

```bash
just qc
```

Expected: all checks pass. If term validation fails on a pre-existing file unrelated to our change, note it but do not fix it in this PR.

- [ ] **Step 8: Commit**

```bash
git add kb/disorders/Noonan_Syndrome.yaml
git commit -m "feat(exemplar): add modifier: GAIN_OF_FUNCTION to Noonan SHP2 molecular function node"
```

- [ ] **Step 9: Push branch**

```bash
git push -u origin feat/proposal-a-modifier-enum-pato
```

---

## Done

Three commits on `feat/proposal-a-modifier-enum-pato`:
1. Design doc
2. Schema + OAK config
3. Noonan exemplar

Open a PR targeting `main`. PR description should note:
- The ontology verification findings (4 hallucinated PATO IDs from the proposal)
- Which values got bindings and which didn't, and why
- The three follow-up issues to open (retroactive migration, DYSREGULATED binding, GOF/LOF ontology tracking)
