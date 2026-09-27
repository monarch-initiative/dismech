# Blood Disorders Claim–Evidence Review (2026-07-25)

Correctness review of 10 haematology entries in `kb/disorders/`, focused on whether
each asserted claim is actually carried by the evidence attached to it.

> **State this report describes:** rebased onto `main` at `e85b40a8`. Findings were
> re-verified against that tree. One finding (#1, ITP) had been fixed upstream in the
> interim and is marked RESOLVED; the other fourteen still reproduce.
> `just count-verified-snippets` over the ten entries at this commit reports
> `362/372 verified (10 skipped by prefix)` — see Mechanical validation for what the
> skipped ten are and why it matters.

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
- Snippet fidelity, via the repo's own tool
  (`uv run python -m dismech.reference_snippet_audit`, i.e. `just count-verified-snippets`)
  over the ten entries at this tip:

  ```
  Snippets checked: 362/372 verified against cached references (10 skipped by prefix)
  ```

  **Zero mismatches — but "372" is not "every snippet in these files."** Ten are never
  checked by anything: the `DOI:`-prefixed items in `Polycythemia_Vera.yaml`, because
  `DOI` sits in `skip_prefixes` in `conf/reference_validator_config.yaml`. Neither the
  reference validator nor the fast audit reads them. Those ten are *exactly* the
  deep-research boilerplate stubs that finding #15 flags as degenerate — so the items
  most at risk of being junk are the ones no tool verifies. One further reference has no
  cache file at all: `url:https://www.fda.gov/...` in `Alpha_Thalassemia.treatments[6]`.

Full text is cached for 20 of the cited references; the remainder are `abstract_only`.
Findings were first reached from abstracts, then re-checked against full text (see
[Full-text re-examination](#full-text-re-examination)).

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
| Immune_Thrombocytopenia | ~~3/4~~ → 0/4 | ~~3~~ → 0 | ~~5/5~~ → 0/6 | 0/4 | — |
| Polycythemia_Vera | 0/26 | 0 | 5/5 | 3/4 | 3/3 |
| Diamond-Blackfan_Anemia | 0/8 | 0 | 2/6 | 0/3 | 10/10 |

`Hemophilia_A` and `Hemophilia_B` are the reference-quality entries: every
phenotype, treatment, and pathophysiology node is evidenced.

---

## High-severity findings

### 1. `Immune_Thrombocytopenia` — the defining mechanism is marked `NO_EVIDENCE` but the explanation claims confirmation

> **RESOLVED UPSTREAM — fixed on `main` before this report merged.** The contradictory
> explanation is gone, replaced by an honest one stating the snippet enumerates therapies
> "rather than directly evidencing autoantibody-mediated platelet destruction; retained for
> context". A proper supporting item was added: PMID:30801909, a meta-analysis naming
> "anti-glycoprotein IIbIIIa or anti-glycoprotein IbIX" — exactly the two glycoproteins in
> the node description. The rest of the entry was filled in too: all 4 phenotypes and all 6
> treatments now carry evidence (was 3/4 and 5/5 unevidenced). Recorded for the pattern, not
> as outstanding work.


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

> **Revised after full-text review — see Full-text re-examination below.** Downgraded: the
> evidence exists in PMID:40246933, already cited 11× in this file.


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

> **Revised after full-text review — see Full-text re-examination below.** Strengthened: PV
> `Splenomegaly` is numerically contradicted (~30%) by the entry's own primary source.


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

> **Revised after full-text review — see Full-text re-examination below.** Downgraded: the
> evidence is in PMID:20492708, already cited 9× — one sentence is already quoted in this file.


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

> **Revised after full-text review — see Full-text re-examination below.** Moderated: RPL35A is
> a genuine DBA gene; the citation is secondary and a better snippet exists.


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

---

## Full-text re-examination

The reference cache holds full text for 20 of the cited references (the rest are
`abstract_only`). The findings above were reached from abstracts; re-reading the full
texts changes four of them and leaves the rest intact. Sources behind findings #1, #2,
#7, #9, #10, and #11 are all still `abstract_only`, so those are unaffected.

### #4 downgraded — Polycythemia_Vera's evidence exists, in a paper already cited 11×

PMID:40246933 (*Polycythaemia vera*, Nat Rev Dis Primers) is cached in full (18,782
words) and supplies clean support for every unevidenced treatment and for the JAK2
node. This is a distribution problem, not a sourcing problem. Ready-to-use snippets:

| Target | Snippet from PMID:40246933 |
|---|---|
| `Hydroxyurea`, `Ruxolitinib`, `Interferon-alpha` | "Hydroxyurea or interferons remain the preferred first-line cytoreductive agents, with the JAK1 and JAK2 inhibitor, ruxolitinib, currently approved for the treatment of patients who are resistant to, or intolerant of, hydroxyurea." |
| `Therapeutic Phlebotomy`, `Low-Dose Aspirin` | "High-risk patients are those aged ≥60 years and/or with a history of thrombosis, and typically are eligible for cytoreductive therapy, in addition to therapeutic phlebotomy and low-dose aspirin." |
| `JAK2 V617F Constitutive Activation`, and the entry's uncited "~95% of PV cases" | "Case ascertainment in epidemiological studies has been refined by the demonstration in 2005 that most patients (~95%) have the acquired (somatic) mutation JAK2V617F, indicating clonal disease" |
| the node's pseudokinase description | "the other is a pseudokinase domain located upstream of the kinase domain that binds ATP, but has no or a very weak ability to directly phosphorylate substrates" |

One sentence closes three treatments at once, and it matches the entry's ruxolitinib
description almost word for word.

**Two rows were withdrawn from this table after review, and the reason is the point of
the section below.** The original JAK2 row proposed *"A unique clonal JAK2 mutation
leading to constitutive signalling causes polycythaemia vera"* — which is a **bibliography
entry** at `references_cache/PMID_40246933.md:1876-1877`, the title of James et al. 2005
(PMID:15793561), not a claim by the Nat Rev review. Attributing it to PMID:40246933 is a
misattribution, and quoting a title as a finding separately violates CLAUDE.md §6
("A Title Is Not a Finding"). It would have passed `count-verified-snippets` cleanly.
This report identified that exact hazard two sections down and then walked into it — the
flattened full-text grep used to find candidates did not distinguish body from back
matter. Cite PMID:15793561 directly if the 2005 claim is wanted; the replacement row
above is genuine body text and covers the same ground.

A phlebotomy row quoting *"Need for phlebotomy to keep haematocrit <45%"* was also
withdrawn: at `PMID_40246933.md:1520` that is a bullet under **"Hydroxyurea resistance
after 3 months of treatment"**, so its subject is a resistance criterion, not a treatment
goal. The high-risk-patients row already covers phlebotomy and aspirin without the caveat.

### #5 strengthened — the Orphanet splenomegaly band is numerically contradicted

The original argument was clinical implausibility. The full text makes it concrete:

> "palpable splenomegaly (present in about 30% of patients at diagnosis)"

The entry bands `Splenomegaly` as `VERY_FREQUENT` (80–99%) on Orphanet's authority. The
review the entry already cites 11 times says ~30% — `FREQUENT` at best, right at the
band boundary. So this is no longer a judgement call about Orphanet's reliability; it is
a direct numerical conflict with the entry's own primary source.

### #6 downgraded — Beta_Thalassemia's evidence is already in the file

PMID:20492708 (GeneReviews *Beta-thalassemia*) is cached in full (13,213 words) and
already cited 9 times. Two sentences cover roughly ten of the seventeen unevidenced
phenotypes:

> "extramedullary hematopoiesis and its complications (osteoporosis, masses of
> erythropoietic tissue that primarily affect the spleen, liver, lymph nodes, chest and
> spine, and bone deformities and typical facial changes), gallstones, painful leg
> ulcers and increased predisposition to thrombosis."

covers `Extramedullary Hematopoiesis`, `Osteoporosis`, `Splenomegaly`, `Hepatomegaly`,
`Cholelithiasis`, and `Frontal Bossing`. And:

> "Findings in untreated or poorly transfused individuals with thalassemia major … are
> growth retardation, pallor, jaundice, poor musculature, hepatosplenomegaly, leg
> ulcers, development of masses from extramedullary hematopoiesis, and skeletal changes
> that result from expansion of the bone marrow."

covers `Short Stature`, `Jaundice`, and reinforces the rest — and is **already quoted in
this very file**, under `biochemical[4] Indirect Bilirubin`. Plus:

> "However, cardiac disease remains the main cause of death in patients with iron overload."

which directly evidences the previously uncited *"leading cause of death in
transfusion-dependent beta-thalassemia"* claim on `Cardiomyopathy`, and:

> "Cardiac involvement in thalassemia intermedia results mainly from a high-output state
> and pulmonary hypertension"

for `Pulmonary Hypertension`.

**Caveat that survives:** these sentences establish *occurrence*, not the frequency
*bands*. Attaching them fixes the "no evidence at all" problem but not the
`VERY_FREQUENT`/`FREQUENT` justification, which still needs quantitative sources or
omission per `docs/frequency-evidence-guidelines.md`.

### #8 moderated — RPL35A is a real DBA gene, the citation is just secondary

The full text of PMID:19773262 shows the paper treats RPL35A as established throughout,
not only in its abstract's background. Its Introduction:

> "The genetic basis of DBA is heterogeneous. Approximately 40% of patients have
> mutations in one of the genes for ribosomal proteins (RP): RPS7, RPS17, RPS19, RPS24,
> RPL5, RPL11, or RPL35A."

and its Discussion notes that genotype–phenotype data are unavailable for RPS24, RPS17,
and RPL35A "because the number of subjects studied are too small" — i.e. the negative
result is a cohort limitation, not a refutation. So the entry's substance is right; the
citation is attributive rather than primary.

Better still, that Introduction sentence is a **strictly better snippet** than the one
in use, and it would simultaneously evidence `RPS7`, `RPS17`, and `RPS24`, which
currently have no evidence at all. Downgrade #8 from "wrong paper" to "secondary
citation, better snippet available."

### #9 — partially improved, sub-point stands

A better snippet exists for the malformation claim:

> "Most of the patients with RPL5 (83%) and RPL11 (73%) mutations had physical malformations."

But the paper's own results prose still contains no thumb-specific claim, so binding
`Triphalangeal Thumb` to a hand-malformation quote remains an over-read. Thumb data
appear only in per-patient table rows, which are not clean snippet material.

### One live example of the full-text quoting risk

The string *"Ribosomal protein L5 and L11 mutations are associated with cleft palate and
abnormal thumbs in Diamond-Blackfan anemia patients"* appears in the PMID:19773262 cache
and would validate as a snippet — but it is a **title in the bibliography**, not a claim
by that paper. Worth a lint rule: flag snippets that match only inside a reference list.

---

## Suggested priority

1. ~~Fix the `NO_EVIDENCE`/explanation contradiction on the ITP antibody node (#1).~~
   **Done upstream** — resolved on `main` with PMID:30801909 before this report merged.
2. Re-band or `subtype:`-scope the Alpha_Thalassemia phenotypes (#3).
3. **Cheap and mechanical, now that full text is cached:** attach the
   Polycythemia_Vera treatment/JAK2 snippets and the Beta_Thalassemia phenotype
   snippets tabulated above (#4, #6). No new literature search required.
4. Re-band PV `Splenomegaly` down from `VERY_FREQUENT` — contradicted at ~30% by the
   entry's own primary source (#5) — then audit the remaining Orphanet bands in PV and
   `Hereditary_Spherocytosis` and drop the invented mechanistic descriptions.
5. Swap the DBA `RPL35A` snippet for the Introduction sentence and reuse it for
   `RPS7`/`RPS17`/`RPS24` (#8).
6. Mechanical sweep: `gene_term` bindings, `inheritance_term` bindings, subtype
   naming, `creation_date`.

## Reproducing

```bash
# per-edit loop (seconds, offline)
just validate kb/disorders/<file>.yaml
just count-verified-snippets kb/disorders/<file>.yaml

# pre-PR sweep over all changed files at once — what CI runs
just validate-disorders kb/disorders/<file>.yaml ...
```

The snippet counts quoted above come from `just count-verified-snippets` over all ten
entries in one invocation. Avoid per-file `just validate-references`: CLAUDE.md records
it at 65 minutes for a single entry, and `just validate-terms-file` — cited in an earlier
draft of this section — is not a recipe at all (`just validate-terms <file>` is).
