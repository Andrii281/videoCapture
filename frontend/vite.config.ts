import react from "@vitejs/plugin-react";
import * as path from "path";
import { defineConfig } from "vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "~/components": path.resolve(__dirname, "src/components"),
      "~/layout": path.resolve(__dirname, "src/layout"),
      "~/pages": path.resolve(__dirname, "src/pages"),
      "~/context": path.resolve(__dirname, "src/context"),
      "~/core": path.resolve(__dirname, "src/core"),
      "~/streamApi": path.resolve(__dirname, "src/streamApi"),
      "~/utils": path.resolve(__dirname, "src/utils"),
    },
  },
});
