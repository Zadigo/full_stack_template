import axios from 'axios'
import store from './stores'

// Create a new axios instance with
// default parameters such headers with
// the token on post requests or the
// withCredentials parameter. This prevents
// from having to repeat this in each
// and every requests
var axiosClient = axios.create({
    baseUrl: 'http://127.0.0.1:8000/api/v1/',
    responseType: 'json',
    headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    },
    withCredentials: true
})

axiosClient.interceptors.request.use(
    // Before sending any POST requests,
    // especially those that requrie
    // Authorization header, intercep and
    // inject the Authorization Token header
    // to the request.
    function (request) {
        if (request.method == 'post') {
            request.headers['Authorization'] = `Token ${store.state.authenticationModule.token}`
        }
        return request
    },
    function (error) {
        return Promise.reject(error)
    }
)

export default axiosClient
