/** Runnable example generated from the official Medux API Reference. */

const baseUrl = process.env.MEDUX_API_BASE_URL ?? "https://api.medux.io";
const placeholders = new Set([]);

function requireEnv(name) {
  const value = process.env[name];
  if (!value) throw new Error(`Set ${name} before running this example`);
  return value;
}

function resolvePlaceholders(value) {
  if (Array.isArray(value)) return value.map(resolvePlaceholders);
  if (value && typeof value === "object") {
    return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, resolvePlaceholders(item)]));
  }
  if (typeof value === "string" && placeholders.has(value)) return requireEnv(value);
  return value;
}

let path = "/api/app/v1/results";
const url = new URL(path, baseUrl);

if (process.env.CURSOR) url.searchParams.set("cursor", process.env.CURSOR);
if (process.env.LIMIT) url.searchParams.set("limit", process.env.LIMIT);
if (process.env.MEDIA_TYPE) url.searchParams.set("media_type", process.env.MEDIA_TYPE);
if (process.env.CAPABILITY_ID) url.searchParams.set("capability_id", process.env.CAPABILITY_ID);
if (process.env.STATUS) url.searchParams.set("status", process.env.STATUS);

const response = await fetch(url, {
  method: "GET",
  headers: {
    Authorization: `Bearer ${requireEnv("MEDUX_API_KEY")}`,
  },
});

const result = await response.json();
if (!response.ok) {
  throw new Error(`${response.status} ${JSON.stringify(result)}`);
}
if (result.code !== undefined && result.code !== 0) {
  throw new Error(`Medux API error: ${result.code} ${result.message ?? ""}`);
}
console.log(JSON.stringify(result, null, 2));
