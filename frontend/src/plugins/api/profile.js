export default ($axios) => ({
    // Profile

    updateDetails: (position, details) => {
        return $axios({
            method: 'patch',
            url: '/profile/update/personal-details',
            data: { position: position, details: details },
        })
    },

    changePassword: (userId, credentials) => {
        return $axios({
            method: 'post',
            url: `/profile/${userId}/password/change`,
            data: credentials
        })
    },

    getUserDetails: () => {
        return $axios({
            method: 'get',
            url: '/profile/'
        })
    },

    // Addresses

    modifyAddress: (data) => {
        return $axios({
            method: 'patch',
            url: `/addresses/${data.id}/`,
            data: data
        })
    },

    getAddresses: () => {
        return $axios({
            method: 'get',
            url: `/addresses/`
        })
    },

    createAddress: (data) => {
        return $axios({
            method: 'post',
            url: '/addresses/',
            data: data
        })
    },

    removeAddress: (data) => {
        return $axios({
            method: 'delete',
            url: `/addresses/${data.id}/`,
            data: data
        })
    },

    // Preferences

    updatePreferences: (data) => {
        return $axios({
            method: 'post',
            url: '/profile/update/preferences',
            data: data,
        })
    }
})
