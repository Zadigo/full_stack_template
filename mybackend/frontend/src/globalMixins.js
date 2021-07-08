// var _ = require('lodash')

// function buildSocials(socials) {
//     var socialsArray = []
//     _.forEach(socials, (social, index) => {
//         socialsArray.push(
//             { id: index, link: social[0], icon: social[1]}
//         )
//     })
//     console.log(socialsArray)
//     return socialsArray
// }

export default {
    data() {
        return {
            companyDetails: {
                name: 'My Website',
                domain: 'http://example.com',
                address: '4 rue de la Véga, 59000',
                email: 'google@google.com',
                telephone: '+3308797904',
                sales: {
                    validityDate: ''
                },
                availableDays: 14,
                shippingDelay: 13,
                shippingCompany: 'MyWebsite',
                returnDelay: 14,
                services: [],
                socials: [
                    { id: 1, link: '#', icon: 'fab fa-facebook-f' },
                    { id: 2, link: '#', icon: 'fab fa-twitter' },
                    { id: 3, link: '#', icon: 'fab fa-youtube' },
                    { id: 4, link: '#', icon: 'fab fa-instagram' },
                ]
                // socials: buildSocials(
                //     [
                //         ['#', 'fab-fa-facebook'],
                //         ['#', 'fab-fa-twitter'],
                //         ['#', 'fab-fa-youtube'],
                //         ['#', 'fab-fa-instagram'],
                //     ]
                // )
            }
        }
    },

    beforeMount(vm) {
        console.log(vm)
    },

    methods: {
        _validateEmail(email) {
            if (/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
                // this.msg['email'] = 'Please enter a valid email address';
                return true
            } else {
                // this.msg['email'] = '';
                return false
            }
        }
    },
    
    filters: {
        currency(value) {
            return `$${value}`
        }
    }
}
