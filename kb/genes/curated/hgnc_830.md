---
hgnc_id: hgnc:830
symbol: ATP5F1B
status: DRAFT
---

# ATP5F1B across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:830")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ATP5F1B<span class="method"></span></span>** (<span class="result" data-code="g.name()">ATP synthase F1 subunit beta<span class="method"></span></span>) is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span> disorder entry.

## Normal function

ATP5F1B is the beta subunit of the F1 catalytic head of mitochondrial ATP synthase; the three
beta subunits carry the catalytic nucleotide-binding sites whose rotation-driven conformational
changes make ATP. ai-gene-review gives its core molecular function as
<span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">ATP binding<span class="method"></span></span>,
contributing to
<span class="result" data-compare="names" data-code="g.core_function_terms('contributes_to_molecular_function')">proton-transporting ATP synthase activity, rotational mechanism<span class="method"></span></span>
in the
<span class="result" data-compare="names" data-code="g.core_function_terms('in_complex')">proton-transporting ATP synthase complex<span class="method"></span></span>.

## Records by relationship type

Hypermetabolism Due To Uncoupled Mitochondrial Oxidative Phosphorylation 2 types ATP5F1B as
<span class="result" data-code="g.relationship('Hypermetabolism Due To Uncoupled Mitochondrial Oxidative Phosphorylation 2')">unknown<span class="method"></span></span>,
with variant origin
<span class="result" data-code="g.variant_origin('Hypermetabolism Due To Uncoupled Mitochondrial Oxidative Phosphorylation 2')">de novo<span class="method"></span></span>:
the entry rests on one pair of twins and no ClinGen classification. The gene sits on
<span class="result" data-code="g.node('Hypermetabolism Due To Uncoupled Mitochondrial Oxidative Phosphorylation 2', 'ATP5F1B Beta Subunit Gamma-Stalk Interface Disruption')">ATP5F1B Beta Subunit Gamma-Stalk Interface Disruption<span class="method"></span></span>,
recorded as
<span class="result" data-code="g.functional_impact('Hypermetabolism Due To Uncoupled Mitochondrial Oxidative Phosphorylation 2')">dominant negative<span class="method"></span></span>,
which binds the rotational ATP synthase activity as decreased: the variant uncouples respiration
from ATP synthesis rather than removing the subunit.

## Where the layers agree and disagree

The KB node carries the holoenzyme activity and no process term, so the layers share
<span class="result" data-code="len(g.shared_processes())">0<span class="method"></span></span>
process terms by exact identifier. ClinGen classifies ATP5F1B for
<span class="result" data-code="g.clingen_diseases()">0<span class="method"></span></span>
diseases.
