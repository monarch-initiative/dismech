---
hgnc_id: hgnc:61
symbol: ABCD1
status: DRAFT
---

# ABCD1 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:61")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ABCD1<span class="method"></span></span>**
(<span class="result" data-code="g.name()">ATP binding cassette subfamily D member 1<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">2<span class="method"></span></span>
disorder entries.

## Normal function

ABCD1 encodes ALDP, a peroxisomal membrane ABC half-transporter that brings
saturated very-long-chain fatty acyl-CoA esters into the peroxisome for
beta-oxidation. ai-gene-review gives its core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">ABC-type fatty-acyl-CoA transporter activity; and fatty acyl-CoA hydrolase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">long-chain fatty acid import into peroxisome; fatty acid beta-oxidation; and fatty acid homeostasis<span class="method"></span></span>
at the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">peroxisomal membrane<span class="method"></span></span>.
The review notes that whether the thioesterase activity is part of native
transport is unresolved.

## Causative records

The entries naming ABCD1 type it as causative with a germline origin,
including
<span class="result" data-compare="names" data-code="g.includes('adrenoleukodystrophy', 'Chronic Primary Adrenal Insufficiency', relationship='causative')">adrenoleukodystrophy; and Chronic Primary Adrenal Insufficiency<span class="method"></span></span>.
In adrenoleukodystrophy the gene sits on
<span class="result" data-code="g.node('adrenoleukodystrophy', 'ABCD1-mediated peroxisomal fatty acid transport defect')">ABCD1-mediated peroxisomal fatty acid transport defect<span class="method"></span></span>,
which binds the ABC-type fatty-acyl-CoA transporter activity as decreased; that
node conforms to the module
<span class="result" data-code="g.in_module('peroxisomal_metabolic_failure')">peroxisomal_metabolic_failure<span class="method"></span></span>.
Chronic Primary Adrenal Insufficiency records ABCD1 for its genetic subtype,
because adrenal failure is often the first sign of adrenoleukodystrophy, and
places it on no mechanism node.

## Where the layers agree and disagree

The KB's ABCD1 node and ai-gene-review share
<span class="result" data-compare="names" data-code="g.shared_processes()">fatty acid beta-oxidation<span class="method"></span></span>
by exact GO identifier, and both bind the same transporter activity.

ClinGen classifies ABCD1 for
<span class="result" data-code="g.clingen_diseases()">1<span class="method"></span></span>
disease, adrenoleukodystrophy, rated
<span class="result" data-code="g.clingen('adrenoleukodystrophy')">definitive<span class="method"></span></span>;
the matching dismech entry records that tier.
