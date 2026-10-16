/* Pathograph "Group by" (#14539): collapse sets of nodes into super-nodes.

   Collapsing happens here, in the client, on a copy of the payload. graph.py's
   output is never changed, so every member node and its evidence stays one
   expand away, and the exports (CX2, KGX) are unaffected.

   This file is plain JavaScript with no Jinja syntax, so the page inlines it
   with an include and tests/test_pathograph_grouping.py loads it under node. */
var PathographGrouping = (function() {
    var MODES = [
        {key: "none", label: "None"},
        {key: "phenotype_system", label: "Phenotype system"},
        {key: "treatment_target", label: "Treatment target"},
        {key: "module", label: "Mechanism module"},
        {key: "chain", label: "Linear chains"}
    ];

    /* Predicates that explain a phenotype (qc_plugins.CAUSAL_PREDICATES). A
       phenotype reached only by a treatment or readout edge is not explained. */
    var CAUSAL_PREDICATES = {causes: true, leads_to: true, triggers: true, exacerbates: true};

    /* A group needs at least two members, and grouping stops before the graph
       shrinks below MIN_VISIBLE_NODES nodes or MIN_KEPT_FRACTION of its nodes,
       so the main chains stay readable rather than folding into two boxes. The
       mechanism backbone (pathophysiology nodes) is held to the same floor. */
    var MIN_GROUP_SIZE = 2;
    var MIN_VISIBLE_NODES = 3;
    var MIN_KEPT_FRACTION = 1 / 3;
    var GROUP_ID_PREFIX = "__group__:";

    function modeLabel(mode) {
        for (var i = 0; i < MODES.length; i++) {
            if (MODES[i].key === mode) return MODES[i].label;
        }
        return mode;
    }

    /* Orphan targets signal a curation error, so they are never swallowed. */
    function isGroupable(node) {
        return !!node && !node.is_orphan && node.node_type !== "orphan" && node.node_type !== "unknown";
    }

    function groupKeys(node) {
        return (node && node.group_keys) || {};
    }

    function humanizeModule(stem) {
        var text = String(stem).replace(/_/g, " ");
        return text.charAt(0).toUpperCase() + text.slice(1);
    }

    function neighbourSets(data) {
        var preds = {}, succs = {};
        data.nodes.forEach(function(n) { preds[n.id] = {}; succs[n.id] = {}; });
        data.edges.forEach(function(e) {
            if (succs[e.source]) succs[e.source][e.target] = true;
            if (preds[e.target]) preds[e.target][e.source] = true;
        });
        return {preds: preds, succs: succs};
    }

    function explainedPhenotypes(data) {
        var explained = {};
        data.edges.forEach(function(e) {
            if (CAUSAL_PREDICATES[e.predicate]) explained[e.target] = true;
        });
        return explained;
    }

    function bucket(nodes, keyFn) {
        var buckets = {}, order = [];
        nodes.forEach(function(n) {
            var key = keyFn(n);
            if (!key) return;
            if (!buckets[key]) { buckets[key] = []; order.push(key); }
            buckets[key].push(n.id);
        });
        return order.map(function(key) { return {key: key, members: buckets[key]}; });
    }

    function phenotypeSystemGroups(data) {
        var phenotypes = data.nodes.filter(function(n) {
            return n.node_type === "phenotype" && isGroupable(n);
        });
        return bucket(phenotypes, function(n) { return groupKeys(n).phenotype_system; })
            .map(function(g) {
                return {key: g.key, label: g.key + " phenotypes", members: g.members};
            });
    }

    function treatmentTargetGroups(data) {
        var nb = neighbourSets(data);
        var treatments = data.nodes.filter(function(n) {
            return n.node_type === "treatment" && isGroupable(n);
        });
        return bucket(treatments, function(n) {
            var targets = Object.keys(nb.succs[n.id] || {}).sort();
            return targets.length ? JSON.stringify(targets) : null;
        }).map(function(g) {
            var targets = JSON.parse(g.key);
            var shown = targets.length > 2 ? targets.slice(0, 2).join(", ") + ", …" : targets.join(", ");
            return {key: g.key, label: "Treatments → " + shown, members: g.members};
        });
    }

    function moduleGroups(data) {
        var mechanisms = data.nodes.filter(function(n) {
            return n.node_type === "pathophysiology" && isGroupable(n);
        });
        return bucket(mechanisms, function(n) {
            var modules = groupKeys(n).modules;
            return modules && modules.length ? modules[0] : null;
        }).map(function(g) {
            return {key: g.key, label: humanizeModule(g.key) + " module", members: g.members};
        });
    }

    /* Maximal runs of nodes with exactly one predecessor and one successor,
       followed predecessor to successor. Branch points and the chain's ends stay
       visible, so the collapsed run reads "A -> ... -> D (n steps)" in place. */
    function chainGroups(data) {
        var nb = neighbourSets(data);
        var byId = {};
        data.nodes.forEach(function(n) { byId[n.id] = n; });
        function single(map) {
            var keys = Object.keys(map);
            return keys.length === 1 ? keys[0] : null;
        }
        function linear(id) {
            var n = byId[id];
            if (!isGroupable(n)) return false;
            var p = single(nb.preds[id]), s = single(nb.succs[id]);
            return !!p && !!s && p !== id && s !== id;
        }
        var used = {}, groups = [];
        data.nodes.forEach(function(n) {
            if (used[n.id] || !linear(n.id)) return;
            /* Walk back to the start of the run; stop on a cycle. */
            var start = n.id, seen = {};
            seen[start] = true;
            while (true) {
                var p = single(nb.preds[start]);
                if (!linear(p) || seen[p] || used[p]) break;
                seen[p] = true;
                start = p;
            }
            var run = [], cur = start, inRun = {};
            while (cur && linear(cur) && !inRun[cur] && !used[cur]) {
                run.push(cur);
                inRun[cur] = true;
                cur = single(nb.succs[cur]);
            }
            run.forEach(function(id) { used[id] = true; });
            if (run.length >= MIN_GROUP_SIZE) {
                groups.push({
                    key: run[0],
                    label: run[0] + " → … → " + run[run.length - 1] + " (" + run.length + " steps)",
                    members: run
                });
            }
        });
        return groups;
    }

    function candidateGroups(data, mode) {
        var groups;
        if (mode === "phenotype_system") groups = phenotypeSystemGroups(data);
        else if (mode === "treatment_target") groups = treatmentTargetGroups(data);
        else if (mode === "module") groups = moduleGroups(data);
        else if (mode === "chain") groups = chainGroups(data);
        else groups = [];
        groups = groups.filter(function(g) { return g.members.length >= MIN_GROUP_SIZE; });
        groups.forEach(function(g) { g.id = GROUP_ID_PREFIX + mode + ":" + g.key; });
        /* Largest first, so the floor below spends its budget on the biggest wins. */
        groups.sort(function(a, b) {
            return b.members.length - a.members.length || (a.label < b.label ? -1 : a.label > b.label ? 1 : 0);
        });
        return groups;
    }

    function edgeStyleKey(e) {
        return [
            e.predicate || "",
            e.is_orphan ? "orphan" : "",
            (e.hypothesis_groups || []).slice().sort().join(",")
        ].join("|");
    }

    /* Build the drawn graph for a mode. `expanded` holds the ids of groups the
       reader has opened. Returns {nodes, edges, groups, skipped, ...}. */
    function applyGrouping(data, mode, expanded) {
        expanded = expanded || {};
        var byId = {};
        data.nodes.forEach(function(n) { byId[n.id] = n; });
        var candidates = candidateGroups(data, mode);
        var total = data.nodes.length;
        var floor = Math.max(MIN_VISIBLE_NODES, Math.ceil(total * MIN_KEPT_FRACTION));
        var mechanismTotal = data.nodes.filter(function(n) { return n.node_type === "pathophysiology"; }).length;
        var mechanismFloor = Math.min(mechanismTotal, Math.max(MIN_VISIBLE_NODES, Math.ceil(mechanismTotal * MIN_KEPT_FRACTION)));

        var visible = total, visibleMechanisms = mechanismTotal;
        var applied = [], skipped = [], expandedGroups = [];
        candidates.forEach(function(g) {
            if (expanded[g.id]) { expandedGroups.push(g); return; }
            var saved = g.members.length - 1;
            var mechanismMembers = g.members.filter(function(id) { return byId[id].node_type === "pathophysiology"; }).length;
            var mechanismSaved = mechanismMembers ? mechanismMembers - 1 : 0;
            if (visible - saved < floor || visibleMechanisms - mechanismSaved < mechanismFloor) {
                skipped.push(g);
                return;
            }
            visible -= saved;
            visibleMechanisms -= mechanismSaved;
            applied.push(g);
        });

        var explained = explainedPhenotypes(data);
        var repOf = {};
        var groupNodes = applied.map(function(g) {
            var members = g.members.map(function(id) { return byId[id]; });
            var types = {};
            members.forEach(function(m) { types[m.node_type] = true; repOf[m.id] = g.id; });
            var first = members[0];
            var unexplained = members.filter(function(m) {
                return m.node_type === "phenotype" && !explained[m.id];
            }).map(function(m) { return m.id; });
            return {
                id: g.id,
                label: g.label,
                node_type: Object.keys(types).length === 1 ? first.node_type : "pathophysiology",
                color: first.color,
                is_orphan: false,
                is_group: true,
                group_mode: mode,
                members: members,
                unexplained: unexplained,
                internal_edges: 0
            };
        });
        var groupById = {};
        groupNodes.forEach(function(g) { groupById[g.id] = g; });

        var nodes = data.nodes.filter(function(n) { return !repOf[n.id]; }).concat(groupNodes);

        var edges = [], merged = {};
        data.edges.forEach(function(e) {
            var s = repOf[e.source] || e.source, t = repOf[e.target] || e.target;
            if (s === t && (groupById[s])) { groupById[s].internal_edges += 1; return; }
            if (s === e.source && t === e.target) { edges.push(e); return; }
            var key = s + "\u0000" + t + "\u0000" + edgeStyleKey(e);
            var m = merged[key];
            if (!m) {
                m = {};
                for (var k in e) { if (Object.prototype.hasOwnProperty.call(e, k)) m[k] = e[k]; }
                m.source = s;
                m.target = t;
                m.multiplicity = 0;
                m.merged = [];
                merged[key] = m;
                edges.push(m);
            }
            m.multiplicity += 1;
            m.merged.push(e);
        });

        return {
            mode: mode,
            nodes: nodes,
            edges: edges,
            groups: groupNodes,
            skipped: skipped,
            expanded: expandedGroups,
            candidate_count: candidates.length
        };
    }

    /* Drawn-edge count is the complexity the reader sees; node count breaks ties. */
    function complexity(view) {
        return view.edges.length * 10000 + view.nodes.length;
    }

    /* Which mode to show first. Off unless the graph has more edges than the
       knowledge-base mean; then the mode that removes the most drawn edges. */
    function chooseDefaultMode(data, meanEdgeCount) {
        if (meanEdgeCount == null || !(data.edges.length > meanEdgeCount)) return "none";
        var base = complexity({nodes: data.nodes, edges: data.edges});
        var best = "none", bestScore = base;
        MODES.forEach(function(m) {
            if (m.key === "none") return;
            var view = applyGrouping(data, m.key, {});
            if (!view.groups.length) return;
            var score = complexity(view);
            if (score < bestScore) { best = m.key; bestScore = score; }
        });
        return best;
    }

    return {
        MODES: MODES,
        CAUSAL_PREDICATES: CAUSAL_PREDICATES,
        MIN_VISIBLE_NODES: MIN_VISIBLE_NODES,
        modeLabel: modeLabel,
        candidateGroups: candidateGroups,
        applyGrouping: applyGrouping,
        chooseDefaultMode: chooseDefaultMode
    };
})();

if (typeof module !== "undefined" && module.exports) module.exports = PathographGrouping;
