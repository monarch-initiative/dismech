# Blood Disorders Claim–Evidence Review (2026-07-25)

Correctness review of 10 haematology entries in `kb/disorders/`, focused on whether
each asserted claim is actually carried by the evidence attached to it.

## Entries reviewed

| Entry | Lines |
|---|---|
| `Sickle_Cell_Disease` | 1118 |
| `Hereditary_Spherocytosis` | 1075 |
| `Beta_Thalassemia` | 979 |
| `Polycythemia_Vera` | 928 |
| `Alpha_Thalassemia` | 888 |
| `Hemophilia_A` | 650 |
| `Diamond-Blackfan_Anemia` | 630 |
| `Immune_Thrombocytopenia` | 316 |
| `Hemophilia_B` | 267 |
| `Hereditary_von_Willebrand_Disease` | 234 |

## Mechanical validation: clean

- `linkml-validate` (Disease target class): **no issues** across all 10.
- `linkml-reference-validator`: no ERRORs (only 403/404 full-text fetch noise).
- Independent re-check of **every** `reference`+`snippet` pair against
  `references_cache/` (Unicode-normalised substring match): **331 snippets checked,
  0 mismatches**. One reference has no cache file:
  `url:https://www.fda.gov/...` in `Alpha_Thalassemia.treatments[6]`.

No fabricated quotes, no hallucinated PMIDs. **Every finding below is semantic** —
the quote is real, but it does not carry the claim attached to it, or the claim
contradicts something else in the same file.

## Evidence-coverage profile

| Entry | phenotypes w/o evidence | frequency bands w/o evidence | treatments w/o evidence | pathophys nodes w/o evidence | `genetic[]` w/o `gene_term` |
|---|---|---|---|---|---|
| Sickle_Cell_Disease | 1/21 | 1 | 7/9 | 1/5 | 3/3 |
| Beta_Thalassemia | 17/18 | 17 | 6/8 | 0/6 | 4/4 |
| Alpha_Thalassemia | 0/12 | 0 | 2/7 | 0/5 | 2/2 |
| Hemophilia_A | 0/7 | 0 | 0/7 | 0/5 | 0/1 |
| Hemophilia_B | 0/2 | 0 | 0/4 | 0/1 | 0/1 |
| Hereditary_von_Willebrand_Disease | 0/3 | 0 | 0/2 | 0/1 | — |
| Hereditary_Spherocytosis | 0/28 | 0 | 3/4 | 0/3 | 0/5 |
| Immune_Thrombocytopenia | 3/4 | 3 | 5/5 | 0/4 | — |
| Polycythemia_Vera | 0/26 | 0 | 5/5 | 3/4 | 3/3 |
| Diamond-Blackfan_Anemia | 0/8 | 0 | 2/6 | 0/3 | 10/10 |

`Hemophilia_A` and `Hemophilia_B` are the reference-quality entries: every
phenotype, treatment, and pathophysiology node is evidenced.

---

## High-severity findings

### 1. `Immune_Thrombocytopenia` — the defining mechanism is marked `NO_EVIDENCE` but the explanation claims confirmation

`pathophysiology[0] "Antiplatelet Antibody Production"` (the anti-GPIIb/IIIa →
splenic Fc-mediated clearance mechanism, i.e. what makes ITP ITP) carries a single
evidence item with `supports: NO_EVIDENCE`, whose snippet is a list of new targeted
therapies, and whose `explanation` reads *"This review confirms that
autoantibody-mediated platelet destruction is central to ITP pathogenesis."*

The cached PMID:38396839 abstract contains no such statement — it is entirely about
management and prediction of treatment response. So the enum is honest and the
explanation is not; either way the flagship node has **zero supporting evidence**.
Replace with a mechanism paper (e.g. anti-GPIIb/IIIa autoantibody or splenic
clearance literature) and drop the contradictory explanation.

### 2. `Alpha_Thalassemia` — prevalence record evidenced by a mutation-count sentence

`prevalence[0]` has no `measure_type`, no `prevalence_class`, and no
`rate_per_100000`. Its `notes` assert *"widespread in tropical and subtropical
regions… Highest prevalence in Southeast Asia, southern China, the Mediterranean,
Middle East, and Africa."* The only evidence is PMID:25390741 with the snippet
*"More than 100 varieties of α-thalassemia have been identified."*

That quote supports allelic heterogeneity, not prevalence and not geography. The
cached NEJM record is a two-sentence stub, so the geographic claim cannot be
sourced from it at all. Either cite a real epidemiology source with structured
slots filled, or move the geography to `description`.

### 3. Subtype-restricted phenotypes given disease-level `VERY_FREQUENT` bands

`Alpha_Thalassemia` defines a four-tier severity spectrum whose top tier is
explicitly *clinically silent*, then assigns disease-level `VERY_FREQUENT` to
phenotypes its own `notes` scope to one subtype:

- `Hydrops Fetalis` — `VERY_FREQUENT`, `notes: Specific to Hb Bart syndrome (four-gene deletion)`
- `Congestive Heart Failure` — `VERY_FREQUENT`, `notes: Specific to Hb Bart syndrome; occasional in severe HbH disease`
- `Splenomegaly` — `VERY_FREQUENT`, description says *"Present in most individuals with HbH disease"*
- `Hypochromic Microcytic Anemia` — `VERY_FREQUENT`, description says severity *"ranges from absent (silent carriers)"*

Across all alpha-thalassemia, hydrops fetalis is rare. The schema already provides
`phenotypes[].subtype` as a foreign key into `has_subtypes[].name`, and the
treatments block in this same file uses `notes` to scope by subtype correctly —
but **0 of 12 phenotypes use `subtype:`**. Across all 10 entries reviewed, `subtype:`
scoping is used **zero times**.

### 4. `Polycythemia_Vera` — three of four mechanism nodes and all five treatments are unevidenced

Unevidenced pathophysiology: `JAK2 V617F Constitutive Activation`, `STAT5
Hyperactivation`, `Erythropoietin-Independent Erythropoiesis`. The `description`
asserts *"JAK2 V617F… present in approximately 95% of PV cases"* with no citation at
that point (the claim is evidenced later under `genetic[0]`, so this is a placement
problem rather than a sourcing problem).

All five treatments — phlebotomy, aspirin, hydroxyurea, ruxolitinib,
interferon-alpha — have no evidence, despite carrying specific claims
("maintain hematocrit below 45%", "approved for PV inadequately controlled by
hydroxyurea"). The relevant trials are already sitting in the file's `references:`
block (MAJIC-PV `DOI:10.1200/jco.22.01935`, RuxoBEAT, ropeginterferon); they need
promoting to evidence items.

`genetic[1] TET2` and `genetic[2] ASXL1` state 18% and 15% with no evidence, though
both figures appear verbatim in the Tefferi 2024 review already listed in
`references:`.

### 5. Uncritical bulk import of Orphanet HPO frequencies

`Hereditary_Spherocytosis` imports 28 phenotypes from `ORPHA:822`. The snippets are
faithful (verified against the cache), but several annotations are not credible for
HS, and each has been given an **invented mechanistic `description` that no cited
source supports**:

- `Ataxia` `OCCASIONAL` — *"a rare neurological finding that may occur in severe cases"*
- `Maculopapular Exanthema` `OCCASIONAL` — *"an occasional dermatological manifestation"*
- `Hypofibrinogenemia` `FREQUENT` (30–79%) — *"potentially related to chronic hemolysis and coagulation factor consumption"*
- `Hypercoagulability` `FREQUENT` — *"potentially related to membrane vesiculation and phosphatidylserine exposure"*
- `Restrictive Cardiomyopathy` `OCCASIONAL`
- `Muscle Weakness` `FREQUENT` — *"likely related to chronic anemia"*

Also internally inconsistent: `Spherocytosis` is `FREQUENT` (30–79%) while
`Increased red cell osmotic fragility` is `VERY_FREQUENT` — spherocytes on smear are
the defining finding and cannot be rarer than a secondary assay abnormality. The
entry's own description calls it *"the characteristic finding that distinguishes HS
from other hemolytic anemias."*

`Polycythemia_Vera` has the same problem from `ORPHA:729`, and demonstrates that the
curator already knew the source was unreliable: `Myelofibrosis` and `Acute Leukemia`
were **correctly** overridden from Orphanet's `Very frequent` down to `OCCASIONAL`,
with `supports: PARTIAL` and a note explaining that Orphanet likely encodes lifetime
cumulative risk. That same scepticism was not applied to the other twelve
Orphanet-derived bands in the file:

- `Epistaxis`, `Gingival Bleeding`, `Bruising Susceptibility` at `VERY_FREQUENT` (80–99%)
- `Weight Loss`, `Hypertension`, `Tinnitus`, `Vertigo`, `Abdominal Pain`, `Hepatomegaly` at `VERY_FREQUENT`
- `Splenomegaly` at `VERY_FREQUENT` (≈30–40% at diagnosis in practice)

while `Thrombocytosis` and `Leukocytosis` sit at `OCCASIONAL` (5–29%) — contradicting
both the entry's own description (*"often accompanied by increased white blood cells
and platelets"*) and its second evidence item on those very phenotypes (REVEAL:
*"characterized by erythrocytosis, thrombocytosis, leukocytosis, and splenomegaly"*).
The resulting profile ranks nosebleeds above the cardinal features of the disease.

### 6. `Beta_Thalassemia` — 17 of 18 phenotypes carry frequency bands with no evidence

Only `Microcytic Hypochromic Anemia` is evidenced. Everything else — target cells,
extramedullary haematopoiesis, splenomegaly, hepatomegaly, cholelithiasis, jaundice,
elevated ferritin, cardiomyopathy, pulmonary hypertension, frontal bossing,
osteoporosis, short stature, delayed puberty — has a `FREQUENT`/`VERY_FREQUENT`/
`OCCASIONAL` band and no evidence item at all. Per
`docs/frequency-evidence-guidelines.md` these bands should be evidenced or omitted.

`Cardiomyopathy` additionally asserts *"the leading cause of death in
transfusion-dependent beta-thalassemia"* uncited.

The `pathophysiology` and `biochemical` blocks in this same file are excellent
(per-edge evidence, `readouts` with `regulatory_endpoint_refs`) — the gap is
confined to `phenotypes`.

---

## Medium-severity findings

### 7. `Diamond-Blackfan_Anemia` — p53/MDM2 node evidenced by a phenotype sentence

`pathophysiology[1] "p53-Mediated Erythroid Apoptosis"` describes free ribosomal
proteins binding MDM2 and stabilising p53. Its only evidence is GeneReviews
PMID:20301769 with the snippet *"characterized by a profound normochromic and usually
macrocytic anemia with normal leukocytes and platelets"* — which supports
erythroid-restricted failure but says nothing about p53, MDM2, or apoptosis. The
canonical mechanism is unevidenced despite abundant literature.

### 8. `Diamond-Blackfan_Anemia` — `RPL35A` cited to a paper that found no RPL35A mutations

`genetic[3] RPL35A` cites PMID:19773262 quoting its BACKGROUND sentence. That paper's
own RESULTS state *"No mutations were found in RPS14, RPS16, or RPL35A."* The quote is
accurate, but this is the wrong paper to anchor RPL35A causation. (The neighbouring
`RPL5`/`RPL11` claims from the same paper are correct — the cohort is 92
RPS19-negative Italian probands, so the "20% of RPS19-negative" explanation checks out.)

### 9. `Diamond-Blackfan_Anemia` — "congenital malformations, 50%" bound to `Craniofacial dysostosis`

The phenotype is named `Congenital Malformations`, described as covering craniofacial,
thumb, cardiac, and genitourinary anomalies, evidenced by *"congenital malformations in
up to 50% of affected individuals"* — and bound to `HP:0004439 Craniofacial dysostosis`.
The 50% figure is for all malformations combined; craniofacial dysostosis specifically
is not a DBA feature. Split into specific terms (cleft palate, micrognathia, thumb
anomalies) or bind to a broader parent.

Related: `Triphalangeal Thumb` is evidenced by a snippet about *"hand malformations and
RPL11 mutations"* that never mentions thumbs, with the explanation supplying
"including thumb anomalies."

### 10. `Sickle_Cell_Disease` — HBB has no evidence naming HBB

`genetic[0] HBB` (`notes: Glu6Val mutation (rs334)`) is evidenced by PMID:18667698 with
*"Sickle cell disease (SCD) is a debilitating monogenic blood disorder…"* — correctly
flagged `PARTIAL`, but the snippet never mentions HBB, β-globin, or Glu6Val. The single
most fundamental genetic claim in the entry lacks a quote that names the gene.

### 11. `Sickle_Cell_Disease` — acute chest syndrome supported only by murine NET data

`Acute Chest Syndrome` (`notes: Leading cause of death`) is evidenced by two
`MODEL_ORGANISM` snippets from PMID:24620350 (heme-induced neutrophil extracellular
traps in mice), neither of which mentions acute chest syndrome; the explanations
supply the extrapolation. CLAUDE.md: *"Model organism evidence should not be the only
support for human phenotypes."* The same pattern affects `Pain Crises`, though there a
second `ORPHA:232` item rescues it.

`Splenic Sequestration` has no evidence at all.

### 12. `Sickle_Cell_Disease` — unevidenced regulatory-status claims

Seven of nine treatments have no `treatment_term` and no evidence. Two make specific
falsifiable regulatory assertions with nothing attached:

- `Voxelotor`: *"voluntarily withdrawn from worldwide markets in 2024 due to postmarketing safety concerns"*
- `Crizanlizumab`: *"EU authorization revocation was recommended in 2023 when STAND did not confirm benefit"*

Both are accurate but need citations. `Penicillin Prophylaxis` lacks the PROPS trial.

Also `prevalence[0]` (GBD 2021, 7.74 M living cases) carries no `measure_type`,
`prevalence_class`, or `rate_per_100000` — the sole record in this file that was not
migrated to structured slots.

### 13. `Hereditary_von_Willebrand_Disease` — imprecise disease term and no genetics

- `disease_term` is `MONDO:0024574 "von Willebrand disease (hereditary or acquired)"`
  on an entry explicitly scoped to hereditary disease. `MONDO:0019565 "hereditary von
  Willebrand disease"` exists and is the precise match.
- No `genetic:` block and no `inheritance:` block — VWF is never bound to HGNC anywhere
  in the file.
- Subtypes list Type 1, Type 2, Type 2N, Type 3; 2N is a member of the Type 2 group, and
  2A/2B/2M are absent, though the cited PMID:21289515 abstract enumerates all four.
- `prevalence[1]` assigns `BAND_1_5_PER_10000` to a range spanning `<1` to `450` per
  million (`rate_low: 0.1`, `rate_high: 45.0`) — the band matches only the top of a
  range covering four orders of magnitude.

### 14. `Hemophilia_A` — same PMID tagged three different `evidence_source` values

PMID:26743572 is an in-vitro iPSC gene-correction study. It appears as
`HUMAN_CLINICAL` (inheritance block), `IN_VITRO` (twice), and `OTHER` (genetic
features). Per the CLAUDE.md classification rules it is `IN_VITRO` throughout.

`Easy Bruising` is `VERY_FREQUENT` on a `PARTIAL` generic-bleeding snippet; easy
bruising is a platelet/VWD phenotype, not a hallmark of haemophilia A, whose
signature is deep bleeding (haemarthrosis, muscle haematoma).

### 15. `Polycythemia_Vera` — deep-research boilerplate as evidence

The `references[].findings[].evidence[]` items are DR-generated stubs where
`snippet == statement == supporting_text` and every explanation reads *"Deep research
cited this publication as relevant literature for Polycythemia Vera."* Several are
degenerate:

- `snippet: "The Swedish nationwide study by Leontyeva et al."` marked `supports: SUPPORT`
- `snippet: "of review Development of hepcidin therapeutics has been…"` — a truncated
  "Purpose of review" fragment

These are non-informative and should be dropped or converted to real evidence items.

---

## Low-severity / conventions

- **`genetic[]` HGNC bindings missing**: DBA 10/10, Beta_Thalassemia 4/4,
  Sickle_Cell_Disease 3/3, Polycythemia_Vera 3/3, Alpha_Thalassemia 2/2. In the
  thalassemias and SCD the genes *are* bound in `pathophysiology[].genes`, so the
  fix is mechanical. `Hereditary_Spherocytosis` (5/5 bound) is the model.
- **Subtype naming**: `Hereditary_Spherocytosis`, `Beta_Thalassemia`, and
  `Alpha_Thalassemia` all use long parenthetical subtype `name` values
  (`"Hemoglobin Bart Hydrops Fetalis Syndrome (Four Alpha-Globin Genes Deleted)"`)
  against the CLAUDE.md rule to keep `name` slug-friendly and put verbose labels in
  `display_name`. None carry `subtype_term` despite MONDO terms existing.
  `Hemophilia_A` (`Severe`/`Moderate`/`Mild` + `subtype_term`) is the model.
- **Unbound `inheritance_term`**: `Beta_Thalassemia` (`Autosomal recessive`, no term,
  no evidence) and `Alpha_Thalassemia` (no term). `Hemophilia_B` has no `inheritance:`
  block at all despite being X-linked throughout.
- **Metadata**: `Beta_Thalassemia` has no `creation_date` — only the deprecated
  `updated_date`. The deprecated `percentage` field is still populated on recently
  edited prevalence records in Hemophilia A/B and VWD.
- **`Beta_Thalassemia` node genes**: `Alpha-Globin Chain Excess` lists `HBA1`/`HBA2` in
  `genes:`. In β-thalassemia those loci are normal — the excess is stoichiometric.
  Listing them as node genes implies pathogenicity.
- **Unverifiable reference**: `Alpha_Thalassemia.treatments[6]` cites
  `url:https://www.fda.gov/...` with no cache file; `url:` references sit outside the
  reference-validation stack entirely.
- **Thin fragment snippets** in `Alpha_Thalassemia`: `"Couples who are members of
  populations at risk"`, `"hematologic and hemoglobin (Hb) findings"`, `"chelation
  therapy for iron overload"` — sentence stubs that carry no claim standing alone.
  `Iron Overload` is banded `FREQUENT` on the strength of *"iron chelation therapy
  should be instituted."*
- **Upstream data artifact**: `Sickle_Cell_Disease` quotes
  `"1-5 / 10 000 | Europe | Point prevalence | PMID:2019"` from `ORPHA:232` — a year
  mis-parsed as a PMID in the Orphanet source. Faithful quote, upstream ingestion bug.
- **`Polycythemia_Vera`** has no `prevalence:` block, and its
  `classifications.icdo_morphology: Leukemia` is a forced approximation — PV is
  ICD-O 9950/3 (MPN block), and `ICDOMorphologyEnum` has no myeloproliferative value.
  A schema-enum gap rather than a curation error.

---

## Suggested priority

1. Fix the `NO_EVIDENCE`/explanation contradiction on the ITP antibody node (#1).
2. Re-band or `subtype:`-scope the Alpha_Thalassemia phenotypes (#3).
3. Audit Orphanet-derived frequency bands in `Hereditary_Spherocytosis` and
   `Polycythemia_Vera`, and drop the invented mechanistic descriptions (#5).
4. Evidence the Beta_Thalassemia phenotype block (#6) and the Polycythemia_Vera
   treatment block (#4) — the sources are largely already in each file's
   `references:` list.
5. Mechanical sweep: `gene_term` bindings, `inheritance_term` bindings, subtype
   naming, `creation_date`.

## Reproducing

```bash
uv run linkml-validate --schema src/dismech/schema/dismech.yaml \
  --target-class Disease kb/disorders/<file>.yaml
just validate-references kb/disorders/<file>.yaml
just validate-terms-file kb/disorders/<file>.yaml
```
