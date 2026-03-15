---
title: "Live Engine Results"
---

# Live Engine Results

<div class="engine-panel" id="live-panel">Fetching...</div>

<script>
async function loadResults() {
  const panel = document.getElementById('live-panel');
  const endpoints = [
    {label: 'Riemann KS', url: 'https://smarthub.my/engine/riemann/rmt', key: 'ks_statistic'},
    {label: 'Spectral Gap', url: 'https://smarthub.my/engine/riemann/rmt', key: 'spectral_gap'},
    {label: 'Yang-Mills Δ', url: 'https://smarthub.my/engine/yang-mills/fermions', key: 'plateau_mass'},
    {label: 'NS Lyapunov', url: 'https://smarthub.my/engine/navier-stokes/3d', key: 'lyapunov'},
  ];
  const rows = await Promise.allSettled(
    endpoints.map(e => fetch(e.url).then(r=>r.json()).then(d=>({...e, val: d[e.key] ?? '—'})))
  );
  panel.innerHTML = '<table><tr><th>Metric</th><th>Value</th><th>Target</th></tr>' +
    rows.map(r => r.status==='fulfilled'
      ? `<tr><td>${r.value.label}</td><td class="engine-val">${r.value.val}</td><td>—</td></tr>`
      : '').join('') +
    `</table><small>Last updated: ${new Date().toISOString()}</small>`;
}
loadResults();
</script>

## Verified Results (2026-03-05)

| Metric | Value | Significance |
|---|---|---|
| Riemann KS statistic | **0.099218** | GUE agreement |
| Spectral gap | **0.960906** | Consistent with RH |
| Kolmogorov -5/3 | ✓ | Turbulence scaling |
| Yang-Mills mass gap | Active | Plateau mass computed |

## Endpoints

```
GET smarthub.my/engine/riemann/rmt
GET smarthub.my/engine/yang-mills/fermions
GET smarthub.my/engine/navier-stokes/3d
GET smarthub.my/engine/bsd/elliptic
POST smarthub.my/engine/agent/register
```
