---
hgnc_id: hgnc:341
symbol: AGXT
status: DRAFT
---

# AGXT across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:341")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">AGXT<span class="method"></span></span>**
(<span class="result" data-code="g.name()">alanine--glyoxylate aminotransferase<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">2<span class="method"></span></span>
disorder entries:
<span class="result" data-compare="names" data-code="g.disorders()">Primary Hyperoxaluria Type 1; and Primary Hyperoxaluria Type 3<span class="method"></span></span>.

## Normal function

ai-gene-review gives AGXT's core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">L-alanine:glyoxylate transaminase activity; and L-serine:pyruvate transaminase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">L-alanine catabolic process; L-serine catabolic process; glycine biosynthetic process; and glyoxylate catabolic process<span class="method"></span></span>,
located in
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">peroxisomal matrix; and peroxisome<span class="method"></span></span>.
The KB's AGXT nodes share
<span class="result" data-compare="names" data-code="g.shared_processes()">glyoxylate catabolic process<span class="method"></span></span>
with those core functions: the PH1 trigger node marks that process as decreased,
the dysfunction counterpart of the transamination of glyoxylate to glycine.

## Causative record

One entry types AGXT as causative,
<span class="result" data-compare="names" data-code="g.disorders('causative', 'germline')">Primary Hyperoxaluria Type 1<span class="method"></span></span>,
with the variants recorded as
<span class="result" data-code="g.variant_origin('Primary Hyperoxaluria Type 1')">germline<span class="method"></span></span>.
There the gene sits on the node
<span class="result" data-code="g.node('Primary Hyperoxaluria Type 1', 'AGXT Alanine-Glyoxylate Aminotransferase Deficiency')">AGXT Alanine-Glyoxylate Aminotransferase Deficiency<span class="method"></span></span>.

## Modifier record

In Primary Hyperoxaluria Type 3 AGXT is typed
<span class="result" data-code="g.relationship('Primary Hyperoxaluria Type 3')">modifier<span class="method"></span></span>,
from a single family in which a heterozygous AGXT variant accompanied a more
severe HOGA1-related phenotype. No pathophysiology node in that entry names
AGXT (<span class="result" data-code="len(g.nodes('Primary Hyperoxaluria Type 3'))">0<span class="method"></span></span>).

## Where the layers disagree

ClinGen classifies AGXT for
<span class="result" data-code="g.clingen_diseases()">1<span class="method"></span></span>
disease, and that disease has no dismech entry matched to it:
<span class="result" data-compare="names" data-code="g.clingen_without_entry()">alanine glyoxylate aminotransferase deficiency<span class="method"></span></span>.
That MONDO term is the parent of primary hyperoxaluria type 1, so the ClinGen
tier is not attached to the PH1 record.
