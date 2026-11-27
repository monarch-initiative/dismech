---
hgnc_id: hgnc:600
symbol: APOA1
status: DRAFT
---

# APOA1 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:600")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">APOA1<span class="method"></span></span>**
(<span class="result" data-code="g.name()">apolipoprotein A1<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry. It encodes apoA-I, the principal structural protein of HDL.

## Normal function

ai-gene-review has no completed review for APOA1
(<span class="result" data-code="len(g.core_function_terms())">0<span class="method"></span></span> core-function terms).

## Causative record

Familial Visceral Amyloidosis types APOA1 as
<span class="result" data-code="g.relationship('Familial Visceral Amyloidosis')">causative<span class="method"></span></span>,
with a
<span class="result" data-code="g.variant_origin('Familial Visceral Amyloidosis')">germline<span class="method"></span></span>
origin, for its apolipoprotein A-I amyloidosis subtype. The gene sits on the
shared precursor node
<span class="result" data-code="g.node('Familial Visceral Amyloidosis', 'Variant Plasma Protein Amyloidogenic Precursor')">Variant Plasma Protein Amyloidogenic Precursor<span class="method"></span></span>,
which records abnormal protein folding and binds no molecular function: the
amyloidogenic variants give the protein a tendency to aggregate rather than
removing one of its normal activities.

## ClinGen

ClinGen has classified APOA1 for
<span class="result" data-code="g.clingen_diseases()">0<span class="method"></span></span>
diseases.
