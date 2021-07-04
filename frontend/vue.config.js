module.exports = {
    devserver: {
        proxy: {
            '^/api/': {
                target: 'http://127.0.0.1:8000/api/v1/',
                // ws: false,
            }
        }
    },
    // outputDir: './dist/',
    // assetsDir: 'static',
}
