import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

export default defineConfig(({ command }) => ({
  plugins: [svelte()],
  base: command === "serve" ? "/" : "/KBBI-SQL-database/",
}));
