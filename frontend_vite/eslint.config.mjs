import vue from "eslint-plugin-vue";
import typescriptEslint from "@typescript-eslint/eslint-plugin";
import parser from "vue-eslint-parser";
import path from "node:path";
import js from "@eslint/js";

import { fileURLToPath } from "node:url";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const compat = new FlatCompat({
    baseDirectory: __dirname,
    recommendedConfig: js.configs.recommended,
    allConfig: js.configs.all
});

// NOTE: Notes for eslint 9: https://eslint.org/docs/latest/use/configure/migration-guide

export default [...compat.extends(
    "eslint:recommended",
    "plugin:vue/vue3-strongly-recommended",
    "plugin:@typescript-eslint/recommended",
), {
    plugins: {
        vue,
        "@typescript-eslint": typescriptEslint,
    },

    languageOptions: {
        parser: parser,
        ecmaVersion: 2021,
        sourceType: "script",

        parserOptions: {
            parser: "@typescript-eslint/parser",
        },
    },

    rules: {
        "@typescript-eslint/no-unused-vars": ["error", {
            argsIgnorePattern: "^_",
        }],

        "brace-style": "error",
        "block-scoped-var": "error",
        "consistent-return": "warn",
        curly: "error",
        eqeqeq: "error",

        "arrow-spacing": ["error", {
            before: true,
            after: true,
        }],

        "default-case": "error",
        "default-case-last": "warn",
        "dot-notation": "error",
        "func-style": ["warn", "declaration"],
        "no-array-constructor": "error",
        "no-use-before-define": "error",
        "no-undef-init": "error",
        "no-undefined": "warn",
        "no-bitwise": "error",
        "no-eq-null": "error",
        "no-fallthrough": "error",
        "no-floating-decimal": "error",
        "no-loop-func": "error",
        "no-param-reassign": "error",
        "no-redeclare": "error",
        "no-return-assign": "error",
        "no-self-compare": "warn",
        "no-throw-literal": "error",
        "no-unneeded-ternary": "error",
        "prefer-const": "error",
        radix: "warn",
        "vars-on-top": "warn",
        yoda: "warn",
        "vue/comma-dangle": "error",
        "vue/attribute-hyphenation": "error",
        "vue/attributes-order": "warn",
        "vue/html-quotes": "warn",
        "vue/html-indent": "warn",
        "vue/order-in-components": "warn",
        "vue/require-explicit-emits": "error",
        "vue/require-prop-types": "error",
        "vue/this-in-template": "error",
        "vue/v-on-style": "warn",
        "vue/component-definition-name-casing": ["error", "PascalCase"],
        "vue/html-closing-bracket-spacing": "warn",
        "vue/block-spacing": "error",
        "vue/no-sparse-arrays": "error",
        "vue/no-useless-concat": "warn",
        "vue/object-shorthand": "warn",
        "vue/mustache-interpolation-spacing": "error",
        "vue/html-button-has-type": "warn",
        "vue/match-component-import-name": "error",
        "vue/require-emit-validator": "warn",
        "vue/v-on-function-call": "error",
        "vue/no-unused-refs": "warn",
        "vue/no-irregular-whitespace": "error",
        "vue/padding-line-between-blocks": "error",
        "vue/v-for-delimiter-style": ["error", "in"],
        "vue/prefer-separate-static-class": "error",
        "vue/no-multi-spaces": "error",
        "vue/no-template-target-blank": "error",
        "vue/no-this-in-before-route-enter": "error",
        "vue/no-unused-properties": "error",

        "vue/component-tags-order": ["error", {
            order: ["docs", ["script", "template"], "style", "i18n"],
        }],

        "vue/max-attributes-per-line": ["warn", {
            singleline: {
                max: 15,
            },
        }],

        "vue/v-bind-style": ["error", "shorthand"],
    },
}];
