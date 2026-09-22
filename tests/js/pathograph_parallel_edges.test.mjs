import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import { runInNewContext } from "node:vm";

// Model graphlib's named-edge storage contract without downloading browser
// libraries in CI. Real Dagre geometry is independent of this wiring test.
class Graph {
    constructor({ multigraph = false } = {}) {
        this.multigraph = multigraph;
        this.edges = new Map();
    }
    setGraph() {}
    setDefaultEdgeLabel(factory) { this.defaultLabel = factory; }
    setNode() {}
    key(source, target, name) {
        if (name !== undefined && !this.multigraph) {
            throw new Error("Named edges require a multigraph");
        }
        return JSON.stringify([source, target, name]);
    }
    setEdge(source, target, label, name) {
        this.edges.set(this.key(source, target, name), label || this.defaultLabel());
    }
    edge(source, target, name) {
        return this.edges.get(this.key(source, target, name));
    }
}

class Element {
    constructor(tag) {
        this.tag = tag;
        this.attributes = {};
        this.children = [];
    }
    append(tag) {
        const child = new Element(tag);
        this.children.push(child);
        return child;
    }
    attr(name, value) { this.attributes[name] = value; return this; }
    text(value) { this.content = value; return this; }
}

for (const templateName of ["disorder", "module"]) {
    test(`${templateName} routes parallel roles separately and retains their titles`, () => {
        const template = readFileSync(
            new URL(`../../src/dismech/templates/${templateName}.html.j2`, import.meta.url),
            "utf8",
        );
        const layoutStart = template.indexOf("var g = new dagre.graphlib.Graph(");
        const drawStart = template.indexOf('var edgesG = rootG.append("g")');
        assert.ok(layoutStart >= 0 && drawStart >= 0);
        const layout = template.slice(layoutStart, template.indexOf("var graphInfo", layoutStart));
        const draw = template.slice(drawStart, template.indexOf("function drawNodeShape", drawStart));
        const rootG = new Element("g");
        const data = {
            nodes: [{ id: "SV" }, { id: "LMNB1" }],
            edges: [
                { source: "SV", target: "LMNB1", predicate: "variant_of", description: "Sequence overlap" },
                { source: "SV", target: "LMNB1", predicate: "has_regulatory_target", description: "Expression target" },
                // Distinct assertions may also share a predicate.
                { source: "SV", target: "LMNB1", predicate: "variant_of", description: "Additional assertion" },
            ],
        };
        const line = points => JSON.stringify(points);
        line.x = line.y = line.curve = () => line;
        runInNewContext(layout + draw, {
            data,
            rootG,
            dagre: {
                graphlib: { Graph },
                layout(graph) {
                    let index = 0;
                    for (const edge of graph.edges.values()) {
                        edge.points = [{ x: 0, y: index }, { x: 10, y: index }];
                        index++;
                    }
                },
            },
            d3: { line: () => line },
            edgeStroke: () => "gray",
            edgeDashArray: () => "none",
            edgeMarker: () => "arrow",
            hasHypothesisGroups: () => false,
            edgeTitle: edge => `${edge.predicate}: ${edge.description}`,
        });
        const paths = rootG.children[0].children;
        assert.equal(paths.length, data.edges.length);
        assert.equal(new Set(paths.map(path => path.attributes.d)).size, data.edges.length);
        assert.deepEqual(paths.map(path => path.attributes["data-predicate"]), data.edges.map(edge => edge.predicate));
        assert.deepEqual(
            paths.map(path => path.children.find(child => child.tag === "title").content),
            data.edges.map(edge => `${edge.predicate}: ${edge.description}`),
        );
    });
}
