---
hgnc_id: hgnc:646
symbol: ARAF
status: DRAFT
---

# ARAF across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:646")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ARAF<span class="method"></span></span>**
(<span class="result" data-code="g.name()">A-Raf proto-oncogene, serine/threonine kinase<span class="method"></span></span>)
is the least represented of the three RAF kinases in the KB: one disorder entry
names it
(<span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>).

## Normal function

ai-gene-review gives ARAF's core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">MAP kinase kinase kinase activity; and protein heterodimerization activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">MAPK cascade<span class="method"></span></span>.

## Somatic driver record

Langerhans Cell Histiocytosis types ARAF as a
<span class="result" data-code="g.relationship('Langerhans Cell Histiocytosis')">somatic driver<span class="method"></span></span>,
origin
<span class="result" data-code="g.variant_origin('Langerhans Cell Histiocytosis')">somatic<span class="method"></span></span>:
activating ARAF mutations are a rare alternative to BRAF V600E there. The
entry places ARAF beside BRAF on the node
<span class="result" data-code="g.node('Langerhans Cell Histiocytosis', 'Somatic MAPK Lesion in a Myeloid Precursor')">Somatic MAPK Lesion in a Myeloid Precursor<span class="method"></span></span>.

## Where the layers disagree

ClinGen classifies ARAF for
<span class="result" data-code="g.clingen_diseases()">0<span class="method"></span></span>
diseases, and the KB's ARAF node and the ai-gene-review core functions share
<span class="result" data-code="len(g.shared_processes())">0<span class="method"></span></span>
GO process terms by exact identifier.
