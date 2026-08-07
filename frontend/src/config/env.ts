/**
 * Application environment configuration
 * This is the only place in the frontend that should access environment variables directly.
 */

export const env = {
  // Backend API base URL
  apiBaseUrl: process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000/api/v1",

  // Application name
  appName: process.env.NEXT_PUBLIC_APP_NAME ?? "AstraAtlas",

  // Current application version
  appVersion: process.env.NEXT_PUBLIC_APP_VERSION ?? "0.1.0",
} as const;
