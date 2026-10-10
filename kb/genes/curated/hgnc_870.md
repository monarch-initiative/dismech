---
hgnc_id: hgnc:870
symbol: ATP7B
status: DRAFT
---

# ATP7B across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:870")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ATP7B<span class="method"></span></span>**
(<span class="result" data-code="g.name()">ATPase copper transporting beta<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">2<span class="method"></span></span> disorder entries.

## Normal function

ai-gene-review gives ATP7B's core molecular function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">P-type monovalent copper transporter activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">cellular detoxification of copper ion; copper ion export; copper ion transport; and intracellular copper ion homeostasis<span class="method"></span></span>,
at the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">cytoplasmic vesicle; and trans-Golgi network membrane<span class="method"></span></span>.
The upstream review is being updated; this summary reflects the pinned ingest.

## Causative record

<span class="result" data-compare="names" data-code="g.disorders('causative')">Wilson Disease<span class="method"></span></span>
types ATP7B as causative, with
<span class="result" data-code="g.variant_origin('Wilson Disease')">germline<span class="method"></span></span>
variants, and ClinGen rates the pair
<span class="result" data-code="g.clingen('Wilson Disease')">definitive<span class="method"></span></span>.
The gene sits on
<span class="result" data-code="len(g.nodes('Wilson Disease'))">3<span class="method"></span></span>
pathophysiology nodes there, beginning with
<span class="result" data-code="g.node('Wilson Disease', 'ATP7B Copper-Trafficking Defect')">ATP7B Copper-Trafficking Defect<span class="method"></span></span>
and including
<span class="result" data-code="g.node('Wilson Disease', 'Impaired Biliary Copper Excretion')">Impaired Biliary Copper Excretion<span class="method"></span></span>
and <span class="result" data-code="g.node('Wilson Disease', 'Impaired Ceruloplasmin Loading')">Impaired Ceruloplasmin Loading<span class="method"></span></span>.

## Where the layers agree and disagree

The KB mechanism nodes and the ai-gene-review core functions share
<span class="result" data-compare="names" data-code="g.shared_processes()">copper ion transport<span class="method"></span></span>
by exact GO identifier; the Wilson Disease nodes also mark the review's core molecular function,
the P-type copper transporter activity, as decreased.

<span class="result" data-compare="names" data-code="g.untyped()">Liver Cirrhosis<span class="method"></span></span>
carries a genetic record for ATP7B with no relationship type
(<span class="result" data-code="g.relationship('Liver Cirrhosis')">untyped<span class="method"></span></span>),
which is the remaining curation gap on this page.
