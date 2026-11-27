---
hgnc_id: hgnc:29
symbol: ABCA1
status: DRAFT
---

# ABCA1 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:29")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ABCA1<span class="method"></span></span>**
(<span class="result" data-code="g.name()">ATP binding cassette subfamily A member 1<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">4<span class="method"></span></span>
disorder entries. It encodes the transporter that hands cellular phospholipid and cholesterol to lipid-poor apolipoprotein A-I, the first step of HDL formation.

## Normal function

ai-gene-review gives ABCA1's core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">apolipoprotein A-I receptor activity; ATPase-coupled intramembrane lipid transporter activity; and cholesterol transfer activity<span class="method"></span></span>.
The intramembrane lipid term is the phospholipid floppase activity, moving
phospholipid to the outer leaflet, and the receptor term is the docking of
apoA-I that receives it.

## Causative records

The entries that type ABCA1 as causative include
<span class="result" data-compare="names" data-code="g.includes('Tangier Disease', 'Hypoalphalipoproteinemia, Primary, 1', relationship='causative')">Tangier Disease; and Hypoalphalipoproteinemia, Primary, 1<span class="method"></span></span>.
They are the two dosages of one locus: biallelic loss in Tangier Disease and a
single allele in the dominant low-HDL disorder, recorded with a
<span class="result" data-code="g.functional_impact('Hypoalphalipoproteinemia, Primary, 1')">partial loss of function<span class="method"></span></span>
impact. Tangier Disease places the gene on
<span class="result" data-code="g.node('Tangier Disease', 'ABCA1 Dysfunction')">ABCA1 Dysfunction<span class="method"></span></span>,
which binds the floppase activity and apolipoprotein A-I binding as decreased,
and the heterozygous entry places it on
<span class="result" data-code="g.node('Hypoalphalipoproteinemia, Primary, 1', 'ABCA1 Heterozygous Loss of Function')">ABCA1 Heterozygous Loss of Function<span class="method"></span></span>
with the floppase activity decreased.

## Other records

Smith-Lemli-Opitz syndrome carries ABCA1 as a modifier
(<span class="result" data-compare="names" data-code="g.includes('Smith-Lemli-Opitz syndrome', relationship='modifier')">Smith-Lemli-Opitz syndrome<span class="method"></span></span>).
MEND Syndrome types it as
<span class="result" data-code="g.relationship('MEND Syndrome')">unknown<span class="method"></span></span>:
there ABCA1 is a candidate modifier from a single-family variant-burden analysis that has
not been replicated or functionally validated.

## Where the layers agree

The KB nodes naming ABCA1 and the ai-gene-review core functions share
<span class="result" data-compare="names" data-code="g.shared_processes()">cholesterol efflux; and phospholipid efflux<span class="method"></span></span>
by exact GO identifier.

ClinGen has classified ABCA1 for
<span class="result" data-code="g.clingen_diseases()">0<span class="method"></span></span>
diseases.
