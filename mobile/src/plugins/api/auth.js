export default ($axios) => ({
    getContent: () => {
        return $axios({
            method: 'get',
            url: '/'
        })
    }
})
