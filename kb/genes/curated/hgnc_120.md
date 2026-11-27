---
hgnc_id: hgnc:120
symbol: ACOX2
status: DRAFT
---

# ACOX2 across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:120")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ACOX2<span class="method"></span></span>**
(<span class="result" data-code="g.name()">acyl-CoA oxidase 2<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span>
disorder entry.

## Normal function

ACOX2 is the peroxisomal branched-chain acyl-CoA oxidase. It performs the first,
oxygen-dependent step of beta-oxidation for 2-methyl-branched acyl-CoAs: the C27
bile acid intermediates whose side chain must be shortened to make the C24
primary bile acids, and branched-chain fatty acids such as pristanic acid. It is
the only human acyl-CoA oxidase that acts on the bile acid intermediates, while
ACOX3 also handles the branched-chain fatty acids.

## Disease record

Inborn Disorder of Bile Acid Synthesis records ACOX2 for its BASD Type 6
subtype, congenital bile acid synthesis defect 6, with a
<span class="result" data-code="g.variant_origin('Inborn Disorder of Bile Acid Synthesis')">germline<span class="method"></span></span>
origin. It types the relationship as
<span class="result" data-code="g.relationship('Inborn Disorder of Bile Acid Synthesis')">causative<span class="method"></span></span>,
copying ClinGen's tier for the subtype's own disease term; the entry's notes
also cite the four patient reports. The gene sits on
<span class="result" data-code="g.node('Inborn Disorder of Bile Acid Synthesis', 'Peroxisomal C27 Side-Chain Enzyme Deficiency (ACOX2)')">Peroxisomal C27 Side-Chain Enzyme Deficiency (ACOX2)<span class="method"></span></span>,
which binds the bile acid intermediate oxidase and pristanoyl-CoA oxidase
activities as decreased and feeds the accumulation of C27 intermediates,
mainly trihydroxycholestanoic acid, that the patients show.

## ClinGen

ClinGen classifies ACOX2 for
<span class="result" data-code="g.clingen_diseases()">1<span class="method"></span></span>
disease, congenital bile acid synthesis defect 6, and the entry records that
tier as
<span class="result" data-code="g.clingen('Inborn Disorder of Bile Acid Synthesis')">definitive<span class="method"></span></span>.
