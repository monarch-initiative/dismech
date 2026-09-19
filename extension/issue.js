// Pure issue-template logic — no DOM, no chrome APIs — so it can be unit-tested
// under node. Exposed as globalThis.DismechIssue in the browser and via
// module.exports under node.
(function (root) {
  "use strict";

  // Single source of truth for extension defaults (also consumed by popup.js
  // and options.js so the values are not duplicated across files).
  const DEFAULTS = {
    owner: "monarch-initiative",
    repo: "dismech",
    trackerIssue: "1079",
    diseaseLabels: "curation,enhancement",
    paperLabels: "curation",
    mode: "url", // "url" (prefilled GitHub form) | "api" (token, one-click)
  };

  // GitHub caps issues/new prefill URLs (~8 KB in practice); past this we fall
  // back to clipboard + an empty form in the popup.
  const MAX_PREFILL_URL = 8000;

  const pmidUrl = (id) => `https://pubmed.ncbi.nlm.nih.gov/${id}/`;
  const doiUrl = (id) => `https://doi.org/${id}`;
  const pmcUrl = (id) => `https://www.ncbi.nlm.nih.gov/pmc/articles/${id}/`;
  const mondoUrl = (id) => `https://monarchinitiative.org/${id}`;
  const omimUrl = (id) => `https://omim.org/entry/${id.replace("OMIM:", "")}`;
  const orphaUrl = (id) =>
    `https://www.orpha.net/en/disease/detail/${id.replace("ORPHA:", "")}`;

  // A GitHub issue-search URL for an identifier, used as a duplicate-check link.
  const dupSearchUrl = (settings, query) =>
    `https://github.com/${settings.owner}/${settings.repo}/issues?q=` +
    encodeURIComponent(`is:issue ${query}`);

  function truncate(s, n) {
    s = (s || "").trim();
    return s.length > n ? s.slice(0, n - 1).trimEnd() + "…" : s;
  }

  // Real disease pages produce noisy titles (OMIM "# 154700 MARFAN SYNDROME;
  // MFS", OLS "MONDO:0007947 - Marfan syndrome | OLS", "Orphanet: …", or a
  // label with the id already parenthesised). Strip those decorations so the
  // issue title stays "Curate <label> (<id>)" like the claim-disease convention.
  function normalizeDiseaseLabel(label) {
    let s = (label || "").replace(/\s+/g, " ").trim();
    s = s.replace(/\s*\|.*$/, "").trim(); // trailing " | Site [| …]" segments
    s = s.replace(/^[#%+*^]\s*\d{4,7}\s+/, "").trim(); // leading OMIM "# 154700 " (also % + * ^)
    s = s.replace(/^Orphanet:\s*/i, "").trim(); // leading "Orphanet: "
    s = s
      .replace(/^(?:MONDO|OMIM|ORPHA|ORPHANET|DOID):\S+\s*[-–—]\s*/i, "")
      .trim(); // leading "MONDO:0007947 - " (e.g. OLS)
    s = s
      .replace(/\s*\((?:MONDO|OMIM|ORPHA|DOID):[^)]*\)\s*$/i, "")
      .trim(); // trailing "(MONDO:…)"
    return s;
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
      const label = normalizeDiseaseLabel(meta.title) || primary || "disease";
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
        `**Check for existing issues:** ${dupSearchUrl(settings, primary)}\n` +
        selectionBlock(meta.selection) +
        `\n### Curation checklist\n` +
        `- [ ] Confirm the disease is not already in \`kb/disorders/\` (check MONDO id, label, synonyms)\n` +
        `- [ ] Draft the entry with \`/curate\` or the \`initiate-new-disorder-creation\` skill\n` +
        `- [ ] Evidence items use exact-quote PMID snippets and pass \`just validate-kb-references\`\n` +
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
        (ids.pmid || ids.doi) &&
          `- **Check for existing issues:** ${dupSearchUrl(
            settings,
            ids.pmid ? `PMID:${ids.pmid}` : ids.doi
          )}`,
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
        `- [ ] ${fetchCmd} then \`just validate-kb-references\`\n` +
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

  // A title-only prefill URL, for the fallback when the full body would blow
  // past GitHub's URL length limit (the popup copies the body to the clipboard).
  function titleOnlyUrl(settings, title, labels) {
    return prefilledUrl(settings, title, "", labels);
  }

  const api = {
    DEFAULTS,
    MAX_PREFILL_URL,
    buildIssue,
    prefilledUrl,
    titleOnlyUrl,
    truncate,
    selectionBlock,
    normalizeDiseaseLabel,
    dupSearchUrl,
  };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.DismechIssue = api;
})(typeof globalThis !== "undefined" ? globalThis : this);
