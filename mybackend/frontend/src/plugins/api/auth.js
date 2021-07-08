export default ($axios) => ({
    login: (email, password) => {
        return $axios({
            method: 'post',
            url: null,
            data: {
                email: email,
                password: password
            },
            withCredentials: true
        })
    }
})
