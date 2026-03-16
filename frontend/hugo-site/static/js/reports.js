function renderReports(rows) {
  const tbody = document.querySelector("#reportsTable tbody");
  tbody.innerHTML = "";
  rows.forEach((row) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${row.snapshot_date}</td>
      <td>${row.region}</td>
      <td>${row.network_uptime}</td>
      <td>${row.latency}</td>
      <td>${row.packet_loss}</td>
      <td>${row.traffic_volume}</td>
    `;
    tbody.appendChild(tr);
  });
}

apiGet("/api/kpis")
  .then((rows) => renderReports(rows))
  .catch((err) => console.error("Reports load failed:", err));
