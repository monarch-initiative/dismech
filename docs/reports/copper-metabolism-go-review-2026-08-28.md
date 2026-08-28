# Copper Metabolism Disorders — GO Pathway Annotation Review (2026-08-28)

Review of every KB entry involving disorders of copper metabolism, focused on
how Gene Ontology terms are used to describe the disease pathways. This document
records both the review and the curation pass that acted on it: every finding
below was fixed in the same-dated pass, and the "Fix applied" notes and the
Validation section at the end record what changed.

## Scope

The curated grouping
[`kb/groupings/Disorders_of_Copper_Metabolism.yaml`](../../kb/groupings/Disorders_of_Copper_Metabolism.yaml)
(closeMatch to `MONDO:0017762`) defines the core set, and its membership logic
was confirmed correct against the entries:

| Entry | Gene | Direction of copper defect |
|---|---|---|
| `Wilsons_Disease` | ATP7B (`hgnc:870`) | Overload — failed biliary excretion |
| `Menkes_Disease` | ATP7A (`hgnc:869`) | Deficiency — failed intestinal export |
| `MEDNIK_syndrome` | AP1S1 (`hgnc:559`) | Mixed — AP-1 trafficking of both pumps |
| `Huppke-Brendel_syndrome` | SLC33A1 (`hgnc:95`) | Low serum copper/ceruloplasmin, secondary |

Also reviewed because they touch copper biology:

- `aceruloplasminemia` (CP, `hgnc:2295`) — deliberately excluded from the
  grouping as iron-primary; the exclusion rationale in the grouping is sound
  and the entry's annotation bears it out (see below).
- The mitochondrial copper-chaperone trio `SCO1-Related_COX_Deficiency`,
  `SCO2-Related_Fatal_Infantile_Cardioencephalomyopathy`,
  `COX11-Related_COX_Deficiency` — copper delivery to cytochrome c oxidase,
  grouped under `Mitochondrial_Complex_IV_Deficiency` and conforming to the
  `complex_iv_assembly_deficiency` module.
- `com_Wilsons_Disease__Osteoporosis` (comorbidity).

All gene CURIEs, MONDO anchors, and every GO binding's `id`/`label` pair in
these files were verified against the authority-backed caches
(`cache/go/terms.csv`, `cache/hgnc/terms.csv`, enum membership caches). **No
hallucinated or mislabeled GO term was found** — every bound label matches the
canonical label, including recent GO additions.

## What is done well

1. **Canonical labels and modern terms.** The set uses current GO labels
   throughout, including terms many curation pipelines miss:
   `GO:0160119` *cuproptosis* and `GO:0097707` *ferroptosis* as first-class
   cell-death nodes in Wilson disease, `GO:0150076` *neuroinflammatory
   response*, `GO:0034102` *erythrocyte clearance*, and `GO:0006879` under its
   current label *intracellular iron ion homeostasis* (aceruloplasminemia).

2. **Chemically precise molecular function.** Wilson disease binds
   `GO:0140581` *P-type monovalent copper transporter activity* — correctly
   Cu(I), not a generic copper-transporter term — on the ATP7B nodes.

3. **Module conformance carries shared GO vocabulary.** Wilson's fibrosis
   cascade conforms to `fibrotic_response` (TGF-β `GO:0007179` INCREASED, ECM
   organization `GO:0030198` INCREASED, collagen biosynthesis `GO:0032964`
   INCREASED) and its hemolysis arm to
   `hemolytic_anemia_erythrocyte_destruction`. The SCO1/SCO2/COX11 trio
   conforms to `complex_iv_assembly_deficiency`, and their use of the general
   `GO:0006825` *copper ion transport* for chaperone-mediated copper delivery
   is the module's own contract — appropriately general, since metallochaperone
   hand-off is not transmembrane transport.

4. **Secondary copper phenotypes are not force-fitted to copper GO terms.**
   Huppke-Brendel is modeled through its actual proximal pathway — acetyl-CoA
   transport (`GO:0035348`/`GO:0008521`, ER `GO:0005783`) → protein acetylation
   (`GO:0006473`) → protein secretion (`GO:0009306` DECREASED) → low
   ceruloplasmin/copper — rather than borrowing copper-transport terms the gene
   does not participate in. MEDNIK similarly leads with AP-1 trafficking terms
   (`GO:0006886`, `GO:0016192`) and only introduces copper GO terms on the
   downstream copper-pump-trafficking and hepatic-overload nodes. This is the
   right application of the "no term beats a bad term" rule.

5. **Aceruloplasminemia annotates iron, not copper.** Its three nodes bind
   `GO:0004322` *ferroxidase activity* (DECREASED), `GO:0006826` *iron ion
   transport*, and `GO:0006879` — consistent with the grouping's decision that
   its proximal lesion is iron export despite the ceruloplasmin connection.

## Findings and fixes applied

Every finding below was **fixed** in the same-dated curation pass (commit on
`claude/copper-metabolism-disorders-w3e4il`); the "Fix applied" note under each
records what changed. All eight edited entries pass `just validate-disorders`
(schema + terms + reference snippets), the duplicate-key and entity-ref checks,
and the offline title/grading/length/hyphen/environmental gates. Candidate GO
terms were verified against OLS before binding, and matching history records
were added under `history/disorders/`.

Ranked by impact on the machine-readable pathway description. None was a
validation failure; all files passed the term contract before and after.

### 1. Wilson disease GO descriptors carry no direction modifiers

Every copper-pathway GO binding in `Wilsons_Disease.yaml` lacks a `modifier`,
so the direction of the lesion lives only in node names and prose ("Impaired
Biliary Copper Excretion", "Hepatic Copper Accumulation"). The sibling entries
annotate direction (Menkes `GO:0006825` DECREASED on brain copper transport;
MEDNIK ABNORMAL; SCO1/SCO2/COX11 DECREASED throughout), so Wilson is the
outlier in the grouping, and pathograph/KGX consumers cannot see that copper
transport is *decreased* in the very entry that is the copper-overload
archetype. Suggested minimal fix: `DECREASED` on `GO:0006825` and `GO:0140581`
for the "ATP7B Copper-Trafficking Defect", "Impaired Biliary Copper
Excretion", and "Impaired Ceruloplasmin Loading" nodes. Menkes' apex node
("ATP7A-mediated copper export failure", `GO:0006825` unmodified) has the same
gap even though its child nodes are modified.

**Fix applied.** `DECREASED` added to `GO:0006825` and `GO:0140581` on the three
Wilson ATP7B nodes and to the Menkes apex node (which also gained the
`GO:0140581` copper-transporter MF, `DECREASED`). Downstream oxidative-stress
and homeostasis nodes across both entries received `INCREASED`/`ABNORMAL`
modifiers to match.

### 2. One GO triple copy-pasted across mechanistically distinct nodes

Wilson's "ATP7B Copper-Trafficking Defect" and "Impaired Biliary Copper
Excretion" carry the identical BP/MF/CC triple (`GO:0006825` + `GO:0140581` +
`GO:0005794` *Golgi apparatus*), and "Impaired Ceruloplasmin Loading" reuses
two of the three. In GO space the three nodes are near-indistinguishable, while
their own descriptions distinguish them precisely: the biliary-excretion node
describes ATP7B trafficking to the **bile canalicular membrane**, for which
`GO:0035434` *copper ion transmembrane transport* (already in the cache and
used by `Cardiomyopathy-Hypotonia-Lactic_Acidosis_Syndrome`) is the more
specific accurate BP, and the Golgi CC is arguably wrong — the site of that
step is the apical/canalicular membrane, not the TGN. Aceruloplasminemia has
the same pattern in miniature: the identical iron BP pair is stamped onto all
three of its nodes, with `modifier: ABNORMAL` uniformly, so the ferroxidase
node and the two accumulation nodes differ only by the MF binding.

**Fix applied.** The Wilson biliary-excretion node now binds `GO:0035434`
*copper ion transmembrane transport* (`DECREASED`) with `GO:0016324` *apical
plasma membrane* as the canalicular CC, replacing the Golgi triple. The
aceruloplasminemia nodes were left on the shared iron pair but are now
differentiated by `biological_scale` (MOLECULAR / ORGANISM / TISSUE); their
`ABNORMAL` homeostasis modifier is correct under the finding-5 convention, with
iron level carried by the `INCREASED` iron `chemical_entities`.

### 3. The treatment-targeted hub nodes have no ontology grounding at all

Wilson's "Hepatic Copper Accumulation" and "Systemic Copper Distribution" are
the two most connected nodes in the KB's copper pathograph — every chelator,
zinc, and dietary treatment `target_mechanisms` link points at them — yet
neither carries any GO (or other ontology) binding. Candidates worth
validating through the `dismech-terms` workflow: `GO:0055070` (or the more
specific `GO:0006878` *intracellular copper ion homeostasis*, not yet in the
cache) with an `INCREASED`/`ABNORMAL` modifier, and `GO:0046688` *response to
copper ion* for the downstream injury claims. As curated, an export of these
nodes is free text only.

**Fix applied.** "Hepatic Copper Accumulation" now binds `GO:0006878`
*intracellular copper ion homeostasis* (`ABNORMAL`) and "Systemic Copper
Distribution" binds `GO:0055070` *copper ion homeostasis* (`ABNORMAL`).

### 4. Cuproenzymes are named in prose but their molecular functions are never bound

A cross-entry pattern: the copper-deficiency arm of the group repeatedly names
specific cuproenzymes — dopamine-β-hydroxylase, cytochrome c oxidase, lysyl
oxidase, tyrosinase — in `description` text, but the only cuproenzyme MF bound
anywhere in the group is `GO:0004322` *ferroxidase activity* (in
aceruloplasminemia). Concretely:

- Menkes "Lysyl oxidase deficiency and connective tissue fragility" binds only
  the consequence (`GO:0030198` ECM organization) and not the cause; a
  DECREASED protein-lysine 6-oxidase activity MF binding would make the node's
  own name machine-readable.
- Menkes "Cuproenzyme deficiency and neurodevelopmental injury" binds the
  processes (`GO:0042423` catecholamine biosynthesis, `GO:0006119` oxidative
  phosphorylation) but not dopamine β-monooxygenase or cytochrome-c oxidase
  activity, despite the description and the DOPA:DHPG biomarker resting on
  DBH specifically.
- Menkes "Hair-shaft keratinization and pigmentation enzyme dysfunction" has
  no ontology bindings at all (tyrosinase/melanin biosynthesis are the obvious
  candidates).
- Wilson "Impaired Ceruloplasmin Loading" could mirror aceruloplasminemia's
  `GO:0004322` DECREASED — the two diseases converge on lost ceruloplasmin
  ferroxidase activity by different routes, and a shared MF binding would make
  that convergence queryable.

**Fix applied.** All four cuproenzyme MFs were verified against OLS and bound
(`DECREASED`): Menkes lysyl oxidase `GO:0004720`, dopamine β-monooxygenase
`GO:0004500`, cytochrome-c oxidase `GO:0004129`, and tyrosinase `GO:0004503`
(with melanin biosynthesis `GO:0042438` on the hair node); Wilson's
ceruloplasmin-loading node gained the shared `GO:0004322` *ferroxidase activity*
binding, making its convergence with aceruloplasminemia queryable. New
mechanistic citations were added for the previously prose-only claims:
`PMID:32381719` (Elesclomol/COX in Menkes) and `PMID:18650808`
(ATP7A→tyrosinase in melanosomes).

### 5. Inconsistent modifier semantics on homeostasis terms

Menkes "Systemic copper deficiency" annotates `GO:0055070` *copper ion
homeostasis* with `DECREASED`; MEDNIK "Hepatic copper overload" annotates the
same term with `ABNORMAL`. The two nodes describe opposite derangements, but
the annotations don't encode that — and "decreased homeostasis" conflates the
copper *level* with the homeostatic *process* (if anything, a deficiency state
means homeostasis has failed, not diminished). A convention worth adopting
KB-wide: homeostasis-class terms take `ABNORMAL`/`DYSREGULATED`, and
directionality is carried by the transport/level-specific binding or the node
itself.

**Fix applied.** The convention was adopted across the copper set: Menkes
"Systemic copper deficiency" changed from `DECREASED` to `ABNORMAL` on
`GO:0055070`, and the Wilson and MEDNIK homeostasis nodes were made consistent.
Direction now rides on the copper-transport MF/BP bindings and the copper
`chemical_entities` level, not on the homeostasis process term.

### 6. Menkes OXPHOS binding sits in mild tension with its own cited evidence

The "Cuproenzyme deficiency" node binds `GO:0006119` *oxidative
phosphorylation* (unmodified) with PMID:27226607 among its support — but the
same paper, quoted on the adjacent "Mitochondrial redox imbalance" node,
reports that redox misbalance "does not significantly affect … the activity of
respiratory complex IV" in that model. The OXPHOS-impairment claim is
defensible from the broader cuproenzyme literature, but the specific
27226607 snippet on this node ("ATP7A activity protects mitochondria from
excessive copper entry") supports the copper-*accumulation* redox node, not
the deficiency-driven cuproenzyme node it is attached to. Worth re-homing that
evidence item and deciding whether OXPHOS merits a `DECREASED` modifier backed
by COX-specific human data.

**Fix applied.** The misplaced `PMID:27226607` item was removed from the
cuproenzyme node (it remains, correctly, on the redox node) and replaced with
`PMID:32381719`, which attributes the Menkes mitochondrial energy deficit
specifically to cytochrome c oxidase dysfunction. `GO:0006119` oxidative
phosphorylation now carries `DECREASED`, grounded on that COX-specific evidence
plus the new `GO:0004129` cytochrome-c-oxidase MF.

### 7. Secondary observations (non-GO)

- **Cell-death edge direction.** Wilson previously modeled `Hepatocyte Injury →
  Cuproptosis` and `→ Ferroptosis` (death programs as leaf consequences), while
  the entry's own hypothesis files treat cuproptosis as a *mechanism of*
  hepatocyte injury. **Fixed:** the two death nodes are now wired
  `Hepatic Copper Accumulation → Cuproptosis → Hepatocyte Injury` (with
  `PMID:35298263` grounding copper's direct binding to lipoylated TCA proteins)
  and `Ferroptosis → Hepatocyte Injury` (with `PMID:41966025`), so the graph and
  the hypothesis register now agree. The former leaf edges were removed.
- **ICIMD classification was inconsistent across the grouping.** **Fixed:**
  Menkes and MEDNIK gained `classifications.icimd_category: copper_metabolism`;
  aceruloplasminemia gained an `iron_metabolism` classification recording why it
  is iron-primary. Huppke-Brendel was **deliberately left unclassified** on the
  ICIMD axis — its proximal lesion is the acetyl-CoA transporter and its low
  copper is explicitly secondary, so a `copper_metabolism` tag would contradict
  the entry's own framing; its placement between the acetylation/CDG and copper
  groups is a genuine curator decision, not an omission to paper over. This means
  the grouping's rationale sentence claiming all four fall in the ICIMD Copper
  group is itself slightly overstated for Huppke-Brendel and is worth softening.
- **`biological_scale`** is now tagged on every node in all eight entries
  (MOLECULAR pump/enzyme defect → CELLULAR → TISSUE/ORGANISM injury).
- Wilson's deprecated `prevalence.percentage` fields were removed; the verbatim
  source phrasing was preserved in `notes`.
- The comorbidity `com_Wilsons_Disease__Osteoporosis` binds `GO:0046849`
  *bone remodeling* correctly (label verified); left unchanged.

## Literature added

- `PMID:35298263` (Tsvetkov 2022, *Science*) — copper binding to lipoylated TCA
  proteins; grounds the rewired Wilson cuproptosis edge.
- `PMID:32381719` (Guthrie 2020, *Science*) — Elesclomol/COX rescue in a Menkes
  model; grounds the Menkes cytochrome-c-oxidase and OXPHOS annotations.
- `PMID:18650808` (Setty 2008, *Nature*) — ATP7A sustains melanosomal tyrosinase;
  grounds the Menkes hair-node tyrosinase/melanin bindings.
- `PMID:42018271` (2026) — January 2026 FDA first approval of copper histidinate
  (ZYCUBO) for pediatric Menkes disease, added to the treatment.
- `NCT04537377` (VTX-801) and `NCT04884815` (UX701) — the two active Wilson
  disease AAV gene-therapy trials, added as `clinical_trials`.

## Remaining follow-up (not in this pass)

- Soften the `Disorders_of_Copper_Metabolism` grouping rationale's claim that all
  four members fall in the ICIMD "Copper" group, given Huppke-Brendel's
  acetyl-CoA-transporter primary lesion (see finding 7).
- Earlier suggested items now **done** in this pass: direction modifiers
  (finding 1), node differentiation (finding 2), hub-node grounding and
  cuproenzyme MFs (findings 3–4), the homeostasis-modifier convention and the
  re-homed Menkes evidence item (findings 5–6), and the ICIMD/`biological_scale`
  backfill (finding 7).

## Validation

All eight edited entries pass `just validate-disorders` (schema + terms +
reference snippets; 503/535 snippets verified, the remainder skipped by prefix),
`just check-duplicate-keys`, `just check-entity-refs`, and the offline
title/grading/length/hyphen/environmental gates. New GO terms were verified
against OLS before binding, new reference titles match their cache frontmatter,
and one `history/disorders/` record was added per edited entry
(`just validate-history-all` clean).
