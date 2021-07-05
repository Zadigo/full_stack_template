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
            }
        }
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
