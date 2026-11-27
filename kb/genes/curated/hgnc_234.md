---
hgnc_id: hgnc:234
symbol: ADCY3
status: DRAFT
---

# ADCY3 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:234")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ADCY3<span class="method"></span></span>**
(<span class="result" data-code="g.name()">adenylate cyclase 3<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry. It encodes the adenylyl cyclase of neuronal primary cilia.

## Normal function

ai-gene-review has no completed review for ADCY3
(<span class="result" data-code="len(g.core_function_terms())">0<span class="method"></span></span> core-function terms).

## Record

Avoidant Restrictive Food Intake Disorder records ADCY3 as
<span class="result" data-code="g.relationship('Avoidant Restrictive Food Intake Disorder')">unknown<span class="method"></span></span>,
with a <span class="result" data-code="g.variant_origin('Avoidant Restrictive Food Intake Disorder')">germline<span class="method"></span></span> origin. The evidence is
a genome-wide association with a parent-reported avoidant and restrictive
eating trait in a birth cohort, whose definition did not assess the full
ARFID diagnostic criteria, so the relationship to diagnosed ARFID is open. No
mechanism node names the gene
(<span class="result" data-code="len(g.nodes('Avoidant Restrictive Food Intake Disorder'))">0<span class="method"></span></span>).
