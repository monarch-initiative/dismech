import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import { runInNewContext } from "node:vm";

const regionFormatter = readFileSync(
    new URL("../../src/dismech/templates/_genomic_regions.js.j2", import.meta.url),
    "utf8",
);

for (const templateName of ["disorder", "module"]) {
    test(`${templateName} tooltip distinguishes sequence landmarks from targets`, () => {
        const template = readFileSync(
            new URL(`../../src/dismech/templates/${templateName}.html.j2`, import.meta.url),
            "utf8",
        );
        const start = template.indexOf("function formatGeneTerm(gene)");
        const end = template.indexOf('{% include "_genomic_regions.js.j2" %}', start);
        assert.ok(start >= 0 && end > start);
        const contextStart = template.indexOf("function formatGeneticContext(context)", end);
        const contextEnd = template.indexOf("var html = [];", contextStart);
        const context = {
            humanizeEnum: value => value.replaceAll("_", " ").toLowerCase(),
            region: {
                name: "Boundary",
                chromosomal_region: "2q36.1",
                regulatory_element_type: "TAD_BOUNDARY",
                between_genes: [
                    { preferred_term: "EPHA4", term: { id: "hgnc:3388", label: "EPHA4" } },
                    { preferred_term: "PAX3", term: { id: "hgnc:8617", label: "PAX3" } },
                ],
                within_gene: { preferred_term: "Host" },
                overlaps_genes: [{ preferred_term: "Overlapped" }],
                adjacent_to_genes: [{ preferred_term: "Abutted" }],
                description: "Only the boundary is described.",
            },
        };
        runInNewContext(
            template.slice(start, end) + regionFormatter + template.slice(contextStart, contextEnd)
            + "result = formatGeneticContext({affected_regions: [region]});",
            context,
        );
        for (const text of [
            "Affected regions (reference genome): Boundary; 2q36.1; tad boundary",
            "between genes: EPHA4 hgnc:3388, PAX3 hgnc:8617",
            "within gene: Host",
            "overlaps genes: Overlapped",
            "abuts genes (shared boundary): Abutted",
            "Only the boundary is described.",
        ]) assert.ok(context.result.includes(text), context.result);
        assert.ok(!context.result.includes("Regulatory target"));
    });
}
