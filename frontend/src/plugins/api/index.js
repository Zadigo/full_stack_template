import authAPI from './auth'
import profileAPI from './profile'
import client from '../../axiosclient'

var subscribeUser = ($axios) => {
    return (email) => {
        return $axios({
            method: 'post',
            url: '/subscribe',
            data: { email: email }
        })
    }
}

export default {
    install: (Vue) => {
        const repositories = {
            auth: authAPI(client),
            profile: profileAPI(client),
            subscribe: subscribeUser(client)
        }
        Vue.prototype.$api = repositories
    }
}
