/// <reference types="vitest" />

import { defineConfig } from 'vite'
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";

import UnheadVite from "@unhead/addons/vite";
import vue from '@vitejs/plugin-vue'
import eslint from "vite-plugin-eslint"

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const root = process.cwd()
  const env = loadEnv(mode, root)
  process.env = { ...process.env, ...env }

  return {
    root,
    resolve: {
      alias: [
        {
          find: "@",
          replacement: resolve(__dirname, "src"),
        },
        {
          find: "src",
          replacement: resolve(__dirname, 'src')
        }
      ],
    },
    plugins: [
      vue(),
      UnheadVite(),
      eslint({
        lintOnStart: true,
      }),
    ],
    test: {
      globals: true,
      environment: 'jsdom'
    }
  }
})
