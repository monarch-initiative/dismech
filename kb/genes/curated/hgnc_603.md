---
hgnc_id: hgnc:603
symbol: APOB
status: DRAFT
---

# APOB across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:603")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">APOB<span class="method"></span></span>**
(<span class="result" data-code="g.name()">apolipoprotein B<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">5<span class="method"></span></span>
disorder entries. It encodes apolipoprotein B, the structural
protein of chylomicrons, VLDL and LDL particles.

## Normal function

The pinned ai-gene-review snapshot that the ingest layer reads has no core
functions for APOB
(<span class="result" data-code="len(g.core_function_terms())">0<span class="method"></span></span>
terms). An upstream review of the gene is being added or updated.

## Causative records

The entries that type APOB as causative are
<span class="result" data-compare="names" data-code="g.disorders('causative')">Familial Defective Apolipoprotein B-100; Hypobetalipoproteinemia<span class="method"></span></span>,
and the germline-origin causative entries are
<span class="result" data-compare="names" data-code="g.disorders('causative', 'germline')">Familial Defective Apolipoprotein B-100; Hypobetalipoproteinemia<span class="method"></span></span>.
ClinGen rates the gene
<span class="result" data-code="g.clingen('Familial Defective Apolipoprotein B-100')">definitive<span class="method"></span></span>
for familial defective apolipoprotein B-100 and
<span class="result" data-code="g.clingen('Hypobetalipoproteinemia')">definitive<span class="method"></span></span>
for hypobetalipoproteinemia.

In Familial Defective Apolipoprotein B-100 the gene sits on the nodes
<span class="result" data-code="g.node('Familial Defective Apolipoprotein B-100', 'APOB Receptor-Binding-Region Missense Variant')">APOB Receptor-Binding-Region Missense Variant<span class="method"></span></span>
and
<span class="result" data-code="g.node('Familial Defective Apolipoprotein B-100', 'Defective ApoB-100 Binding to a Structurally Normal LDL Receptor')">Defective ApoB-100 Binding to a Structurally Normal LDL Receptor<span class="method"></span></span>.
In Hypobetalipoproteinemia it sits on
<span class="result" data-code="g.node('Hypobetalipoproteinemia', 'APOB Truncating Variant')">APOB Truncating Variant<span class="method"></span></span>
and
<span class="result" data-code="g.node('Hypobetalipoproteinemia', 'Impaired Hepatic and Intestinal ApoB-Lipoprotein Assembly and Secretion')">Impaired Hepatic and Intestinal ApoB-Lipoprotein Assembly and Secretion<span class="method"></span></span>.
The KB's mechanism annotations for APOB name the processes
<span class="result" data-compare="names" data-code="g.mechanism_processes()">cholesterol metabolic process; low-density lipoprotein particle clearance; receptor-mediated endocytosis; very-low-density lipoprotein particle assembly<span class="method"></span></span>.

## Other entries

MEND Syndrome records APOB as
<span class="result" data-code="g.relationship('MEND Syndrome')">modifier<span class="method"></span></span>.
The entries with a genetic record for APOB that carries no relationship type are
<span class="result" data-compare="names" data-code="g.untyped()">Familial Hypercholesterolemia; Hyperlipidemia<span class="method"></span></span>.

## Where the layers disagree

Because the pinned ai-gene-review snapshot has no core functions for the gene,
the KB and ai-gene-review currently share
<span class="result" data-code="len(g.shared_processes())">0<span class="method"></span></span>
GO process terms.
