export default ($axios) => ({
    login: (email, password) => {
        return $axios({
            method: 'post',
            url: '/auth/login',
            data: { email: email, password: password },
        })
    },
    
    logout: () => {
        return $axios({
            method: 'post',
            url: '/auth/logout',
        })
    },

    signup: (credentials) => {
        return $axios({
            method: 'post',
            url: '/auth/signup',
            data: credentials,
        })
    },

    forgotPassword: (email) => {
        return $axios({
            method: 'post',
            url: '/auth/forgot-password',
            data: { email: email }
        })
    }
})
