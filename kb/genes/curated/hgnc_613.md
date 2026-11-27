---
hgnc_id: hgnc:613
symbol: APOE
status: DRAFT
---

# APOE across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:613")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">APOE<span class="method"></span></span>**
(<span class="result" data-code="g.name()">apolipoprotein E<span class="method"></span></span>)
is named by <span class="result" data-code="g.disorder_count()">14<span class="method"></span></span>
disorder entries, more than any other gene in the lipoprotein family. It
encodes apolipoprotein E, the ligand that targets lipoproteins to the LDL
receptor family and carries cholesterol between cells, including in the brain.

## Normal function

ai-gene-review gives APOE's core molecular functions as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">cholesterol transfer activity; and low-density lipoprotein particle receptor binding<span class="method"></span></span>.
The two are the two halves of its work: lipid loading and transport, and
receptor-mediated clearance of the particles it rides on.

## Causative records

Rare structural variants cause two distinctive diseases. The entries that type
APOE as causative include
<span class="result" data-compare="names" data-code="g.includes('Lipoprotein Glomerulopathy', 'Sea-Blue Histiocyte Syndrome', relationship='causative')">Lipoprotein Glomerulopathy; and Sea-Blue Histiocyte Syndrome<span class="method"></span></span>.
Lipoprotein Glomerulopathy places the gene on
<span class="result" data-code="g.node('Lipoprotein Glomerulopathy', 'APOE Variants Near the LDL-Receptor-Binding Region')">APOE Variants Near the LDL-Receptor-Binding Region<span class="method"></span></span>,
and Sea-Blue Histiocyte Syndrome on
<span class="result" data-code="g.node('Sea-Blue Histiocyte Syndrome', 'Defective Macrophage Lipid and Lipoprotein Handling')">Defective Macrophage Lipid and Lipoprotein Handling<span class="method"></span></span>;
both bind LDL particle receptor binding as abnormal rather than simply
decreased.

Familial Hypercholesterolemia records APOE as
<span class="result" data-code="g.relationship('Familial Hypercholesterolemia')">unknown<span class="method"></span></span>:
its one implicated variant, p.(Leu167del), cosegregates with dominant
hypercholesterolemia but is still described as a candidate locus. There the
node
<span class="result" data-code="g.node('Familial Hypercholesterolemia', 'APOE-Related Lipoprotein Clearance Defect')">APOE-Related Lipoprotein Clearance Defect<span class="method"></span></span>
records that VLDL carrying the mutant apoE is taken up more avidly by
hepatocytes, so LDL receptor expression falls.

## Common-allele records

Most entries record the common e2/e3/e4 alleles as risk rather than cause. The
entries typing APOE as a risk factor include
<span class="result" data-compare="names" data-code="g.includes('Alzheimer Disease', 'Cerebral Amyloid Angiopathy', 'Coronary Artery Disease', 'Hyperlipidemia', relationship='risk factor')">Alzheimer Disease; Cerebral Amyloid Angiopathy; Coronary Artery Disease; and Hyperlipidemia<span class="method"></span></span>,
and the susceptibility records include
<span class="result" data-compare="names" data-code="g.includes('Dementia with Lewy Bodies', relationship='susceptibility')">Dementia with Lewy Bodies<span class="method"></span></span>.
In Alzheimer Disease the gene is also wired to
<span class="result" data-code="g.node('Alzheimer Disease', 'Oligodendrocyte and Myelin Dysfunction')">Oligodendrocyte and Myelin Dysfunction<span class="method"></span></span>,
which binds cholesterol transfer activity as decreased for APOE4. The
modifier records include
<span class="result" data-compare="names" data-code="g.includes('Early-Onset Autosomal Dominant Alzheimer Disease', 'Chronic Traumatic Encephalopathy', relationship='modifier')">Early-Onset Autosomal Dominant Alzheimer Disease; and Chronic Traumatic Encephalopathy<span class="method"></span></span>.
Tuberculosis records the gene as
<span class="result" data-code="g.relationship('Tuberculosis')">unknown<span class="method"></span></span>,
on mouse knockout evidence alone.

## ClinGen

ClinGen has classified APOE for
<span class="result" data-code="g.clingen_diseases()">0<span class="method"></span></span>
diseases.
