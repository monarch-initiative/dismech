// Minimal, dependency-free tests for the dismech-curator extension logic.
// Run with:  node extension/test/run.mjs
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import assert from "node:assert/strict";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const here = dirname(fileURLToPath(import.meta.url));
const {
  buildIssue,
  prefilledUrl,
  titleOnlyUrl,
  normalizeDiseaseLabel,
  dupSearchUrl,
  MAX_PREFILL_URL,
} = require(join(here, "..", "issue.js"));

let passed = 0;
const test = (name, fn) => {
  fn();
  passed++;
  console.log("  ok -", name);
};

// ---- Tiny DOM shim so we can exercise extract.js under node ----------------
function makeElement(tag, attrs = {}, textContent = "") {
  return {
    tag,
    attrs,
    textContent,
    getAttribute: (k) => (k in attrs ? attrs[k] : null),
    get href() {
      return attrs.href || "";
    },
  };
}
function matchSingle(el, sel) {
  const m = sel
    .trim()
    .match(/^([a-z0-9]+)(?:\[([a-z-]+)="([^"]*)"(?:\s*i)?\])?$/i);
  if (!m) return false;
  const [, tag, attr, val] = m;
  if (el.tag.toLowerCase() !== tag.toLowerCase()) return false;
  if (!attr) return true;
  const got = el.attrs[attr];
  return got != null && String(got).toLowerCase() === val.toLowerCase();
}
function makeDoc({ metas = [], title = "", h1 = "", canonical = "" } = {}) {
  const els = [];
  for (const m of metas) els.push(makeElement("meta", m, ""));
  if (h1) els.push(makeElement("h1", {}, h1));
  if (canonical) els.push(makeElement("link", { rel: "canonical", href: canonical }));
  const match = (sel) =>
    els.filter((el) => sel.split(",").some((s) => matchSingle(el, s)));
  return {
    title,
    querySelector: (sel) => match(sel)[0] || null,
    querySelectorAll: (sel) => match(sel),
  };
}
function runExtract({ url, doc, selection = "" }) {
  const u = new URL(url);
  globalThis.document = doc;
  globalThis.location = { href: url, hostname: u.hostname, pathname: u.pathname };
  globalThis.window = { getSelection: () => selection };
  const src = readFileSync(join(here, "..", "extract.js"), "utf8");
  return (0, eval)(src);
}

const SETTINGS = {
  owner: "monarch-initiative",
  repo: "dismech",
  trackerIssue: "1079",
  diseaseLabels: "curation,enhancement",
  paperLabels: "curation",
};

console.log("extract.js:");

test("PubMed page → PMID + kind=paper", () => {
  const meta = runExtract({
    url: "https://pubmed.ncbi.nlm.nih.gov/21376230/",
    doc: makeDoc({
      metas: [
        { name: "citation_pmid", content: "21376230" },
        { name: "citation_doi", content: "10.1016/j.cell.2011.02.013" },
        { name: "citation_title", content: "Hallmarks of Cancer: The Next Generation" },
        { name: "citation_journal_title", content: "Cell" },
        { name: "citation_author", content: "Hanahan D" },
        { name: "citation_author", content: "Weinberg RA" },
      ],
    }),
    selection: "Cancer is a disease of the genome.",
  });
  assert.equal(meta.kind, "paper");
  assert.equal(meta.ids.pmid, "21376230");
  assert.equal(meta.ids.doi, "10.1016/j.cell.2011.02.013");
  assert.match(meta.title, /Hallmarks of Cancer/);
  assert.equal(meta.authors.length, 2);
  assert.match(meta.selection, /disease of the genome/);
});

test("Monarch disease page → MONDO + kind=disease", () => {
  const meta = runExtract({
    url: "https://monarchinitiative.org/MONDO:0007947",
    doc: makeDoc({
      metas: [{ property: "og:title", content: "Marfan syndrome" }],
      title: "Marfan syndrome (MONDO:0007947)",
    }),
  });
  assert.equal(meta.kind, "disease");
  assert.equal(meta.ids.mondo, "MONDO:0007947");
});

test("OMIM entry page → OMIM id", () => {
  const meta = runExtract({
    url: "https://www.omim.org/entry/154700",
    doc: makeDoc({ title: "# 154700 MARFAN SYNDROME; MFS" }),
  });
  assert.equal(meta.kind, "disease");
  assert.equal(meta.ids.omim, "OMIM:154700");
});

test("doi.org resolver URL → DOI + kind=paper", () => {
  const meta = runExtract({
    url: "https://doi.org/10.1038/s41586-020-2649-2",
    doc: makeDoc({ title: "Array programming with NumPy" }),
  });
  assert.equal(meta.kind, "paper");
  assert.equal(meta.ids.doi, "10.1038/s41586-020-2649-2");
});

test("unrecognized page → kind=unknown", () => {
  const meta = runExtract({
    url: "https://example.com/some/article",
    doc: makeDoc({ title: "Some article" }),
  });
  assert.equal(meta.kind, "unknown");
  assert.deepEqual(meta.ids, {});
});

test("modern Orphanet URL → ORPHA id + kind=disease", () => {
  const meta = runExtract({
    url: "https://www.orpha.net/en/disease/detail/558",
    doc: makeDoc({ title: "Orphanet: Marfan syndrome" }),
  });
  assert.equal(meta.kind, "disease");
  assert.equal(meta.ids.orpha, "ORPHA:558");
});

test("legacy Orphanet Expert= URL still works", () => {
  const meta = runExtract({
    url: "https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=558",
    doc: makeDoc({ title: "Orphanet: Marfan syndrome" }),
  });
  assert.equal(meta.ids.orpha, "ORPHA:558");
});

test("URL with a bare percent sign does not abort extraction", () => {
  const meta = runExtract({
    url: "https://pubmed.ncbi.nlm.nih.gov/21376230/?q=50%off",
    doc: makeDoc({ metas: [{ name: "citation_pmid", content: "21376230" }] }),
  });
  assert.equal(meta.kind, "paper");
  assert.equal(meta.ids.pmid, "21376230");
});

console.log("issue.js:");

test("disease issue title & body", () => {
  const meta = {
    kind: "disease",
    ids: { mondo: "MONDO:0007947" },
    title: "Marfan syndrome",
    url: "https://monarchinitiative.org/MONDO:0007947",
    selection: "",
  };
  const issue = buildIssue(meta, SETTINGS);
  assert.equal(issue.title, "Curate Marfan syndrome (MONDO:0007947)");
  assert.match(issue.body, /part of #1079/);
  assert.match(issue.body, /kb\/disorders\//);
  assert.equal(issue.labels, "curation,enhancement");
});

test("disease titles are normalized from noisy page titles", () => {
  const cases = [
    ["# 154700 MARFAN SYNDROME; MFS", "OMIM:154700", "MARFAN SYNDROME; MFS"],
    ["MONDO:0007947 - Marfan syndrome | OLS", "MONDO:0007947", "Marfan syndrome"],
    ["Orphanet: Marfan syndrome", "ORPHA:558", "Marfan syndrome"],
    ["Marfan syndrome (MONDO:0007947)", "MONDO:0007947", "Marfan syndrome"],
  ];
  for (const [raw, , expected] of cases) {
    assert.equal(normalizeDiseaseLabel(raw), expected, `normalize ${raw}`);
  }
  // End-to-end through buildIssue: id is never duplicated in the title.
  const issue = buildIssue(
    { kind: "disease", ids: { mondo: "MONDO:0007947" }, title: "Marfan syndrome (MONDO:0007947)", url: "https://x", selection: "" },
    SETTINGS
  );
  assert.equal(issue.title, "Curate Marfan syndrome (MONDO:0007947)");
});

test("disease body carries a duplicate-check search link", () => {
  const issue = buildIssue(
    { kind: "disease", ids: { mondo: "MONDO:0007947" }, title: "Marfan syndrome", url: "https://x", selection: "" },
    SETTINGS
  );
  assert.match(issue.body, /Check for existing issues:/);
  assert.match(issue.body, /issues\?q=/);
  assert.match(issue.body, /MONDO/);
});

test("paper issue includes fetch-reference PMID command", () => {
  const meta = {
    kind: "paper",
    ids: { pmid: "21376230", doi: "10.1016/j.cell.2011.02.013" },
    title: "Hallmarks of Cancer",
    journal: "Cell",
    year: "2011",
    authors: ["Hanahan D", "Weinberg RA"],
    url: "https://pubmed.ncbi.nlm.nih.gov/21376230/",
    selection: "",
  };
  const issue = buildIssue(meta, SETTINGS);
  assert.match(issue.title, /^Curate from literature:/);
  assert.match(issue.body, /just fetch-reference PMID:21376230/);
  assert.match(issue.body, /exact-quote/);
  assert.match(issue.body, /Check for existing issues:.*issues\?q=/);
  assert.equal(issue.labels, "curation");
});

test("selection is rendered as a blockquote", () => {
  const issue = buildIssue(
    { kind: "unknown", ids: {}, title: "x", url: "https://e.com", selection: "line one\nline two" },
    SETTINGS
  );
  assert.match(issue.body, /> line one/);
  assert.match(issue.body, /> line two/);
});

test("prefilledUrl encodes title, body, labels", () => {
  const url = prefilledUrl(SETTINGS, "Curate X (MONDO:1)", "hello world", "a,b");
  const u = new URL(url);
  assert.equal(u.pathname, "/monarch-initiative/dismech/issues/new");
  assert.equal(u.searchParams.get("title"), "Curate X (MONDO:1)");
  assert.equal(u.searchParams.get("body"), "hello world");
  assert.equal(u.searchParams.get("labels"), "a,b");
});

test("long bodies overflow prefill limit; titleOnlyUrl is the fallback", () => {
  const huge = "x".repeat(20000);
  assert.ok(prefilledUrl(SETTINGS, "T", huge, "a").length > MAX_PREFILL_URL);
  const url = titleOnlyUrl(SETTINGS, "T", "a");
  const u = new URL(url);
  assert.equal(u.searchParams.get("title"), "T");
  assert.equal(u.searchParams.get("body"), "");
  assert.ok(url.length <= MAX_PREFILL_URL);
});

test("dupSearchUrl builds an is:issue search for the identifier", () => {
  const url = dupSearchUrl(SETTINGS, "MONDO:0007947");
  const u = new URL(url);
  assert.equal(u.pathname, "/monarch-initiative/dismech/issues");
  assert.equal(u.searchParams.get("q"), "is:issue MONDO:0007947");
});

console.log(`\n${passed} passed`);
