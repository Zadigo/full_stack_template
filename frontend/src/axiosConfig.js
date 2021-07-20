import axios from 'axios'
import store from './store'

axios.defaults.baseUrl = 'http://127.0.0.1:8000/api/v1/'
axios.defaults.headers.post['Content-Type'] = 'application/json'
axios.defaults.headers.common['Authorization'] = store.getters.getAuthenticationHeader

axios.interceptors.request.use((config) => ({
    get: () => {
        return config
    },

    response: (request) => {
        return new Promise.reject(request)
    }
}))

export default axios
