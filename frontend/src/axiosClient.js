var _ = require('lodash')

import axios from 'axios'
import store from './stores'
// import router from './router'

// Create a new axios instance with
// default parameters such headers with
// the token on post requests or the
// withCredentials parameter. This prevents
// from having to repeat this in each
// and every requests
var axiosClient = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1/',
    responseType: 'json',
    headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    },
    withCredentials: true
})

// var authToken = store.state.authenticationModule.token
// if (authToken) {
//     axiosClient.defaults.headers.common['Autorization'] = authToken
// }

axiosClient.interceptors.request.use(
    // Before sending any POST requests,
    // especially those that requrie
    // Authorization header, intercep and
    // inject the Authorization Token header
    // to the request.
    request => {
        // There are cases where the user might not
        // be logged in. In which case this can cause
        // an error on the request
        var token = store.state.authenticationModule.token
        if (!_.isNull(token)) {
            request.headers['Authorization'] = `Token ${token}`
        }
        return request
    },

    error => {
        return Promise.reject(error)
    }
)

axiosClient.interceptors.response.use(
    undefined,
    error => {
        // Intercept request errors and those that
        // return a 401 Unautorized will automatically
        // logout the user to prevent any issues
        return new Promise(() => {
            // if (error.response.status === 401 && error.config && !error.config.__isRetryRequest) {
            if (error.response.status === 401) {
                console.log('Axios', error.response)
                store.dispatch('authenticationModule/logout')
                window.location.reload()
            }
            throw error
        })
    }
)

export default axiosClient
