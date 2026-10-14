---
hgnc_id: hgnc:838
symbol: ATP5F1E
status: DRAFT
---

# ATP5F1E across dismech

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:838")
</code></pre>

</details>

**<span class="result" data-code="g.symbol()">ATP5F1E<span class="method"></span></span>** (<span class="result" data-code="g.name()">ATP synthase F1 subunit epsilon<span class="method"></span></span>) is named by <span class="result" data-code="g.disorder_count()">1<span class="method"></span></span> disorder entry.

## Normal function

ai-gene-review gives ATP5F1E's core molecular function as <span class="result" data-compare="names" data-code="g.core_function_terms('molecular_function')">structural molecule activity<span class="method"></span></span>, contributing to <span class="result" data-compare="names" data-code="g.core_function_terms('contributes_to_molecular_function')">proton-transporting ATP synthase activity, rotational mechanism<span class="method"></span></span> as part of the <span class="result" data-compare="names" data-code="g.core_function_terms('in_complex')">proton-transporting ATP synthase complex<span class="method"></span></span>, and acting in <span class="result" data-compare="names" data-code="g.core_function_terms('directly_involved_in')">proton motive force-driven mitochondrial ATP synthesis<span class="method"></span></span>. The epsilon subunit is a non-catalytic part of the central stalk.

## Causative record

The one entry naming ATP5F1E types it as <span class="result" data-code="g.relationship('Mitochondrial Complex V (ATP Synthase) Deficiency, Nuclear Type 3')">causative<span class="method"></span></span>: <span class="result" data-compare="names" data-code="g.disorders('causative')">Mitochondrial Complex V (ATP Synthase) Deficiency, Nuclear Type 3<span class="method"></span></span>, with variant origin <span class="result" data-code="g.variant_origin('Mitochondrial Complex V (ATP Synthase) Deficiency, Nuclear Type 3')">germline<span class="method"></span></span>. The gene sits on the node <span class="result" data-code="g.node('Mitochondrial Complex V (ATP Synthase) Deficiency, Nuclear Type 3', 'ATP5F1E p.Tyr12Cys Substitution')">ATP5F1E p.Tyr12Cys Substitution<span class="method"></span></span>.

## Where the layers agree and disagree

The KB's gene-bound node carries a molecular function rather than a process, so the layers share <span class="result" data-code="len(g.shared_processes())">0<span class="method"></span></span> GO process terms by exact identifier. ClinGen classifies ATP5F1E for <span class="result" data-code="g.clingen_diseases()">1<span class="method"></span></span> disease, <span class="result" data-compare="names" data-code="g.clingen_without_entry()">mitochondrial disease<span class="method"></span></span>, a lumped grouping with no matching dismech entry.
