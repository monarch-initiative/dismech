---
hgnc_id: hgnc:59
symbol: ABCC8
status: DRAFT
---

# ABCC8 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:59")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ABCC8<span class="method"></span></span>** (<span class="result" data-code="g.name()">ATP binding cassette subfamily C member 8<span class="method"></span></span>) is named by <span class="result" data-code="g.disorder_count()">4<span class="method"></span></span> disorder
entries, including
<span class="result" data-compare="names" data-code="g.includes('Congenital Isolated Hyperinsulinism', 'Hyperinsulinemic Hypoglycemia', 'Diabetes mellitus', relationship='causative')">Congenital Isolated Hyperinsulinism; Diabetes mellitus; and Hyperinsulinemic Hypoglycemia<span class="method"></span></span>.
The same gene causes opposite diseases depending on the direction of the
variant: loss of SUR1 function causes hyperinsulinism, gain of function
causes neonatal diabetes.

## Normal function

ai-gene-review gives SUR1's core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">ATP hydrolysis activity; and potassium channel regulator activity<span class="method"></span></span>, at the
<span class="result" data-compare="names" data-code="g.core_function_terms('locations')">plasma membrane<span class="method"></span></span>, acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">potassium ion transmembrane transport; and regulation of insulin secretion<span class="method"></span></span>.
SUR1 is the regulatory subunit of the beta-cell K-ATP channel whose pore is
Kir6.2 (KCNJ11), so each K-ATP node that carries ABCC8 binds potassium channel
regulator activity alongside the Kir6.2 channel activity.

## Causative records

The causative records with a germline variant origin are
<span class="result" data-compare="names" data-code="g.disorders('causative', 'germline')">Congenital Isolated Hyperinsulinism; Diabetes mellitus; and Hyperinsulinemic Hypoglycemia<span class="method"></span></span>.
In Congenital Isolated Hyperinsulinism the gene sits on
<span class="result" data-code="g.node('Congenital Isolated Hyperinsulinism', 'KATP Channel Loss of Function')">KATP Channel Loss of Function<span class="method"></span></span>;
in Hyperinsulinemic Hypoglycemia on
<span class="result" data-code="g.node('Hyperinsulinemic Hypoglycemia', 'K-ATP Channel Loss of Function')">K-ATP Channel Loss of Function<span class="method"></span></span>
and on
<span class="result" data-code="g.node('Hyperinsulinemic Hypoglycemia', 'Focal Lesion Formation by Paternal K-ATP Variant and Somatic 11p15 Maternal Loss')">Focal Lesion Formation by Paternal K-ATP Variant and Somatic 11p15 Maternal Loss<span class="method"></span></span>.
Both hyperinsulinism nodes mark the regulator activity decreased. Diabetes
mellitus records the activating arm on
<span class="result" data-code="g.node('Diabetes mellitus', 'K-ATP Channel Overactivity from Activating ABCC8 or KCNJ11 Variants')">K-ATP Channel Overactivity from Activating ABCC8 or KCNJ11 Variants<span class="method"></span></span>,
which marks it increased, with ClinGen rating the gene
<span class="result" data-code="g.clingen('Diabetes mellitus')">definitive<span class="method"></span></span> for monogenic diabetes.

Placental Abruption records ABCC8 as
<span class="result" data-code="g.relationship('Placental Abruption')">unknown<span class="method"></span></span>: its only evidence is a
suggestive, not genome-wide significant, association.

## Where the layers agree and disagree

The KB and ai-gene-review share <span class="result" data-code="len(g.shared_processes())">2<span class="method"></span></span> GO process terms:
<span class="result" data-compare="names" data-code="g.shared_processes()">potassium ion transmembrane transport; and regulation of insulin secretion<span class="method"></span></span>.
ClinGen classifies ABCC8 for <span class="result" data-code="g.clingen_diseases()">4<span class="method"></span></span> diseases; those with no
matching dismech entry are <span class="result" data-compare="names" data-code="g.clingen_without_entry()">hyperinsulinemic hypoglycemia, familial, 1; and hyperinsulinism<span class="method"></span></span>. The hyperinsulinism
entries cover this biology, but they map HHF1 only as a narrower match and do
not bind the broader hyperinsulinism class, so neither ClinGen tier is recorded
on them.
