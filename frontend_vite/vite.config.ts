/// <reference types="vitest" />

import { defineConfig, loadEnv } from 'vite'
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";

import UnheadVite from "@unhead/addons/vite";
import VueI18nPlugin from "@intlify/unplugin-vue-i18n/vite";
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
        lintOnStart: true
        
      }),
      VueI18nPlugin({
        include: resolve(
          dirname(fileURLToPath(import.meta.url)),
          "./src/locales/**"
        ),
        fullInstall: false,
        compositionOnly: true,
      }),
    ],
    test: {
      globals: true,
      environment: 'node'
    }
  }
})
