/** @type {import('vls').VeturConfig} */
module.exports = {
    settings: {
        'vetur.useWorkspaceDependencies': true,
        'vetur.experimental.templateInterpolationService': true
    },
    projects: [
        './full_stack_website', // shorthand for only root.
        {
            root: './frontend',
            package: './package.json',
            globalComponents: [
                './src/components/**/*.vue',
            ]
        }
    ]
}
