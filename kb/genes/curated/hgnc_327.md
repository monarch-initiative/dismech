---
hgnc_id: hgnc:327
symbol: AGPS
status: DRAFT
---

# AGPS across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:327")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">AGPS<span class="method"></span></span>**
(<span class="result" data-code="g.name()">alkylglycerone phosphate synthase<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry. It encodes the peroxisomal enzyme that
forms the ether bond in the second step of plasmalogen synthesis.

## Normal function

The ai-gene-review core functions for AGPS name
<span class="result" data-compare="names" data-code="g.core_function_terms()">alkylglycerone-phosphate synthase activity; ether lipid biosynthetic process; peroxisomal matrix; peroxisomal membrane<span class="method"></span></span>.

## Causative records

One entry types AGPS as causative:
<span class="result" data-compare="names" data-code="g.disorders('causative')">Rhizomelic Chondrodysplasia Punctata, Plasmalogen-Synthesis Defect<span class="method"></span></span>,
recording the variants as
<span class="result" data-code="g.variant_origin('Rhizomelic Chondrodysplasia Punctata, Plasmalogen-Synthesis Defect')">germline<span class="method"></span></span>.
There the gene sits on the node
<span class="result" data-code="g.node('Rhizomelic Chondrodysplasia Punctata, Plasmalogen-Synthesis Defect', 'Plasmalogen-Synthesis Enzyme Deficiency')">Plasmalogen-Synthesis Enzyme Deficiency<span class="method"></span></span>,
which reaches the mechanism module
<span class="result" data-compare="names" data-code="g.modules()">peroxisomal_metabolic_failure<span class="method"></span></span>.

## Where the layers agree

The KB's mechanism annotations and the ai-gene-review core functions share the
GO process
<span class="result" data-compare="names" data-code="g.shared_processes()">ether lipid biosynthetic process<span class="method"></span></span>.
ClinGen classifies AGPS for
<span class="result" data-code="g.clingen_diseases()">1<span class="method"></span></span>
disease,
<span class="result" data-compare="names" data-code="g.clingen_without_entry()">alkylglycerone-phosphate synthase deficiency<span class="method"></span></span>,
which the join to dismech does not match to any entry.
