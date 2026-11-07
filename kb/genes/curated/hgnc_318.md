---
hgnc_id: hgnc:318
symbol: AGA
status: DRAFT
---

# AGA across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:318")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">AGA<span class="method"></span></span>**
(<span class="result" data-code="g.name()">aspartylglucosaminidase<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">2<span class="method"></span></span>
disorder entries: the disease it causes and the class entry for the
glycoproteinoses.

## How the entries record the gene

Both entries type AGA as causative
(<span class="result" data-compare="names" data-code="g.disorders('causative')">Aspartylglucosaminuria; Glycoprotein Storage Disease<span class="method"></span></span>),
with germline variants in Aspartylglucosaminuria
(<span class="result" data-code="g.variant_origin('Aspartylglucosaminuria')">germline<span class="method"></span></span>).
No record is left untyped
(<span class="result" data-code="len(g.untyped())">0<span class="method"></span></span>).
ClinGen classifies AGA for
<span class="result" data-code="g.clingen_diseases()">1<span class="method"></span></span>
disease, and for Aspartylglucosaminuria its tier is
<span class="result" data-code="g.clingen('Aspartylglucosaminuria')">definitive<span class="method"></span></span>;
the entry records that assertion in its `gene_disease_validity`.

## Where the gene sits in the pathograph

In Aspartylglucosaminuria the gene is bound to two nodes
(<span class="result" data-compare="names" data-code="g.nodes('Aspartylglucosaminuria')">AGA lysosomal enzyme deficiency; AGA protein maturation and folding defects<span class="method"></span></span>):
loss of the GlcNAc-Asn-cleaving activity in the lysosome, and the failure of
the mutant precursor to fold and mature. The processes carried by those nodes are
<span class="result" data-compare="names" data-code="g.mechanism_processes()">glycoprotein catabolic process; protein deglycosylation; protein folding; protein maturation<span class="method"></span></span>.
The class entry Glycoprotein Storage Disease names AGA on its shared node
<span class="result" data-code="g.node('Glycoprotein Storage Disease', 'Lysosomal Glycosidase Deficiency and Impaired Glycoprotein Catabolism')">Lysosomal Glycosidase Deficiency and Impaired Glycoprotein Catabolism<span class="method"></span></span>,
which marks glycoprotein catabolic process as decreased.

The gene reaches the
<span class="result" data-code="g.in_module('lysosomal_substrate_accumulation')">lysosomal_substrate_accumulation<span class="method"></span></span>
module through its node, and no treatment record names it
(<span class="result" data-code="len(g.treatments())">0<span class="method"></span></span>).

## Normal function

ai-gene-review gives AGA's core molecular function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">N4-(beta-N-acetylglucosaminyl)-L-asparaginase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">glycoprotein catabolic process; and protein deglycosylation<span class="method"></span></span>,
at the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">lysosome<span class="method"></span></span>
(<span class="result" data-code="len(g.core_function_terms())">4<span class="method"></span></span>
terms in all). The review describes the enzyme as an N-terminal nucleophile
hydrolase whose precursor is cleaved autocatalytically, hydrolysing the
GlcNAc-Asn bond as a late step of N-glycoprotein degradation. Those two
processes are also the terms the Aspartylglucosaminuria node marks as decreased,
so the two layers share
<span class="result" data-code="len(g.shared_processes())">2<span class="method"></span></span>
GO process terms by exact identifier; the KB adds the folding and maturation
pair beneath them.
