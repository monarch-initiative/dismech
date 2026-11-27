---
hgnc_id: hgnc:609
symbol: APOC2
status: DRAFT
---

# APOC2 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:609")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">APOC2<span class="method"></span></span>**
(<span class="result" data-code="g.name()">apolipoprotein C2<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry. 

## Normal function

ApoC-II is the apolipoprotein cofactor that activates lipoprotein lipase on
the surface of triglyceride-rich lipoproteins. ai-gene-review has no completed
review for the gene
(<span class="result" data-code="len(g.core_function_terms())">0<span class="method"></span></span> core-function terms).

## Causative record

Familial Chylomicronemia Syndrome types APOC2 as
<span class="result" data-code="g.relationship('Familial Chylomicronemia Syndrome')">causative<span class="method"></span></span>,
with a <span class="result" data-code="g.variant_origin('Familial Chylomicronemia Syndrome')">germline<span class="method"></span></span> origin, for its APOC2
subtype. The gene sits on the shared node
<span class="result" data-code="g.node('Familial Chylomicronemia Syndrome', 'Defective LPL Maturation, Trafficking, and Activation')">Defective LPL Maturation, Trafficking, and Activation<span class="method"></span></span>,
which binds lipoprotein lipase activator activity as decreased.

## ClinGen

ClinGen has classified APOC2 for
<span class="result" data-code="g.clingen_diseases()">0<span class="method"></span></span>
diseases, so the causative typing rests on the entries' own evidence.
