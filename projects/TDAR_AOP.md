---
title: TDAR AOP Network
status: IN_PROGRESS
description: >-
  Reading the three AOP-Wiki pathways that terminate at impaired T-cell dependent
  antibody response against dismech's own humoral-immunity modeling, in both
  directions: what the comparison exposes about dismech, and what dismech exposes
  as knowledge gaps in the TDAR AOPs.
tags: [FRAMEWORK_ALIGNMENT, EVIDENCE, EXTERNAL_COLLABORATION, IMMUNOLOGY, KNOWLEDGE_GAP]
diseases:
  - Autosomal_Agammaglobulinemia
  - Common_Variable_Immunodeficiency
  - Specific_Antibody_Deficiency
  - X-linked_Agammaglobulinemia
  - Hyper-IgM_Syndrome_Type_2
  - Selective_IgA_Deficiency
  - Activated_PI3K-delta_Syndrome
  - Kabuki_Syndrome
  - Follicular_Lymphoma
modules:
  - germinal_center_reaction
  - phagocyte_oxidative_burst_failure
  - complement_dysregulation
  - innate_antiviral_interferon_response
  - molecular_mimicry_autoimmunity
  - necrotizing_vasculitis
  - il6_hypercytokinemia
  - cgas_sting_pathway_activation
---

# TDAR AOP Network

## Scope

The T-cell dependent antibody response (TDAR) is a functional immunotoxicology
endpoint. Three AOP-Wiki pathways terminate at it — **AOP 154** (calcineurin
inhibition), **AOP 277** (impaired IL-1R1 signaling) and **AOP 315** (JAK3
inhibition) — and a fourth, **AOP 14** (glucocorticoid receptor activation),
terminates at increased disease susceptibility while sharing intermediate Key
Events with them.

This project uses that cluster as a comparator against dismech's own modeling of
humoral immunity. It is a two-way comparison, and the two directions are kept
separate because they have different audiences and different standards of proof.

This page records findings. It does not decide adoption: whether dismech gains a
module, an edge, or a schema construct as a result belongs in its own issue.

The AOP-side observations are **not** being tracked as dismech work. They are
findings about the framework rather than about this repository, and no issue,
worklist, or follow-up here depends on them. They are recorded on this page
because the comparison produced them, and that is all.

**Relationship to [`AOP_EMOD_ALIGNMENT`](AOP_EMOD_ALIGNMENT.md).** That project
asks how dismech's constructs map onto the AOP/EMOD data model, grounded on
`Lead_Poisoning`. This one asks what a specific, well-populated AOP cluster
reveals when set against a specific, well-populated dismech module. The first is
a schema comparison; this is a content comparison. They are expected to inform
each other.

## Lines of questioning

### A. What elements of dismech are exposed through comparison of TDAR AOPs?

Open.

### B. How does dismech expose knowledge gaps in TDAR AOPs?

Open.

Further questions under each line are expected to follow once the first are
answered.

## Provenance

The starting material is an OpenScientist autonomous deep-research run,
commissioned to assemble a TDAR-centred AOP network with assay-anchored Key
Events and to aggregate evidence for a causal linkage between TDAR and increased
susceptibility to infection.

| Field | Value |
|---|---|
| Provider | OpenScientist (`openscientist-autonomous`) |
| Job ID | `7e9ef238-7aae-4374-b936-1d312f62c1d5` |
| Status | completed |
| Created | 2026-09-14T21:05:03Z |
| Report | [`TDAR_AOP/openscientist-tdar-aop-network.md`](TDAR_AOP/openscientist-tdar-aop-network.md) |
| Artifacts | `TDAR_AOP/artifacts/` — two network JSONs and their rendered PNGs |

Two companion documents sit beside the report in `TDAR_AOP/`. Neither renders on
the website — only top-level `projects/*.md` does — so they are read in the
repository:

- [`TDAR_AOP/failed-claims.md`](TDAR_AOP/failed-claims.md) — the report's claims
  that do not survive checking against their own sources, each with the claim in
  the report's own words, what was checked, and what the source says.
- [`TDAR_AOP/findings-to-actions.md`](TDAR_AOP/findings-to-actions.md) — a
  checklist over all twelve finding sections, separating the ones implying work
  in this repository from the ones that are observations about the AOP framework
  with no dismech action.

The report is a **lead**, not a source. Its citations have not been put through
`just validate-research-references`, and the verification below was done by hand
against AOP-Wiki and PubMed. The provider bundle also contained iteration
transcripts, container logs and a PDF rendering of the same report; those are
recoverable from the job and are not committed.

**AOP-Wiki snapshot.** AOP-Wiki figures below are from the `09-03-2026` export
unless a figure names another snapshot: the F010 ratings check and the
infection-outcome census were both run against `09-15-2026`. Export counts move
between dates — 1,602 events in `09-15-2026` against 1,598 in `08-06-2026` — so
which snapshot produced a figure is load-bearing for anyone re-running it. Both
were read through
[`aop-wiki-cli`](https://github.com/gingin77/aop_wiki_cli). AOP-Wiki is not a
citable reference in dismech's validation stack — there is no `AOP:` prefix and
no fetcher — so anything curated from it must cite the primary literature
instead.

## Verification record

What follows was checked directly, and in several places it does not agree with
the report.

### The TDAR → infection edge is not curated anywhere

KE984 (*Impairment, T-cell dependent antibody response*, AOPs 154 and 277) and
KE1719 (*Impairment of T-cell dependent antibody response*, AOP 315) are both
terminal Adverse Outcomes with **zero downstream Key Event Relationships**. The
link the report was commissioned to establish is not a KER, so it carries no
weight-of-evidence or empirical-support table.

This is a consequence of the OECD review of AOP 277. That AOP was originally
titled *"Impaired IL-1R1 signaling leading to increased susceptibility to
infection"*; reviewers found "susceptibility to infection" hard to define as a
measurable Adverse Outcome, and it was replaced by the TDAR endpoint. Nothing
re-attached the infection outcome downstream, so the claim was orphaned rather
than strengthened.

### What survives in AOP-Wiki is one field, and it is about a different assay

The only quantitative bridge to infection in the cluster is the
`quantitative_understanding` field of KER2928 (*Suppression of T cell activation
→ Impairment, TDAR*), 207 characters:

> "Luster et al (1993) demonstrated that Concanavalin A response of splenocytes
> showed the linear dose-response relationship with the host resistnace to
> Listeria monocytogenes or Streptococcus pneumoniae."

Concanavalin A splenocyte proliferation, not TDAR — one Key Event upstream. The
report inherited that substitution rather than introducing it.

### The High/High weight-of-evidence ratings are not in the export

The report's F010 presents a table of terminal-KER ratings — Evidence **High**,
Quantitative Understanding **High** for all three AOPs — introduced as
"Extraction of the AOP-Wiki Key Event Relationship (KER) weight-of-evidence
tables". No such tables are present.

In the `09-15-2026` export, each KER's four evidence blocks carry `free_text`,
`tables` and `headers`. For all three terminal KERs, `tables` is empty, `headers`
is empty, `has_any_tables` is `false`, and no `High` / `Moderate` / `Low` token
appears anywhere in the record:

| KER | AOP | Edge | `weight_of_evidence` | `quantitative_understanding` | Rating tokens |
|---|---|---|---|---|---|
| KER1510 | 154 | IL-2 & IL-4 suppression → Impaired TDAR | **0 chars** | **0 chars** | none |
| KER2928 | 277 | Suppression of T-cell activation → Impaired TDAR | 1,506 chars | 207 chars | none |
| KER2027 | 315 | IL-4 suppression → Impaired TDAR | 260 chars | 292 chars | none |

Character counts are measured **after** HTML stripping; AOP-Wiki free-text fields
hold raw HTML, and a direct cache read has to strip it. The three KER records were
read from `all_kers_09-15-2026.json`, materialized by the command in
*Reproducing it* above and keyed by the AOP-Wiki KER IDs shown.

Nor are the ratings on the parent AOP records, whose `woe_evidence` is narrative
prose rather than a ratings table. AOP 277 and AOP 315 contain no rating token at
all; AOP 154 contains only **Moderate**, never High.

So the claim that the terminal KER is rated High/High in all three pathways, and
the "exceptional confidence" the report draws from it, cannot be confirmed from
the export, and the one rating word that does appear anywhere in the three AOP
records is weaker than the claim. KER1510 is the sharpest case: AOP 154 is the
OECD-endorsed pathway of the three, and its terminal KER carries no evidence text
whatsoever. AOP 315, by contrast, is still `Under Development`.

This does not prove the ratings do not exist — they may be held in a structured
field the XML export does not carry, or be visible on the rendered wiki page. It
does mean the report's stated method, extraction from KER weight-of-evidence
tables, cannot have produced them from this data.

### The primary source does not support the reading placed on it

[PMID:8365588](https://pubmed.ncbi.nlm.nih.gov/8365588/) (Luster et al. 1993,
*Risk assessment in immunotoxicology. II*) is the origin of the quantitative
claim. Three statements in its own abstract qualify it:

- *"No single immune test could be identified which was fully predictive for
  altered host resistance, although most assays were relatively good indicators
  (i.e., > 70%)."*
- *"A good correlation exists between changes in the immune tests and altered
  host resistance in that there were no instances where host resistance was
  altered without affecting an immune test(s). However, in some instances immune
  changes occurred without corresponding changes in host resistance."* — this
  establishes the immune tests as sensitive detectors of immunotoxicity, not as
  predictors that a suppressed response means more infection. The AOP needs the
  converse direction.
- The linear model was confirmed for cyclophosphamide only: *"For most of the
  relationships this could not be confirmed using a large chemical data set and,
  thus, a more mechanistically based approach for modeling will need to be
  developed."*

The frequently quoted *"enumeration of lymphocyte populations and quantitation of
the T-dependent antibody response were particularly beneficial"* describes
predicting **immunotoxicants**, and cites the 1992 companion paper rather than
this one. The 1993 abstract names it outright — *"(Luster et al., Fundam. Appl.
Toxicol., 18, 200-210, 1992)"* — immediately before that sentence, so the
identification rests on the paper's own citation and not on inference.

One statement in the **1993** abstract cuts the other way, toward the AOP's
reading, and is recorded here so the page carries both sides — conclusion (3):

> "The ability to resist infectious agent challenge is dependent upon the degrees
> of immunosuppression and the quantity of infectious agent administered."

That is a dose-dependence claim about immunosuppression and host resistance, and
it is the paper's clearest support for a graded relationship. What it does not
supply is the part the pathway needs: it names neither TDAR nor any single immune
test as the measure of "degrees of immunosuppression", which is what conclusion
(2) explicitly declines to do.

### The 1992 companion paper does not say TDAR is best, or that it predicts infection

Following that citation to its source —
[PMID:1534777](https://pubmed.ncbi.nlm.nih.gov/1534777/) (Luster et al. 1992,
*Risk assessment in immunotoxicology. I. Sensitivity and predictability of immune
tests*) — settles two things the "particularly beneficial" phrase is routinely
used to imply.

**TDAR ranked second, not first.** The abstract reports:

> "The tests that showed the highest association with immunotoxicity were the
> splenic antibody plaque forming cell response (78%) and cell surface marker
> analysis (83%)."

The splenic antibody plaque-forming cell response *is* the TDAR assay. At 78% it
is outscored by cell surface marker analysis at 83%. "Among the most predictive"
is fair; anything stronger is not.

**And the 78% measures a different endpoint.** It is the association with
*immunotoxicity* — the ability to detect an immunotoxic compound — not with
susceptibility to infection. The same abstract says the host-resistance question
was still open at the time:

> "Efforts are currently underway using this database to determine the
> relationships between these immune tests and susceptibility to challenge with
> infectious agents or transplantable tumor cells."

That work became the 1993 paper above, whose conclusion (2) is that no single
immune test was fully predictive of altered host resistance.

So the chain of attribution closes without ever establishing the claim it is
cited for. The phrase is real and sits in the 1993 abstract; it points to 1992;
and 1992 measures compound detection, ranks TDAR second, and explicitly defers
the infection question to the paper that then declines to answer it in TDAR's
favour.

### Reframed from TDAR to impaired antibody response, the evidence is strong

[PMID:20675197](https://pubmed.ncbi.nlm.nih.gov/20675197/) (Orange et al. 2010),
a meta-analysis of 17 studies, 676 patients and 2,127 patient-years in primary
immunodeficiency with hypogammaglobulinemia:

> "Pneumonia incidence declined by 27% with each 100mg/dL increment in trough IgG
> (incidence rate ratio, 0.726; 95% confidence interval, 0.658-0.801). Pneumonia
> incidence with maintenance of 500 mg/dL IgG trough levels (0.113 cases per
> patient-year) was 5-fold that with 1000 mg/dL (0.023 cases per patient-year)."

Human, quantitative, with confidence intervals, and interventional rather than
correlational — immunoglobulin replacement moves the exposure, and restoring the
antibody level restores resistance to infection in a graded way.

Compare what the TDAR framing rests on: a single rodent database — assembled by
the NTP tier-approach screening battery reported in 1988, and analysed for
host-resistance relationships in 1993
([PMID:8365588](https://pubmed.ncbi.nlm.nih.gov/8365588/)) — whose own abstract
states that no single immune test was fully predictive of altered host
resistance. The reframed claim is not a stronger version of the TDAR claim. It
is a different claim — about a measured serum protein in patients rather than an
assay endpoint in mice — and it is the one the evidence actually supports.

### The infection outcome is barely represented, as nodes or as edges

This is a claim about the whole of AOP-Wiki, so it is stated with the query that
produces it.

#### Reproducing it

```bash
# 1. Pin the CLI. c24ce8c is published on origin/main.
#    Point the data directory anywhere that is NOT a dismech checkout.
export AOP_WIKI_CLI_DATA_DIR=~/aop-wiki-data

# 2. Materialize a dated snapshot. Any KER command parses the full XML and
#    writes all_events_<date>.json and all_kers_<date>.json under
#    $AOP_WIKI_CLI_DATA_DIR/outputs/cache/<date>/. This is the slow step.
uvx --from git+https://github.com/gingin77/aop_wiki_cli@c24ce8c aop-wiki-cli \
  find-kers-for-events --ke-terms "antibody" --date 09-15-2026
```

**3. The filter.** Over `all_events_<date>.json`, select every event whose
`title` matches, case-insensitively,
`infect|host resist|susceptib|pathogen load|viral (load|titer)`. For each, record
`level_of_biological_organization` and the character counts of `description` and
`measurement_method` after HTML stripping. Then over `all_kers_<date>.json`,
select every KER whose `downstream_ke.id` is one of those events, and record the
character counts of the four evidence blocks.

That last step is an ad-hoc read of the CLI's cache, which is what the
`aop-wiki-cli` skill permits while working in that directory. It is deliberately
**not** committed as a dismech script: the CLI owns the parsers and the entity
model, and the durable home for this query is a command there rather than
parsing code in this repository.

#### The census

Snapshot `09-15-2026`: **1,602 events, 2,373 KERs.**

Every Key Event in the entire wiki denoting an infection or host-resistance
outcome:

| KE | Title | AOPs | Level | `description` | `measurement_method` | KERs into it |
|---|---|---|---|---|---|---|
| 323 | Increased, Disease susceptibility | 14 | Individual | **0 chars** | **0 chars** | none |
| 576 | Increased, Viral susceptibility | 84, 85 | Individual | **0 chars** | **0 chars** | KER570 |
| 1412 | Helicobacter pylori infection | 229 | Tissue | **0 chars** | **0 chars** | none |
| 1939 | Viral infection and host-to-host transmission, proliferated | 430 | Individual | 7,037 chars | 1,204 chars | KER2498 |

Four events. Two incoming relationships. The evidence on those two:

| KER | Edge | WoE / Empirical / Plausibility / Quantitative |
|---|---|---|
| KER570 (AOPs 84, 85) | Suppression, Immune system → Increased, Viral susceptibility | 0 / 0 / 0 / 0 |
| KER2498 (AOP 430) | Increased SARS-CoV-2 production → Viral infection and host-to-host transmission | 67 / 5,680 / 2,257 / 3,545 |

Separately, KER3702 (AOP 618) is the only downstream edge from AOP-Wiki's one
*Reduced antibody production* Key Event (KE2398). It runs to *Diminished vaccine
response* rather than to infection, and its four evidence blocks are also empty.

#### What it means

Across the whole immunosuppression space the wiki carries no evidence-bearing
edge into an infection outcome, and the outcome nodes themselves are mostly
empty: three of the four carry no definition and no statement of how they would
be measured. The framework names the outcome and then leaves it unspecified,
which is consistent with what the AOP 277 reviewers said when they removed it —
that susceptibility to infection was hard to define as a measurable Adverse
Outcome. It also explains KE323 having no incoming relationship at all: an
undefined node is hard to draw an evidenced edge into.

The relationship is well established in medicine — it is why immunoglobulin
replacement is standard care in primary antibody deficiency — and absent from the
framework.

**KER2498 is the one exception, and it is not a counterexample.** It is the only
evidence-bearing edge into any infection node in the wiki, and it is richly
evidenced. But it runs from SARS-CoV-2 production to onward transmission: its
description is about respiratory droplets, aerosols, fecal-oral spread, masks and
surface disinfection, and its assay detects virus or antibody in a person. It
measures a virus establishing itself and spreading between hosts, not a host
losing the capacity to resist one. Note that
`level_of_biological_organization` does **not** carry this distinction — KE576
and KE1939 are both tagged `Individual` — so the difference has to be read from
the records rather than inferred from that field.

## Module classification

The modules in `kb/modules/` that touch antibody response, with their terminal
nodes and conformer counts. Tiering matters: a module in which antibodies appear
as pathogenic effectors says nothing about whether a patient can mount a
protective response, and must not be counted as coverage.

### Tier 1 — models the antibody response itself

| Module | Role | Terminal node | Conformers |
|---|---|---|---|
| `germinal_center_reaction` | The adaptive humoral arm end to end: antigen capture → Tfh help → GC reaction (AID-dependent SHM/CSR) → affinity-matured class-switched output → durable humoral immunity. Models the normal process; conformers set direction with modifiers. | **Durable Protective Humoral Immunity** (`downstream: []`) | 6 |

### Tier 2 — sibling arms of host defense

Each is declared complementary in `germinal_center_reaction`'s own description.

| Module | Role | Terminal node | Conformers |
|---|---|---|---|
| `phagocyte_oxidative_burst_failure` | NOX2 respiratory-burst failure; innate cellular arm | **Recurrent Bacterial and Fungal Infection** | 3 |
| `complement_dysregulation` | Loss of control over the alternative pathway | Complement-Mediated Tissue Injury Syndrome | 4 |
| `innate_antiviral_interferon_response` | Sensing → interferon-induced antiviral state | Restriction of Viral Replication | 6 |

### Tier 3 — antibodies as pathogenic effectors, not as response capacity

| Module | Role | Conformers |
|---|---|---|
| `molecular_mimicry_autoimmunity` | Cross-reactive autoantibody generation | 3 |
| `necrotizing_vasculitis` | ANCA / immune-complex vessel-wall injury | 8 |
| `cgas_sting_pathway_activation` | Antibodies incidental to the chain | 3 |
| `il6_hypercytokinemia` | Antibodies incidental to the chain | 2 |

### Conformance state of the antibody-deficiency entries

At the time of this survey, `germinal_center_reaction`'s description named five
entries as intended conformers and three of the six antibody-deficiency entries
declared `conforms_to`. That gap is what issue #11897 was opened against, and it
has since been closed — so both states are recorded here, because the survey
finding is what motivated the work and the current state is what a reader needs.

| Entry | At the survey | Now (`main`) |
|---|---|---|
| `Common_Variable_Immunodeficiency` | `#Germinal Center Reaction` | unchanged |
| `Specific_Antibody_Deficiency` | `#Affinity-Matured Class-Switched B Cell Output` | unchanged |
| `Autosomal_Agammaglobulinemia` | `#Durable Protective Humoral Immunity` | unchanged |
| `X-linked_Agammaglobulinemia` | **none** | `#Durable Protective Humoral Immunity` |
| `Hyper-IgM_Syndrome_Type_2` | **none** | `#Germinal Center Reaction` |
| `Selective_IgA_Deficiency` | none | **none — deliberate** |

All anchors are on `germinal_center_reaction`; the module stem is elided in the
table for width.

So five of six now declare, not three. `Selective_IgA_Deficiency` remains
unconformed on purpose: #11897 recorded it as genuinely uncertain — the defect is
isotype-restricted, the entry records intact heavy-chain alpha loci, its genetics
are associative rather than a lesion in the chain, and mucosal IgA sits partly in
the T-independent territory the module explicitly scopes out. A recorded decision
not to conform was named there as an acceptable outcome, and that is the outcome.

The module description was updated in the same work and now names seven entries
in the decreased-or-absent direction rather than five.

Also conforming: `Activated_PI3K-delta_Syndrome`, `Kabuki_Syndrome` (both in the
decreased direction) and `Follicular_Lymphoma` (dysregulated direction).

### The structural observation

`phagocyte_oxidative_burst_failure` terminates at **Recurrent Bacterial and
Fungal Infection**. `germinal_center_reaction` terminates one step earlier, at
**Durable Protective Humoral Immunity**, with nothing downstream — the same place
AOP-Wiki's KE984 stops.

dismech already carries "increased susceptibility to infection" in its module
vocabulary, on the innate arm. It is absent from the humoral one. Both frameworks
stop at the same node, independently.

### Where the report's chemical branches would go

`germinal_center_reaction`'s notes list, as explicitly out of scope and "to be
argued as its own module", *iatrogenic B-cell depletion (rituximab, transplant
immunosuppression)*. The report's calcineurin, JAK3, AhR and glucocorticoid
branches fall within that reservation. Note that dismech currently holds no
drug- or chemical-induced immunosuppression disease entries: cyclosporine,
tacrolimus and JAK inhibitors appear throughout `kb/disorders/` as treatments,
not as toxicity entries. Any such module would begin with no conformers.

## Not yet explored

- The remainder of the OpenScientist report. The verification above covers its
  central causal claim and the network structure. Six of its twelve finding
  sections have not been checked: the assay mapping (F004), the 2026 B6C3F1/N in
  vivo dataset (F006, F013), the convergent-literature section citing Burleson,
  Descotes and White (F007), the 2024 *Front. Toxicol.* mapping said to confirm
  the four-AOP network independently (F008), the regulatory-framework and NAM 3R
  section (F011), and the AhR/PAC branch (F012, F014).
- One checked section was only partly checked. F009's sources
  ([PMID:30068597](https://pubmed.ncbi.nlm.nih.gov/30068597/), Bohrer 2018;
  [PMID:26430088](https://pubmed.ncbi.nlm.nih.gov/26430088/), Cippà 2015) were
  assessed for what they bear on — both skip the TDAR node — but not verified
  against their abstracts.
- The report's own five limitations and six proposed follow-up experiments have
  not been assessed at all.
- Whether the F010 High/High ratings exist anywhere outside the XML export — in a
  structured field the export does not carry, or on the rendered AOP-Wiki KER
  pages. The check above establishes only that they are not extractable from the
  export by the method the report states.
- Only the abstract of the 1992 companion paper
  ([PMID:1534777](https://pubmed.ncbi.nlm.nih.gov/1534777/)) was consulted, not
  its full text.
- AOP 14's bridge into *Increased, Disease susceptibility* (KE323). Note this is
  not the same gap as KER570, whose empty evidence blocks are recorded above:
  KE323 has **no incoming relationship at all**, so there is no KER there to
  evidence.
