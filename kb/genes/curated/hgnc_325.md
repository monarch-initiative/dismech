---
hgnc_id: hgnc:325
symbol: AGPAT2
status: DRAFT
---

# AGPAT2 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:325")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">AGPAT2<span class="method"></span></span>**
(<span class="result" data-code="g.name()">1-acylglycerol-3-phosphate O-acyltransferase 2<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry.

## Normal function

ai-gene-review gives AGPAT2's core molecular function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">1-acylglycerol-3-phosphate O-acyltransferase activity<span class="method"></span></span>,
acting in
<span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">CDP-diacylglycerol biosynthetic process; and phosphatidic acid biosynthetic process<span class="method"></span></span>:
the acylation of lysophosphatidic acid to phosphatidic acid on the way to
triglyceride and phospholipid.

## Causative record

Berardinelli-Seip Congenital Lipodystrophy types AGPAT2 as
<span class="result" data-code="g.relationship('Berardinelli-Seip Congenital Lipodystrophy')">causative<span class="method"></span></span>,
with a <span class="result" data-code="g.variant_origin('Berardinelli-Seip Congenital Lipodystrophy')">germline<span class="method"></span></span>
origin, for its CGL1 subtype. The gene sits on
<span class="result" data-code="g.node('Berardinelli-Seip Congenital Lipodystrophy', 'AGPAT2 acylglycerol synthesis defect')">AGPAT2 acylglycerol synthesis defect<span class="method"></span></span>,
which binds the same 1-acylglycerol-3-phosphate O-acyltransferase activity
ai-gene-review names, decreased.

## ClinGen

ClinGen classifies AGPAT2 for
<span class="result" data-code="g.clingen_diseases()">1<span class="method"></span></span>
disease, lipodystrophy as a whole, which no dismech entry curates
(<span class="result" data-compare="names" data-code="g.clingen_without_entry()">lipodystrophy<span class="method"></span></span>); that lumped disease is
broader than the congenital generalized form, so its tier is not copied onto
the entry.
