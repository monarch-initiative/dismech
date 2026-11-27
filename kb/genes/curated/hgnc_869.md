---
hgnc_id: hgnc:869
symbol: ATP7A
status: DRAFT
---

# ATP7A across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:869")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ATP7A<span class="method"></span></span>**
(<span class="result" data-code="g.name()">ATPase copper transporting alpha<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry.

## Normal function

ai-gene-review gives ATP7A's core molecular function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">P-type monovalent copper transporter activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">copper ion export; copper ion import; and intracellular copper ion homeostasis<span class="method"></span></span>,
at the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">plasma membrane; and trans-Golgi network membrane<span class="method"></span></span>.
Those two locations are the pump's two jobs: in the trans-Golgi network it
loads copper onto secretory cuproenzymes, and when copper rises it moves
towards the plasma membrane and exports copper across polarized epithelia such
as the intestine and the blood-brain barrier.

## How Menkes Disease records the gene

ATP7A has one entry, which records it
<span class="result" data-code="g.relationship('Menkes Disease')">causative and unknown<span class="method"></span></span>,
with
<span class="result" data-code="g.variant_origin('Menkes Disease')">germline<span class="method"></span></span>
variants. The two types belong to two records. The causative record covers
classical and atypical Menkes disease and occipital horn syndrome; a second
record, scoped to the distal motor neuropathy subtype, is typed unknown
because ClinGen rates that entity below the Definitive or Strong level that
causative requires. ClinGen's classifications
for the entry are
<span class="result" data-code="g.clingen('Menkes Disease')">moderate and definitive<span class="method"></span></span>:
Moderate for X-linked distal spinal muscular atrophy type 3, the subtype's
MONDO term, and Definitive for Menkes disease itself. ClinGen classifies ATP7A
for <span class="result" data-code="g.clingen_diseases()">2<span class="method"></span></span>
diseases, and both are matched to this entry.

The gene sits on one mechanism node,
<span class="result" data-code="g.node('Menkes Disease', 'ATP7A-mediated copper export failure')">ATP7A-mediated copper export failure<span class="method"></span></span>,
which marks the copper transporter activity as decreased. The severity of the
allelic series is read as how much transport survives: truncating variants in
classical Menkes disease, splice and residual-function variants in occipital
horn syndrome, and trafficking-impairing missense variants in the motor
neuropathy.

## Where the layers agree and disagree

The KB and ai-gene-review agree on the molecular function: the node's
decreased activity is the review's core function. They share no process by
exact GO identifier
(<span class="result" data-compare="names" data-code="g.shared_processes()"><span class="method"></span></span>):
the node carries the generic
<span class="result" data-compare="names" data-code="g.mechanism_processes()">copper ion transport<span class="method"></span></span>,
where the review names the export, import and homeostasis processes that term
covers.
