/**
 * plugins/webfontloader.js
 *
 * webfontloader documentation: https://github.com/typekit/webfontloader
 */

import { ref } from 'vue'

export async function loadFonts () {
    const webFontLoader = await import(/* webpackChunkName: "webfontloader" */'webfontloader')

    webFontLoader.load({
        google: {
            families: [
                // 'Roboto:100,300,400,500,700,900&display=swap',
                'Ubuntu:100,300,400,500,700,900&display=swap'
            ]
        }
    })
}

export function useMessagesPlugin ({ store }) {
    store.messages = ref([])

    function addMessage (type, message) {
        let numberOfItems = store.messages.length
        if (!numberOfItems) {
            numberOfItems = 0
        } else {
            numberOfItems = numberOfItems + 1
        }
        store.messages.push({ id: numberOfItems, type: type, message: message })
    }

    function addSuccessMessage (message) {
        addMessage('success', message)
    }
    
    function addErrorMessage (message) {
        addMessage('error', message)    
    }
    
    function addWarningMessage (message) {
        addMessage('warning', message)
    }

    function resetMessages () {
        store.messages = []
    }

    return {
        addMessage,
        addSuccessMessage,
        addErrorMessage,
        addWarningMessage,
        resetMessages
    }
}
