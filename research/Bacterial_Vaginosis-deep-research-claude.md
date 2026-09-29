---
provider: claude
model: claude-opus-5
cached: false
start_time: '2026-08-25T12:00:00Z'
end_time: '2026-08-25T13:00:00Z'
duration_seconds: 3600
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bacterial Vaginosis
  mondo_id: MONDO:0005316
  category: Infectious/dysbiotic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains:
    - pubmed.ncbi.nlm.nih.gov
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Pathophysiology Research — Bacterial Vaginosis (MONDO:0005316)

Focus: content-completeness sweep for the dismech entry created in PR #9073.
The entry was curated directly from primary literature without a deep-research
provider report, and the PR review (2026-08-20) blocked on the absence of one,
specifically because a completeness sweep is the kind of pass that catches
missing licensed therapies — which it did.

Method: PubMed E-utilities searches (`esearch` + `esummary` + `efetch`) across
eight dimensions, with every PMID, title, journal, year and publication type
read back from the NCBI record rather than recalled. Numeric results quoted
below are from the fetched abstracts.

**Standing caveat.** Everything here is a *lead*. No statement below may be
copied into a YAML `snippet:`. Any PMID used for curation must first be fetched
with `just fetch-reference` and the exact quote verified with
`just count-verified-snippets`.

---

## 1. Treatment landscape — the confirmed gap

The entry as first written curated metronidazole, clindamycin, LACTIN-V and
partner treatment. The sweep found three further agents with randomised data,
two of them FDA-approved. **All three have been added to the entry in this
revision.**

| Agent | Status | Key trial | PMID |
|---|---|---|---|
| Secnidazole 2 g single oral dose | FDA-approved 2017 | Phase 3, placebo-controlled, 189 women, 21 US centres | 28867602 |
| Tinidazole (1 g × 5 d; 2 g × 2 d) | FDA-approved; CDC alternative regimen | Phase 3, placebo-controlled, 235 women, 10 US centres (NCT00229216) | 17666604 |
| Dequalinium chloride 10 mg × 6 d | Widely used in Europe; non-antibiotic antiseptic | Phase 4 non-inferiority vs oral metronidazole, 147 women | 38696172 |

Notes that shaped how these were curated:

- Secnidazole and tinidazole are **nitroimidazole class-mates of metronidazole**,
  so they attach to the same `Polymicrobial Anaerobic Overgrowth` node and *not*
  to the ribosome node that carries clindamycin. Neither was tested against
  metronidazole for superiority; both were placebo-controlled, so no comparative
  efficacy claim is warranted.
- The tinidazole trial's cure rates (36.8% and 27.4% vs 5.1% placebo) look far
  worse than the 70–85% quoted elsewhere in the entry. **This is an endpoint
  artefact, not a drug difference** — Livengood used the strict five-criterion
  FDA definition, and the same paper states efficacy was greater under
  traditional criteria. Curating the number without the caveat would have
  produced a false comparison inside one entry. Both halves are now curated.
- Dequalinium is mechanistically distinct (membrane-active antiseptic, no
  resistance-selection pressure of the nitroimidazole kind), which is the
  trial's stated rationale.

### Still uncurated treatment leads

- **Astodrimer sodium 1% gel** (dendrimer, approved in Europe/Australia, not US).
  Mini-review PMID:35246717 reports BV cure rates of 50–57% and a
  recurrence-prevention result against placebo. A dendrimer that acts by
  physically blocking adhesion would attach to the **biofilm/adhesion** node
  rather than the overgrowth node — i.e. it would be the only agent in the entry
  targeting the arm that metronidazole is explicitly curated as *not* reaching.
  Worth a follow-up pass; the primary trials, not the mini-review, should be the
  cited source.
- **Vaginal microbiome transplantation (VMT).** PMID:31591599 (Nat Med 2019,
  NCT02236429) is an exploratory case series of five women with intractable BV;
  four achieved long-term remission with reconstitution of a
  Lactobacillus-dominated microbiome, some requiring repeat transplant and one a
  donor change. This is a **five-patient uncontrolled series** and should be
  curated, if at all, as an EMERGING hypothesis-linked intervention with the
  sample size in the description — not as an established treatment. A 2025
  engraftment preprint exists (PMID:40909844) and is explicitly a preprint.
- **Boric acid** and **TOL-463** returned no BV-specific randomised evidence in
  this sweep. Do not curate from the searches above.

## 2. Adverse outcomes — where the entry is thin, and one genuine controversy

The entry curates `Premature birth` as `OCCASIONAL` from a single cohort (9/115).
The sweep found the meta-analytic literature, and it contains a live dispute that
is more interesting than the point estimate:

- **PMID:36251068** (2023, 20 articles, 290,397 observations): OR 1.79
  (1.32–2.43), RR 1.44 (1.19–1.73). Concludes BV is "undoubtedly associated" with
  preterm birth and argues for routine screening.
- **PMID:39442804** (2025, 28 studies, 50,466 patients): OR 1.60 (1.36–1.89),
  I²=67%. Concludes the association is **weaker than previously documented**, and
  explicitly offers that as an explanation for why treating BV in pregnancy has
  not reduced preterm birth.
- **PMID:36651636** (2023): individual-participant-data meta-analysis of
  *antibiotic treatment* of BV to prevent preterm delivery.

This is a candidate `mechanistic_hypotheses` / `discussions` item rather than a
frequency band: a robust association whose causal interpretation is undermined by
the failure of the corresponding intervention. The entry's existing
`Ascending Infection and Adverse Pregnancy Outcomes` node is the attachment
point, and the treatment-failure argument is exactly the sort of constraint this
entry already handles well elsewhere (see its retained `REFUTE` items).

Other outcome leads with real effect sizes:

- **PID**: PMID:34396403 (Longitudinal Study of Vaginal Flora, N=2956,
  prospective) — Nugent-BV aHR 1.53 (1.05–2.21), *symptomatic* Amsel-BV aHR 2.15
  (1.23–3.75), vaginal douching aHR 1.47 (1.03–2.09). Note this **cuts against**
  the entry's retained `REFUTE` item (PMID:35086915, no association between a
  Gardnerella-dominated microbiome and subsequent PID). The two are not
  necessarily inconsistent — one measures a taxon, the other measures the
  syndrome — but curating both would materially improve the PID arm, and the
  distinction between them is itself the finding.
- **HIV acquisition**: PMID:18614873 is already curated. Additional:
  PMID:22745608 (female-to-male transmission, prospective African couples),
  PMID:21358808 (IPD meta-analysis of intravaginal practices).
- **Infertility**: PMID:23543384 (Hum Reprod 2013 meta-analysis) — BV more
  prevalent in infertility than antenatal controls (OR 3.32, 1.53–7.20), and more
  prevalent in *tubal* infertility specifically (OR 2.77, 1.62–4.75), but **not
  associated with decreased conception rates** (OR 1.03, 0.79–1.33) though
  associated with preclinical pregnancy loss. The negative conception result is
  the more useful curation target, because it constrains the mechanism.

## 3. Mechanism — the sexual-transmission hypothesis has a named model

The entry curates recurrence as two hypotheses (`biofilm_persistence_relapse`
CANONICAL, `sexual_reinfection` EMERGING). The sweep found that the transmission
account is not only a recurrence hypothesis but a **primary-pathogenesis** model
with an explicit published statement:

- **PMID:31369673** — Muzny et al., "An Updated Conceptual Model on the
  Pathogenesis of Bacterial Vaginosis" (J Infect Dis 2019). States that BV
  epidemiology supports sexual transmission and that the central debate is
  primary pathogen versus sexually transmitted polymicrobial consortium. Its
  update responds to the objection that *G. vaginalis* is found in virginal
  women, by proposing that the genus contains 13 species and that healthy women
  carry non-pathogenic ones while virulent strains cause BV. Also names
  *Prevotella bivia* and *Atopobium vaginae* as model components.
- **PMID:24511102** — the earlier (2014) version of the same conceptual model.
- **PMID:30001418** — phenotypic characterisation of *G. vaginalis* subgroups
  suggesting they differ in virulence potential.

**Why this matters for the entry as written.** The entry currently records that
*P. bivia* does **not** adhere (from PMID:39162399) and treats the consortium as
the pathogenic unit. The Muzny model is a genuinely competing framing — a
virulent-strain model, where identity within Gardnerella is doing the work that
the entry attributes to the community. That is a candidate ALTERNATIVE
`mechanistic_hypotheses` group, and it also bears on the entry's
`HUMAN_MODEL_MISMATCH`, since a strain-resolved model changes what an animal or
organ-chip system would have to reproduce.

## 4. Host genetics — an absent section

The entry has no `genetic:` section. There is real, if modest, literature:

- **PMID:17314118** — IL-1B −511 CC (OR 1.5, 1.03–2.14) and +3954 TT (OR 2.8,
  1.37–5.88) associated with BV in non-pregnant Italian women; the −511/+3954 T-C
  haplotype protective (OR 0.7).
- **PMID:17123692** — TNFA −308G>A and the TNF-α response to altered vaginal flora.
- **PMID:23021866**, **PMID:19200604** — TLR variants and BV / Gardnerella–Atopobium
  carriage.
- **PMID:32723796** — host genetic factors associated with vaginal microbiome
  composition (Kenyan women).

**Recommendation: curate with restraint or not at all.** These are small
single-population candidate-gene association studies of the kind that replicate
poorly, and no GWAS surfaced. If curated, `relationship_type: SUSCEPTIBILITY`
with the population named in the description, and the absence of replication
stated. A `KNOWLEDGE_GAP` recording that BV has no GWAS-scale host-genetic
evidence may be worth more than the individual associations.

## 5. Immune / barrier mechanism — one strong addition

- **PMID:32094253** (Infect Immun 2020) — host **matrix metalloproteinases**
  secreted in response to BV-associated bacteria disrupt endocervical epithelial
  polarisation and increase HIV-1 transmigration through the epithelium; an MMP
  inhibitor reduces the effect, and cervicovaginal fluid with higher BV-associated
  MMP concentrations increases transmigration.

This is a **host-derived** barrier-damage mechanism running in parallel to the
bacterial glycosidase mechanism the entry already curates (sialidase/fucosidase
stripping the glycocalyx). The entry's barrier arm is currently entirely
bacterial-enzyme-driven; this would add the host-protease arm and would sit
naturally upstream of the HIV-susceptibility node. Strongest single mechanistic
addition found by this sweep.

Supporting: PMID:24403560 (species-specific effects of vaginal taxa on innate
immunity and barrier properties), PMID:32515473 (Prevotella species modulate
barrier function in a 3D endometrial epithelial model — relevant to the entry's
`HUMAN_MODEL_MISMATCH`, since it is a human 3D model rather than an animal one),
PMID:18403235 (*Atopobium vaginae* innate immune response in vitro).

## 6. Diagnostics — molecular assays

The entry curates Amsel and Nugent as `definitions`. Molecular assays are absent:
PMID:22535982 (validated semiquantitative multitarget PCR), PMID:20814710 (qPCR
vs Gram stain accuracy), PMID:38061216 (real-time PCR for intermediate Nugent
scores). A molecular definition would be a genuine addition, because the entry
already argues that BV's prevalence range is partly an artefact of diagnostic
method — a third method with its own operating characteristics is the evidence
for that argument.

## 7. Sialidase source — already correctly curated

PMID:39186657 (PNAS 2024, "Prevotella are major contributors of sialidases in the
human vaginal microbiome") is already cited in the entry. The sweep confirms this
is the current state of the art on sialidase provenance and that the entry's
choice to treat sialidase as a consortium property rather than a Gardnerella
property is the correct reading.

## 8. Datasets

No `datasets:` block exists on the entry. This sweep did not run a repository
search; `just discover-datasets Bacterial_Vaginosis` and
`just verify-datasets` are the right tools and were not run here. Flagged as an
open item rather than answered.

---

## Summary of what this sweep changed

**Acted on in this revision:** section 1 (three treatments added), plus the
review's other two blocking findings.

**Recommended follow-ups, in descending value:**

1. Host-MMP barrier-disruption arm (PMID:32094253) — section 5.
2. Preterm-birth association-vs-intervention controversy as a discussion —
   section 2.
3. Muzny virulent-strain conceptual model as an ALTERNATIVE hypothesis —
   section 3.
4. PID prospective cohort alongside the existing REFUTE item — section 2.
5. Astodrimer sodium as a biofilm/adhesion-targeting agent — section 1.
6. Molecular diagnostic definition — section 6.
7. Host genetics, with restraint, or as a knowledge gap — section 4.
8. Dataset discovery — section 8.

These are deliberately **not** all done in this PR. The PR is a review-response
on an entry that is already approved-in-substance; folding eight new arms into it
would make the diff unreviewable and would re-open questions the reviewer has
already settled. They belong in a follow-up pass.

## References surfaced by this sweep

All PMIDs below were returned by PubMed E-utilities during this sweep and their
titles read back from the NCBI record.

| PMID | Section | Title (abbreviated) |
|---|---|---|
| 28867602 | 1 | Phase-3 placebo-controlled single-dose secnidazole 2 g for BV |
| 17666604 | 1 | Effectiveness of two tinidazole regimens in treatment of BV |
| 38696172 | 1 | Dequalinium chloride vs metronidazole for BV: RCT |
| 35246717 | 1 | Astodrimer sodium and bacterial vaginosis: a mini review |
| 31591599 | 1 | Vaginal microbiome transplantation in intractable BV |
| 40909844 | 1 | Donation strain engraftment, VMT (preprint) |
| 36251068 | 2 | Effect of BV on preterm birth: a meta-analysis |
| 39442804 | 2 | Reassessing the association between BV and preterm birth |
| 36651636 | 2 | Antibiotic treatment of BV to prevent preterm delivery: IPD MA |
| 34396403 | 2 | BV and behavioral factors in incident PID (LSVF) |
| 22745608 | 2 | BV and female-to-male HIV-1 transmission |
| 21358808 | 2 | Intravaginal practices, BV and HIV: IPD meta-analysis |
| 23543384 | 2 | Risks associated with BV in infertility patients: meta-analysis |
| 31369673 | 3 | An updated conceptual model on the pathogenesis of BV |
| 24511102 | 3 | Role of G. vaginalis in BV pathogenesis: a conceptual model |
| 30001418 | 3 | Phenotypic characterization of G. vaginalis subgroups |
| 17314118 | 4 | IL-1beta and IL-1ra polymorphisms and BV |
| 17123692 | 4 | TNFA-308G>A and the TNF-alpha response to altered vaginal flora |
| 23021866 | 4 | TLR gene variants and BV among HIV-1 infected adolescents |
| 32723796 | 4 | Host genetic factors and vaginal microbiome composition |
| 32094253 | 5 | MMPs disrupt endocervical epithelium, increasing HIV transmigration |
| 24403560 | 5 | Vaginal bacteria alter innate immunity and barrier properties |
| 32515473 | 5 | Prevotella modulate barrier function in 3D endometrial model |
| 22535982 | 6 | Validated semiquantitative multitarget PCR for BV diagnosis |
