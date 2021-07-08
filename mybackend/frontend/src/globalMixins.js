import { isUndefined } from 'lodash'

var _ = require('lodash')

class Company {
    details = {
        name: 'Example Website',
        domain: 'http://example.com',
        address: '4, rue example, 75001',
        email: 'example@gmail.com',
        emails: {
            default: 'example@gmail.com',
            contact: null,
            sales: null
        },
        telephone: '+33000000',
        sales: {
            validityDate: ''
        },
        availableDays: 14,
        shippingDelay: 13,
        shippingCompany: 'Example Company',
        returnDelay: 14,
        services: [],
        socials: [
            { link: '#', icon: 'fab fa-facebook-f' },
            { link: '#', icon: 'fab fa-twitter' },
            { link: '#', icon: 'fab fa-youtube' },
            { link: '#', icon: 'fab fa-instagram' },
        ]
    }

    constructor(name, domain) {
        if (!isUndefined(name)) {
            this.details['name'] = name
        }

        if (!isUndefined(domain)) {
            this.details['domain'] = domain
        }
    }

    _setIndex(payload) {
        _.forEach(payload, (element, index) => {
            element['id'] = index
        })
    }

    setDetails() {
        this._setIndex(this.details.services)
        this._setIndex(this.details.socials)
        return this.details
    }

    addSocial(path, icon) {
        var details = this.setDetails()
        var lastSocial = _.last(details.socials)
        details.socials.push({ id: lastSocial.id + 1, path: path, icon: icon })
        this.details = details
    }
}

const companyDetails = new Company()


function pageTitle(vm) {
    const { title } = vm.$options
    if (title) {
        return typeof title === 'function' ? title.call(vm) : title
    }
}


export default {
    data() {
        return {
            companyDetails: companyDetails.setDetails(),
            currentYear: new Date().getFullYear()
        }
    },

    created() {
        // Sets the page titles
        const title = pageTitle(this)
        if (title) {
            document.title = `${title} - ${this.companyDetails.name}`
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
