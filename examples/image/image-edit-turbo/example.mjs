/** Runnable example generated from the official Medux API Reference. */

const baseUrl = process.env.MEDUX_API_BASE_URL ?? "https://api.medux.io";
const placeholders = new Set(["FILE_ID", "PROMPT"]);

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

let path = "/api/app/v1/generate/image/image_edit_turbo";
const url = new URL(path, baseUrl);

const payload = resolvePlaceholders({
  "height": 1024,
  "image_file_ids": [
    "FILE_ID"
  ],
  "model_id": "qwen-image-edit",
  "prompt": "PROMPT",
  "width": 1024
});

const response = await fetch(url, {
  method: "POST",
  headers: {
    Authorization: `Bearer ${requireEnv("MEDUX_API_KEY")}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify(payload),
});

const result = await response.json();
if (!response.ok) {
  throw new Error(`${response.status} ${JSON.stringify(result)}`);
}
if (result.code !== undefined && result.code !== 0) {
  throw new Error(`Medux API error: ${result.code} ${result.message ?? ""}`);
}
console.log(JSON.stringify(result, null, 2));
