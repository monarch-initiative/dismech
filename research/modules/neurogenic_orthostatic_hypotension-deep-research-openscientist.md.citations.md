# Citations for Research Query

**Query:** # Mechanism Module Research Template

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

**Provider:** openscientist
**Generated:** 2026-11-05T11:37:11.855727

1. PMID:28702747
2. PMID:26373628
3. PMID:32979782
4. PMID:26092297
5. PMID:31733702
6. PMID:27061071
7. PMID:30571543
8. PMID:12707437
9. PMID:38216420
10. PMID:16404729
11. PMID:19155193
12. PMID:40900869
13. PMID:18951069
14. PMID:37164280
15. PMID:31822578
16. PMID:27778639
17. PMID:29343526
18. PMID:36647224
19. PMID:39294522
20. PMID:16476804
21. PMID:8089252
22. PMID:11927799
23. PMID:9890307
24. PMID:34634681
25. PMID:19047577
26. PMID:27148966
27. PMID:17531968
28. PMID:25081417
29. PMID:23934851
30. PMID:41533304