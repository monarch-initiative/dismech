"use strict";

const DEFAULTS = {
  owner: "monarch-initiative",
  repo: "dismech",
  trackerIssue: "1079",
  diseaseLabels: "curation,enhancement",
  paperLabels: "curation",
  mode: "url", // "url" (prefilled GitHub form) | "api" (token, one-click)
};

const $ = (id) => document.getElementById(id);
const { buildIssue, prefilledUrl } = globalThis.DismechIssue;

function showStatus(html, cls) {
  const s = $("status");
  s.hidden = false;
  s.className = "status" + (cls ? " " + cls : "");
  s.innerHTML = html;
}

async function getSettings() {
  const sync = await chrome.storage.sync.get(DEFAULTS);
  const { githubToken } = await chrome.storage.local.get({ githubToken: "" });
  return { ...sync, githubToken };
}

async function getActiveTab() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  return tab;
}

async function extractFromTab(tabId) {
  const results = await chrome.scripting.executeScript({
    target: { tabId },
    files: ["extract.js"],
  });
  return results && results[0] ? results[0].result : null;
}

async function createViaApi(settings, title, body, labels) {
  const granted = await chrome.permissions.request({
    origins: ["https://api.github.com/*"],
  });
  if (!granted) throw new Error("Permission for api.github.com was denied.");

  const res = await fetch(
    `https://api.github.com/repos/${settings.owner}/${settings.repo}/issues`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${settings.githubToken}`,
        Accept: "application/vnd.github+json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title,
        body,
        labels: labels
          ? labels.split(",").map((s) => s.trim()).filter(Boolean)
          : [],
      }),
    }
  );
  if (!res.ok) {
    const txt = await res.text();
    throw new Error(`GitHub API ${res.status}: ${txt.slice(0, 200)}`);
  }
  return res.json();
}

let SETTINGS = null;
let META = null;

async function init() {
  $("settings-link").addEventListener("click", (e) => {
    e.preventDefault();
    chrome.runtime.openOptionsPage();
  });

  SETTINGS = await getSettings();
  const tab = await getActiveTab();

  if (
    !tab ||
    !tab.id ||
    /^(chrome|edge|about|chrome-extension):/.test(tab.url || "")
  ) {
    showStatus(
      "Open a paper or disease page (PubMed, DOI, Monarch, OMIM, Orphanet…) then click the extension.",
      "error"
    );
    return;
  }

  try {
    META = await extractFromTab(tab.id);
  } catch (err) {
    showStatus(
      "Couldn't read this page. It may be a restricted page. " +
        (err.message || ""),
      "error"
    );
    return;
  }
  if (!META) {
    showStatus("No metadata could be extracted from this page.", "error");
    return;
  }

  const issue = buildIssue(META, SETTINGS);

  $("form").hidden = false;
  const badge = $("kind-badge");
  badge.textContent = META.kind;
  badge.classList.toggle("unknown", META.kind === "unknown");

  $("id-chips").innerHTML = Object.values(META.ids)
    .map((v) => `<span class="chip">${v}</span>`)
    .join("");

  $("title").value = issue.title;
  $("labels").value = issue.labels;
  $("body").value = issue.body;

  $("mode-note").textContent =
    SETTINGS.mode === "api" && SETTINGS.githubToken
      ? `One-click mode → creates directly in ${SETTINGS.owner}/${SETTINGS.repo}.`
      : `Opens a pre-filled issue form in ${SETTINGS.owner}/${SETTINGS.repo} — review, then submit.`;

  $("copy").addEventListener("click", async () => {
    await navigator.clipboard.writeText($("body").value);
    $("copy").textContent = "Copied";
    setTimeout(() => ($("copy").textContent = "Copy"), 1200);
  });

  $("create").addEventListener("click", onCreate);
}

async function onCreate() {
  const title = $("title").value.trim();
  const body = $("body").value;
  const labels = $("labels").value.trim();
  const btn = $("create");
  btn.disabled = true;

  try {
    if (SETTINGS.mode === "api" && SETTINGS.githubToken) {
      btn.textContent = "Creating…";
      const issue = await createViaApi(SETTINGS, title, body, labels);
      showStatus(
        `Created <a href="${issue.html_url}" target="_blank">#${issue.number}</a>.`,
        "ok"
      );
      chrome.tabs.create({ url: issue.html_url });
    } else {
      chrome.tabs.create({ url: prefilledUrl(SETTINGS, title, body, labels) });
      window.close();
    }
  } catch (err) {
    showStatus("Failed: " + (err.message || err), "error");
    btn.disabled = false;
    btn.textContent = "Create issue";
  }
}

init();
