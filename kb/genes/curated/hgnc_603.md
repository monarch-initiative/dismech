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

ai-gene-review gives APOB's core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">lipid carrier activity; and low-density lipoprotein particle receptor binding<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">cholesterol homeostasis; cholesterol transport; lipoprotein transport; low-density lipoprotein particle clearance; and very-low-density lipoprotein particle assembly<span class="method"></span></span>,
at the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">endoplasmic reticulum lumen; extracellular region; and smooth endoplasmic reticulum<span class="method"></span></span>.
The two functions are the two halves of the particle's life: the structural
lipid-carrier role it plays from assembly in the ER lumen onwards, and the
receptor binding that clears it from circulation.

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

## Where the layers agree

The KB mechanism nodes and the ai-gene-review core functions share
<span class="result" data-compare="names" data-code="g.shared_processes()">low-density lipoprotein particle clearance; and very-low-density lipoprotein particle assembly<span class="method"></span></span>
by exact GO identifier. The nodes naming APOB carry
<span class="result" data-compare="names" data-code="g.mechanism_processes()">cholesterol metabolic process; low-density lipoprotein particle clearance; receptor-mediated endocytosis; and very-low-density lipoprotein particle assembly<span class="method"></span></span>,
so the two layers meet on the assembly and clearance steps and the KB adds the
endocytic mechanism beneath the clearance one.
