export default ($axios) => ({
    login: (email, password) => {
        return $axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/v1/signin',
            data: { email: email, password: password },
        })
    },
    
    logout: () => {
        return $axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/v1/logout',
        })
    },

    signup: (credentials) => {
        return $axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/v1/signup',
            data: credentials,
        })
    }
})
