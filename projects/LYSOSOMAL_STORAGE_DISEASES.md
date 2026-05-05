# Lysosomal Storage Diseases Project

## Overview

This project organizes curation of lysosomal storage diseases (LSDs) in
`dismech`, with a specific focus on where to **lump**, where to **split**, and
where to use a **project umbrella** rather than forcing everything into one
root disease file.

Lysosomal storage disease is a useful project label, but it is usually **too
broad to be a single good dismech disease entry**. The disorders share a common
cell-biologic theme — failure of lysosomal degradation, trafficking, or
substrate clearance — but they often diverge sharply in:

- the stored substrate
- the defective enzyme / transporter / accessory factor
- the dominant cell types and organs affected
- treatment logic
- age-of-onset structure and subtype conventions

So the right default in `dismech` is:

- **project umbrella at the LSD level**
- **disease-level files for biologically distinct roots**
- **subtypes within a root** when the proximal mechanism is still shared

This document is a project brief, not a claim that all lysosomal diseases should
collapse into one disease YAML.

## Existing LSD-ish KB Anchors

Current `kb/disorders/` files already touching the lysosomal-storage space:

Clearly in scope:

- `Fabry_Disease.yaml`
- `Gaucher_Disease.yaml`
- `Pompe_Disease.yaml`
- `Niemann_Pick_Disease_Type_C.yaml`
- `Krabbe_Disease.yaml`
- `Metachromatic_Leukodystrophy.yaml`
- `Tay-Sachs_Disease.yaml`
- `Beta_Mannosidosis.yaml`
- `Salla_Disease.yaml`
- `Hurler_syndrome.yaml`
- `Mucopolysaccharidosis.yaml`
- `Neuronal_Ceroid_Lipofuscinosis.yaml`

Borderline / adjacent but still useful to track here:

- `Danon_disease.yaml`
  - lysosome/autophagic vacuolar biology is relevant, but this is not the same
    curation bucket as classic substrate-storage disorders.

Important current modeling signal from the repo:

- `Hurler_syndrome.yaml` already exists as a **split disease root**.
- `Mucopolysaccharidosis.yaml` also exists as a **broader umbrella/family**.
- `Neuronal_Ceroid_Lipofuscinosis.yaml` exists as an **umbrella root**.
- `Sanfilippo` is currently mentioned under `Mucopolysaccharidosis`, not yet as
  its own standalone disease file in `kb/disorders/`.

That means the repo already wants a **mixed strategy**: broad family/project
anchors plus selected biologically strong disease roots.

## Recommended Modeling Strategy

### Recommendation: project umbrella + family roots + selective subtype splits

Use three levels deliberately:

1. **Project level** — `projects/LYSOSOMAL_STORAGE_DISEASES.md`
   - tracks the whole class
   - records split/lump rules
   - organizes priorities

2. **Disease-family or disease-root files** in `kb/disorders/`
   - used when a disease has a stable mechanistic trunk and established clinical
     identity

3. **Subtype structure**
   - used when named subtypes mostly share the same proximal defect and differ
     more by severity, age, tissue weighting, or branch-point consequences than
     by a truly different mechanistic trunk

## Working Lump / Split Rules

### Split into separate top-level disease files when:

- the **causal gene / enzyme / transporter / accessory factor changes** and that
  change materially alters the proximal mechanism
- the **stored substrate class** changes in a way that changes the mechanistic
  trunk (for example sphingolipid vs glycogen vs glycosaminoglycan vs free
  sialic acid)
- the **organelle/process framing** changes enough that one file would blur the
  biology (for example cholesterol trafficking in NPC vs acid sphingomyelinase
  deficiency in Niemann-Pick A/B)
- the **treatment logic** materially differs (enzyme replacement, substrate
  reduction, chaperone therapy, HSCT, CNS-targeted gene therapy, etc.)
- the literature and clinical practice treat the entity as a distinct disease
  family, not just a subtype label

### Keep within one disease file and use internal subtype structure when:

- the **proximal defect is the same**, and subtypes mainly reflect severity,
  age of onset, neuroinvolvement, or tempo
- the named subtype labels are clinically useful but do **not** imply a new
  mechanistic trunk
- splitting would mostly produce ontology noise rather than more accurate
  pathographs

### Use a family umbrella plus separate roots when:

- the family has a shared biochemical identity but several clearly distinct
  enzyme-level disease roots
- the family is useful for project organization but not as a single final
  disease pathograph

## Family-Specific Guidance

### 1. Mucopolysaccharidoses (MPS)

**Do not force all MPS into one disease file.**

Recommended:

- keep `Mucopolysaccharidosis.yaml` as a **family umbrella / project anchor**
- maintain separate root files for major enzyme-defined diseases

Good split candidates / existing anchors:

- `Hurler_syndrome.yaml` (already split)
- Hunter syndrome
- Sanfilippo syndrome
- Morquio syndrome
- Maroteaux-Lamy syndrome
- Sly syndrome

Within-family rule:

- **split at the major enzyme/disease level**
- but do **not automatically split every subtype letter into a new file** unless
  the subtype has a meaningfully distinct mechanistic trunk

Specific recommendation:

- treat **Sanfilippo syndrome** as a strong candidate for a root file
- treat **Sanfilippo A/B/C/D** as likely **subtypes under that root first**,
  not four premature top-level files by default

### 2. Neuronal ceroid lipofuscinoses (NCL / Batten spectrum)

Recommended:

- keep `Neuronal_Ceroid_Lipofuscinosis.yaml` as the **umbrella root**
- do **not** start by creating standalone root files for every age label

Key rule:

- labels like infantile / late-infantile / juvenile / adult NCL are often best
  treated as **subtypes**, not automatic separate roots

Specific recommendation:

- **adult neuronal ceroid lipofuscinosis should default to subtype treatment**
  under NCL rather than its own root entry unless the literature supports a
  clearly distinct mechanistic trunk that would justify separation

### 3. Gaucher disease

Recommended:

- keep **one Gaucher root file**
- represent type 1 / 2 / 3 as **subtypes or internal branches**, not separate
  top-level files by default

Why:

- the proximal GBA / glucocerebroside-storage mechanism is shared
- the main differences are neurologic involvement and tempo, not a totally
  different mechanistic trunk

### 4. Niemann-Pick family

Recommended:

- keep **NPC** as a separate root (`Niemann_Pick_Disease_Type_C.yaml` already
  exists)
- do **not** lump NPC together with acid sphingomyelinase deficiency forms just
  because the family name overlaps

Why:

- NPC is a cholesterol-trafficking / lysosomal export problem
- Niemann-Pick A/B are acid sphingomyelinase deficiency disorders with a
  different proximal defect

So:

- **split NPC from Niemann-Pick A/B**
- family label can remain project-level only

### 5. GM2 gangliosidosis branch

Recommended:

- do **not** make a generic GM2 root the default endpoint unless needed for
  project organization
- prefer separate root files for:
  - Tay-Sachs disease
  - Sandhoff disease

Why:

- HEXA vs HEXB matters mechanistically and clinically
- the shared ganglioside theme is useful, but gene/enzyme-specific roots are
  clearer in dismech

### 6. Leukodystrophy / sphingolipid storage edge cases

Recommended:

- keep `Krabbe_Disease.yaml` and `Metachromatic_Leukodystrophy.yaml` as separate
  roots
- do not lump them just because both are lysosomal leukodystrophies

Why:

- galactocerebrosidase deficiency vs arylsulfatase A / sulfatide handling are
  different trunks

### 7. Borderline lysosomal / autophagic disorders

`Danon_disease.yaml` is worth tracking in this project, but it should be treated
as an **edge case** rather than the template for classic LSD curation.

Why:

- the lysosome/autophagy axis is central
- but the disease family framing, tissue weighting, and treatment context differ
  from many classic substrate-storage disorders

## Current Modeling Stance

### Strong root files already present or clearly justified

- Fabry disease
- Gaucher disease
- Pompe disease
- Niemann-Pick disease type C
- Krabbe disease
- Metachromatic leukodystrophy
- Tay-Sachs disease
- Beta mannosidosis
- Salla disease
- Hurler syndrome
- Neuronal ceroid lipofuscinosis
- Mucopolysaccharidosis (as umbrella/family anchor, not final lump)

### Strong next-wave disease roots

- Hunter syndrome
- Sanfilippo syndrome
- Morquio syndrome
- Sandhoff disease
- Niemann-Pick disease type A/B branch
- Wolman disease
- Farber disease
- Alpha-mannosidosis
- GM1 gangliosidosis

### Likely subtype-first rather than root-first

- adult neuronal ceroid lipofuscinosis
- Sanfilippo A/B/C/D when a Sanfilippo root does not yet exist
- Gaucher type 1 / 2 / 3
- late-infantile / juvenile / adult NCL labels in isolation

## Practical Curation Rules for This Project

- Do not let a **family label** stand in for a good mechanistic disease root.
- Do not create a new root file just because medicine has a subtype name.
- Prefer **enzyme/gene/substrate-defined roots** over purely age-labeled roots.
- Keep phenotypes downstream from the storage / trafficking defect rather than
  turning severity labels into fake mechanisms.
- When the same trunk feeds several subtype branches, use **one file + subtype
  structure** instead of multiple thin YAMLs.
- When distinct biochemical lesions produce distinct treatment and mechanism
  logic, **split**.

## Initial Execution Plan

1. Keep this project file as the organizing umbrella.
2. Audit current lysosomal-related entries for consistency of lump/split style.
3. Normalize the MPS strategy:
   - retain `Mucopolysaccharidosis.yaml` as umbrella
   - use disease-level roots for major enzyme-defined forms
   - use subtype structure under those roots where appropriate
4. Normalize the NCL strategy:
   - umbrella root first
   - age-form labels as subtype-first unless clearly justified otherwise
5. Add missing high-value roots in this order:
   - Hunter syndrome
   - Sanfilippo syndrome
   - Sandhoff disease
   - Morquio syndrome
   - Wolman disease
6. Reassess whether a reusable lysosomal mechanism module is worth creating only
   after 3-5 more roots exist.

## Open Questions

- Should `Mucopolysaccharidosis.yaml` stay a lightweight umbrella, or should it
  become more explicitly a family-summary page with `has_subtypes` pointing to
  major enzyme-defined roots?
- Should Sanfilippo be rooted first as one disease family with subtype letters,
  or should A/B/C/D split immediately once a Sanfilippo root exists?
- Should `Neuronal_Ceroid_Lipofuscinosis.yaml` remain the main umbrella while
  CLN gene-specific branches stay internal, or is there enough repeated
  divergence to justify selected separate roots later?
- How much lysosome/autophagy edge territory belongs here versus adjacent
  disease-family projects?

---
# STATUS

## Existing Anchors
- [x] Identified current lysosomal-related disorder files already present in the KB
- [x] Recorded current umbrella/root tension in MPS and NCL
- [x] Wrote initial lump/split strategy for LSD curation

## Next Curation Targets
- [ ] Hunter syndrome
- [ ] Sanfilippo syndrome
- [ ] Sandhoff disease
- [ ] Morquio syndrome
- [ ] Wolman disease
- [ ] Farber disease
- [ ] Alpha-mannosidosis

# NOTES

## 2026-04-14

- Started `LYSOSOMAL_STORAGE_DISEASES` project brief.
- Chose a **project umbrella + disease-root + subtype** strategy rather than a
  single giant LSD disease file.
- Recorded that current repo state already implies mixed granularity:
  `Hurler_syndrome.yaml` is split, while `Mucopolysaccharidosis.yaml` and
  `Neuronal_Ceroid_Lipofuscinosis.yaml` act as broader umbrellas.
- Explicitly treated adult neuronal ceroid lipofuscinosis as subtype-first,
  not an automatic standalone root.
