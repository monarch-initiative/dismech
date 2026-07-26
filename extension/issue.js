// Pure issue-template logic — no DOM, no chrome APIs — so it can be unit-tested
// under node. Exposed as globalThis.DismechIssue in the browser and via
// module.exports under node.
(function (root) {
  "use strict";

  const pmidUrl = (id) => `https://pubmed.ncbi.nlm.nih.gov/${id}/`;
  const doiUrl = (id) => `https://doi.org/${id}`;
  const pmcUrl = (id) => `https://www.ncbi.nlm.nih.gov/pmc/articles/${id}/`;
  const mondoUrl = (id) => `https://monarchinitiative.org/${id}`;
  const omimUrl = (id) => `https://omim.org/entry/${id.replace("OMIM:", "")}`;
  const orphaUrl = (id) =>
    `https://www.orpha.net/en/disease/detail/${id.replace("ORPHA:", "")}`;

  function truncate(s, n) {
    s = (s || "").trim();
    return s.length > n ? s.slice(0, n - 1).trimEnd() + "…" : s;
  }

  function selectionBlock(sel) {
    if (!sel) return "";
    const quoted = sel
      .split("\n")
      .map((l) => "> " + l)
      .join("\n");
    return `\n**Highlighted on page:**\n\n${quoted}\n`;
  }

  function buildIssue(meta, settings) {
    const ids = meta.ids || {};
    const tracker = settings.trackerIssue
      ? `\nTracker: part of #${settings.trackerIssue}.\n`
      : "";

    if (meta.kind === "disease") {
      const primary = ids.mondo || ids.omim || ids.orpha || ids.doid;
      const label = meta.title || primary || "disease";
      const url = ids.mondo
        ? mondoUrl(ids.mondo)
        : ids.omim
        ? omimUrl(ids.omim)
        : ids.orpha
        ? orphaUrl(ids.orpha)
        : meta.url;

      const idLines = [
        ids.mondo && `- MONDO: [${ids.mondo}](${mondoUrl(ids.mondo)})`,
        ids.omim && `- OMIM: [${ids.omim}](${omimUrl(ids.omim)})`,
        ids.orpha && `- ORPHA: [${ids.orpha}](${orphaUrl(ids.orpha)})`,
        ids.doid && `- DOID: ${ids.doid}`,
      ]
        .filter(Boolean)
        .join("\n");

      const title = `Curate ${truncate(label, 90)} (${primary})`;
      const body =
        `Curate a dismech entry for **${label}** ([${primary}](${url})).\n\n` +
        `Requested via the [dismech curator](https://github.com/${settings.owner}/${settings.repo}/tree/main/extension) browser extension.\n\n` +
        `**Identifiers:**\n${idLines}\n\n` +
        `**Source page:** ${meta.url}\n` +
        selectionBlock(meta.selection) +
        `\n### Curation checklist\n` +
        `- [ ] Confirm the disease is not already in \`kb/disorders/\` (check MONDO id, label, synonyms)\n` +
        `- [ ] Draft the entry with \`/curate\` or the \`initiate-new-disorder-creation\` skill\n` +
        `- [ ] Evidence items use exact-quote PMID snippets and pass \`just validate-references\`\n` +
        tracker;

      return { title, body, labels: settings.diseaseLabels };
    }

    if (meta.kind === "paper") {
      const title = `Curate from literature: ${truncate(meta.title || meta.url, 80)}`;
      const bits = [
        meta.title && `- **Title:** ${meta.title}`,
        ids.pmid &&
          `- **PMID:** [${ids.pmid}](${pmidUrl(ids.pmid)}) \`PMID:${ids.pmid}\``,
        ids.doi && `- **DOI:** [${ids.doi}](${doiUrl(ids.doi)})`,
        ids.pmcid && `- **PMCID:** [${ids.pmcid}](${pmcUrl(ids.pmcid)})`,
        meta.journal &&
          `- **Journal:** ${meta.journal}${meta.year ? " (" + meta.year + ")" : ""}`,
        meta.authors &&
          meta.authors.length &&
          `- **Authors:** ${meta.authors.slice(0, 6).join(", ")}${
            meta.authors.length > 6 ? ", et al." : ""
          }`,
        `- **Source page:** ${meta.url}`,
      ]
        .filter(Boolean)
        .join("\n");

      const fetchCmd = ids.pmid
        ? `\`just fetch-reference PMID:${ids.pmid}\``
        : ids.doi
        ? `\`just fetch-reference doi:${ids.doi}\``
        : "`just fetch-reference <ID>`";

      const body =
        `Curate dismech evidence from this paper.\n\n` +
        `${bits}\n` +
        selectionBlock(meta.selection) +
        `\n### Curation checklist\n` +
        `- [ ] Identify the target disorder(s) in \`kb/disorders/\`\n` +
        `- [ ] Extract **exact-quote** snippet(s) for each mechanistic claim (verbatim from the abstract — no paraphrase)\n` +
        `- [ ] ${fetchCmd} then \`just validate-references\`\n` +
        `\nRequested via the dismech curator browser extension.\n` +
        tracker;

      return { title, body, labels: settings.paperLabels };
    }

    // unknown
    const title = `Curation lead: ${truncate(meta.title || meta.url, 80)}`;
    const body =
      `Captured from a page with no recognized paper or disease identifier.\n\n` +
      `- **Title:** ${meta.title || "(none)"}\n` +
      `- **Source page:** ${meta.url}\n` +
      selectionBlock(meta.selection) +
      `\nRequested via the dismech curator browser extension.\n` +
      tracker;
    return { title, body, labels: settings.paperLabels };
  }

  function prefilledUrl(settings, title, body, labels) {
    const p = new URLSearchParams();
    p.set("title", title);
    p.set("body", body);
    if (labels) p.set("labels", labels);
    return `https://github.com/${settings.owner}/${settings.repo}/issues/new?${p.toString()}`;
  }

  const api = { buildIssue, prefilledUrl, truncate, selectionBlock };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.DismechIssue = api;
})(typeof globalThis !== "undefined" ? globalThis : this);
