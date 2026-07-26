"use strict";

const DEFAULTS = {
  owner: "monarch-initiative",
  repo: "dismech",
  trackerIssue: "1079",
  diseaseLabels: "curation,enhancement",
  paperLabels: "curation",
  mode: "url",
};

const $ = (id) => document.getElementById(id);
const SYNC_KEYS = ["owner", "repo", "trackerIssue", "diseaseLabels", "paperLabels", "mode"];

async function load() {
  const sync = await chrome.storage.sync.get(DEFAULTS);
  const { githubToken } = await chrome.storage.local.get({ githubToken: "" });
  for (const k of SYNC_KEYS) {
    if (k === "mode") continue;
    $(k).value = sync[k];
  }
  document.querySelector(`input[name="mode"][value="${sync.mode}"]`).checked = true;
  $("githubToken").value = githubToken;
}

async function save() {
  const sync = {};
  for (const k of SYNC_KEYS) {
    if (k === "mode") continue;
    sync[k] = $(k).value.trim();
  }
  sync.mode = document.querySelector('input[name="mode"]:checked').value;
  await chrome.storage.sync.set(sync);
  await chrome.storage.local.set({ githubToken: $("githubToken").value.trim() });

  const saved = $("saved");
  saved.hidden = false;
  setTimeout(() => (saved.hidden = true), 1500);
}

$("save").addEventListener("click", save);
load();
