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
<span class="result" data-code="g.disorder_count()">2<span class="method"></span></span>
disorder entries.

## Normal function

ai-gene-review gives ACOX1's core molecular function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">acyl-CoA oxidase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">fatty acid beta-oxidation using acyl-CoA oxidase; hydrogen peroxide biosynthetic process; and very long-chain fatty acid beta-oxidation<span class="method"></span></span>
in the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">peroxisomal matrix<span class="method"></span></span>.
This is the first, FAD-dependent step of peroxisomal beta-oxidation, which
passes electrons to oxygen and so produces hydrogen peroxide.

## Causative records

Both entries that name ACOX1 type it as causative:
<span class="result" data-compare="names" data-code="g.disorders('causative')">Mitchell Syndrome; and Peroxisomal Acyl-CoA Oxidase Deficiency<span class="method"></span></span>.
They are allelic disorders with opposite mechanisms.

In the recessive disorder the variants are
<span class="result" data-code="g.variant_origin('Peroxisomal Acyl-CoA Oxidase Deficiency')">germline<span class="method"></span></span>,
the gene sits on the node
<span class="result" data-code="g.node('Peroxisomal Acyl-CoA Oxidase Deficiency', 'ACOX1 Straight-Chain Acyl-CoA Oxidase Deficiency')">ACOX1 Straight-Chain Acyl-CoA Oxidase Deficiency<span class="method"></span></span>,
and the functional impact is recorded as
<span class="result" data-code="g.functional_impact('Peroxisomal Acyl-CoA Oxidase Deficiency')">loss of function<span class="method"></span></span>.
ClinGen rates that relationship
<span class="result" data-code="g.clingen('Peroxisomal Acyl-CoA Oxidase Deficiency')">definitive<span class="method"></span></span>.

In Mitchell syndrome the recurrent p.Asn237Ser variant is
<span class="result" data-code="g.variant_origin('Mitchell Syndrome')">germline<span class="method"></span></span>
(usually de novo), the gene sits on the node
<span class="result" data-code="g.node('Mitchell Syndrome', 'ACOX1 N237S Gain-of-Function Acyl-CoA Oxidase Hyperactivity')">ACOX1 N237S Gain-of-Function Acyl-CoA Oxidase Hyperactivity<span class="method"></span></span>,
and the functional impact is recorded as
<span class="result" data-code="g.functional_impact('Mitchell Syndrome')">gain of function<span class="method"></span></span>:
the same acyl-CoA oxidase activity is increased rather than lost, and the
excess hydrogen peroxide damages glia. ClinGen rates this relationship
<span class="result" data-code="g.clingen('Mitchell Syndrome')">definitive<span class="method"></span></span>
as well.

## Agreement between the layers

The KB annotates ACOX1 nodes with
<span class="result" data-compare="names" data-code="g.mechanism_processes()">fatty acid beta-oxidation using acyl-CoA oxidase; and very long-chain fatty acid beta-oxidation<span class="method"></span></span>,
and both terms are among ai-gene-review's core processes for the gene
(<span class="result" data-code="len(g.shared_processes())">2<span class="method"></span></span>
shared by exact identifier).

## Coverage

ClinGen classifies ACOX1 for
<span class="result" data-code="g.clingen_diseases()">2<span class="method"></span></span>
diseases, and
<span class="result" data-code="len(g.clingen_without_entry())">0<span class="method"></span></span>
of them lack a dismech entry.
