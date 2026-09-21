# Chlorpromazine as an ALS treatment: hypothesis investigation

Literature investigation, 2026-09-21. Requested as "investigate this as a hypothesis".

Curated artifact: the `hyp_als_phenothiazine_autophagy_repurposing` discussion in
[`kb/disorders/Amyotrophic_Lateral_Sclerosis.yaml`](../../kb/disorders/Amyotrophic_Lateral_Sclerosis.yaml),
`kind: EMERGING_HYPOTHESIS`, with fifteen evidence items and two decisive experiments.

## Verdict

**The hypothesis is mechanistically real and translationally discouraged.** There is a
specific, recent, chlorpromazine-specific molecular result in motor neurons — TPC2
channel agonism driving TFEB-dependent autophagy — and it sits inside a class whose two
closest in vivo precedents in ALS produced *no benefit* and *active harm* respectively.

The decisive question is not whether chlorpromazine induces autophagy in motor neurons.
It does. It is whether a therapeutic window exists between the concentration that engages
TPC2/TFEB and the concentration at which D2 blockade causes rigidity, sedation and
dysphagia — in a population whose leading causes of death are respiratory and bulbar
failure. Nobody has measured that window, and it is a cheap experiment.

Recommendation: **do not add chlorpromazine to `treatments:`**. There is no human ALS
evidence, no registered trial, and the nearest neuroleptic that reached a human ALS trial
subsequently shortened survival in mice. Record it as a hypothesis with its refuting
evidence attached, which is what has been done.

## What the hypothesis actually is

Chlorpromazine (CPZ) is a phenothiazine antipsychotic, marketed since 1952, a D2 receptor
antagonist and a cationic amphiphilic drug. The repurposing proposal is *not* about
dopamine. It is a proteostasis argument: phenothiazines induce neuronal autophagy, ALS is
a proteinopathy in which >97% of cases carry cytoplasmic TDP-43 aggregates, and the ALS
entry already carries `pathophysiology#Impaired Autophagy` as a node.

Three independent lines reach the scaffold, and it matters that they are independent.

### 1. Unbiased screening lands on phenothiazines (PMID:24974230)

Barmada et al. built a neuronal autophagy-inducing pharmacophore by structure-activity
assay and screened it. The top two candidates were **fluphenazine and
methotrimeprazine** — both phenothiazine antipsychotics. Autophagy induction then
"improved TDP43 clearance and localization and enhanced survival in primary murine
neurons and in human stem cell-derived neurons and astrocytes harboring mutant TDP43."

This is the strongest structural argument, because the class was reached by screening
rather than by analogy. Note the paper's own framing: "phenothiazine derivatives,
including FPZ, have been used for decades to treat patients with psychoses" — the
tolerability record is the attraction.

### 2. The class clears TDP-43 aggregates in an ALS model (PMID:34571136)

Thioridazine, another phenothiazine, "cleared TDP-43 aggregates and recovered TDP-43
functionality" and significantly improved the locomotive defect in a Drosophila ALS
model.

**But read the mechanism sentence.** In this system "the degradation of the aggregates
occurs independent of the autophagy pathway beyond autophagosome-lysosome fusion, but
requires a functional proteasome pathway." That is *proteasome*-dependent and
*autophagy*-independent — the opposite of the chlorpromazine result below. The two
strongest class findings do not currently describe one mechanism, so "phenothiazines
work on TDP-43 via autophagy" is not a supported class generalization. This is recorded
as a `REFUTE` item in the KB entry, against that specific claim.

### 3. Chlorpromazine itself, in motor neurons, with a named target (PMID:40796055)

Tedeschi et al. (2025) is the only chlorpromazine-specific mechanistic result in a
motor-neuron system, and it is a good one:

- Patch-clamp on enlarged lysosomes in **NSC-34 motor neurons**: CPZ evokes large
  inwardly-rectifying TPC2 currents, blocked by trans-Ned-19 and by siTPC2.
- CPZ raises intracellular Ca²⁺ → TFEB nuclear translocation.
- "TPC2 stimulation by both the drugs boosted autophagy, as revealed by the activation of
  autophagy initiators ULK and AMPK α and modification of LC3-II/p62(SQSTM1) ratio."
- CPZ counteracts L-BMAA (the cyanobacterial ALS/PDC neurotoxin): preserves ATP, limits
  ROS, blocks LDH, cytochrome c and SMAC/DIABLO release.
- Critically, "siTPC2 partially reverted CMI- and CPZ-induced neuroprotection" — a
  knockdown arm distinguishing target-mediated action from the generic lysosomotropism
  every cationic amphiphilic drug shows.

The word to hold onto is **partially**. Some of the protection is not TPC2-attributable
even in the paper that establishes the target.

### 4. A fourth, weaker line: broad-spectrum in vitro neuroprotection (PMID:42061810)

A 2026 repurposing pipeline screened eight CNS drugs against Caᵥ1, Orai1 and P2X7:
"Several compounds demonstrated significant efficacy, with chlorpromazine showing
broad-spectrum activity." SH-SY5Y and HEK293 cells, and the authors themselves frame the
relevance as Parkinson's. Suggestive, not ALS evidence.

### 5. A tool-compound coincidence worth not over-reading (PMID:31148094)

Poly-PR, the most toxic C9orf72 dipeptide repeat, enters cells by clathrin-dependent
endocytosis. Chlorpromazine is the canonical clathrin-mediated endocytosis inhibitor, so
it is tempting to propose it blocks DPR cell-to-cell propagation. But in that paper CPZ
is a *tool compound used to characterize the uptake route*, not a therapeutic proposal.
Reading a mechanistic tool use as a therapeutic lead is a category error, and it is not
carried into the KB entry.

## Why this probably does not translate

### The epidemiological premise is gone

The idea originates with Stommel et al. (PMID:17475413), a *Medical Hypotheses* paper
whose premise is that "the development of amyotrophic lateral sclerosis (ALS) in the
relatively common psychiatric disorder schizophrenia is very rare", observed by the
authors "and a number of other neuromuscular specialists at large ALS centers". That is
an uncontrolled clinical impression, not a measured association.

It points the wrong way. McLaughlin et al. (PMID:28322246, *Nat Commun* 2017) estimate the
ALS–schizophrenia genetic correlation at **14.3%** — positive — and conclude "a modest
increase in comorbidity of ALS and schizophrenia is expected given these findings (odds
ratio 1.08-1.26)". Whatever motivates phenothiazine repurposing in ALS, it should not be
the claim that antipsychotics protect against it.

### The class precedent failed exactly here (PMID:19560462 → PMID:22230045, PMID:21998625)

Methylene blue shares the tricyclic phenothiazine-type core. In 2009 it reduced TDP-43
aggregates by 50% in cells, and the authors concluded "MB and dimebon may be useful for
the treatment of ALS, FTLD-U and other TDP-43 proteinopathies" — phrasing nearly
identical to the present hypothesis.

Three years later: "Despite its established neuroprotective properties, MB failed to
confer protection in both mouse models of ALS" (SOD1-G93A and TDP-43-G348C; no effect on
lifespan, motor function, motor neuron loss, SOD1 aggregation, TDP-43 translocation, or
inflammation). Independently: "In spite of a strong theoretical rationale, MB had no
significant effects on onset or survival in the inbred SOD1 G93A mouse model of ALS."

This is the exact in-vitro-to-in-vivo gap the present hypothesis has to cross, previously
attempted by the closest available chemical relative, and failed.

### The nearest neuroleptic to reach a human ALS trial then harmed mice

This thread is the most informative, because it ran the full length.

Patten et al. (PMID:29202456, 2017) screened in C. elegans, validated in zebrafish, and
"identified a class of neuroleptics that restored motility". Pimozide was most potent,
blocked T-type Ca²⁺ channels, stabilized neuromuscular transmission, and "a short
randomized controlled trial of sporadic ALS subjects demonstrated stabilization of
motility and evidence of target engagement at the neuromuscular junction."

Then Pozzi et al. (PMID:29790082, 2018) dosed it chronically in two ALS mouse models:
"Chronic administration of pimozide exacerbated motor performances in both animal models
and reduced survival in SOD1G93A mice." And, against the proteostatic rationale directly:
"In TDP-43A315T, it decreased the percentage of innervated neuromuscular junctions (NMJs)
and increased the accumulation of insoluble TDP-43." Insoluble TDP-43 went **up**.

As of today, neither registered Phase 2 pimozide ALS trial has posted results:
NCT03272503 (n=100, Phase 2) is `UNKNOWN` status, last updated 2020-05-28, `hasResults:
false`; NCT02463825 (n=25) is `UNKNOWN`, last updated 2016-10-26. No results publication
is indexed in PubMed. The program's definitive answer is, publicly, missing.

### The dose-response changes sign (PMID:14598305)

Turner et al. gave clozapine to SOD1-G93A mice: "Low-dose treatment was associated with
delayed locomotor impairment and death, compared to high-dose clozapine, which
accelerated paralysis and mortality (P < 0.05)." And the mechanism of the harm is named:
"High-dose clozapine, however, produced extrapyramidal symptoms in mice manifest by
hindlimb rigidity, despite reducing spinal cord p75(NTR) levels overall."

Target engagement and motor harm coexisted in the same animals. A single-dose
chlorpromazine mouse study would therefore be uninterpretable whichever way it came out.

### Chlorpromazine may be the wrong phenothiazine (PMID:33663349)

Within the same scaffold: "Compared with the normal blood SOD1 activity, the percent of
O2 production increased with trifluoperazine, while it decreased with the chlorpromazine."
CPZ inhibited SOD1 enzymatic activity; trifluoperazine activated it.

Weight this carefully. SOD1-linked ALS is driven by misfolding gain-of-function, not loss
of dismutase activity, so this is indirect. But if the class is pursued, it is a reason to
prefer a different member, and fluphenazine/methotrimeprazine were the screen's own picks
anyway.

### The adverse-effect profile overlaps the disease trajectory

Antipsychotic-associated oropharyngeal dysphagia is a class effect: "both typical and
atypical antipsychotics can be associated with OD" (PMID:29023321), with swallowing
problems in 21.9–69.5% of antipsychotic-treated patients across the included studies
versus 5–30.5% in comparison groups. Dysphagia in ALS drives aspiration pneumonia and
gastrostomy. Sedation and orthostatic hypotension compound it. These are not independent
risks bolted onto a neutral drug — they act on the same axis the disease is already
failing along.

## What would settle it

Both experiments are recorded in the KB entry with decision criteria.

**1. The window study** (`exp_als_phenothiazine_therapeutic_window_csf_exposure`).
Measure, for CPZ and for the screen-derived fluphenazine and methotrimeprazine, the free
concentration needed in human iPSC-derived motor neurons for TPC2-dependent TFEB
translocation and TDP-43 clearance. Compare against free CSF and spinal-cord
concentrations in mice at doses below the catalepsy/hindlimb-rigidity threshold. Keep a
TPC2-null arm.

*Decision*: a viable window needs the engagement EC50 several-fold below the free CNS
concentration at a non-cataleptic dose. If engagement only happens at motor-toxic
concentrations, abandon the marketed antipsychotics and redirect to TPC2 agonists without
dopamine-receptor affinity — which is the honest read of what the mechanism actually
recommends.

**2. Dose-ranging survival in two models**
(`exp_als_chlorpromazine_dose_ranging_two_model_survival`). Three-plus doses spanning that
window, in both TDP-43-A315T and SOD1-G93A, powered for survival, with prespecified NMJ
innervation, insoluble TDP-43, misfolded SOD1 and spinal-cord LC3-II/p62 endpoints. Two
models and a dose range are both mandatory given the pimozide and clozapine results.

*Decision*: survival extension or preserved NMJ innervation at a dose with confirmed
spinal-cord autophagy induction. Worsened motor performance, shortened survival, or
increased insoluble TDP-43 or misfolded SOD1 at any dose closes it.

The first experiment is cheap and comes first. If the window does not exist, the second is
unnecessary — and given the pimozide result, running the mouse study without the window
measurement would repeat a known mistake.

## The generalizable point

The interesting target here is **TPC2**, not chlorpromazine. Chlorpromazine is how TPC2
was found, and it arrives carrying seventy years of dopaminergic baggage that acts
directly on bulbar and respiratory function. The repurposing appeal — a cheap,
well-characterized, off-patent drug — is real, but the pharmacology that makes it
available is the pharmacology that makes it dangerous in this disease.

If the window study shows engagement only at motor-toxic exposures, the productive move
is not to abandon the mechanism. It is to keep the target and drop the scaffold.

## Sources

All fifteen cited references are cached under `references_cache/` and every quoted snippet
in the KB entry is exact-quote verified (240/240 snippets in the file verified by
`just validate`).

| PMID | Role |
|---|---|
| 40796055 | CPZ → TPC2 → Ca²⁺/TFEB → autophagy in NSC-34 motor neurons; L-BMAA protection |
| 24974230 | Autophagy-inducer screen; top hits fluphenazine and methotrimeprazine; TDP-43 clearance in human neurons |
| 34571136 | Thioridazine clears TDP-43 aggregates in cells and Drosophila — but proteasome-dependent |
| 42061810 | CPZ broad-spectrum in vitro neuroprotection (SH-SY5Y/HEK293, PD-framed) |
| 31148094 | Poly-PR uptake is clathrin-dependent (CPZ used as tool compound) |
| 17475413 | Origin of the neuroleptic-protection hypothesis |
| 28322246 | ALS–schizophrenia genetic correlation is *positive* (14.3%) |
| 29202456 | Neuroleptics stabilize NMJ transmission; short RCT with target engagement |
| 29790082 | Chronic pimozide worsens motor function, shortens SOD1-G93A survival, raises insoluble TDP-43 |
| 14598305 | Clozapine dose-response changes sign; high dose causes hindlimb rigidity |
| 19560462 | Methylene blue clears TDP-43 in cells; "may be useful for the treatment of ALS" |
| 22230045 | Methylene blue fails in SOD1-G93A and TDP-43-G348C mice |
| 21998625 | Methylene blue fails in SOD1-G93A mice (independent) |
| 33663349 | CPZ inhibits SOD1 activity; trifluoperazine activates it |
| 29023321 | Antipsychotic-associated oropharyngeal dysphagia, systematic review |

Trial registry checked 2026-09-21 via the ClinicalTrials.gov v2 API: no ALS study for
chlorpromazine, thioridazine, trifluoperazine or methylene blue; two pimozide Phase 2
studies, both `UNKNOWN` status with no posted results.
