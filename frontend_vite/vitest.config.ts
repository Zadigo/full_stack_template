import { defineConfig } from 'vitest/config'

export default defineConfig({
    test: {
        globals: true,
        environment: 'happy-dom',
        setupFiles: './tests/setupTests.ts',

        env: {
            VITE_BASE_API_DOMAIN: 'jsonplaceholder.typicode.com'
        }
    }
})
