---
hgnc_id: hgnc:491
symbol: ANGPTL3
status: DRAFT
---

# ANGPTL3 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:491")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ANGPTL3<span class="method"></span></span>**
(<span class="result" data-code="g.name()">angiopoietin like 3<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span> disorder entry:
<span class="result" data-compare="names" data-code="g.disorders()">Hypobetalipoproteinemia<span class="method"></span></span>.

## Normal function

ai-gene-review gives ANGPTL3's core molecular function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">lipase inhibitor activity<span class="method"></span></span>,
in the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">extracellular region<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">cholesterol homeostasis; phospholipid homeostasis; and triglyceride homeostasis<span class="method"></span></span>.

## Familial combined hypolipidemia

Hypobetalipoproteinemia types ANGPTL3 as
<span class="result" data-code="g.relationship('Hypobetalipoproteinemia')">causative<span class="method"></span></span>
with a <span class="result" data-code="g.variant_origin('Hypobetalipoproteinemia')">germline<span class="method"></span></span>
variant origin and a functional impact of
<span class="result" data-code="g.functional_impact('Hypobetalipoproteinemia')">loss of function<span class="method"></span></span>.
ClinGen rates the gene
<span class="result" data-code="g.clingen('Hypobetalipoproteinemia')">definitive<span class="method"></span></span>
for familial hypobetalipoproteinemia 2, which the entry carries as its ANGPTL3
subtype. The gene sits on the node
<span class="result" data-code="g.node('Hypobetalipoproteinemia', 'ANGPTL3 Loss-of-Function Variant')">ANGPTL3 Loss-of-Function Variant<span class="method"></span></span>,
which records lipase inhibitor activity as decreased. Downstream nodes record
increased lipoprotein lipase activity and increased triglyceride catabolism.
