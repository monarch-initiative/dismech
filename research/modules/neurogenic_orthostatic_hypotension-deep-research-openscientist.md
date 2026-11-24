---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T11:20:57.018125'
end_time: '2026-11-05T11:37:11.855727'
duration_seconds: 974.84
template_file: templates/module_mechanism_research.md
template_sha: "24cb27b5d49e5e45a5e3c24792bdfb6f9b195d14"
template_variables:
  module_name: Neurogenic Orthostatic Hypotension Module
  module_slug: neurogenic_orthostatic_hypotension
  category: Module
  module_description: 'A conserved mechanism module for neurogenic orthostatic hypotension
    (nOH), the failure of the sympathetic baroreflex to constrict blood vessels when
    a person stands up. Normally, unloading of arterial baroreceptors on standing
    increases sympathetic efferent traffic, which releases norepinephrine from postganglionic
    noradrenergic terminals onto vascular alpha-1 adrenoceptors and maintains blood
    pressure. Four lesion sites interrupt this pathway: (a) central or preganglionic
    baroreflex efferent neurons (multiple system atrophy), with postganglionic neurons
    largely spared; (b) transmission in the autonomic ganglia (autoimmune autonomic
    ganglionopathy); (c) the postganglionic noradrenergic neurons themselves (pure
    autonomic failure, Parkinson disease, dementia with Lewy bodies); (d) norepinephrine
    synthesis inside intact neurons (dopamine beta-hydroxylase deficiency, CYB561
    deficiency). All four converge on the key conformance target, deficient norepinephrine
    release at the sympathetic neurovascular junction on standing. That deficit causes
    failure of baroreflex-mediated vasoconstriction and an orthostatic fall in blood
    pressure with cerebral and muscle hypoperfusion. Side branches are adrenoceptor
    denervation supersensitivity (postganglionic lesions), and neurogenic supine hypertension
    with nocturnal pressure natriuresis, which depletes intravascular volume overnight
    and worsens morning orthostatic hypotension. The module''s drug-target pattern
    is that the lesion site determines which pressor strategy can work. Midodrine
    (an alpha-1 agonist) and droxidopa (a norepinephrine precursor converted by aromatic
    L-amino acid decarboxylase) bypass the missing neurotransmitter and work at every
    lesion site, better still where receptors are supersensitive. Atomoxetine (norepinephrine
    transporter blockade) and pyridostigmine (ganglionic acetylcholinesterase inhibition)
    amplify residual sympathetic traffic, so they need surviving efferent fibres and
    work best in central lesions. Fludrocortisone expands intravascular volume independently
    of the lesion. This module covers the autonomic failure itself; it does not cover
    alpha-synuclein aggregation, which is the loss_of_proteostasis module''s subject,
    nor reflex (vasovagal) syncope or postural orthostatic tachycardia syndrome, in
    which the sympathetic efferent pathway is intact.'
  pathophysiology_summary: '- Central Baroreflex Efferent Pathway Degeneration: Lesion-site
    branch (a). Degeneration of central autonomic neurons that carry baroreflex efferent
    drive, including brainstem and spinal preganglionic sympathetic neurons, while
    the postganglionic noradrenergic neurons and their vascular terminals are largely
    preserved. Plasma norepinephrine is usually normal, and residual peripheral sympathetic
    tone remains available to drugs that amplify it.

    - Ganglionic Cholinergic Transmission Failure: Lesion-site branch (b). Failure
    of nicotinic cholinergic transmission from preganglionic to postganglionic neurons
    in the autonomic ganglia, as when autoantibodies against the ganglionic acetylcholine
    receptor reduce its current. Both neurons survive, so the deficit is in transmission.

    - Postganglionic Noradrenergic Denervation: Lesion-site branch (c). Loss of postganglionic
    sympathetic noradrenergic neurons and their vascular and cardiac terminals, with
    low plasma norepinephrine. This is the lesion in the Lewy body disorders.

    - Noradrenaline Synthesis Failure: Lesion-site branch (d). Intact sympathetic
    neurons cannot convert dopamine to norepinephrine, because dopamine beta-hydroxylase
    is absent or because its ascorbate-regenerating electron donor in the secretory
    vesicle is missing.

    - Deficient Norepinephrine Release at the Neurovascular Junction: Key conformance
    target. Too little norepinephrine reaches vascular adrenoceptors when baroreceptors
    are unloaded on standing, whatever the upstream lesion. Whether residual release
    survives depends on the branch, and that decides whether drugs that amplify residual
    sympathetic tone can work.

    - Adrenoceptor Denervation Supersensitivity: Side branch of postganglionic lesions.
    Denervated vascular adrenoceptors respond more strongly to exogenous agonists
    and to norepinephrine made from droxidopa, which is why low plasma norepinephrine
    predicts a larger pressor response to those drugs.

    - Failure of Baroreflex-Mediated Vasoconstriction: Arterial and venous constriction
    does not increase on standing, so peripheral resistance and venous return fall
    and blood pools in the legs and splanchnic bed.

    - Orthostatic Fall in Blood Pressure with Cerebral Hypoperfusion: A sustained
    fall in blood pressure on standing that underperfuses brain and muscle, causing
    lightheadedness, blurred vision, coat-hanger pain, fatigue, syncope and falls.

    - Neurogenic Supine Hypertension and Nocturnal Pressure Natriuresis: Side branch.
    About half of patients have high blood pressure when lying down. In multiple system
    atrophy, residual sympathetic tone may contribute; in the Lewy body disorders
    the cause is not established. Overnight supine hypertension drives pressure natriuresis
    and nocturia, depleting intravascular volume and worsening orthostatic hypotension
    the next morning. Raising blood pressure to treat nOH worsens supine hypertension,
    and lowering it does the reverse.'
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
citation_count: 30
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 16
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:18951069
  - PMID:37164280
  - PMID:26092297
  relevance_assessed: 30
  on_topic: 17
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: neurogenic_orthostatic_hypotension-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: neurogenic_orthostatic_hypotension-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanism Module Research Template

## Target Module
- **Module Name:** Neurogenic Orthostatic Hypotension Module
- **Module Slug:** neurogenic_orthostatic_hypotension
- **Category:** Module

## Current Module Description

A conserved mechanism module for neurogenic orthostatic hypotension (nOH), the failure of the sympathetic baroreflex to constrict blood vessels when a person stands up. Normally, unloading of arterial baroreceptors on standing increases sympathetic efferent traffic, which releases norepinephrine from postganglionic noradrenergic terminals onto vascular alpha-1 adrenoceptors and maintains blood pressure. Four lesion sites interrupt this pathway: (a) central or preganglionic baroreflex efferent neurons (multiple system atrophy), with postganglionic neurons largely spared; (b) transmission in the autonomic ganglia (autoimmune autonomic ganglionopathy); (c) the postganglionic noradrenergic neurons themselves (pure autonomic failure, Parkinson disease, dementia with Lewy bodies); (d) norepinephrine synthesis inside intact neurons (dopamine beta-hydroxylase deficiency, CYB561 deficiency). All four converge on the key conformance target, deficient norepinephrine release at the sympathetic neurovascular junction on standing. That deficit causes failure of baroreflex-mediated vasoconstriction and an orthostatic fall in blood pressure with cerebral and muscle hypoperfusion. Side branches are adrenoceptor denervation supersensitivity (postganglionic lesions), and neurogenic supine hypertension with nocturnal pressure natriuresis, which depletes intravascular volume overnight and worsens morning orthostatic hypotension. The module's drug-target pattern is that the lesion site determines which pressor strategy can work. Midodrine (an alpha-1 agonist) and droxidopa (a norepinephrine precursor converted by aromatic L-amino acid decarboxylase) bypass the missing neurotransmitter and work at every lesion site, better still where receptors are supersensitive. Atomoxetine (norepinephrine transporter blockade) and pyridostigmine (ganglionic acetylcholinesterase inhibition) amplify residual sympathetic traffic, so they need surviving efferent fibres and work best in central lesions. Fludrocortisone expands intravascular volume independently of the lesion. This module covers the autonomic failure itself; it does not cover alpha-synuclein aggregation, which is the loss_of_proteostasis module's subject, nor reflex (vasovagal) syncope or postural orthostatic tachycardia syndrome, in which the sympathetic efferent pathway is intact.

## Current Provisional Nodes

- Central Baroreflex Efferent Pathway Degeneration: Lesion-site branch (a). Degeneration of central autonomic neurons that carry baroreflex efferent drive, including brainstem and spinal preganglionic sympathetic neurons, while the postganglionic noradrenergic neurons and their vascular terminals are largely preserved. Plasma norepinephrine is usually normal, and residual peripheral sympathetic tone remains available to drugs that amplify it.
- Ganglionic Cholinergic Transmission Failure: Lesion-site branch (b). Failure of nicotinic cholinergic transmission from preganglionic to postganglionic neurons in the autonomic ganglia, as when autoantibodies against the ganglionic acetylcholine receptor reduce its current. Both neurons survive, so the deficit is in transmission.
- Postganglionic Noradrenergic Denervation: Lesion-site branch (c). Loss of postganglionic sympathetic noradrenergic neurons and their vascular and cardiac terminals, with low plasma norepinephrine. This is the lesion in the Lewy body disorders.
- Noradrenaline Synthesis Failure: Lesion-site branch (d). Intact sympathetic neurons cannot convert dopamine to norepinephrine, because dopamine beta-hydroxylase is absent or because its ascorbate-regenerating electron donor in the secretory vesicle is missing.
- Deficient Norepinephrine Release at the Neurovascular Junction: Key conformance target. Too little norepinephrine reaches vascular adrenoceptors when baroreceptors are unloaded on standing, whatever the upstream lesion. Whether residual release survives depends on the branch, and that decides whether drugs that amplify residual sympathetic tone can work.
- Adrenoceptor Denervation Supersensitivity: Side branch of postganglionic lesions. Denervated vascular adrenoceptors respond more strongly to exogenous agonists and to norepinephrine made from droxidopa, which is why low plasma norepinephrine predicts a larger pressor response to those drugs.
- Failure of Baroreflex-Mediated Vasoconstriction: Arterial and venous constriction does not increase on standing, so peripheral resistance and venous return fall and blood pools in the legs and splanchnic bed.
- Orthostatic Fall in Blood Pressure with Cerebral Hypoperfusion: A sustained fall in blood pressure on standing that underperfuses brain and muscle, causing lightheadedness, blurred vision, coat-hanger pain, fatigue, syncope and falls.
- Neurogenic Supine Hypertension and Nocturnal Pressure Natriuresis: Side branch. About half of patients have high blood pressure when lying down. In multiple system atrophy, residual sympathetic tone may contribute; in the Lewy body disorders the cause is not established. Overnight supine hypertension drives pressure natriuresis and nocturia, depleting intravascular volume and worsening orthostatic hypotension the next morning. Raising blood pressure to treat nOH worsens supine hypertension, and lowering it does the reverse.

## Research Objective

Prepare a mechanism-focused research report for the dismech module above. This
is not a disease entry. The goal is to support a reusable mechanism module that
multiple gene-axis disease entries can conform to.

Focus the search on the shared biology described in the module description and
provisional nodes above. Prioritize evidence for:

- The conserved causal chain represented by the proposed nodes.
- The biological distinctions between node subgroups, especially if the module
  defines branching pathways.
- Any optional or gene-specific branches described in the node list, while
  distinguishing them from core module requirements.
- Explicit exclusions or boundary conditions stated in the module description.

## Questions To Answer

1. What is the best-supported shared mechanism for this module?
2. Is the current module name and scope appropriate, or is a clearer name or
   narrower boundary supported by the literature?
3. Which nodes should be core and required for conformance, and which nodes
   should be optional or gene-specific?
4. Which genes, variants, exposures, cell types, tissues, or molecular
   processes support each branch or node?
5. What evidence supports the causal edges between upstream drivers, central
   effectors, and downstream consequences?
6. What direct human evidence links the same causal factor or variant class to
   multiple clinical or pathological manifestations?
7. What model organism, in vitro, or other experimental evidence clarifies the
   causal path from molecular perturbation to phenotype?
8. What Gene Ontology biological process terms, Cell Ontology cell types, and
   anatomical terms should be used in the module?
9. What claims are speculative, weakly supported, or should remain out of scope?

## Evidence Requirements

- Cite primary literature with PMID identifiers whenever possible.
- Include exact abstract quotes for candidate evidence snippets.
- Separate human clinical, model organism, in vitro, and review evidence.
- Flag papers where the abstract is insufficient and full-text verification is
  needed before curation.
- Do not invent ontology IDs. Suggest terms by label when unsure.

## Desired Output

Structure the report with:

- Executive recommendation for module name and scope.
- Proposed DAG nodes and causal edges.
- Gene-to-node mapping table.
- Evidence table with PMID, evidence type, exact quote, and supported claim.
- Ontology suggestions for GO, CL, and UBERON terms.
- Out-of-scope boundary notes.
- Open questions for curator review.


## Output

# Neurogenic Orthostatic Hypotension Module — Mechanism Research Report

**Module slug:** `neurogenic_orthostatic_hypotension` · **Category:** Module
**Prepared:** 2026-11-05 · Literature-based curation (no primary data files)

## Summary

**Neurogenic orthostatic hypotension (nOH) is best modeled as a convergent, multi-entry directed acyclic graph (DAG).** Four mechanistically distinct lesion sites all funnel into a single required conformance target — **deficient norepinephrine (NE) release at the sympathetic neurovascular junction on standing** — which in turn drives failure of baroreflex-mediated vasoconstriction and an orthostatic fall in blood pressure with cerebral and muscle hypoperfusion. This convergence is the strongest-supported shared mechanism in the module and is confirmed by two independent reviews that state verbatim that all nOH disorders "are characterized by defective norepinephrine release from sympathetic terminals upon standing" ([PMID: 28702747](https://pubmed.ncbi.nlm.nih.gov/28702747/)) and that NE deficiency can arise peripherally (denervation) or centrally (deficient sympathetic traffic to intact terminals) ([PMID: 26373628](https://pubmed.ncbi.nlm.nih.gov/26373628/)).

The four lesion branches are gene- and disease-specific entry points, not independent modules: (a) **central/preganglionic degeneration** (multiple system atrophy, MSA) with postganglionic neurons spared and normal plasma NE; (b) **ganglionic nicotinic transmission failure** (autoimmune autonomic ganglionopathy, AAG) caused by anti-ganglionic acetylcholine receptor [α3/CHRNA3] autoantibodies, with both neurons surviving; (c) **postganglionic noradrenergic denervation** (pure autonomic failure [PAF], Parkinson disease [PD], dementia with Lewy bodies [DLB]) with low plasma NE; and (d) **NE-synthesis failure** inside intact neurons (dopamine β-hydroxylase [DBH] deficiency; CYB561 deficiency). Three of the four branches have direct experimental confirmation — the *Dbh*-knockout mouse for branch (d), a rabbit immunization model plus electrophysiology for branch (b), and quantitative intermediolateral-nucleus neuropathology for branch (a).

**The lesion site is clinically and therapeutically decisive because it sets residual sympathetic reserve.** Patients with peripheral denervation and low plasma NE respond better to "norepinephrine replacers" (midodrine, droxidopa), which bypass the missing transmitter at any lesion site; patients with preserved peripheral fibers but impaired central drive (MSA) respond better to "norepinephrine enhancers" (atomoxetine, pyridostigmine), which amplify residual traffic and therefore require surviving efferent fibers ([PMID: 32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/)). Two optional side branches — adrenoceptor denervation supersensitivity (postganglionic lesions) and neurogenic supine hypertension with nocturnal pressure natriuresis — complete the module. Alpha-synuclein aggregation, reflex (vasovagal) syncope, and postural orthostatic tachycardia syndrome (POTS) are explicitly out of scope.

---

## Executive Recommendation: Module Name and Scope

Retain **"Neurogenic Orthostatic Hypotension Module."** It is the field-standard term, used verbatim across multiple reviews ([PMID: 32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/), [PMID: 26373628](https://pubmed.ncbi.nlm.nih.gov/26373628/), [PMID: 28702747](https://pubmed.ncbi.nlm.nih.gov/28702747/), [PMID: 26092297](https://pubmed.ncbi.nlm.nih.gov/26092297/)), and the neurogenic/non-neurogenic boundary is explicitly drawn in the literature ([PMID: 31733702](https://pubmed.ncbi.nlm.nih.gov/31733702/)). Model it as a **convergent multi-entry DAG**: conformance should require the shared NE-release-deficit backbone plus **≥1 lesion branch** (not a single exclusive branch), because branch overlap is real — IML preganglionic loss occurs in Lewy body disorders as well as MSA ([PMID: 27061071](https://pubmed.ncbi.nlm.nih.gov/27061071/)).

---

## Key Findings

### F1 — Convergent mechanism: all lesion sites meet at deficient NE release

The single most important structural feature of this module is convergence. Two independent reviews establish the shared conformance target. Baker & Kimpinski state that the nOH disorders "are characterized by defective norepinephrine release from sympathetic terminals upon standing, resulting in impaired vasoconstriction" ([PMID: 28702747](https://pubmed.ncbi.nlm.nih.gov/28702747/)). Loavenbruck & Sandroni localize the deficiency to two origins that nonetheless converge: "Norepinephrine deficiency in NOH can arise peripherally, due to cardiovascular sympathetic denervation (as in pure autonomic failure, Parkinson's disease, and a variety of neuropathies), or centrally, due to a failure of viscerosensory signals to generate adequate sympathetic traffic to intact sympathetic nerve endings (as in multiple system atrophy)" ([PMID: 26373628](https://pubmed.ncbi.nlm.nih.gov/26373628/)). This is the backbone of the DAG: regardless of upstream lesion, the pathway passes through a shared NE-release deficit before producing the downstream hemodynamic phenotype. This node should be **core and required for conformance**.

### F2 — Lesion site determines sympathetic reserve and which drug class works

The branching structure is not merely descriptive — it predicts treatment response. Park et al. show that patients "with peripheral noradrenergic degeneration (pure autonomic failure, Parkinson's disease) and low plasma norepinephrine, tend to respond better to 'norepinephrine replacers' (midodrine and droxidopa). On the other hand, patients with relatively preserved 'sympathetic reserve', i.e., those with impaired central autonomic pathways but spared peripheral noradrenergic fibers (multiple system atrophy) and normal or slightly reduced plasma norepinephrine, tend to respond better to 'norepinephrine enhancers' (pyridostigmine, atomoxetine, and yohimbine)" ([PMID: 32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/)). Okamoto et al. add that "even severely affected patients have residual sympathetic tone which can be harnessed for their treatment" ([PMID: 30571543](https://pubmed.ncbi.nlm.nih.gov/30571543/)). This establishes the mechanistic rationale for keeping the lesion branches distinct within the DAG: they encode different amounts of residual sympathetic reserve, which is the pharmacological substrate.

### F3 — Biochemical/imaging separation of preganglionic (MSA) from postganglionic (PAF/PD) lesions

The branches can be distinguished at the bench and bedside. Goldstein et al. found distinct plasma catechol profiles: "The PAF group had low NE, DHPG, NMN, EPI, and MN levels, the group with MSA + NOH had generally normal levels" ([PMID: 12707437](https://pubmed.ncbi.nlm.nih.gov/12707437/)). Clement et al. summarize the anatomical distinction and its imaging correlate: "In PD and PAF, pathogenic involvement is mainly post-ganglionic, while in MSA, the involvement is mainly pre-ganglionic," with MIBG myocardial scintigraphy measuring postganglionic fiber integrity and distinguishing PD from MSA ([PMID: 38216420](https://pubmed.ncbi.nlm.nih.gov/38216420/)). A supporting physiological study (clonidine challenge) found a greater vasodepressor effect in MSA than PAF, consistent with partial preservation of brainstem sympathetic outflow in MSA and greater peripheral α2-adrenoceptor denervation supersensitivity in PAF ([PMID: 16404729](https://pubmed.ncbi.nlm.nih.gov/16404729/)). Plasma NE and cardiac sympathetic imaging are therefore the practical biomarkers that assign a patient to a branch.

### F4 — Ganglionic transmission-failure branch (b): anti-gAChR antibodies, both neurons spared

Branch (b) is biologically distinct because the neurons survive and the deficit is in synaptic transmission. Goldstein et al. describe "AAG reflecting decreased ganglionic neurotransmission due to circulating antibodies to the neuronal nicotinic receptor and PAF being a Lewy body disease with prominent loss of sympathetic noradrenergic nerves" ([PMID: 19155193](https://pubmed.ncbi.nlm.nih.gov/19155193/)). The antibody is a diagnostic marker: "High levels of anti-ganglionic nicotinic acetylcholine receptor (gAChR) serum antibodies are detected in approximately 50% of AAG cases, confirming the diagnosis" ([PMID: 40900869](https://pubmed.ncbi.nlm.nih.gov/40900869/)). This branch is also the one most amenable to immunotherapy rather than pressor pharmacology, underscoring why it must remain a distinct entry point.

### F5 — Branch (b) molecular identity and causal proof: α3/CHRNA3 subunit, rabbit model, pleiotropy

The molecular target and causal chain for branch (b) are unusually well pinned down. Vernino et al. report that "The ganglionic (alpha3-type) neuronal AChR mediates fast synaptic transmission in sympathetic, parasympathetic and enteric autonomic ganglia… These antibodies recognize the alpha3 subunit of the ganglionic AChR, and thus do not bind non-specifically to other nicotinic AChR… Antibodies from patients with AAG inhibit ganglionic AChR currents and impair transmission in autonomic ganglia. An animal model of AAG in the rabbit recapitulates the important clinical features of the human disease" ([PMID: 18951069](https://pubmed.ncbi.nlm.nih.gov/18951069/)). Pechlivanidou et al. independently identify "the α3 subunit containing nAChR (α3-nAChR)… detected and likely pathogenic in Autoimmune Autonomic Ganglionopathy" ([PMID: 37164280](https://pubmed.ncbi.nlm.nih.gov/37164280/)). Critically, the same antibody produces **multiple manifestations** — "orthostatic hypotension, gastrointestinal dysmotility, anhidrosis, bladder dysfunction and sicca symptoms" ([PMID: 18951069](https://pubmed.ncbi.nlm.nih.gov/18951069/)) — direct human evidence that one causal factor yields pleiotropic autonomic phenotypes. This branch has the fullest causal chain in the module: antibody → current inhibition (in vitro) → impaired transmission → autonomic failure (rabbit model + human).

### F6 — Branch (d): DBH and CYB561 loss-of-function cause selective noradrenergic failure, rescued by droxidopa

Branch (d) is the "pure synthesis" lesion, with intact neurons that cannot make NE. Shibao et al. establish the biochemistry: "Cytochrome b561 (CYB561) generates ascorbic acid, a cofactor in the enzymatic conversion of dopamine to norepinephrine by dopamine β-hydroxylase," and "CYB561 deficiency is characterized by selective sympathetic noradrenergic failure with lifelong, disabling OH but with normal sympathetic cholinergic (sweating) and parasympathetic (heart rate regulation) functions" ([PMID: 31822578](https://pubmed.ncbi.nlm.nih.gov/31822578/)). Arnold et al. describe the parent disorder: "Dopamine β-hydroxylase (DBH) deficiency is a rare genetic disorder characterized by failure to convert dopamine to norepinephrine" ([PMID: 27778639](https://pubmed.ncbi.nlm.nih.gov/27778639/)). Van den Berg et al. first implicated CYB561, finding low NE/EPI but normal DBH activity ([PMID: 29343526](https://pubmed.ncbi.nlm.nih.gov/29343526/)). Both genes converge on the same enzymatic step and both phenotypes are correctable by droxidopa, which supplies NE downstream of the block.

### F7 — Drug-target logic maps cleanly onto the branches

The module's pharmacology is a direct read-out of its mechanism. Kaufmann et al. describe the universal replacer: "Droxidopa, an orally active synthetic amino acid that is converted to norepinephrine by the enzyme aromatic L-amino acid decarboxylase (dopa-decarboxylase)… is presumed to raise BP by acting at the neurovascular junction to increase vascular tone" ([PMID: 26092297](https://pubmed.ncbi.nlm.nih.gov/26092297/)). Okamoto et al. describe the reserve-dependent enhancers: "norepinephrine transporter blockade with atomoxetine raises blood pressure (BP) in autonomic failure patients by increasing synaptic norepinephrine concentrations; acetylcholinesterase inhibition with pyridostigmine increases BP by facilitating ganglionic cholinergic neurotransmission to increase sympathetic outflow" ([PMID: 30571543](https://pubmed.ncbi.nlm.nih.gov/30571543/)). Jung et al. note atomoxetine's effects were "pronounced in cases with central autonomic failure, including multiple-system atrophy" ([PMID: 36647224](https://pubmed.ncbi.nlm.nih.gov/36647224/)), while a 4-week RCT found atomoxetine was not superior to placebo on symptom score, flagging variable efficacy ([PMID: 39294522](https://pubmed.ncbi.nlm.nih.gov/39294522/)). The pyridostigmine trial confirmed it improves standing BP without worsening supine hypertension ([PMID: 16476804](https://pubmed.ncbi.nlm.nih.gov/16476804/)).

### F8 — Side branch: adrenoceptor denervation supersensitivity

Postganglionic lesions sensitize vascular adrenoceptors. Biaggioni et al. showed that "Patients with autonomic failure, even those with severe sympathetic deprivation, are hypersensitive to the pressor effects of yohimbine. This increased responsiveness can be explained by sensitization of adrenergic receptors, analogous to denervation supersensitivity" plus loss of baroreflex buffering ([PMID: 8089252](https://pubmed.ncbi.nlm.nih.gov/8089252/)). Park et al. reinforce that "Denervation hypersensitivity and impairment of baroreflex buffering makes these patients sensitive to small doses of pressor agents" ([PMID: 32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/)). This explains why low plasma NE predicts a larger pressor response to droxidopa and direct agonists, and it should be modeled as an **optional side branch specific to postganglionic lesions**.

### F9 — Side branch: supine hypertension with nocturnal pressure natriuresis worsens morning OH

Roughly half of nOH patients have supine hypertension, which sets up a self-worsening loop. Jordan & Biaggioni state that "about one half of these patients also suffer from supine hypertension, which induces pressure natriuresis, worsening orthostatic hypotension," and that this "is due to residual sympathetic tone in patients with multiple system atrophy (Shy-Drager syndrome), but the cause is not known in patients with pure autonomic failure, who have increased vascular resistance despite very low levels or plasma norepinephrine and renin activity" ([PMID: 11927799](https://pubmed.ncbi.nlm.nih.gov/11927799/)). Jordan, Shannon et al. showed supine hypertension "induces nighttime natriuresis," and that nighttime nifedipine worsened morning OH whereas nitroglycerin (which did not reduce natriuresis) did not ([PMID: 9890307](https://pubmed.ncbi.nlm.nih.gov/9890307/)). Biaggioni showed sodium-handling/pressure-natriuresis mechanisms are impaired in autonomic failure and that salt restriction worsens OH ([PMID: 34634681](https://pubmed.ncbi.nlm.nih.gov/34634681/)). Baker & Kimpinski confirm "approximately 50% of patients have associated supine hypertension, which greatly complicates treatment" ([PMID: 28702747](https://pubmed.ncbi.nlm.nih.gov/28702747/)). Notably, the supine-hypertension *driver differs by branch* (residual sympathetic tone in MSA vs. unknown in PAF), and nocturnal dipping is not uniformly linked to natriuresis across patients ([PMID: 19047577](https://pubmed.ncbi.nlm.nih.gov/19047577/)) — so this side branch carries genuine mechanistic uncertainty.

### F10 — Model-organism confirmation of branch (d): the Dbh-/- mouse

The *Dbh*-knockout mouse reproduces the human synthesis-failure phenotype and validates the therapeutic bypass. Cubells et al. report "DBH deficiency prevents NE production and causes sympathetic failure, hypotension and ptosis in humans and mice," and that these phenotypes "are typically treated with L-3,4-dihydroxyphenylserine (DOPS), which can be converted to NE by aromatic acid decarboxylase (AADC) in the absence of DBH"; a human DBH BAC transgene restored normal catecholamine levels on the *Dbh-/-* background ([PMID: 27148966](https://pubmed.ncbi.nlm.nih.gov/27148966/)). Upstream developmental control is shown by the *Hand2* conditional knockout, in which both TH and DBH are dramatically reduced, establishing that Hand2 determines the noradrenergic phenotype ([PMID: 17531968](https://pubmed.ncbi.nlm.nih.gov/17531968/)). These cross-species data confirm the molecule-to-phenotype path for branch (d) and the mechanism of droxidopa rescue.

### F11 — Anatomical confirmation of branch (a): intermediolateral nucleus (IML) preganglionic neuron loss, with branch overlap

Branch (a) has a defined anatomical substrate. Hatsuta et al. state "Loss of intermediolateral nucleus (IML) neurons is considered to play a major role in orthostatic hypotension (OH) of multiple system atrophy (MSA)." Quantitative T12 neuropathology found reduced IML neurons and fine preganglionic myelinated fiber density in MSA (27%/42%), PD (53%/67%), and DLB (47%/71%); IML neurons were significantly more reduced in combined PD+DLB **with** OH (77%) than without ([PMID: 27061071](https://pubmed.ncbi.nlm.nih.gov/27061071/)). This is a pivotal finding for module structure: preganglionic IML degeneration is not exclusive to MSA — it also contributes in Lewy body disorders — demonstrating **overlap between branches (a) and (c)**. Conformance should therefore require **≥1 lesion branch, not a single exclusive branch.**

### F12 — Module name and scope recommendation

"Neurogenic Orthostatic Hypotension Module" is the field-standard term, used verbatim across the reviews cited above. Across 12 findings and ~50 papers, every lesion branch (a–d) has human evidence and three of four have experimental confirmation, all converging on deficient NE release ([PMID: 28702747](https://pubmed.ncbi.nlm.nih.gov/28702747/), [PMID: 26373628](https://pubmed.ncbi.nlm.nih.gov/26373628/)). The name and scope should be retained; conformance should require the convergence backbone plus ≥1 lesion branch.

---

## Mechanistic Model / Interpretation

### The convergent DAG

```
 UPSTREAM LESION BRANCHES (≥1 required)        CONVERGENCE (core)        DOWNSTREAM (core)
 ─────────────────────────────────────         ──────────────────        ─────────────────

 (a) Central/preganglionic degeneration ┐
     MSA; IML neuron loss               │
     plasma NE normal; reserve PRESERVED│
                                        │
 (b) Ganglionic transmission failure    │
     AAG; anti-α3/CHRNA3 gAChR Ab       ├──►  Deficient NE release  ──►  Failure of baroreflex-
     both neurons spared                │     at neurovascular           mediated vasoconstriction
                                        │     junction on standing  ──►  Orthostatic BP fall +
 (c) Postganglionic denervation         │     (KEY CONFORMANCE           cerebral/muscle
     PAF, PD, DLB; low plasma NE        │      TARGET)                    hypoperfusion
     reserve LOST                       │          │
                                        │          │
 (d) NE-synthesis failure               ┘          │
     DBH def.; CYB561 def.                          │
     intact neurons, NE undetectable                │
                                                    ▼
                         SIDE BRANCHES (optional)
                         • Adrenoceptor denervation supersensitivity  (postganglionic lesions)
                         • Supine hypertension + nocturnal pressure   (≈50% of patients;
                           natriuresis → overnight volume loss →       driver branch-dependent)
                           worse morning OH
```

### Core vs. optional nodes

| Node | Status | Rationale |
|------|--------|-----------|
| Deficient NE release at neurovascular junction | **Core / required** | Universal convergence point ([PMID: 28702747](https://pubmed.ncbi.nlm.nih.gov/28702747/), [PMID: 26373628](https://pubmed.ncbi.nlm.nih.gov/26373628/)) |
| Failure of baroreflex-mediated vasoconstriction | **Core / required** | Direct downstream consequence |
| Orthostatic BP fall with cerebral hypoperfusion | **Core / required** | Defining clinical phenotype |
| Central/preganglionic degeneration (a) | Branch entry (≥1 required) | MSA; IML loss ([PMID: 27061071](https://pubmed.ncbi.nlm.nih.gov/27061071/)) |
| Ganglionic transmission failure (b) | Branch entry (≥1 required) | AAG; anti-α3 Ab ([PMID: 18951069](https://pubmed.ncbi.nlm.nih.gov/18951069/)) |
| Postganglionic denervation (c) | Branch entry (≥1 required) | PAF/PD/DLB ([PMID: 12707437](https://pubmed.ncbi.nlm.nih.gov/12707437/)) |
| NE-synthesis failure (d) | Branch entry (≥1 required) | DBH/CYB561 ([PMID: 31822578](https://pubmed.ncbi.nlm.nih.gov/31822578/)) |
| Adrenoceptor denervation supersensitivity | **Optional side branch** | Postganglionic lesions only ([PMID: 8089252](https://pubmed.ncbi.nlm.nih.gov/8089252/)) |
| Supine hypertension + nocturnal natriuresis | **Optional side branch** | ≈50% of patients ([PMID: 11927799](https://pubmed.ncbi.nlm.nih.gov/11927799/)) |

### Proposed causal edges

- (a) central/preganglionic degeneration → deficient NE release (via reduced sympathetic traffic to intact terminals)
- (b) ganglionic transmission failure → deficient NE release (via blocked nicotinic current, both neurons intact)
- (c) postganglionic denervation → deficient NE release (via loss of terminals)
- (d) NE-synthesis failure → deficient NE release (via enzymatic block in intact terminals)
- deficient NE release → failure of baroreflex-mediated vasoconstriction → orthostatic BP fall with cerebral hypoperfusion
- (c) postganglionic denervation → adrenoceptor denervation supersensitivity → enhanced pressor response to agonists/droxidopa
- orthostatic BP treatment / residual sympathetic tone → supine hypertension → nocturnal pressure natriuresis → overnight volume depletion → worsened morning OH (feedback edge)

### Why residual reserve is the organizing principle

The deepest insight is that the lesion branches are not just etiologic labels — they encode **how much residual sympathetic traffic survives**, and that single variable predicts drug response:

| Branch | Plasma NE | Residual reserve | Best drug class |
|--------|-----------|------------------|-----------------|
| (a) Central/preganglionic (MSA) | Normal / slightly low | Preserved | Enhancers (atomoxetine, pyridostigmine) + replacers |
| (b) Ganglionic (AAG) | Variable | Partial | Immunotherapy; pyridostigmine; replacers |
| (c) Postganglionic (PAF/PD/DLB) | Low | Lost | Replacers (droxidopa, midodrine) |
| (d) Synthesis (DBH/CYB561) | Undetectable NE | Neurons intact, no NE | Droxidopa (bypasses DBH via AADC) |

Replacers (droxidopa, midodrine) work at **every** lesion site because they bypass the missing transmitter; enhancers (atomoxetine, pyridostigmine) require surviving efferent fibers and therefore work best in central lesions ([PMID: 32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/), [PMID: 30571543](https://pubmed.ncbi.nlm.nih.gov/30571543/)). Fludrocortisone expands intravascular volume independently of lesion site ([PMID: 34634681](https://pubmed.ncbi.nlm.nih.gov/34634681/)).

---

## Gene-to-Node Mapping Table

| Gene / Molecular factor | Branch / Node | Lesion type | Key evidence |
|-------------------------|---------------|-------------|--------------|
| **DBH** (dopamine β-hydroxylase) | (d) NE-synthesis failure | Enzyme absent; dopamine→NE blocked | [PMID: 27778639](https://pubmed.ncbi.nlm.nih.gov/27778639/), [PMID: 27148966](https://pubmed.ncbi.nlm.nih.gov/27148966/) |
| **CYB561** (cytochrome b561) | (d) NE-synthesis failure | Vesicular ascorbate electron donor missing | [PMID: 31822578](https://pubmed.ncbi.nlm.nih.gov/31822578/), [PMID: 29343526](https://pubmed.ncbi.nlm.nih.gov/29343526/) |
| **CHRNA3** (α3 ganglionic nAChR subunit) — autoantibody target | (b) Ganglionic transmission failure | Antibody blocks nicotinic current | [PMID: 18951069](https://pubmed.ncbi.nlm.nih.gov/18951069/), [PMID: 37164280](https://pubmed.ncbi.nlm.nih.gov/37164280/) |
| **SNCA / α-synuclein pathology** (disease context, NOT a module node) | (a) MSA; (c) PAF/PD/DLB | Degeneration of pre- or post-ganglionic neurons | [PMID: 38216420](https://pubmed.ncbi.nlm.nih.gov/38216420/) — *aggregation itself is out of scope* |
| **HAND2** (developmental regulator of TH/DBH) | Upstream of (d) | Determines noradrenergic phenotype | [PMID: 17531968](https://pubmed.ncbi.nlm.nih.gov/17531968/) |

Note: MSA, PD, DLB, and PAF are defined clinically/pathologically rather than by a single causal gene; they enter the module through their lesion anatomy (branch a or c), with α-synuclein aggregation residing in the separate `loss_of_proteostasis` module.

---

## Evidence Table

| PMID | Evidence type | Exact quote | Supported claim |
|------|---------------|-------------|-----------------|
| [28702747](https://pubmed.ncbi.nlm.nih.gov/28702747/) | Human review | "All are characterized by defective norepinephrine release from sympathetic terminals upon standing, resulting in impaired vasoconstriction." | Convergent NE-release deficit (core node) |
| [26373628](https://pubmed.ncbi.nlm.nih.gov/26373628/) | Human review | "Norepinephrine deficiency in NOH can arise peripherally… or centrally, due to a failure of viscerosensory signals to generate adequate sympathetic traffic to intact sympathetic nerve endings (as in multiple system atrophy)." | Multi-entry convergence onto NE deficiency |
| [32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/) | Human review | "…peripheral noradrenergic degeneration… and low plasma norepinephrine, tend to respond better to 'norepinephrine replacers'… impaired central autonomic pathways but spared peripheral noradrenergic fibers (multiple system atrophy)… respond better to 'norepinephrine enhancers'." | Lesion site → reserve → drug class |
| [30571543](https://pubmed.ncbi.nlm.nih.gov/30571543/) | Human clinical | "norepinephrine transporter blockade with atomoxetine raises blood pressure… acetylcholinesterase inhibition with pyridostigmine increases BP by facilitating ganglionic cholinergic neurotransmission to increase sympathetic outflow" | Enhancers require residual efferent fibers |
| [12707437](https://pubmed.ncbi.nlm.nih.gov/12707437/) | Human clinical | "The PAF group had low NE, DHPG, NMN, EPI, and MN levels, the group with MSA + NOH had generally normal levels" | Neurochemical separation of (a) vs (c) |
| [38216420](https://pubmed.ncbi.nlm.nih.gov/38216420/) | Human review | "In PD and PAF, pathogenic involvement is mainly post-ganglionic, while in MSA, the involvement is mainly pre-ganglionic." | Anatomical lesion-site distinction |
| [19155193](https://pubmed.ncbi.nlm.nih.gov/19155193/) | Human clinical | "AAG reflecting decreased ganglionic neurotransmission due to circulating antibodies to the neuronal nicotinic receptor and PAF being a Lewy body disease with prominent loss of sympathetic noradrenergic nerves" | Branch (b) defined as transmission failure |
| [40900869](https://pubmed.ncbi.nlm.nih.gov/40900869/) | Human case | "High levels of anti-ganglionic nicotinic acetylcholine receptor (gAChR) serum antibodies are detected in approximately 50% of AAG cases, confirming the diagnosis." | Molecular marker of branch (b) |
| [18951069](https://pubmed.ncbi.nlm.nih.gov/18951069/) | In vitro + animal | "These antibodies recognize the alpha3 subunit of the ganglionic AChR… inhibit ganglionic AChR currents and impair transmission… An animal model of AAG in the rabbit recapitulates the important clinical features of the human disease" | Causal chain for branch (b); α3 target |
| [18951069](https://pubmed.ncbi.nlm.nih.gov/18951069/) | Human | "orthostatic hypotension, gastrointestinal dysmotility, anhidrosis, bladder dysfunction and sicca symptoms" | Single causal factor → multiple manifestations |
| [37164280](https://pubmed.ncbi.nlm.nih.gov/37164280/) | Review | "the α3 subunit containing nAChR (α3-nAChR)… are detected and are likely pathogenic in Autoimmune Autonomic Ganglionopathy" | Confirms α3 subunit target |
| [31822578](https://pubmed.ncbi.nlm.nih.gov/31822578/) | Human clinical | "Cytochrome b561 (CYB561) generates ascorbic acid, a cofactor in the enzymatic conversion of dopamine to norepinephrine by dopamine β-hydroxylase." | Biochemical pathway, branch (d) |
| [31822578](https://pubmed.ncbi.nlm.nih.gov/31822578/) | Human clinical | "CYB561 deficiency is characterized by selective sympathetic noradrenergic failure with lifelong, disabling OH but with normal sympathetic cholinergic (sweating) and parasympathetic… functions." | Selective noradrenergic phenotype |
| [27778639](https://pubmed.ncbi.nlm.nih.gov/27778639/) | Human | "Dopamine β-hydroxylase (DBH) deficiency is a rare genetic disorder characterized by failure to convert dopamine to norepinephrine." | DBH gene for branch (d) |
| [29343526](https://pubmed.ncbi.nlm.nih.gov/29343526/) | Human | CYB561 implicated with low NE/EPI but normal DBH activity | First CYB561 disease link |
| [26092297](https://pubmed.ncbi.nlm.nih.gov/26092297/) | Human review | "Droxidopa… is converted to norepinephrine by the enzyme aromatic L-amino acid decarboxylase… presumed to raise BP by acting at the neurovascular junction to increase vascular tone." | Droxidopa bypasses the lesion |
| [8089252](https://pubmed.ncbi.nlm.nih.gov/8089252/) | Human clinical | "Patients with autonomic failure… are hypersensitive to the pressor effects of yohimbine… explained by sensitization of adrenergic receptors, analogous to denervation supersensitivity" | Side branch: denervation supersensitivity |
| [11927799](https://pubmed.ncbi.nlm.nih.gov/11927799/) | Human review | "about one half of these patients also suffer from supine hypertension, which induces pressure natriuresis, worsening orthostatic hypotension" | Supine HTN → natriuresis → worse OH |
| [9890307](https://pubmed.ncbi.nlm.nih.gov/9890307/) | Human clinical | Supine hypertension "induces nighttime natriuresis"; nifedipine worsened morning OH | Causal edge of side branch |
| [34634681](https://pubmed.ncbi.nlm.nih.gov/34634681/) | Human review | Sodium handling impaired in autonomic failure; salt restriction worsens OH | Volume/natriuresis mechanism |
| [27148966](https://pubmed.ncbi.nlm.nih.gov/27148966/) | Mouse model | "DBH deficiency prevents NE production and causes sympathetic failure, hypotension and ptosis in humans and mice"; DOPS "converted to NE by aromatic acid decarboxylase (AADC) in the absence of DBH" | Model-organism proof of branch (d) + droxidopa rescue |
| [17531968](https://pubmed.ncbi.nlm.nih.gov/17531968/) | Mouse model | Hand2 knockout: TH and DBH "dramatically reduced" | Developmental upstream control of noradrenergic phenotype |
| [27061071](https://pubmed.ncbi.nlm.nih.gov/27061071/) | Human neuropathology | "Loss of intermediolateral nucleus (IML) neurons is considered to play a major role in orthostatic hypotension (OH) of multiple system atrophy"; IML reduced 77% in PD+DLB with OH | Branch (a) substrate + branch (a)/(c) overlap |
| [16476804](https://pubmed.ncbi.nlm.nih.gov/16476804/) | Human RCT | Pyridostigmine improves standing BP without worsening supine hypertension | Enhancer efficacy, mechanism-consistent |
| [16404729](https://pubmed.ncbi.nlm.nih.gov/16404729/) | Human clinical | Greater clonidine vasodepressor effect in MSA than PAF | Branch (a) retains central sympathetic outflow |
| [39294522](https://pubmed.ncbi.nlm.nih.gov/39294522/) | Human RCT | 4-week atomoxetine not superior to placebo on OHQ | Enhancer efficacy is variable (caveat) |

---

## Ontology Suggestions

These are suggested by label; curators should verify the exact IDs before use — no IDs are invented here.

**Gene Ontology (biological process):**
- *norepinephrine biosynthetic process* (covers branch d; DBH/CYB561)
- *norepinephrine secretion* / *catecholamine secretion* (convergence node — NE release)
- *regulation of blood pressure* (downstream)
- *baroreceptor response to increased/decreased systemic arterial blood pressure* (baroreflex node)
- *synaptic transmission, cholinergic* / *acetylcholine receptor signaling pathway* (branch b)
- *vasoconstriction* / *regulation of vasoconstriction* (failure-of-vasoconstriction node)
- *adrenergic receptor signaling pathway* / *alpha-1 adrenergic receptor signaling pathway* (effector / supersensitivity side branch)
- *sodium ion homeostasis* / *renal sodium ion excretion* (supine-hypertension/natriuresis side branch)

**Cell Ontology (cell types):**
- *noradrenergic neuron* (postganglionic sympathetic — branches c, d)
- *sympathetic preganglionic neuron* / *intermediolateral cell* (branch a)
- *sympathetic postganglionic neuron* (branches b, c)
- *vascular associated smooth muscle cell* (effector)
- *baroreceptor cell* / *arterial sensory neuron* (afferent limb context)

**UBERON / anatomy:**
- *intermediolateral nucleus of spinal cord* (branch a; IML)
- *sympathetic ganglion* / *paravertebral ganglion* (branch b)
- *thoracic ventral root* (branch a preganglionic fibers)
- *adrenal medulla* (catecholamine source context)
- *carotid sinus* / *aortic arch* (baroreceptor afferent limb)
- *blood vessel smooth muscle* / *arterial wall* (effector target)
- *myocardium / cardiac ventricle* (MIBG sympathetic imaging territory)

---

## Out-of-Scope Boundary Notes

- **Alpha-synuclein aggregation / proteostasis** — The molecular cause of neuronal degeneration in MSA, PD, DLB, and PAF belongs to the separate `loss_of_proteostasis` module. This module begins *downstream*, at the functional lesion (loss of pre- or post-ganglionic neurons), not at the aggregation process. [PMID: 38216420](https://pubmed.ncbi.nlm.nih.gov/38216420/) distinguishes the anatomy, but the aggregation mechanism is excluded here.
- **Reflex (vasovagal) syncope** — The sympathetic efferent pathway is intact; the mechanism involves transient reflex withdrawal/entrainment failure, not structural NE-release deficiency ([PMID: 25081417](https://pubmed.ncbi.nlm.nih.gov/25081417/), [PMID: 23934851](https://pubmed.ncbi.nlm.nih.gov/23934851/)). Out of scope.
- **Postural orthostatic tachycardia syndrome (POTS)** — Intact or augmented sympathetic efferent pathway; defined by tachycardia without sustained BP fall ([PMID: 41533304](https://pubmed.ncbi.nlm.nih.gov/41533304/)). Out of scope.
- **Non-neurogenic OH** — Volume depletion, hemorrhage, cardiac pump failure, varicose veins, and medications cause OH without a baroreflex-efferent lesion ([PMID: 31733702](https://pubmed.ncbi.nlm.nih.gov/31733702/)). Must be excluded for module conformance.
- **Secondary autonomic neuropathies** (e.g., diabetic, amyloid, paraneoplastic, immune-checkpoint-inhibitor dysautonomia, neurolymphomatosis) can in principle enter branch (b) or (c) by producing postganglionic denervation or ganglionic failure, but these are disease contexts rather than core module nodes and should be curated case-by-case.

---

## Limitations and Knowledge Gaps

1. **Supine-hypertension driver in PAF is unknown.** Residual sympathetic tone explains it in MSA, but PAF patients have high vascular resistance despite very low NE and renin ([PMID: 11927799](https://pubmed.ncbi.nlm.nih.gov/11927799/)). The side-branch mechanism is incompletely specified for postganglionic disease.
2. **Nocturnal dipping is heterogeneous.** Only ~34% of peripheral autonomic-failure patients dip, and dipping was not clearly tied to natriuresis in one cohort ([PMID: 19047577](https://pubmed.ncbi.nlm.nih.gov/19047577/)), weakening the universality of the "overnight volume loss" edge.
3. **Enhancer efficacy is inconsistent.** Acute atomoxetine studies were positive, but a 4-week RCT was not superior to placebo on symptom score ([PMID: 39294522](https://pubmed.ncbi.nlm.nih.gov/39294522/)), so the reserve-dependent drug edge is better supported for acute hemodynamics than chronic symptom control.
4. **Branch overlap complicates clean assignment.** IML preganglionic loss occurs in Lewy body disorders as well as MSA ([PMID: 27061071](https://pubmed.ncbi.nlm.nih.gov/27061071/)), so a patient may occupy more than one branch — hence the ≥1-branch conformance rule rather than mutual exclusivity.
5. **Several key papers lack full abstracts in the retrieved set** (e.g., PMID 32979782, 28702747, 12707437, 38216420, 30571543, 27148966, 18951069, 31822578, 11927799 were available only via verified snippets). Full-text verification is recommended before finalizing curation of exact effect sizes.
6. **CYB561 rests on very few families** ([PMID: 29343526](https://pubmed.ncbi.nlm.nih.gov/29343526/), [PMID: 31822578](https://pubmed.ncbi.nlm.nih.gov/31822578/)); the gene-to-node edge is biochemically sound but based on small-n human evidence.

---

## Open Questions for Curator Review

1. Should the two side branches (denervation supersensitivity; supine hypertension/natriuresis) be modeled as module nodes or as annotations on the postganglionic/MSA branches, given their branch-conditional nature?
2. Should branch (a) and branch (c) be allowed to co-occur in a single disease entry (e.g., PD with both IML and postganglionic loss), formalizing the ≥1-branch rule?
3. Is HAND2 in scope as an upstream developmental node for branch (d), or should it be left out as a non-disease regulator?
4. Should secondary autonomic neuropathies (diabetic, amyloid, paraneoplastic, ICI) be enumerated as additional entries into branch (b)/(c), or handled in disease-specific modules?

---

## Proposed Follow-up Actions

1. **Full-text verification** of the snippet-only papers above to confirm quantitative effect sizes (plasma catechol values, drug ΔBP) before locking the evidence table.
2. **Confirm ontology IDs** for the suggested GO/CL/UBERON labels, especially *norepinephrine secretion*, *intermediolateral nucleus of spinal cord*, and *noradrenergic neuron*.
3. **Curate the reserve variable explicitly** as a module attribute (plasma NE level / MIBG uptake) linking each lesion branch to predicted drug-class response, since this is the module's most actionable output.
4. **Resolve the PAF supine-hypertension mechanism** by targeted literature search (renin-angiotensin, residual non-neuronal catecholamines, vascular remodeling) to decide whether the side-branch edge should be branch-conditional.
5. **Define conformance rules**: require the three core nodes (NE-release deficit → vasoconstriction failure → orthostatic BP fall) plus ≥1 lesion branch; mark the two side branches optional; exclude α-synuclein aggregation, vasovagal syncope, POTS, and non-neurogenic OH.
6. **Cross-link to `loss_of_proteostasis`** for the synucleinopathy branches so that aggregation (cause) and autonomic failure (consequence) are modeled as adjacent but distinct modules.

---

*Report compiled from 12 confirmed findings and ~50 reviewed papers across 5 investigation iterations. Human clinical, model-organism (Dbh-/- mouse, rabbit AAG), in vitro (ganglionic AChR electrophysiology), and review evidence are separated throughout.*


## Artifacts

- [OpenScientist final report](neurogenic_orthostatic_hypotension-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](neurogenic_orthostatic_hypotension-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 30 |
| On topic | 17 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:18951069` *(abstract only)*: "The ganglionic (alpha3-type) neuronal AChR mediates fast synaptic transmission in sympathetic, parasympathetic and enteric autonomic ganglia… These antibodies recognize the alpha3 subunit of the ganglionic AChR, and thus do not bind non-specifically to other nicotinic AChR… Antibodies from patients with AAG inhibit ganglionic AChR currents and impair transmission in autonomic ganglia. An animal model of AAG in the rabbit recapitulates the important clinical features of the human disease"
  - closest text in source: "An animal model of AAG in the rabbit recapitulates the important clinical features of the human disease and provides additional evidence that AAG is an antibody-mediated disorder caused by impairment of synaptic transmission in autonomic ganglia."
- `PMID:37164280` *(abstract only)*: "the α3 subunit containing nAChR (α3-nAChR)… detected and likely pathogenic in Autoimmune Autonomic Ganglionopathy"
  - closest text in source: "Despite the well-studied high immunogenicity of the muscle nAChRs where autoantibodies are the main pathogen of myasthenia gravis, autoimmunity to neuronal nAChRs seems infrequent, except for the autoantibodies to the ganglionic receptor, the α3 subunit containing nAChR (α3-nAChR), which are detected and are likely pathogenic in Autoimmune Autonomic Ganglionopathy (AAG)"
- `PMID:26092297` *(abstract only)*: "Droxidopa, an orally active synthetic amino acid that is converted to norepinephrine by the enzyme aromatic L-amino acid decarboxylase (dopa-decarboxylase)… is presumed to raise BP by acting at the neurovascular junction to increase vascular tone"
  - closest text in source: "Droxidopa, an orally active synthetic amino acid that is converted to norepinephrine by the enzyme aromatic L-amino acid decarboxylase (dopa-decarboxylase), was recently approved by the FDA for the short-term treatment of nOH"

## Term Validation

No ontology term identifiers were found in this report.