#!/usr/bin/env python3
"""Build self-contained public/index.html from public/data.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "public" / "data.json"
OUT = ROOT / "public" / "index.html"

HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Painel de Monitoramento de AVCB</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<style>
:root {
  --bg: #F4F5F9;
  --card: #FFFFFF;
  --sidebar: #2E2D39;
  --border: #E2E2EC;
  --border2: #BCC1D6;
  --text: #1E1D24;
  --accent: #FFD919;
  --chart2: #C2C6D6;
  --muted: #6B6A76;
}
* { box-sizing: border-box; }
html, body { height: 100%; margin: 0; font-family: Inter, sans-serif; background: var(--bg); color: var(--text); overflow: hidden; }
.app { display: flex; flex-direction: column; height: 100vh; position: relative; }
.header {
  display: flex; align-items: center; gap: 14px; padding: 10px 16px;
  background: var(--card); border-bottom: 1px solid var(--border); flex-shrink: 0; z-index: 20;
}
.header img { height: 28px; }
.header h1 { font-size: 18px; font-weight: 600; margin: 0; flex: 1; }
.btn-menu {
  width: 36px; height: 36px; border: 1px solid var(--border); background: #fff; border-radius: 8px;
  cursor: pointer; color: var(--text); font-size: 16px;
}
.filters-bar {
  display: flex; flex-wrap: wrap; gap: 8px; padding: 8px 16px; background: var(--bg);
  border-bottom: 1px solid var(--border); flex-shrink: 0; z-index: 15; position: relative;
}
.ms {
  position: relative; min-width: 140px;
}
.ms-btn {
  width: 100%; text-align: left; padding: 7px 28px 7px 10px; border: 1px solid var(--border2);
  background: #fff; border-radius: 8px; font-size: 12px; cursor: pointer; position: relative;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.ms-btn::after {
  content: "▾"; position: absolute; right: 8px; top: 50%; transform: translateY(-50%); color: var(--muted);
}
.ms-panel {
  display: none; position: absolute; top: calc(100% + 4px); left: 0; min-width: 220px; max-height: 260px;
  overflow: auto; background: #fff; border: 1px solid var(--border2); border-radius: 10px;
  box-shadow: 0 8px 24px rgba(30,29,36,.12); z-index: 50; padding: 6px;
}
.ms.open .ms-panel { display: block; }
.ms-item {
  display: flex; align-items: center; gap: 8px; padding: 6px 8px; font-size: 12px; border-radius: 6px; cursor: pointer;
}
.ms-item:hover { background: #F4F5F9; }
.ms-item.all { font-weight: 600; border-bottom: 1px solid var(--border); margin-bottom: 4px; }
.sidebar-backdrop {
  display: none; position: fixed; inset: 0; background: rgba(30,29,36,.35); z-index: 40;
}
.sidebar-backdrop.show { display: block; }
.sidebar {
  position: fixed; top: 0; left: 0; height: 100vh; width: 280px; background: var(--sidebar);
  color: #fff; transform: translateX(-105%); transition: transform .25s ease; z-index: 50;
  padding: 18px 12px; display: flex; flex-direction: column; gap: 6px;
  box-shadow: 8px 0 24px rgba(0,0,0,.2);
}
.sidebar.open { transform: translateX(0); }
.sidebar .side-title { font-size: 12px; opacity: .7; padding: 4px 10px 10px; letter-spacing: .04em; text-transform: uppercase; }
.nav-btn {
  text-align: left; background: transparent; border: 0; color: #fff; padding: 10px 12px; border-radius: 8px;
  cursor: pointer; font-size: 13px; font-family: inherit;
}
.nav-btn:hover { background: rgba(255,255,255,.08); }
.nav-btn.active { background: var(--accent); color: #1E1D24; font-weight: 600; }
.main { flex: 1; overflow: hidden; padding: 10px 16px 12px; display: flex; flex-direction: column; min-height: 0; }
.page { display: none; flex-direction: column; height: 100%; min-height: 0; gap: 8px; }
.page.active { display: flex; }
.note { text-align: right; font-size: 11px; color: var(--muted); flex-shrink: 0; }
.cards {
  display: grid; gap: 8px; flex-shrink: 0;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
}
.card {
  background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 10px 12px;
  display: flex; align-items: center; gap: 10px; min-height: 64px;
}
.card i { font-size: 20px; color: var(--accent); width: 24px; text-align: center; flex-shrink: 0; }
.card .meta { min-width: 0; }
.card .label { font-size: 11px; color: var(--muted); line-height: 1.2; }
.card .value { font-size: 16px; font-weight: 700; margin-top: 2px; }
.charts { display: grid; gap: 8px; flex: 1; min-height: 0; }
.charts.row3 { grid-template-columns: repeat(3, 1fr); }
.charts.row2 { grid-template-columns: repeat(2, 1fr); }
.charts.row5 { grid-template-columns: repeat(5, 1fr); }
.charts.row4 { grid-template-columns: repeat(4, 1fr); }
.charts.stack { grid-template-rows: 1fr 1fr; }
.chart-card {
  background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 8px 10px;
  display: flex; flex-direction: column; min-height: 0;
}
.chart-card h3 { margin: 0 0 4px; font-size: 12px; font-weight: 600; flex-shrink: 0; }
.chart-wrap { flex: 1; min-height: 0; position: relative; padding: 5px; }
.table-wrap {
  background: var(--card); border: 1px solid var(--border); border-radius: 10px;
  display: flex; flex-direction: column; flex: 1; min-height: 0; overflow: hidden;
}
.table-toolbar {
  display: flex; align-items: center; justify-content: space-between; gap: 10px;
  padding: 8px 10px; border-bottom: 1px solid var(--border); flex-shrink: 0;
}
.table-toolbar h3 { margin: 0; font-size: 13px; font-weight: 600; }
.table-toolbar input {
  border: 1px solid var(--border2); border-radius: 8px; padding: 6px 10px; font-size: 12px; min-width: 200px;
}
.table-scroll { overflow: auto; flex: 1; min-height: 0; }
table.data { width: 100%; border-collapse: collapse; font-size: 12px; }
table.data th, table.data td {
  border-bottom: 1px solid var(--border); padding: 7px 8px; text-align: left; white-space: nowrap;
}
table.data th {
  position: sticky; top: 0; background: #fff; z-index: 2; cursor: pointer; user-select: none;
  font-weight: 600; border-bottom: 1px solid var(--border2);
}
table.data th .sort { margin-left: 4px; color: var(--muted); font-size: 10px; }
table.data th.sorted-asc .sort::after { content: "▲"; color: var(--text); }
table.data th.sorted-desc .sort::after { content: "▼"; color: var(--text); }
table.data th .sort::after { content: "⇅"; }
table.resizable th { position: sticky; }
.resize-handle {
  position: absolute; right: 0; top: 0; width: 5px; height: 100%; cursor: col-resize; user-select: none;
}
@media (max-width: 1100px) {
  .charts.row3, .charts.row5, .charts.row4 { grid-template-columns: 1fr 1fr; }
  body { overflow: auto; }
  html, body { height: auto; }
  .app { height: auto; min-height: 100vh; }
  .main, .page { overflow: visible; height: auto; }
}
</style>
</head>
<body>
<div class="app">
  <header class="header">
    <button class="btn-menu" id="btnMenu" aria-label="Abrir menu"><i class="fa-solid fa-bars"></i></button>
    <img src="logo-vtal-footer.png" alt="V.tal" />
    <h1>Painel de Monitoramento de AVCB</h1>
  </header>
  <div class="filters-bar" id="filtersBar"></div>
  <div class="sidebar-backdrop" id="backdrop"></div>
  <aside class="sidebar" id="sidebar">
    <div class="side-title">Navegação</div>
    <button class="nav-btn active" data-page="avcb">AVCB</button>
    <button class="nav-btn" data-page="det-avcb">Detalhamento AVCB</button>
    <button class="nav-btn" data-page="det-desc">Detalhamento AVCB Descontinuados</button>
    <button class="nav-btn" data-page="pi">Prevenção a Incêndio (PI)</button>
    <button class="nav-btn" data-page="det-pi">Detalhamento PI</button>
    <button class="nav-btn" data-page="laudos">Laudos</button>
    <button class="nav-btn" data-page="det-laudos">Detalhamento Laudos</button>
    <button class="nav-btn" data-page="det-laudos-pend">Detalhamento Laudos Pendentes</button>
  </aside>
  <main class="main">
    <section class="page active" id="page-avcb"></section>
    <section class="page" id="page-det-avcb"></section>
    <section class="page" id="page-det-desc"></section>
    <section class="page" id="page-pi"></section>
    <section class="page" id="page-det-pi"></section>
    <section class="page" id="page-laudos"></section>
    <section class="page" id="page-det-laudos"></section>
    <section class="page" id="page-det-laudos-pend"></section>
  </main>
</div>
<script>
const DATA = __DATA_JSON__;

const PAGE_FILTERS = {
  avcb: ["regional","uf","municipio","tipo","resp_legal","prioridade","status_projeto_ppci"],
  "det-avcb": ["regional","uf","municipio","tipo","resp_legal","prioridade","status_projeto_ppci"],
  "det-desc": ["regional","uf","municipio","tipo","resp_legal","prioridade","status_projeto_ppci"],
  pi: ["brigada","sdai","regional","uf","municipio","tipo","resp_legal","prioridade"],
  "det-pi": ["regional","uf","municipio","tipo","resp_legal","prioridade"],
  laudos: ["uf","municipio","tipo","resp_legal","prioridade"],
  "det-laudos": ["regional","uf","municipio","tipo","resp_legal","prioridade"],
  "det-laudos-pend": ["regional","uf","municipio","tipo","resp_legal","prioridade"],
};

const FILTER_LABELS = {
  regional: "Regional",
  uf: "UF",
  municipio: "Município",
  tipo: "Tipo de Prédio",
  resp_legal: "Resp. Legal",
  prioridade: "Prioridade",
  status_projeto_ppci: "Status do projeto PPCI",
  brigada: "Brigada",
  sdai: "SDAI",
};

const state = {
  page: "avcb",
  filters: {},
  charts: {},
  sort: {},
  search: {},
};

function pct(n, d) {
  if (!d) return "0,00%";
  return ((n / d) * 100).toFixed(2).replace(".", ",") + "%";
}
function fmt(n, d) { return `${n} (${pct(n, d)})`; }
function isDescAvcb(v) {
  const s = String(v || "").toLowerCase();
  return s.startsWith("descontinu");
}
function isDescStatus(v) {
  return isDescAvcb(v);
}
function eqCI(a, b) { return String(a||"").trim().toLowerCase() === String(b||"").trim().toLowerCase(); }
function includesCI(a, list) {
  if (!list || !list.length) return true;
  const t = String(a||"").trim().toLowerCase();
  return list.some(x => String(x).trim().toLowerCase() === t);
}
function uniq(arr) {
  const s = new Set();
  const out = [];
  for (const v of arr) {
    const k = String(v ?? "").trim();
    if (!k) continue;
    const lk = k.toLowerCase();
    if (s.has(lk)) continue;
    s.add(lk); out.push(k);
  }
  return out.sort((a,b)=>a.localeCompare(b,"pt-BR"));
}

function datasetForPage(page) {
  if (page === "avcb" || page === "det-avcb" || page === "det-desc") return DATA.avcb;
  if (page === "pi" || page === "det-pi") return DATA.pi;
  return DATA.laudos;
}

function baseRows(page) {
  let rows = datasetForPage(page).slice();
  if (page === "avcb" || page === "det-avcb") {
    rows = rows.filter(r => !isDescAvcb(r.avcb) && !isDescStatus(r.status_avcb));
  } else if (page === "det-desc") {
    rows = rows.filter(r => isDescAvcb(r.avcb) || isDescStatus(r.status_avcb));
  } else if (page === "det-laudos-pend") {
    rows = rows.filter(r => eqCI(r.pendencias_laudos, "Sim"));
  }
  return rows;
}

function municipiosForUFs(ufs) {
  let rows = DATA.municipios;
  if (ufs && ufs.length) rows = rows.filter(m => includesCI(m.uf, ufs));
  return uniq(rows.map(m => m.municipio));
}

function applyFilters(page) {
  const f = state.filters[page] || {};
  return baseRows(page).filter(r => {
    for (const key of (PAGE_FILTERS[page] || [])) {
      const sel = f[key];
      if (!sel || !sel.length) continue;
      if (key === "municipio") {
        if (!includesCI(r.municipio, sel)) return false;
      } else if (!includesCI(r[key], sel)) return false;
    }
    return true;
  });
}

function countBy(rows, key, mapFn) {
  const map = new Map();
  for (const r of rows) {
    let v = mapFn ? mapFn(r) : r[key];
    if (v == null) v = "";
    v = String(v).trim();
    if (!v) continue;
    map.set(v, (map.get(v) || 0) + 1);
  }
  return [...map.entries()].sort((a,b)=>b[1]-a[1]);
}

function destroyCharts(page) {
  const bag = state.charts[page] || [];
  bag.forEach(c => { try { c.destroy(); } catch(e){} });
  state.charts[page] = [];
}

function barPlugin() {
  return {
    id: "barLabels",
    afterDatasetsDraw(chart) {
      const {ctx} = chart;
      const total = chart.$total || 0;
      ctx.save();
      ctx.font = "9px Inter, sans-serif";
      ctx.fillStyle = "#1E1D24";
      chart.data.datasets.forEach((ds, di) => {
        const meta = chart.getDatasetMeta(di);
        meta.data.forEach((el, i) => {
          const val = ds.data[i];
          if (val == null) return;
          const p = total ? ((val/total)*100).toFixed(2).replace(".", ",") + "%" : "0,00%";
          const label = `${val} (${p})`;
          const pos = el.tooltipPosition();
          if (chart.options.indexAxis === "y") {
            ctx.textAlign = "left";
            ctx.textBaseline = "middle";
            ctx.fillText(label, pos.x + 4, pos.y);
          } else {
            ctx.textAlign = "center";
            ctx.textBaseline = "bottom";
            ctx.fillText(label, pos.x, pos.y - 2);
          }
        });
      });
      ctx.restore();
    }
  };
}

function makeBar(canvas, labels, values, total, horizontal, opts={}) {
  const cfg = {
    type: "bar",
    data: {
      labels,
      datasets: [{
        data: values,
        backgroundColor: "#FFD919",
        borderSkipped: false,
        barThickness: opts.barThickness,
        categoryPercentage: opts.categoryPercentage || 0.8,
        barPercentage: opts.barPercentage || 0.9,
      }]
    },
    options: {
      indexAxis: horizontal ? "y" : "x",
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: { enabled: false },
      },
      layout: { padding: 5 },
      scales: {
        x: {
          display: opts.showX !== false,
          ticks: { display: !!opts.xTicks, font: { size: 9 }, color: "#1E1D24" },
          grid: { display: false },
          border: { display: opts.showX !== false },
        },
        y: {
          display: opts.showY !== false,
          ticks: { display: opts.yTicks !== false, font: { size: 9 }, color: "#1E1D24" },
          grid: { display: false },
          border: { display: opts.showY !== false },
        }
      }
    },
    plugins: [barPlugin()]
  };
  if (opts.xTicks === false) cfg.options.scales.x.ticks.display = false;
  if (opts.hideX) { cfg.options.scales.x.display = false; }
  if (opts.hideY) { cfg.options.scales.y.display = false; }
  const chart = new Chart(canvas.getContext("2d"), cfg);
  chart.$total = total;
  return chart;
}

/* ---------- Multi-select filters ---------- */
function ensureFilterState(page) {
  if (!state.filters[page]) state.filters[page] = {};
}

function selectedLabel(key, selected, allValues) {
  if (!selected || selected.length === 0 || selected.length === allValues.length)
    return `${FILTER_LABELS[key]}: Todos`;
  if (selected.length === 1) return `${FILTER_LABELS[key]}: ${selected[0]}`;
  return `${FILTER_LABELS[key]}: ${selected.length} sel.`;
}

function optionsForFilter(page, key) {
  const rows = baseRows(page);
  const f = state.filters[page] || {};
  if (key === "municipio") {
    const ufs = f.uf && f.uf.length ? f.uf : uniq(DATA.municipios.map(m => m.uf));
    return municipiosForUFs(ufs);
  }
  return uniq(rows.map(r => r[key]));
}

function renderFilters() {
  const page = state.page;
  ensureFilterState(page);
  const bar = document.getElementById("filtersBar");
  bar.innerHTML = "";
  for (const key of PAGE_FILTERS[page]) {
    const all = optionsForFilter(page, key);
    if (!state.filters[page][key]) state.filters[page][key] = all.slice();
    // prune invalid after cascade
    state.filters[page][key] = state.filters[page][key].filter(v => all.some(a => eqCI(a,v)));
    if (!state.filters[page][key].length) state.filters[page][key] = all.slice();

    const wrap = document.createElement("div");
    wrap.className = "ms";
    wrap.dataset.key = key;
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "ms-btn";
    btn.textContent = selectedLabel(key, state.filters[page][key], all);
    const panel = document.createElement("div");
    panel.className = "ms-panel";

    const allItem = document.createElement("label");
    allItem.className = "ms-item all";
    const allCb = document.createElement("input");
    allCb.type = "checkbox";
    allCb.checked = state.filters[page][key].length === all.length;
    allCb.addEventListener("change", () => {
      state.filters[page][key] = allCb.checked ? all.slice() : [];
      if (key === "uf") {
        const munAll = optionsForFilter(page, "municipio");
        state.filters[page].municipio = munAll.slice();
      }
      renderFilters();
      renderPage();
    });
    allItem.appendChild(allCb);
    allItem.appendChild(document.createTextNode("Selecionar Todos"));
    panel.appendChild(allItem);

    all.forEach(val => {
      const item = document.createElement("label");
      item.className = "ms-item";
      const cb = document.createElement("input");
      cb.type = "checkbox";
      cb.checked = state.filters[page][key].some(x => eqCI(x, val));
      cb.addEventListener("change", () => {
        const set = new Set(state.filters[page][key]);
        if (cb.checked) set.add(val); else {
          // remove case-insensitive
          [...set].forEach(x => { if (eqCI(x,val)) set.delete(x); });
        }
        state.filters[page][key] = [...set];
        if (key === "uf") {
          const munAll = optionsForFilter(page, "municipio");
          state.filters[page].municipio = munAll.slice();
        }
        renderFilters();
        renderPage();
      });
      item.appendChild(cb);
      item.appendChild(document.createTextNode(val));
      panel.appendChild(item);
    });

    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      document.querySelectorAll(".ms.open").forEach(el => { if (el !== wrap) el.classList.remove("open"); });
      wrap.classList.toggle("open");
    });
    wrap.appendChild(btn);
    wrap.appendChild(panel);
    bar.appendChild(wrap);
  }
}

document.addEventListener("click", () => {
  document.querySelectorAll(".ms.open").forEach(el => el.classList.remove("open"));
});

/* ---------- Cards / pages ---------- */
function cardHTML(icon, label, value) {
  return `<div class="card"><i class="fa-solid ${icon}"></i><div class="meta"><div class="label">${label}</div><div class="value">${value}</div></div></div>`;
}

function renderAvcbPage(el, rows) {
  const ativos = rows.length;
  const validos = rows.filter(r => eqCI(r.avcb, "VÁLIDO") || eqCI(r.avcb, "VALIDO")).length;
  const vencidos = rows.filter(r => eqCI(r.avcb, "VENCIDO")).length;
  const ppciConc = rows.filter(r => eqCI(r.status_projeto_ppci, "Concluído") || eqCI(r.status_projeto_ppci, "Concluido")).length;
  const ppciApr = rows.filter(r => eqCI(r.status_ppci, "Aprovado")).length;

  el.innerHTML = `
    <div class="note">Essa aba do painel não considera os prédios com AVCB descontinuado</div>
    <div class="cards">
      ${cardHTML("fa-circle-check", "AVCBs Válidos", fmt(validos, ativos))}
      ${cardHTML("fa-circle-exclamation", "AVCBs Vencidos", fmt(vencidos, ativos))}
      ${cardHTML("fa-file-signature", "Status do Projeto PPCI Concluído", fmt(ppciConc, ativos))}
      ${cardHTML("fa-file-signature", "Status PPCI Aprovado", fmt(ppciApr, ativos))}
    </div>
    <div class="charts row3" style="flex:1.1">
      <div class="chart-card"><h3>AVCB</h3><div class="chart-wrap"><canvas id="c-avcb-1"></canvas></div></div>
      <div class="chart-card"><h3>Status AVCB</h3><div class="chart-wrap"><canvas id="c-avcb-2"></canvas></div></div>
      <div class="chart-card"><h3>Detalhes AVCB Pendentes</h3><div class="chart-wrap"><canvas id="c-avcb-3"></canvas></div></div>
    </div>
    <div class="charts row2" style="flex:0.9">
      <div class="chart-card"><h3>Status do Projeto PPCI</h3><div class="chart-wrap"><canvas id="c-avcb-4"></canvas></div></div>
      <div class="chart-card"><h3>Status PPCI</h3><div class="chart-wrap"><canvas id="c-avcb-5"></canvas></div></div>
    </div>`;

  destroyCharts("avcb");
  const bag = [];

  const avcbMap = {"VENCIDO":"Projetos Vencidos","VÁLIDO":"Protocolos Válidos","VALIDO":"Protocolos Válidos"};
  const a1 = countBy(rows, "avcb", r => avcbMap[String(r.avcb).toUpperCase()] || null).filter(x=>x[0]);
  bag.push(makeBar(document.getElementById("c-avcb-1"), a1.map(x=>x[0]), a1.map(x=>x[1]), ativos, true, {xTicks:false}));

  const allowedStatus = ["Pendente","Válido","Aguardando vistoria do CBM","Aguardando emissão de AVCB","Vistoria comunicada"];
  const a2 = countBy(rows.filter(r => !isDescStatus(r.status_avcb)), "status_avcb")
    .filter(([k]) => allowedStatus.some(a => eqCI(a,k)));
  bag.push(makeBar(document.getElementById("c-avcb-2"), a2.map(x=>x[0]), a2.map(x=>x[1]), ativos, true, {xTicks:false}));

  const pend = rows.filter(r => eqCI(r.status_avcb, "Pendente"));
  const detMap = (v) => {
    const s = String(v||"").trim();
    if (!s || s === "0") return "Sem detalhamento";
    return s;
  };
  const a3 = countBy(pend, "detalhes_avcb", r => detMap(r.detalhes_avcb));
  bag.push(makeBar(document.getElementById("c-avcb-3"), a3.map(x=>x[0]), a3.map(x=>x[1]), pend.length || 1, true, {xTicks:false}));

  const a4 = countBy(rows, "status_projeto_ppci");
  bag.push(makeBar(document.getElementById("c-avcb-4"), a4.map(x=>x[0]), a4.map(x=>x[1]), ativos, true, {xTicks:false}));
  const a5 = countBy(rows, "status_ppci");
  bag.push(makeBar(document.getElementById("c-avcb-5"), a5.map(x=>x[0]), a5.map(x=>x[1]), ativos, true, {xTicks:false}));
  state.charts.avcb = bag;
}

function sortableTable(page, elId, columns, rows, searchKey) {
  if (!state.sort[page]) state.sort[page] = { col: columns[0].key, dir: "asc" };
  if (!state.search[page]) state.search[page] = "";
  const q = state.search[page].toLowerCase();
  let filtered = rows;
  if (q) {
    filtered = rows.filter(r => String(r[searchKey] || r.nome_comum || r.nome || r.predio || "").toLowerCase().includes(q));
  }
  const {col, dir} = state.sort[page];
  filtered = filtered.slice().sort((a,b) => {
    const av = String(a[col] ?? "");
    const bv = String(b[col] ?? "");
    const cmp = av.localeCompare(bv, "pt-BR", {numeric:true});
    return dir === "asc" ? cmp : -cmp;
  });

  const head = columns.map(c => {
    const cls = state.sort[page].col === c.key ? (state.sort[page].dir === "asc" ? "sorted-asc" : "sorted-desc") : "";
    return `<th class="${cls}" data-key="${c.key}" style="min-width:${c.width||110}px; position:relative;">${c.label}<span class="sort"></span><span class="resize-handle"></span></th>`;
  }).join("");
  const body = filtered.map(r => `<tr>${columns.map(c => `<td>${r[c.key] ?? ""}</td>`).join("")}</tr>`).join("");

  const wrap = document.getElementById(elId);
  wrap.innerHTML = `
    <div class="table-toolbar">
      <h3>Detalhamento</h3>
      <input type="search" placeholder="Buscar por nome do prédio..." value="${state.search[page].replace(/"/g,"&quot;")}" id="search-${page}" />
    </div>
    <div class="table-scroll">
      <table class="data resizable" id="table-${page}">
        <thead><tr>${head}</tr></thead>
        <tbody>${body}</tbody>
      </table>
    </div>`;

  wrap.querySelector(`#search-${page}`).addEventListener("input", (e) => {
    state.search[page] = e.target.value;
    sortableTable(page, elId, columns, rows, searchKey);
  });
  wrap.querySelectorAll("th[data-key]").forEach(th => {
    th.addEventListener("click", (e) => {
      if (e.target.classList.contains("resize-handle")) return;
      const key = th.dataset.key;
      if (state.sort[page].col === key) state.sort[page].dir = state.sort[page].dir === "asc" ? "desc" : "asc";
      else state.sort[page] = { col: key, dir: "asc" };
      sortableTable(page, elId, columns, rows, searchKey);
    });
  });
  enableColumnResize(wrap.querySelector(`#table-${page}`));
}

function enableColumnResize(table) {
  if (!table) return;
  table.querySelectorAll("th").forEach(th => {
    const handle = th.querySelector(".resize-handle");
    if (!handle) return;
    let startX, startW;
    handle.addEventListener("mousedown", (e) => {
      e.preventDefault(); e.stopPropagation();
      startX = e.pageX; startW = th.offsetWidth;
      const onMove = (ev) => { th.style.width = Math.max(60, startW + (ev.pageX - startX)) + "px"; th.style.minWidth = th.style.width; };
      const onUp = () => { document.removeEventListener("mousemove", onMove); document.removeEventListener("mouseup", onUp); };
      document.addEventListener("mousemove", onMove);
      document.addEventListener("mouseup", onUp);
    });
  });
}

function renderDetAvcb(el, rows, page, note) {
  const ativos = rows.length || 1;
  const denom = page === "det-desc"
    ? (rows.length || 1)
    : (rows.length || 1);
  const validos = rows.filter(r => eqCI(r.avcb, "VÁLIDO") || eqCI(r.avcb, "VALIDO")).length;
  const vencidos = rows.filter(r => eqCI(r.avcb, "VENCIDO")).length;
  const ppciConc = rows.filter(r => eqCI(r.status_projeto_ppci, "Concluído") || eqCI(r.status_projeto_ppci, "Concluido")).length;
  const ppciApr = rows.filter(r => eqCI(r.status_ppci, "Aprovado")).length;
  el.innerHTML = `
    <div class="note">${note}</div>
    <div class="cards">
      ${cardHTML("fa-circle-check", "AVCBs Válidos", fmt(validos, denom))}
      ${cardHTML("fa-circle-exclamation", "AVCBs Vencidos", fmt(vencidos, denom))}
      ${cardHTML("fa-file-signature", "Status do Projeto PPCI Concluído", fmt(ppciConc, denom))}
      ${cardHTML("fa-file-signature", "Status PPCI Aprovado", fmt(ppciApr, denom))}
    </div>
    <div class="table-wrap" id="tbl-${page}"></div>`;
  sortableTable(page, `tbl-${page}`, [
    {key:"predio", label:"Prédio (ID)"},
    {key:"nome_comum", label:"Nome Comum"},
    {key:"uf", label:"UF", width:60},
    {key:"status_avcb", label:"Status AVCB"},
    {key:"status_ppci", label:"Status PPCI"},
    {key:"laudos_op", label:"Laudos OP"},
  ], rows, "nome_comum");
}

function renderPi(el, rows) {
  const total = rows.length || 1;
  const brigadaVals = ["12 Horas","24 Horas","12H - noturno","12h - noturno","12H - diurno","12h - diurno"];
  const brigada = rows.filter(r => brigadaVals.some(v => eqCI(v, r.brigada))).length;
  const sdaiSim = rows.filter(r => eqCI(r.sdai, "SIM")).length;
  const semFalhas = rows.filter(r => eqCI(r.operacional_sem_falhas, "SIM")).length;
  const comFalhasSet = ["Operacional com falhas - Alto","Inoperante","Operacional com falhas - Médio","Operacional com falhas - Medio","Operacional com falhas - Baixo","Operacional com falhas - Muito alto"];
  const comFalhas = rows.filter(r => comFalhasSet.some(v => eqCI(v, r.sdai_operante))).length;
  const fm = rows.filter(r => eqCI(r.fm200, "SIM")).length;
  const ext = rows.filter(r => eqCI(r.extintor, "SIM")).length;

  el.innerHTML = `
    <div class="cards">
      ${cardHTML("fa-user-shield", "Brigada", fmt(brigada, total))}
      ${cardHTML("fa-bell", "SDAI válido", fmt(sdaiSim, total))}
      ${cardHTML("fa-circle-check", "SDAI/SDACI sem falhas", fmt(semFalhas, total))}
      ${cardHTML("fa-circle-exclamation", "SDAI/SDACI com falhas", fmt(comFalhas, total))}
      ${cardHTML("fa-database", "FM200 válido", fmt(fm, total))}
      ${cardHTML("fa-fire-extinguisher", "Extintor presente", fmt(ext, total))}
    </div>
    <div class="charts row2" style="flex:1.1">
      <div class="chart-card"><h3>Brigada Civil</h3><div class="chart-wrap"><canvas id="c-pi-1"></canvas></div></div>
      <div class="chart-card"><h3>SDAI/SDACI Operante</h3><div class="chart-wrap"><canvas id="c-pi-2"></canvas></div></div>
    </div>
    <div class="charts row3" style="flex:0.9">
      <div class="chart-card"><h3>SDAI</h3><div class="chart-wrap"><canvas id="c-pi-3"></canvas></div></div>
      <div class="chart-card"><h3>FM200</h3><div class="chart-wrap"><canvas id="c-pi-4"></canvas></div></div>
      <div class="chart-card"><h3>Extintor</h3><div class="chart-wrap"><canvas id="c-pi-5"></canvas></div></div>
    </div>`;

  destroyCharts("pi");
  const bag = [];
  const brigWanted = ["SIM","NÃO","12 Horas","24 Horas"];
  const brigCounts = countBy(rows, "brigada", r => {
    const b = r.brigada;
    if (eqCI(b,"SIM") || eqCI(b,"NÃO") || eqCI(b,"NAO") || eqCI(b,"12 Horas") || eqCI(b,"24 Horas")) return b.toUpperCase() === "NAO" ? "NÃO" : (eqCI(b,"SIM")?"SIM": eqCI(b,"NÃO")||eqCI(b,"Nao")?"NÃO": b);
    if (String(b).toLowerCase().includes("12") && String(b).toLowerCase().includes("hora")) return "12 Horas";
    if (String(b).toLowerCase().includes("24")) return "24 Horas";
    if (eqCI(b,"NÃO") || eqCI(b,"Nao") || eqCI(b,"NAO")) return "NÃO";
    return null;
  }).filter(([k]) => brigWanted.some(w => eqCI(w,k)));
  // also map NÃO from raw
  const bmap = new Map(brigCounts);
  rows.forEach(r => {
    if (eqCI(r.brigada,"NÃO") || eqCI(r.brigada,"Nao") || eqCI(r.brigada,"NAO")) {
      bmap.set("NÃO", (bmap.get("NÃO")||0));
    }
  });
  // recount brigada properly
  const brigAgg = new Map();
  rows.forEach(r => {
    let k = String(r.brigada||"").trim();
    if (!k) return;
    const kl = k.toLowerCase();
    if (kl === "não" || kl === "nao") k = "NÃO";
    else if (kl === "sim") k = "SIM";
    else if (kl.includes("12") && kl.includes("hora") && !kl.includes("noturno") && !kl.includes("diurno")) k = "12 Horas";
    else if (kl.includes("24")) k = "24 Horas";
    else if (kl.includes("12")) {
      // keep 12h variants out of chart items list unless mapped - chart items are SIM, NÃO, 12 Horas, 24 Horas
      if (kl.includes("noturno") || kl.includes("diurno")) return;
      k = "12 Horas";
    } else return;
    brigAgg.set(k, (brigAgg.get(k)||0)+1);
  });
  const bArr = [...brigAgg.entries()].sort((a,b)=>b[1]-a[1]);
  bag.push(makeBar(document.getElementById("c-pi-1"), bArr.map(x=>x[0]), bArr.map(x=>x[1]), total, true, {xTicks:false}));

  const opArr = countBy(rows, "sdai_operante");
  bag.push(makeBar(document.getElementById("c-pi-2"), opArr.map(x=>x[0]), opArr.map(x=>x[1]), total, true, {xTicks:false, barThickness: 14}));

  function yn(key) {
    const m = new Map([["SIM",0],["NÃO",0]]);
    rows.forEach(r => {
      let v = String(r[key]||"").trim().toUpperCase().replace("NAO","NÃO");
      if (v === "SIM" || v === "NÃO") m.set(v, m.get(v)+1);
    });
    return [...m.entries()].filter(x=>x[1]>0).sort((a,b)=>b[1]-a[1]);
  }
  const s = yn("sdai");
  bag.push(makeBar(document.getElementById("c-pi-3"), s.map(x=>x[0]), s.map(x=>x[1]), total, true, {xTicks:false}));
  const f = yn("fm200");
  bag.push(makeBar(document.getElementById("c-pi-4"), f.map(x=>x[0]), f.map(x=>x[1]), total, true, {xTicks:false}));
  const e = yn("extintor");
  bag.push(makeBar(document.getElementById("c-pi-5"), e.map(x=>x[0]), e.map(x=>x[1]), total, true, {xTicks:false}));
  state.charts.pi = bag;
}

function renderDetPi(el, rows) {
  const total = rows.length || 1;
  const brigadaVals = ["12 Horas","24 Horas","12H - noturno","12h - noturno","12H - diurno","12h - diurno"];
  const brigada = rows.filter(r => brigadaVals.some(v => eqCI(v, r.brigada)) || /12h|12 h|24/i.test(r.brigada||"")).length;
  const sdaiSim = rows.filter(r => eqCI(r.sdai, "SIM")).length;
  const fm = rows.filter(r => eqCI(r.fm200, "SIM")).length;
  const ext = rows.filter(r => eqCI(r.extintor, "SIM")).length;
  const comFalhasSet = ["Operacional com falhas - Alto","Inoperante","Operacional com falhas - Médio","Operacional com falhas - Medio","Operacional com falhas - Baixo","Operacional com falhas - Muito alto"];
  const comFalhas = rows.filter(r => comFalhasSet.some(v => eqCI(v, r.sdai_operante))).length;
  const semFalhas = rows.filter(r => eqCI(r.operacional_sem_falhas, "SIM")).length;
  el.innerHTML = `
    <div class="cards">
      ${cardHTML("fa-user-shield", "Brigada", fmt(brigada, total))}
      ${cardHTML("fa-bell", "SDAI válido", fmt(sdaiSim, total))}
      ${cardHTML("fa-database", "FM200 válido", fmt(fm, total))}
      ${cardHTML("fa-fire-extinguisher", "Extintor presente", fmt(ext, total))}
      ${cardHTML("fa-circle-exclamation", "SDAI/SDACI com falhas", fmt(comFalhas, total))}
      ${cardHTML("fa-circle-check", "SDAI/SDACI sem falhas", fmt(semFalhas, total))}
    </div>
    <div class="table-wrap" id="tbl-det-pi"></div>`;
  sortableTable("det-pi", "tbl-det-pi", [
    {key:"predio", label:"Prédio (ID)"},
    {key:"nome_comum", label:"Nome Comum"},
    {key:"uf", label:"UF", width:50},
    {key:"municipio", label:"Município"},
    {key:"tipo", label:"Tipo"},
    {key:"resp_legal", label:"Responsável"},
    {key:"brigada", label:"Brigada Civil"},
    {key:"sdai", label:"SDAI"},
    {key:"fm200", label:"FM200"},
    {key:"status_extintor", label:"Status Extintor"},
    {key:"data_venc_extintor", label:"Data de Vencimento Extintor"},
    {key:"data_venc_mangueira", label:"Data de Vencimento Mangueira"},
    {key:"sdai_operante", label:"SDAI/SDACI operante"},
  ], rows, "nome_comum");
}

function renderLaudos(el, rows) {
  const total = rows.length || 1;
  const artE = rows.filter(r => eqCI(r.art_eletrica, "SIM")).length;
  const artS = rows.filter(r => eqCI(r.art_spda, "SIM")).length;
  const artG = rows.filter(r => eqCI(r.art_gmg, "SIM")).length;
  const artT = rows.filter(r => eqCI(r.art_tanques, "SIM")).length;
  el.innerHTML = `
    <div class="cards">
      ${cardHTML("fa-bolt", "ART ELÉTRICA PENDENTE", fmt(artE, total))}
      ${cardHTML("fa-bolt", "ART SPDA PENDENTE", fmt(artS, total))}
      ${cardHTML("fa-charging-station", "ART GMG PENDENTE", fmt(artG, total))}
      ${cardHTML("fa-database", "ART TANQUES PENDENTE", fmt(artT, total))}
    </div>
    <div class="charts" style="flex:1.1; grid-template-columns:1fr">
      <div class="chart-card"><h3>Laudos Pendentes por Estado (UF)</h3><div class="chart-wrap"><canvas id="c-lau-1"></canvas></div></div>
    </div>
    <div class="charts row4" style="flex:0.9">
      <div class="chart-card"><h3>Laudos "ART ELÉTRICA" Pendentes</h3><div class="chart-wrap"><canvas id="c-lau-2"></canvas></div></div>
      <div class="chart-card"><h3>Laudos "ART SPDA" Pendentes</h3><div class="chart-wrap"><canvas id="c-lau-3"></canvas></div></div>
      <div class="chart-card"><h3>Laudos "ART GMG" Pendentes</h3><div class="chart-wrap"><canvas id="c-lau-4"></canvas></div></div>
      <div class="chart-card"><h3>Laudos "ART TANQUES" Pendentes</h3><div class="chart-wrap"><canvas id="c-lau-5"></canvas></div></div>
    </div>`;
  destroyCharts("laudos");
  const bag = [];
  const byUf = countBy(rows.filter(r => eqCI(r.pendencias_laudos, "Sim")), "uf");
  bag.push(makeBar(document.getElementById("c-lau-1"), byUf.map(x=>x[0]), byUf.map(x=>x[1]), total, false, {hideY:true, xTicks:true, yTicks:false}));

  function artBar(id, key) {
    const n = rows.filter(r => eqCI(r[key], "SIM")).length;
    return makeBar(document.getElementById(id), ["SIM"], [n], total, true, {xTicks:false});
  }
  bag.push(artBar("c-lau-2","art_eletrica"));
  bag.push(artBar("c-lau-3","art_spda"));
  bag.push(artBar("c-lau-4","art_gmg"));
  bag.push(artBar("c-lau-5","art_tanques"));
  state.charts.laudos = bag;
}

function renderDetLaudos(el, rows, page) {
  const total = rows.length || 1;
  const artE = rows.filter(r => eqCI(r.art_eletrica, "SIM")).length;
  const artS = rows.filter(r => eqCI(r.art_spda, "SIM")).length;
  const artG = rows.filter(r => eqCI(r.art_gmg, "SIM")).length;
  const artT = rows.filter(r => eqCI(r.art_tanques, "SIM")).length;
  el.innerHTML = `
    <div class="cards">
      ${cardHTML("fa-bolt", "ART ELÉTRICA PENDENTE", fmt(artE, total))}
      ${cardHTML("fa-bolt", "ART SPDA PENDENTE", fmt(artS, total))}
      ${cardHTML("fa-charging-station", "ART GMG PENDENTE", fmt(artG, total))}
      ${cardHTML("fa-database", "ART TANQUES PENDENTE", fmt(artT, total))}
    </div>
    <div class="table-wrap" id="tbl-${page}"></div>`;
  sortableTable(page, `tbl-${page}`, [
    {key:"predio", label:"Prédio"},
    {key:"nome", label:"Nome"},
    {key:"uf", label:"UF", width:50},
    {key:"municipio", label:"Município"},
    {key:"pendencias_laudos", label:"Pendências de Laudos"},
    {key:"art_eletrica", label:"ART ELÉTRICA"},
    {key:"art_spda", label:"ART SPDA"},
    {key:"art_gmg", label:"ART GMG"},
    {key:"art_tanques", label:"ART TANQUES"},
  ], rows, "nome");
}

function renderPage() {
  const page = state.page;
  const rows = applyFilters(page);
  const el = document.getElementById("page-" + page);
  if (page === "avcb") renderAvcbPage(el, rows);
  else if (page === "det-avcb") renderDetAvcb(el, rows, page, "Essa aba do painel não considera os prédios com AVCB descontinuado");
  else if (page === "det-desc") renderDetAvcb(el, rows, page, "Essa aba do painel considera todos os prédios (AVCB descontinuado, AVCB Válidos, AVCBs Vencidos)");
  else if (page === "pi") renderPi(el, rows);
  else if (page === "det-pi") renderDetPi(el, rows);
  else if (page === "laudos") renderLaudos(el, rows);
  else if (page === "det-laudos") renderDetLaudos(el, rows, page);
  else if (page === "det-laudos-pend") renderDetLaudos(el, rows, page);
}

/* ---------- Nav / sidebar ---------- */
const sidebar = document.getElementById("sidebar");
const backdrop = document.getElementById("backdrop");
document.getElementById("btnMenu").addEventListener("click", () => {
  sidebar.classList.add("open");
  backdrop.classList.add("show");
});
backdrop.addEventListener("click", () => {
  sidebar.classList.remove("open");
  backdrop.classList.remove("show");
});
document.querySelectorAll(".nav-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".nav-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    state.page = btn.dataset.page;
    document.querySelectorAll(".page").forEach(p => p.classList.remove("active"));
    document.getElementById("page-" + state.page).classList.add("active");
    sidebar.classList.remove("open");
    backdrop.classList.remove("show");
    renderFilters();
    renderPage();
  });
});

renderFilters();
renderPage();
</script>
</body>
</html>
"""


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    html = HTML.replace("__DATA_JSON__", json.dumps(data, ensure_ascii=False))
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
