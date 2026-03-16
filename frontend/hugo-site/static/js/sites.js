function renderTable(rows) {
  const tbody = document.querySelector("#sitesTable tbody");
  tbody.innerHTML = "";
  rows.forEach((row) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${row.site_id}</td>
      <td>${row.region}</td>
      <td>${row.latitude ?? ""}</td>
      <td>${row.longitude ?? ""}</td>
      <td>${row.signal_strength}</td>
      <td>${row.status}</td>
    `;
    tbody.appendChild(tr);
  });
}

function populateRegions(rows) {
  const regionFilter = document.getElementById("regionFilter");
  const regions = [...new Set(rows.map((row) => row.region))].sort();
  regions.forEach((region) => {
    const option = document.createElement("option");
    option.value = region;
    option.textContent = region;
    regionFilter.appendChild(option);
  });
}

let allSites = [];
apiGet("/api/sites")
  .then((rows) => {
    allSites = rows;
    populateRegions(rows);
    renderTable(rows);
  })
  .catch((err) => console.error("Sites load failed:", err));

document.getElementById("regionFilter").addEventListener("change", (event) => {
  const selected = event.target.value;
  const filtered = selected ? allSites.filter((site) => site.region === selected) : allSites;
  renderTable(filtered);
});
