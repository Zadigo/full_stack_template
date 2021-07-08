// import { isUndefined } from 'lodash'

// var _ = require('lodash')

// function requiredKeys(payload) {
//     // Checks that all the keys are implemented
//     // in the the incoming data
//     var keys = ['item_id', 'item_name', 'price', 'item_brand', 'item_category', 'index']
//     var missingKeys = []
//     _.forEach(Object.keys(), (key) => {
//         if (!keys.includes(key)) {
//             missingKeys.append(key)
//         }
//     })
    
//     if (missingKeys.length > 0) {
//         var stringifiedMissingKeys = _.join(missingKeys, ', ')
//         console.error(`In order for your ecommerce analytics to be efficient, please implement the following missing keys ${stringifiedMissingKeys}`)
//     }
// }

// function productClick(payload, itemListName, itemListId, currency) {
//     if (isUndefined(currency)) {
//         currency = 'EUR'
//     }
//     // {
//     //     item_id: "f6be8",
//     //     item_name: "Comverges T-Shirt",
//     //     price: "33.00",
//     //     item_brand: "Comverges",
//     //     item_category: "T-Shirts",
//     //     index: "2"
//     // }
//     dataLayer.push({
//         event: 'select_item',
//         ecommerce: {
//             items: requiredKeys(payload),
//             item_list_name: itemListName,
//             item_list_id: itemListId,
//             currency: currency
//         }
//     })
// }

// function collectionView(payload) {
//     // {
//     //     item_id: "f6be8",
//     //     item_name: "Comverges T-Shirt",
//     //     price: "33.00",
//     //     item_brand: "Comverges",
//     //     item_category: "T-Shirts",
//     //     item_list_name: "shirts you may like",
//     //     index: 0
//     // }
//     dataLayer.push({
//         event: "view_item_list",
//         ecommerce: {
//             items: requiredKeys(payload),
//         }
//     })
// }

// function addToCart(payload) {

// }

// function removeFromCart(payload, value, currency) {
//     dataLayer.push({
//         event: "remove_from_cart",
//         ecommerce: {
//             currency: isUndefined(currency) ? 'EUR' : curency,
//             value: value,
//             items: requiredKeys(payload)
//         }
//     })
// }

// function cartView(payload, step) {
//     if (typeof step !== 'number') {
//         console.error('Step should be a number')
//         return false
//     } else {

//     }
// }


class Analytics {
    'use strict'

    payload = null
    currency = 'EUR'

    constructor(payload) {
        this.payload = payload
        this.datalayer = document.getElementById('datalayer')
    }

    _sendDatalayer(event, payload) {
        // Sends the Datalayer to
        // Analytics
        // dataLayer.push({
        this.datalayer.push({
            event: event,
            ecommerce: payload
        })
    }

    _createDict({ id, name, price, brand, category, index }) {
        // Creates a base product dict
        // to be used in the datalayer
        return {
            item_id: id,
            item_name: name,
            price: price,
            item_brand: brand,
            item_category: category,
            index: index
        }
    }

    simpleClick(product, itemListName, itemListId) {
        // Generate an event when the user clicks
        // on a single product element
        var baseDict = this._createDict(product)
        this._sendDatalayer(
            'select_item',
            {
                items: baseDict,
                item_list_name: itemListName,
                item_list_id: itemListId,
                currency: this.currency
            }
        )
    }
}

export default {
    install: function (Vue, options) {
        console.log(options)
        // const repositories = {
        //     click: productClick,
        //     collectionView: collectionView,
        //     addToCart: addToCart,
        //     removeFromCart: removeFromCart,
        //     cartView: cartView
        // }
        
        // Vue.prototype.$analytics = repositories
        
        Vue.prototype.$analytics = new Analytics()
    }
}
