---
hgnc_id: hgnc:406
symbol: ALDH4A1
status: DRAFT
---

# ALDH4A1 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:406")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ALDH4A1<span class="method"></span></span>**
(<span class="result" data-code="g.name()">aldehyde dehydrogenase 4 family member A1<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry.

## Normal function

ai-gene-review gives ALDH4A1's core molecular function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">L-glutamate gamma-semialdehyde dehydrogenase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">L-proline catabolic process; and trans-4-hydroxy-L-proline catabolic process<span class="method"></span></span>
in the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">mitochondrial matrix<span class="method"></span></span>.

## Causative record

One entry types ALDH4A1 as causative:
<span class="result" data-compare="names" data-code="g.disorders('causative')">Hyperprolinemia Type 2<span class="method"></span></span>,
and it records the variants as
<span class="result" data-code="g.variant_origin('Hyperprolinemia Type 2')">germline<span class="method"></span></span>.
ClinGen rates the gene
<span class="result" data-code="g.clingen('Hyperprolinemia Type 2')">definitive<span class="method"></span></span>
for this disease. The gene sits on the node
<span class="result" data-code="g.node('Hyperprolinemia Type 2', 'ALDH4A1 P5C Dehydrogenase Deficiency')">ALDH4A1 P5C Dehydrogenase Deficiency<span class="method"></span></span>.

## Where the layers agree

ClinGen classifies ALDH4A1 for
<span class="result" data-code="g.clingen_diseases()">1<span class="method"></span></span>
disease, and no dismech entry matched to it leaves the gene untyped
(<span class="result" data-code="len(g.clingen_but_untyped())">0<span class="method"></span></span>).
The KB's ALDH4A1 node and ai-gene-review share
<span class="result" data-compare="names" data-code="g.shared_processes()">L-proline catabolic process<span class="method"></span></span>
by exact identifier; the hydroxyproline catabolic process that ai-gene-review
also assigns to the enzyme is not among them.
