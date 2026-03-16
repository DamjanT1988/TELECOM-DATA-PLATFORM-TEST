const API_BASE = window.TELECOM_API_BASE || "http://localhost:5000";

async function apiGet(path) {
  const response = await fetch(`${API_BASE}${path}`);
  if (!response.ok) {
    const msg = await response.text();
    throw new Error(`API ${response.status}: ${msg}`);
  }
  return response.json();
}
