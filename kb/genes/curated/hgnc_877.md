---
hgnc_id: hgnc:877
symbol: ALDH7A1
status: DRAFT
---

# ALDH7A1 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:877")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ALDH7A1<span class="method"></span></span>**
(<span class="result" data-code="g.name()">aldehyde dehydrogenase 7 family member A1<span class="method"></span></span>), also called
antiquitin, is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span> disorder entry,
<span class="result" data-compare="names" data-code="g.disorders()">Pyridoxine-Dependent Epilepsy<span class="method"></span></span>.

## Normal function

ai-gene-review gives ALDH7A1's core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">L-aminoadipate-semialdehyde dehydrogenase [NAD(P)+] activity; and aldehyde dehydrogenase (NAD+) activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">L-lysine catabolic process; aldehyde metabolic process; and negative regulation of ferroptosis<span class="method"></span></span>.

## Causative record

Pyridoxine-Dependent Epilepsy types ALDH7A1 as
<span class="result" data-code="g.relationship('Pyridoxine-Dependent Epilepsy')">causative<span class="method"></span></span>, with a
<span class="result" data-code="g.variant_origin('Pyridoxine-Dependent Epilepsy')">germline<span class="method"></span></span> variant origin. The gene sits on the
node <span class="result" data-code="g.node('Pyridoxine-Dependent Epilepsy', 'Antiquitin (ALDH7A1) Deficiency')">Antiquitin (ALDH7A1) Deficiency<span class="method"></span></span>.

## Agreement between the layers

The KB mechanism and the ai-gene-review core functions share
<span class="result" data-compare="names" data-code="g.shared_processes()">L-lysine catabolic process<span class="method"></span></span>: loss of the
lysine-degradation step is what lets alpha-aminoadipic semialdehyde and its
cyclic form accumulate and inactivate PLP.

ClinGen classifies ALDH7A1 for <span class="result" data-code="g.clingen_diseases()">1<span class="method"></span></span> disease, and the
ClinGen diseases with no matching dismech entry are
<span class="result" data-compare="names" data-code="g.clingen_without_entry()">pyridoxine-dependent epilepsy<span class="method"></span></span>. The entry
is anchored on the narrower MONDO term for the ALDH7A1-caused form, while
ClinGen's assertion uses the broader pyridoxine-dependent epilepsy term, so the
ClinGen tier is not copied onto the entry's genetic record.
