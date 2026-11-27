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

## How the entries record the gene

Both entries type ABCD4
<span class="result" data-compare="names" data-code="g.disorders('unknown', 'germline')">Inborn Disorder of Cobalamin Metabolism and Transport; and Methylmalonic Acidemia With Homocystinuria, Type cblJ<span class="method"></span></span>
as unknown, with a germline origin. The typing follows ClinGen, which rates the
gene <span class="result" data-code="g.clingen('Methylmalonic Acidemia With Homocystinuria, Type cblJ')">moderate<span class="method"></span></span>
for cblJ, below the Definitive or Strong tier that causative requires; the
grouping entry carries the same tier on its cblJ subtype
(<span class="result" data-code="g.clingen('Inborn Disorder of Cobalamin Metabolism and Transport')">moderate<span class="method"></span></span>).

In the cblJ entry ABCD4 sits on
<span class="result" data-code="len(g.nodes('Methylmalonic Acidemia With Homocystinuria, Type cblJ'))">2<span class="method"></span></span>
nodes, starting with
<span class="result" data-code="g.node('Methylmalonic Acidemia With Homocystinuria, Type cblJ', 'ABCD4 Variants Disabling the Lysosomal Cobalamin Exporter')">ABCD4 Variants Disabling the Lysosomal Cobalamin Exporter<span class="method"></span></span>,
which records a
<span class="result" data-code="g.functional_impact('Methylmalonic Acidemia With Homocystinuria, Type cblJ')">loss of function<span class="method"></span></span>
and marks the transporter activity as decreased, and continuing to
<span class="result" data-code="g.node('Methylmalonic Acidemia With Homocystinuria, Type cblJ', 'Failure of the ABCD4-LMBD1 Complex at the Lysosomal Membrane')">Failure of the ABCD4-LMBD1 Complex at the Lysosomal Membrane<span class="method"></span></span>.
The grouping entry places it on
<span class="result" data-code="g.node('Inborn Disorder of Cobalamin Metabolism and Transport', 'Defective cobalamin absorption, transport, and cellular uptake')">Defective cobalamin absorption, transport, and cellular uptake<span class="method"></span></span>.
In every case the export activity is ABCD4's: reconstituted in liposomes,
ABCD4 moves cobalamin out in an ATPase-dependent way, while LMBD1 has no
transport activity and is needed only to bring ABCD4 to the lysosome.

## Agreement between the layers

The KB mechanism and the gene review share
<span class="result" data-compare="names" data-code="g.shared_processes()">cobalamin transport<span class="method"></span></span>
by exact GO identifier, and the nodes' decreased activity is the review's core
transporter function.
