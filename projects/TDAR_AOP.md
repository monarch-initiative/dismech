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
module, an edge, or a schema construct as a result belongs in its own issue, and
whether the AOP-side observations are communicated to the AOP community is a
separate call again.

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

The report is a **lead**, not a source. Its citations have not been put through
`just validate-research-references`, and the verification below was done by hand
against AOP-Wiki and PubMed. The provider bundle also contained iteration
transcripts, container logs and a PDF rendering of the same report; those are
recoverable from the job and are not committed.

**AOP-Wiki snapshot.** All AOP-Wiki figures below are from the `09-03-2026`
export, read through
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
this one.

One statement in the same abstract cuts the other way, toward the AOP's reading,
and is recorded here so the page carries both sides — conclusion (3):

> "The ability to resist infectious agent challenge is dependent upon the degrees
> of immunosuppression and the quantity of infectious agent administered."

That is a dose-dependence claim about immunosuppression and host resistance, and
it is the paper's clearest support for a graded relationship. What it does not
supply is the part the pathway needs: it names neither TDAR nor any single immune
test as the measure of "degrees of immunosuppression", which is what conclusion
(2) explicitly declines to do.

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

`germinal_center_reaction`'s description and notes name five entries as intended
conformers. Three currently declare `conforms_to`:

| Entry | `conforms_to` |
|---|---|
| `Common_Variable_Immunodeficiency` | `germinal_center_reaction#Germinal Center Reaction` |
| `Specific_Antibody_Deficiency` | `germinal_center_reaction#Affinity-Matured Class-Switched B Cell Output` |
| `Autosomal_Agammaglobulinemia` | `germinal_center_reaction#Durable Protective Humoral Immunity` |
| `X-linked_Agammaglobulinemia` | none |
| `Hyper-IgM_Syndrome_Type_2` | none |
| `Selective_IgA_Deficiency` | none |

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
  central causal claim and the network structure; its assay mapping (F004), its
  regulatory-framework section (F011), the AhR/PAC branch (F012, F014) and the
  2026 B6C3F1/N in vivo dataset (F006) have not been checked.
- The Luster 1992 companion paper (*Fundam. Appl. Toxicol.* 18, 200-210), which
  is where the "particularly beneficial" claim for TDAR originates.
- AOP 14's bridge, whose KER570 evidence blocks are empty.
