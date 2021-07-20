export default ($axios) => ({
    login: (email, password) => {
        return $axios({
            method: 'post',
            url: 'login',
            data: {
                email: email,
                password: password
            },
            withCredentials: true
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
            url: null,
            data: credentials,
            withCredentials: true
        })
    }
})
