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
    }
}
