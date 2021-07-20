export default ($axios) => ({
    updateDetails: (data) => {
        return $axios({
            method: 'post',
            url: null,
            data: data,
        })
    }
})
