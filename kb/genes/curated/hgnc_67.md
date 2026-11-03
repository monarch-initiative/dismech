---
hgnc_id: hgnc:67
symbol: ABCD3
status: DRAFT
---

# ABCD3 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:67")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ABCD3<span class="method"></span></span>** (<span class="result" data-code="g.name()">ATP binding cassette subfamily D member 3<span class="method"></span></span>), also called PMP70, is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span> disorder entry.

## Normal function

ai-gene-review gives ABCD3's core molecular functions as <span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">ABC-type fatty-acyl-CoA transporter activity; fatty acyl-CoA hydrolase activity; and long-chain fatty acid transmembrane transporter activity<span class="method"></span></span>, acting in <span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">bile acid and bile salt transport; bile acid biosynthetic process; fatty acid beta-oxidation; long-chain fatty acid import into peroxisome; and phytanic acid metabolic process<span class="method"></span></span>, at the <span class="result" data-compare="names" data-code="g.core_function_terms('locations')">peroxisomal membrane<span class="method"></span></span>. The transporter activity and the thioesterase activity are the two halves of substrate handling at the membrane, feeding the beta-oxidation and bile-acid processes the disease entry turns on.

## Disease records

The one entry types ABCD3 as causative: <span class="result" data-compare="names" data-code="g.disorders('causative')">Congenital Bile Acid Synthesis Defect 5<span class="method"></span></span>, with a <span class="result" data-code="g.variant_origin('Congenital Bile Acid Synthesis Defect 5')">germline<span class="method"></span></span> variant origin and a functional impact of <span class="result" data-code="g.functional_impact('Congenital Bile Acid Synthesis Defect 5')">loss of function<span class="method"></span></span>. ABCD3 sits on the node <span class="result" data-code="g.node('Congenital Bile Acid Synthesis Defect 5', 'ABCD3 Loss of Function')">ABCD3 Loss of Function<span class="method"></span></span>. ClinGen rates the relationship only <span class="result" data-code="g.clingen('Congenital Bile Acid Synthesis Defect 5')">limited<span class="method"></span></span>, below the Definitive or Strong tier that a causative typing implies.

## Where the layers agree and disagree

The KB process on ABCD3's own node is <span class="result" data-compare="names" data-code="g.mechanism_processes()">peroxisome organization<span class="method"></span></span>, recorded as abnormal, while the import and bile-acid processes sit on downstream nodes; the exact-identifier overlap with ai-gene-review core processes is therefore <span class="result" data-code="len(g.shared_processes())">0<span class="method"></span></span>.
