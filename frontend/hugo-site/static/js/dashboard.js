function averageByRegion(rows, field) {
  const groups = {};
  rows.forEach((row) => {
    groups[row.region] = groups[row.region] || [];
    groups[row.region].push(Number(row[field]));
  });
  const labels = Object.keys(groups);
  const values = labels.map((region) => {
    const vals = groups[region];
    return vals.reduce((a, b) => a + b, 0) / vals.length;
  });
  return { labels, values };
}

function renderDashboard(kpis) {
  const uptime = averageByRegion(kpis, "network_uptime");
  const traffic = averageByRegion(kpis, "traffic_volume");
  const labels = [...new Set(kpis.map((k) => k.snapshot_date))].sort();

  const latencyByRegion = {};
  kpis.forEach((k) => {
    latencyByRegion[k.region] = latencyByRegion[k.region] || {};
    latencyByRegion[k.region][k.snapshot_date] = Number(k.latency);
  });
  const latencyDatasets = Object.keys(latencyByRegion).map((region) => ({
    label: region,
    data: labels.map((d) => latencyByRegion[region][d] ?? null),
    borderWidth: 2,
    fill: false,
  }));

  new Chart(document.getElementById("uptimeChart"), {
    type: "bar",
    data: { labels: uptime.labels, datasets: [{ label: "Uptime %", data: uptime.values }] },
  });

  new Chart(document.getElementById("latencyChart"), {
    type: "line",
    data: { labels, datasets: latencyDatasets },
  });

  new Chart(document.getElementById("trafficChart"), {
    type: "pie",
    data: {
      labels: traffic.labels,
      datasets: [{ label: "Traffic Volume", data: traffic.values }],
    },
  });
}

apiGet("/api/kpis")
  .then((kpis) => renderDashboard(kpis))
  .catch((err) => console.error("Dashboard load failed:", err));
