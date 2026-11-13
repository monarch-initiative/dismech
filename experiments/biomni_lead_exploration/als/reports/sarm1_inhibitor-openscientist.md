---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T12:57:45.014587'
end_time: '2026-11-11T13:18:04.266854'
duration_seconds: 1219.25
template_file: experiments/biomni_lead_exploration/repurposing_template.md
template_variables:
  disease_name: Amyotrophic Lateral Sclerosis
  drug: a SARM1 inhibitor
  drug_action: inhibiting the NADase activity of SARM1, the executor of programmed
    axon degeneration
  mechanism: distal axon degeneration and denervation of neuromuscular junctions,
    which precedes motor neuron cell death
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 14
  validator_version: 0.5.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: sarm1_inhibitor-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sarm1_inhibitor-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Drug Repurposing Hypothesis Assessment

## The Hypothesis

- **Disease:** Amyotrophic Lateral Sclerosis
- **Drug:** a SARM1 inhibitor
- **Drug's target and action:** inhibiting the NADase activity of SARM1, the executor of programmed axon degeneration
- **Disease mechanism the drug would act on:** distal axon degeneration and denervation of neuromuscular junctions, which precedes motor neuron cell death

The hypothesis is that a SARM1 inhibitor, by inhibiting the NADase activity of SARM1, the executor of programmed axon degeneration, would benefit patients with
Amyotrophic Lateral Sclerosis because it interrupts "distal axon degeneration and denervation of neuromuscular junctions, which precedes motor neuron cell death". Your job is to assess this
hypothesis, not to advocate for it. Evidence against it is as valuable as evidence for it.

Every factual claim MUST cite a primary source by PMID (or DOI, or NCT number for a
trial registration) and include a short verbatim quote from the cited abstract or record.
Do not paraphrase quotes. Do not invent identifiers. Separate established findings from
your own inference, and label which is which.

## Questions

### 1. Is the mechanism active in this disease?

- Evidence that the drug's target or pathway is active, elevated or genetically implicated
  in patients with Amyotrophic Lateral Sclerosis: in affected tissue, in blood, or through human genetics.
- Whether activity is uniform or confined to a subgroup of patients, and how that subgroup
  is identified (a biomarker, a clinical feature).

### 2. Does blocking it help?

- Clinical trials of a SARM1 inhibitor in Amyotrophic Lateral Sclerosis: registration numbers, phase, status and
  reported results, if any exist.
- Trials of other drugs acting on the same target or pathway in Amyotrophic Lateral Sclerosis, with their
  outcomes, including failures.
- Results of a SARM1 inhibitor in related diseases that share the mechanism, and how far those results
  should transfer here.
- Animal or human tissue experiments in which blocking the pathway changed
  Amyotrophic Lateral Sclerosis-like features.

### 3. Reasons it might fail

- Redundant pathways, wrong cell compartment, wrong disease stage, drug not reaching the
  affected tissue, or trial endpoints that cannot detect the effect.
- Safety concerns specific to this patient population.

### 4. Verdict

- One paragraph: how strong is the case, and what single experiment or trial design would
  most efficiently test it?
- List the PMIDs and trial identifiers that carry the most weight, with one line each.


## Output

# Drug Repurposing Hypothesis Assessment: SARM1 Inhibition in Amyotrophic Lateral Sclerosis

**Hypothesis under test:** A SARM1 inhibitor, by blocking the NADase activity of SARM1 (the executor of programmed axon degeneration), would benefit ALS patients by interrupting distal axon degeneration and neuromuscular-junction (NMJ) denervation that precedes motor-neuron death.

**Role:** Assessor, not advocate. Evidence against is weighted equally with evidence for. Every factual claim carries a PMID or trial identifier with a verbatim quote. *Established findings* and *my inference* are labelled throughout.

---

## Summary

The hypothesis is **mechanistically plausible, supported by human genetics and by the most disease-representative animal model, but clinically unproven and shadowed by a recurring structure–function dissociation.** SARM1 is genetically implicated in ALS — rare constitutively-active (gain-of-function) *SARM1* variants are >5-fold enriched in patients versus controls ([PMID: 34991663](https://pubmed.ncbi.nlm.nih.gov/34991663/)) — and the premise that distal axon/NMJ loss precedes motor-neuron death is well established. The pathway substrate is also depleted in the right tissue: NAD+ is reduced in human ALS motor cortex bearing TDP-43 pathology, the proteinopathy found in ~97% of ALS ([PMID: 35277554](https://pubmed.ncbi.nlm.nih.gov/35277554/)).

Critically, the preclinical picture is **mixed, not uniformly negative**. In a **TDP-43 model** — the near-universal ALS proteinopathy — *Sarm1* deletion protected axons, NMJs, motor-neuron cell bodies and cortical spines and improved male survival ([PMID: 31661035](https://pubmed.ncbi.nlm.nih.gov/31661035/)), and the WldS NAD-maintenance gene modestly prolonged survival in SOD1 mice ([PMID: 15837585](https://pubmed.ncbi.nlm.nih.gov/15837585/)). But in **both** positive models the pathological rescue **failed to translate into behavioural/functional benefit**, and in the SOD1 *Sarm1*-knockout and genetic Charcot-Marie-Tooth (CMT) studies there was no disease-progression benefit at all ([PMID: 35863521](https://pubmed.ncbi.nlm.nih.gov/35863521/), [PMID: 40833344](https://pubmed.ncbi.nlm.nih.gov/40833344/)). A dominant ALS denervation route (TDP-43 → STMN2) operates independently of SARM1 ([PMID: 35767949](https://pubmed.ncbi.nlm.nih.gov/35767949/)), and the one completed rigorous same-axis (NAD-support) trial — CNM-Au8 in the Phase 2/3 HEALEY platform — showed no benefit ([PMID: 40067821](https://pubmed.ncbi.nlm.nih.gov/40067821/)).

A SARM1 inhibitor (**NB-4746**, Nura Bio) is now in a recruiting Phase 1b/2 ALS trial ([NCT07369076](https://clinicaltrials.gov/study/NCT07369076)), so the hypothesis will soon be tested directly — but no SARM1-inhibitor efficacy data in ALS exist yet. **Overall: a moderately strong, mechanistically well-grounded hypothesis whose central uncertainty is whether axon/structural protection will translate into functional benefit — most likely to succeed, if at all, in a genetically or biomarker-defined subgroup.**

---

## Key Findings

### Finding 1 — Human genetics implicates SARM1 gain-of-function in a definable ALS subgroup

This is the single strongest piece of evidence that the drug's target is genuinely active in ALS patients, and it is human genetic evidence rather than model-derived inference. Bloom and colleagues functionally assayed all 42 rare *SARM1* alleles found across 8,507 ALS patients and 9,671 controls. Twelve of the 42 alleles showed constitutive NADase activity, and constitutively-active variants were **>5-fold enriched** in patients versus controls: *"There is a > 5-fold enrichment of constitutively active variants among patients compared to controls"* ([PMID: 34991663](https://pubmed.ncbi.nlm.nih.gov/34991663/)). The authors concluded that *"These results implicate rare hypermorphic SARM1 alleles as candidate genetic risk factors for ALS and other neurodegenerative conditions."* An independent cohort replicated enrichment of rare constitutively-active SARM1 variants ([PMID: 34796871](https://pubmed.ncbi.nlm.nih.gov/34796871/)), and a 2026 review summarises: *"SARM1 gain-of-function variants with constitutively active NADase activity are enriched in amyotrophic lateral sclerosis patients"* ([PMID: 42341897](https://pubmed.ncbi.nlm.nih.gov/42341897/)).

*My inference:* because the genetic signal comes from **rare** hypermorphic variants, the great majority of ALS patients are not SARM1 variant carriers. The activity is therefore **not uniform**; the clearest mechanistically-enriched population is genotype-defined (rare SARM1-GOF carriers). There is no established evidence that SARM1 NADase is pathologically overactive in the sporadic majority.

### Finding 2 — A SARM1 inhibitor is in active ALS trials, but no efficacy data exist

The hypothesis is being tested in humans. ClinicalTrials.gov entry **NCT07369076** ("A Phase 1b/2 Study to Evaluate NB-4746 in Participants With Amyotrophic Lateral Sclerosis", sponsor Nura Bio, status RECRUITING, verified via the ClinicalTrials.gov API) evaluates NB-4746 — an oral, brain-penetrant, reversible SARM1 inhibitor — against placebo. Additional industry programs exist (Eli Lilly LY3873862 from the Disarm Therapeutics acquisition; Sironax SIR2501, an allosteric inhibitor with FDA Fast Track in CIPN). SARM1 is now broadly accepted as a tractable axonal target: *"sterile alpha and TIR motif containing 1 (SARM1) has emerged as the first compelling axonal-specific target for therapeutic intervention"* ([PMID: 32107050](https://pubmed.ncbi.nlm.nih.gov/32107050/)). *Established vs. inferred:* the trial registration and drug mechanism are established; no efficacy or outcome data have been reported — a statement of current absence, not a negative result.

### Finding 3 — Key caution: SARM1 loss does not slow disease in mSOD1 ALS, and fails in genetic axonopathies

This is the primary counterweight. In mSOD1 transgenic ALS mice, *Sarm1* knockout modified neurodegeneration biomarkers and spinal-cord circuitry but did **not** change disease progression (Collins et al.; the paper notes *"SARM1 has been identified as a genetic risk variant in sporadic ALS, and the SARM1 protein is a key mediator of axon degeneration,"* while reporting no progression change — [PMID: 35863521](https://pubmed.ncbi.nlm.nih.gov/35863521/)). In three genetic CMT models, a dominant-negative SARM1 that worked in nerve-crush controls gave *"no change in the phenotypes of any of the CMT mouse models examined. The neuropathy-related phenotypes neither worsened nor improved"* ([PMID: 40833344](https://pubmed.ncbi.nlm.nih.gov/40833344/)). By contrast, SARM1 inhibition is robustly protective in acute/toxic degeneration: *"Sarm1 knockout rescued sciatic nerve morphology"* after chemotherapy ([PMID: 41419972](https://pubmed.ncbi.nlm.nih.gov/41419972/)). *Interpretation:* SARM1 inhibition works best where the trigger is an acute, NAD-depleting axonal insult; where degeneration is driven by an ongoing genetic/cell-intrinsic program (CMT; arguably much of ALS), blocking the Wallerian executor downstream may be insufficient.

### Finding 4 — Mechanistic rationale holds, but the trigger may be somatic and SARM1-independent

ALS is topologically a "dying-back" disease — distal axon/NMJ pathology appears first, exactly the compartment a SARM1 inhibitor would protect. Yet Coleman (2022) cautions that *"many of the major initiating events are thought to occur within the soma"* ([PMID: 36207571](https://pubmed.ncbi.nlm.nih.gov/36207571/)). Crucially, TDP-43 dysfunction causes loss of STMN2, and constitutive STMN2 loss alone reproduces the ALS-relevant denervation without the SARM1 pathway: *"Constitutive STMN2 loss results in early-onset sensory and motor neuropathy featuring impaired motor behavior and dramatic distal neuromuscular junction (NMJ) denervation of fast-fatigable motor units, which are selectively vulnerable in ALS, without axon or motoneuron degeneration"* ([PMID: 35767949](https://pubmed.ncbi.nlm.nih.gov/35767949/)). This is a SARM1-independent route to the precise lesion the drug aims to prevent. Separately, NfL is an established axonal-injury biomarker usable as a pharmacodynamic endpoint: *"Neurofilament light chain levels serve as an indicator of neuronal axonal injury"* ([PMID: 39314138](https://pubmed.ncbi.nlm.nih.gov/39314138/)).

### Finding 5 — POSITIVE: Sarm1 deletion rescues structure and improves male survival in a TDP-43 ALS model, but not behaviour

This is the most ALS-relevant positive experiment, because TDP-43 proteinopathy — unlike SOD1 — models the near-universal ALS pathology. In TDP-43^Q331K;YFP-H mice, *Sarm1* deletion *"attenuated motor axon degeneration and neuromuscular junction denervation. Motor neuron cell bodies were also significantly protected"* ([PMID: 31661035](https://pubmed.ncbi.nlm.nih.gov/31661035/)), attenuated loss of layer-V cortical dendritic spines, and increased male viability. The authors conclude *"these results indicate that anti-SARM1 strategies have therapeutic potential in ALS-FTD."* However, the same study reports the pivotal caveat: *"Sarm1 deletion did not attenuate age-related behavioural deficits caused by TDP-43Q331K."* *Interpretation:* this single study encapsulates both the promise and the peril — SARM1 blockade protected not just axons/NMJs but also motor-neuron somata (arguing against pure axon-soma uncoupling in this context), yet the protection was structurally impressive without being behaviourally meaningful.

### Finding 6 — Supportive but modest: WldS modestly prolongs survival and delays NMJ denervation in SOD1 ALS mice

The WldS gene (slow Wallerian degeneration, an NMNAT-mediated NAD-maintenance mechanism functionally parallel to SARM1 inhibition) crossed into SOD1^G93A mice *"modestly prolonged survival and delayed denervation at the neuromuscular junction"* ([PMID: 15837585](https://pubmed.ncbi.nlm.nih.gov/15837585/)). But protection was incomplete: *"SOD/Wld(S) mice showed levels of motor axon loss similar to that seen in SOD1G93A mice."* WldS provides stronger NAD maintenance than *Sarm1* deletion, which may explain why it showed a modest benefit where *Sarm1* knockout in mSOD1 (Finding 3) did not.

### Finding 7 — Tissue-level support: NAD+ is reduced in ALS motor cortex with TDP-43 pathology

HPLC-MS/MS metabolite profiling of human ALS motor cortex with TDP-43 pathology found that *"reduced levels of NAD+ is one of the underlying causes of metabolomic problems,"* and NMN treatment improved diseased corticospinal motor-neuron health ([PMID: 35277554](https://pubmed.ncbi.nlm.nih.gov/35277554/)). *Established vs. inferred:* NAD+ depletion in ALS motor cortex is established; that SARM1 specifically causes it is inferred — the signature is consistent with SARM1 activity but non-specific (mitochondrial failure and reduced NAD synthesis also lower NAD+).

### Finding 8 — Reasons it might fail: axon-soma uncoupling and non-durable protection in chronic CNS disease

Two mechanistic failure modes are documented. First, in optic-nerve-crush, *"Genetic deletion of SARM1 did not... prevent DLK/JNK pathway activation in RGC somas nor did it prevent or delay RGC cell death,"* despite rescuing electrophysiologically active axons ([PMID: 29526794](https://pubmed.ncbi.nlm.nih.gov/29526794/)) — axons saved, neurons still die. Second, in experimental autoimmune encephalomyelitis (chronic CNS inflammation), *Sarm1* knockout *"delayed axonal degeneration early in the course of CNS inflammation, but did not confer long-term protection from axonal degeneration"* ([PMID: 32584865](https://pubmed.ncbi.nlm.nih.gov/32584865/)) — early protection that decays. A 2025 multi-model study again found limited clinically-relevant benefit from *Sarm1* deletion ([PMID: 40798926](https://pubmed.ncbi.nlm.nih.gov/40798926/)). Both failure modes are directly relevant to chronic, soma-involved ALS. (The TDP-43 model in Finding 5 showed soma protection, so axon-soma uncoupling is context-dependent, not universal.)

### Finding 9 — Same-pathway failure: CNM-Au8 showed no benefit in a Phase 2/3 ALS platform trial

The most sobering clinical datapoint. CNM-Au8 (a gold-nanocrystal catalyst that raises NAD+) was tested in the HEALEY ALS Platform Trial (Phase 2/3, randomized, double-blind; n=161 on drug vs pooled placebo). The primary disease rate ratio was 0.97 (95% credible interval 0.783–1.175), posterior probability of DRR<1 only 0.65, and the authors concluded *"No benefit of CNM-Au8 on ALS disease progression was observed at 24 weeks"* ([PMID: 40067821](https://pubmed.ncbi.nlm.nih.gov/40067821/); NCT04297683, NCT04414345). The mechanism is explicitly NAD-axis: *"CNM-Au8 is a suspension of gold nanocrystals that catalyzes the conversion of nicotinamide adenine dinucleotide hydride into NAD+, resulting in an increase of cellular adenosine triphosphate production."* *Important qualifier:* CNM-Au8 raises NAD+ broadly whereas a SARM1 inhibitor prevents NAD+ consumption at the axonal-death step — same broad pathway, mechanistically distinct — so this is a caution, not a direct refutation.

---

## Direct Answers to the Research Questions

### Q1. Is the mechanism active in this disease?

**Yes, in a genetically-defined subgroup, with supportive tissue-level evidence.** Rare constitutively-active *SARM1* variants are >5-fold enriched in ALS patients ([PMID: 34991663](https://pubmed.ncbi.nlm.nih.gov/34991663/); replicated [PMID: 34796871](https://pubmed.ncbi.nlm.nih.gov/34796871/); reviewed [PMID: 42341897](https://pubmed.ncbi.nlm.nih.gov/42341897/)). The affected subgroup is defined by **genotype** (rare SARM1-GOF carriers). Activity is **not uniform** — there is no established evidence of pathological SARM1 overactivity in the sporadic majority. Indirect tissue support comes from NAD+ depletion in ALS motor cortex with TDP-43 pathology ([PMID: 35277554](https://pubmed.ncbi.nlm.nih.gov/35277554/)), though this is non-specific. A downstream axonal readout (NfL) is elevated and trial-ready ([PMID: 39314138](https://pubmed.ncbi.nlm.nih.gov/39314138/)).

### Q2. Does blocking it help?

**No clinical answer yet; preclinical evidence is mixed.** A SARM1 inhibitor (NB-4746) is recruiting in Phase 1b/2 ([NCT07369076](https://clinicaltrials.gov/study/NCT07369076)) with no results; LY3873862 and SIR2501 are additional programs. Same-pathway (NAD-support) drugs have underdelivered: CNM-Au8 showed no benefit in HEALEY ([PMID: 40067821](https://pubmed.ncbi.nlm.nih.gov/40067821/)), and human nicotinamide data are negative. In ALS models, *Sarm1* deletion rescued structure and improved male survival in a TDP-43 model ([PMID: 31661035](https://pubmed.ncbi.nlm.nih.gov/31661035/)) and WldS modestly prolonged SOD1 survival ([PMID: 15837585](https://pubmed.ncbi.nlm.nih.gov/15837585/)) — but neither rescued behaviour, and SOD1 *Sarm1*-KO changed no disease progression ([PMID: 35863521](https://pubmed.ncbi.nlm.nih.gov/35863521/)). Transfer from acute/toxic axonopathy (where SARM1 blockade works well, [PMID: 41419972](https://pubmed.ncbi.nlm.nih.gov/41419972/)) to genetic axonopathy is poor ([PMID: 40833344](https://pubmed.ncbi.nlm.nih.gov/40833344/)).

### Q3. Reasons it might fail

Redundant/parallel pathway (TDP-43→STMN2 denervation independent of SARM1, [PMID: 35767949](https://pubmed.ncbi.nlm.nih.gov/35767949/)); axon-soma uncoupling (axons saved, somata die, [PMID: 29526794](https://pubmed.ncbi.nlm.nih.gov/29526794/)); non-durable protection in chronic CNS disease ([PMID: 32584865](https://pubmed.ncbi.nlm.nih.gov/32584865/)); somatic "dying-forward" initiation ([PMID: 36207571](https://pubmed.ncbi.nlm.nih.gov/36207571/)); endpoint insensitivity (NfL fall need not equal functional benefit — the exact dissociation seen in models); and population-specific safety risk from chronic NAD-homeostasis perturbation in frail, older patients (an open risk, not documented harm).

### Q4. Verdict

**Moderate strength — one of the better-grounded repurposing hypotheses, but with a genuine risk of structural-only benefit.** The target is druggable, genetically implicated, and the "axon-degeneration-first" premise is sound. The strongest support is that *Sarm1* deletion rescues axons, NMJs, motor-neuron bodies and cortical spines — and improves survival — in a TDP-43 model representative of ~97% of ALS ([PMID: 31661035](https://pubmed.ncbi.nlm.nih.gov/31661035/)), corroborated by a modest WldS survival benefit ([PMID: 15837585](https://pubmed.ncbi.nlm.nih.gov/15837585/)). The principal worry is consistent across models: structural protection repeatedly fails to produce functional rescue, and in SOD1/CMT settings there is no progression benefit at all ([PMID: 35863521](https://pubmed.ncbi.nlm.nih.gov/35863521/), [PMID: 40833344](https://pubmed.ncbi.nlm.nih.gov/40833344/)). The most efficient test is the ongoing **NB-4746 Phase 1b/2 (NCT07369076)** run as a **biomarker-enriched, adaptive trial**: enrich/stratify for pathway engagement (rare SARM1-GOF carriers; a CSF/plasma NMN:NAD or cADPR pharmacodynamic marker), use **plasma NfL** as the primary pharmacodynamic endpoint to prove axon protection early, and pre-specify **ALSFRS-R slope/survival** as confirmatory — so the trial can distinguish "protects axons but not function" from true clinical benefit and futility-stop quickly.

**Highest-weight identifiers:**
- **PMID 34991663** — >5-fold enrichment of constitutively-active SARM1 variants in ALS (core human-genetics support).
- **PMID 31661035** — Sarm1 deletion rescues axons/NMJs/motor-neuron bodies and improves survival in a TDP-43 model, but not behaviour (strongest, most ALS-relevant preclinical datum — both support and caveat).
- **NCT07369076** — recruiting Phase 1b/2 of SARM1 inhibitor NB-4746 in ALS (direct clinical test, no results yet).
- **PMID 35863521** — Sarm1 KO does not alter mSOD1 ALS disease progression (pivotal negative; SOD1 ≈ 2% of ALS).
- **PMID 15837585** — WldS modestly prolongs survival/delays NMJ denervation in SOD1 ALS mice (independent modest positive).
- **PMID 40067821** — NAD-support agent CNM-Au8 showed no benefit in a Phase 2/3 ALS platform trial (same-axis clinical failure; not SARM1-specific).
- **PMID 40833344** — SARM1 inhibition fails in genetic CMT models despite acute-injury efficacy (transferability caveat).
- **PMID 35767949** — TDP-43/STMN2 causes NMJ denervation independent of SARM1 (redundant pathway).
- **PMID 36207571** — somatic "dying-forward" initiation in ALS (wrong-compartment risk).
- **PMID 35277554** — NAD+ depletion in human ALS motor cortex (tissue-level pathway support).

---

## Mechanistic Model / Interpretation

The hypothesis sits on a chain in which every link is plausible but several are contested. The drug acts at the "SARM1 NADase activation" node; the strength of the hypothesis depends on **how much of ALS axon/NMJ loss flows through that node** versus bypassing it.

```
  TDP-43 dysfunction / genetic risk (soma)
            |
            v
  [Loss of STMN2] ------------------> distal axon + NMJ pathology
            |            (SARM1-INDEPENDENT route; PMID 35767949)
            v
  NMNAT2 loss / NAD+ precursor fall  -> NAD+ depletion in motor cortex
            |                             (PMID 35277554)
            v
  SARM1 NADase ACTIVATION  <--- gain-of-function variants (PMID 34991663)
            |   (the step the drug blocks)
            v
  Programmed (Wallerian-type) axon self-destruction
            |
            v
  Distal axon degeneration + NMJ denervation
            |
            v
  Motor neuron cell death  <--- can proceed even if axons saved
                                  (PMID 29526794)
```

| Evidence axis | Supports hypothesis | Challenges hypothesis |
|---|---|---|
| Human genetics | GoF SARM1 >5× enriched (34991663) | Variants *rare*; majority of ALS not carriers |
| Human tissue | NAD+ depleted in motor cortex (35277554) | Cause of depletion not proven to be SARM1 |
| TDP-43 model (~97% of ALS) | Structure + soma + male survival rescued (31661035) | No behavioural rescue (31661035) |
| SOD1 model | WldS modest survival benefit (15837585) | Sarm1 KO: no progression change (35863521) |
| Genetic axonopathy | — | SARM1 blockade fails in CMT (40833344, 40798926) |
| Chronic CNS | — | Protection non-durable (32584865); soma uncoupling (29526794) |
| Clinical (same pathway) | — | CNM-Au8 failed (40067821) |
| Clinical (same target) | NB-4746 recruiting (NCT07369076) | No efficacy data yet |

The recurring theme is a **structure–function gap**: the intervention most reliably protects the morphology of axons and NMJs, and sometimes somata, but this has not translated to functional rescue in models or to clinical benefit for the adjacent NAD-raising strategy. Whether this gap reflects insufficient potency/duration, wrong disease stage, parallel SARM1-independent degeneration (STMN2), or a genuine ceiling on what axon protection can achieve when the soma is independently sick, is the central unresolved question.

---

## Evidence Base

| PMID / ID | Role | One-line relevance |
|---|---|---|
| [34991663](https://pubmed.ncbi.nlm.nih.gov/34991663/) | **FOR (strongest)** | Constitutively-active SARM1 variants >5× enriched in ALS patients |
| [34796871](https://pubmed.ncbi.nlm.nih.gov/34796871/) | FOR | Independent cohort: rare constitutively-active SARM1 variants in ALS |
| [42341897](https://pubmed.ncbi.nlm.nih.gov/42341897/) | FOR | Review confirms SARM1 GoF enrichment in ALS |
| [31661035](https://pubmed.ncbi.nlm.nih.gov/31661035/) | **FOR + caveat** | TDP-43 model: Sarm1 deletion rescues structure + male survival, not behaviour |
| [35277554](https://pubmed.ncbi.nlm.nih.gov/35277554/) | FOR | NAD+ depleted in human ALS motor cortex with TDP-43 pathology |
| [15837585](https://pubmed.ncbi.nlm.nih.gov/15837585/) | FOR (modest) | WldS modestly prolongs survival, delays NMJ denervation in SOD1 mice |
| [32107050](https://pubmed.ncbi.nlm.nih.gov/32107050/) | Context | Establishes SARM1 as the first compelling axon-specific drug target |
| [39314138](https://pubmed.ncbi.nlm.nih.gov/39314138/) | Trial tool | NfL as axonal-injury pharmacodynamic biomarker |
| NCT07369076 | Trial (ongoing) | Phase 1b/2 of NB-4746 (SARM1 inhibitor) in ALS, recruiting, no results |
| [35863521](https://pubmed.ncbi.nlm.nih.gov/35863521/) | **AGAINST** | Sarm1 KO changes biomarkers but not progression in mSOD1 ALS |
| [40833344](https://pubmed.ncbi.nlm.nih.gov/40833344/) | AGAINST | SARM1 inhibition fails in three genetic CMT models |
| [40798926](https://pubmed.ncbi.nlm.nih.gov/40798926/) | AGAINST | Sarm1 deletion: no benefit across three neurological-disease models |
| [29526794](https://pubmed.ncbi.nlm.nih.gov/29526794/) | AGAINST | SARM1 deletion saves axons but not RGC cell bodies (uncoupling) |
| [32584865](https://pubmed.ncbi.nlm.nih.gov/32584865/) | AGAINST | Protection non-durable in chronic CNS inflammation |
| [35767949](https://pubmed.ncbi.nlm.nih.gov/35767949/) | AGAINST | STMN2 loss drives ALS-type NMJ denervation SARM1-independently |
| [36207571](https://pubmed.ncbi.nlm.nih.gov/36207571/) | Caveat | Many ALS initiating events are somatic, upstream of axon death |
| [40067821](https://pubmed.ncbi.nlm.nih.gov/40067821/) | AGAINST (clinical) | CNM-Au8 (NAD-axis) showed no benefit in HEALEY platform trial |
| [41419972](https://pubmed.ncbi.nlm.nih.gov/41419972/) | Context | SARM1 loss protects in toxic/chemotherapy axon degeneration (where it works best) |

---

## Limitations and Knowledge Gaps

1. **No efficacy data for any SARM1 inhibitor in ALS.** The entire clinical case is prospective; NB-4746 is only recruiting (NCT07369076). All conclusions about human benefit are extrapolated from genetics, tissue metabolomics, and animal models.
2. **Weak model-to-human translation.** SOD1 models (where Sarm1 KO failed, PMID 35863521) represent ~2% of ALS and lack TDP-43 pathology. The TDP-43 model that supported the hypothesis (PMID 31661035) is more representative but is a single study, and its own behavioural null is a red flag.
3. **The structure–function gap is unexplained.** Whether it reflects potency, timing, parallel pathways, or an intrinsic ceiling is unknown — and this is the variable that determines clinical success.
4. **Incomplete causal attribution of NAD+ depletion.** Reduced cortical NAD+ (PMID 35277554) is consistent with SARM1 activity but not proven SARM1-driven.
5. **Unresolved subgroup definition.** Rare SARM1-GOF carriers are too rare to power a standalone trial; whether a surrogate (high baseline NfL, a plasma NAD-metabolite signature) identifies a SARM1-dependent sporadic subgroup is untested.
6. **Disease-stage uncertainty.** Dying-back biology argues for early intervention, but ALS is diagnosed late, and chronic-disease protection has proven non-durable (PMID 32584865).
7. **Safety in ALS is uncharacterised.** Chronic SARM1/NADase inhibition perturbs NAD homeostasis; long-term CNS safety in an ageing, metabolically stressed ALS population is not established.
8. **Assessment is literature-only** (no primary data analysis); some abstracts were truncated in retrieval.

---

## Proposed Follow-up Experiments / Actions

### 1. The single most efficient clinical test — a biomarker-enriched, NfL-anchored adaptive trial
Run NB-4746 (or equivalent) in ALS with: **primary pharmacodynamic endpoint** = change in plasma NfL at 12–24 weeks (regulatory-accepted axonal readout, PMID 39314138) to prove the drug reaches and acts on the affected axonal compartment; **confirmatory endpoints** = ALSFRS-R slope and survival; **enrichment** for SARM1 gain-of-function carriers (PMID 34991663) and/or high baseline NfL. Pre-specify the carrier subgroup even if an all-comer arm is primary. This converts the central uncertainty (does axon protection translate?) into a two-step question — prove target engagement first, then test clinical benefit — avoiding an under-enriched endpoint-only trial that could fail for the wrong reason (as CNM-Au8 arguably did, PMID 40067821).

### 2. Close the structure–function gap preclinically
Re-run the TDP-43^Q331K Sarm1-deletion paradigm (PMID 31661035) with **pharmacological** SARM1 inhibition at defined disease stages, adding electrophysiology (CMAP, motor-unit number estimation) and detailed motor-behaviour batteries to test whether earlier/more complete blockade converts structural rescue into functional rescue. Test combination with STMN2 restoration to address the SARM1-independent route (PMID 35767949).

### 3. Define the SARM1-dependent sporadic subgroup
Develop and validate a SARM1-activity signature in human biofluids (e.g., cADPR, NMN:NAD ratio) and test whether it correlates with NfL and progression rate and identifies responsive patients beyond rare variant carriers — enabling precision enrichment without relying solely on rare genetics.

### 4. Durability and stage study
In a chronic TDP-43 model, test whether sustained SARM1 inhibition maintains protection long-term or decays as in EAE (PMID 32584865), and whether early vs. late dosing changes the trajectory — to set the clinical dosing window and expectation.

---

## Conclusion

The SARM1-inhibition hypothesis for ALS is **plausible, genetically anchored, and mechanistically coherent**, with a genuine target-active signal in patients (rare gain-of-function enrichment; cortical NAD+ depletion) and a representative-model experiment showing structural and partial survival benefit. It is counterbalanced by a consistent, specific liability — structural protection repeatedly failing to produce functional benefit — reinforced by negative results in SOD1 ALS, genetic axonopathies, and chronic CNS models, and by the clinical failure of the adjacent NAD-raising agent CNM-Au8. The hypothesis is neither confirmed nor refuted; it is now entering its first direct human test (NB-4746, NCT07369076). The most informative next step is a biomarker-enriched, NfL-anchored adaptive trial that proves axonal target engagement before betting on clinical endpoints.


## Artifacts

- [OpenScientist final report](sarm1_inhibitor-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sarm1_inhibitor-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.
