var usersModule = {
    state: () => ({
        users: []
    })
}



export default adminModule = {
    state: () => ({
        products: []
    }),

    modules: {
        usersModule: usersModule
    },
    
    mutations: {
        duplicateItems(state, payload) {

        },

        activateItems(state, payload) {

        },

        deactivateItems(state, payload) {

        },

        deleteItems(state, payload) {

        }
    },

    getters: {
        getPreviousItem ({ state, getters }) {
            return (moduleName, name, id) => {
                if (!_.isUndefined(moduleName)) {
                    return getters[`${moduleName}/${name}`]
                }
                return _.find(state[name], ['id', id])
            }
        },

        getNextItem ({ state, getters }) {
            return (module, name, id) => {
                return _.find(state[name], ['id', id])
            }
        }
    }
}
