// import vue from 'vue'

const { setupDevtoolsPlugin } = require('@vue/devtools-api')

const DEBUG = (process.env.NODE_ENV !== 'production')

// const storageSymbol = (DEBUG ? Symbol('vue-local-storage') : Symbol())

// const storageSymbol = /*#__PURE__*/ Symbol('local')

function setupDevtools(app, storage) {
    let devtoolsApi = null
    const devtools = {}

    setupDevtoolsPlugin({
        id: 'vue-local-storage',
        label: 'Vue Local Storage',
        packageName: 'vue-local-storage',
        homepage: 'http://example.com',
        componentStateTypes: ['vue-local-storage'],
        enableEarlyProxy: true,
        app
    }, api => {
        devtoolsApi = api
        devtoolsApi
        api.addInspector({
            id: 'vue-local-storage',
            label: 'Vue Local Storage',
            icon: 'storage'
        })

        api.on.getInspectorState((payload) => {
            if (payload.inspectorId === 'vue-local-storage') {
                payload.state = {
                    state: {
                        key: 'vue-local-storage',
                        value: storage.data
                    }
                }
            }
        })

        api.on.getInspectorTree((payload) => {
            if (payload.inspectorId === 'vue-local-storage') {
                payload.rootNodes = [
                    {
                        id: 'storage',
                        label: 'Storage'
                    }
                ]
            }
        })

        // api.notifyComponentUpdate('vue-local-storage')
        // api.sendInspectorTree('vue-local-storage')
        // api.sendInspectorState('vue-local-storage')
    })

    return devtools
}

class VueLocalStorage {
    constructor() {
        this.DEFAULT_KEY_NAME = 'vue_local'
        this.storage = localStorage
    }
    
    get data() {
        var result = JSON.parse(this.storage.getItem(this.DEFAULT_KEY_NAME))

        if (!result) {
            this._save({})
            return {}
        } else {
            return result
        }
    }

    _save(data) {
        // Saves an element under the global session key
        this.storage.setItem(this.DEFAULT_KEY_NAME, JSON.stringify(data))
    }

    retrieve(key) {
        return this.data[key]
    }
    
    create(key, value) {
        var storedData = this.data
        storedData[key] = value
        this._save(storedData)
    }

    remove(key) {
        var result = this.data
        delete result[key]
        this._save(result)
    }

    save(key, value) {
        this.storage.setItem(key, value)
    }

    getValue(key) {
        return this.storage.getItem(key)
    }

    install(app) {
        setupDevtools(app, this)
        // app.provide(storageSymbol, this)
        app.config.globalProperties.$localstorage = this
        app.mixin({
            data: () => ({
                localStorage: this.data
            })
        })

        if (DEBUG) {
            window.VueLocalStorage = this
        }
    }
}

function createLocalStorage () {
    return new VueLocalStorage()
}

export {
    createLocalStorage,
    VueLocalStorage
}
