---
hgnc_id: hgnc:68
symbol: ABCD4
status: DRAFT
---

# ABCD4 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:68")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ABCD4<span class="method"></span></span>**
(<span class="result" data-code="g.name()">ATP binding cassette subfamily D member 4<span class="method"></span></span>) is named by
<span class="result" data-code="g.disorder_count()">2<span class="method"></span></span> disorder entries:
<span class="result" data-compare="names" data-code="g.disorders()">Methylmalonic Acidemia With Homocystinuria, Type cblJ; and Inborn Disorder of Cobalamin Metabolism and Transport<span class="method"></span></span>.

## Normal function

ai-gene-review gives ABCD4's core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">ABC-type vitamin B12 transporter activity; and ATP hydrolysis activity<span class="method"></span></span>,
acting in <span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">cobalamin transport; and cobalamin metabolic process<span class="method"></span></span>.
With its escort LMBD1, ABCD4 exports cobalamin from the lysosome to the cytosol.

## Causative record

<span class="result" data-compare="names" data-code="g.disorders('causative')">Methylmalonic Acidemia With Homocystinuria, Type cblJ<span class="method"></span></span> types ABCD4 as causative, with a
<span class="result" data-code="g.variant_origin('Methylmalonic Acidemia With Homocystinuria, Type cblJ')">germline<span class="method"></span></span> variant origin. ABCD4 sits on
<span class="result" data-code="len(g.nodes('Methylmalonic Acidemia With Homocystinuria, Type cblJ'))">2<span class="method"></span></span> of its nodes, including
<span class="result" data-code="g.node('Methylmalonic Acidemia With Homocystinuria, Type cblJ', 'ABCD4 Variants Disabling the Lysosomal Cobalamin Exporter')">ABCD4 Variants Disabling the Lysosomal Cobalamin Exporter<span class="method"></span></span>.
ClinGen rates the relationship <span class="result" data-code="g.clingen('Methylmalonic Acidemia With Homocystinuria, Type cblJ')">moderate<span class="method"></span></span>.

## Agreement between the layers

The KB mechanism and the gene review share
<span class="result" data-compare="names" data-code="g.shared_processes()">cobalamin transport<span class="method"></span></span>.

The grouping-level entry Inborn Disorder of Cobalamin Metabolism and Transport
places ABCD4 on a node
(<span class="result" data-code="g.node('Inborn Disorder of Cobalamin Metabolism and Transport', 'Defective cobalamin absorption, transport, and cellular uptake')">Defective cobalamin absorption, transport, and cellular uptake<span class="method"></span></span>)
but has <span class="result" data-code="g.relationship('Inborn Disorder of Cobalamin Metabolism and Transport')">no genetic record<span class="method"></span></span>
for it; the ClinGen-matched entries that do not type ABCD4 are
<span class="result" data-compare="names" data-code="g.clingen_but_untyped()">Inborn Disorder of Cobalamin Metabolism and Transport<span class="method"></span></span>.
