---
hgnc_id: hgnc:321
symbol: AGL
status: DRAFT
---

# AGL across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:321")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">AGL<span class="method"></span></span>**
(<span class="result" data-code="g.name()">amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase<span class="method"></span></span>) is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry, Cori Forbes Disease. AGL is the glycogen debranching enzyme, a single protein with two catalytic activities, and its deficiency is glycogen storage disease III.

## Normal function

ai-gene-review gives AGL's core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">4-alpha-glucanotransferase activity; and amylo-alpha-1,6-glucosidase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">glycogen catabolic process<span class="method"></span></span>,
in the <span class="result" data-compare="names" data-code="g.core_function_terms('locations')">cytosol<span class="method"></span></span>
(<span class="result" data-code="len(g.core_function_terms())">4<span class="method"></span></span> core terms in all).

## The record

Cori Forbes Disease types AGL as
<span class="result" data-code="g.relationship('Cori Forbes Disease')">causative<span class="method"></span></span>, with variant origin
<span class="result" data-code="g.variant_origin('Cori Forbes Disease')">germline<span class="method"></span></span>. ClinGen rates the gene <span class="result" data-code="g.clingen('Cori Forbes Disease')">definitive<span class="method"></span></span> for it. The gene sits on
<span class="result" data-code="g.node('Cori Forbes Disease', 'Glycogen debranching enzyme deficiency')">Glycogen debranching enzyme deficiency<span class="method"></span></span>, which binds both activities, marked decreased, as ai-gene-review gives them.
The KB node and the review share <span class="result" data-compare="names" data-code="g.shared_processes()">glycogen catabolic process<span class="method"></span></span>.
