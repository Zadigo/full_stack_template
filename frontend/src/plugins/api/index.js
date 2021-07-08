import AuthAPI from './auth'
import Axios from 'axios'

export default {
    install: (Vue) => {
        Axios.interceptors.response.use(function (response) {
            return response
        }, function (error) {
            return Promise.reject(error)
        })
        
        const repositories = {
            auth: AuthAPI(Axios)
        }
        Vue.prototype.$http = repositories
    }
}
