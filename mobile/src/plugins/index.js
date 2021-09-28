import authApis from './api/auth'
import client from '../axiosclient'

export default {
    install: (Vue) => {
        Vue.prototype.$api = {
            auth: authApis(client)
        }
    }
}
