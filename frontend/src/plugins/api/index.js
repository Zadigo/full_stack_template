import authAPI from './auth'
import profileAPI from './profile'

import axiosClient from '../../axiosClient'

export default {
    install: (Vue) => {
        const repositories = {
            auth: authAPI(axiosClient),
            profile: profileAPI(axiosClient)
        }
        Vue.prototype.$api = repositories
    }
}
