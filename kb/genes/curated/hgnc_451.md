---
hgnc_id: hgnc:451
symbol: AMACR
status: DRAFT
---

# AMACR across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:451")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">AMACR<span class="method"></span></span>**
(<span class="result" data-code="g.name()">alpha-methylacyl-CoA racemase<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">2<span class="method"></span></span>
disorder entries.

## Normal function

AMACR converts the (R)-stereoisomers of 2-methyl-branched acyl-CoAs, pristanoyl-CoA
and the C27 bile acid intermediates, into their (S)-stereoisomers, the only form
peroxisomal beta-oxidation can degrade. ai-gene-review gives its core molecular
function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">alpha-methylacyl-CoA racemase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">bile acid biosynthetic process; and fatty acid beta-oxidation using acyl-CoA oxidase<span class="method"></span></span>
in the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">peroxisomal matrix; and mitochondrion<span class="method"></span></span>.

## Causative records

The entries naming AMACR type it as causative with a germline origin,
including
<span class="result" data-compare="names" data-code="g.includes('Alpha-Methylacyl-CoA Racemase Deficiency', 'Inborn Disorder of Bile Acid Synthesis', relationship='causative')">Alpha-Methylacyl-CoA Racemase Deficiency; and Inborn Disorder of Bile Acid Synthesis<span class="method"></span></span>.
They model the same enzyme deficiency from two sides. Alpha-Methylacyl-CoA
Racemase Deficiency covers both substrate streams, including the pristanic
acid arm behind the adult neuropathy and retinopathy, and places the gene on
<span class="result" data-code="g.node('Alpha-Methylacyl-CoA Racemase Deficiency', 'AMACR Racemase Loss of Function')">AMACR Racemase Loss of Function<span class="method"></span></span>,
with a
<span class="result" data-code="g.functional_impact('Alpha-Methylacyl-CoA Racemase Deficiency')">loss of function<span class="method"></span></span>
impact. Inborn Disorder of Bile Acid Synthesis records it for its BASD Type 4
subtype, congenital bile acid synthesis defect 4, on
<span class="result" data-code="g.node('Inborn Disorder of Bile Acid Synthesis', 'Peroxisomal C27 Side-Chain Enzyme Deficiency (AMACR)')">Peroxisomal C27 Side-Chain Enzyme Deficiency (AMACR)<span class="method"></span></span>.
Both nodes bind the racemase activity as decreased.

## Where the layers agree and disagree

Both layers give AMACR the same molecular function by GO identifier. They share
<span class="result" data-code="len(g.shared_processes())">0<span class="method"></span></span>
process terms by exact identifier, because the entries put the beta-oxidation
and bile acid processes on the nodes downstream of the racemase node rather
than on it.

ClinGen classifies AMACR for
<span class="result" data-code="g.clingen_diseases()">1<span class="method"></span></span>
disease, alpha-methylacyl-CoA racemase deficiency, a lumped entity that includes
the bile acid synthesis defect, rated
<span class="result" data-code="g.clingen('Alpha-Methylacyl-CoA Racemase Deficiency')">definitive<span class="method"></span></span>;
the matching dismech entry records that tier.
