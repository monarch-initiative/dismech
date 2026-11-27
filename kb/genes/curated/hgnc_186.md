---
hgnc_id: hgnc:186
symbol: ADA
status: DRAFT
---

# ADA across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:186")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ADA<span class="method"></span></span>**
(<span class="result" data-code="g.name()">adenosine deaminase<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry.

## Normal function

ai-gene-review gives ADA's core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">2'-deoxyadenosine deaminase activity; and adenosine deaminase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">adenosine catabolic process; and deoxyadenosine catabolic process<span class="method"></span></span>.
The enzyme deaminates adenosine and 2'-deoxyadenosine, the two nucleosides
whose accumulation the KB records as lymphotoxic.

## Causative record

ADA is named by the Severe Combined Immunodeficiency entry, which types it
<span class="result" data-code="g.relationship('Severe Combined Immunodeficiency')">causative<span class="method"></span></span>
with a
<span class="result" data-code="g.variant_origin('Severe Combined Immunodeficiency')">germline<span class="method"></span></span>
origin for its ADA deficiency subtype. ClinGen rates the gene
<span class="result" data-code="g.clingen('Severe Combined Immunodeficiency')">definitive<span class="method"></span></span>
for ADA-deficient T-B-NK- SCID, the subtype's own MONDO term.

The gene sits on
<span class="result" data-code="g.node('Severe Combined Immunodeficiency', 'Toxic purine metabolite accumulation')">Toxic purine metabolite accumulation<span class="method"></span></span>,
which marks both deaminase activities as decreased. The SCID it causes is
metabolic rather than a defect of a lymphocyte receptor or signalling protein:
adenosine and above all deoxyadenosine, with intracellular dATP, accumulate and
are toxic to every lymphoid lineage, which is why ADA deficiency gives a
T-B-NK- immunophenotype.

## Where the layers agree

The node and the review share
<span class="result" data-compare="names" data-code="g.shared_processes()">adenosine catabolic process; and deoxyadenosine catabolic process<span class="method"></span></span>
by exact GO identifier, and the node's two decreased activities are the
review's two core molecular functions.
