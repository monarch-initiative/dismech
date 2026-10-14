---
hgnc_id: hgnc:343
symbol: AHCY
status: DRAFT
---

# AHCY across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:343")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">AHCY<span class="method"></span></span>**
(<span class="result" data-code="g.name()">adenosylhomocysteinase<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry.

## Normal function

ai-gene-review gives AHCY's core molecular function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">adenosylhomocysteinase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">L-homocysteine biosynthetic process; and L-methionine cycle<span class="method"></span></span>:
the enzyme hydrolyses S-adenosyl-L-homocysteine, the product inhibitor of
methyltransferases, to adenosine and homocysteine.

## Causative record

The one entry that names AHCY,
<span class="result" data-compare="names" data-code="g.disorders('causative', 'germline')">S-Adenosylhomocysteine Hydrolase Deficiency<span class="method"></span></span>,
types it
<span class="result" data-code="g.relationship('S-Adenosylhomocysteine Hydrolase Deficiency')">causative<span class="method"></span></span>
with a
<span class="result" data-code="g.variant_origin('S-Adenosylhomocysteine Hydrolase Deficiency')">germline<span class="method"></span></span>
origin, and records a
<span class="result" data-code="g.functional_impact('S-Adenosylhomocysteine Hydrolase Deficiency')">loss of function<span class="method"></span></span>
impact. ClinGen rates the gene
<span class="result" data-code="g.clingen('S-Adenosylhomocysteine Hydrolase Deficiency')">definitive<span class="method"></span></span>
for this disease. The gene sits on the node
<span class="result" data-code="g.node('S-Adenosylhomocysteine Hydrolase Deficiency', 'AHCY Loss of Function')">AHCY Loss of Function<span class="method"></span></span>,
which marks the same adenosylhomocysteinase activity that ai-gene-review
gives as the core function as decreased.

## Where the layers disagree

The KB's AHCY node carries a molecular-function term but no GO process, so the
two layers share
<span class="result" data-code="len(g.shared_processes())">0<span class="method"></span></span>
process terms by identifier; at the level of molecular function they agree.
