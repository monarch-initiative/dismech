---
hgnc_id: hgnc:119
symbol: ACOX1
status: DRAFT
---

# ACOX1 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:119")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ACOX1<span class="method"></span></span>**
(<span class="result" data-code="g.name()">acyl-CoA oxidase 1<span class="method"></span></span>)
is named by
<span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry.

## Normal function

ai-gene-review gives ACOX1's core molecular function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">acyl-CoA oxidase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">fatty acid beta-oxidation using acyl-CoA oxidase; hydrogen peroxide biosynthetic process; and very long-chain fatty acid beta-oxidation<span class="method"></span></span>
in the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">peroxisomal matrix<span class="method"></span></span>.
This is the first, FAD-dependent step of peroxisomal beta-oxidation, which
passes electrons to oxygen and so produces hydrogen peroxide.

## Causative record

The one entry that names ACOX1 types it as causative:
<span class="result" data-compare="names" data-code="g.disorders('causative')">Peroxisomal Acyl-CoA Oxidase Deficiency<span class="method"></span></span>,
with germline variants
(<span class="result" data-code="g.variant_origin('Peroxisomal Acyl-CoA Oxidase Deficiency')">germline<span class="method"></span></span>).
The gene sits on the node
<span class="result" data-code="g.node('Peroxisomal Acyl-CoA Oxidase Deficiency', 'ACOX1 Straight-Chain Acyl-CoA Oxidase Deficiency')">ACOX1 Straight-Chain Acyl-CoA Oxidase Deficiency<span class="method"></span></span>,
whose functional impact is recorded as
<span class="result" data-code="g.functional_impact('Peroxisomal Acyl-CoA Oxidase Deficiency')">loss of function<span class="method"></span></span>.
ClinGen rates the relationship
<span class="result" data-code="g.clingen('Peroxisomal Acyl-CoA Oxidase Deficiency')">definitive<span class="method"></span></span>.

## Agreement between the layers

The KB annotates the ACOX1 node with
<span class="result" data-compare="names" data-code="g.mechanism_processes()">fatty acid beta-oxidation using acyl-CoA oxidase; and very long-chain fatty acid beta-oxidation<span class="method"></span></span>,
and both terms are among ai-gene-review's core processes for the gene
(<span class="result" data-code="len(g.shared_processes())">2<span class="method"></span></span>
shared by exact identifier).

## Gaps

ClinGen classifies ACOX1 for
<span class="result" data-code="g.clingen_diseases()">2<span class="method"></span></span>
diseases. The one with no dismech entry is
<span class="result" data-compare="names" data-code="g.clingen_without_entry()">Mitchell syndrome<span class="method"></span></span>,
the dominant gain-of-function ACOX1 disorder, which is a candidate for a new
entry.
