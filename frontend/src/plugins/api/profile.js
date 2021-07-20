export default ($axios) => ({
    updateDetails: (data) => {
        return $axios({
            method: 'post',
            url: null,
            data: data,
        })
    },

    // Addresses

    modifyAddress: (data) => {
        return $axios({
            method: 'patch',
            url: `http://127.0.0.1:8000/api/v1/addresses/${data.id}/`,
            data: data
        })
    },

    getAddresses: () => {
        return $axios({
            method: 'get',
            url: `http://127.0.0.1:8000/api/v1/addresses/`
        })
    },

    createAddress: (data) => {
        return $axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/v1/addresses/',
            data: data
        })
    },

    removeAddress: (data) => {
        return $axios({
            method: 'delete',
            url: `http://127.0.0.1:8000/api/v1/addresses/${data.id}/`,
            data: data
        })
    }
})
