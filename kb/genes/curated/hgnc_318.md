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

The ai-gene-review ingest layer currently reports
<span class="result" data-code="len(g.core_function_terms())">0<span class="method"></span></span>
core function terms for AGA, because the ingest tables are pinned to an
ai-gene-review commit that predates the review of this gene. The upstream
review, written in the same round of work as this page, gives
N4-(beta-N-acetylglucosaminyl)-L-asparaginase activity in the lysosome, acting
in glycoprotein catabolism and protein deglycosylation, as the core function,
and records the autoproteolytic activation of the precursor. Glycoprotein
catabolic process and protein deglycosylation are the same terms the
Aspartylglucosaminuria node marks as decreased, so the two layers should share
them once the ingest pin is advanced; until then they share
<span class="result" data-code="len(g.shared_processes())">0<span class="method"></span></span>.
