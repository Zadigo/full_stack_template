import authAPI from './auth'
import profileAPI from './profile'

import axiosClient from '../../axiosClient'

var subscribeUser = ($axios) => {
    return (email) => {
        return $axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/v1/subscribe',
            data: { email: email }
        })
    }
}

export default {
    install: (Vue) => {
        const repositories = {
            auth: authAPI(axiosClient),
            profile: profileAPI(axiosClient),
            subscribe: subscribeUser(axiosClient)
        }
        Vue.prototype.$api = repositories
    }
}
