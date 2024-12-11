import { defineConfig } from 'vitest/config'
import { resolve } from "path";

export default defineConfig({
    test: {
        globals: true,
        environment: 'happy-dom',
        setupFiles: './tests/setupTests.ts',
        include: ['**/*.{test,spec}.{js,ts,vue}'],
        alias: [
            {
                find: "@",
                replacement: resolve(__dirname, "src"),
            }
        ],
        env: {
            VITE_BASE_API_DOMAIN: 'jsonplaceholder.typicode.com'
        }
    }
})
